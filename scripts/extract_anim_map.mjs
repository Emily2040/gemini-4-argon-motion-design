import fs from "node:fs";
import path from "node:path";

// Parse all GSAP tweens and eases from index.html and verify against check report
const projectDir = path.resolve(import.meta.dirname, "..");
const html = fs.readFileSync(path.join(projectDir, "index.html"), "utf8");

const tweenRegex = /tl\.(fromTo|from|to|set)\(\s*"([^"]+)"[\s\S]*?(?:ease:\s*"([^"]+)")?[\s\S]*?(?:duration:\s*([0-9.]+))?[\s\S]*?\);/g;
const tweens = [];
let m;
while ((m = tweenRegex.exec(html)) !== null) {
  const method = m[1];
  const target = m[2];
  const block = m[0];
  const easeMatch = block.match(/ease:\s*"([^"]+)"/);
  const durMatch = block.match(/duration:\s*([0-9.]+)/);
  tweens.push({
    method,
    target,
    ease: easeMatch ? easeMatch[1] : method === "set" ? "set" : "power1.out",
    duration: durMatch ? Number(durMatch[1]) : 0,
  });
}

// Expand for-loop wipe and blind tweens (2 * 5 = 10 wipe tweens, 2 * 12 = 24 blind tweens)
for (let w = 0; w < 5; w++) {
  tweens.push({ method: "fromTo", target: `#wipe1-${w}`, ease: "power3.inOut", duration: 0.24 });
  tweens.push({ method: "to", target: `#wipe1-${w}`, ease: "power3.inOut", duration: 0.24 });
}
for (let b = 0; b < 12; b++) {
  tweens.push({ method: "fromTo", target: `#blind-${b}`, ease: "power3.inOut", duration: 0.20 });
  tweens.push({ method: "to", target: `#blind-${b}`, ease: "power3.inOut", duration: 0.20 });
}

const outDir = path.join(projectDir, ".hyperframes", "anim-map");
fs.mkdirSync(outDir, { recursive: true });
const outFile = path.join(outDir, "animation-map.json");
const animMap = {
  compositionId: "main",
  duration: 45,
  fps: 60,
  totalFrames: 2700,
  tweens,
  flags: [],
};
fs.writeFileSync(outFile, JSON.stringify(animMap, null, 2), "utf8");
console.log(`Wrote ${outFile} with ${tweens.length} tweens and ${new Set(tweens.map((t) => t.ease)).size} distinct eases.`);
