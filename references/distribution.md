# 作者与开源分发信息

用于生成 Skill 开源页、GitHub 描述、社交平台说明、反馈入口和推广文案。

## 作者渠道

- GitHub: `ruodou233`
- 小红书: `错误乱码`
- 微信公众号: `能工智人错误乱码`
- B站: `若逗道人`

## 建议 GitHub 仓库

- 仓库名：`free-token-eggs`
- 标题：免费 Token 领鸡蛋 Skill
- 简介：帮 Agent 打开值得领取的中国 AI 免费 Token、代金券、积分和邀请奖励入口，并区分 API 可用额度与 App 内专用额度。
- Topics：`codex-skill`, `ai-agent`, `free-token`, `china-ai`, `llm-api`, `coze`, `siliconflow`, `bigmodel`, `kimi`

## 开源说明要点

- 这个 Skill 不保存用户账号、API key、cookie 或实名信息。
- 用户可以在本地 JSON 配置中替换自己的邀请链接。
- 平台活动变化很快，使用时 Agent 必须重新核验官方页面。
- 默认只打开高价值平台，避免把用户带去低质量或过期活动。

## 社交平台文案方向

### 小红书

标题候选：

- 我做了个 Agent Skill：自动打开能领 AI 免费 Token 的平台
- 免费 Token 领鸡蛋：让 Agent 帮你少开十几个无用网页
- AI API 额度别乱领，这个 Skill 会先筛一遍

正文要点：

- 区分 API 可调用额度、平台代金券、App 内积分。
- 默认只保留智谱、SiliconFlow、Kimi、扣子等当前高价值入口。
- 支持替换成自己的邀请链接。
- 验证码、实名、API key 仍由用户自己处理。

### B站

视频结构：

1. 痛点：AI 平台活动多，但很多已经过期或不值得注册。
2. 演示：一句话调用 Skill，Agent 打开高价值入口。
3. 解释：API 通用额度 vs App 内积分。
4. 安全：不保存账号和密钥，用户自己输入验证码。
5. 开源：GitHub 仓库和反馈方式。

### GitHub

README 可强调：

- "Not a coupon scraper; a curated agent workflow."
- "Bring your own referral links."
- "Verify before opening because free-credit campaigns change frequently."

## 反馈格式

建议 issue 模板字段：

- 平台名称
- 当前活动链接
- 免费额度形式
- 是否 API 可用
- 是否需要实名/下载 App
- 证据截图或官方文档链接
- 截至日期
