# Open Growth Intel

个人开源增长工具集：将海外增长、SEO/GEO 落地页、竞品情报能力抽象为可复用的 Claude Code Skill + Python CLI。

## 能力单元

| Skill | 触发词 | 用途 |
|---|---|---|
| `growth-site` | `/growth-site` | 管理静态增长站点（总览 / 工作记录 / 维护说明） |
| `landing-builder` | `/build-landing` | 基于 A/B/C/Article 模板生成 SEO/GEO 友好落地页 |
| `competitor-report` | `/competitor-report` | 基于公开 URL 生成竞品双周报 + 事件账本 |

## 项目结构

```
open-growth-intel/
├── cli/                   # Python CLI（Typer）
├── skills/                # Claude Code Skill 定义
├── templates/             # Jinja2 页面模板
├── site/                  # 静态管理页面（GitHub Pages）
├── examples/              # Mock 配置与示例输出
├── docs/                  # 文档
├── tests/                 # 测试
├── README.md
├── CLAUDE.md
└── pyproject.toml
```

## 快速开始

```bash
pip install -r cli/requirements.txt
pip install -e .

# 生成落地页
ogi landing build --type a --brand "DemoBrand" --keyword "ai music video generator" --output ./out/page.html

# 生成文章页
ogi landing build --type article --brand "DemoBrand" --title "Top 10 AI Music Video Tools" --output ./out/article.html

# 运行测试
python3 -m unittest discover -s tests -p 'test_*.py'
```

## 当前实现状态

- 已实现：`ogi landing build`
- 已实现页面类型：`a`、`b`、`c`、`article`
- 已实现能力：模板渲染、SEO metadata、`WebApplication` / `FAQPage` / `Article` schema 注入、FAQ 解析、输出目录自动创建
- 尚未接入统一 CLI：`site`、`competitor`
- 保留中的旧工具：`python3 -m cli.page_builder`，当前用于页面清单/竞品抓取实验，不是 `ogi landing build` 的底层入口

## 设计原则

- **无服务器**：全部本地运行 + GitHub Pages 静态托管
- **Skill + CLI 双层**：Skill 负责交互，CLI 负责执行
- **零敏感数据**：所有示例使用 mock 品牌与占位符
- **暗色优先**：`#050b07` + `#9bdc2a`，支持亮暗切换

## 文档

- [Skill 使用指南](docs/skill-guide.md)
- [落地页类型说明](docs/landing-types.md)
- [竞品情报方法论](docs/competitor-methodology.md)
- [站点架构说明](docs/site-architecture.md)
- [敏感数据处理声明](docs/sensitive-data-policy.md)
- [项目总体方案](docs/project-proposal.md)

## 安全扫描

提交前运行：

```bash
grep -riE 'sk-[a-zA-Z0-9]{20,}|sk-ant-|api[_-]?key|password|token|secret' . --exclude-dir=.git
grep -riE '/Users/|/home/|file:///Users/' . --exclude-dir=.git
grep -riE 'ohyesai|freebeat|neuralframes|vidmuse|tunee' . --exclude-dir=.git
```

以上命令必须全部无命中。
