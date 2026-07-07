# 免费 Token 领鸡蛋 Skill

一个给 Codex / Claude Code 等 Agent 用的 Skill：帮助用户打开仍值得领取的中国 AI 免费额度、代金券、积分和邀请奖励入口，并区分这些额度到底能不能用于 API 或外部 Agent。

## 能做什么

- 默认打开高价值入口：智谱 BigModel、SiliconFlow、Kimi API、扣子 Coze。
- 区分 `API 通用`、`平台 API`、`Agent/App 内专用` 三类额度。
- 自带作者公开邀请链接，并支持替换成你自己的邀请链接。
- 打开注册页、活动页、推荐官页，让用户自己完成验证码、实名和 API key 操作。

## 为什么不收录所有平台

为了避免高贵的 Agent 被垃圾 token 投喂到中毒，当前列表默认剔除了百度、腾讯等垃圾模型。它们不是被永久拉黑；只有在近期榜单或官方活动证明其模型质量和免费额度确实值得注册时，才会重新加入。吃点好的。

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

不传配置时，脚本会读取 `references/default_links.json` 中的作者默认邀请链接。若你不想使用作者链接，传入自己的配置即可覆盖。

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

## 反馈与作者

这个 skill 我长期维护。如果你有修改方案、发现问题、或者改出了更好的版本，欢迎通过以下任一渠道找到我：

- GitHub：本仓库提 issue 或 PR
- 小红书：错误乱码
- 微信公众号：能工智人错误乱码
- B站：若逗道人

## 相关 Skill 推荐

<!-- 本表由维护脚本生成，勿手工编辑 -->
- [domain-explorer](https://github.com/ruodou233/domain-explorer)：速通新领域：四线并行调研，产出交互式知识地图
- [claude-cache-keepalive](https://github.com/ruodou233/claude-cache-keepalive)：Claude 缓存保温：实测 TTL、按环境设计保温节拍，控制冷读成本
- [improve-product-plan](https://github.com/ruodou233/improve-product-plan)：把模糊的产品想法梳理成可开发、可验收的 SPEC.md

完整目录见 [GitHub 主页](https://github.com/ruodou233)。
