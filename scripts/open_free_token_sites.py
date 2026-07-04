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
        "url": "https://www.bigmodel.cn/console/overview?showUppop=true",
        "note": "API/控制台资源包；如有用户邀请链接则优先打开。",
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
        "note": "新用户 API 代金券；通常没有个人邀请奖励。",
    },
    {
        "key": "coze",
        "name": "扣子 Coze",
        "category": "app",
        "tier": "high",
        "url": "https://www.coze.cn/studio",
        "note": "扣子积分/邀请奖励；App/Agent 内专用，不是通用 API key。",
    },
    {
        "key": "dashscope",
        "name": "阿里百炼",
        "category": "api",
        "tier": "medium",
        "url": "https://bailian.console.aliyun.com/",
        "note": "中优先级；活动常变，打开前应先核验。",
    },
    {
        "key": "modelscope",
        "name": "ModelScope",
        "category": "api",
        "tier": "medium",
        "url": "https://www.modelscope.cn/my/myaccesstoken",
        "note": "中优先级；活动常变，打开前应先核验。",
    },
]


def load_links(path: str | None) -> dict[str, str]:
    if not path:
        return {}
    p = Path(path).expanduser()
    if not p.exists():
        raise SystemExit(f"配置文件不存在: {p}")
    data = json.loads(p.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise SystemExit("配置文件必须是 JSON object，例如 {\"coze\":\"https://...\"}")
    return {str(k): str(v) for k, v in data.items() if v}


def open_url(url: str) -> None:
    if sys.platform == "darwin":
        subprocess.run(["open", url], check=False)
    else:
        webbrowser.open_new_tab(url)


def main() -> int:
    parser = argparse.ArgumentParser(description="Open curated AI free-credit pages.")
    parser.add_argument("--config", help="JSON file mapping site keys to referral URLs.")
    parser.add_argument("--category", choices=["all", "api", "app"], default="all")
    parser.add_argument("--tier", choices=["high", "medium", "all"], default="high")
    parser.add_argument("--dry-run", action="store_true", help="Print URLs without opening them.")
    args = parser.parse_args()

    links = load_links(args.config)
    selected = []
    for site in SITES:
        if args.category != "all" and site["category"] != args.category:
            continue
        if args.tier != "all" and site["tier"] != args.tier:
            continue
        url = links.get(site["key"], site["url"])
        selected.append((site, url))

    if not selected:
        print("没有匹配的网站。")
        return 1

    for site, url in selected:
        print(f"{site['name']} [{site['key']}]")
        print(f"  URL: {url}")
        print(f"  NOTE: {site['note']}")
        if not args.dry_run:
            open_url(url)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
