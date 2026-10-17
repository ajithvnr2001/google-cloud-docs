#!/usr/bin/env python3
"""Incremental update for docs.cloud.google.com — same mechanics as the
cloudflare/copilotkit/ai-docs updaters: crawl NEW sitemap docs AND refetch
pages whose sitemap lastmod is newer than our fetched_at (newest first, capped).

State lives in crawl_state.db (sqlite `visited`, incl. per-row fetched_at), so this
never re-crawls existing content. Output format identical to crawl_gcp.py
(frontmatter .md + _meta/*.json + _index.jsonl).

Usage:
  python3 update_gcp.py --check-only                 # diff only, no writes
  python3 update_gcp.py --concurrency 20             # full incremental pass
  python3 update_gcp.py --refresh-cap 400 ...        # refresh more stale pages
  python3 update_gcp.py ... --publish-delta          # also tar today's changes into releases/docs-delta-<date>.tar.gz
"""
import argparse, asyncio, json, re, sqlite3, sys, tarfile
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import crawl_gcp as cg  # normalize_url, url_to_relpath, fetch_one, OUT_ROOT

INDEX_URL = "https://docs.cloud.google.com/sitemap.xml"
DEFAULT_REFRESH_CAP = 600
REFRESH_SOFT_CAP = 5000  # safety abort if stale list explodes (site overhaul)
STATE_LOG = ROOT / "STATUS.log"
STATUS_JSON = ROOT / "STATUS.json"
REL_DIR = ROOT / "releases"


def glog(msg):
    line = f"{datetime.now(timezone.utc).isoformat()} [update] {msg}"
    print(line, flush=True)
    try:
        with open(STATE_LOG, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass


async def fetch_sitemap_urls(concurrency=8):
    """Return (live_urls_set, lastmod_dict{url: lastmod}). Discovers shard files live (no /tmp dependency).
    loc and lastmod may be separated by whitespace (GCP shards put lastmod on its own line)."""
    import httpx
    live_urls, lastmod = set(), {}
    async with httpx.AsyncClient(follow_redirects=True, timeout=90) as c:
        r = await c.get(INDEX_URL)
        r.raise_for_status()
        files = sorted(set(re.findall(r"https://docs\.cloud\.google\.com/sitemap[^<]*\.xml", r.text)))
        glog(f"sitemap index -> {len(files)} shard files")
        sem = asyncio.Semaphore(concurrency)

        async def one(sm):
            async with sem:
                for attempt in range(4):
                    try:
                        rr = await c.get(sm, timeout=120)
                        rr.raise_for_status()
                        text = rr.text
                        for loc in re.findall(r"<loc>([^<]+)</loc>", text):
                            n = cg.normalize_url(loc)
                            if n:
                                live_urls.add(n)
                        for u, d in re.findall(r"<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>", text):
                            n = cg.normalize_url(u)
                            if n and (n not in lastmod or d > lastmod[n]):
                                lastmod[n] = d
                        return
                    except Exception as e:
                        if attempt == 3:
                            glog(f"FAIL {sm}{str(e)[:100]}")
                        await asyncio.sleep(5)

        await asyncio.gather(*(one(sm) for sm in files))
    return live_urls, lastmod


def db_state():
    con = sqlite3.connect(ROOT / "crawl_state.db")
    con.execute("PRAGMA journal_mode=WAL")
    return con


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check-only", action="store_true")
    ap.add_argument("--concurrency", type=int, default=20)
    ap.add_argument("--refresh-cap", type=int, default=DEFAULT_REFRESH_CAP)
    ap.add_argument("--publish-delta", action="store_true")
    ap.add_argument("--force", default=None)
    a = ap.parse_args()
    asyncio.run(run(a))


async def run(a):
    live, lastmod = await fetch_sitemap_urls()
    glog(f"live sitemap urls (normalized): {len(live)} (lastmod tracked: {len(lastmod)})")

    con = db_state()
    visited = {}
    n = con.execute("SELECT COUNT(*) FROM visited").fetchone()[0]
    glog(f"db visited rows: {n}")
    # stream rows (607k — don't load blindly; but a dict of url->fetched_at is fine ~200MB RSS)
    for u, fa in con.execute("SELECT url, fetched_at FROM visited"):
        visited[u] = fa

    new = [u for u in live if u not in visited]
    glog(f"new since last state: {len(new)}")

    stale = []
    for u, d in lastmod.items():
        fa = visited.get(u)
        if not fa:
            continue
        try:
            if datetime.fromisoformat(d) > datetime.fromisoformat(fa.replace("Z", "+00:00")):
                stale.append((d, u))
        except Exception:
            pass
    stale.sort(reverse=True)
    glog(f"stale (lastmod > fetched_at): {len(stale)}")
    refresh = [u for _, u in stale[:a.refresh_cap]]
    if len(stale) > REFRESH_SOFT_CAP:
        glog(f"NOTE: big backlog ({len(stale)} > {REFRESH_SOFT_CAP}): crawling all {len(new)} NEW pages now and "
             f"draining {len(refresh)} newest stale pages (cap {a.refresh_cap}/run; {len(stale)} total backlog). "
             "For a faster drain run with --refresh-cap 4000 for a few days; for one-shot 100% freshness re-run crawl_gcp.py.")
        if len(stale) > 300000:
            glog("SEVERE backlog (>half the corpus): lastmod regeneration suggests a site overhaul — schedule a full crawl_gcp.py redo.")

    if a.check_only:
        print("\n-- NEW --")
        for u in new[:30]:
            print("  NEW:", u)
        print("-- REFRESH (newest first) --")
        for u in refresh[:20]:
            print("  REFRESH:", u)
        print(f"summary: live={len(live)} new={len(new)} stale={len(stale)} would_refresh={len(refresh)}")
        con.close()
        return

    targets = ([a.force] if a.force else []) + new + refresh
    if not targets:
        stamp = {"date": datetime.now(timezone.utc).strftime("%F"), "new": 0, "refreshed": 0, "stale": len(stale)}
        write_status(stamp, con)
        glog("no changes — up to date")
        con.close()
        return

    glog(f"fetching {len(targets)} pages ({len(new)} new + {len(refresh)} refresh)...")
    idx_path = cg.OUT_ROOT / "_index.jsonl"
    changed_relpaths = []
    sem = asyncio.Semaphore(a.concurrency)
    ok = fail = 0

    async def one(url):
        nonlocal ok, fail
        async with sem:
            try:
                data = await cg.fetch_one(url)
            except Exception as e:
                con.execute("INSERT OR REPLACE INTO failed VALUES (?,?)", (url, f"update: {str(e)[:380]}"))
                con.commit()
                fail += 1
                glog(f"[fail] {url} {str(e)[:80]}")
                return
            rel = cg.url_to_relpath(url)
            fpath = cg.OUT_ROOT / rel
            fpath.parent.mkdir(parents=True, exist_ok=True)
            now = datetime.now(timezone.utc).isoformat()
            fm = f"---\nurl: {url}\ntitle: {json.dumps(data['title'])[1:-1]}\nmethod: {data['method']}\nfetched_at: {now}\n---\n\n"
            fpath.write_text(fm + data["markdown"], encoding="utf-8")
            meta_rel = Path("_meta") / (rel.with_suffix(".json") if rel.suffix == ".md" else Path(str(rel) + ".json"))
            (cg.OUT_ROOT / meta_rel).parent.mkdir(parents=True, exist_ok=True)
            (cg.OUT_ROOT / meta_rel).write_text(json.dumps(
                {"url": url, "file": str(rel), "title": data["title"], "method": data["method"], "fetched_at": now},
                indent=2), encoding="utf-8")
            con.execute("INSERT OR REPLACE INTO visited VALUES (?,?,?,?,?)", (url, str(rel), data["title"], data["method"], now))
            con.commit()
            with open(idx_path, "a") as f:
                f.write(json.dumps({"url": url, "file": str(rel), "title": data["title"], "method": data["method"]}) + "\n")
            changed_relpaths.append(str(rel))
            ok += 1
            glog(f"[ok] {url[:110]}")

    await asyncio.gather(*(one(u) for u in targets))
    stamp = {"date": datetime.now(timezone.utc).strftime("%F"), "at": datetime.now(timezone.utc).isoformat(),
             "new": len(new), "refreshed": len(refresh), "fetched_ok": ok, "fetched_fail": fail,
             "stale_total": len(stale), "stale_backlog": len(stale) - len(refresh), "visited_total": n + len(new)}
    write_status(stamp, con)
    con.close()
    glog(f"done ok={ok} fail={fail}")

    if a.publish_delta and changed_relpaths:
        publish_delta(changed_relpaths, stamp)


def write_status(stamp, con):
    try:
        snap = json.loads(STATUS_JSON.read_text()) if STATUS_JSON.exists() else {}
        snap.update({"phase": "update", "last_update": stamp, "updated": datetime.now(timezone.utc).isoformat(),
                     "visited": con.execute("SELECT COUNT(*) FROM visited").fetchone()[0]})
        STATUS_JSON.write_text(json.dumps(snap, indent=2))
    except Exception as e:
        glog(f"status write skip: {e}")


def publish_delta(relpaths, stamp):
    """Tar changed pages (paths relative to docs/) into releases/docs-delta-<date>.tar.gz."""
    REL_DIR.mkdir(exist_ok=True, parents=True)
    out = REL_DIR / f"docs-delta-{stamp['date']}.tar.gz"
    base = cg.OUT_ROOT
    with tarfile.open(out, "w:gz") as tar:
        for rel in relpaths:
            for p in (Path(rel), Path("_meta") / (Path(rel).with_suffix(".json") if Path(rel).suffix == ".md" else Path(str(rel) + ".json"))):
                fp = base / p
                if fp.exists():
                    tar.add(fp, arcname=str(p))
    glog(f"delta published: {out} ({len(relpaths)} pages, {out.stat().st_size // 1024} KB)")
    (REL_DIR / f"docs-delta-{stamp['date']}.manifest.txt").write_text("\n".join(sorted(relpaths)) + "\n")


if __name__ == "__main__":
    main()
