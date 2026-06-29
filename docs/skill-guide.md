# Skill 使用指南

## 1. growth-site

**触发词**：`/growth-site`

管理 `site/` 目录下的静态页面。

```
/growth-site preview index
/growth-site update worklog --entry "完成 homepage v1 设计"
/growth-site status
```

## 2. landing-builder

**触发词**：`/build-landing`

基于模板生成 SEO-ready 落地页。

```
/build-landing --type a --brand "DemoBrand" --keyword "ai music video generator" --output ./out/page.html
/build-landing --type b --brand "DemoBrand" --keyword "band name generator" --output ./out/tool.html
/build-landing --type article --brand "DemoBrand" --title "Top 10 AI Music Video Tools" --output ./out/article.html
```

## 3. competitor-report

**触发词**：`/competitor-report`

基于公开信息生成竞品双周报。

```
/competitor-report --config ./examples/competitors.example.yaml --output-dir ./reports --week 2026-W26
```

## CLI 直接调用

所有 Skill 底层均调用 `ogi` CLI：

```bash
# 站点
ogi site preview --page index
ogi site update --page worklog --entry "..."

# 落地页
ogi landing build --type a --brand "DemoBrand" --keyword "..." --output ./out/page.html

# 竞品报告
ogi competitor report --config ./examples/competitors.example.yaml --output-dir ./reports
```

## 安装

```bash
git clone <repo>
cd open-growth-intel
pip install -r cli/requirements.txt
pip install -e .
```
