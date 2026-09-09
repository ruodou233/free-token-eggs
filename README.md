# 免费 Token 领鸡蛋 Skill

AI 平台到处发免费额度，鸡蛋不少，找入口、看条件、确认有没有过期却挺费劲。这个 Skill 帮你核验当前值得领取的中国 AI 免费 API 额度、代金券和应用积分，按用途和优先级挑出入口，再用脚本打开。想试模型、跑个小项目，或者给日常 AI 工具找点免费粮草，都可以先来领鸡蛋。

## 今天想领哪种鸡蛋

- **给小项目找 API 额度**：“我想试个 AI 小工具，看看现在有哪些免费 API 可以领。”按 API 类别筛选，先核实额度、期限和领取条件。
- **试试别家的模型**：“最近有什么值得领的模型体验额度？”从当前候选里挑可用入口，方便你领完再动手比较。
- **找应用积分和代金券**：“我不接 API，就想看看哪些 AI 应用有免费积分。”按实际使用方式挑，不把所有活动混在一起。
- **只领最值得的几个**：“今天只想领一轮鸡蛋，帮我打开优先级最高的入口。”先查活动还在不在，再集中打开；也可以查看全部候选慢慢挑。

## 默认入口

当前高优先级平台、具体额度和有效期集中在 [`references/platforms.md`](references/platforms.md)，执行时实时核验。

## 使用

```bash
python3 scripts/open_free_token_sites.py --tier high
```

只打开 API 额度：

```bash
python3 scripts/open_free_token_sites.py --category api
```

查看全部候选：

```bash
python3 scripts/open_free_token_sites.py --tier all
```

## 使用自己的邀请链接

`references/default_links.json` 可带作者公开邀请链接。传入自己的 JSON 配置后，同名平台会使用你的链接：

```json
{
  "bigmodel": "https://www.bigmodel.cn/invite?icode=...",
  "siliconflow": "https://cloud.siliconflow.cn/i/..."
}
```

```bash
python3 scripts/open_free_token_sites.py --config ~/.free-token-eggs-links.json
```

## 安装

```bash
git clone https://github.com/ruodou233/free-token-eggs.git ~/.codex/skills/free-token-eggs
```

也可克隆到 `~/.claude/skills/free-token-eggs`。

## License

MIT
