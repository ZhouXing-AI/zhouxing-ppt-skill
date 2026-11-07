# INDEX · 索引

用户于 2026-11-06 确认的第五套主题，内部 ID `index`，主题版本 `1.0.0`。用户说「第五套」「INDEX」「索引」「彩色档案」时选择本主题。`Ideas, In Order.` 和「让想法有迹可循」是中英文示例标题，新稿按用户内容另拟标题。

## 创建与文件

先查看 `assets/styles/index/preview.png`、`preview-zh.png` 和 `artwork-preview.png`；完整样例为同目录的 `example-en.html` 与 `example-zh.html`。

```sh
python3 scripts/create_deck.py --style index --prompt "做一份关于知识整理的演示" --out /absolute/path/to/new-deck
```

中文或混排输入默认中文，纯英文输入默认英文；明确指定输出语言时用 `--lang zh-CN` 或 `--lang en`。脚本创建三十页样例副本，随后按内容修改 `source/slides.html`、`deck.json` 并增删、调序页面，再运行 `build_deck.py`。三十页样例包含原有风格布局和新增信息布局，页数并不固定。

- 构建器读取完整的 `source/style.css`；不要仅拼接 `theme.css` 与 `player-shared.css` 覆盖它，否则会丢失 `palette-ui.css` 的页签导航和播放器配色。
- 中文排版在共享源目录的 `source/locale-zh.css`，规则仅作用于 `html:lang(zh)`。中文文案、元数据和双语菜单在 `locales/zh-CN/`；创建中文副本时覆盖 `source/slides.html`、`source/ui.json`，并以 locale 的完整 `fonts` 数组覆盖英文配置。
- 英文 `source/ui.json` 只含英文，英文 HTML 只内嵌西文字体；中文 HTML 同时内嵌标题、正文、标签三种完整中文字库。不要只改英文副本的 `lang` 或菜单语言便交付中文，应使用中文 locale 的文案、排版、菜单和字体配置。
- `source/artwork.css`、`artwork.js`、`artwork.html` 提供素材选择器；资源及双语名称、分类和关键词在 `graphics/catalog.json`。字体、图库、播放器和 PDF 依赖均嵌入单文件 HTML，离线可用。

## 视觉与排版

- 固定 1920×1080，黑色外部空间和内容黑底 `#191919`，外部留边 `#0d0d0d`；资料纸 `#fdfaf7`。蓝 `#1e4bd7`、绿 `#0c7866`、紫 `#581e70`、黄 `#ffe927` 分别组织收集、整理、连接、应用，红 `#d71e1e` 用于问题与检验。多色用于索引总览、封面和结尾，中间页围绕一个主色展开。
- 核心语言是彩色封套、圆滑肩部的档案页签、浅色资料纸、穿孔与细索引线。叠放表达分类和资料层级，正文须完整可读；不加厚重三维材质、渐变或持续漂浮。
- 英文主标题为 Anton 400（`IndexDisplay`），页签与衬线短句为 Newsreader 400（`IndexSerif`），正文、元数据与界面为 IBM Plex Mono 400／500（`IndexMono`）。保留窄粗标题、衬线标签、等宽索引的分工。
- 中文主标题使用未来荧黑 SC Compressed ExtraBold v0.93（未来荧黑 SC 压缩特粗，`IndexCJKDisplay`），真实字重 800；中文 `h1`、`h2` 的字族顺序为 `'IndexDisplay','IndexCJKDisplay','IndexCJK',sans-serif`，字重设为 800。采用字体原生窄高字形，与 Anton 的粗窄视觉相配，不用 CSS 横向压缩。正文与界面继续使用 Noto Sans SC 400（`IndexCJK`，图库标题可用真实 900）；宋体标签与短句继续使用 Noto Serif SC 400（`IndexCJKSerif`）。
- 英文与数字保留既有西文字体，中文按句意独立断行，不机械沿用英文大字行长。中文标题字号与行高按窄高字形局部调整，保留各页构图及文案。设置 `font-synthesis:none`；三种完整 WOFF2 中文字库、覆盖检查与 OFL 见 [typography.md](typography.md)。
- 唯一视觉参考是 [Mosby's Files](https://www.mosbyfiles.com/) 的分类封套、展开资料纸和三类字体分工。本主题的文案、构图与 24 张 SVG 均独立制作，不包含原站品牌、建筑图片或商业字体。
- 动效以文件轻移入、文字错峰、关系线展开及插图短距离平移淡入为主；插图不随鼠标三维倾斜。关闭动效或减少动态时保持完整静态画面。
- 鼠标使用可见主体约 23px 的实心档案页签，以左上角为热点；通常为黄页签与蓝色错边，黄底切换黑色主体，移动时带两枚递减的短页签残影。保留平面轮廓，不展开成大片文件或加立体阴影。行为与回退见 [player-contract.md](player-contract.md)。

| 可复用布局 | 适合表达 |
|---|---|
| `cover` | 黑底大标题、独立插图与短说明 |
| `problem` | 两行对照观点与说明纸签 |
| `directory` | 四个分类文件夹的总览 |
| `collect` | 一个重点与三条采集线索 |
| `sorting` | 单色封套内的字段与资料记录 |
| `connecting` | 两个对象及其明确联系 |
| `retrieve` | 深色书脊与检索图形分栏 |
| `routine` | 大数字与三个行动步骤 |
| `review` | 主结论与三项检查清单 |
| `finale` | 行动结语、插图与彩色分类回顾 |

## 24 张原创平面 SVG

图库四类各六张，用于后续新内容，可直接选择替换，不必每次重新生成。完整条目以 `graphics/catalog.json` 为准。

| 类别 | 素材示例 |
|---|---|
| 收集／`collect` | `open-index`、`capture-frame`、`intake-tray`、`field-notes` |
| 整理／`sort` | `sorted-set`、`branching-taxonomy`、`indexed-drawers`、`comparison-table` |
| 连接／`connect` | `linked-records`、`reference-wheel`、`evidence-chain`、`synthesis-map` |
| 应用／`use` | `search-window`、`living-library`、`decision-route`、`working-template` |

原六张 `open-index`、`capture-frame`、`sorted-set`、`linked-records`、`search-window`、`living-library` 原样保留；新增十八张带 `added_version: "1.0.0"`，可用「新增」筛选。全部为透明背景、1000×1000 viewBox 的原创平面矢量，无字体、外链、渐变、阴影或第三方图片，沿用随包 MIT 许可；字体与 PDF 库保持各自许可。

默认只在第 **1、4、7、30** 页放可替换插图，其他页面以文字或内容图解表达。按新内容增删插槽时先为图片留出空间，不让它覆盖正文。保留所在页的 `.cover-art` 等尺寸容器，并使用以下协议，不添加 `data-tilt`：

```html
<div class="cover-art art-entrance">
  <div class="artwork-slot" data-artwork-slot="unique-slot-id"
       data-artwork-id="open-index" data-artwork-default="open-index"
       data-artwork-label="这一页的标题"></div>
</div>
```

`data-artwork-slot` 是唯一位置 ID，素材 ID 可以重复。构建器嵌入图像，替换时保持插槽尺寸并按 contain 等比缩放；沿用原配色，不套用其他主题的金属、浮雕或色彩转换。

## 播放、替换与保存

- 导航是 16:9 画布内部底端的微型档案页签，前序实心、后序空心，当前页签加宽；按页面 `data-tone` 使用浅白或深黑保持对比，数量与顺序自动跟随页面。
- 沿用 [player-contract.md](player-contract.md)：窗口模式底部操作栏常驻并预留空间，全屏移动到底部唤出，保留鼠标；全屏按钮始终最右，滚轮一次手势只翻一页。
- 「替换素材」可选目标页、四类或新增筛选、预览后应用、取消及恢复默认。只有应用会改变当前图片，取消不改变；模态框内的滚动与按键不翻动底层幻灯片。没有插图的页可选择已有插图页，不自动插图。
- 「下载 HTML」保留文字、当前图片、完整 24 张图库、字体和许可，离线重开仍能继续替换。「下载 PDF」只呈现已应用的内容，隐藏导航、工具栏与未应用预览；为高清静态画面 PDF，不含可选择文字层。
- 新内容逐页检查标题行长、纸签叠放和图文间距。修改素材或选择器时检查四类各六张、新增十八张、应用／取消、保存重开、移动端以及实际 PDF；中文另检查主标题、正文、宋体标签和菜单均来自内嵌字体。

文字较多的页面由 Agent 在生成时判断配图与布局，见 [content-layout.md](content-layout.md)。中英文三十页样片只展示视觉风格，不限定新稿页数，也不要求逐页沿用样片配图。

## 三十页信息布局

版本仍为 `1.0.0`。中英文各30页，原前9页原样保留，原收尾移到第30页；第10–29页加入四列卡片、六种柱形／构成图、六种分析图、目标进度、数据表、方案对比、时间轴、分支、环形占比与漏斗。顺序、单位和读数规则见 [index-data-layouts.md](index-data-layouts.md)。不要求新稿使用全部布局，也不把30页当成页数上限。

新增标题容器位于1920×1080画布的左120、上80px，说明与实际图形至少间隔60px；正文图框在左120、上340px，大小1680×610，保留底部导航空间。全宽、三栏、图表与大读数、矩阵、表格与流程交替使用；保留本主题字族和配色，不给每页套同一右侧批注栏。画布不显示“示例数据”等制作标签，示例性质写入 `deck.json.data_provenance` 与页内数据属性。

工作副本的 `source/expansion30.py` 自包含本套内容、数据、几何和双语文本，提供 `get_slides(lang='en')` 与 `validate_data()`；中文接受 `zh` 或 `zh-CN`。修改后重渲染页面并重新构建，不只修改标签而保留旧图形。`source/expansion30.css` 使用本主题专有 `.x30-index` 命名空间，已追加在完整 `style.css` 和中文样式末尾，原页面规则不变。

图表采用 `data-chart-motion` 和原生SVG，数据容器只淡入，坐标系不整体位移。全部图表效果进入播放器原 `animations` 数组，由 `finish()` 在翻页、编辑、关闭动效、保存及PDF时统一结束；`pop` 使用 `transform-box:view-box`，虚线使用 `wipe-x`。保留最终静态几何与24张装饰图库，不把数据图当作可替换插图。

PDF在字体加载完成后，将附着导出副本的SVG文字计算字形样式冻结，再交给 `html-to-image`；字族、字号、字重、字距、对齐与绘制颜色须和HTML一致。只处理副本，不改播放DOM，不保存动画中间态。原有字体、完整字库、许可和24张SVG均保留。
