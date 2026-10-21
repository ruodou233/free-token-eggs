# 免费 Token 平台当前清单

> **它是什么**：用于判断现在有哪些 AI 免费 API 额度或应用积分值得领取的时效清单，不是社区信号库。
> **本轮核验**：2026-10-20。额度、活动和有效期执行时从所列官方页面再看一遍。
> **相较 2026-09-04 版的变化**：智谱新增 GLM-4-Flash / GLM-4.7-Flash 永久免费；SiliconFlow 小模型永久免费已取消；Qoder CN 新增每日可领 100 通用 Credits；新增 DeepSeek 与海外平台 Gemini / NVIDIA NIM / Kiro。

## 字段说明

- `type`: `api-general` 可用于 API/外部 Agent；`app-only` 专属 App/Agent 内消耗。
- 优先级由所属章节决定：高优先级默认打开，中优先级用户要求扩展时再打开。
- 标题带「· 海外」的是海外平台（国内访问可能需代理，注意其免费层数据政策），未标注的为国内平台。
- `replaceable_link_key`: 用户可在 `~/.free-token-eggs-links.json` 中用该 key 替换为自己的邀请链接。

## 收录门槛

- 以最新权威榜单（SuperCLUE 综合榜 / LMArena 文本榜）为准：模型口碑须达到 **DeepSeek V4.1 同级**（第一梯队）才收录。
- 2026-10 核验后不收录：豆包（SuperCLUE 约第 5，低于 DeepSeek 旗舰，LMArena 未进第一梯队）、百度文心、腾讯混元、商汤、讯飞星火；海外 OpenRouter / Groq / Cloudflare / Mistral / Cerebras（免费档只到中档开源模型）。
- 平台聚合型（SiliconFlow、ModelScope）自身不产模型，但托管多家第一梯队开源模型，仍保留。

## 高优先级

### 智谱 BigModel

- key: `bigmodel`
- type: `api-general`
- 默认入口: `https://open.bigmodel.cn/overview`
- 官方说明: `https://open.bigmodel.cn/special_area`
- 当前免费内容：新用户 2000 万 Tokens，以及 120 次图像/视频资源包。
- 永久免费模型（2026-10 新增）：GLM-4-Flash、GLM-4.7-Flash 在开放平台长期免费调用，无需信用卡，适合作为常驻免费后端。
- 邀请活动：官网当前仍展示邀请实名注册可累计获得 Tokens，累计上限 2 亿。
- 使用范围：智谱开放平台 API；不等同于 GLM Coding Plan。
- 有效期：执行时以账户资源包页面为准。
- 核验建议：查官方活动公告、控制台 overview 弹窗、资源包页面；旗舰已迭代至 GLM-5.x。

### SiliconFlow

- key: `siliconflow`
- type: `api-general`
- 默认入口: `https://cloud.siliconflow.cn/me/campaigns/inviter`
- 官方说明: `https://www.siliconflow.cn/developer-talk/od7wj9rr23p95uhihmhrombp`
- 当前免费内容：国内站完成实名认证可领 16 元通用代金券；通过推荐官链接注册并实名，邀请双方另各得 16 元。
- ⚠️ 缩水提醒（2026-10）：此前"部分小模型 0 元永久免费"已取消，当前仅 embedding、语音、OCR、翻译、Kolors 仍在免费列表；调用主流大模型需消耗代金券或余额。
- 使用范围：API、批量推理、微调及 Pro / 高速模型。
- 有效期：推荐官计划至 2026-12-31；代金券自获得起 180 天。

### Kimi API

- key: `kimi`
- type: `api-general`
- 默认入口: `https://platform.kimi.com/console`
- 官方说明: `https://www.kimi.com/zh-cn/help/kimi-api/api-free-trial`
- 当前免费内容：中国大陆手机号新用户自动获得 15 元 API 代金券（2026-10 核验仍有效）。
- 使用范围：Kimi API，可接入脚本 / 外部 Agent / IDE。
- 有效期：自发放起 3 个月。
- 注：15 元代金券不可用于体验最新旗舰 Kimi K3，需充值解锁。

### 扣子 Coze

- key: `coze`
- type: `app-only`
- 默认入口: `https://www.coze.cn/studio`
- 官方说明: `https://docs.coze.cn/coze_pro_credits`
- 当前免费内容：个人免费版首次注册获得 1500 积分，有效 30 天；每日登录获得 1500 积分，有效 1 天；邀请新用户得 6000 积分（30 天）。
- 可用模型（2026-10 核验，含第一梯队）：内置可切换 DeepSeek-V4-Pro、GLM-5.3、Kimi K3、MiniMax、豆包等；DeepSeek / 豆包按 token 扣积分，Kimi-8k/32k/128k、阶跃星辰等限时免费（约 100 次/天，不扣积分）。免费积分可直接用于 DeepSeek 等第一梯队模型，符合收录门槛。
- 使用范围：扣子任务、扣子编程、低代码项目、模型、工具、音视频和存储等扣子内服务。

### 阿里百炼 / Qwen

- key: `dashscope`
- type: `api-general`
- 默认入口: `https://bailian.console.aliyun.com/`
- 官方说明: `https://help.aliyun.com/zh/model-studio/new-free-quota`
- 当前免费内容：参与活动的模型通常各有独立新人额度，常见为 100 万 Token；新用户总额超 7000 万 Token。
- 使用范围：华北 2（北京）的实时推理。
- 有效期：通常为 90 天，从开通、模型发布或申请通过三者中较晚的日期起算。

### ModelScope

- key: `modelscope`
- type: `api-general`
- 默认入口: `https://www.modelscope.cn/my/myaccesstoken`
- 官方说明: `https://modelscope.cn/docs/model-service/API-Inference/limits`
- 当前免费内容：API Inference 免费；每账号每日总计 2000 次，单模型每日上限最高 500 次（DeepSeek-R1/V3 等大模型限 100 次）。
- 使用范围：带 API Inference 标识的开源模型。
- 注：需绑定阿里云账号并完成实名。

### DeepSeek

- key: `deepseek`
- type: `api-general`
- 默认入口: `https://platform.deepseek.com/`
- 当前免费内容：新开发者账号送 500 万 Tokens（30 天）；网页 / App 对话长期免费。
- 使用范围：DeepSeek 开放平台 API。

### Google Gemini（AI Studio）· 海外

- key: `gemini`
- type: `api-general`
- 默认入口: `https://aistudio.google.com/`
- 官方说明: `https://ai.google.dev/gemini-api/docs/rate-limits`
- 当前免费内容：免费层覆盖 Gemini 3.x Flash / 2.5 Flash / Gemma 4 等前沿模型，无需信用卡；约 10 RPM / ~1500 RPD（以 AI Studio 控制台显示为准）。
- 使用范围：Gemini API（原生 + OpenAI 兼容端点），可接入脚本 / 外部 Agent / IDE。
- 卡点：免费层提示词可能被用于改进 Google 产品；国内访问可能需代理；超限即 429、无自动扣费。

## 中优先级

### Qoder CN

- key: `qoder`
- type: `app-only`
- 默认入口: `https://qoder.cn/`
- 官方说明: `https://docs.qoder.cn/product-overview/billing-description`
- 当前免费内容：个人体验版含 2 周 Pro 试用和 300 Credits。
- 🟢 新增（2026-10）：2026-09-18 起个人用户每日可在桌面端主动领取 100 通用 Credits（30 天有效，可跨天保留）；Qwen3.8-Flash 调用系数 0.0× 不耗 Credits。
- 使用范围：Qoder CN IDE、JetBrains、QoderWork、CLI、QoderWake 和 Mobile 等端内能力。

### NVIDIA NIM（build.nvidia.com）· 海外

- key: `nvidia-nim`
- type: `api-general`
- 默认入口: `https://build.nvidia.com/`
- 官方说明: `https://build.nvidia.com/`
- 当前免费内容：注册赠 1000 推理 Credits（企业邮箱可到 5000），40 RPM；托管 DeepSeek / GLM-5.3 / Qwen3.8 / Kimi 等第一梯队模型（及 Gemma / Nemotron），可用免费 Credits 调用。
- 使用范围：OpenAI 兼容端点 `integrate.api.nvidia.com/v1`。
- 卡点：Credits 为消耗型、不自动刷新；需手机验证。

### Amazon Kiro · 海外

- key: `kiro`
- type: `app-only`
- 默认入口: `https://kiro.dev/`
- 官方说明: `https://kiro.dev/pricing`
- 当前免费内容：免费档 $0/月含 50 Credits/月（非试用、无需卡）；社交 / AWS Builder ID 首登再送 500 Credits。免费档可用 Claude Sonnet 4.5（前沿，>V4.1）+ 开源模型（Qwen3 Coder Next / DeepSeek 3.2 / MiniMax M2.1）；Opus 5 / GPT-5.6 等旗舰需付费。
- 使用范围：Kiro IDE / CLI / 网页 / 移动端的 spec 驱动 agentic 编程；app-only，非通用 API key。
- 卡点：免费档仅 50 Credits/月，量很小；旗舰模型锁付费档；GovCloud 无免费档。

## 作者邀请链接

发行版当前为 BigModel 和 SiliconFlow 提供作者邀请链接；用户配置可替换。
