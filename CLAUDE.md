# CLAUDE.md

本文件为 Claude Code 使用本项目时的参考指南。

## 项目定位

`open-growth-intel` 是个人开源增长工具集，包含 3 个 Claude Code Skill：

- `/growth-site`：管理 `site/` 静态页面
- `/build-landing`：生成 SEO/GEO 落地页
- `/competitor-report`：生成竞品双周报

## 常用命令

```bash
# 安装依赖
pip install -r cli/requirements.txt
pip install -e .

# 站点管理
ogi site preview --page index
ogi site update --page worklog --entry "..."

# 落地页
ogi landing build --type a --brand "DemoBrand" --keyword "..." --output ./out/page.html

# 竞品报告
ogi competitor report --config ./examples/competitors.example.yaml --output-dir ./reports
```

## 修改 HTML 时的强制规范

1. 属性引号必须使用英文半角 `"..."`，严禁中文弯引号。
2. 修改后必须运行：

```bash
rg -n 'class=[""]|style=[""]|href=[""]|src=[""]|id=[""]|target=[""]|rel=[""]' 文件路径
```

## 敏感数据红线

- 不提交任何真实品牌名（OhYesAI、Freebeat、NeuralFrames、VidMuse、Tunee）
- 不提交真实竞品 URL
- 不提交本地路径 `/Users/...`
- 不提交 API key、token、password

## 目录约定

- `cli/`：Typer CLI，所有 Skill 的实际执行层
- `skills/`：Skill 元数据与 prompt
- `templates/`：Jinja2 模板
- `site/`：GitHub Pages 静态源
- `examples/`：mock 配置
- `docs/`：文档

## 测试

```bash
pytest tests/
```
