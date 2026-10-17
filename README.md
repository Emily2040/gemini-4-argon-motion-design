# Gemini 4 Argon Motion Design: Principles of Motion (1080p60)

**Principles of Motion** is a 45.00-second (`1920×1080` at `60fps`, `2,700` frames) motion graphics studio reel. I built and verified it with Gemini 4 Argon in Google Antigravity using HyperFrames, GSAP 3.14, and a deterministic Python stereo synthesiser.

* **Master Video (`1080p60`)**: [`principles-of-motion.mp4`](./principles-of-motion.mp4) (`H.264` High Profile, `1920×1080`, `60/1` fps, `2,700` frames, `45.00s`, stereo `AAC` audio)
* **Interactive Composition**: [`index.html`](./index.html) (`133` GSAP tweens across `23` easing curves, plus a `60Hz` per-frame telemetry and audio-reactive callback loop)
* **Synthesised Score (`120.0 BPM`)**: [`soundtrack.wav`](./soundtrack.wav) (`44,100 Hz`, 16-bit stereo PCM, `45.000s`) and [`audio-data.js`](./audio-data.js) (`2,700` frames × `16` normalised frequency bands)
* **Design & Verification Records**: [`DESIGN.md`](./DESIGN.md), [`VERIFICATION_REPORT.md`](./VERIFICATION_REPORT.md), [`ledger.json`](./ledger.json), and [`scripts/run_gates.mjs`](./scripts/run_gates.mjs)

---

## Six-Act Structure (`120.0 BPM` · `7.50s` / `450` Frames per Act)

Every act tests one motion discipline. Each scene shows its live maths. Acts I, II, III, and V run on a dark obsidian surface (`#090A0D`); Acts IV and VI invert canvas polarity onto archival paper (`#F4F1EA`).

| Act | Time & Frame Window | Surface Polarity | Discipline & On-Screen Telemetry | Still Frame (`1920×1080`) |
| :--- | :--- | :--- | :--- | :--- |
| **01** | `0.00s – 7.50s` (`0001 – 0450`) | Dark Obsidian (`#090A0D`) | **Inertia & Impulse**: Compares `expo.out` ballistic deceleration, `elastic.out(1.1, 0.35)` spring overshoot, and `steps(6)` quantization on a phase-space displacement plot. | ![Act I](./frames_audit/act1_2.5s.png) |
| **02** | `7.50s – 15.00s` (`0451 – 0900`) | Dark Obsidian (`#090A0D`) | **Parallax & Z-Space**: Five spatial planes (`L05` at `Z = -200px` / `0.68×` through `L01` at `Z = +200px` / `1.42×`) inside a `1250px` CSS 3D stage rotated by a 3-axis Euler gimbal. | ![Act II](./frames_audit/act2_10.5s.png) |
| **03** | `15.00s – 22.50s` (`0901 – 1350`) | Dark Obsidian (`#090A0D`) | **Telemetry in Motion**: Three procedural Catmull-Rom trajectory splines with a `±2σ` confidence corridor, an anomaly reticle lock (`+4.82σ`), and `tabular-nums` KPI counters. | ![Act III](./frames_audit/act3_18.5s.png) |
| **04** | `22.50s – 30.00s` (`1351 – 1800`) | Archival Paper (`#F4F1EA`) | **Vector Morphology**: Dual-blade shutter polarity inversion into carbon ink (`#0B0C10`), crimson (`#B01204`), and cobalt (`#0033B8`) counter-rotating constructivist rotors and golden-ratio (`1.618`) calipers. | ![Act IV](./frames_audit/act4_25.5s.png) |
| **05** | `30.00s – 37.50s` (`1801 – 2250`) | Dark Obsidian (`#090A0D`) | **Acoustic Resonance**: Samples 16 pre-extracted frequency bands per `16.67ms` frame to drive concentric harmonic rings and a 3:4 Lissajous phase lock at `120.0 BPM`. | ![Act V](./frames_audit/act5_33.5s.png) |
| **06** | `37.50s – 45.00s` (`2251 – 2700`) | Archival Paper (`#F4F1EA`) | **Symphonic Synthesis**: Unifies all five disciplines in a five-column exhibition grid with live mini-viewports, locking at `2700 / 2700` before resolving to black at `44.20s – 45.00s`. | ![Act VI](./frames_audit/act6_41.0s.png) |

---

## Reproducing the Build and Verification Suite

### 1. Synthesize the Stereo Score and 60fps Audio Matrix

```bash
python scripts/generate_soundtrack.py
```

This script uses only the Python standard library (`math`, `wave`, `struct`, `json`) to generate `soundtrack.wav` (`44.1kHz`, 16-bit stereo, `45.000s`) and `audio-data.js` (`2,700` frames at `60fps`, `16` normalized bands per frame).

### 2. Run Static, Runtime, Layout, and WCAG AA Contrast Checks

```bash
npx hyperframes check --strict --samples 18 --at 1.5,3.8,6.5,9.0,12.5,16.5,20.0,24.0,27.5,31.5,35.0,39.0,42.5,44.0
```

* **Lint & Runtime**: `0` errors, `0` warnings
* **Layout Bounds**: `0` clipping or overflow issues across `14` timestamp samples
* **Contrast**: `140/140` text elements pass WCAG AA

### 3. Render the 1080p 60fps Video and Run the Gate Suite

```bash
npx hyperframes render --output principles-of-motion.mp4 --fps 60 --quality high
node scripts/extract_anim_map.mjs
node scripts/run_gates.mjs
```

`scripts/run_gates.mjs` checks the WAV header (`G1`), the 2,700-frame `AUDIO_DATA` array (`G2`), HTML determinism and font rules (`G3`), the 133-tween / 23-ease animation map (`G4`), the `ffprobe` stream properties of `principles-of-motion.mp4` (`G5`), and a failure-injection self-test (`G6`).
