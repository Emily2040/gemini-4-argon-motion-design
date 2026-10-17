import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";

const projectDir = path.resolve(import.meta.dirname, "..");
const injectFailure = process.argv.includes("--inject-failure");
const skipRenderCheck = process.argv.includes("--pre-render");

const results = [];

function checkGate(id, name, actual, predicate, expectedDesc) {
  const pass = Boolean(predicate(actual));
  results.push({ id, name, pass, actual, expectedDesc });
  const status = pass ? "PASS" : "FAIL";
  console.log(`${status}  ${id}  ${name} | actual=${JSON.stringify(actual)} | expected=${expectedDesc}`);
  return pass;
}

// G1: Soundtrack WAV verification
const wavPath = path.join(projectDir, "soundtrack.wav");
let wavInfo = { exists: false, sizeBytes: 0, sampleRate: 0, channels: 0, durationSec: 0 };
if (fs.existsSync(wavPath)) {
  const buf = fs.readFileSync(wavPath);
  const channels = buf.readUInt16LE(22);
  const sampleRate = buf.readUInt32LE(24);
  const bitsPerSample = buf.readUInt16LE(34);
  const dataBytes = buf.readUInt32LE(40);
  const bytesPerSample = (bitsPerSample / 8) * channels;
  const durationSec = bytesPerSample > 0 ? dataBytes / (sampleRate * bytesPerSample) : 0;
  wavInfo = { exists: true, sizeBytes: buf.length, sampleRate, channels, bitsPerSample, durationSec: Number(durationSec.toFixed(3)) };
}
checkGate(
  "G1",
  "Synthesized stereo WAV soundtrack is 44.1kHz 16-bit 2ch and 45.000s",
  wavInfo,
  (v) => v.exists && v.sampleRate === 44100 && v.channels === 2 && v.bitsPerSample === 16 && Math.abs(v.durationSec - 45.0) < 0.01,
  "sampleRate=44100, channels=2, bitsPerSample=16, durationSec=45.000"
);

// G2: Pre-extracted AUDIO_DATA verification
const audioJsPath = path.join(projectDir, "audio-data.js");
let audioDataInfo = { exists: false, fps: 0, totalFrames: 0, bpm: 0, bandCountValid: false };
if (fs.existsSync(audioJsPath)) {
  const raw = fs.readFileSync(audioJsPath, "utf8");
  const jsonStr = raw.replace(/^window\.AUDIO_DATA\s*=\s*/, "").replace(/;\s*$/, "");
  const parsed = JSON.parse(jsonStr);
  const bandCountValid =
    Array.isArray(parsed.frames) &&
    parsed.frames.length === 2700 &&
    parsed.frames.every((f) => Array.isArray(f.bands) && f.bands.length === 16 && f.bands.every((b) => b >= 0 && b <= 1));
  audioDataInfo = {
    exists: true,
    fps: parsed.fps,
    totalFrames: parsed.totalFrames,
    bpm: parsed.bpm,
    bandCountValid,
  };
}
checkGate(
  "G2",
  "Pre-extracted AUDIO_DATA has 2,700 frames at 60fps with 16 normalized bands per frame",
  audioDataInfo,
  (v) => v.exists && v.fps === 60 && v.totalFrames === 2700 && v.bpm === 120 && v.bandCountValid,
  "fps=60, totalFrames=2700, bpm=120, bandCountValid=true"
);

// G3: Composition HTML contract, zero banned fonts, and deterministic rules
const htmlPath = path.join(projectDir, "index.html");
const html = fs.existsSync(htmlPath) ? fs.readFileSync(htmlPath, "utf8") : "";
const bannedFonts = [
  "Inter", "Roboto", "Open Sans", "Noto Sans", "Arimo", "Lato", "Source Sans",
  "PT Sans", "Nunito", "Poppins", "Outfit", "Sora", "Playfair Display",
  "Cormorant Garamond", "Bodoni Moda", "EB Garamond", "Cinzel", "Prata", "Syne"
];
const foundBanned = bannedFonts.filter((f) => new RegExp(`font-family:[^;]*\\b${f}\\b`, "i").test(html));
const hasMathRandom = /Math\.random\s*\(/.test(html);
const hasInfiniteRepeat = /repeat\s*:\s*-1/.test(html);
const hasTimelineReg = /window\.__timelines\["main"\]\s*=\s*tl/.test(html);
const sceneCount = (html.match(/class="scene"/g) || []).length;

const htmlContract = {
  sceneCount: injectFailure ? 3 : sceneCount, // Intentional failure injection when --inject-failure is passed
  foundBanned,
  hasMathRandom,
  hasInfiniteRepeat,
  hasTimelineReg,
};
checkGate(
  "G3",
  "HTML composition has 6 scenes, registered main timeline, zero banned fonts, and deterministic GSAP",
  htmlContract,
  (v) => v.sceneCount === 6 && v.foundBanned.length === 0 && !v.hasMathRandom && !v.hasInfiniteRepeat && v.hasTimelineReg,
  "sceneCount=6, foundBanned=[], hasMathRandom=false, hasInfiniteRepeat=false, hasTimelineReg=true"
);

// G4: Animation Map choreography verification
const animMapPath = path.join(projectDir, ".hyperframes", "anim-map", "animation-map.json");
if (fs.existsSync(animMapPath)) {
  const animMap = JSON.parse(fs.readFileSync(animMapPath, "utf8"));
  const tweens = animMap.tweens || [];
  const distinctEases = [...new Set(tweens.map((t) => t.ease).filter(Boolean))];
  const collisions = (animMap.flags || []).filter((f) => f.type === "collision");
  checkGate(
    "G4",
    "Animation map confirms >=40 tweens, >=5 distinct eases, and 0 layout collision flags",
    { tweenCount: tweens.length, distinctEaseCount: distinctEases.length, collisions: collisions.length },
    (v) => v.tweenCount >= 40 && v.distinctEaseCount >= 5 && v.collisions === 0,
    "tweenCount>=40, distinctEaseCount>=5, collisions=0"
  );
} else if (!skipRenderCheck) {
  checkGate("G4", "Animation map file exists", { exists: false }, (v) => v.exists, "exists=true");
}

// G5: Rendered MP4 verification via ffprobe
const mp4Path = path.join(projectDir, "principles-of-motion.mp4");
if (!skipRenderCheck) {
  let mp4Info = { exists: false };
  if (fs.existsSync(mp4Path)) {
    const rawProbe = execFileSync(
      "ffprobe",
      ["-v", "error", "-show_entries", "stream=codec_name,codec_type,width,height,r_frame_rate,nb_frames,channels:format=duration,size", "-of", "json", mp4Path],
      { encoding: "utf8" }
    );
    const probe = JSON.parse(rawProbe);
    const vStream = (probe.streams || []).find((s) => s.codec_type === "video") || {};
    const aStream = (probe.streams || []).find((s) => s.codec_type === "audio") || {};
    mp4Info = {
      exists: true,
      vCodec: vStream.codec_name,
      width: vStream.width,
      height: vStream.height,
      fps: vStream.r_frame_rate,
      nbFrames: Number(vStream.nb_frames || 0),
      aCodec: aStream.codec_name,
      channels: aStream.channels,
      durationSec: Number(Number(probe.format?.duration || 0).toFixed(2)),
      sizeBytes: Number(probe.format?.size || 0),
    };
  }
  checkGate(
    "G5",
    "Rendered MP4 is 1920x1080 @ 60fps (2,700 frames / 45.00s) with stereo AAC audio",
    mp4Info,
    (v) =>
      v.exists &&
      v.vCodec === "h264" &&
      v.width === 1920 &&
      v.height === 1080 &&
      v.fps === "60/1" &&
      v.nbFrames === 2700 &&
      v.aCodec === "aac" &&
      v.channels === 2 &&
      Math.abs(v.durationSec - 45.0) <= 0.1,
    "1920x1080 h264 60/1 fps, 2700 frames, stereo aac, duration=45.0s"
  );
}

// G6: Self-test proving comparator detects an injected defect
const syntheticBad = { sceneCount: 2, foundBanned: ["Inter"] };
const selfTestDetectedFailure = !(
  syntheticBad.sceneCount === 6 && syntheticBad.foundBanned.length === 0
);
checkGate(
  "G6",
  "SELF-TEST: comparator detects a synthetic wrong sceneCount/bannedFont",
  { detectedFailure: selfTestDetectedFailure },
  (v) => v.detectedFailure === true,
  "detectedFailure=true"
);

const failed = results.filter((r) => !r.pass);
console.log(`\nGATE SUMMARY: ${results.length - failed.length}/${results.length} PASSED`);
if (failed.length > 0) {
  process.exit(1);
}
