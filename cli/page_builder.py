#!/usr/bin/env python3
"""
Open Growth Intelligence — Page Builder CLI
用法:
  python3 -m cli.page_builder --list                  # 查看所有页面状态
  python3 -m cli.page_builder --fetch <slug>           # 抓取单页竞品
  python3 -m cli.page_builder --fetch-all              # 抓取所有 pending 页面竞品
  python3 -m cli.page_builder --fetch-all --dry-run    # 模拟抓取（不实际请求）
  python3 -m cli.page_builder --mark-built <slug>      # 标记页面为已完成
"""

import sys
import time
import yaml
import requests
import html2text
from pathlib import Path


# ── 路径配置 ───────────────────────────────────────────────────────────────────
BUILDER_DIR   = Path(__file__).parent
MANIFEST_PATH  = BUILDER_DIR / "pages_manifest.yaml"
COMPETITOR_DIR = BUILDER_DIR / "competitor_structures"


def set_manifest_path(path: Path):
    global MANIFEST_PATH
    MANIFEST_PATH = path


def set_competitor_dir(path: Path):
    global COMPETITOR_DIR
    COMPETITOR_DIR = path


# ── 竞品抓取 ───────────────────────────────────────────────────────────────────
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


def fetch_competitor(url: str) -> str:
    try:
        r = requests.get(url, headers=HEADERS, timeout=20)
        r.raise_for_status()
        h = html2text.HTML2Text()
        h.ignore_links = True
        h.ignore_images = True
        h.body_width = 0
        return h.handle(r.text)[:8000]
    except Exception as e:
        print(f"  [warn] fetch failed: {e}")
        return f"[Fetch failed: {url}] {e}"


def competitor_cache_path(slug: str, competitor_url: str) -> Path:
    domain = competitor_url.split("/")[2] if competitor_url.startswith("http") else "unknown"
    return COMPETITOR_DIR / f"{domain}_{slug}.md"


def fetch_and_cache(page_info: dict, dry_run: bool = False) -> bool:
    slug = page_info["slug"]
    url  = page_info.get("competitor_url", "")
    if not url:
        print(f"  [skip] {slug}: 无 competitor_url")
        return False

    path = competitor_cache_path(slug, url)
    if path.exists():
        print(f"  [cached] {slug}: {path.name}")
        return True

    if dry_run:
        print(f"  [dry-run] 会抓取: {url}")
        return True

    print(f"  [fetch] {slug}: {url}")
    md = fetch_competitor(url)
    COMPETITOR_DIR.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"# 竞品结构存档：{url.split('/')[2]} / {slug}\n\n"
        f"> 采集日期：2026-06-29\n> 来源 URL：{url}\n\n---\n\n{md}",
        encoding="utf-8"
    )
    print(f"  [saved] {path.name}")
    return True


# ── manifest 读写 ──────────────────────────────────────────────────────────────
def load_manifest(path: Path = None) -> dict:
    target = path or MANIFEST_PATH
    raw = yaml.safe_load(target.read_text(encoding="utf-8"))
    return {p["slug"]: p for p in raw["pages"]}


def save_manifest(pages: dict, path: Path = None):
    target = path or MANIFEST_PATH
    data = {"pages": list(pages.values())}
    target.write_text(
        yaml.dump(data, allow_unicode=True, default_flow_style=False, sort_keys=False),
        encoding="utf-8"
    )


# ── CLI ────────────────────────────────────────────────────────────────────────
def cmd_list(pages: dict):
    print(f"\n{'序':>3}  {'状态':5}  {'类型':10}  {'页面名称':40}  P1  搜索量  竞品缓存")
    print("-" * 100)
    for i, (slug, info) in enumerate(pages.items(), 1):
        status_icon = "✓" if info.get("status") == "built" else "○"
        cat = f"{info['page_type']}型/{info['tool_category'][:8]}"
        url = info.get("competitor_url", "")
        cache_path = competitor_cache_path(slug, url) if url else None
        cached = "✓" if (cache_path and cache_path.exists()) else "-"
        print(f"{i:>3}  {status_icon:5}  {cat:10}  {info['name']:40}  {info.get('p1',0):2}  {info.get('search_vol',0):>8,}  {cached}")
    built   = sum(1 for p in pages.values() if p.get("status") == "built")
    pending = len(pages) - built
    print(f"\n已完成: {built} / {len(pages)}   待构建: {pending}")


def cmd_fetch(pages: dict, slug: str, dry_run: bool):
    if slug not in pages:
        print(f"✗ 未知页面: {slug}"); return
    fetch_and_cache(pages[slug], dry_run=dry_run)


def cmd_fetch_all(pages: dict, dry_run: bool):
    pending = [p for p in pages.values() if p.get("status") != "built"]
    print(f"\n抓取 {len(pending)} 个 pending 页面的竞品...\n")
    for info in pending:
        fetch_and_cache(info, dry_run=dry_run)
        if not dry_run:
            time.sleep(1)
    print("\n完成")


def cmd_mark_built(pages: dict, slug: str):
    if slug not in pages:
        print(f"✗ 未知页面: {slug}"); return
    pages[slug]["status"] = "built"
    save_manifest(pages)
    print(f"✓ 已标记为 built: {slug}")


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__); return

    pages    = load_manifest()
    dry_run  = "--dry-run" in args
    pos_args = [a for a in args if not a.startswith("--")]

    if "--list" in args:
        cmd_list(pages)

    elif "--fetch-all" in args:
        cmd_fetch_all(pages, dry_run=dry_run)

    elif "--fetch" in args:
        slug = pos_args[0] if pos_args else ""
        if not slug:
            print("用法: python3 -m cli.page_builder --fetch <slug>"); return
        cmd_fetch(pages, slug, dry_run=dry_run)

    elif "--mark-built" in args:
        slug = pos_args[0] if pos_args else ""
        if not slug:
            print("用法: python3 -m cli.page_builder --mark-built <slug>"); return
        cmd_mark_built(pages, slug)

    else:
        print(__doc__)


if __name__ == "__main__":
    main()
