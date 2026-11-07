# ECHO · 回响

用户要求完整制作并收录的第九套主题，内部 ID `echo`，版本 `1.0.0`。用户说「第九套」「ECHO」「回响」「午夜蓝玻璃主题」时选择本套。中英文示例标题为「让想法产生共鸣」／`Make space for resonance`，讲述关注、表达和体验；主题名称与内容独立，新稿按实际题材重写。

## 创建与语言

查看 `assets/styles/echo/preview.png`、`preview-zh.png` 与 `artwork-preview.png`。完整样片为 `example-en.html`、`example-zh.html`，各三十页。

```sh
python3 scripts/create_deck.py --style echo --prompt "为一场文化活动设计演示" --out /absolute/path/to/new-deck
```

中文或混排创作输入默认中文版，纯英文默认英文版；用户明确指定输出语言时传 `--lang zh-CN` 或 `--lang en`。工作副本改文案、页数、构图与 `deck.json`，再用 `build_deck.py` 编译。模板不是对题材、页数或配图数量的限制。

- `source/style.css` 为完整页面与播放器样式，`source/locale-zh.css` 仅在 `html:lang(zh)` 生效。
- 中文内容、菜单和字体配置来自 `locales/zh-CN/`；英文单文件只载入西文字体，中文额外内嵌两种完整中文字库。不能只改 HTML 的语言属性。
- 字体、SVG、交互和 PDF 依赖与许可内嵌，离线打开即可使用。

## 视觉系统

唯一网站参考为 [Overworld Audio](https://overworldaudio.com/)：午夜蓝空间、雾状层次、衬线字、细线与克制导航。我们将空间氛围转为原创声学玻璃物件和独立演示版式，不使用其群岛地形、3D 场景、商标、摄影、音视频、文案或商业字体。

- 主色：午夜蓝 `#12141F`、雾蓝 `#A8B9CB`、珍珠白 `#F0F1ED`；浅页 `#E2E8E9`，中间蓝页 `#293E53`，辅助 `#607E9A`。留白、背景明暗与字级形成节奏，不依赖满屏粒子或持续运动。
- 英文标题 Cormorant Garamond 真实 500（`EchoDisplay`），正文与界面 Instrument Sans 400/500（`EchoSans`）。中文标题 Noto Serif SC 300（`EchoCJKDisplay`），正文与界面 Noto Sans SC 400（`EchoCJK`）。中文独立断行，正常字形比例与字距，不合成粗斜体。
- 采用完整官方字库，不按样稿裁字。OFL、固定来源、SHA、真实字重范围与 cmap 覆盖位于 `fonts/font-manifest.json`、`NOTICE.txt` 和 coverage 文件；本套 Instrument Sans 使用完整官方源，不使用早期主题的拉丁子集。
- 配图与文字各有独立区域。大幅标题、居中观点、双栏问答、三层说明、左右对照、四阶段时间线和三项原则交替出现。低信息量页面保留空间，不靠重复微小标签填满。
- 文字轻微上移淡入，物件短距离淡入。没有音频、持续漂浮、无限旋转或鼠标倾斜。

| 布局 | 适合内容 |
|---|---|
| `cover` | 一句主张与独立共鸣物件 |
| `listen` | 居中观点、前后两句、留白与停顿 |
| `signal` | 三个筛选问题或判断标准 |
| `layers` | 三个层次、因素或组成部分 |
| `contrast` | 左右对照、差异与一条信息波形 |
| `frequency` | 一组关系图与三步回应 |
| `rhythm` | 四阶段时间线或过程 |
| `memory` | 重点结论与记忆物件 |
| `discovery` | 三个平行原则、条件或建议 |
| `closing` | 下一步邀请与开放远景 |

用户材料较多时按 [content-layout.md](content-layout.md) 逐页重排，必要时省去装饰；保留关系图、表格、数据与必要说明。没有观众端「纯文字」开关。

## 24 张原创 SVG

`listen` 聆听、`tune` 调谐、`connect` 联结、`resonate` 回响各六张。全部为初始完整库，无新增标记。双语名称、关键词、用途见 `graphics/catalog.json`；原创素材采用随包 MIT 许可。

透明 1000×1000 SVG：冰蓝与石墨蓝渐变、半透明叠层、细边高光与少量暖白内核。24 张各有语义和轮廓，不使用外部图片、字体、脚本或滤镜。图形在浅底与深底均已复核，不通过替换逻辑强行改色。必要时在页面上用柔和光场承托暗侧，保留图形自身比例。

默认配图在第 1、3、4、6、8、30 页，分别为 `resonance-vessel`、`listening-shell`、`signal-lens`、`paired-waves`、`memory-loop`、`open-horizon`；不要求新演示逐页沿用。插槽拥有唯一 `data-artwork-slot`、当前 `data-artwork-id`、`data-artwork-default` 与对应语言的 `data-artwork-label`，按 contain 显示。

## 播放与导出

遵守 [player-contract.md](player-contract.md)。细边午夜蓝工具栏提供编辑、替换素材、动效、下载 HTML、下载 PDF；带图标的全屏在最右。音阶短柱导航位于 16:9 画布内，当前项加宽。左右明暗分栏页通过 `.split` 或 `data-cursor-split` 识别，不绑定页码，导航使用双层明暗轮廓。

实心水滴拨片鼠标可见主体约 23 CSS px，尖端对应真实热点，移动带两条约 160ms 的短弧尾。分栏页按实际左右位置即时选择明暗填充；如改变分栏，可用 `data-cursor-split="light-dark"`／`"dark-light"`，子区可标注 `data-cursor-half` 和 `data-cursor-tone`。控件、编辑、触屏、关闭动效和减少动态使用原生鼠标。

保存 HTML 保留文字改动、当前配图和完整图库。PDF 使用当前已应用的图形，逐页生成高清静态画面，不弹打印窗口；不包含工具栏、导航和鼠标，也不含可编辑文字层。检查中英文实际字体、逐页边界、分栏导航与鼠标、素材替换/取消/恢复、离线保存重开、滚轮和全屏，再实际下载 PDF。

## 三十页样稿与数据扩展

中英文各30页，原前9页的内容和动效保留，原结尾移到第30页；第10–29页增加20种内容布局，见 [echo-data-layouts.md](echo-data-layouts.md)。本主题版本保持1.0.0，24张原创素材和完整字库不变。新增页面讲述聆听、调谐、联结和回响；午夜蓝、雾蓝与珍珠白，细线、留白及无填色雷达。玻璃感只用于既有装饰素材，数据保持准确二维尺度。

新增页不是每页一套相同卡片：全宽图、左右分栏、关键大数、并列小图、完整表格、时间轴与逻辑流程交替使用。标题与说明整体从80px开始，图文区从350px开始，按实际字体测量至少60px间距。中文采用本套既有字体独立安排标题及标签，不机械沿用英文负字距。

工作副本的 `source/expansion30.py` 暴露 `get_slides(lang='en')` 和 `validate_data()`，可重生成这20页。所有数值是本地原创概念数据，来源属性留在两份 `deck.json` 的 `data_provenance` 与配方中，成品不展示示例/制作标签。用户提供真实资料后，同时重算数据、单位、SVG几何与结论，不能仅编辑数字标签。样稿不是固定30页的填空表。

图表只使用有限时长的显现动画；`source/chart-motion.js` 返回的全部效果加入既有播放器 `animations`，由同一个 `finish()` 生命周期清理。原页动效不变，信息图不随正文整体平移。保存、编辑、目录、关闭动效和PDF导出时保留完整终态。PDF导出副本冻结SVG `text`/`tspan`的实际字体样式，保留衬线数字和百分号字级；原稿不被导出过程改写。
