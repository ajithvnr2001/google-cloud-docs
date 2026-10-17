#!/usr/bin/env python3
"""Final gap-fill: fetch URLs from missing_urls.txt with the same stack + save format as crawl_gcp.py.
Run: python3 final_gapfill.py   (reads missing_urls.txt, resumes-safe via sqlite visited table)
"""
import asyncio, sqlite3, json, importlib.util, sys
from pathlib import Path
from datetime import datetime, timezone
import httpx

ROOT = Path("/data/opencode/gcpdocs")
spec = importlib.util.spec_from_file_location("cg", str(ROOT / "crawl_gcp.py"))
cg = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cg)

async def fetch_txt_raw(url):
    async with httpx.AsyncClient(follow_redirects=True, timeout=25) as c:
        resp = await c.get(url)
        resp.raise_for_status()
        body = resp.text
    name = url.rsplit("/", 1)[-1].removesuffix(".txt")
    title = name.replace("-", " ").replace("_", " ") or url
    return {"url": url, "title": title, "html": "", "markdown": f"# {title}\n\n> Source: {url}\n\n{body}",
            "links": [], "method": "httpx-raw-text"}

async def main():
    urls = [l.strip() for l in (ROOT / "missing_urls.txt").read_text().splitlines() if l.strip()]
    con = sqlite3.connect(ROOT / "crawl_state.db")
    have = set()
    for i in range(0, len(urls), 500):
        chunk = urls[i:i + 500]
        q = f"SELECT url FROM visited WHERE url IN ({','.join('?' * len(chunk))})"
        have |= {r[0] for r in con.execute(q, chunk)}
    todo = [u for u in urls if u not in have and not u.lower().endswith(".pdf")]
    print(f"total={len(urls)} already_visited={len(have)} pdf_skipped={sum(1 for u in urls if u.lower().endswith('.pdf'))} todo={len(todo)}", flush=True)
    idx_f = open(ROOT / "docs" / "_index.jsonl", "a")
    sem = asyncio.Semaphore(10)

    async def one(u):
        async with sem:
            try:
                data = await fetch_txt_raw(u) if u.endswith(".txt") else await cg.fetch_one(u)
            except Exception as e:
                con.execute("INSERT OR REPLACE INTO failed VALUES (?,?)", (u, f"gapfill: {str(e)[:380]}"))
                con.commit()
                print("[fail]", u[:110], str(e)[:70], flush=True)
                return
            rel = cg.url_to_relpath(u)
            fpath = cg.OUT_ROOT / rel
            fpath.parent.mkdir(parents=True, exist_ok=True)
            fm = f"---\nurl: {u}\ntitle: {json.dumps(data['title'])[1:-1]}\nmethod: {data['method']}\nfetched_at: {datetime.now(timezone.utc).isoformat()}\n---\n\n"
            fpath.write_text(fm + data["markdown"], encoding="utf-8")
            meta_rel = Path("_meta") / (rel.with_suffix(".json") if rel.suffix == ".md" else Path(str(rel) + ".json"))
            (cg.OUT_ROOT / meta_rel).parent.mkdir(parents=True, exist_ok=True)
            (cg.OUT_ROOT / meta_rel).write_text(json.dumps(
                {"url": u, "file": str(rel), "title": data["title"], "method": data["method"],
                 "fetched_at": datetime.now(timezone.utc).isoformat()}, indent=2), encoding="utf-8")
            con.execute("INSERT OR REPLACE INTO visited VALUES (?,?,?,?,?)",
                        (u, str(rel), data["title"], data["method"], datetime.now(timezone.utc).isoformat()))
            con.commit()
            idx_f.write(json.dumps({"url": u, "file": str(rel), "title": data["title"], "method": data["method"]}) + "\n")
            print("[ok]", u[:110], flush=True)

    await asyncio.gather(*(one(u) for u in todo))
    idx_f.close()
    print("GAPFILL DONE", flush=True)

asyncio.run(main())
