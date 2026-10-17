<div align="center">

# Gemini 4 Argon Motion Design // 运动法则 (Principles of Motion)

### 45 秒 1080p60 六幕动态图形视觉设计作品集、实时遥测舞台与 120 BPM 立体声合成引擎

**[English](./README.md)** · **[简体中文](./README.zh-CN.md)** · **[日本語](./README.ja.md)** · **[한국어](./README.ko.md)**

*作者：**[@Iamemily2050](https://x.com/Iamemily2050)** (**[@Emily2040](https://github.com/Emily2040)**) — 在 Google Antigravity 中由 **Gemini 4 Argon** 全程主导视觉编排、确定性时间轴构建、立体声合成、形式化验证与 1080p60 渲染。*

</div>

<!-- SHOWCASE_VIDEO -->
<p align="center">
  <a href="https://github.com/Emily2040/gemini-4-argon-motion-design/releases/download/v1.0.0/principles-of-motion.mp4">
    <img src="./frames_audit/showcase-preview.webp" width="100%" alt="Principles of Motion — 45 秒 1080p60 六幕动态设计展示动态预览（点击播放或下载含 44.1 kHz 立体声音频的完整 1080p60 视频）" />
  </a>
</p>

<p align="center">
  <a href="https://github.com/Emily2040/gemini-4-argon-motion-design/releases/download/v1.0.0/principles-of-motion.mp4"><strong>▶ 点击播放 / 下载完整 45 秒 1080p60 有声视频（MP4, 16.7 MB）</strong></a>
  ·
  <a href="https://github.com/Emily2040/gemini-4-argon-motion-design/raw/HEAD/principles-of-motion.mp4">仓库内直链 1080p60 MP4</a>
  ·
  <a href="https://github.com/Emily2040/gemini-4-argon-motion-design/releases/download/v1.0.0/soundtrack.wav">44.1 kHz 无损立体声 WAV 配乐</a>
</p>

---

**Principles of Motion（运动法则）** 是一部时长精确为 `45.00` 秒（`1920×1080` 全高清、`60fps`、共 `2,700` 帧）的动态图形（Motion Graphics）视觉宣言短片。我在 Google Antigravity 中使用 **Gemini 4 Argon**，结合 HyperFrames、GSAP 3.14 以及纯 Python 标准库编写的确定性立体声合成器完成了全流程构建与双重验证。

* **1080p60 母带视频**：[`principles-of-motion.mp4`](./principles-of-motion.mp4)（`H.264` High Profile，`1920×1080`，`60/1` fps，`2,700` 帧，`45.00s`，含 `AAC` 立体声音轨）
* **交互式时间轴合成源码**：[`index.html`](./index.html)（包含 `133` 个 GSAP 补间动画、横跨 `23` 种缓动函数，并挂载 `60Hz` 逐帧物理遥测与频谱驱动回调循环）
* **程序化合成配乐（`120.0 BPM`）**：[`soundtrack.wav`](./soundtrack.wav)（`44,100 Hz`，16-bit 立体声 PCM，`45.000s`）与 [`audio-data.js`](./audio-data.js)（`2,700` 帧 × `16` 个归一化频段能量矩阵）
* **多语种单次完整复现提示词**：**[English](./prompts/en.md)** · **[简体中文](./prompts/zh-CN.md)** · **[日本語](./prompts/ja.md)** · **[한국어](./prompts/ko.md)** · **[提示词说明](./prompts/README.md)**
* **设计规范与验证档案**：[`DESIGN.md`](./DESIGN.md)、[`VERIFICATION_REPORT.md`](./VERIFICATION_REPORT.md)、[`ledger.json`](./ledger.json) 与 [`scripts/run_gates.mjs`](./scripts/run_gates.mjs)

---

## 六幕交响结构（`120.0 BPM` · 每幕精确 `7.50s` / `450` 帧）

每一幕专注呈现一项核心动态设计法则，并在画面中实时解算并展示其底层数学公式。第 I、II、III、V 幕采用深邃黑曜石暗场底色（`#090A0D`），第 IV、VI 幕则通过双叶片机械快门反转为瑞士档案级暖白纸面极性（`#F4F1EA`）。

| 幕次 | 时间与帧区间 (`60fps`) | 画布极性 | 动态设计法则与实时屏幕遥测 | 1080p 静态关键帧 (`1920×1080`) |
| :--- | :--- | :--- | :--- | :--- |
| **01** | `0.00s – 7.50s` (`0001 – 0450`) | 黑曜石暗场 (`#090A0D`) | **惯性与冲量 (Inertia & Impulse)**：在相空间位移轨迹图上同屏对比 `expo.out` 弹道减速、`elastic.out(1.1, 0.35)` 弹簧欠阻尼过冲，以及 `steps(6)` 离散采样量化。 | ![Act I](./frames_audit/act1_2.5s.png) |
| **02** | `7.50s – 15.00s` (`0451 – 0900`) | 黑曜石暗场 (`#090A0D`) | **视差与 Z 轴空间 (Parallax & Z-Space)**：在 `1250px` 透视 CSS 3D 舞台中排布五层空间深度平面（从 `L05` `Z = -200px` / `0.68×` 至 `L01` `Z = +200px` / `1.42×`），由三轴欧拉云台实时旋转解算。 | ![Act II](./frames_audit/act2_10.5s.png) |
| **03** | `15.00s – 22.50s` (`0901 – 1350`) | 黑曜石暗场 (`#090A0D`) | **动态遥测 (Telemetry in Motion)**：三条程序化生成的 Catmull-Rom 连续样条轨迹、实时收缩的 `±2σ` 置信区间走廊、`+4.82σ` 峰值异常锁定准星，以及等宽数字（`tabular-nums`）KPI 跳动仪表。 | ![Act III](./frames_audit/act3_18.5s.png) |
| **04** | `22.50s – 30.00s` (`1351 – 1800`) | 档案纸浅场 (`#F4F1EA`) | **矢量形态学 (Vector Morphology)**：双叶片快门切入高对比纸面极性，呈现碳黑墨水（`#0B0C10`）、国际主义朱红（`#B01204`）与群青钴蓝（`#0033B8`）的反向旋转构成主义转子与黄金分割（`1.618`）动态卡尺。 | ![Act IV](./frames_audit/act4_25.5s.png) |
| **05** | `30.00s – 37.50s` (`1801 – 2250`) | 黑曜石暗场 (`#090A0D`) | **声学共振 (Acoustic Resonance)**：以 `16.67ms`（`60Hz`）步进读取 16 频段预提取声学能量矩阵，同步驱动同心谐波圆环与 `120.0 BPM` 下的 3:4 利萨如（Lissajous）相位锁定曲线。 | ![Act V](./frames_audit/act5_33.5s.png) |
| **06** | `37.50s – 45.00s` (`2251 – 2700`) | 档案纸浅场 (`#F4F1EA`) | **交响综合 (Symphonic Synthesis)**：将全部五项动态设计法则汇聚于五列瑞士网格展厅与实时微型视口中，在帧计数器锁定 `2700 / 2700` 后，于 `44.20s – 45.00s` 平滑收束至纯黑尾帧。 | ![Act VI](./frames_audit/act6_41.0s.png) |

---

## 本地复现构建与自动化验证门禁

### 1. 合成 45 秒立体声配乐与 60fps 频谱矩阵

```bash
python scripts/generate_soundtrack.py
```

该脚本仅依赖 Python 标准库（`math`、`wave`、`struct`、`json`），一次性生成 `soundtrack.wav`（`44.1kHz`，16-bit 立体声 PCM，`45.000s`）以及供前端逐帧读取的 `audio-data.js`（`2,700` 帧 × 每帧 `16` 个归一化频段）。

### 2. 运行静态分析、运行时无错、布局边界与 WCAG AA 对比度门禁

```bash
npx hyperframes check --strict --samples 18 --at 1.5,3.8,6.5,9.0,12.5,16.5,20.0,24.0,27.5,31.5,35.0,39.0,42.5,44.0
```

* **静态与运行时检查 (Lint & Runtime)**：`0` 错误，`0` 警告
* **布局边界检查 (Layout Bounds)**：跨越 `14` 个关键采样时间戳实现 `0` 裁切、`0` 溢出
* **无障碍对比度 (Contrast)**：全部 `140/140` 个文本节点 100% 通过 WCAG AA 标准

### 3. 渲染 1080p60 成片并运行六项确定性验证门禁

```bash
npx hyperframes render --output principles-of-motion.mp4 --fps 60 --quality high
node scripts/extract_anim_map.mjs
node scripts/run_gates.mjs
```

`scripts/run_gates.mjs` 会依次独立校验：WAV 音频头与非静音振幅（`G1`）、`2,700` 帧 `AUDIO_DATA` 矩阵完整性（`G2`）、HTML 时间确定性与等宽字体规范（`G3`）、`133` 个补间与 `23` 种缓动曲线的动画图谱（`G4`）、`principles-of-motion.mp4` 的 `ffprobe` 音视频流参数（`G5`），以及注入故障自检（`G6`）。

---

## 作者与署名

* **创作者与发布者**：**[@Iamemily2050](https://x.com/Iamemily2050)** (**[@Emily2040](https://github.com/Emily2040)**)
* **AI 导演与工程实现**：在 Google Antigravity 中由 **Gemini 4 Argon** 驱动构建
