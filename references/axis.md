# AXIS · 轴线

用户于 2026-11-07 确认收录的第六套主题，内部 ID `axis`，版本 `1.0.0`。用户说「第六套」「AXIS」「轴线」「工程结构主题」时选择此套。英文样稿 `Give progress a direction` 与中文样稿「让每一步都有方向」是概念内容，新演示按用户主题另拟标题。

## 创建

先看 `assets/styles/axis/preview.png`、`preview-zh.png` 及 `artwork-preview.png`；完整例稿为 `example-en.html`、`example-zh.html`。

```sh
python3 scripts/create_deck.py --style axis --prompt "为产品团队做一份工作方法演示" --out /absolute/path/to/new-deck
```

中文或混排输入默认中文，纯英文默认英文；明确语言时使用 `--lang zh-CN` / `--lang en`。生成的三十页是工作副本，随后按内容改文案、页数、构图和元数据，再运行 `build_deck.py`。主题名不等于演示标题。

- `source/style.css` 是完整已确认样式，不要重新拼接其他主题的 UI 样式覆盖它。`source/locale-zh.css` 只作用于 `html:lang(zh)`。
- 中文文案、菜单及字体配置来自 `locales/zh-CN/`。英文仅内嵌西文字体；中文另外内嵌完整 Noto Sans SC。不能只修改 `lang` 就当作完成翻译与排版。
- 字体、24 张 SVG、播放器、PDF 依赖及许可全部内嵌，输出的单文件可离线使用。

## 视觉与排版

- 唯一参考网站为 [Atlas Motion Systems](https://atlasmotion.com/)：借鉴炭黑与暖象牙白、精密细线、大字和小标注的尺度差、工程部件之间的关系。此套不包含原站商标、电机、无人机图片、字体文件或原站模型；文案、构图及插图独立制作。
- 页面用石墨黑 `#181a18` 与暖象牙白 `#fffde0` 建立明暗节奏，银灰 `#b9bcb4` 用于次级信息。不要把留白填满，也不把所有页面做成相同卡片。明暗比例按内容决定。
- 英文标题、正文用 Instrument Sans（`AxisSans`，真实 400–700），精密编号与标签用 IBM Plex Mono Regular（`AxisMono`）。中文标题用 Noto Sans SC 500，正文、短标签与界面用 400（`AxisCJK`）；使用 `font-synthesis:none`。中文独立断行和接近正常的字距，不沿用英文大字的强负字距。
- 正文与标题左边线、分栏规则和图形锚点对齐。信息关系图可以用矢量线、箭头和选中区域；必要的图表属于内容，不随装饰图片一起去掉。
- 动效为短距离轴向进入、文字逐组出现、细线展开，停止后保留完整静态构图。不持续旋转、漂浮或跟随鼠标倾斜。
- 鼠标为约 23 CSS px 的实心精密箭头，明暗页切换填充，尖端对准热点，短粒点拖尾有限消退。沿用共享的操作区原生鼠标、减少动态和触屏回退。

| 布局 | 适合表达 |
|---|---|
| `cover` | 大字标识、短主张与独立结构图 |
| `bearing` | 一个方向性判断与两项边界 |
| `forces` | 三项原则、能力或构成因素 |
| `tradeoffs` | 取舍维度、决策矩阵与选择 |
| `evidence` | 问题、验证与结果三阶段 |
| `layers` | 系统关系、输入、决策与输出 |
| `loop` | 有明确回路的四步流程 |
| `adapt` | 两组对照、稳定与可变因素 |
| `scale` | 从单次实践到可重复系统 |
| `closing` | 一条行动结语与方向性插图 |

新内容可重组版式，十页不是限制。文字较多时由 Agent 重新安排文字区并省略不必要的装饰，见 [content-layout.md](content-layout.md)。AXIS 不预设多文字展示页，也不提供观众端的「纯文字」开关；需要新的文字主导布局时为该页补充 CSS，不只隐藏图片留下空洞。

## 24 张原创结构 SVG

四类各六张：`structure` 结构、`direction` 方向、`feedback` 反馈、`capacity` 容量。完整名称、关键词和文件在 `graphics/catalog.json`。原八张保留，新十六张标记 `added_version: "1.0.0"`。

全部是 800×800 viewBox、透明背景、石墨黑侧壁、银灰切面和暖白细边的原创矢量。按本套几何投影和光照制作，不用其他主题图片补数量；不含位图、外链、脚本或实际电机结构。原创插图随附 MIT 许可，字体与第三方库保留各自许可。

默认第 1、3、6、9、30 页有插图，其他页以文字和信息关系图表达。并非每页都要配图，也不必把 24 张全部放进三十页样稿；完整图库供用户替换与后续内容复用。图形保留本色，以石墨色衬底承托；放到浅色页时先检查对比。

```html
<div class="cover-art art-entrance">
  <div class="artwork-slot" data-artwork-slot="unique-position"
       data-artwork-id="linear-core" data-artwork-default="linear-core"
       data-artwork-label="当前页的插图" data-decoration></div>
</div>
```

位置 ID 必须唯一，素材 ID 可重复。图片按插槽 contain 缩放，替换不会改变文字构图。宽扁图应放在较宽的区域，不添加 `data-tilt` 或 FORM 的颜色替换逻辑。

## 播放与验证

遵循 [player-contract.md](player-contract.md)。16:9 画布内底部为工程刻度导航：普通短刻度、已读加深、当前加宽实心块，随明暗页切换对比。底部操作栏含编辑、替换素材、动效、下载 HTML、下载 PDF，带图标的全屏始终最右。

检查中英文各三十页完整、字体覆盖、四类各六张、切换和应用素材、保存 HTML 离线重开，以及实际三十页 PDF。PDF 保留当前已应用图形和静态排版，隐藏工具、导航与鼠标，为高清栅格页面，不含可编辑文字层。

## 三十页信息布局

版本仍为 `1.0.0`。中英文各30页，原前9页原样保留，原收尾移到第30页；第10–29页加入四列卡片、六种柱形／构成图、六种分析图、目标进度、数据表、方案对比、时间轴、分支、环形占比与漏斗。顺序、单位和读数规则见 [axis-data-layouts.md](axis-data-layouts.md)。不要求新稿使用全部布局，也不把30页当成页数上限。

新增标题容器位于1920×1080画布的左120、上80px，说明与实际图形至少间隔60px；正文图框在左120、上340px，大小1680×610，保留底部导航空间。全宽、三栏、图表与大读数、矩阵、表格与流程交替使用；保留本主题字族和配色，不给每页套同一右侧批注栏。画布不显示“示例数据”等制作标签，示例性质写入 `deck.json.data_provenance` 与页内数据属性。

工作副本的 `source/expansion30.py` 自包含本套内容、数据、几何和双语文本，提供 `get_slides(lang='en')` 与 `validate_data()`；中文接受 `zh` 或 `zh-CN`。修改后重渲染页面并重新构建，不只修改标签而保留旧图形。`source/expansion30.css` 使用本主题专有 `.x30-axis` 命名空间，已追加在完整 `style.css` 和中文样式末尾，原页面规则不变。

图表采用 `data-chart-motion` 和原生SVG，数据容器只淡入，坐标系不整体位移。全部图表效果进入播放器原 `animations` 数组，由 `finish()` 在翻页、编辑、关闭动效、保存及PDF时统一结束；`pop` 使用 `transform-box:view-box`，虚线使用 `wipe-x`。保留最终静态几何与24张装饰图库，不把数据图当作可替换插图。

PDF在字体加载完成后，将附着导出副本的SVG文字计算字形样式冻结，再交给 `html-to-image`；字族、字号、字重、字距、对齐与绘制颜色须和HTML一致。只处理副本，不改播放DOM，不保存动画中间态。原有字体、完整字库、许可和24张SVG均保留。
