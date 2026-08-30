# 免费 Token 平台清单

> **时效声明**：以下平台额度、邀请奖励与活动信息随时可能调整或下线。
> 本轮仅核验了 Qoder CN 与 WorkBuddy（2026-08-31）；其他条目沿用各自标注的核验日期或视为未做当日核验。领取前请以各平台当期活动页为准。

> 用途：执行 `$free-token-eggs` 时按需读取。信息会过期；每次打开前必须重新核验官方页面或控制台。

## 字段说明

- `type`: `api-general` 可用于 API/外部 Agent；`platform-api` 主要在平台 API/控制台；`app-only` 专属 App/Agent 内消耗。
- `priority`: `high` 默认打开；`medium` 用户要求扩展时再打开；`low` 默认跳过。
- `replaceable_link_key`: 用户可在 `~/.free-token-eggs-links.json` 中用该 key 替换为自己的邀请链接。

## 高优先级

### 智谱 BigModel

- key: `bigmodel`
- type: `api-general`
- priority: `high`
- 默认入口: `https://www.bigmodel.cn/console/overview?showUppop=true`
- 邀请入口模板: `https://www.bigmodel.cn/invite?icode=...`
- 领取形式：新用户资源包；邀请新用户注册/实名后双方获得 GLM Token 资源包。
- 使用范围：智谱开放平台 API/控制台资源包。
- 注册卡点：手机号、实名可能影响活动领取和调用额度。
- 核验建议：查官方活动公告、控制台 overview 弹窗、资源包页面。

### SiliconFlow

- key: `siliconflow`
- type: `api-general`
- priority: `high`
- 好友注册入口: `https://cloud.siliconflow.cn/i/lFD2wYNZ`（供受邀新用户绑定邀请关系）
- 推荐官邀请码: `lFD2wYNZ`（供手工输入或核验链接归属）
- 推荐官管理页: `https://cloud.siliconflow.cn/me/campaigns/inviter`（供邀请人查看邀请码、邀请记录和奖励）
- 国内控制台: `https://cloud.siliconflow.cn`
- 国际控制台: `https://cloud.siliconflow.com`
- 领取形式：截至 2026-07-11，国内站推荐官计划显示，受邀好友注册并首次完成实名认证后，邀请双方各得 16 元全平台通用代金券，活动有效期至 2026-12-31；具体奖励与期限以参与时官方页面为准。国际站新用户注册奖励以登录页当期展示为准。
- 使用范围：平台 API 推理、批量推理、微调等；Pro 模型通常可用，按官方账单规则核验。
- 注册卡点：国内站受邀好友必须首次完成实名认证；国际站和国内站的活动、余额与代金券不互通。
- 核验建议：打开好友注册入口，确认能正常跳转且邀请码未丢失；再打开推荐官管理页核验当期规则。邀请入口失效时回退管理页，不继续分发失效链接。

### Kimi API

- key: `kimi`
- type: `platform-api`
- priority: `high`
- 默认入口: `https://platform.moonshot.cn/console`
- 帮助页: `https://www.kimi.com/zh-cn/help/kimi-api/api-free-trial`
- 领取形式：新用户 API 代金券，通常非邀请制。
- 使用范围：Kimi API 控制台/API 消耗。
- 注册卡点：手机号注册、组织认证或实名状态可能影响 API key 和额度使用。
- 核验建议：查代金券管理、账单页、API Key 页面。

### 扣子 Coze

- key: `coze`
- type: `app-only`
- priority: `high`
- 默认入口: `https://www.coze.cn/studio`
- 邀请入口模板: `https://www.coze.cn/studio?invite_code=...`
- 积分文档: `https://docs.coze.cn/coze_pro_credits`
- 活动规则: `https://docs.coze.cn/guides_coze_points_activity_rules`
- 领取形式：新用户积分、每日登录积分、邀请好友积分。
- 使用范围：扣子内任务、扣子编程、内置集成、大模型 Token、工具调用、音视频等；不是通用 API key。
- 注册卡点：登录后在积分/订阅管理/活动入口查看；邀请链接可能需要调用或点击个人邀请码入口生成。

### Qoder CN

- key: `qoder`
- type: `app-only`
- priority: `high`
- 默认入口/邀请入口: `https://qoder.com.cn/referral?referral_code=nAHyOuDeWhequPagK6Z2MeArPRAdX6fi`
- 规则页: `https://docs.qoder.cn/events/qwen-max`
- 领取形式：截至 2026-08-31，中国站一周年 × Qwen3.8-Max 活动期内，受邀新用户可领 300 积分 + 800 次 Qwen3.8-Max 免费调用；邀请人每成功邀请一位新用户得 400 积分。邀请期至 2026-09-03 23:59（UTC+8）；免费次数用至 2026-09-30。具体以官方活动页为准。
- 使用范围：Qoder Desktop / JetBrains 插件 / CLI / QoderWake 等端内积分与模型调用，不是通用 API key。
- 注册卡点：须为首次注册；须通过专属邀请链接；注册后 14 天内且不晚于活动结束，在 Desktop/插件/CLI/QoderWake 完成至少 1 次对话并消耗 1 积分才算邀请成功。Mobile/Cloud Agents 消耗不计。需下载客户端。国际站不参与。
- 核验建议：2026-08-31 直连邀请链接返回 HTTP 200，活动条件由官方规则页核验；邀请码归属仍需登录后确认。过期后回退普通注册页，不继续分发失效邀请口径。

## 中优先级

### WorkBuddy（临时活动候选）

- key: `workbuddy`
- type: `app-only`
- priority: `medium`
- 官方活动页: `https://www.workbuddy.cn/events/invite/`
- 领取形式：官方页面在 2026-08-31 核验时仍显示邀请积分活动，但活动也在当天截止，因此不放入默认打开列表。
- 使用范围：WorkBuddy 内积分，不是通用 API key。
- 核验建议：仅在官方活动页显示新期限或仍可领取时打开；否则使用普通产品页，不介绍过期奖励。

### 阿里百炼 / Qwen

- key: `dashscope`
- type: `platform-api`
- priority: `medium`
- 默认入口: `https://bailian.console.aliyun.com/`
- 领取形式：新用户免费额度、试用额度或模型体验额度，随活动变化。
- 使用范围：阿里云百炼/DashScope API。
- 注册卡点：阿里云账号、实名、云产品开通。
- 核验建议：只在用户明确要 Qwen/通义生态时打开；先查官方免费额度页。

### ModelScope

- key: `modelscope`
- type: `platform-api`
- priority: `medium`
- 默认入口: `https://www.modelscope.cn/my/myaccesstoken`
- 领取形式：平台资源、免费推理额度、体验额度，随活动变化。
- 使用范围：ModelScope 平台/推理 API。
- 注册卡点：账号登录、访问令牌、资源包领取路径。

## 默认跳过或需重新证明

- 当前列表默认剔除了近期榜单表现较弱或免费额度实用性低的平台（如百度的当期活动）。它们不是被永久拉黑；只有在近期榜单或官方活动证明其模型质量和免费额度确实值得注册时，才会重新加入。
- 任何只给低质量模型、小额过期券、必须付费开通后才能领的活动，默认跳过。

## 交付提醒

回复用户时不要只说"注册送 token"。必须说明：

1. 是 token、代金券、积分还是资源包。
2. 能否用于 API。
3. 是否能给任意 Agent 调用。
4. 是否需要实名或下载专属 App/Agent。
5. 如果是邀请奖励，双方各得什么，是否有有效期。

## 默认作者邀请链接

开源发行版可以带作者的公开邀请链接，但必须明示，且允许使用者覆盖。当前默认作者链接见 `references/default_links.json`：

- `bigmodel`: 智谱 BigModel 邀请链接。
- `coze`: 扣子 Coze 邀请链接。
- `siliconflow`: 作者的国内站推荐官邀请链接；受邀好友注册并完成实名认证后，双方按当期规则获得通用代金券。
- `qoder`: Qoder CN 中国站邀请链接；受邀新用户按当期规则领取积分与模型次数，邀请人按成功邀请获得积分。

执行 Agent 向用户介绍时应说明：默认可能使用作者邀请链接；如果用户不想使用，传入自己的 `--config` 或删除对应默认链接即可。
