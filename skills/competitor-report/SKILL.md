# competitor-report Skill

## 触发词

`/competitor-report`

## 作用

基于公开 URL 生成竞品双周报 Markdown + 事件账本 CSV。

## 输入

- `config`: `competitors.yaml` 路径（必填）
- `output_dir`: 报告输出目录（必填）
- `week`: 周次，默认当前周（可选）

## 输出

- `{week}_competitor_report.md`
- `{week}_event_ledger.csv`
- 可选：`{week}_summary.html` 静态摘要

## 执行逻辑

1. 读取 competitors.yaml，获取竞品名称、官网、sitemap、pricing、blog URL
2. 对每个竞品做轻量公开信息采集（sitemap 条目数、pricing 页文本 hash、blog RSS/最近文章）
3. 与上一次输出对比，识别变化事件（新页面、定价文案变更、新博客）
4. 生成结构化事件账本
5. 按双周报模板生成 Markdown 报告
6. 不读写数据库，不存储历史快照，只输出文件

## 规则

- 只使用公开 URL，不抓取登录内容
- 不使用付费 API
- 事实边界清晰，未确认项明确标注
- 连续两次运行确认后才写入正式事件
