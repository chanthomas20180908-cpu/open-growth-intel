# growth-site Skill

## 触发词

`/growth-site`

## 作用

管理 `site/` 目录下的静态页面，支持工作记录和维护说明的增删改查与本地预览。

## 输入

- `action`: `preview`（默认）| `update` | `status`
- `page`: `index` | `worklog` | `maintenance`
- `entry`: 当 action=update 且 page=worklog/maintenance 时，提供自然语言描述的新条目

## 输出

- 本地浏览器打开对应 HTML 文件
- 更新 `site/data/worklog.json` 或 `site/data/maintenance.json`
- 返回 GitHub Pages 线上链接

## 执行逻辑

1. Skill 解析用户意图，提取 action / page / entry
2. 若需更新，调用 `cli/site.py update --page worklog --entry "..."`
3. CLI 修改 JSON 数据源后重新渲染对应 HTML（Jinja2）
4. 调用本地浏览器打开文件
