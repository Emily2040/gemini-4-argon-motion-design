# Single-Shot Build Prompt (English)

**[English](./en.md)** · **[简体中文](./zh-CN.md)** · **[日本語](./ja.md)** · **[한국어](./ko.md)** · **[Back to Main README](../README.md)**

```markdown
Build and verify a 45.00-second Full HD (`1920×1080` at `60fps`, `2,700` frames) motion graphics studio showcase reel titled "Principles of Motion" using HyperFrames, GSAP 3.14, and a deterministic Python stereo synthesiser (`120.0 BPM`).

1. Six-Act Architecture (`7.50s` / `450` frames per act at `60fps`):
   - Act I (`0.00s–7.50s`, Dark Obsidian `#090A0D`): Inertia & Impulse — compare `expo.out`, `elastic.out(1.1, 0.35)`, and `steps(6)` on a live phase-space displacement plot.
   - Act II (`7.50s–15.00s`, Dark Obsidian `#090A0D`): Parallax & Z-Space — 5 stepped spatial planes (`L05` at `Z=-200px` / `0.68×` through `L01` at `Z=+200px` / `1.42×`) inside a `1250px` CSS 3D stage driven by a 3-axis Euler gimbal.
   - Act III (`15.00s–22.50s`, Dark Obsidian `#090A0D`): Telemetry in Motion — 3 procedural Catmull-Rom trajectory splines, `±2σ` confidence corridor, `+4.82σ` anomaly reticle lock, and `tabular-nums` KPI counters.
   - Act IV (`22.50s–30.00s`, Archival Paper `#F4F1EA`): Vector Morphology — dual-blade shutter polarity inversion into carbon ink (`#0B0C10`), crimson (`#B01204`), and cobalt (`#0033B8`) constructivist rotors and golden-ratio (`1.618`) calipers.
   - Act V (`30.00s–37.50s`, Dark Obsidian `#090A0D`): Acoustic Resonance — sample 16 pre-extracted frequency bands per `16.67ms` (`60Hz`) frame from `AUDIO_DATA` to drive concentric harmonic rings and a 3:4 Lissajous phase lock at `120.0 BPM`.
   - Act VI (`37.50s–45.00s`, Archival Paper `#F4F1EA`): Symphonic Synthesis — unify all 5 disciplines in a 5-column exhibition grid with live mini-viewports, lock the frame counter at `2700 / 2700`, and fade cleanly to black at `44.20s–45.00s`.

2. Deterministic Audio & Verification Gates:
   - Write `scripts/generate_soundtrack.py` using only the Python standard library to synthesize `soundtrack.wav` (`44.1kHz`, 16-bit stereo PCM, `45.000s`) and `audio-data.js` (`2,700` frames × `16` normalized bands).
   - Ensure zero `Math.random()`, `Date.now()`, or `requestAnimationFrame` calls in `index.html`; drive all motion from the HyperFrames timeline clock and GSAP tweens.
   - Pass `npx hyperframes check --strict` with 0 lint/runtime errors, 0 layout overflows, and 100% WCAG AA contrast compliance, then render `principles-of-motion.mp4` at `1920×1080`, `60fps` (`2,700` frames) and verify with `scripts/run_gates.mjs`.
```
