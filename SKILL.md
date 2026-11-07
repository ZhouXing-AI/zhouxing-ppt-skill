---
name: zhouxing-ppt-skill
description: 使用昼星已确认的 SHIFT／流变、FOCUS／明晰、EDIT／精选、FORM／成形、INDEX／索引、AXIS／轴线、SKETCH／构想、GLOW／晴光、ECHO／回响、SPARK／燃点、BLEND／融合、GROVE／共生主题创建或修改中英文离线 HTML 演示，按每页内容调整排版与配图，支持文字编辑、素材替换和直接下载 PDF。适用于用户点名 zhouxing-ppt-skill、上述主题，或要求沿用已确认样式制作演示。
metadata:
  version: 1.0.0
---

# zhouxing-ppt-skill

这是用户自己的演示样式库，首次公开发布版本为 v1.0.0。十二套均已收录，登记见 [styles.json](styles.json)，按用户指定的主题选择，不必再次要求挑选风格。

| 用户所指 | 主题与内部 ID | 先读 |
|---|---|---|
| 第一套、SHIFT、流变 | **SHIFT · 流变**（`shift`） | [references/shift.md](references/shift.md) |
| 第二套、绿色主题、FOCUS、明晰 | **FOCUS · 明晰**（`focus`） | [references/focus.md](references/focus.md) |
| 第三套、红色主题、EDIT、精选、旧称 THE GOOD EDIT | **EDIT · 精选**（`edit`） | [references/edit.md](references/edit.md) |
| 第四套、蓝色浮雕主题、FORM、成形 | **FORM · 成形**（`form`） | [references/form.md](references/form.md) |
| 第五套、彩色档案主题、INDEX、索引 | **INDEX · 索引**（`index`） | [references/index.md](references/index.md) |
| 第六套、工程结构主题、AXIS、轴线 | **AXIS · 轴线**（`axis`） | [references/axis.md](references/axis.md) |
| 第七套、手稿主题、SKETCH、构想 | **SKETCH · 构想**（`sketch`） | [references/sketch.md](references/sketch.md) |
| 第八套、复古阳光主题、GLOW、晴光 | **GLOW · 晴光**（`glow`） | [references/glow.md](references/glow.md) |
| 第九套、午夜蓝玻璃主题、ECHO、回响 | **ECHO · 回响**（`echo`） | [references/echo.md](references/echo.md) |
| 第十套、荧光绿行动主题、SPARK、燃点 | **SPARK · 燃点**（`spark`） | [references/spark.md](references/spark.md) |
| 第十一套、柔润组合主题、BLEND、融合 | **BLEND · 融合**（`blend`） | [references/blend.md](references/blend.md) |
| 第十二套、植物线描主题、GROVE、共生 | **GROVE · 共生**（`grove`） | [references/grove.md](references/grove.md) |

仅说“上一套”“最终那套”时结合当前会话判断，不固定映射到第一套。主题名称与内容标题独立：例如「让灵感流动」「先看清，再行动」、`A Good Edit` 和「让想法成形」都是示例标题，新内容应另拟标题。

## 使用

1. 读取上表对应的主题参考，查看该主题 `assets/styles/<id>/preview.png` 或 `preview-zh.png`；完整样例是同目录的 `example-en.html` 与 `example-zh.html`。中文与混排还需读 [references/typography.md](references/typography.md)。十二套各有自己的 24 张 SVG 库和 `artwork-preview.png`，合计 288 张素材。上传的材料包含较多文字、表格或复杂信息时，先读 [references/content-layout.md](references/content-layout.md)。
2. 用脚本创建工作副本。十二套主题中英文样片均各 30 页，共 24 份中英文样片、720 页（中英各 360 页），用来展示主题视觉风格与布局能力；新演示按实际内容确定页数和构图。完整覆盖清单与复用方式见 [references/layout-coverage.md](references/layout-coverage.md)。路径相对于本 SKILL.md 所在目录：

   ```sh
   python3 scripts/create_deck.py --style shift --lang zh-CN --out /absolute/path/to/new-deck
   ```

   `--style` 使用已选定的主题 ID。默认按用户本次创作输入选择版本：中文或中英混排用中文版，纯英文用英文版；明确指定输出语言时优先遵循。用 `--prompt "用户输入"` 或 `--prompt-file /path/to/brief.txt` 自动识别语言，或显式传 `--lang zh-CN` / `--lang en`。`--prompt` 只选择语言，不替 Agent 写内容，也不自动选择主题。不要仅因为正在中文对话就覆盖英文创作输入。

3. 在新副本中改 `source/slides.html` 的文案/版式，按内容增删、调序页面；必要时修改工作副本的 `source/style.css` 或 `source/locale-zh.css`。修改 `deck.json` 的 title/subtitle/download_name/lang。Agent 在生成阶段逐页判断装饰 SVG 是否有助于表达；文字较多时可不配图，并为完整内容重新安排文字区、层级与留白。该判断不交给观众操作，也不是播放时自动隐藏图片。预览、实际生成、下载 HTML 和 PDF 均来自同一份成品 HTML；不另做预览专用隐藏规则。
4. 编译单文件 HTML：

   ```sh
   python3 scripts/build_deck.py --project /absolute/path/to/new-deck
   ```

5. 按 [references/player-contract.md](references/player-contract.md) 检查，打开最终 `index.html` 给用户看。文件已内嵌字体、SVG、CSS、JS和许可，不依赖联网/本地服务器。“下载 PDF”在浏览器内生成并下载高清静态 PDF，不打开打印窗口。每页以 2880×1620 画面嵌入 PDF，保留外观但不含可单独选择/编辑的文字层；不要声称是矢量或可编辑 PPTX。生成器与 MIT 许可证均内嵌，支持断网使用。

## 设计约定

- EDIT 使用暖纸白、酒红、校改红，结合纸张、红漆文具、划线批注与留白。FOCUS 使用灰纸色、翡翠绿、深绿与银黑金属雕塑。两套各自的 24 张 SVG 按本主题色彩、光照和造型设计，可用于该主题的新内容，不跨主题随意混用，也不要求每页有插图。
- EDIT 包含四列卡片与 15 种数据图表，按 [references/edit-data-layouts.md](references/edit-data-layouts.md) 选择布局与复用数据配方。图表采用纸面校样、修订对照、细红线与批注边栏；仅独立柱形可带不影响正面尺度的浅纸边，其余保持二维。语义进场只临时显现完整图形，不更改比例；保存、减少动态和 PDF 均保留静态终态。
- FOCUS 包含四列卡片与 15 种数据图表，按 [references/focus-data-layouts.md](references/focus-data-layouts.md) 选择布局和验证比例；保留衬线标题、无衬线数轴、纸灰与银绿语言，新增图表不进入装饰素材库。只有垂直柱形允许不影响读数的浅侧面，其余保持二维。
- SHIFT 来源于 Superlocal 单站拆解：点阵字、银灰/铜橙/棕黑、圆形空间对象、金属圆牌、日程细线。优先维持整套语言，而非用任意配色配任意版式。SHIFT 包含四列卡片与 15 种数据图表，按 [references/shift-data-layouts.md](references/shift-data-layouts.md) 选择并验证图形，3D 仅用于不影响读数的浅立体柱形。
- FORM 使用钴蓝、灰白、古典字形和窄缝分栏，配图是与页面同色的正视浅浮雕；24 张原创 SVG 按空间、结构、推进、平衡分组，蓝底页自动匹配同色蓝浮雕。保留贴面刻纹与浅阴影，不改成悬浮的厚重立体模型。
- INDEX 使用黑色画布、彩色档案封套和白纸内容层；粗窄标题、衬线标签与等宽索引各司其职。24 张平面 SVG 按收集、整理、连接、应用分组；采用页签、叠层和资料卡组织关系，保留不同页面的构图变化。
- AXIS 使用石墨黑、暖象牙白、工程细线和无衬线大字，配原创银灰结构 SVG；结构、方向、反馈、容量四类各六张。中文使用 Noto Sans SC 500 标题与 400 正文，英文保留 Instrument Sans 与 IBM Plex Mono。
- SKETCH 使用纸白、薄荷绿、墨黑、厚实衬线标题、细线手绘与错位纸片；24 张原创 SVG 按发现、组合、试验、行动各六张。中文标题用狮尾四季春加糖 SC Black 900，正文和界面用霞鹜文楷 GB Regular 400；英文保持 Fraunces 600/700 与 Poppins 400/500。
- GLOW 使用糖果粉、柠檬黄、奶油与可可棕，高对比复古衬线字配粗轮廓印刷徽章；24 张 SVG 按到场、相聚、玩乐、留存各六张。英文使用 DM Serif Display 400 正体/真斜体与 Poppins 400/500，中文用 Noto Serif SC 900 标题、Noto Sans SC 400 正文。
- ECHO 使用午夜蓝、雾蓝、珍珠白、细线和疏朗衬线字，配原创声学玻璃 SVG；聆听、调谐、联结、回响四类各六张。英文为 Cormorant Garamond 500 与 Instrument Sans 400/500，中文用 Noto Serif SC 300 标题、Noto Sans SC 400 正文。
- SPARK 使用荧光绿、墨黑、浅灰与深绿，大幅窄体标题配原创短挤出树脂模块；启动、塑形、试验、推进四类各六张。英文为 Barlow Condensed 800 与 Manrope 400/500，中文用得意黑真实 400 斜体标题、Noto Sans SC 400 正文，不额外斜切或压缩字形。
- BLEND 使用灰白、墨黑、紫色、蜜桃、淡紫与浅薄荷，干净几何字配光滑柔软的半透明组合物件；收集、组合、塑形、发布四类各六张。英文使用 Space Grotesk 400/500/600 与 DM Mono 400，中文为 Noto Sans SC 500 标题、400 正文。时间分配与折线样页采用准确二维度量，装饰材质不应用到数据比例。
- GROVE 使用暖奶油纸、深绿墨、翠绿、浅叶绿、浅紫与少量蓝，轻柔无衬线字配原创彩色植物线描；播种、联结、培育、共生四类各六张。英文使用 Onest 400/500 与 DM Mono 400，中文标题、正文与界面均用寒蝉半圆体 Regular 400，按字号建立层级，不合成粗体。时间分配和每周贡献样页保持准确二维比例；原站动态未完整实测，本套入场为独立设计。
- 按每页的信息结构和阅读负担选择布局与配图，不按统一字数阈值机械处理。文字较多时优先保留用户需要的信息，减少装饰并重排；关系图、数据图表和必要说明应保留。更多内容的生成规则见 [references/content-layout.md](references/content-layout.md)，不强制套用固定多文字模板。
- 中英文字体必须有明确许可，允许免费商用、嵌入和随开源 Skill 再分发；具体核实与保留声明要求见 [references/typography.md](references/typography.md)。
- 不加常驻四角品牌、日期、来源小字；需要的来源放在交付说明或用户要求的位置。
- 成品页面不展示「示例数据」「ILLUSTRATIVE DATA」「四列卡片」或图表类型等制作标签，也不把内部布局名称当作内容标题。标题表达主题或结论；理解内容所需的单位、图例与条件保留在图表或实义说明中。示例数据属性、来源与假设记录在演示元数据、数据配方或制作资料中，不通过预览 CSS 临时遮盖标签。
- 中文字体按主题选择，不统一绑定未来荧黑。SHIFT 保留已确认的未来荧黑宽体重黑（`ShiftCJK`）；FOCUS 使用 Noto Serif SC 400（`FocusCJK`）表达正文与标题，绿底描边标题用 500，短标签、界面及学习回路用 Noto Sans SC 400（`FocusCJKSans`），英文保持 Instrument Serif、真斜体与 Instrument Sans；EDIT 使用 Noto Serif SC（`EditCJK`），大标题 300、正文与界面 400，深底及红底大标题用 400，英文保留 Instrument Serif、真斜体与 Instrument Sans；FORM 使用朱雀仿宋 Regular（`FormCJK`），搭配 Marcellus 与 Instrument Sans；INDEX 中文标题使用未来荧黑 SC Compressed ExtraBold 800（`IndexCJKDisplay`）的原生窄高字形，正文与界面使用 Noto Sans SC 400，标签使用 Noto Serif SC 400，英文保留 Anton、Newsreader、IBM Plex Mono。INDEX 中文版内嵌三种完整中文字库，英文版仅内嵌西文字体。各套按中文可读性独立组织标题与层级，字体随包保留完整字库及许可；具体搭配与覆盖见排版参考。`.dot` 只放它支持的英文/数字。构建器会阻止缺字汉字和误放在点阵字中的汉字，不能忽略错误后交付。
- 十二套均保留「替换素材」。是否使用装饰配图由 Agent 在生成时逐页决定，成品不提供「纯文字」开关；文字布局随 HTML 保存与 PDF 导出保留。
- 保留共享播放器约定：固定16:9、导航点在画布内、底部操作栏、全屏保留鼠标。窗口模式为操作栏预留空间；全屏自动收起，鼠标靠近底部显示。支持滚轮向下下一页、向上上一页，避免触控板惯性连翻。
- 十二套分别内嵌铜橙游标、实心镜片、朱红笔尖、实心刻片、档案页签、精密箭头、铅笔笔尖、四角闪芒、水滴拨片、闪电楔、柔角拨片、叶尖鼠标，可见实心主体约 23 CSS px（原方案的 2/3），移动时带短拖尾，并随背景调整填充色。操作界面与文字编辑恢复系统鼠标；具体动效、回退和保存检查见播放器约定。
- 示例文案与样例数据是原创概念内容；生成用户演示时替换为用户提供或已核实的内容与数据。缺少真实数据时按用户请求制作概念示意，并在元数据与交付资料中记录假设，不把样例当作真实外部事实或数据来源。

## 新增样式

只有用户要制作/收录下一套时才新增。先形成完整可审阅样稿；确认后放入 `assets/styles/<id>/` 并登记 `styles.json`，将该套配色、字体、布局写入独立参考文件。保留现有已确认主题，不用新方向覆盖。普通演示的文案修改只在工作副本中完成，不反写 Skill 模板。
