# 单次复制版完整创作提示词 (简体中文)

**[English](./en.md)** · **[简体中文](./zh-CN.md)** · **[日本語](./ja.md)** · **[한국어](./ko.md)** · **[返回主 README](../README.zh-CN.md)**

```markdown
使用 HyperFrames、GSAP 3.14 以及基于纯 Python 标准库的确定性立体声合成器（`120.0 BPM`），构建并验证一部时长精确为 45.00 秒的全高清（`1920×1080`、`60fps`、共 `2,700` 帧）动态图形视觉设计作品集短片《Principles of Motion（运动法则）》。

1. 六幕交响结构（`60fps` 下每幕精确为 `7.50s` / `450` 帧）：
   - 第一幕（`0.00s–7.50s`，黑曜石暗场 `#090A0D`）：惯性与冲量 (Inertia & Impulse) — 在实时相空间位移轨迹图上同屏对比 `expo.out` 弹道减速、`elastic.out(1.1, 0.35)` 弹簧欠阻尼过冲，以及 `steps(6)` 离散采样量化。
   - 第二幕（`7.50s–15.00s`，黑曜石暗场 `#090A0D`）：视差与 Z 轴空间 (Parallax & Z-Space) — 在 `1250px` 透视 CSS 3D 舞台中排布 5 层空间深度平面（从 `L05` `Z=-200px` / `0.68×` 至 `L01` `Z=+200px` / `1.42×`），由三轴欧拉云台实时驱动旋转。
   - 第三幕（`15.00s–22.50s`，黑曜石暗场 `#090A0D`）：动态遥测 (Telemetry in Motion) — 绘制 3 条程序化 Catmull-Rom 连续样条轨迹、实时 `±2σ` 置信区间走廊、`+4.82σ` 峰值异常锁定准星，以及等宽数字（`tabular-nums`）KPI 跳动仪表。
   - 第四幕（`22.50s–30.00s`，档案纸浅场 `#F4F1EA`）：矢量形态学 (Vector Morphology) — 通过双叶片机械快门反转为纸面极性，呈现碳黑墨水（`#0B0C10`）、朱红（`#B01204`）与群青钴蓝（`#0033B8`）反向旋转构成主义转子及黄金分割（`1.618`）动态卡尺。
   - 第五幕（`30.00s–37.50s`，黑曜石暗场 `#090A0D`）：声学共振 (Acoustic Resonance) — 以 `16.67ms`（`60Hz`）步进从 `AUDIO_DATA` 读取 16 频段能量矩阵，同步驱动同心谐波圆环与 `120.0 BPM` 下的 3:4 利萨如（Lissajous）相位锁定曲线。
   - 第六幕（`37.50s–45.00s`，档案纸浅场 `#F4F1EA`）：交响综合 (Symphonic Synthesis) — 将全部五项动态设计法则汇聚于五列瑞士网格展厅与实时微型视口中，帧计数器锁定 `2700 / 2700`，并于 `44.20s–45.00s` 平滑收束至纯黑尾帧。

2. 确定性音频合成与六道自动化验证门禁：
   - 编写仅依赖 Python 标准库的 `scripts/generate_soundtrack.py`，生成 `soundtrack.wav`（`44.1kHz`，16-bit 立体声 PCM，`45.000s`）与 `audio-data.js`（`2,700` 帧 × `16` 个归一化频段）。
   - 确保 `index.html` 中零 `Math.random()`、`Date.now()` 或 `requestAnimationFrame` 调用，所有动画严格由 HyperFrames 时间轴时钟与 GSAP 补间驱动。
   - 通过 `npx hyperframes check --strict`（0 静态与运行时错误、0 布局溢出裁切、100% 通过 WCAG AA 对比度），随后渲染 `1920×1080` `60fps`（`2,700` 帧）的 `principles-of-motion.mp4`，并通过 `scripts/run_gates.mjs` 全部六道门禁测试。
```
