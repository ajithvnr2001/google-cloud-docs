#!/usr/bin/env python3
"""Resumable sitemap inventory for docs.cloud.google.com.
Saves per-shard URL lists + _progress.json + STATUS lines under /data,
so a crash/restart resumes by skipping finished shards.
"""
import asyncio, json, time, pathlib, sys
from datetime import datetime, timezone

ROOT = pathlib.Path("/data/opencode/gcpdocs")
SEEDS = ROOT / "seeds"
STATUS_LOG = ROOT / "STATUS.log"
SNAP = ROOT / "STATUS.json"

def log(msg):
    line = f"{datetime.now(timezone.utc).isoformat()} [inventory] {msg}"
    print(line, flush=True)
    with open(STATUS_LOG, "a") as f:
        f.write(line + "\n")

async def get(c, u, sem):
    async with sem:
        for attempt in range(4):
            try:
                import httpx
                r = await c.get(u, timeout=90); r.raise_for_status()
                import re
                return u, re.findall(r"<loc>([^<]+)</loc>", r.text)
            except Exception as e:
                if attempt == 3:
                    return u, f"ERR {str(e)[:120]}"
                await asyncio.sleep(5)

async def main():
    import httpx
    SEEDS.mkdir(parents=True, exist_ok=True)
    urls = [l.strip() for l in open("/tmp/gcp-sitemaps-real.txt") if l.strip()]
    prog_f = SEEDS / "_progress.json"
    prog = json.loads(prog_f.read_text()) if prog_f.exists() else {}
    todo = [u for u in urls if prog.get(u, {}).get("done")]
    pending = [u for u in urls if u not in todo]
    log(f"sitemap files={len(urls)} done={len(todo)} pending={len(pending)}")
    sem = asyncio.Semaphore(8)
    async with httpx.AsyncClient(follow_redirects=True, timeout=90) as c:
        for i in range(0, len(pending), 8):
            batch = pending[i:i + 8]
            res = await asyncio.gather(*[get(c, u, sem) for u in batch])
            for u, locs in res:
                if isinstance(locs, str):
                    prog[u] = {"done": False, "error": locs}
                    log(f"FAIL {u.split('/')[-1]} {locs}")
                else:
                    name = u.split("/")[-1].replace(".xml", ".txt")
                    (SEEDS / name).write_text("\n".join(locs))
                    prog[u] = {"done": True, "urls": len(locs)}
                    log(f"shard {name} urls={len(locs)}")
            prog_f.write_text(json.dumps(prog, indent=2))
    total = sum(v.get("urls", 0) for v in prog.values() if v.get("done"))
    with open(SEEDS / "ALL_URLS.txt", "w") as f:
        for u in urls:
            name = u.split("/")[-1].replace(".xml", ".txt")
            p = SEEDS / name
            if p.exists():
                f.write(p.read_text() + "\n")
    SNAP.write_text(json.dumps({"phase": "inventory", "shards_done": sum(1 for v in prog.values() if v.get("done")),
                                "total_urls": total, "updated": datetime.now(timezone.utc).isoformat()}, indent=2))
    log(f"DONE total_urls={total}")

if __name__ == "__main__":
    asyncio.run(main())
