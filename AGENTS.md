# AGENTS.md

本文件为 Codex 等读取 `AGENTS.md` 的 AI 提供项目级说明。

**范围限定**：本文档只放当前代码事实与维护约束，不重复对外产品说明。对外项目定位、能力介绍见 `README.md`，各 Skill 用法见 `skills/*/SKILL.md`。

## 当前代码事实

- 统一 CLI 入口文件：`cli/main.py`
- 当前唯一已实现的 `ogi` 子命令：`landing build`
- 落地页渲染模块：`cli/landing_builder.py`
- 历史模块 `cli/page_builder.py` 仍保留，但不负责 `ogi landing build`，仅用于页面清单/竞品抓取实验
- `ogi site ...` 与 `ogi competitor ...` 仍为规划态，没有对应实现文件

## 落地页命令约束

```bash
ogi landing build --type a --brand "DemoBrand" --keyword "ai music video generator" --output ./out/page.html
ogi landing build --type article --brand "DemoBrand" --title "Top 10 AI Music Video Tools" --output ./out/article.html
```

- `--type` 允许：`a`、`b`、`c`、`article`
- Type A/B/C 必填 `--keyword`
- Article 必填 `--title`
- `--faq-items` 支持 JSON/YAML 字符串或文件路径
- `--output` 支持自动创建父目录

## 测试

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## 文档同步约定

- 不要把 `ogi site ...` 或 `ogi competitor ...` 写成已可运行命令，除非代码先实现
- 修改 HTML 模板后，保持属性引号为英文半角 `"..."`
- 示例数据继续使用 `DemoBrand` 与 `example.com`
- 对外产品说明改 `README.md` 或 `skills/*/SKILL.md`，不在这里堆叠
