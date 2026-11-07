# SHIFT · 流变 / 已确认风格与中英文适配

视觉参考唯一来自 [Superlocal](https://www.superlocaldesign.com/)。已核对其首页、Lineup、Cronograma及公开CSS/JS；点群分步显现和滚动机制来自源码。它是设计参考，成品不代表 Superlocal 官方。

## 样式

- 主题英文名：SHIFT；中文名：流变；内部 ID：`shift`。不同演示可使用不同内容标题，不把“让灵感流动”作为所有演示的固定标题。

- 主色：银灰 #BCBCBC、棕黑 #1A1302、铜橙 #FF661A。浅纸色 #E3E3D9 是演示适配色，金色 #FFB948 用于少量叠层。棕黑背景是对原站前景色的反转扩展，也用于新增图表的深底构图。
- 字体：点阵 Doto 子集内部名 ShiftDots，900，ROND100；无衬线 Instrument Sans 子集内部名 ShiftSans，原有叙事页正文500、标题600，新增图表使用400–600区分轴、数值和标题。中文只使用未来荧黑 SC Wide Heavy 完整字库（PDF 编码修正版，CSS 名 ShiftCJK）；中文标题与正文的规格见 [typography.md](typography.md)。完整 SIL OFL 在 fonts 中并随HTML内嵌。没有复制原站专有 RST Reactor / Plata 字体。
- 圆点同时构成字形、背景和空间图形；只给界面按钮用小圆角/胶囊，避免整套变成圆角卡片集合。
- 少文字页由一个主对象组织一页，配短标题；较多内容按 [content-layout.md](content-layout.md) 另行组织。参考1920画布留边80–100，主标题通常100–180，封面点阵约310；尺寸按字符数量与构图调整，保留底部导航安全区。
- 动效：文字错峰上移、点群组装、空间对象轻微指针倾斜、日程行悬停变色。把原站滚动推进转成换页入场；不用文字反复闪烁或循环计数干扰讲解。
- 鼠标使用可见主体约 23px 的铜橙实心游标，以尖端为热点；移动时保留三颗递减粒点短尾，延续点阵语汇。铜橙背景切换为深色主体，避免同色消失；不叠加系统箭头或大型环形装饰。行为与回退见 [player-contract.md](player-contract.md)。
- SVG/CSS图形为本次原创重绘，没有打包网站照片、Logo或硬币纹理。

## 原有十种构图

| class | 作用 | 组织方式 |
|---|---|---|
| hero | 开场 | 银灰→铜橙地平线、点阵大字、空间点环、两端短说明 |
| manifesto | 观点 | 大句子、一个点阵关键词、圆形强调与留白 |
| beginnings | 三项 | 三个金属质感圆牌+短动词 |
| signal | 聚合关系 | 左点阵标题、右点群从分散到集中 |
| practice | 流程/清单 | 顶部标题与四条细线日程行 |
| constraint | 转场/对照 | 中心点环、两端简短条件 |
| forms | 多种形式 | 叠放纸面与三个图形，标题保持无遮挡 |
| surprise | 停顿/提示 | 暗底圆环负空间、右侧短句 |
| ritual | 一项行动 | 大点阵数+三步短清单；数值需真实含义 |
| closing | 收尾 | 回到暖色渐变、点阵文字和箭头，可用data-restart回首页 |

每个section必须有 `.slide` 和 `data-title`。使用 `data-tone="silver|orange|dark"`，渐变底部暖色时额外指定 `data-nav-tone="warm"`。`.reveal`控制文字错峰，`.sculpture`内的SVG组控制点群显现，`data-tilt`启用指针倾斜。

图形占位 `__TORUS__`、`__ORBIT__`、`__PORTAL__`、`__SIGNAL__`、`__GRID__`、`__CLUSTER__`、`__ARROW__` 从graphics中编译为内联SVG。可新增SVG文件并使用同名占位，或直接写入HTML。

## 编辑边界

工作副本可自由改内容、增删页和设计同语汇新布局。不要改掉已确认的画布内导航/底部操作栏以解决文字拥挤；先重排内容。深浅页的导航必须能辨识。SHIFT 的颜色规则只约束这一套，不应套到未来新样式。

`approved-example.html` 保留早期冻结的验收基准；当前完整 30 页样稿为 `example-en.html` 与 `example-zh.html`。`source/` 是可复用版本：把页码猜色改成明确属性、把标题/下载名改成deck.json元数据，允许增删和调序页面；当前注册的完整示例与源文件一同维护。

## 24 张点阵素材

24 张 SVG 见 `graphics/catalog.json` 和 `artwork-preview.png`。保留原七张点阵图形，新增球面、螺旋、连续环、曲面、桥、联结环、棱面、层叠、折扇、扩散、阶梯、放射、脉冲、透镜、缎带、容器和绽放图形。全部为原创纯矢量，许可在 `source/SHIFT-Artwork-LICENSE.txt` 随 HTML 内嵌；不依赖图片生成服务。

当前 30 页样稿的第 1、6、8、30 页保留原装饰插槽；第 11、12、18、21、24、26、29 页增加小幅点阵插槽，可从底部「替换素材」选择24张图之一。小图按语义分别使用 link、lens、wave、prism、stack、cascade、bloom；每页最多一幅，放在标题右侧或主数值旁的留白区，不覆盖信息图。原默认内联图保持点群动效，小图随页面有限进场。SIGNAL、GRID、CLUSTER 按语义保留为信息图。工具栏遵守共享播放器约定，具体见 [player-contract.md](player-contract.md)。

文字较多的页面由 Agent 在生成时判断配图与布局，见 [content-layout.md](content-layout.md)。中英文样片现各 30 页：保留原有 9 页内容，在收尾前加入 20 页图表与业务布局，第 30 页为原收尾。新增四列卡片、垂直圆柱、水平柱、象形柱、分组柱、100%堆积、瀑布、折线、面积、雷达、桑基、散点、热力、目标进度。详见 [shift-data-layouts.md](shift-data-layouts.md)，含复用生成器及数据验证要求；新稿不固定页数或配图位置。


## 当前30页样稿

原有24页内容全部保留，原收尾移到30；第24–29页为六种新增业务版式。十二套现在均为中英文各30页，共720页。详细页码、能力与复用见 [统一能力清单](layout-coverage.md)。这一扩展为用户要求的新样稿，待本轮审阅；主题本身及原有页面的确认不变。
