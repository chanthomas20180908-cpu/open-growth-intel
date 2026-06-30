# 落地页类型说明

## Type A — 核心转化页

- **用途**：高搜索量核心关键词，承担主要转化任务。
- **结构**：Hero + 价值主张 + 功能网格 + FAQ + CTA
- **示例关键词**：`ai music video generator`、`ai video generator`
- **模板**：`templates/landing/type-a/base.html`

## Type B — 单工具页

- **用途**：具体工具关键词，用户意图明确。
- **结构**：工具入口 + 交互演示 + 使用步骤 + 相关工具
- **示例关键词**：`band name generator`、`rap lyrics generator`
- **模板**：`templates/landing/type-b/base.html`

## Type C — 工具入口/Hub 页

- **用途**：聚合多个工具或子页面的入口。
- **结构**：指标卡 + entry-card 网格 + 子页面导航
- **示例关键词**：`audio to video`、`ai music tools`
- **模板**：`templates/landing/type-c/base.html`

## Article — 文章页

- **用途**：教程、榜单、对比类内容，获取信息型流量。
- **结构**：面包屑 + 标题 + 元信息 + 正文 + 相关推荐
- **示例标题**：`Top 10 AI Music Video Tools`、`How to Make a Lyric Video with AI`
- **模板**：`templates/landing/article/base.html`

## Schema 要求

- Type A/B/C 工具页：必须包含 `WebApplication` LD+JSON。
- 所有含 FAQ 的页面：必须包含 `FAQPage` LD+JSON。
- Article 页：必须包含 `Article` LD+JSON。

## 当前 CLI 输入约束

- 公共必填参数：`--type`、`--brand`、`--output`
- Type A/B/C：额外必填 `--keyword`
- Article：额外必填 `--title`
- 可选参数：`--value-prop`、`--faq-items`
- `--faq-items` 可传 JSON/YAML 字符串，或指向本地 JSON/YAML 文件

## 当前输出约束

- 生成结果是单个 HTML 文件
- 输出目录不存在时自动创建
- HTML 必含 `title`、`meta description`、`canonical`、`og:*`、`twitter:card`
- 渲染结果不得残留未展开的 `{{ ... }}` 模板占位符

## 设计系统

- 暗色优先：`#050b07` 背景 + `#9bdc2a` accent
- 亮暗切换：通过 `data-theme="light"` 覆盖 CSS 变量
- 字体：`JetBrains Mono` + system mono/sans fallback
