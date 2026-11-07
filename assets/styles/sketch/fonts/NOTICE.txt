# SKETCH · 构想 — 英文字体

Fraunces 与 Poppins 均来自 Google Fonts 官方仓库，并以固定提交下载。两者采用 SIL Open Font License 1.1，允许免费商用、嵌入、修改，以及随软件重新分发。随包保留各自版权说明和 OFL；字体继续使用 OFL，不改成项目的 MIT 许可，也不把字体单独出售。两份源 OFL 的版权头均未声明 Reserved Font Name。

| 用途 | CSS 别名 | 文件 | 实际字重 |
|---|---|---|---|
| 大标题 | `SketchSerif` | `FrauncesSoft72-Bold.woff2` | 700 |
| 小标题、素材库标题 | `SketchSerif` | `FrauncesSoft72-SemiBold.woff2` | 600 |
| 正文 | `SketchSans` | `Poppins-Regular.woff2` | 400 |
| 标签、按钮强调 | `SketchSans` | `Poppins-Medium.woff2` | 500 |

Fraunces 实例来自原始可变字体：`SOFT=100`、`WONK=1`、`opsz=72`，分别实例化真实 600/700 字重。柔软圆润的粗衬线用于 SKETCH 标题，没有使用原网站的字体文件。Poppins 使用真正的 Regular/Medium 原始字重，无人工加粗。

四份 WOFF2 保留各自 Google Fonts 原文件的全部 Unicode 映射，未按样稿文字裁剪。Fraunces 为 624 个码位，Poppins 为 471 个码位；这是原始英文字体的完整覆盖，不代表支持中文。原始 TTF 字节、METADATA.pb、OFL.txt 均保存在 `originals/`。

## 固定来源

- Fraunces：Google Fonts 提交 `4024282d9b0cffcdb8e3024560862746178d741f`
  https://github.com/google/fonts/tree/4024282d9b0cffcdb8e3024560862746178d741f/ofl/fraunces
- Poppins：Google Fonts 提交 `8b0a1d0f5983c89bc2b93f1b5fb55f9e252744b5`
  https://github.com/google/fonts/tree/8b0a1d0f5983c89bc2b93f1b5fb55f9e252744b5/ofl/poppins

每个原文件与派生文件的 URL、SHA-256、字节数、字重、转换方式均记录在 `font-manifest.json`；固定提交另外保存在 `source-pins.json`。`Fraunces-OFL.txt` 与 `Poppins-OFL.txt` 是未经编辑的官方许可文本。

## 嵌入约定

分别为 600、700 注册 `SketchSerif`，分别为 400、500 注册 `SketchSans`。使用 `font-synthesis:none`，避免浏览器合成粗体。静态实例已包含上述可变轴配置，无需再设置 `font-variation-settings`。

长标题可以减少字号或手动分行；不要横向压缩字体。

重新处理：使用已安装 fontTools 和 Brotli 的 Python 运行 `prepare_fonts.py`。脚本优先使用已保存的提交锁定文件，保留源字节，并校验输出码位集合与源字体一致。
