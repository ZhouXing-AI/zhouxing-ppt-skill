# FOCUS · 明晰

英文主题名 FOCUS，中文主题名 明晰，内部 ID `focus`，主题版本 `1.0.0`。名称与内容独立；`Clarity in Motion` 只是英文示例标题。由用户选择的绿色编辑设计方向发展而来，原创概念雕塑替代棋子与棋盘；不引用或复制 Money in Check 的品牌、文案、棋子造型、首屏构图和棋盘背景。

## 创建

这是用户确认的第二套主题。提供完整中文与英文模板。先读本参考，查看 `assets/styles/focus/preview.png`、`assets/styles/focus/preview-zh.png` 和 `assets/styles/focus/artwork-preview.png`。

```sh
python3 scripts/create_deck.py --style focus --prompt "先看清，再行动" --out /absolute/path/to/new-deck
# 明确要求英文时使用 --lang en；纯英文 prompt 也会自动选择英文。
```

中文或中英混排输入默认中文；纯英文输入默认英文；用户明确指定的输出语言优先。中文示例标题为「先看清，再行动」，并非主题名。两套模板共享 SVG 与播放器，但中文按自己的字号、换行、字距和留白排版。中英文样稿现各30页：原有前9页，14页四列布局与数据图表，新增6页业务布局，原收尾移到第30页。新增布局的规则和复用脚本见 [focus-data-layouts.md](focus-data-layouts.md)。

## 视觉系统

- 画布 1920×1080；浅纸灰 `#ededeb`、墨绿 `#162720`、翡翠绿 `#00856c`、深绿 `#073d32`。样片用薄线与留白突出重点；新稿按真实内容安排文字空间。
- 英文标题 Instrument Serif，真斜体 Instrument Serif Italic；界面和短标签 Instrument Sans。字体文件与 OFL 声明内嵌。斜体用 `MoveItalic` 字族或现有 `em` 规则，不用伪斜体，不引入商业字体 PP Editorial Old。
- 中文内容用 Noto Serif SC（`FocusCJK`）：主标题、小标题、正文与图注用真实 400 字重，绿底描边标题 `.outline` 用 500。短标签、导航、工具栏、素材库界面、学习回路，以及新增图表的数轴、精确读数与图例用 Noto Sans SC 400（`FocusCJKSans`）；图表内的叙事大数字和部分分类名可使用 Instrument Serif／Noto Serif SC400，保留编辑式层次。中文 `em` 使用正常体改色，不伪斜体，Latin 强调仍用 `MoveItalic`，英文版保留原衬线、真斜体及 Instrument Sans。两版均嵌入这两套完整中文字库及 OFL 声明，浏览器改写中文后仍可离线显示；来源与覆盖见 [typography.md](typography.md)。
- 让字形、银黑金属体积和绿色形成共同风格。不要复刻另一网站的特色主视觉；不加棋子、棋盘、格子满屏背景。
- 鼠标使用可见主体约 23px 的银绿实心镜片，以中心为热点；浅底用深翡翠绿填充，绿底与深底用浅银绿填充，移动时带两枚短镜片余影。不退回空心细环，不增加机械叶片、外圈粒子或系统箭头。行为与回退见 [player-contract.md](player-contract.md)。
- `source/theme.css` 是主题布局，`player-shared.css` 和 `palette-ui.css` 是播放器样式；修改后把三者及新增的 `source/data-layouts.css` 依次拼接回 `source/style.css`；中文样式末尾也保留新增图表规则，避免原十页通用规则覆盖它们。素材选择器独立于 `style.css`，构建器追加 `source/artwork.css`。
- 原有十种视觉布局：左文右雕塑封面／中心宣言／问题与透镜／绿色大字与丝带／三列时间范围／投入账本／打开的工作笔记与学习回路／深色留白与框架／四个决策问题／下一步与阶梯。按内容选择，不要求每份稿件十页。
- 新增四列卡片与13种数据图表，按 [focus-data-layouts.md](focus-data-layouts.md) 复用；其中只有独立垂直柱形使用准确正面加固定浅侧面的银绿材质，其余分析图保持二维。样例性质与来源记录在配方、元数据和制作资料中；成品不出现“示例数据”“四列卡片”等制作标签，必要单位融入内容说明或图表。预览直接使用最终输出页面，不靠截图专用隐藏规则清理画面。
- 新增页面标题容器位于左120、上82px，标题不留上边距；图表框默认位于左120、上340px，尺寸1680×610，第10页卡片与第23页目标图表上沿为350px。副标题与图形实际边界至少间隔60px。标题可局部绿色强调，配合衬线大数字、细线与深浅节奏，不把标题下压到图表附近，也不套用统一左图右KPI。
- 最终第10–16页依次为：纸面四卡（末卡绿色）、左大数字与右银绿浅金属柱、深绿全宽横条、三列文档计数、水平成对条、垂直100%堆积柱、暗色预算瀑布。第17–23页依次为：折线与侧读数、深绿面积、雷达与表、纸面桑基、散点、热力、三列大衬线目标百分比与精准细进度条。具体数值、定义与数学检查保留在数据布局文档及配方中，主题版本仍为 `1.0.0`。
- 示例仅在第 1、3、4、8、30 页摆放可替换雕塑。其余页面可保留纯文字或内容图解。不要为用完素材强制逐页放图。

## 24 张主题素材

资源在 `graphics/`，目录与中英文名称在 `graphics/catalog.json`，对应六类：

| 类别 | 素材 |
|---|---|
| 观察 | focus-ring 聚焦透镜；signal-prism 信号棱镜；orbit-signal 环绕信号；wave-channel 波形通道 |
| 连接 | linked-rings 协作双环；bridge-connector 连接桥；woven-link 交织连接；relay-nodes 协作节点 |
| 推进 | rising-steps 递进阶梯；flow-ribbon 流动丝带；momentum-arrow 动量箭头；ascending-helix 上升螺旋 |
| 结构 | layered-system 层叠系统；modular-cluster 模块集群；nested-architecture 嵌套架构；core-assembly 核心组件 |
| 取舍 | balanced-form 平衡构件；branching-path 分岔路径；pivot-disc 决策支点；selective-gate 选择之门 |
| 空间 | open-frame 开放框架；unfolding-form 展开形态；expanding-fan 扩展扇面；horizon-portal 远景之窗 |

这些是本主题可复用的语义素材，不是限定给某一份演示的一次性插图。默认优先按内容从内置库选择，不调用图像模型重画，不临时拼出风格不一致的图；没有合适配图时保留文字或图解页。新素材须独立审核风格，保持透明背景、1000×1000 viewBox、银黑金属、克制绿色和左上照明。纯矢量、无外部链接和脚本；许可随资源分发。

插槽写法：

```html
<div class="artwork-slot" data-artwork-slot="unique-slot-id"
     data-artwork-id="focus-ring" data-artwork-default="focus-ring"
     data-artwork-label="Read the signals"></div>
```

每个插槽有唯一 ID，置于布局定义好的 `.artwork-tilt` 容器内。构建时自动填入自包含 SVG 图像，不改变插槽位置和 contain 缩放。没有素材库的旧主题不启用该功能。相同素材可用于不同插槽，SVG 通过独立图像隔离渐变 ID。

## 替换、保存与导出

- 底部「替换素材」（英文为 Replace artwork）打开内置库，「新增」筛选可查看后加入的 12 张，选择目标页与素材，预览后应用；取消不改当前内容；可恢复默认素材。
- 无插图页仍可打开库并选择有配图的页面，不能把图片随意盖在文字页上。
- 替换素材时暂时屏蔽底层翻页；关闭后恢复滚轮、键盘与全屏操作。
- 「下载 HTML」保留当前图片选择、文字修改、字体、许可与整套可替换库。重新打开还能继续替换，不依赖原目录、本地服务器或网络。未下载的修改只存在当前打开页面。
- 为支持离线替换，交付 HTML 包含全部 24 张素材；这是有意保留的文件体积，不要为了减小体积删掉未使用素材库。
- 「下载 PDF」使用当前已经应用的图片，逐页生成高清静态 PDF，不包含操作栏和选择器；不会弹打印窗口。PDF 不具备 HTML 的替换和交互功能。
- PDF截图前等待字体就绪，并在已挂入文档的导出副本上冻结全部 SVG `text`／`tspan` 的计算字形样式，包括字族、字号、字重、字距、对齐、填色与描边。不要只复制class名；否则衬线数字、斜体或目标百分比可能回退。只处理导出副本，不修改原DOM或记录动画中间变换；实际PDF须与HTML字形一致。

## 验收

除 player-contract.md 外，验证 24 张预览、取消/应用/恢复默认、无图页选择目标页、选择器内滚动不翻页；替换两页后下载 HTML 并离线重开再替换；实际导出 PDF 检查更新后的图片。中文另检查逐页字形、学习回路内的 SVG 汉字、输入法编辑保存、中文 PDF 与缺字覆盖。`source/locale-zh.css` 随两个版本复制，但仅作用于 `html:lang(zh)`；不能漏掉此文件或把它改成全局英文排版。

图表进场保留语义动画钩子与最终静态几何。`pop` 的缩放原点由SVG绝对坐标计算，必须使用 `transform-box:view-box`，不能用 `fill-box`；虚线采用 `wipe-x`，不能用 `draw` 改写虚线间隔。检查标题区间距、中英文局部强调、逐点读数，以及实际下载PDF后的衬线大数字、字重与对齐。

文字较多的页面由 Agent 在生成时判断配图与布局，见 [content-layout.md](content-layout.md)。中英文30页样片展示视觉风格与数据布局能力，不限定新稿页数，也不要求逐页沿用样片配图。


## 当前30页样稿

原有24页内容全部保留，原收尾移到30；第24–29页为六种新增业务版式。十二套现在均为中英文各30页，共720页。详细页码、能力与复用见 [统一能力清单](layout-coverage.md)。这一扩展为用户要求的新样稿，待本轮审阅；主题本身及原有页面的确认不变。
