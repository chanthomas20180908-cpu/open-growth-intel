# 站点架构说明

## 1. 设计目标

- **零构建步骤**：纯静态 HTML/CSS/JS，可直接用浏览器打开。
- **本地优先**：数据源为 JSON 文件，不依赖数据库或服务器。
- **GitHub Pages 托管**：`site/` 目录即为站点根目录。
- **亮暗主题切换**：全站统一 `data-theme` 属性，持久化到 `localStorage`。

## 2. 页面类型

| 类型 | 用途 | 代表文件 |
|---|---|---|
| Meta | 项目总览、工作记录、维护说明 | `site/index.html` / `worklog.html` / `maintenance.html` |
| Type A | 核心转化页 | `templates/landing/type-a/base.html` |
| Type B | 单工具页 | `templates/landing/type-b/base.html` |
| Type C | 工具入口/Hub 页 | `templates/landing/type-c/base.html` |
| Article | 教程/榜单/对比文章 | `templates/landing/article/base.html` |

## 3. 数据层

- **管理页**：`site/data/*.json` 为数据源，CLI 更新后重新渲染 HTML。
- **落地页**：通过 Jinja2 模板直接注入变量生成 HTML。
- **工作记录**：浏览器端解析 JSON 并渲染 timeline，支持搜索/筛选。

## 4. 样式系统

- 暗色优先，默认背景 `#050b07`，主 accent `#9bdc2a`。
- CSS 变量集中在 `:root` 与 `[data-theme="light"]`。
- `site/assets/css/main.css` 为 Meta 页设计系统。
- 落地页模板保留各自页面样式，确保独立可用。

## 5. 导航规范

- 所有页面顶部固定 3 项导航：总览、工作记录、维护说明。
- Hub/子页使用 `.page-nav` pill 按钮风格。
- Meta 页使用 `.nav-links` 胶囊风格。

## 6. HTML 属性引号规范

- `class / style / href / src / id / target / rel` 等属性必须使用英文半角 `"..."`。
- 中文弯引号只能出现在正文文案中。
- 修改后必须运行：

```bash
rg -n 'class=[""]|style=[""]|href=[""]|src=[""]|id=[""]|target=[""]|rel=[""]' 文件路径
```

## 7. 更新流程

1. 修改 `site/data/*.json` 或通过 CLI 更新。
2. 重新渲染对应 HTML。
3. 同步 `site/index.html` 统计数字。
4. 本地浏览器验证。
5. 运行敏感信息扫描。
