# SPARK · 燃点

用户要求完整制作并收录的第十套主题，内部 ID `spark`，版本 `1.0.0`。用户说「第十套」「SPARK」「燃点」「荧光树脂主题」「荧光绿行动主题」时选择本套。中英文示例标题为「迈一小步，改变开始。」／`Small moves, real momentum`，讲述把想法变成行动；主题名称与题材独立，新稿按用户实际内容重写。

## 创建与语言

查看 `assets/styles/spark/preview.png`、`preview-zh.png` 与 `artwork-preview.png`。完整样片为 `example-en.html`、`example-zh.html`，各三十页。

```sh
python3 scripts/create_deck.py --style spark --prompt "为一个创意项目制作行动方案演示" --out /absolute/path/to/new-deck
```

中文或混排输入默认中文版，纯英文默认英文版；用户明确指定输出语言时传 `--lang zh-CN` 或 `--lang en`。在工作副本中调整文案、页数、构图与 `deck.json`，再用 `build_deck.py` 编译。三十页示例和六个默认插图位置不限制新稿。

- `source/style.css` 为页面与播放器样式，`source/locale-zh.css` 的中文规则仅在 `html:lang(zh)` 生效。
- 中文内容、双语菜单与字体配置来自 `locales/zh-CN/`；英文只内嵌西文字体，中文额外内嵌两种完整中文字库。切换语言不能仅修改 HTML 语言属性。
- 字体、SVG、交互、PDF 依赖及各自许可均内嵌，支持离线使用。

## 视觉系统

唯一网站参考为 [Anyflow Labs](https://labs.anyflow.agency/)：荧光绿与黑灰对比、紧凑大字、明确的板块节奏和短促动作。转译为原创树脂模块及独立演示构图，不使用原站 3D 字母标志、六边形蜂窝、首屏构图、商标、商业字体或文案。

- 主色为荧光绿 `#B7FF3C`、墨黑 `#11140F`、浅灰 `#F1F2EE`、深绿 `#396214`。荧光色承载重点和完整观点页；浅灰页留出说明空间，墨黑页强调开场、试验和收束。
- 英文标题 Barlow Condensed ExtraBold 800（`SparkDisplay`），全大写、窄高字形与紧凑行距；正文与界面 Manrope 400/500（`SparkSans`）。不通过横向缩放制造窄体。
- 中文标题使用得意黑 Smiley Sans Oblique 的真实 400 字重（`SparkCJKDisplay`）。字体元数据与 CSS 均声明 italic，选择字体自身约 8° 的倾斜字形；设置 `font-synthesis:none`，不额外斜切、压缩或伪加粗。正文与界面 Noto Sans SC 400（`SparkCJK`）使用 normal。中文按完整短句独立断行，不硬套英文行宽。
- 使用完整官方字库，不按样稿裁字。得意黑官方 v2.0.1 WOFF2 原字节保留 `fsType=8`（Editable Embedding），其他本套字体为 `fsType=0`；未改权限位。免费商用、嵌入与开源再分发依据为随包 OFL 1.1，完整版权、固定来源、release 证据、SHA、真实字重与 cmap 覆盖见本套 `fonts/font-manifest.json`、`NOTICE.txt` 和 coverage 文件。
- 大标题、三项判断、资源卡、版本对照、试验步骤、累积进展、复盘和四阶段实践交替出现。文字与配图有独立区域，短句优先；不以重复小标签填充留白。
- 动效为文字短距离进入、线条展开与插图轻微上移淡入。关闭动效或减少动态时保留完整静态内容，不持续漂浮或跟随鼠标倾斜。

| 布局 | 适合内容 |
|---|---|
| `cover` | 一句行动主张与独立启动物件 |
| `action` | 两行大字观点与方向提示 |
| `specific` | 三个问题、判断标准或目标约束 |
| `resources` | 三项可用资源与组合关系 |
| `version` | 想法到初版的转变或前后对照 |
| `experiment` | 三步试验、观察与调整 |
| `progress` | 三层累积、阶段成果或里程碑 |
| `review` | 三项复盘、保留与修正建议 |
| `practice` | 四阶段实践、流程或习惯 |
| `closing` | 下一步行动与推进物件 |

较多文字按 [content-layout.md](content-layout.md) 逐页重排，必要时省去装饰，保留表格、数据、流程和说明。没有观众端「纯文字」开关；浏览器编辑新增内容后仍需检查版面。

## 三十页与新增内容布局

中英文样片各30页：原前9页保持，原收尾移到第30页，第10–29页补充20种内容布局。原24张素材和完整字体保持不变。新演示不受30页限制；按用户信息结构选择版式，不把示例值作为外部事实。

新增布局由 `source/expansion30.py` 的 `get_slides(lang='en')` 和 `validate_data()` 复现，支持 `en`、`zh`、`zh-CN`；样式在 `source/expansion30.css`，已追加到 `style.css` 和中文样式。每页带 `data-layout-id`。详见 [spark-data-layouts.md](spark-data-layouts.md)。

新增图表用主题原有字体和二维刻度，图表不属于装饰替换槽。没有四角品牌小字、示例数据或版式类型标签；必要单位直接保留。示例属性保留在 `deck.json` 与配方。标题整体上距80px、图区上距340px；字体与内容变更后重新验证间距和中文行长。

数据动效使用有限时长的 `data-chart-motion` 与 step；虚线采用 wipe-x，不用 draw。坐标系只淡入，数据按实际方向展开，不整图平移。所有动画进入同一播放器清理数组，快速翻页、关闭动效、编辑、保存HTML、PDF和减少动态时回到完整终态。PDF内联SVG文字计算样式后截图，保留本套实际字体。

## 24 张原创 SVG

`start` 启动、`shape` 塑形、`test` 试验、`advance` 推进各六张。全部为初始完整库，不显示新增筛选。双语名称、关键词和用途见 `graphics/catalog.json`；原创图形按随包 MIT 许可分发。

透明 1000×1000 SVG，以荧光绿树脂正面、深绿短挤出侧面、墨黑连接结构和细窄高光表现可触及的行动模块。各图有不同轮廓和用途，不是换色重复图标；不引入原站标志、位图、外部字体、脚本或资源。浅底、绿底与黑底均保留原色及比例，不套用其他主题的改色逻辑。

默认配图如下；新稿可以随内容增删，不要求每页配图。

| 页码 | 插槽 | 默认素材 |
|---|---|---|
| 1 | `ignition` | `ignition-switch` 启动开关 |
| 3 | `idea` | `idea-capsule` 想法胶囊 |
| 4 | `resources` | `modular-joint` 组合接头 |
| 6 | `experiment` | `test-loop` 试验回路 |
| 7 | `progress` | `step-blocks` 递进块 |
| 30 | `momentum` | `momentum-arrow` 动量箭头 |

每个插槽保留唯一 `data-artwork-slot`、当前 `data-artwork-id`、`data-artwork-default` 与对应语言的 `data-artwork-label`，按 contain 显示；不要把装饰插槽变为承载必要信息的唯一载体。

## 播放与导出

遵守 [player-contract.md](player-contract.md)。黑色快捷栏依次提供翻页/页码目录、编辑文字/替换素材、动效/下载 HTML/下载 PDF，带图标的全屏在最右。斜切导航位于 16:9 画布内部底部，当前项加宽并描边，深浅页维持清晰对比。

实心闪电楔鼠标可见主体约 22.67 CSS px，左上尖端对应真实热点，移动带两段约 160ms 的短切片尾。浅灰与荧光绿页面使用墨黑主体，深底使用荧光绿；尺寸不随画布放大。控件、编辑、触屏、关闭动效和减少动态保留原生鼠标。

保存 HTML 保留文字修改、当前素材、完整图库、字体与许可。PDF 使用已应用的图形生成逐页高清静态画面，不弹打印窗口，不包含导航、快捷栏、鼠标或可编辑文字层。交付前检查真实字体、所有页边界、导航与鼠标、素材替换/取消/恢复、离线保存重开、滚轮、全屏，并实际下载 PDF 核对静态画面。
