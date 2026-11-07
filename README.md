<div align="center">

# 简体中文 &nbsp;|&nbsp; [English](README.en.md)

</div>

# zhouxing-ppt-skill

昼星 PPT Skill · **v1.0.0** 首次公开发布。

用十二套已确认的离线 HTML 演示主题，快速做出可编辑、可下载的中英文 PPT。

## 功能亮点

- 十二套已确认主题：SHIFT 流变、FOCUS 明晰、EDIT 精选、FORM 成形、INDEX 索引、AXIS 轴线、SKETCH 构想、GLOW 晴光、ECHO 回响、SPARK 燃点、BLEND 融合、GROVE 共生
- 每套 PPT 内置 **24 个 SVG 图标**，支持替换图标
- HTML PPT **支持编辑文字**，支持下载 **HTML**，支持下载 **PDF**
- 每套 PPT 的鼠标都按对应主题单独设计
- 中英双语模板、字体与许可文件随包提供，可离线使用

## 快速使用

把本仓库作为 Cursor / Agent 的 Skill 目录加载后，按 [SKILL.md](SKILL.md) 操作。创建工作副本示例：

```sh
python3 scripts/create_deck.py --style shift --lang zh-CN --out /absolute/path/to/new-deck
python3 scripts/build_deck.py --project /absolute/path/to/new-deck
```

主题登记见 [styles.json](styles.json)。详细约定见各 `references/*.md`。

## 主题样张

每套展示 6 张样稿（两行，每行 3 张）。完整样片见各主题目录下的 `example-zh.html` / `example-en.html`。

### [SHIFT · 流变](assets/styles/shift/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/shift/previews-zh/slide-08.png"><img src="assets/styles/shift/previews-zh/slide-08.png" alt="SHIFT p08" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/shift/previews-zh/slide-09.png"><img src="assets/styles/shift/previews-zh/slide-09.png" alt="SHIFT p09" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/shift/previews-zh/slide-07.png"><img src="assets/styles/shift/previews-zh/slide-07.png" alt="SHIFT p07" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/shift/previews-zh/slide-29.png"><img src="assets/styles/shift/previews-zh/slide-29.png" alt="SHIFT p29" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/shift/previews-zh/slide-20.png"><img src="assets/styles/shift/previews-zh/slide-20.png" alt="SHIFT p20" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/shift/previews-zh/slide-25.png"><img src="assets/styles/shift/previews-zh/slide-25.png" alt="SHIFT p25" width="32%" /></a>

### [FOCUS · 明晰](assets/styles/focus/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/focus/previews-zh/slide-01.png"><img src="assets/styles/focus/previews-zh/slide-01.png" alt="FOCUS p01" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/focus/previews-zh/slide-07.png"><img src="assets/styles/focus/previews-zh/slide-07.png" alt="FOCUS p07" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/focus/previews-zh/slide-10.png"><img src="assets/styles/focus/previews-zh/slide-10.png" alt="FOCUS p10" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/focus/previews-zh/slide-11.png"><img src="assets/styles/focus/previews-zh/slide-11.png" alt="FOCUS p11" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/focus/previews-zh/slide-23.png"><img src="assets/styles/focus/previews-zh/slide-23.png" alt="FOCUS p23" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/focus/gallery-zh/slide-30.webp"><img src="assets/styles/focus/gallery-zh/slide-30.webp" alt="FOCUS p30" width="32%" /></a>

### [EDIT · 精选](assets/styles/edit/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/edit/previews-zh/slide-03.png"><img src="assets/styles/edit/previews-zh/slide-03.png" alt="EDIT p03" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/edit/previews-zh/slide-02.png"><img src="assets/styles/edit/previews-zh/slide-02.png" alt="EDIT p02" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/edit/previews-zh/slide-08.png"><img src="assets/styles/edit/previews-zh/slide-08.png" alt="EDIT p08" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/edit/previews-zh/slide-10.png"><img src="assets/styles/edit/previews-zh/slide-10.png" alt="EDIT p10" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/edit/previews-zh/slide-12.png"><img src="assets/styles/edit/previews-zh/slide-12.png" alt="EDIT p12" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/edit/gallery-zh/slide-30.webp"><img src="assets/styles/edit/gallery-zh/slide-30.webp" alt="EDIT p30" width="32%" /></a>

### [FORM · 成形](assets/styles/form/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/form/gallery-zh/slide-01.webp"><img src="assets/styles/form/gallery-zh/slide-01.webp" alt="FORM p01" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/form/gallery-zh/slide-02.webp"><img src="assets/styles/form/gallery-zh/slide-02.webp" alt="FORM p02" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/form/gallery-zh/slide-07.webp"><img src="assets/styles/form/gallery-zh/slide-07.webp" alt="FORM p07" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/form/gallery-zh/slide-12.webp"><img src="assets/styles/form/gallery-zh/slide-12.webp" alt="FORM p12" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/form/gallery-zh/slide-13.webp"><img src="assets/styles/form/gallery-zh/slide-13.webp" alt="FORM p13" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/form/gallery-zh/slide-18.webp"><img src="assets/styles/form/gallery-zh/slide-18.webp" alt="FORM p18" width="32%" /></a>

### [INDEX · 索引](assets/styles/index/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/index/gallery-zh/slide-01.webp"><img src="assets/styles/index/gallery-zh/slide-01.webp" alt="INDEX p01" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/index/gallery-zh/slide-02.webp"><img src="assets/styles/index/gallery-zh/slide-02.webp" alt="INDEX p02" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/index/gallery-zh/slide-03.webp"><img src="assets/styles/index/gallery-zh/slide-03.webp" alt="INDEX p03" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/index/gallery-zh/slide-13.webp"><img src="assets/styles/index/gallery-zh/slide-13.webp" alt="INDEX p13" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/index/gallery-zh/slide-16.webp"><img src="assets/styles/index/gallery-zh/slide-16.webp" alt="INDEX p16" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/index/gallery-zh/slide-23.webp"><img src="assets/styles/index/gallery-zh/slide-23.webp" alt="INDEX p23" width="32%" /></a>

### [AXIS · 轴线](assets/styles/axis/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/axis/gallery-zh/slide-01.webp"><img src="assets/styles/axis/gallery-zh/slide-01.webp" alt="AXIS p01" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/axis/gallery-zh/slide-02.webp"><img src="assets/styles/axis/gallery-zh/slide-02.webp" alt="AXIS p02" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/axis/gallery-zh/slide-03.webp"><img src="assets/styles/axis/gallery-zh/slide-03.webp" alt="AXIS p03" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/axis/gallery-zh/slide-04.webp"><img src="assets/styles/axis/gallery-zh/slide-04.webp" alt="AXIS p04" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/axis/gallery-zh/slide-19.webp"><img src="assets/styles/axis/gallery-zh/slide-19.webp" alt="AXIS p19" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/axis/gallery-zh/slide-30.webp"><img src="assets/styles/axis/gallery-zh/slide-30.webp" alt="AXIS p30" width="32%" /></a>

### [SKETCH · 构想](assets/styles/sketch/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/sketch/previews-zh/slide-01.png"><img src="assets/styles/sketch/previews-zh/slide-01.png" alt="SKETCH p01" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/sketch/previews-zh/slide-02.png"><img src="assets/styles/sketch/previews-zh/slide-02.png" alt="SKETCH p02" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/sketch/previews-zh/slide-04.png"><img src="assets/styles/sketch/previews-zh/slide-04.png" alt="SKETCH p04" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/sketch/previews-zh/slide-05.png"><img src="assets/styles/sketch/previews-zh/slide-05.png" alt="SKETCH p05" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/sketch/gallery-zh/slide-11.webp"><img src="assets/styles/sketch/gallery-zh/slide-11.webp" alt="SKETCH p11" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/sketch/gallery-zh/slide-18.webp"><img src="assets/styles/sketch/gallery-zh/slide-18.webp" alt="SKETCH p18" width="32%" /></a>

### [GLOW · 晴光](assets/styles/glow/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/glow/previews-zh/slide-01.png"><img src="assets/styles/glow/previews-zh/slide-01.png" alt="GLOW p01" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/glow/previews-zh/slide-02.png"><img src="assets/styles/glow/previews-zh/slide-02.png" alt="GLOW p02" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/glow/previews-zh/slide-03.png"><img src="assets/styles/glow/previews-zh/slide-03.png" alt="GLOW p03" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/glow/previews-zh/slide-04.png"><img src="assets/styles/glow/previews-zh/slide-04.png" alt="GLOW p04" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/glow/gallery-zh/slide-13.webp"><img src="assets/styles/glow/gallery-zh/slide-13.webp" alt="GLOW p13" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/glow/gallery-zh/slide-23.webp"><img src="assets/styles/glow/gallery-zh/slide-23.webp" alt="GLOW p23" width="32%" /></a>

### [ECHO · 回响](assets/styles/echo/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/echo/previews-zh/slide-01.png"><img src="assets/styles/echo/previews-zh/slide-01.png" alt="ECHO p01" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/echo/previews-zh/slide-05.png"><img src="assets/styles/echo/previews-zh/slide-05.png" alt="ECHO p05" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/echo/previews-zh/slide-04.png"><img src="assets/styles/echo/previews-zh/slide-04.png" alt="ECHO p04" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/echo/gallery-zh/slide-13.webp"><img src="assets/styles/echo/gallery-zh/slide-13.webp" alt="ECHO p13" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/echo/gallery-zh/slide-20.webp"><img src="assets/styles/echo/gallery-zh/slide-20.webp" alt="ECHO p20" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/echo/gallery-zh/slide-30.webp"><img src="assets/styles/echo/gallery-zh/slide-30.webp" alt="ECHO p30" width="32%" /></a>

### [SPARK · 燃点](assets/styles/spark/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/spark/previews-zh/slide-01.png"><img src="assets/styles/spark/previews-zh/slide-01.png" alt="SPARK p01" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/spark/previews-zh/slide-03.png"><img src="assets/styles/spark/previews-zh/slide-03.png" alt="SPARK p03" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/spark/previews-zh/slide-04.png"><img src="assets/styles/spark/previews-zh/slide-04.png" alt="SPARK p04" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/spark/previews-zh/slide-07.png"><img src="assets/styles/spark/previews-zh/slide-07.png" alt="SPARK p07" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/spark/previews-zh/slide-08.png"><img src="assets/styles/spark/previews-zh/slide-08.png" alt="SPARK p08" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/spark/previews-zh/slide-09.png"><img src="assets/styles/spark/previews-zh/slide-09.png" alt="SPARK p09" width="32%" /></a>

### [BLEND · 融合](assets/styles/blend/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/blend/previews-zh/slide-01.png"><img src="assets/styles/blend/previews-zh/slide-01.png" alt="BLEND p01" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/blend/previews-zh/slide-07.png"><img src="assets/styles/blend/previews-zh/slide-07.png" alt="BLEND p07" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/blend/previews-zh/slide-03.png"><img src="assets/styles/blend/previews-zh/slide-03.png" alt="BLEND p03" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/blend/previews-zh/slide-04.png"><img src="assets/styles/blend/previews-zh/slide-04.png" alt="BLEND p04" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/blend/previews-zh/slide-05.png"><img src="assets/styles/blend/previews-zh/slide-05.png" alt="BLEND p05" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/blend/previews-zh/slide-09.png"><img src="assets/styles/blend/previews-zh/slide-09.png" alt="BLEND p09" width="32%" /></a>

### [GROVE · 共生](assets/styles/grove/)

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/grove/previews-zh/slide-01.png"><img src="assets/styles/grove/previews-zh/slide-01.png" alt="GROVE p01" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/grove/previews-zh/slide-04.png"><img src="assets/styles/grove/previews-zh/slide-04.png" alt="GROVE p04" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/grove/previews-zh/slide-05.png"><img src="assets/styles/grove/previews-zh/slide-05.png" alt="GROVE p05" width="32%" /></a>

<a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/grove/gallery-zh/slide-13.webp"><img src="assets/styles/grove/gallery-zh/slide-13.webp" alt="GROVE p13" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/grove/previews-zh/slide-08.png"><img src="assets/styles/grove/previews-zh/slide-08.png" alt="GROVE p08" width="32%" /></a> <a href="https://raw.githubusercontent.com/ZhouXing-AI/zhouxing-ppt-skill/main/assets/styles/grove/previews-zh/slide-09.png"><img src="assets/styles/grove/previews-zh/slide-09.png" alt="GROVE p09" width="32%" /></a>

## 许可

各主题字体、SVG 与依赖库的许可文件保留在对应 `assets/styles/<id>/` 目录（含 `fonts/`、`graphics/`、`source/` 下的 LICENSE）。请按各文件条款使用与再分发。
