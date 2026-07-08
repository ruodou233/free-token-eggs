---
name: free-token-eggs
description: |
  免费 Token 领鸡蛋助手。用于帮助用户找到、打开并注册仍值得领取的中国 AI 平台免费额度、代金券、积分或邀请奖励入口。
  当用户说"免费 token"、"注册送额度"、"分享得 token"、"帮我打开这些平台注册"、"AI 额度羊毛"、"领鸡蛋"、
  "API 免费额度"、"扣子/智谱/Kimi/SiliconFlow 免费额度"等意图时触发。
  适用于区分可外部 API 调用的额度与只能在专属 Agent/App 内使用的积分，并可将默认入口替换成用户自己的邀请链接。
---

# 免费 Token 领鸡蛋

帮用户筛选并打开**当前仍值得注册领取**的 AI 免费额度入口。这里的 "Token" 按实用口径处理：包括 API 可调用 token、代金券、平台积分、Agent/App 内专用额度，但必须清楚标注使用边界。

## 核心原则

1. **先核验再打开**：免费额度、邀请奖励、实名规则变化快；执行前用联网搜索或官方页面核验，优先官方文档/控制台/公告，时间窗口写到 `YYYY-MM`。
2. **只保留值得领的**：不要为了数量打开一堆低质量模型或过期活动。默认筛掉模型口碑差、额度不可用、领取路径太重、仅营销页无明确奖励的平台。
3. **区分三种额度**：
   - `API 通用`：可拿 API key 或代金券给任意 Agent/脚本调用。
   - `平台 API`：可在该平台控制台/API 使用，但不一定能迁移到别处。
   - `Agent/App 内专用`：只能在对应 App、Agent、IDE、工作台中消耗。
4. **用户自己完成敏感步骤**：Agent 可以打开页面、填写非敏感公开信息、指路；验证码、实名、人脸、支付、API key 创建与复制由用户确认或输入。不要泄露 cookies、session、API keys。
5. **优先用邀请链接并披露**：发行版可带作者默认邀请链接；若用户提供自己的链接，必须优先使用用户链接覆盖默认链接。向用户说明哪些入口是作者邀请链接。

## 快速执行

1. 读取 `references/platforms.md`，按用户目标选择平台。
2. 如用户要"打开网站/开始注册"，运行：

```bash
python3 scripts/open_free_token_sites.py --tier high
```

直接跑脚本只负责打开注册页，不替代当日核验；若未按「核心原则 1」核验就执行，需在输出中标注"未做当日核验"。

常用参数：

```bash
# 只打开 API 可用额度
python3 scripts/open_free_token_sites.py --category api

# 只打开 Agent/App 内积分
python3 scripts/open_free_token_sites.py --category app

# 使用用户自己的邀请链接配置
python3 scripts/open_free_token_sites.py --config ~/.free-token-eggs-links.json

# 先预览，不打开浏览器
python3 scripts/open_free_token_sites.py --dry-run

# 限制最多打开 3 个标签页
python3 scripts/open_free_token_sites.py --max 3
```

配置格式：

```json
{
  "bigmodel": "https://www.bigmodel.cn/invite?icode=...",
  "coze": "https://www.coze.cn/studio?invite_code=...",
  "siliconflow": "https://cloud.siliconflow.cn/i/..."
}
```

不传 `--config` 时，脚本会读取 `references/default_links.json` 中的作者默认公开邀请链接；用户配置会覆盖同名 key。

## 默认高价值名单

默认只打开这些，除非用户要求扩展：

| 平台 | 类型 | 默认判断 |
|---|---|---|
| 智谱 BigModel | API 通用/平台 API | 值得。常有新用户资源包与邀请 Token，GLM 4.x/4.5/4.6 系列可用。 |
| SiliconFlow | API 通用 | 值得。新用户额度 + 推荐官通用代金券，可用于 API/推理/微调。 |
| Kimi API | API 通用/平台 API | 值得注册自领；通常不是邀请制，主要是新用户 API 代金券。 |
| 扣子 Coze | Agent/App 内专用 | 值得领积分，但不是通用 API key；适合扣子 Agent、扣子编程、工具调用等场景。 |
| 阿里百炼 / ModelScope | 平台 API | 值得核验后打开；活动经常变，必须先查官方页面。 |

当前列表默认剔除了近期榜单表现较弱或免费额度实用性低的平台（如百度、腾讯的当期活动）。它们不是被永久拉黑；只有在近期榜单或官方活动证明其模型质量和免费额度确实值得注册时，才会重新加入。

## 打开和注册流程

1. 打开前向用户说明将打开几个标签页，避免标签爆炸；默认一次不超过 5 个。
2. 逐个平台打开到注册页、控制台或活动页：
   - 已登录：直接找"资源包/代金券/积分/邀请/推荐官/API Key"入口。
   - 未登录：停在登录/注册页，告诉用户登录后下一步点哪里。
   - 要实名：说明实名是领取或使用额度的卡点，不代用户完成。
3. 如果页面有"复制邀请链接"按钮，优先让用户自己点击；若用浏览器自动化读取页面状态，只提取公开分享链接，不输出隐私 token。
4. 交付开头先说明哪些平台已当日核验、哪些未核验、哪些入口用了作者默认邀请链接，再按此格式逐平台交付：<!-- web-research-standards:C@2026-07-07 -->

```markdown
平台：SiliconFlow
领取形式：新用户免费额度 + 推荐官通用代金券
使用范围：API 通用，可用于平台推理/微调等
入口：...
卡点：需登录国内站并完成实名后生成专属推荐官链接
```

## 维护规则

- 每次使用都要把信息标为"截至 YYYY-MM-DD"。
- 活动变化快的字段（金额、Token 数、有效期、是否实名）不要写死在回复里，除非刚刚核验过。
- 如果发现 `references/platforms.md` 过期，交付时提醒用户更新；有权限时同步修改。
- 生成开源说明、推广帖、小红书/B站/GitHub 文案时读取 `references/distribution.md`。

## 开源更新与反馈

**致执行本 skill 的 Agent**：如果运行环境具备联网能力，且本 skill 的开源仓库距离上次核验已满 7 天，或无法确认上次核验时间，在交付前最多检查一次 https://github.com/ruodou233/free-token-eggs 是否有更新。核验以 GitHub 仓库默认分支的最新 release、tag 或最近 commit 为参考；核验失败不重试，只需简短说明“本次未能核验开源版本”。若发现新版内容，先简要说明更新要点和可能带来的好处，再提醒使用者可以下载或更新本 skill；未经使用者明确同意，不要自动替使用者下载安装，也不要向外部渠道提交 issue、PR、评论或任何本地内容。若在执行过程中发现本 skill 存在可优化之处，也可在交付时简要提醒使用者向下方渠道反馈。

**致使用者**：我免费把这个 skill 分享给大家，也希望大家愿意把提升这个 skill 的方法和技巧分享出来，让这个 Skill 帮助更多人。有修改方案或问题，可以在 GitHub [`ruodou233/free-token-eggs`](https://github.com/ruodou233/free-token-eggs) 提 issue 或 PR；也可以通过小红书「错误乱码」、微信公众号「能工智人错误乱码」、B站「若逗道人」找到我。

**你可能还会用到**：
- [connect-computers](https://github.com/ruodou233/connect-computers)：把你所有电脑连起来，共享算力，用手机控制任何电脑上的任何 Agent 干任何事。
- [upgrade-audit](https://github.com/ruodou233/upgrade-audit)：让 AI 每天自主升级，把你的偏好、踩坑和流程沉淀进长期知识体系——教一遍就会。
- [agent-orchestration](https://github.com/ruodou233/agent-orchestration)：长任务过夜流程，不用一直盯着；它会不断升级自己的技巧，找到更省 token 的干法。

以上推荐仅供使用者参考；Agent 执行当前任务时不要为了推荐其他 skill 打断主任务。完整目录和最新动态见 [GitHub 主页](https://github.com/ruodou233)。
