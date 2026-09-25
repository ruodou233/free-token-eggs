---
name: free-token-eggs
description: |
  免费 Token 领鸡蛋助手。用于查找、核验并打开当前值得领取的中国 AI 平台免费 API 额度、代金券或应用积分入口。
  当用户说“免费 token”“注册送额度”“API 免费额度”“帮我打开平台注册”“领鸡蛋”等意图时触发。
---

# 免费 Token 领鸡蛋

帮助用户找到现在还能领取、且用途清楚的 AI 免费额度。当前平台事实集中在 [`references/platforms.md`](references/platforms.md)，它是时效清单，不是社区信号库。

## 执行

1. 读取平台清单，按用户需要选择 API 通用额度或应用内积分。
2. 打开前从清单里的官方页面核验当前额度和有效期；旧活动不沿用。
3. 用户要直接打开时运行：

```bash
python3 scripts/open_free_token_sites.py --tier high
```

常用参数：

```bash
python3 scripts/open_free_token_sites.py --category api
python3 scripts/open_free_token_sites.py --category app
python3 scripts/open_free_token_sites.py --tier all
python3 scripts/open_free_token_sites.py --dry-run
python3 scripts/open_free_token_sites.py --config ~/.free-token-eggs-links.json
```

不传 `--config` 时，脚本读取 `references/default_links.json` 中的作者邀请链接；用户配置会覆盖同名入口。使用作者链接时直接说明即可。

## 额度类型

- **API 通用**：可供脚本或外部 Agent 调用。
- **平台 API**：在该平台的模型服务中调用。
- **应用内专用**：只能在对应 App、IDE 或工作台中使用。

## 交付

不要只发平台名：每个平台说清能拿来做什么、当前免费内容、入口和核验日期，形式按数量自选。

金额、Token 数和有效期只使用刚核验的当前值。用户要求代办注册、登录或取码时，在当前环境能力内完成；实名和付费由用户在平台页面完成。

## 维护

平台事实只维护在 `references/platforms.md`；脚本仅保存需要打开的名称、分类、优先级和 URL，不复制额度文案。
