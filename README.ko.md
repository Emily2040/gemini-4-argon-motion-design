<div align="center">

# Gemini 4 Argon Motion Design // Principles of Motion

### 45초 1080p60 6막 모션 그래픽 쇼케이스 릴, 실시간 텔레메트리 스테이지 & 120 BPM 스테레오 신시사이저

**[English](./README.md)** · **[简体中文](./README.zh-CN.md)** · **[日本語](./README.ja.md)** · **[한국어](./README.ko.md)**

*제작 및 공개: **[@Iamemily2050](https://x.com/Iamemily2050)** (**[@Emily2040](https://github.com/Emily2040)**) — Google Antigravity 환경에서 **Gemini 4 Argon**이 모션 디렉팅, 결정론적 타임라인 설계, 스테레오 사운드 합성, 정합성 검증 및 1080p60 영상 렌더링까지 전 과정을 엔드투엔드로 구현.*

</div>

<!-- SHOWCASE_VIDEO -->
<p align="center">
  <a href="https://github.com/Emily2040/gemini-4-argon-motion-design/releases/download/v1.0.0/principles-of-motion.mp4">
    <img src="./frames_audit/showcase-preview.webp" width="100%" alt="Principles of Motion — 45초 1080p60 6막 모션 그래픽 쇼케이스 프리뷰 (클릭하여 44.1 kHz 스테레오 오디오가 포함된 1080p60 전체 영상 재생 및 다운로드)" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/Emily2040/gemini-4-argon-motion-design/releases/download/v1.0.0/principles-of-motion.mp4"><strong>▶ 45초 1080p60 Full HD 전체 영상(스테레오 오디오 포함) 재생 및 다운로드 (MP4, 16.7 MB)</strong></a>
  ·
  <a href="https://github.com/Emily2040/gemini-4-argon-motion-design/raw/HEAD/principles-of-motion.mp4">리포지토리 원본 1080p60 MP4</a>
  ·
  <a href="https://github.com/Emily2040/gemini-4-argon-motion-design/releases/download/v1.0.0/soundtrack.wav">44.1 kHz 스테레오 WAV 사운드트랙</a>
</p>

---

**Principles of Motion(운동의 원리)**은 정확히 `45.00`초(`1920×1080` Full HD, `60fps`, 총 `2,700` 프레임) 동안 펼쳐지는 모션 그래픽 스튜디오 쇼케이스 릴입니다. Google Antigravity의 **Gemini 4 Argon**을 통해 HyperFrames, GSAP 3.14, 그리고 순수 Python 표준 라이브러리로 작성된 결정론적 스테레오 신시사이저를 결합하여 제작 및 검증했습니다.

* **마스터 영상 (`1080p60`)**: [`principles-of-motion.mp4`](./principles-of-motion.mp4) (`H.264` High Profile, `1920×1080`, `60/1` fps, `2,700` 프레임, `45.00s`, 스테레오 `AAC` 오디오)
* **인터랙티브 타임라인 컴포지션**: [`index.html`](./index.html) (`23`종 이징 곡선에 걸친 `133`개 GSAP 트윈 및 `60Hz` 프레임 단위 실시간 텔레메트리·오디오 리액티브 콜백 루프 탑재)
* **프로시저럴 합성 사운드트랙 (`120.0 BPM`)**: [`soundtrack.wav`](./soundtrack.wav) (`44,100 Hz`, 16-bit 스테레오 PCM, `45.000s`) 및 [`audio-data.js`](./audio-data.js) (`2,700` 프레임 × `16`개 정규화 주파수 대역 행렬)
* **4개 국어 원클릭 제작 프롬프트**: **[English](./prompts/en.md)** · **[简体中文](./prompts/zh-CN.md)** · **[日本語](./prompts/ja.md)** · **[한국어](./prompts/ko.md)** · **[프롬프트 가이드](./prompts/README.md)**
* **설계 사양 및 검증 보고서**: [`DESIGN.md`](./DESIGN.md), [`VERIFICATION_REPORT.md`](./VERIFICATION_REPORT.md), [`ledger.json`](./ledger.json), [`scripts/run_gates.mjs`](./scripts/run_gates.mjs)

---

## 6막 구성 (`120.0 BPM` · 각 막 `7.50s` / `450` 프레임)

각 막은 하나의 핵심 모션 디자인 원리를 다루며, 장면을 구동하는 수학적 방정식과 물리 텔레메트리를 화면에 실시간으로 표시합니다. 제 I, II, III, V 막은 깊은 옵시디언 다크 표면(`#090A0D`) 위에서 구동되고, 제 IV, VI 막은 듀얼 블레이드 셔터를 통해 스위스 아카이벌 페이퍼 명암 극성(`#F4F1EA`)으로 반전됩니다.

| 막 (Act) | 시간 및 프레임 구간 (`60fps`) | 캔버스 극성 | 모션 디자인 원리 및 실시간 온스크린 텔레메트리 | 1080p 스틸 프레임 (`1920×1080`) |
| :--- | :--- | :--- | :--- | :--- |
| **01** | `0.00s – 7.50s` (`0001 – 0450`) | 다크 옵시디언 (`#090A0D`) | **관성과 충격량 (Inertia & Impulse)**: 위상 공간 변위 플롯 위에서 `expo.out` 탄도 감속, `elastic.out(1.1, 0.35)` 스프링 오버슈트, `steps(6)` 이산 양자화 궤적을 동시에 비교합니다. | ![Act I](./frames_audit/act1_2.5s.png) |
| **02** | `7.50s – 15.00s` (`0451 – 0900`) | 다크 옵시디언 (`#090A0D`) | **패럴랙스와 Z-공간 (Parallax & Z-Space)**: `1250px` 원근 CSS 3D 스테이지 내부에 5개의 공간 깊이 평면(`L05` `Z = -200px` / `0.68×`부터 `L01` `Z = +200px` / `1.42×`까지)을 배치하고 3축 오일러 짐벌로 회전시킵니다. | ![Act II](./frames_audit/act2_10.5s.png) |
| **03** | `15.00s – 22.50s` (`0901 – 1350`) | 다크 옵시디언 (`#090A0D`) | **모션 텔레메트리 (Telemetry in Motion)**: 3개의 절차적 Catmull-Rom 스플라인 궤적, 실시간 `±2σ` 신뢰 구간 코리도, 이상치 조준선 락온(`+4.82σ`), 고정폭 숫자(`tabular-nums`) KPI 카운터를 구동합니다. | ![Act III](./frames_audit/act3_18.5s.png) |
| **04** | `22.50s – 30.00s` (`1351 – 1800`) | 아카이벌 페이퍼 (`#F4F1EA`) | **벡터 형태학 (Vector Morphology)**: 듀얼 블레이드 셔터로 명암 극성을 반전시켜 카본 잉크(`#0B0C10`), 크림슨(`#B01204`), 코발트(`#0033B8`) 색상의 상호 역회전 구축주의 로터와 황금비(`1.618`) 캘리퍼를 전개합니다. | ![Act IV](./frames_audit/act4_25.5s.png) |
| **05** | `30.00s – 37.50s` (`1801 – 2250`) | 다크 옵시디언 (`#090A0D`) | **음향 공명 (Acoustic Resonance)**: `16.67ms`(`60Hz`) 프레임마다 사전 추출된 16개 주파수 대역 에너지를 샘플링하여 동심 배음 링과 `120.0 BPM`에 동기화된 3:4 리사주(Lissajous) 위상 잠금 곡선을 구동합니다. | ![Act V](./frames_audit/act5_33.5s.png) |
| **06** | `37.50s – 45.00s` (`2251 – 2700`) | 아카이벌 페이퍼 (`#F4F1EA`) | **교향적 통합 (Symphonic Synthesis)**: 앞선 다섯 가지 모션 원리를 5열 스위스 그리드 전시관과 실시간 미니 뷰포트로 통합하며, 프레임 카운터가 `2700 / 2700`에 도달한 뒤 `44.20s – 45.00s` 구간에서 블랙으로 페이드아웃됩니다. | ![Act VI](./frames_audit/act6_41.0s.png) |

---

## 빌드 및 검증 스위트 재현 방법

### 1. 스테레오 사운드트랙 및 60fps 오디오 매트릭스 합성

```bash
python scripts/generate_soundtrack.py
```

Python 표준 라이브러리(`math`, `wave`, `struct`, `json`)만을 사용하여 `soundtrack.wav`(`44.1kHz`, 16-bit 스테레오 PCM, `45.000s`)와 `audio-data.js`(`2,700` 프레임 × 프레임당 `16`개 정규화 주파수 대역 배열)를 생성합니다.

### 2. 정적 분석, 런타임, 레이아웃 경계 및 WCAG AA 명암비 검증

```bash
npx hyperframes check --strict --samples 18 --at 1.5,3.8,6.5,9.0,12.5,16.5,20.0,24.0,27.5,31.5,35.0,39.0,42.5,44.0
```

* **Lint & Runtime**: 오류 `0`건, 경고 `0`건
* **Layout Bounds**: `14`개 샘플 타임스탬프 전 구간에서 클리핑 및 오버플로 `0`건
* **Contrast**: 전체 `140/140`개 텍스트 요소 WCAG AA 기준 통과

### 3. 1080p 60fps 영상 렌더링 및 6단계 자동 검증 게이트 실행

```bash
npx hyperframes render --output principles-of-motion.mp4 --fps 60 --quality high
node scripts/extract_anim_map.mjs
node scripts/run_gates.mjs
```

`scripts/run_gates.mjs`는 WAV 헤더 및 비무음 진폭(`G1`), `2,700` 프레임 `AUDIO_DATA` 배열(`G2`), HTML 결정론성 및 폰트 규칙(`G3`), `133`개 트윈 / `23`종 이징 애니메이션 맵(`G4`), `principles-of-motion.mp4`의 `ffprobe` 스트림 속성(`G5`), 그리고 결함 주입 자체 테스트(`G6`)를 검증합니다.

---

## 제작자 및 크레딧

* **제작 및 공개**: **[@Iamemily2050](https://x.com/Iamemily2050)** (**[@Emily2040](https://github.com/Emily2040)**)
* **AI 디렉션 및 엔지니어링**: Google Antigravity 환경에서 **Gemini 4 Argon**으로 구현
