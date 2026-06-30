# CLAUDE.md

本文件为 Claude Code 使用本项目时的参考指南。

**范围限定**：本文档只放 Claude Code 维护本项目时的操作约束与当前状态，不重复对外产品说明。对外项目定位、能力介绍见 `README.md`，各 Skill 用法见 `skills/*/SKILL.md`。

## 项目定位

`open-growth-intel` 是个人开源增长工具集，包含 3 个 Claude Code Skill：

- `/growth-site`：管理 `site/` 静态页面
- `/build-landing`：生成 SEO/GEO 落地页
- `/competitor-report`：生成竞品双周报

## 当前 CLI 状态

- 统一 Typer 入口当前只有 `ogi landing build`
- `ogi site ...` 与 `ogi competitor ...` 仍是规划态，不要当作已实现命令使用
- 旧模块 `python3 -m cli.page_builder` 仍存在，但职责是页面清单/竞品抓取实验，不负责落地页渲染

## 常用命令

```bash
# 安装依赖
pip install -r cli/requirements.txt
pip install -e .

# 落地页
ogi landing build --type a --brand "DemoBrand" --keyword "..." --output ./out/page.html
ogi landing build --type article --brand "DemoBrand" --title "..." --output ./out/article.html

# 测试
python3 -m unittest discover -s tests -p 'test_*.py'
```

## 目录约定

- `cli/`：Typer CLI，所有 Skill 的实际执行层
- `skills/`：Skill 元数据与 prompt
- `templates/`：Jinja2 模板
- `site/`：GitHub Pages 静态源
- `examples/`：mock 配置
- `docs/`：文档

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

## 测试

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```
