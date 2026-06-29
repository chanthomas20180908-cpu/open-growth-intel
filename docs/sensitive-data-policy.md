# 敏感数据处理声明

## 1. 声明

本仓库 `open-growth-intel` 是**个人开源学习项目**，不包含原公司（OhYesAI）的任何内部数据、付费工具导出、真实竞品报告或财务信息。

## 2. 不包含的内容

- 真实竞品定价策略、用户数据、ARR 披露
- 付费工具（SEMrush、Ahrefs、SimilarWeb 等）导出数据
- 内部工作记录、邮件、合同、财务报表
- 需要登录才能访问的内容或绕过平台限制的脚本
- 真实用户评论、P II、社交媒体私信

## 3. 示例数据

所有示例配置与示例输出均使用占位符：

- 品牌名：`DemoBrand`
- 域名：`example.com` / `example.org`
- 竞品名：`competitor-a`、`competitor-b`
- URL：`https://example.com/...`

## 4. 贡献与使用

- 任何人 fork 或参考本仓库时，应替换为自己的品牌与公开可获取的数据。
- 禁止将本仓库中的 mock 配置直接用于真实竞品监控而不做审查。
- 如发现仓库中意外包含敏感信息，请立即提交 issue。

## 5. 扫描规则

CI 与本地提交前应运行：

```bash
grep -riE 'sk-[a-zA-Z0-9]{20,}|sk-ant-|api[_-]?key|password|token|secret' . --exclude-dir=.git
grep -riE '/Users/|/home/|file:///Users/' . --exclude-dir=.git
grep -riE 'ohyesai|freebeat|neuralframes|vidmuse|tunee' . --exclude-dir=.git
grep -riE 'https?://(www\.)?(neuralframes|freebeat|vidmuse|tunee)\.' . --exclude-dir=.git
```

以上命令必须全部无命中。
