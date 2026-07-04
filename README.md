# 免费 Token 领鸡蛋 Skill

一个给 Codex / Claude Code 等 Agent 用的 Skill：帮助用户打开仍值得领取的中国 AI 免费额度、代金券、积分和邀请奖励入口，并区分这些额度到底能不能用于 API 或外部 Agent。

## 能做什么

- 默认打开高价值入口：智谱 BigModel、SiliconFlow、Kimi API、扣子 Coze。
- 区分 `API 通用`、`平台 API`、`Agent/App 内专用` 三类额度。
- 支持把默认入口替换成你自己的邀请链接。
- 打开注册页、活动页、推荐官页，让用户自己完成验证码、实名和 API key 操作。

## 安装

把仓库放到你的 skills 目录，例如：

```bash
git clone https://github.com/ruodou233/free-token-eggs.git ~/.codex/skills/free-token-eggs
```

或在 Claude Code 中：

```bash
git clone https://github.com/ruodou233/free-token-eggs.git ~/.claude/skills/free-token-eggs
```

然后在新会话中说：

```text
Use $free-token-eggs to open high-value Chinese AI platforms with free credits and guide me through registration.
```

## 使用自己的邀请链接

创建本地配置：

```json
{
  "bigmodel": "https://www.bigmodel.cn/invite?icode=...",
  "coze": "https://www.coze.cn/studio?invite_code=...",
  "siliconflow": "https://cloud.siliconflow.cn/i/..."
}
```

运行：

```bash
python3 scripts/open_free_token_sites.py --config ~/.free-token-eggs-links.json
```

## 安全边界

这个 Skill 不保存账号、密码、cookie、API key 或实名信息。验证码、实名、人脸验证、支付、API key 创建和复制应由用户自己完成。平台活动变化快，Agent 在打开前应重新核验官方页面。

## 反馈

- GitHub: [ruodou233/free-token-eggs](https://github.com/ruodou233/free-token-eggs)
- 小红书：错误乱码
- 微信公众号：能工智人错误乱码
- B站：若逗道人
