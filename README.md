# 免费 Token 领鸡蛋 Skill

这个 Skill 帮你核验并打开当前值得领取的中国 AI 免费 API 额度、代金券和应用积分入口。

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
