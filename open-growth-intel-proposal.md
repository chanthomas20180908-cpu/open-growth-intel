# 海外增长能力抽象开源项目总体方案

## Context

原项目 `/Users/test/code/overseas_growth` 是 OhYesAI 海外出海增长项目，积累了 SEO/GEO 落地页、竞品情报、增长记录中心、关键词分析等能力。目标是将其中**可公开、可复用、低敏感**的部分抽象为个人 GitHub 开源项目，作为面试作品集和长期维护资产。

约束条件：
- 不维护服务器，全部本地运行 + GitHub Pages 静态托管
- 优先做 Claude Code Skill 作为交互入口
- 不做 GPT 登录态自动化
- 采用"一个仓库 + 多个 Skill"的 monorepo 组织形式
- 不迁移原项目原始数据、付费工具导出、内部财务/品牌信息

## Phase 0: Competitive Research Plan（前置调研）

### Objective

在动手实现前，验证 `open-growth-intel` 不是"自嗨"。核心问题：

1. Claude Code 官方是否已经提供重叠能力？
2. 开源社区是否已有 mature 的同类 Skill / CLI？
3. 如果存在，差异点在哪里？是否还值得做？

### Preliminary Findings（快速扫描）

**Claude Code Skill 生态：**
- 官方仓库 `anthropics/skills` 只有通用文档/前端示例，**无专门的增长/SEO/竞品情报 Skill**。
- 社区已有多个 SEO Skill（如 `AgriciDaniel/claude-seo` 9500+ stars、`ChaoticSurfer/seo-skills`），但多为"审计/建议"型，**不生成可部署的静态页面**。
- 竞品情报 Skill 多为广告分析或一次性对比矩阵，**缺乏结构化事件账本 + 时间序列追踪**。
- **未发现** 将 "站点管理 + 落地页生成 + 竞品情报" 串联为统一 monorepo 的项目。

**传统工具生态：**
- 静态站点生成器（Hugo/Astro/Elder.js）很成熟，但**不是 Skill 形态**，也不针对 growth 工作流。
- 竞品监控工具（changedetection.io、Huginn、urlwatch）功能强，但**是通用监控**，不做竞争情报报告结构化。
- 商业工具（SEMrush/Ahrefs/SimilarWeb/Crunchbase）数据聚合能力强，但**付费、闭源、无 Skill 集成**。

**初步结论：** 存在真实差异化空间，但需要用 super-deep 调研做一手验证。

### Methodology: Super-Deep 4-Phase

执行协议参考 [[super_deep_research_protocol.md]]。

| 阶段 | 目标 | 工具 | 产出 |
|---|---|---|---|
| 1. 广度基线 | 建立全网概念地图，发现候选竞品 | WebSearch（多关键词并行） | 候选清单 + 来源表 |
| 2. 深度啃读 | 从官网/GitHub/docs 提取一手信息 | WebFetch / curl / CDP | 结构化事实表 |
| 3. 交叉验证 | 识别数据矛盾，验证声称 | 反向搜索、多源对比 | 矛盾清单 + 可信度评级 |
| 4. 降维整合 | 生成决策报告 | 表格 + 差距矩阵 |  go / no-go / pivot 建议 |

### Research Scope

调研三个能力单元，每个单元找 **官方 + 开源 + 商业** 三类参照：

| 能力单元 | 官方参照 | 开源参照 | 商业参照 |
|---|---|---|---|
| `growth-site` 站点管理 | Claude Code 官方 skills / artifacts | SEO Skill、static site generators | Vercel/Netlify CMS、Notion sites |
| `landing-builder` 落地页 | Claude frontend-design skill | Hugo/Astro pSEO templates、ShipFree | Webflow + Whalesync、Unbounce |
| `competitor-report` 竞品情报 | Claude competitor skills | changedetection.io、Huginn、RSSHub | SEMrush/Ahrefs/SimilarWeb |

### Key Research Questions

1. `growth-site`：是否有 Skill 把"工作记录 + 维护说明 + 部署状态"作为静态站点管理？
2. `landing-builder`：现有 landing page Skill 是否支持 A/B/C/Article 类型模板 + SEO/GEO Schema？
3. `competitor-report`：现有工具能否从公开 URL 生成结构化双周报 + 事件账本？
4. 官方 Anthropic Skills 是否计划覆盖这些领域？
5. 社区最热门的同类项目 stars / installs 多少？活跃度如何？
6. 每个竞品的核心输入输出是什么？与我们的方案对比如何？

### Search Dimensions

每个能力单元至少 4 组独立搜索：

**Claude Code Skill 生态：**
- `"Claude Code Skill" SEO landing page generator`
- `"Claude Code Skill" competitor intelligence report`
- `"Claude Code Skill" static site management worklog`
- `site:github.com "Claude Code" skill SEO`

**开源工具：**
- `open source programmatic SEO landing page generator 2025`
- `open source competitor monitoring sitemap change detection`
- `static site generator growth dashboard worklog`
- `GitHub Pages + Claude Code skill examples`

**商业/官方：**
- `Anthropic skills marketplace growth marketing`
- `Webflow programmatic SEO vs static site generator`
- `SEMrush API free tier competitor report`

### Deliverables

1. **竞品清单表**：每个能力单元 5-10 个候选，含名称、类型、URL、核心功能、输入输出。
2. **核心事实验证表**：关键声称（stars、installs、官方支持状态）的多源验证。
3. **差距矩阵**：我们与每个候选的差异点（功能、形态、成本、集成度）。
4. **决策建议**：
   - **GO**：有清晰差异化，继续按原计划实现
   - **NO-GO**：官方/社区已有成熟方案，停止
   - **PIVOT**：调整能力边界或形态

### Decision Criteria

| 条件 | 结论 |
|---|---|
| 官方 Anthropic 已发布重叠 Skill | 停止对应能力 |
| 开源已有成熟项目且功能完全覆盖 | 停止或明确差异化后 fork/集成 |
| 有重叠但形态不同（CLI vs Skill vs SaaS） | 保留，突出 Skill + CLI + GitHub Pages 的独特组合 |
| 无直接竞品，但需求不存在 | 停止 |
| 无直接竞品，需求真实 | GO |

### Estimated Effort

- 广度基线：30 分钟
- 深度啃读：60 分钟
- 交叉验证：30 分钟
- 降维整合：30 分钟
- **总计约 2.5 小时**

---

## Recommended Approach

建立单一 GitHub 仓库 `open-growth-intel`，内部按能力拆分为 3 个 Skill：

1. `growth-site`：管理页面（index / 工作记录 / 维护说明）的本地预览与更新
2. `landing-builder`：基于模板生成 SEO/GEO 友好的静态落地页
3. `competitor-report`：基于公开信息生成竞品双周报

底层由统一 Python CLI 执行，Skill 仅作为 Claude Code 的触发层。

## Repository Structure

```
open-growth-intel/
├── README.md                          # 项目总览、安装、三个 Skill 演示
├── CLAUDE.md                          # Claude Code / Skill 使用说明
├── pyproject.toml                     # Python 包配置、依赖、CLI 入口
├── .github/
│   └── workflows/
│       └── deploy-site.yml            # GitHub Pages 自动部署 site/ 目录
├── cli/                               # 底层 CLI（所有 Skill 的实际执行层）
│   ├── __init__.py
│   ├── main.py                        # Typer 入口：ogi
│   ├── site.py                        # 管理页面命令
│   ├── landing.py                     # 落地页生成命令
│   └── competitor.py                  # 竞品报告命令
├── skills/                            # Claude Code Skill 定义
│   ├── growth-site/
│   │   ├── skill.yaml                 # Skill 元数据与命令注册
│   │   └── prompt.md                  # Skill 触发后执行的系统提示
│   ├── landing-builder/
│   │   ├── skill.yaml
│   │   └── prompt.md
│   └── competitor-report/
│       ├── skill.yaml
│       └── prompt.md
├── templates/                         # 页面模板（Jinja2）
│   ├── landing/
│   │   ├── type-a/                    # 核心转化页（如 /ai-music-video-generator）
│   │   ├── type-b/                    # 单工具页（如 /tools/band-name-generator）
│   │   ├── type-c/                    # 工具入口页（如 /tools/audio-to-video）
│   │   └── article/                   # 文章页（教程/榜单/对比）
│   └── components/
│       ├── nav.html
│       ├── footer.html
│       ├── faq-schema.html            # FAQPage LD+JSON
│       ├── webapp-schema.html         # WebApplication LD+JSON
│       └── theme-toggle.html
├── site/                              # 静态管理页面（GitHub Pages 源）
│   ├── index.html                     # 项目总览导航
│   ├── worklog.html                   # 工作记录
│   ├── maintenance.html               # 维护说明
│   ├── assets/
│   │   ├── css/
│   │   │   └── main.css               # 设计系统（暗色优先 + 亮暗切换）
│   │   └── js/
│   │       └── theme.js
│   └── data/
│       ├── worklog.json               # 工作记录数据源
│       └── maintenance.json           # 维护说明数据源
├── examples/                          # 示例配置与输出（用于面试 demo）
│   ├── brands.example.yaml
│   ├── competitors.example.yaml
│   ├── prompts.example.csv
│   └── outputs/
│       ├── sample-landing-page.html
│       └── sample-competitor-report.md
├── docs/
│   ├── skill-guide.md                 # Skill 使用指南
│   ├── landing-types.md               # A/B/C 页面类型说明
│   ├── competitor-methodology.md      # 竞品情报方法论
│   └── sensitive-data-policy.md       # 敏感数据处理声明
└── tests/
    ├── test_cli.py
    └── test_skills.py
```

## Skill Specifications

### Skill 1: growth-site

- **触发词**：`/growth-site`
- **作用**：管理 `site/` 目录下的静态页面，支持工作记录和维护说明的增删改查与本地预览
- **输入**（通过对话提供）：
  - `action`: `preview`（默认）| `update` | `status`
  - `page`: `index` | `worklog` | `maintenance`
  - `entry`: 当 action=update 且 page=worklog/maintenance 时，提供自然语言描述的新条目
- **输出**：
  - 本地浏览器打开对应 HTML 文件
  - 更新 `site/data/worklog.json` 或 `site/data/maintenance.json`
  - 返回 GitHub Pages 线上链接
- **执行逻辑**：
  1. Skill 解析用户意图，提取 action / page / entry
  2. 若需更新，调用 `cli/site.py update --page worklog --entry "..."`
  3. CLI 修改 JSON 数据源后重新渲染对应 HTML（Jinja2）
  4. 调用本地浏览器打开文件

### Skill 2: landing-builder

- **触发词**：`/build-landing`
- **作用**：基于 A/B/C/Article 模板生成单个 SEO-ready 静态落地页
- **输入**：
  - `page_type`: `a` | `b` | `c` | `article`（必填）
  - `brand_name`: 品牌名（必填）
  - `primary_keyword`: 主关键词（必填）
  - `output_path`: 输出 HTML 路径（必填）
  - `value_prop`: 一句话价值主张（可选）
  - `faq_items`: FAQ 列表 JSON/YAML（可选）
  - `competitor_url`: 参考竞品 URL（可选，仅用于结构学习，不抓取内容）
- **输出**：
  - 单个 HTML 文件
  - 自动包含 title / meta description / canonical / OG / Twitter Card / Schema
- **执行逻辑**：
  1. 加载 `templates/landing/{page_type}/` 模板
  2. 用 Jinja2 注入 brand_name / primary_keyword / value_prop / faq_items
  3. 组装 nav / footer / faq-schema / webapp-schema 组件
  4. 写入 output_path
  5. 本地浏览器预览

### Skill 3: competitor-report

- **触发词**：`/competitor-report`
- **作用**：基于公开 URL 生成竞品双周报 Markdown + 事件账本 CSV
- **输入**：
  - `config`: `competitors.yaml` 路径（必填）
  - `output_dir`: 报告输出目录（必填）
  - `week`: 周次，默认当前周（可选）
- **输出**：
  - `{week}_competitor_report.md`
  - `{week}_event_ledger.csv`
  - 可选：`{week}_summary.html` 静态摘要
- **执行逻辑**：
  1. 读取 competitors.yaml，获取竞品名称、官网、sitemap、pricing、blog URL
  2. 对每个竞品做轻量公开信息采集（sitemap 条目数、pricing 页文本 hash、blog RSS/最近文章）
  3. 与上一次输出对比，识别变化事件（新页面、定价文案变更、新博客）
  4. 生成结构化事件账本
  5. 按双周报模板生成 Markdown 报告
  6. 不读写数据库，不存储历史快照，只输出文件

## CLI Design

统一入口：`ogi`（Open Growth Intelligence 缩写）

```bash
# 管理页面
ogi site preview --page index
ogi site update --page worklog --entry "完成 homepage v1 设计"

# 落地页生成
ogi landing build --type a --brand "DemoBrand" --keyword "ai music video generator" --output ./out/page.html

# 竞品报告
ogi competitor report --config ./examples/competitors.example.yaml --output-dir ./reports
```

Skill 与 CLI 关系：Skill 是 Claude Code 的交互层，实际调用 CLI 命令执行。用户也可以脱离 Skill 直接使用 CLI。

## Data Flow

```
用户对话
   │
   ▼
Claude Code Skill
   │
   ▼
Skill prompt 解析意图
   │
   ▼
调用 CLI 命令（本地 Python）
   │
   ├── site.py → 修改 JSON → 渲染 HTML
   ├── landing.py → Jinja2 模板 → 输出 HTML
   └── competitor.py → 公开 URL 采集 → CSV + Markdown
   │
   ▼
本地文件系统输出
   │
   ▼
浏览器预览 / GitHub Pages 部署
```

## Sensitive Data Handling

- 不迁移原项目 `/材料/`、`/分析结果/`、真实竞品报告、付费工具导出
- 所有示例数据使用 mock 品牌和占位符
- 删除或替换所有硬编码的本机路径、OhYesAI 品牌名、真实竞品 URL、API Key、数据库配置
- `docs/sensitive-data-policy.md` 明确声明：本仓库不包含原公司数据，不提供绕过平台限制的脚本
- CI 增加敏感信息扫描：禁止提交 password、token、sk-、真实公司品牌

## Dependencies

最小依赖集：
- Python 3.10+
- `typer`：CLI 框架
- `jinja2`：模板渲染
- `requests` + `feedparser`：公开页面采集
- `pyyaml`：YAML 配置解析
- `pytest`：测试

无需数据库、无需服务器、无需付费 API。

## Verification / Test Plan

- 用 mock 品牌跑通 `landing-builder` 完整链路，验证输出 HTML 可离线打开
- 用 `examples/competitors.example.yaml` 跑通 `competitor-report`，验证输出 Markdown 结构正确
- 用示例条目更新 `site/data/worklog.json`，验证 `site/worklog.html` 正确渲染
- 运行敏感信息扫描脚本，确保无 password/token/真实品牌泄漏
- README 提供一键安装和三个 Skill 的演示命令

## Milestones

### Phase 1：仓库骨架（1 周）
- 创建 `open-growth-intel` 仓库
- 搭建 CLI 入口和目录结构
- 实现 `growth-site` Skill + 管理页面
- 编写 README 和 CLAUDE.md

### Phase 2：落地页工具（1 周）
- 抽象 A/B/C/Article 页面模板
- 实现 `landing-builder` Skill
- 提供 2-3 个示例落地页

### Phase 3：竞品报告（1 周）
- 实现 `competitor-report` Skill
- 提供 mock 竞品配置和示例报告
- 配置 GitHub Pages 自动部署

### Phase 4：面试打磨（1 周）
- 完善文档、截图、演示 GIF
- 增加测试和 CI
- 输出项目总结（适合写进简历/面试介绍）
