# Skill 使用指南

## 1. growth-site

**触发词**：`/growth-site`

管理 `site/` 目录下的静态页面。

当前仓库仅保留该 Skill 定义与静态页面资产，统一 CLI 尚未实现对应子命令。

## 2. landing-builder

**触发词**：`/build-landing`

基于模板生成 SEO-ready 落地页。

```
/build-landing --type a --brand "DemoBrand" --keyword "ai music video generator" --output ./out/page.html
/build-landing --type b --brand "DemoBrand" --keyword "band name generator" --output ./out/tool.html
/build-landing --type c --brand "DemoBrand" --keyword "ai music tools" --output ./out/hub.html
/build-landing --type article --brand "DemoBrand" --title "Top 10 AI Music Video Tools" --output ./out/article.html
/build-landing --type a --brand "DemoBrand" --keyword "ai music video generator" --faq-items '[{"question":"What is this?","answer":"A generated page."}]' --output ./out/page.html
```

当前实现约束：

- `--type` 必须是 `a | b | c | article`
- Type A/B/C 必填 `--keyword`
- Article 必填 `--title`
- `--faq-items` 支持 JSON/YAML 字符串或文件路径
- 输出 HTML 自动包含 SEO metadata 与页面类型对应的 schema

## 3. competitor-report

**触发词**：`/competitor-report`

基于公开信息生成竞品双周报。

当前仓库仅保留该 Skill 定义与方法论文档，统一 CLI 尚未实现对应子命令。

## CLI 直接调用

所有 Skill 底层均调用 `ogi` CLI：

```bash
# 落地页
ogi landing build --type a --brand "DemoBrand" --keyword "..." --output ./out/page.html
ogi landing build --type article --brand "DemoBrand" --title "..." --output ./out/article.html

# 兼容测试
python3 -m unittest discover -s tests -p 'test_*.py'
```

## 安装

```bash
pip install -r cli/requirements.txt
pip install -e .
```
