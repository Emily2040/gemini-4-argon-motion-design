# DESIGN.md — PRINCIPLES OF MOTION (45.00s Studio Showcase Reel)

## Style Prompt

**Swiss-Telemetry Kinetic Manifesto** (Josef Müller-Brockmann × GMUNK × Kyle Cooper). A mathematically locked 120 BPM (45.00s / 2,700 frames at 60fps) studio reel structured into 6 distinct acts, each proving a core discipline of motion design while exposing its live mathematical machinery on canvas. The visual language alternates between a deep obsidian dark-room telemetry canvas (`#090A0D`) and an archival Swiss paper canvas (`#F4F1EA`) via intentional polarity inversions. Every scene pairs monumental industrial condensed typography (`Big Shoulders Display` at 80–180px, weight 900 vs 300) with mainframe-grade tabular telemetry (`IBM Plex Mono` at 18–24px) and selective editorial counter-tension (`Instrument Serif` Italic). No element appears statically; every entrance, camera depth shift, SVG vector morph, and audio-reactive pulse is governed by explicit physical easing curves and verified for zero layout collision and full WCAG AA contrast.

## Colors

### Dark Polarity (Acts I, II, III, V)
- **Obsidian Canvas (`#090A0D`)**: Primary dark background surface (radial depth vignette `#12151F` → `#090A0D`, avoiding flat `#000000` and H.264 linear gradient banding).
- **Elevated Telemetry Panel (`#131722`)**: Secondary structural card surface with `1px solid #262C3D` hairline grid rules.
- **Titanium White (`#F7F6F2`)**: Primary headline and hero vector stroke on dark canvas (18.4:1 contrast vs `#090A0D`).
- **Telemetry Silver (`#A3ADC2`)**: Secondary technical labels and coordinate readouts on dark canvas (8.4:1 contrast vs `#090A0D`).
- **Acid Volt (`#D4FF00`)**: High-velocity vector trace, spring curve, and active beat indicator on dark canvas (16.2:1 contrast vs `#090A0D`).
- **Signal Vermilion (`#FF4D38`)**: Primary focal alert, playhead marker, and kinetic accent on dark canvas (5.7:1 contrast vs `#090A0D`).

### Light Polarity (Acts IV, VI)
- **Archival Paper Canvas (`#F4F1EA`)**: Primary light background surface for high-impact polarity inversions.
- **Warm Stone Panel (`#E6E1D6`)**: Secondary structural grid surface with `1px solid #C8C2B4` architectural rules.
- **Carbon Ink (`#0B0C10`)**: Primary monumental display type and structural geometry on light canvas (17.6:1 contrast vs `#F4F1EA`).
- **Archival Graphite (`#3E4350`)**: Secondary technical annotations and axis labels on light canvas (8.6:1 contrast vs `#F4F1EA`).
- **International Crimson (`#C81908`)**: High-contrast focal vector and kinetic highlight on light canvas (6.1:1 contrast vs `#F4F1EA`).
- **Cobalt Telemetry (`#0038CC`)**: Secondary mathematical curve and vector accent on light canvas (8.2:1 contrast vs `#F4F1EA`).

## Typography

- **Primary Display (`Big Shoulders Display`)**: Weights `900` (Black) and `300` (Light). Used for 72px–176px monumental act titles, kinetic slabs, and structural numerals. Tight tracking (`-0.03em` to `-0.04em`), `line-height: 0.92`.
- **Technical Telemetry (`IBM Plex Mono`)**: Weights `400` and `600`. Used for 18px–26px frame counters (`0000 / 2700`), cubic-bezier matrices, velocity vectors, and data callouts. Always set `font-variant-numeric: tabular-nums; font-variant-ligatures: none;`.
- **Counter-Voice Accent (`Instrument Serif`)**: Weight `400 Italic`. Used sparingly for single-word human counter-tension against mechanical precision.
- **Minimum Sizes**: Headlines `64px+`, body/subtitles `22px+`, data/telemetry labels `18px+` (never below `16px`).

## 6-Act Narrative & Choreographic Architecture (45.00s / 120 BPM)

1. **ACT I (0.00s – 7.50s) · 01 / INERTIA & IMPULSE (Kinetic Typography & Easing Physics)**
   - Dark polarity (`#090A0D`). Proves how easing shapes mass and emotion: `expo.out` ballistic arrival vs `elastic.out(1.1, 0.35)` spring oscillation vs `steps(6)` mechanical quantize, plotted live on a real-time SVG cubic-bezier & spring phase-space graph with frame-synced playheads.
2. **ACT II (7.50s – 15.00s) · 02 / PARALLAX & Z-SPACE (3D Spatial Depth & Camera Rigging)**
   - Dark polarity (`#090A0D`). A multi-plane CSS 3D architectural stage (`perspective: 1200px`, `rotationX`, `rotationY`, `z` depth layers from `-320px` to `+180px`) with orbital camera rigging, live frustum reticle, and depth-of-field parallax planes that assemble into a spatial lens tunnel.
3. **ACT III (15.00s – 22.50s) · 03 / TELEMETRY IN MOTION (Procedural Data & Live Signal Choreography)**
   - Dark polarity (`#090A0D`). High-density live observatory: 3-stream procedural trajectory spline curves (`strokeDashoffset`), synchronized tabular counters (`tabular-nums`), confidence bands, and anomaly lock-on markers updating deterministically at 60fps.
4. **ACT IV (22.50s – 30.00s) · 04 / VECTOR MORPHOLOGY (Polarity Inversion & Geometric Transformation)**
   - **Hard Polarity Inversion** via mechanical shutter/iris into Archival Paper (`#F4F1EA`). Inspired by Josef Müller-Brockmann and Saul Bass: razor-sharp SVG geometric primitives, golden-ratio construction grids, rotating bauhaus arcs, and morphing vector aperture blades in Carbon Ink (`#0B0C10`) and International Crimson (`#C81908`).
5. **ACT V (30.00s – 37.50s) · 05 / ACOUSTIC RESONANCE (120 BPM Frame-Synced Audio-Reactive Choreography)**
   - Dark polarity (`#090A0D`). Driven by per-frame pre-extracted `AUDIO_DATA` from our bespoke 120 BPM stereo soundtrack: concentric harmonic phase rings, Lissajous ratio readouts, and kinetic typographic slabs that respond deterministically to sub-bass (`bands[0]`), mid transients (`bands[4]`), and high-frequency foley (`bands[10]`) without cliché equalizer bars.
6. **ACT VI (37.50s – 45.00s) · 06 / SYMPHONIC SYNTHESIS (Multi-Discipline Finale & Precision Resolve)**
   - Archival Paper (`#F4F1EA`) architectural bento grid synthesizing all five disciplines simultaneously — kinetic type, 3D spatial gimbal, live telemetry spline, geometric vector rotor, and acoustic phase lock — culminating in a decisive 120 BPM final lock (`FRAME 2700 / 2700 · Δt = 0.00ms`) and a controlled final fade to obsidian black (`44.20s – 45.00s`).

## What NOT to Do

1. **No banned fonts** (`Inter`, `Roboto`, `Syne`, `Poppins`, `Outfit`, `Sora`, `Playfair Display`, etc.).
2. **No exit animations before scene transitions** — outgoing scenes remain 100% populated and alive while the transition executes; only Act VI (final scene) fades out at `44.2s–45.0s`.
3. **No cliché audio visualizers** — no generic vertical EQ bar graphs, musical notes, or floating neon orbs.
4. **No `Math.random()` or async timeline construction** — every particle, waveform sample, and counter uses a seeded PRNG (`mulberry32`) and synchronous `window.__timelines` registration.
5. **No low-contrast labels or overflowing containers** — every text element must pass `npx hyperframes validate` (WCAG AA) and `npx hyperframes inspect` with zero unintended overflows.
