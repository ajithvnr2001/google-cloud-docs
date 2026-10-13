#!/usr/bin/env python3
"""Coder: incremental update without recrawling (docs.cloud.google.com).
Reads seeds/ALL_URLS.txt (or live sitemap), diffs vs docs/_index.jsonl.
Usage:
  python3 coder_update.py --check-only
  python3 coder_update.py --run --concurrency 10
"""
import argparse, json, re, asyncio, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
from guide_code.coder_scrape import scrape

REPO = pathlib.Path(__file__).resolve().parents[1]
DOCS = REPO / "docs"

def canon(u):
    from urllib.parse import urlparse, urljoin, urldefrag
    abs_u, _ = urldefrag(urljoin("https://docs.cloud.google.com", u.strip()))
    p = urlparse(abs_u)
    c = f"{p.scheme}://{p.netloc}{p.path}"
    if not c.endswith("/") and "." not in c.rsplit("/", 1)[-1]:
        c += "/"
    return c

async def live():
    import httpx
    async with httpx.AsyncClient(follow_redirects=True, timeout=60) as c:
        idx = (await c.get("https://docs.cloud.google.com/sitemap.xml")).text
        sms = sorted(set(re.findall(r"<loc>(https://docs\.cloud\.google\.com/sitemap[^<]+)</loc>", idx)))
        out = set()
        for sm in sms:
            try:
                t = (await c.get(sm, timeout=60)).text
                out.update(canon(u) for u in re.findall(r"<loc>([^<]+)</loc>", t))
            except Exception as e:
                print("sitemap fail", sm, str(e)[:80])
    return sorted(out)

async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--concurrency", type=int, default=10)
    a = ap.parse_args()
    indexed = {json.loads(l)["url"] for l in open(DOCS / "_index.jsonl")} if (DOCS / "_index.jsonl").exists() else set()
    lv = await live()
    new = [u for u in lv if u not in indexed and ".json" not in u and "`" not in u]
    print(f"live={len(lv)} indexed={len(indexed)} new={len(new)}")
    for u in new[:20]:
        print(" NEW:", u)
    if a.check_only or not a.run or not new:
        return
    import sys as _s
    _s.path.insert(0, str(REPO))
    from crawl_gcp import url_to_relpath
    sem = asyncio.Semaphore(a.concurrency)
    idx = open(DOCS / "_index.jsonl", "a")
    async def one(u):
        async with sem:
            md, title, method = await scrape(u)
            rel = url_to_relpath(u)
            (DOCS / rel).parent.mkdir(parents=True, exist_ok=True)
            (DOCS / rel).write_text(md)
            idx.write(json.dumps({"url": u, "file": str(rel), "title": title, "method": method}) + "\n")
            print("[ok]", u)
    await asyncio.gather(*(one(u) for u in new))
    idx.close()

if __name__ == "__main__":
    asyncio.run(main())
