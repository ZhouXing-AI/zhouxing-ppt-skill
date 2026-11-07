# 中文优先与中英混排

## 模式与文件

- 默认 `--lang auto`，通过 `--prompt` 或 `--prompt-file` 识别本次输入：有汉字用 `zh-CN`，纯英文用 `en`；没有输入时回退中文。用户明确指定输出语言时由 Agent 显式传 `--lang`，优先于检测。
- `--lang en` 复制英文视觉样片（SHIFT、FOCUS、EDIT 各 24 页，其余九套各 10 页），随后按内容调整页数。SHIFT、FOCUS、EDIT、FORM 的中英文模式均内嵌本主题完整中文字体；INDEX、AXIS、SKETCH、GLOW、ECHO、SPARK、BLEND 与 GROVE 英文 HTML 只内嵌西文字体。中文版中，INDEX 加入三种完整中文字库，AXIS、BLEND 与 GROVE 各加入一种，SKETCH、GLOW、ECHO 与 SPARK 各加入两种。离线编辑新汉字应使用含相应中文字体的版本。
- `source/style.css` 是原始样式，`source/locale-zh.css` 的中文调整以 `html:lang(zh)` 为范围。不要为了适配中文修改已确认的英文大字字距。
- `deck.json.lang` 控制排版与菜单语言，`ui_lang` 可单独指定菜单语言（`zh-CN` 或 `en`），前提是已包含对应菜单与字体。更改 lang 不会自动翻译已有页面或增加字库，需同时调整文案、布局和字体配置。
- 中文模板在各主题的 `assets/styles/<id>/locales/zh-CN/`，已确认的 ID 为 `shift`、`focus`、`edit`、`form`、`index`、`axis`、`sketch`、`glow`、`echo`、`spark`、`blend`、`grove`。各主题的中英文示例独立保存，不能用中文稿覆盖英文验收基准。
- INDEX、AXIS、SKETCH、GLOW、ECHO、SPARK、BLEND 与 GROVE 的英文 `source/ui.json` 仅含英文；中文版创建时复制 locale 的双语 `ui.json`，并以 locale 元数据中的完整 `fonts` 数组覆盖英文数组。`source/locale-zh.css` 共存于源目录，但样式仅在 `html:lang(zh)` 生效。要从英文转中文，必须同时采用这些中文配置，不能仅改 `lang` 或 `ui_lang`。

## 字体与覆盖

本 Skill 将开源分发，中文与英文字体都必须从作者或正式发行方核实：免费商业使用、HTML/PDF 嵌入、随开源 Skill 再分发字体文件。仅有“免费商用”宣传或桌面文件夹标签不够。修改、格式转换或子集化前，另查修改许可与保留字体名条款；保留完整版权、许可证、来源和修改说明，字体继续使用自身许可，不能由 Skill 的代码许可证覆盖。未取得再分发依据的字体只作为视觉参考，不打包。

**中文字体按主题选择，不统一固定为未来荧黑。** 新主题由 Agent 根据视觉风格选择许可明确的字体，并用实际中文页面检验字形、字号与可读性；已确认主题按本套配置使用，变更遵循用户本次要求。当前配置：

| 主题 | 中文字体 | 配套英文字体 |
|---|---|---|
| SHIFT · 流变 | 未来荧黑 SC Wide Heavy／`ShiftCJK` | Instrument Sans／`ShiftSans`；点阵短英文与数字用 Doto／`ShiftDots` |
| FOCUS · 明晰 | Noto Serif SC／`FocusCJK`：内容 400、绿底描边标题 500；Noto Sans SC／`FocusCJKSans`：短标签、界面与学习回路 SVG 文字 400 | Instrument Serif／`MoveSerif`、真斜体／`MoveItalic`、Instrument Sans／`ShiftSans` |
| EDIT · 精选 | Noto Serif SC／`EditCJK`：标题 300，深底及红底标题、正文、标签与界面 400 | Instrument Serif／`EditSerif`、真斜体／`EditItalic`、Instrument Sans／`ShiftSans` |
| FORM · 成形 | 朱雀仿宋 Regular／`FormCJK` | Marcellus Regular／`FormDisplay`、Instrument Sans／`ShiftSans` |
| INDEX · 索引 | 未来荧黑 SC Compressed ExtraBold／`IndexCJKDisplay`：主标题 800；Noto Sans SC／`IndexCJK`：正文与界面 400；Noto Serif SC／`IndexCJKSerif`：标签 400 | Anton 400／`IndexDisplay`；Newsreader 400／`IndexSerif`；IBM Plex Mono 400／500／`IndexMono` |
| AXIS · 轴线 | Noto Sans SC／`AxisCJK`：标题 500，正文、标签与界面 400 | Instrument Sans／`AxisSans`；IBM Plex Mono Regular／`AxisMono` |
| SKETCH · 构想 | 狮尾四季春加糖 SC Black／`SketchCJKDisplay`：标题 900；霞鹜文楷 GB Regular／`SketchCJK`：正文、标签及界面 400 | Fraunces Soft 72／`SketchSerif` 600/700；Poppins／`SketchSans` 400/500 |
| GLOW · 晴光 | Noto Serif SC 900／`GlowCJKDisplay`：标题；Noto Sans SC 400／`GlowCJK`：正文与界面 | DM Serif Display 400／`GlowDisplay`、真 Italic 400／`GlowItalic`；Poppins 400/500／`GlowSans` |
| ECHO · 回响 | Noto Serif SC 300／`EchoCJKDisplay`：标题；Noto Sans SC 400／`EchoCJK`：正文与界面 | Cormorant Garamond 500／`EchoDisplay`；Instrument Sans 400/500／`EchoSans` |
| SPARK · 燃点 | 得意黑 Smiley Sans Oblique 400／`SparkCJKDisplay`：原生斜体标题；Noto Sans SC 400／`SparkCJK`：正文与界面 | Barlow Condensed 800／`SparkDisplay`；Manrope 400/500／`SparkSans` |
| BLEND · 融合 | Noto Sans SC／`BlendCJK`：标题 500，正文与界面 400 | Space Grotesk 400/500/600／`BlendSans`；DM Mono Regular 400／`BlendMono`：小型英文索引与数字 |
| GROVE · 共生 | 寒蝉半圆体 ChillRoundM Regular／`GroveCJK`：标题、正文与界面均为 400 | Onest 400/500／`GroveSans`；DM Mono Regular 400／`GroveMono`：小型英文索引与数字 |

所有字体的 OFL 许可与必要来源、修改说明随字体及成品 HTML 保存。字体详情以对应主题 `fonts/` 中的 notice 与 coverage 文件为准。

- **SHIFT 的未来荧黑**保留 0.91 版全部 31,808 个码点与原轮廓；为 PDF 正确复制汉字，将 427 个共享映射复制成独立字形，内部名称改为 ShiftGlowWideHeavy，未做子集或视觉改形。版权、来源与修改记录见 `GlowSans-NOTICE.txt`，开发期重建脚本见 `scripts/prepare_glow_font.py`。这是单一 Heavy 字重；标题、正文、菜单中的汉字通过字号、间距、颜色区分层级，不合成细体或加粗。CSS 字重范围只将既有排版字重映射到同一个真实字形。
- **FOCUS 的宋体与黑体**使用 Google Fonts 官方固定提交 `24ddc1f324cac5d9f5aedca126d298f56e3f1640` 的完整 Noto Serif SC 与 Noto Sans SC，无损 WOFF2 分别保留 30,928、30,890 个 Unicode cmap 码点，真实可变字重范围为 200–900、100–900。内容宋体用 400，绿底 `.outline` 标题用 500，短标签、界面和学习回路 SVG 文字用黑体 400；不裁字、不改轮廓、字宽或内部名称。`FocusCJK`、`FocusCJKSans` 为 CSS 别名，随包保留 `NOTICE-zh.txt`、两个 Noto OFL、`font-audit-zh.json` 及两个 `FocusCJK*-coverage.json`。两版均内嵌这两套完整字库，按 OFL 1.1 可免费商用、嵌入及再分发，版权与许可随字体保留。
- **FOCUS 的新增图表页**保持衬线标题与无衬线读数分工：主标题用 `MoveSerif`／`FocusCJK` 400，数轴、标签、图例与数值用 `ShiftSans`／`FocusCJKSans` 400。小数轴不使用衬线真斜体；同一单位/数值不随意拆行，中文按内容独立排版。二十四页模式仍保留原完整字库及许可，不为新增示例裁出另一份子集。
- **EDIT 的 Noto Serif SC**使用 Google Fonts 官方固定提交 `24ddc1f324cac5d9f5aedca126d298f56e3f1640` 的完整字库，保留 30,928 个 Unicode cmap 码点和真实 200–900 可变字重。`EditCJK` 只是 CSS 别名，WOFF2 仅作无损容器压缩，未裁字、改轮廓、字宽或内部名称。大标题用 300，正文、标签、界面及深底／红底标题用 400，设置 `font-synthesis:none`。随包保留 `NotoSerifSC-OFL.txt`、`NotoSerifSC-NOTICE.txt`、`font-audit-zh.json` 与 `EditCJK-coverage.json`；按 OFL 1.1 可免费商用、嵌入及再分发，版权与许可随字体保留。
- **FORM 的朱雀仿宋**使用官方 v0.212 完整原版 TTF，保留 12,882 个码点和内部字体名 `Zhuque Fangsong (technical preview)`；`FormCJK` 仅为 CSS 别名。真实字重为 400，使用 `font-synthesis:none`，不伪加粗、不子集化。官方版权、OFL 及其西文来源 Alegreya 的声明分别保存在 `Zhuque-OFL.txt`、`Alegreya-OFL.txt` 和 `Zhuque-NOTICE.txt`。中文版本不改动已确认的 Marcellus 英文设计。
- **INDEX 的窄高中文主标题**使用[未来荧黑官方 v0.93](https://github.com/welai/glow-sans/releases/tag/v0.93) 的 Glow Sans SC Compressed ExtraBold（未来荧黑 SC 压缩特粗），CSS 别名为 `IndexCJKDisplay`，真实字重 800。完整原版 OTF 转为 `IndexCJKDisplay.woff2` 容器压缩，保留 32,227 个 Unicode cmap 码点、32,094 个字形及原有内部名称、轮廓和字宽；标准编码器移除了不含签名的空 DSIG 占位表。没有子集化、改字形或 CSS 横向压缩；代表汉字字宽为 800/1000 em，直接使用字体原生窄高比例。字体与[官方 OFL 1.1](https://raw.githubusercontent.com/welai/glow-sans/v0.93/OFL.txt) 一起分发，保留 `GlowSansCompressed-OFL.txt`、`GlowSansCompressed-NOTICE.txt`、`font-audit-condensed.json` 和 `IndexCJKDisplay-coverage.json`，转换详情与哈希以审计为准。
- **INDEX 的正文与标签**继续使用 Google Fonts 官方固定提交 `24ddc1f324cac5d9f5aedca126d298f56e3f1640` 的完整 Noto Sans SC 与 Noto Serif SC，WOFF2 分别保留 30,890、30,928 个 Unicode cmap 码点；没有按样稿裁字、改轮廓或改内部字体名。真实可变字重范围分别为 100–900、200–900，正文与界面黑体 400，图库标题可用黑体 900，宋体标签 400；三种中文字体均设置 `font-synthesis:none`。原有 `NOTICE.txt`、`NOTICE-zh.txt`、`font-audit.json`、`font-audit-zh.json` 与两个 Noto coverage 文件继续保留；加上主标题字体，INDEX 共保留六份完整 OFL 和三个 `IndexCJK*-coverage.json`。配套西文 TTF 为官方原始字节；CSS 别名不改变字体许可。字体按随包 OFL 可免费商业使用、嵌入和再分发，声明与字体一起保留。

- **AXIS 的 Noto Sans SC**复用 INDEX 已核验的完整 WOFF2 原字节，CSS 别名 `AxisCJK`，保留 30,890 个 Unicode cmap 码点、31,036 个字形和真实 100–900 字重。标题 500、正文与界面 400；不伪加粗、不压缩字宽。随包保留 `NotoSansSC-OFL.txt`、`NOTICE-zh.txt`、`font-audit-zh.json` 与 `AxisCJK-coverage.json`。西文保持已确认的 Instrument Sans Latin 子集和原版 IBM Plex Mono，来源、修改记录及实际覆盖在 `NOTICE.txt`、`font-manifest.json` 中；英文版不加载中文字库。

- **SKETCH 的中文配对**使用狮尾四季春加糖 SC Black 的真实 900 字重，配霞鹜文楷 GB Regular 的真实 400 字重；厚实简化衬线承接英文 Fraunces 的大字张力，手写正文对应纸张与细线。只用字体发行方明确允许商用、嵌入与再分发的 OFL 字库，完整文件、固定来源、转换记录、SHA 与 cmap 见本套 `fonts/`。`SketchCJKDisplay` 与 `SketchCJK` 为 CSS 别名；中文标题使用独立断行、正常字距和 `font-synthesis:none`。英文单文件不载入中文字库，中文单文件内嵌两种完整中文字库。

- **GLOW 的复古字形**使用完整 Noto Serif SC 900（标题）与 Noto Sans SC 400（正文/界面），不伪加粗或压缩字宽。英文 DM Serif Display 只有真实 400，正体与真 Italic 独立内嵌；`GlowItalic` 的 font-face 和 CSS 都声明 italic，使用 `font-synthesis:none`，中文强调恢复 normal。完整来源、覆盖、固定版本、OFL 与 SHA 位于本套 `fonts/font-manifest.json`、`NOTICE.txt`，中文字体复用此前核实的完整 WOFF2 原字节。

- **ECHO 的疏朗字形**使用完整 Cormorant Garamond 500 与 Instrument Sans 400/500 原始变量 TTF，中文使用完整 Noto Serif SC 300、Noto Sans SC 400 无损 WOFF2。真实字重、完整 cmap、内部名称与 fsType=0 已核验；固定官方版本、完整 OFL 和 SHA 位于本套 `fonts/`。不使用旧主题的拉丁子集，不合成粗体或斜体，中文按完整短句断行。

- **SPARK 的紧凑字形**使用完整 Barlow Condensed ExtraBold 800 与 Manrope 400/500。中文标题为[得意黑官方 v2.0.1](https://github.com/atelier-anchor/smiley-sans/releases/tag/v2.0.1) 完整原版 `SmileySans-Oblique.woff2`，真实字重 400、原生倾斜约 8°，保留全部 9,440 个 Unicode cmap 码点。`SparkCJKDisplay` 的字体元数据与标题 CSS 都指定 `style: italic`／`font-style:italic`，使用 `font-synthesis:none`；这会选择字体自身的倾斜字形，不再用 CSS 斜切、压窄或伪加粗。正文与界面为完整 Noto Sans SC 400（30,890 个码点），恢复 normal。得意黑原始 `fsType=8`（Editable Embedding），与其他本套字体的 `fsType=0` 区分记录，未篡改权限位；结合随包 OFL 1.1，可免费商用、嵌入与开源再分发。完整版权、保留字体名称、官方 release 证据、固定提交、SHA 与真实 cmap 见本套 `fonts/`；保留原始字节和声明，不按样稿裁字。

- **BLEND 的几何字形**使用完整 Space Grotesk 变量 TTF（真实范围 300–700，本套使用 400/500/600）与完整 DM Mono Regular TTF（真实 400）。中文使用完整 Noto Sans SC 无损 WOFF2（真实范围 100–900），标题 500、正文和界面 400；三套字体均为正体、`fsType=0`，使用 `font-synthesis:none`。保留 735、381、30,890 个 Unicode cmap 码点，固定 Google Fonts 官方提交、完整 OFL、原始版权、SHA、覆盖与转换记录位于本套 `fonts/`。`BlendSans`、`BlendMono`、`BlendCJK` 只是 CSS 别名，不改变内部字体名称；中文单独断行，不压缩比例。小索引用 DM Mono，汉字转由 `BlendCJK` 显示，不使用原站 DieGrotesk 或 ABCDiatype。

- **GROVE 的圆润字形**使用完整官方 Onest 变量 TTF（真实范围 100–900，本套使用 400/500）与 DM Mono Regular TTF（400）。中文使用[寒蝉半圆体官方 v1.805](https://github.com/Warren2060/ChillRound/releases/tag/v1.805) 的完整原版 OTF，真实单一字重 400，保留 12,329 个 Unicode cmap 码点和 12,779 个字形，GB2312 的 6,763 汉字全部覆盖；标题、正文与界面均用 400，不伪造 Medium 或 Bold。三字体均为正体、`fsType=0`、OFL 1.1，设置 `font-synthesis:none`；字重轻重由真实字族配置决定，中文层级由字号、间距与位置建立。字体文件保持官方原字节，不裁字、不改内部名称；`GroveSans`、`GroveMono`、`GroveCJK` 仅为 CSS 别名。完整许可、保留字体名、固定官方提交、release/tag 证据、SHA 与覆盖见本套 `fonts/`。英文 HTML 不加载中文字库，中文额外内嵌完整寒蝉半圆体；不用未核实的“源泉 SC”名称代替实际字库。

中文字体不按样稿文本裁剪：更换普通中文文案、浏览器编辑新汉字时仍能离线使用。完整字库也不保证所有生僻字、扩展汉字或其他语言都覆盖。未来荧黑 SC 采用简体中文地区字形；繁体中文若是交付目标，应检查所选字体的地区字形与实际用字覆盖，再选择对应版本。

构建器使用由最终字体真实 cmap 导出的 coverage ranges 检查汉字，并校验覆盖文件中的 font_sha256 与字体一致。遇缺字，补充许可明确且包含该字的字体及覆盖文件，再检查渲染；不要用系统字体静默兜底交付。字体需要更小体积时，可在单份交付中另作子集方案，但必须说明浏览器后续编辑新字符的限制，不能删掉 Skill 的完整源字库。

## 排版判断

- 中文主标题独立设计；以完整短句和清楚的换行为重点。不要把汉字直接塞进 `.dot`，也不要沿用英文 `-30px` 等紧字距。
- 正文的中文、英文与数字使用同一文本行和字号。SHIFT 沿用 `'ShiftSans','ShiftCJK',sans-serif`；FOCUS 中文内容用 `FocusCJK` 400，绿底描边标题用 500，短标签、界面和学习回路 SVG 文字用 `FocusCJKSans` 400，西文仍由 `MoveSerif`、`MoveItalic`、`ShiftSans` 分工，中文 `em` 不伪斜体；EDIT 中文内容用 `'EditCJK','EditSerif',serif`，界面用 `'ShiftSans','EditCJK',sans-serif`，正文与界面为真实 400 字重；FORM 中文正文沿用 `'FormCJK','ShiftSans',sans-serif`；INDEX 中文正文与界面沿用 `'IndexMono','IndexCJK',sans-serif`，衬线标签沿用 `'IndexSerif','IndexCJKSerif',serif`。INDEX 中文 `h1`、`h2` 使用 `'IndexDisplay','IndexCJKDisplay','IndexCJK',sans-serif`，字重设为 800，按原生窄高字形调整标题字号与行高，保留页面构图及文案。AXIS 中文内容使用 `AxisSans,AxisCJK,sans-serif`，数字索引用 `AxisMono,AxisCJK,monospace`，中文标题独立设 500 字重与正常字距。英文页面使用本套既有字族顺序。标题按真实字体字重和构图控制行长；中文接近正常字距，可随大字号构图小幅调整；正文行高通常 1.55–1.7。
- 数字、短缩写及英文关键词可以保留点阵字，但只是辅助信息。大段中文不需要搭配重复的英文译文来装饰。
- 引号、括号、逗号、句号应遵循中文断行；CSS 使用 `line-break: strict`，英文词避免任意拆字。必要的术语/数值单位组合用短 `.keep` 元素保持一行，不能给整段文字强制不换行。
- 保留底部导航安全区。中文比英文更密时，先改叙事、短句和布局，不能单纯缩小整页字体。

## 验证

中文稿逐页检查汉字缺字、句读、标点落位、主标题与图形关系。混排至少看短英文术语、数字百分比与中文单位同一行的表现；检查实际字体加载，不以 CSS 中写了字体名作为成功依据。

用输入法编辑时，组合输入不能触发翻页或退出编辑。保存 HTML 后离线重开，确认新汉字与菜单仍正常。下载的 PDF 按实际页数检查独立分页、中文画面完整以及导航/操作栏被隐藏；该下载功能是高清画面 PDF，不包含可选择的文字层。
