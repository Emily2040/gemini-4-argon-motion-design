#!/usr/bin/env python3
"""
Deterministic 45.00s (2,700 frames @ 60fps, 120 BPM) Stereo Soundtrack & AUDIO_DATA Generator
for "PRINCIPLES OF MOTION".
Uses pure Python standard library (math, wave, struct, json) for 100% reproducibility.
"""

import json
import math
import os
import struct
import wave

SAMPLE_RATE = 44100
DURATION = 45.0
TOTAL_SAMPLES = int(SAMPLE_RATE * DURATION)
FPS = 60
TOTAL_FRAMES = int(DURATION * FPS)  # 2700 frames
BPM = 120.0
BEAT_SEC = 60.0 / BPM  # 0.50s per beat


def clamp(val, lo=-1.0, hi=1.0):
    return max(lo, min(hi, val))


def env_adsr(t, attack, decay, sustain_level, release, total_dur):
    if t < 0.0 or t >= total_dur:
        return 0.0
    if t < attack:
        return t / max(attack, 1e-6)
    t_dec = t - attack
    if t_dec < decay:
        return 1.0 - (1.0 - sustain_level) * (t_dec / max(decay, 1e-6))
    t_rel = t - (total_dur - release)
    if t_rel > 0.0:
        return sustain_level * (1.0 - t_rel / max(release, 1e-6))
    return sustain_level


def kick_drum(t_rel):
    """Punchy architectural sub-kick with pitch drop."""
    if t_rel < 0.0 or t_rel > 0.38:
        return 0.0
    # Instant frequency drop from 150Hz to 46Hz
    freq = 46.0 + 110.0 * math.exp(-t_rel * 38.0)
    phase = 2.0 * math.pi * (46.0 * t_rel + (110.0 / 38.0) * (1.0 - math.exp(-t_rel * 38.0)))
    amp = math.exp(-t_rel * 9.5)
    click = 0.35 * math.exp(-t_rel * 180.0) * math.sin(2.0 * math.pi * 1200.0 * t_rel)
    return (math.sin(phase) * 0.85 + click) * amp


def rim_tick(t_rel, pitch=1800.0, decay=65.0):
    """Crisp mechanical UI / clock transient."""
    if t_rel < 0.0 or t_rel > 0.09:
        return 0.0
    env = math.exp(-t_rel * decay)
    body = math.sin(2.0 * math.pi * pitch * t_rel) + 0.5 * math.sin(2.0 * math.pi * (pitch * 2.41) * t_rel)
    return body * env * 0.35


def snare_hit(t_rel):
    """Deterministic tonal + pseudo-noise backbeat snare."""
    if t_rel < 0.0 or t_rel > 0.24:
        return 0.0
    tonal = math.sin(2.0 * math.pi * 185.0 * t_rel) * math.exp(-t_rel * 24.0)
    # Deterministic high-frequency hash for crisp snare wires
    noise = math.sin(t_rel * 43758.5453) * math.cos(t_rel * 19283.11)
    wires = noise * math.exp(-t_rel * 18.0)
    return (tonal * 0.55 + wires * 0.55) * 0.65


def riser_sweep(t, t_start, t_end, f0=120.0, f1=1400.0):
    """Transition riser leading into scene handoffs."""
    if t < t_start or t > t_end:
        return 0.0
    p = (t - t_start) / (t_end - t_start)
    freq = f0 + (f1 - f0) * (p * p)
    amp = math.sin(p * math.pi) * (0.25 + 0.35 * p)
    return math.sin(2.0 * math.pi * freq * (t - t_start)) * amp


def generate_audio(out_wav_path, out_js_path):
    os.makedirs(os.path.dirname(out_wav_path) or ".", exist_ok=True)

    # Pre-schedule bespoke cue events (time, type, pitch, pan)
    cues = []

    # Act I (0.0 - 7.5s): Easing physics cues
    cues.append((0.15, "impact", 55.0, 0.0))
    # Expo.out laser sweep at 1.20s
    for i in range(12):
        cues.append((1.20 + i * 0.035, "tick", 900.0 + i * 140.0, -0.4 + i * 0.07))
    # Elastic.out spring bounces at 2.30s
    spring_offsets = [0.0, 0.14, 0.27, 0.39, 0.50, 0.60, 0.69]
    for idx, off in enumerate(spring_offsets):
        cues.append((2.30 + off, "tick", 1320.0 - idx * 90.0, 0.35 * ((-1) ** idx)))
    # Steps(6) quantized arpeggio at 3.40s
    for idx in range(6):
        cues.append((3.40 + idx * 0.12, "tick", 660.0 + idx * 220.0, -0.3 + idx * 0.12))
    # Staggered 5-block wipe at 7.10s
    for idx in range(5):
        cues.append((7.10 + idx * 0.04, "tick", 1100.0 + idx * 180.0, -0.5 + idx * 0.25))

    # Act II (7.5 - 15.0s): 5 spatial depth cards lock in
    for idx in range(5):
        cues.append((7.85 + idx * 0.25, "tick", 880.0 + idx * 110.0, -0.4 + idx * 0.2))
    cues.append((14.75, "impact", 48.0, 0.0))

    # Act III (15.0 - 22.5s): Telemetry spline pings & anomaly lock
    for idx in range(14):
        cues.append((15.50 + idx * 0.35, "tick", 1760.0 if idx % 2 == 0 else 1320.0, 0.3 * math.sin(idx)))
    # Anomaly lock-on triple beep at 19.0s
    for idx in range(3):
        cues.append((19.00 + idx * 0.11, "tick", 2637.0, 0.2))
    # Mechanical shutter slam at 22.35s
    cues.append((22.35, "impact", 42.0, 0.0))
    cues.append((22.35, "snare", 220.0, 0.0))

    # Act IV (22.5 - 30.0s): Vector Morphology geometric snaps
    for idx in range(14):
        cues.append((23.00 + idx * 0.50, "tick", 987.77 + (idx % 4) * 246.94, 0.4 * math.cos(idx)))
    cues.append((29.85, "impact", 52.0, 0.0))

    # Act V (30.0 - 37.5s): Acoustic Resonance 120 BPM syncopated accents
    for idx in range(15):
        bt = 30.0 + idx * 0.50
        cues.append((bt, "kick_boost", 55.0, 0.0))
        if idx % 2 == 1:
            cues.append((bt, "snare", 190.0, 0.0))
        cues.append((bt + 0.25, "tick", 2093.0, 0.35 * ((-1) ** idx)))
    # 12-strip blind cascade at 37.10s
    for idx in range(12):
        cues.append((37.10 + idx * 0.018, "tick", 800.0 + idx * 120.0, -0.6 + idx * 0.1))

    # Act VI (37.5 - 45.0s): Symphonic Synthesis culmination
    for idx in range(5):
        cues.append((37.80 + idx * 0.22, "tick", 1108.73 + idx * 220.0, -0.4 + idx * 0.2))
    cues.append((43.50, "impact", 55.0, 0.0))

    # Transition risers before each boundary
    riser_windows = [
        (6.80, 7.35, 140.0, 960.0),
        (14.30, 14.90, 110.0, 1200.0),
        (21.80, 22.35, 160.0, 1400.0),
        (29.30, 29.90, 180.0, 1100.0),
        (36.80, 37.35, 150.0, 1500.0),
    ]

    # Index cues by integer start sample for fast lookup
    cue_buckets = {}
    for c_time, c_type, c_pitch, c_pan in cues:
        b_idx = int(c_time * 10.0)  # 0.1s buckets
        for k in range(b_idx - 1, b_idx + 6):
            cue_buckets.setdefault(k, []).append((c_time, c_type, c_pitch, c_pan))

    pcm_bytes = bytearray(TOTAL_SAMPLES * 4)

    # Per-frame band accumulators (1350 frames x 16 bands)
    frames_data = []
    samples_per_frame = SAMPLE_RATE // FPS  # 1470 samples per frame

    for f_idx in range(TOTAL_FRAMES):
        s_start = f_idx * samples_per_frame
        s_end = min(TOTAL_SAMPLES, s_start + samples_per_frame)

        sub_energy = 0.0
        low_energy = 0.0
        mid_energy = 0.0
        high_energy = 0.0
        rms_acc = 0.0

        for s in range(s_start, s_end):
            t = s / SAMPLE_RATE
            beat_pos = (t / BEAT_SEC) % 1.0
            t_in_beat = t % BEAT_SEC
            sixteenth_pos = (t / (BEAT_SEC * 0.25)) % 1.0
            t_in_sixteenth = t % (BEAT_SEC * 0.25)

            # Master fade-in (0.0 - 0.15s) and final fade-out (44.15s - 45.00s)
            master_gain = 1.0
            if t < 0.12:
                master_gain = t / 0.12
            elif t > 44.15:
                master_gain = max(0.0, 1.0 - (t - 44.15) / 0.85)

            # 1. Global 120 BPM pulse (kick on every 0.5s beat up to 43.5s)
            sub_sig = 0.0
            if t < 43.6:
                # Lighter kick in Act IV (paper act), stronger in Act I, II, III, V, VI
                kick_scale = 0.55 if (22.5 <= t < 30.0) else (0.95 if (30.0 <= t < 37.5) else 0.75)
                sub_sig += kick_drum(t_in_beat) * kick_scale

            # 2. 16th-note precision clock pulse
            high_sig = 0.0
            if t < 43.5:
                hat_amp = 0.18 if sixteenth_pos < 0.5 else 0.09
                if t_in_sixteenth < 0.035:
                    high_sig += math.sin(2.0 * math.pi * 6400.0 * t_in_sixteenth) * math.exp(-t_in_sixteenth * 140.0) * hat_amp

            # 3. Act-specific harmonic pads and basslines
            low_sig = 0.0
            mid_sig = 0.0
            stereo_spread = 0.0

            if t < 7.5:
                # Act I: Dark obsidian drone + tension fifth (A1=55Hz, E2=82.41Hz, B2=123.47Hz)
                low_sig += 0.22 * math.sin(2.0 * math.pi * 55.0 * t)
                mid_sig += 0.14 * math.sin(2.0 * math.pi * 82.41 * t) + 0.10 * math.sin(2.0 * math.pi * 123.47 * t)
                stereo_spread = 0.08 * math.sin(2.0 * math.pi * 0.5 * t)
            elif t < 15.0:
                # Act II: 3D Parallax warm minor-9th chord (A1, E2, G2=98Hz, B2=123.47Hz, C3=130.81Hz)
                low_sig += 0.25 * math.sin(2.0 * math.pi * 55.0 * t + 0.3 * math.sin(2.0 * math.pi * 2.0 * t))
                mid_sig += (
                    0.13 * math.sin(2.0 * math.pi * 98.0 * t)
                    + 0.12 * math.sin(2.0 * math.pi * 123.47 * t)
                    + 0.11 * math.sin(2.0 * math.pi * 164.81 * t)
                )
                stereo_spread = 0.16 * math.sin(2.0 * math.pi * 0.8 * t)
            elif t < 22.5:
                # Act III: Telemetry driving sequence (D2=73.42Hz, A2=110Hz, F3=174.61Hz, A3=220Hz)
                arp_freqs = [146.83, 220.0, 293.66, 349.23]
                step_idx = int(t / 0.125) % 4
                arp_f = arp_freqs[step_idx]
                low_sig += 0.26 * math.sin(2.0 * math.pi * 73.42 * t)
                mid_sig += 0.18 * math.sin(2.0 * math.pi * arp_f * t) * math.exp(-t_in_sixteenth * 18.0)
                stereo_spread = 0.12 * math.cos(2.0 * math.pi * 1.5 * t)
            elif t < 30.0:
                # Act IV: Archival Paper Bauhaus harmonic intervals (F2=87.31Hz, C3=130.81Hz, E3=164.81Hz, A3=220Hz)
                low_sig += 0.20 * math.sin(2.0 * math.pi * 87.31 * t)
                mid_sig += (
                    0.15 * math.sin(2.0 * math.pi * 130.81 * t)
                    + 0.14 * math.sin(2.0 * math.pi * 164.81 * t)
                    + 0.12 * math.sin(2.0 * math.pi * 220.0 * t)
                )
                stereo_spread = 0.14 * math.sin(2.0 * math.pi * 1.0 * t)
            elif t < 37.5:
                # Act V: Acoustic Resonance — dynamic bass progression + harmonic bell pulse
                prog = [55.0, 43.65, 49.0, 65.41][int((t - 30.0) / 2.0) % 4]
                sub_env = 0.55 + 0.45 * math.cos(2.0 * math.pi * 2.0 * t)
                sub_sig += 0.34 * math.sin(2.0 * math.pi * prog * t) * sub_env
                low_sig += 0.22 * math.sin(2.0 * math.pi * (prog * 2.0) * t)
                mid_sig += 0.20 * math.sin(2.0 * math.pi * (prog * 3.0) * t) * math.exp(-t_in_beat * 5.0)
                high_sig += 0.14 * math.sin(2.0 * math.pi * (prog * 8.0) * t) * math.exp(-t_in_beat * 9.0)
                stereo_spread = 0.20 * math.sin(2.0 * math.pi * 2.0 * t)
            else:
                # Act VI: Symphonic Synthesis — Radiant A-major-add9 architectural resolution
                # (A1=55, E2=82.41, A2=110, C#3=138.59, E3=164.81, B3=246.94, E4=329.63)
                chord_swell = min(1.0, (t - 37.5) / 1.5)
                low_sig += 0.26 * math.sin(2.0 * math.pi * 55.0 * t) * chord_swell
                mid_sig += (
                    0.14 * math.sin(2.0 * math.pi * 110.0 * t)
                    + 0.13 * math.sin(2.0 * math.pi * 138.59 * t)
                    + 0.13 * math.sin(2.0 * math.pi * 164.81 * t)
                    + 0.11 * math.sin(2.0 * math.pi * 246.94 * t)
                ) * chord_swell
                high_sig += 0.08 * math.sin(2.0 * math.pi * 329.63 * t) * chord_swell
                stereo_spread = 0.15 * math.sin(2.0 * math.pi * 0.75 * t)

            # 4. Evaluate scheduled discrete cues in this 0.1s bucket
            bucket = cue_buckets.get(int(t * 10.0), [])
            pan_offset = 0.0
            for c_time, c_type, c_pitch, c_pan in bucket:
                dt = t - c_time
                if dt < 0.0 or dt > 0.45:
                    continue
                if c_type == "tick":
                    val = rim_tick(dt, pitch=c_pitch, decay=60.0)
                    high_sig += val
                    pan_offset += val * c_pan
                elif c_type == "snare":
                    val = snare_hit(dt)
                    mid_sig += val * 0.6
                    high_sig += val * 0.5
                elif c_type == "impact":
                    val = kick_drum(dt) * 0.9
                    sub_sig += val
                elif c_type == "kick_boost":
                    val = kick_drum(dt) * 0.45
                    sub_sig += val

            # 5. Evaluate transition risers
            for r_s, r_e, f0, f1 in riser_windows:
                if r_s <= t <= r_e:
                    r_val = riser_sweep(t, r_s, r_e, f0, f1)
                    mid_sig += r_val * 0.6
                    high_sig += r_val * 0.4

            mono = (sub_sig + low_sig + mid_sig + high_sig) * master_gain
            left = clamp(mono + (stereo_spread + pan_offset) * master_gain, -0.96, 0.96)
            right = clamp(mono - (stereo_spread + pan_offset) * master_gain, -0.96, 0.96)

            l_int = int(left * 32767.0)
            r_int = int(right * 32767.0)
            struct.pack_into("<hh", pcm_bytes, s * 4, l_int, r_int)

            # Accumulate band energies for AUDIO_DATA
            sub_energy += abs(sub_sig) * master_gain
            low_energy += abs(low_sig) * master_gain
            mid_energy += abs(mid_sig) * master_gain
            high_energy += abs(high_sig) * master_gain
            rms_acc += mono * mono

        n_s = max(1, s_end - s_start)
        sub_norm = min(1.0, (sub_energy / n_s) * 2.8)
        low_norm = min(1.0, (low_energy / n_s) * 3.2)
        mid_norm = min(1.0, (mid_energy / n_s) * 3.0)
        high_norm = min(1.0, (high_energy / n_s) * 4.2)
        rms_val = min(1.0, math.sqrt(rms_acc / n_s) * 2.2)

        # Interpolate 16 frequency bands (0 = deepest sub-bass, 15 = highest treble)
        bands = []
        for b in range(16):
            if b < 4:
                p = b / 3.0
                val = sub_norm * (1.0 - p * 0.4) + low_norm * (p * 0.4)
            elif b < 8:
                p = (b - 4) / 3.0
                val = low_norm * (1.0 - p) + mid_norm * p
            elif b < 12:
                p = (b - 8) / 3.0
                val = mid_norm * (1.0 - p) + high_norm * p
            else:
                p = (b - 12) / 3.0
                val = high_norm * (1.0 - p * 0.35)
            bands.append(round(clamp(val, 0.0, 1.0), 4))

        frames_data.append({
            "bands": bands,
            "rms": round(rms_val, 4)
        })

    with wave.open(out_wav_path, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(pcm_bytes)

    audio_data_obj = {
        "fps": FPS,
        "totalFrames": TOTAL_FRAMES,
        "bpm": BPM,
        "frames": frames_data,
    }
    with open(out_js_path, "w", encoding="utf-8") as jf:
        jf.write("window.AUDIO_DATA = ")
        json.dump(audio_data_obj, jf, separators=(",", ":"))
        jf.write(";\n")

    print(f"Generated {out_wav_path} ({os.path.getsize(out_wav_path)} bytes, {DURATION}s)")
    print(f"Generated {out_js_path} ({len(frames_data)} frames @ {FPS}fps)")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    wav_path = os.path.join(base_dir, "soundtrack.wav")
    js_path = os.path.join(base_dir, "audio-data.js")
    generate_audio(wav_path, js_path)
