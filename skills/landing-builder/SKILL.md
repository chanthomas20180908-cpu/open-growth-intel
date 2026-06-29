# landing-builder Skill

## 触发词

`/build-landing`

## 作用

基于 A/B/C/Article 模板生成单个 SEO-ready 静态落地页。

## 输入

- `page_type`: `a` | `b` | `c` | `article`（必填）
- `brand_name`: 品牌名（必填）
- `primary_keyword`: 主关键词（必填）
- `output_path`: 输出 HTML 路径（必填）
- `value_prop`: 一句话价值主张（可选）
- `faq_items`: FAQ 列表 JSON/YAML（可选）
- `competitor_url`: 参考竞品 URL（可选，仅用于结构学习，不抓取内容）

## 输出

- 单个 HTML 文件
- 自动包含 title / meta description / canonical / OG / Twitter Card / Schema

## 执行逻辑

1. 加载 `templates/landing/{page_type}/` 模板
2. 用 Jinja2 注入 brand_name / primary_keyword / value_prop / faq_items
3. 组装 nav / footer / faq-schema / webapp-schema 组件
4. 写入 output_path
5. 本地浏览器预览
