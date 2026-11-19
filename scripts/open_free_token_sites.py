#!/usr/bin/env python3
"""Open curated AI free-credit registration pages.

This script intentionally stores no credentials. It only opens public URLs,
optionally replacing default URLs with user-provided referral links.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import webbrowser
from pathlib import Path


SITES = [
    {
        "key": "bigmodel",
        "name": "智谱 BigModel",
        "category": "api",
        "tier": "high",
        "url": "https://open.bigmodel.cn/overview",
        "note": "智谱开放平台 API 额度入口。",
    },
    {
        "key": "siliconflow",
        "name": "SiliconFlow 推荐官计划",
        "category": "api",
        "tier": "high",
        "url": "https://cloud.siliconflow.cn/me/campaigns/inviter",
        "note": "国内站推荐官计划；未登录会跳转登录页。",
    },
    {
        "key": "kimi",
        "name": "Kimi API",
        "category": "api",
        "tier": "high",
        "url": "https://platform.kimi.com/console",
        "note": "Kimi API 免费试用入口。",
    },
    {
        "key": "coze",
        "name": "扣子 Coze",
        "category": "app",
        "tier": "high",
        "url": "https://www.coze.cn/studio",
        "note": "扣子内新用户与每日登录积分。",
    },
    {
        "key": "dashscope",
        "name": "阿里百炼",
        "category": "api",
        "tier": "high",
        "url": "https://bailian.console.aliyun.com/",
        "note": "百炼新人模型免费额度入口。",
    },
    {
        "key": "tokenhub",
        "name": "腾讯云 TokenHub",
        "category": "api",
        "tier": "high",
        "url": "https://console.cloud.tencent.com/tokenhub/models",
        "note": "模型广场右上角「新用户福利免费体验」领取；未登录会跳转登录页。",
    },
    {
        "key": "modelscope",
        "name": "ModelScope",
        "category": "api",
        "tier": "high",
        "url": "https://www.modelscope.cn/my/myaccesstoken",
        "note": "ModelScope API Inference 免费调用入口。",
    },
    {
        "key": "qoder",
        "name": "Qoder CN",
        "category": "app",
        "tier": "medium",
        "url": "https://qoder.cn/",
        "note": "个人体验版入口。",
    },
    {
        "key": "amd-tokenfactory",
        "name": "AMD Token Factory（中国站）",
        "category": "api",
        "tier": "medium",
        "url": "https://developer.amd.com.cn/radeon/tokenfactory",
        "note": "每日重置的免费 API；登录后在页面顶部复制 API Key。",
    },
    {
        "key": "gemini",
        "name": "Google Gemini（AI Studio）",
        "category": "api",
        "tier": "high",
        "url": "https://aistudio.google.com/",
        "note": "Gemini 免费层入口，无需信用卡。",
    },
    {
        "key": "nvidia-nim",
        "name": "NVIDIA NIM",
        "category": "api",
        "tier": "medium",
        "url": "https://build.nvidia.com/",
        "note": "托管 DeepSeek/GLM/Qwen/Kimi 的聚合入口；需手机验证。",
    },
    {
        "key": "kiro",
        "name": "Amazon Kiro",
        "category": "app",
        "tier": "medium",
        "url": "https://kiro.dev/",
        "note": "spec 驱动 agentic IDE，可用 Claude Sonnet 4.5 等；app-only。",
    },
]


def read_json_links(path: Path) -> dict[str, str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit(f"配置文件必须是 JSON object: {path}")
    return {str(k): str(v) for k, v in data.items() if v}


def load_links(path: str | None) -> tuple[dict[str, str], set[str]]:
    default_path = Path(__file__).resolve().parents[1] / "references" / "default_links.json"
    links = read_json_links(default_path) if default_path.exists() else {}
    author_link_keys = set(links)
    if not path:
        return links, author_link_keys
    p = Path(path).expanduser()
    if not p.exists():
        raise SystemExit(f"配置文件不存在: {p}")
    custom_links = read_json_links(p)
    links.update(custom_links)
    author_link_keys.difference_update(custom_links)
    return links, author_link_keys


def open_url(url: str) -> None:
    if sys.platform == "darwin":
        subprocess.run(["open", url], check=False)
    else:
        webbrowser.open_new_tab(url)


def main() -> int:
    parser = argparse.ArgumentParser(description="Open curated AI free-credit pages.")
    parser.add_argument("--config", help="JSON file mapping site keys to referral URLs.")
    parser.add_argument("--category", choices=["all", "api", "app"], default="all")
    parser.add_argument("--tier", choices=["high", "medium", "all"], help="Default: high; all when --only is given.")
    parser.add_argument("--only", help="Comma-separated site keys (e.g. kimi,coze).")
    parser.add_argument("--dry-run", action="store_true", help="Print URLs without opening them.")
    args = parser.parse_args()

    links, author_link_keys = load_links(args.config)
    only_keys = None
    if args.only:
        only_keys = {key.strip() for key in args.only.split(",") if key.strip()}
        unknown = sorted(only_keys - {site["key"] for site in SITES})
        if unknown:
            print(f"未知 key：{', '.join(unknown)}。合法 key：{', '.join(site['key'] for site in SITES)}")
            return 1
    tier = args.tier or ("all" if only_keys else "high")
    selected = []
    for site in SITES:
        if only_keys is not None and site["key"] not in only_keys:
            continue
        if args.category != "all" and site["category"] != args.category:
            continue
        if tier != "all" and site["tier"] != tier:
            continue
        url = links.get(site["key"], site["url"])
        selected.append((site, url))

    if not selected:
        print("没有匹配的网站。")
        return 1

    selected_author_links = [site["name"] for site, _ in selected if site["key"] in author_link_keys]
    selected_custom_links = [
        site["name"]
        for site, _ in selected
        if site["key"] in links and site["key"] not in author_link_keys
    ]
    if selected_author_links:
        print(
            "提示：以下入口使用 Skill 作者的邀请链接，作者可能获得平台奖励："
            + "、".join(selected_author_links)
            + "。可用 --config 替换，或删除 default_links.json 中的对应条目。"
        )
    if selected_custom_links:
        print("提示：以下入口使用了你的自定义链接：" + "、".join(selected_custom_links) + "。")

    for site, url in selected:
        print(f"{site['name']} [{site['key']}]")
        print(f"  URL: {url}")
        print(f"  NOTE: {site['note']}")
        if not args.dry_run:
            open_url(url)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
