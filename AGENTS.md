# AGENTS.md

本文件为 Codex 等读取 `AGENTS.md` 的 AI 提供项目级说明。

## 项目定位

`open-growth-intel` 是一个本地优先的增长工具集，当前仓库重点是：

- `landing-builder`：通过 `/build-landing` 或 `ogi landing build` 生成静态落地页
- `growth-site`：目前只有静态页面资产与 Skill 定义，统一 CLI 未完成
- `competitor-report`：目前只有方法论文档与 Skill 定义，统一 CLI 未完成

## 当前代码事实

- 统一 CLI 入口文件：`cli/main.py`
- 当前唯一已实现的 `ogi` 子命令：`landing build`
- 落地页渲染模块：`cli/landing_builder.py`
- 历史模块 `cli/page_builder.py` 仍保留，但不负责 `ogi landing build`

## 落地页命令约束

```bash
ogi landing build --type a --brand "DemoBrand" --keyword "ai music video generator" --output ./out/page.html
ogi landing build --type article --brand "DemoBrand" --title "Top 10 AI Music Video Tools" --output ./out/article.html
```

- `--type` 允许：`a`、`b`、`c`、`article`
- Type A/B/C 必填 `--keyword`
- Article 必填 `--title`
- `--faq-items` 支持 JSON/YAML 字符串或文件路径

## 测试

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

## 文档同步约定

- 不要把 `ogi site ...` 或 `ogi competitor ...` 写成已可运行命令，除非代码先实现
- 修改 HTML 模板后，保持属性引号为英文半角 `"..."`
- 示例数据继续使用 `DemoBrand` 与 `example.com`
