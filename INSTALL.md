# 安装与 Agent 适配 / Installation and agent compatibility

## 中文

用户只需复制 [README 的安装提示词](README.md#复制提示词安装)。下面是接收提示词的 Agent 执行安装时使用的说明。

### 按宿主能力安装

本仓库是包含 `SKILL.md`、Python 脚本和素材的完整技能目录。安装目标是当前客户端的技能加载器，不是某个模型的名称。不要把一种客户端的路径套用到所有 Agent。

| Agent / 客户端 | 安装时的处理 |
| --- | --- |
| Codex | 使用当前环境的技能安装器或已配置的技能搜索目录；确认技能列表能发现 `zhouxing-ppt-skill`。 |
| Claude Code | 支持个人级 `~/.claude/skills/zhouxing-ppt-skill/` 或项目级 `.claude/skills/zhouxing-ppt-skill/`；按安装范围选择。 |
| WorkBuddy | 使用客户端的本地技能包导入入口，或当前版本实际识别的技能目录；检查导入结果及启用状态。 |
| DeepSeek Harness | 检查当前运行环境的技能加载插件及配置，再注册完整目录；不要假定与 Claude Code 的目录相同。 |
| 豆包、豆包工作 | 检查当前客户端是否提供技能导入、文件操作和脚本执行；有入口则按其格式安装，缺少能力时给出该客户端的导入步骤。 |
| Grok Bot | 先确认具体 Bot 的宿主与工具能力，再选择其技能目录或导入接口；模型名称本身不能确定安装位置。 |
| Cursor 及其他 Agent | 使用当前客户端支持的 Agent Skills 目录或导入器；无原生技能加载器但有文件和执行工具时，可作为工作目录读取 SKILL.md 并运行，标明是工作目录使用。 |

以上是适配策略，不是所有客户端版本的实机认证。客户端升级、企业策略和云端沙箱可能改变安装入口与持久性；以本次环境的实际检查为准。

### 获取完整包

- 优先使用宿主自带的技能安装器，来源为 `https://github.com/ZhouXing-AI/zhouxing-ppt-skill`，仓库根目录就是技能根目录。
- 有 Git 时可将 `main` 浅克隆到目标目录：`git clone --depth 1 https://github.com/ZhouXing-AI/zhouxing-ppt-skill.git <目标目录>/zhouxing-ppt-skill`。把占位路径替换为已确认的实际目录，并按当前 shell 引用路径。读取这个公开仓库不需要用户提供 GitHub 令牌。
- 没有 Git 时可下载 [main ZIP](https://github.com/ZhouXing-AI/zhouxing-ppt-skill/archive/refs/heads/main.zip)。解压后将外层目录重命名为 `zhouxing-ppt-skill`；导入器如要求 ZIP，以此单一目录重新打包，使 `zhouxing-ppt-skill/SKILL.md` 存在，不要多嵌套一层仓库目录。不包含 `.git`。
- 保留整个技能内容，尤其是 `assets/` 中的中英文模板、字体、SVG 及许可证。包包含预览与离线字体，下载可能较大；不能因下载慢就只取 SKILL.md 并声称安装完成。
- 目标目录存在时先检查来源和本地修改；可快进更新无修改的同源 Git 副本，有修改则保留或另存新副本。不要删除现有用户作品。
- 自动化无法操作导入器时，提供准备好的包及该客户端的最短导入步骤；缺少 Python 3 时明确说明生成能力尚未就绪。不要为完成安装而改动无关设置。

### 检查与交付

1. 确认 `SKILL.md` 和 `styles.json` 的版本为 `1.0.0`。当前版本名称不代表必须存在同名 Git 标签；以 `main` 的实际文件为准，并记录提交号。
2. 读取 `styles.json`：顺序应为 BLEND、GROVE、SPARK、ECHO、GLOW、SKETCH、AXIS、INDEX、FORM、LENS、FOCUS、EDIT。逐套检查登记的 `artwork_catalog` 含 24 条素材且文件存在；检查英文 `source/`、中文 `locales/zh-CN/`、字体及许可。主题范围以 styles.json 中登记的 12 套为准。
3. 检测可运行的 Python 3（`python3`、`python` 或 `py -3`）。创建/编译入口只依赖标准库，无需安装 Node、浏览器自动化或额外 Python 包。
4. 在技能根目录执行下例，将路径替换为独立临时目录下尚不存在的输出目录；中文版也应可使用 `--lang zh-CN` 创建。脚本使用 UTF-8 读写文件。

   ```sh
   python3 scripts/create_deck.py --style blend --lang en --out "<新的临时输出目录>"
   python3 scripts/build_deck.py --project "<新的临时输出目录>"
   ```

5. 确认生成的 `index.html` 存在并含页面内容；有浏览器工具时打开检查。再单独检查宿主能否发现并调用技能。若需要重新加载技能或开启新会话，请明确告诉用户，不能将“文件下载完成”等同于“技能已启用”。
6. 报告版本、实际位置、安装范围（个人 / 项目 / 临时沙箱）、实际完成的验证与调用方式。纯聊天端只读网页不能完成持久安装；提供可用入口，不误报成功。

## English

Copy the [installation prompt](README.en.md#copy-the-installation-prompt) into your agent. Install the complete repository using the current client's skill installer or discovered skill directory. This is a portable `SKILL.md` bundle with Python scripts and assets, not a client-specific plugin.

- **Codex:** use the installed skill installer or configured skill discovery directories; verify discovery.
- **Claude Code:** choose personal `~/.claude/skills/zhouxing-ppt-skill/` or project `.claude/skills/zhouxing-ppt-skill/` scope.
- **WorkBuddy:** use local skill-package import or the skill directory recognized by the current client; verify enablement.
- **DeepSeek Harness:** inspect the active skill-loading plugin and configuration; register the complete directory using that mechanism.
- **Doubao / Doubao Work:** inspect the current client's import, file, and execution capabilities. Use supported installation or provide the shortest manual import steps.
- **Grok Bot:** identify the actual bot host and available tools before choosing its directory or import interface.
- **Cursor / other agents:** use their supported skill mechanism. If only workspace file execution is available, load SKILL.md explicitly and label this as workspace use, not native installation.

These are capability-based integration strategies, not certification of every client version. Do not invent paths or claim persistent installation in a temporary chat sandbox.

Prefer the host's installer. Otherwise shallow-clone the public repository's `main` branch into a new `zhouxing-ppt-skill` directory, or download the [main ZIP](https://github.com/ZhouXing-AI/zhouxing-ppt-skill/archive/refs/heads/main.zip). For package import, place SKILL.md directly inside the single top-level `zhouxing-ppt-skill/` folder. Preserve scripts, references, templates, fonts, SVGs, and licenses; exclude `.git`. Preserve existing local edits and user presentations. Reading this public repository requires no GitHub token.

Verify version **1.0.0**, the 12 registered themes in the documented order, 24 catalog assets per theme with existing files, both language templates, fonts, and licenses. The supported theme set is defined by the 12 entries in styles.json. Use the files on `main` and record the commit; do not assume a release tag exists.

Detect Python 3 (`python3`, `python`, or `py -3`). The creation and build entrypoints use only its standard library and explicit UTF-8 file I/O. Run `scripts/create_deck.py` and `scripts/build_deck.py` from the skill root, with a new temporary output directory; the commands above demonstrate the English build, and `--lang zh-CN` selects Chinese. Verify the resulting index.html, and separately confirm skill discovery in the host. Report the actual location, version, scope, completed checks, invocation method, and any reload or manual import still needed. A chat-only client without file or execution tools cannot complete this installation merely by reading the repository.

## 官方参考 / Official references

Installation behavior depends on the installed client version; consult its current documentation when resolving a host-specific mechanism.

- [OpenAI: Skills](https://developers.openai.com/plugins/concepts/skills)
- [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [WorkBuddy: Skills](https://www.workbuddy.ai/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills)
- [DeepSeek Harness](https://deepseek.com/en/harness/)
