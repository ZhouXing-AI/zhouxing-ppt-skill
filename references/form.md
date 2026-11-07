# FORM · 成形

用户于 2026-11-06 确认的第四套主题，内部 ID `form`，主题版本 `1.0.0`。用户说「第四套」「FORM」「成形」「蓝色浮雕主题」时选择本主题。`Ideas Take Shape` 和「让想法成形」是中英文示例内容，新稿按用户主题另拟标题。

## 创建与文件

先查看 `assets/styles/form/preview.png`、`preview-zh.png` 和 `artwork-preview.png`；完整样例为该目录的 `example-en.html` 与 `example-zh.html`。

```sh
python3 scripts/create_deck.py --style form --prompt "做一份关于产品设计的演示" --out /absolute/path/to/new-deck
```

中文或混排输入默认中文，纯英文输入默认英文；明确要求英文时用 `--lang en`。脚本创建三十页样例副本，随后由 Agent 根据实际内容修改 `source/slides.html` 与 `deck.json`，再运行 `build_deck.py`。三十页是样例规模，可以按内容增删、调序。

- `source/style.css` 包含完整主题布局和播放器配色，构建器直接读取它。修改副本时以此文件为准；不要只合并 `theme.css` 与 `player-shared.css` 覆盖它，否则会漏掉 `palette-ui.css` 中的成品规则。
- 中文独立构图在 `source/locale-zh.css`，限定于 `html:lang(zh)`；中文文案在 `locales/zh-CN/slides.html`，创建中文副本时会覆盖 `source/slides.html`。不要为中文适配改坏英文构图。
- `source/artwork.css`、`artwork.js` 和 `artwork.html` 提供素材选择器；资源与双语名称、类别、关键词见 `graphics/catalog.json`。字体、素材、选择器和 PDF 依赖随 HTML 内嵌，成品不依赖本地服务器。

## 视觉与排版

- 固定 1920×1080。钴蓝 `#0755bb` 配石灰白 `#dcdbd5`，辅以浅白 `#ecece6`、分栏缝隙 `#c7c8c4` 和外部留边 `#c6c9c7`。通过灰白内容页与整页钴蓝建立节奏，不引入其他主题的强调色或材质。
- 大字、错位行首、窄缝分栏、细框和罗马数字索引共同组织画面。标题、图形和注释各有明确空间，按内容密度调整布局并保留底部导航安全区。
- 英文标题使用 Marcellus Regular（`FormDisplay`），正文与界面用 Instrument Sans（`ShiftSans`）。中文标题、正文和界面使用朱雀仿宋 Regular（`FormCJK`），英文、数字与罗马序号保留相应西文字体。两款标题字体都是真实 400 字重，不合成粗体或斜体。
- 中文按完整短句独立断行，例如「让想法／成形。」；通过字号、行距、颜色和留白区分层级。不要把长中文逐词塞进英文超大标题，也不要改回其他主题的重黑体。完整字库、覆盖检查与许可见 [typography.md](typography.md)。
- 配图像从底板中微微凸起：正视轮廓、宽幅柔和曲面、局部细刻槽和贴边短阴影。不要改成有明显侧面、地面椭圆影或悬浮透视的白色几何模型。第7页的浅凹空腔也保持正视。
- 唯一视觉参考为 [Wild Week — Athens](https://week.wild.plus/athens-26) 的配色、浮雕材质、分栏和索引节奏；本主题的文字、构图和 24 张图案已独立设计，不使用原站字标、人物浮雕、花瓶或活动文案。
- 动效使用短时板块上移、文字错峰、线条展开及浮雕淡入。浮雕不随鼠标倾斜；鼠标反馈和共享导航交互保留。关闭动效或减少动态时呈现完整静态画面。
- 鼠标使用可见主体约 23px 的实心菱形刻片，以中央落点为热点；灰白底用钴蓝主体，蓝底用灰白主体，移动时带两道短切面余影。保留浅刻边缘，不退回同色细轮廓，也不增加悬浮体积或多重波纹。行为与回退见 [player-contract.md](player-contract.md)。

十种样例布局可按叙事复用：

| 页面类型 | 适合表达 |
|---|---|
| `cover` | 错位大标题、右侧浮雕与独立说明 |
| `question` | 钴蓝整页的核心问题 |
| `observe` | 左侧观点、右侧细节与三项观察 |
| `boundary` | 三个并列边界、条件或原则 |
| `experiment` | 一个变化对应三种内容图解 |
| `relation` | 浮雕与结构、节奏、关系的组合 |
| `balance` | 重点与留白的对照 |
| `process` | 四个阶段的水平流程 |
| `review` | 三个问题或检验标准 |
| `finale` | 钴蓝结尾、行动短句与同色浮雕 |

## 24 张原创浅浮雕

图库分四类，每类六张；按内容选择，不必为新演示重新生成图片。

| 类别 | 常见语义与素材示例 |
|---|---|
| 空间 | 展开、边界、开放：`open-volume`、`quiet-arch`、`veined-leaf`、`open-courtyard` |
| 结构 | 联系、聚合、整体：`joined-planes`、`carved-loop`、`braided-current`、`shared-spine` |
| 推进 | 观察、迭代、生长：`ribbed-wave`、`step-study`、`terraced-contours`、`branching-path` |
| 平衡 | 重心、对照、留白：`balanced-mass`、`twin-seeds`、`counter-curves`、`still-ripple` |

完整列表以 catalog 为准，新增的 18 张带有 `added_version`，可用「新增」筛选。原有 ID 如 `open-volume`、`joined-planes` 已指向最终浅浮雕，不应按旧 ID 名称重做成体块。所有素材为透明背景、1000×1000 viewBox、无脚本或外链的 SVG 路径与渐变，使用随包 MIT 许可；字体和 PDF 库保持自己的许可。

默认在第 **1、3、6、7、30** 页使用可替换浮雕，其余页面由文字和内容图解表达。不要为了用完图库给每页堆图；需要插图时先给它独立空间。插槽保持以下协议，置于 `.artwork-relief` 内，不加 `data-tilt`：

```html
<div class="artwork-relief">
  <div class="artwork-slot" data-artwork-slot="unique-slot-id"
       data-artwork-id="open-volume" data-artwork-default="open-volume"
       data-artwork-label="这一页的标题"></div>
</div>
```

`data-artwork-slot` 标识位置且须唯一；素材 ID 可重复使用。构建器嵌入图像，选择器保持插槽尺寸并按 contain 缩放。灰白页使用石膏原色，`data-tone="dark"` 的蓝底页由 `artwork.js` 中 `sourceFor()` 将 SVG 的六位 HEX 色值转换为同色钴蓝。更换素材后自动适配，不另算一张素材；不要只在 CSS 上给整张图片套滤镜。扩充图案时沿用这一颜色格式并验证两种底色。

## 替换、保存与验证

- 「替换素材」支持目标页、四类浏览、预览后应用、取消和恢复默认。没有插图的页面可选择已有配图页，不自动盖住正文；模态框滚动和按键不翻动底层幻灯片。
- 「下载 HTML」保留当前图、完整 24 张库、文字、字体和许可；单文件离线重开仍可替换，未使用的图也保留。
- 英文第 5 页的首行强调使用显式 `.experiment-lead` 元素；不要改为 `::first-line`，以保持浏览器和 PDF 的字号一致。导出器在副本中固化 SVG 绘制样式，保留图解的填充与描边。
- 「下载 PDF」呈现已经应用的文字与浅浮雕，不含未应用预览、导航和工具栏。它是高清静态画面 PDF，不是可编辑 PPTX 或可选择文字层。
- 按 [player-contract.md](player-contract.md) 验证共享播放器。新文案重点看中文行长、分栏对齐和图文距离；改素材或选择器时，再检查浅色与蓝色预览、应用／取消、保存重开和实际 PDF 中的浮雕。

文字较多的页面由 Agent 在生成时判断配图与布局，见 [content-layout.md](content-layout.md)。中英文三十页样片只展示视觉风格，不限定新稿页数，也不要求逐页沿用样片配图。

## 三十页信息布局

版本仍为 `1.0.0`。中英文各30页，原前9页原样保留，原收尾移到第30页；第10–29页加入四列卡片、六种柱形／构成图、六种分析图、目标进度、数据表、方案对比、时间轴、分支、环形占比与漏斗。顺序、单位和读数规则见 [form-data-layouts.md](form-data-layouts.md)。不要求新稿使用全部布局，也不把30页当成页数上限。

新增标题容器位于1920×1080画布的左120、上80px，说明与实际图形至少间隔60px；正文图框在左120、上340px，大小1680×610，保留底部导航空间。全宽、三栏、图表与大读数、矩阵、表格与流程交替使用；保留本主题字族和配色，不给每页套同一右侧批注栏。画布不显示“示例数据”等制作标签，示例性质写入 `deck.json.data_provenance` 与页内数据属性。

工作副本的 `source/expansion30.py` 自包含本套内容、数据、几何和双语文本，提供 `get_slides(lang='en')` 与 `validate_data()`；中文接受 `zh` 或 `zh-CN`。修改后重渲染页面并重新构建，不只修改标签而保留旧图形。`source/expansion30.css` 使用本主题专有 `.x30-form` 命名空间，已追加在完整 `style.css` 和中文样式末尾，原页面规则不变。

图表采用 `data-chart-motion` 和原生SVG，数据容器只淡入，坐标系不整体位移。全部图表效果进入播放器原 `animations` 数组，由 `finish()` 在翻页、编辑、关闭动效、保存及PDF时统一结束；`pop` 使用 `transform-box:view-box`，虚线使用 `wipe-x`。保留最终静态几何与24张装饰图库，不把数据图当作可替换插图。

PDF在字体加载完成后，将附着导出副本的SVG文字计算字形样式冻结，再交给 `html-to-image`；字族、字号、字重、字距、对齐与绘制颜色须和HTML一致。只处理副本，不改播放DOM，不保存动画中间态。原有字体、完整字库、许可和24张SVG均保留。
