# 竞品情报方法论

## 1. 核心原则

1. **GIQ 驱动**：所有采集围绕 Growth Intelligence Questions（增长情报问题）展开，不漫无目的抓取。
2. **事实边界**：只写证据能证明的事；推断必须标注“未确认”。
3. **来源分级**：独立来源 > 同源互证 > 单一来源 > 冲突。
4. **本地优先**：不使用付费 API，只读取公开 URL、Sitemap、RSS、社媒搜索。

## 2. 增长情报问题（GIQ）

每个竞品至少覆盖：

- 本周期有哪些新 SEO 落地页或内容发布？
- 付费广告素材或落地页有变化吗？
- 定价 / Free tier 有调整吗？
- 有没有新的 KOL/Creator 合作或社媒高互动内容？
- 产品有新版本或重大功能更新吗？

## 3. 信号分类

| 类别 | 说明 | 来源示例 |
|---|---|---|
| seo_content | SEO 内容动作 | 新文章、新落地页、旧页更新 |
| product_update | 产品更新 | Changelog、新功能页 |
| pricing_change | 定价变化 | Pricing 页、促销文案 |
| paid_ad | 付费广告 | Meta Ad Library、广告素材 |
| social_content | 官方社媒内容 | X/YouTube/LinkedIn/TikTok |
| creator_partnership | 创作者合作 | 第三方教程、优惠码 |
| community_signal | 社区信号 | Reddit、Trustpilot ≥3 回复 |
| launch_distribution | 发布与分销 | Product Hunt、市场合作 |
| media_coverage | 媒体报道 | Forbes、TechCrunch 等 |

## 4. 事件确认规则

1. **URL 新增/消失**：可作为线索，但正文变化需单独确认。
2. **lastmod 变化**：Sitemap 的 `lastmod` 单独变化不得直接写成内容更新。
3. **正文变化**：需连续两次运行确认，避免瞬态噪音。
4. **批量 lastmod 刷新技术时间**：超过 `mass_lastmod_threshold` 时忽略。
5. **社区信号入账**：Reddit 讨论 ≥3 回复、评论平台新增评论、第三方教程记录 URL+时间+互动量。

## 5. 输出格式

每次运行产出：

- `{week}_competitor_report.md`：双周报正文
- `{week}_event_ledger.csv`：结构化事件台账
- 可选 `{week}_summary.html`：HTML 摘要

报告必须包含：

1. 执行摘要（TL;DR）
2. 事件时间线表格
3. 未确认/待跟踪项
4. 覆盖状态矩阵
5. 来源台账
6. 下一步行动建议

## 6. 变更检测流程

```
读取 competitors.yaml
  ↓
对每个竞品：
  - 抓取 sitemap 获取 URL 清单
  - 提取关键页（首页/pricing/blog/产品页）内容指纹
  - 与上一次 state 对比
  ↓
识别变更事件（created / content_updated / commercial_updated / removed）
  ↓
连续两次运行确认后才写入正式报告
  ↓
生成 Markdown 报告 + CSV 事件台账
```

## 7. 来源关系标注

| 关系 | 含义 |
|---|---|
| independent_source | 独立来源，可信度最高 |
| same_source_corroboration | 同源不同文章互证 |
| repost_copy | 转载/复制，可信度低 |

## 8. 禁止事项

- 不抓取需要登录的内容
- 不存储全站 HTML 快照
- 不使用付费 SEO/广告情报 API
- 不伪造或推断竞品未公开的数据（ARR、用户数等）
- 不将社媒观点直接升级为产品事实
