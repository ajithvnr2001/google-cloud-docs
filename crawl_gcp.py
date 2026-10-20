#!/usr/bin/env python3
"""
End-to-end crawler for https://developers.cloudflare.com/ including subdomains.
Uses all three requested stacks:
  1. Scrapling (D4Vinci/Scrapling)  - fast static fetch + CSS/XPath extraction (primary)
  2. Crawl4AI (unclecode/crawl4AI)   - JS rendering fallback + markdown generation
  3. ScrapeGraphAI (ScrapeGraphAI/Scrapegraph-ai) - cleanup_html + convert_to_md (HTML->MD)

Saves markdown docs to /data/opencode/cloudflare/docs
"""
import asyncio
import os
import re
import json
import time
import hashlib
import importlib.util
from pathlib import Path
from urllib.parse import urlparse, urljoin, urldefrag, unquote
from datetime import datetime, timezone

import httpx
from bs4 import BeautifulSoup

# ---------- paths (repo-relative so GitHub Actions runners work; override via env) ----------
REPO_ROOT = Path(__file__).resolve().parent
BASE_URL = "https://docs.cloud.google.com"
SITEMAP_INDEX = "https://docs.cloud.google.com/sitemap.xml"
MAIN_LLMS = "https://docs.cloud.google.com/llms.txt"
OUT_ROOT = Path(os.environ.get("DOCS_OUT", str(REPO_ROOT / "docs")))
TOOLS_ROOT = Path(os.environ.get("TOOLS_DIR", str(REPO_ROOT / "tools")))
STATE_FILE = Path(os.environ.get("CRAWL_STATE", str(REPO_ROOT / "crawl_state.json")))
SEEDS_DIR = Path(os.environ.get("SEEDS_DIR", str(REPO_ROOT / "seeds")))
DB_FILE = Path(os.environ.get("CRAWL_DB", str(REPO_ROOT / "crawl_state.db")))
STATUS_LOG = Path(os.environ.get("STATUS_LOG", str(REPO_ROOT / "STATUS.log")))
STATUS_JSON = Path(os.environ.get("STATUS_JSON", str(REPO_ROOT / "STATUS.json")))
INDEX_FILE = OUT_ROOT / "_index.jsonl"
MANIFEST_FILE = OUT_ROOT / "_manifest.json"

OUT_ROOT.mkdir(parents=True, exist_ok=True)
(OUT_ROOT / "_subdomains").mkdir(exist_ok=True, parents=True)
(OUT_ROOT / "_llms").mkdir(exist_ok=True, parents=True)
(OUT_ROOT / "_meta").mkdir(exist_ok=True, parents=True)

# ---------- load ScrapeGraphAI utils directly from cloned repo (bypass broken langchain imports) ----------
def load_module_from_file(name, filepath):
    spec = importlib.util.spec_from_file_location(name, filepath)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

def _resolve_sg_utils():
    cands = [
        TOOLS_ROOT / "scrapegraph-ai" / "scrapegraphai" / "utils",
        REPO_ROOT / "tools" / "scrapegraph-ai" / "scrapegraphai" / "utils",
        Path("/data/opencode/cloudflare/tools/scrapegraph-ai/scrapegraphai/utils"),
    ]
    for c in cands:
        if (c / "convert_to_md.py").exists():
            return c
    try:  # pip-installed package fallback (utils files are langchain-free)
        import scrapegraphai
        c = Path(scrapegraphai.__file__).parent / "utils"
        if (c / "convert_to_md.py").exists():
            return c
    except Exception:
        pass
    return cands[0]

SCRAPEGRAPH_UTILS = _resolve_sg_utils()
convert_to_md_mod = load_module_from_file("sg_convert_to_md", str(SCRAPEGRAPH_UTILS / "convert_to_md.py"))
cleanup_html_mod = load_module_from_file("sg_cleanup_html", str(SCRAPEGRAPH_UTILS / "cleanup_html.py"))
sg_convert_to_md = convert_to_md_mod.convert_to_md
try:
    sg_cleanup_html = cleanup_html_mod.cleanup_html
    print("[scrapegraph-ai] loaded convert_to_md + cleanup_html from", SCRAPEGRAPH_UTILS)
except Exception as e:
    sg_cleanup_html = None
    print("[scrapegraph-ai] cleanup_html unavailable:", e)

# ---------- Scrapling ----------
from scrapling import Fetcher
print("[scrapling] Fetcher loaded:", Fetcher)

# ---------- Crawl4AI (lazy, only for fallback) ----------
_crawler = None
async def get_crawler():
    global _crawler
    if _crawler is None:
        from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode  # noqa
        from crawl4ai.async_webcrawler import BrowserConfig
        browser_cfg = BrowserConfig(headless=True, verbose=False)
        _crawler = AsyncWebCrawler(config=browser_cfg)
        await _crawler.start()
        print("[crawl4ai] AsyncWebCrawler started")
    return _crawler

# ---------- helpers ----------
ALLOWED_ROOT_SUFFIXES = (".cloud.google.com", ".google.com")
MAIN_HOST = "docs.cloud.google.com"
# Non-doc google hosts seen in guides: fetched shallow (depth<=1), failures tolerated.
SHALLOW_HOSTS = ("developers.google.com", "support.google.com", "console.cloud.google.com")

def normalize_url(u, base=BASE_URL):
    if not u:
        return None
    u = u.strip()
    if u.startswith("#") or u.startswith("mailto:") or u.startswith("tel:") or u.startswith("javascript:") or u.startswith("data:"):
        return None
    abs_u = urljoin(base, u)
    abs_u, _ = urldefrag(abs_u)
    try:
        p = urlparse(abs_u)
    except Exception:
        return None
    if p.scheme not in ("http", "https"):
        return None
    host = p.netloc.lower().split(":")[0]
    if host == MAIN_HOST or host.endswith(".cloud.google.com") or host == "cloud.google.com":
        pass
    elif host.endswith(".google.com") or host == "google.com":
        pass  # reference domains inside guides: fetched shallow, see main loop
    else:
        return None
    # skip binary assets
    low = p.path.lower()
    for ext in (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico", ".css", ".js", ".woff", ".woff2", ".ttf", ".mp4", ".webm", ".zip", ".pdf"):
        if low.endswith(ext):
            # allow .pdf? skip for now to keep docs focused, but record
            return None
    # canonicalize: map /index.md -> /, /index -> /, *.md (doc source) -> HTML url
    # e.g. /zaraz/history/versions/index.md -> /zaraz/history/versions/
    #      /zaraz/history/versions/index -> /zaraz/history/versions/
    #      /zaraz/history/versions.md -> /zaraz/history/versions/
    path = p.path
    if path.endswith("/index.md"):
        path = path[:-len("/index.md")] + "/"
    elif path.endswith("/index"):
        # be careful: /index as root file vs legit slug ending with -index? only strip exact /index segment
        path = path[:-len("/index")] + "/"
    elif path == "/index.md" or path == "/index":
        path = "/"
    elif path.endswith(".md"):
        # product llms.txt markdown source links: strip .md -> trailing slash
        path = path[:-3]
        if not path.endswith("/"):
            path = path + "/"
    # rebuild canonical url (drop query/fragment for docs; query hashed later only if needed)
    # keep query? docs don't need query; strip to dedupe (except search/page params handled via relpath hash, but we drop here)
    # Preserve query only if it looks like pagination? For now strip query to avoid dupes.
    canon = f"{p.scheme}://{p.netloc}{path}"
    # normalize trailing slash: keep "/" for root, ensure directory urls end with "/"
    # sitemap uses trailing slash, so enforce it for consistency (except files)
    if not canon.endswith("/") and "." not in canon.rsplit("/", 1)[-1]:
        canon = canon + "/"
    return canon

def url_to_relpath(url):
    p = urlparse(url)
    host = p.netloc.lower()
    path = unquote(p.path)
    # strip query for filename, but hash it if meaningful
    query = p.query
    path = path.strip("/")
    # canonical: trailing /index already stripped in normalize, but guard again
    if path.endswith("/index"):
        path = path[:-len("/index")].strip("/")
    if not path:
        fname = "_index"
    else:
        # remove trailing / already, keep hierarchy
        fname = path
    # sanitize each segment
    parts = []
    for seg in fname.split("/"):
        seg = re.sub(r'[<>:"\\|?*\x00-\x1F]', "_", seg).strip()
        if len(seg) > 120:
            seg = seg[:100] + "_" + hashlib.md5(seg.encode()).hexdigest()[:8]
        if seg in ("", ".", ".."):
            seg = "_"
        parts.append(seg)
    rel = "/".join(parts) if parts else "_index"
    if query:
        qh = hashlib.md5(query.encode()).hexdigest()[:8]
        rel = rel + f"__q_{qh}"
    if host == MAIN_HOST:
        return Path(rel + ".md")
    else:
        return Path("_subdomains") / host / (rel + ".md")

def extract_main_content_html(html, base_url):
    """Strip nav/header/footer, keep main article. Fallback to body."""
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    # Cloudflare docs use <main id="main-content"> or <article>
    main = soup.find("main") or soup.find("article") or soup.find("div", {"id": "main-content"})
    if main:
        # remove nav/aside inside main that is TOC
        return str(main), soup.title.string.strip() if soup.title and soup.title.string else ""
    # fallback: body
    body = soup.find("body")
    title = soup.title.string.strip() if soup.title and soup.title.string else ""
    if body:
        return str(body), title
    return html, title

def scrapegraph_markdown(html, url):
    try:
        return sg_convert_to_md(html, url)
    except Exception as e:
        # fallback html2text direct
        import html2text
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.body_width = 0
        return h.handle(html)

# ---------- fetch with Scrapling (sync -> thread) ----------
def scrapling_fetch_sync(url):
    t0 = time.time()
    page = Fetcher.get(url, stealthy_headers=True, follow_redirects=True, timeout=25)
    dt = time.time() - t0
    if page.status != 200:
        raise RuntimeError(f"scrapling status {page.status}")
    html = page.html_content
    if not html or len(html) < 500:
        raise RuntimeError("scrapling empty html")
    # links via css
    links = []
    try:
        for a in page.css("a"):
            href = a.attrib.get("href", "")
            if href:
                links.append(href)
    except Exception:
        pass
    # title
    title = ""
    try:
        t = page.css("title::text")
        if t:
            title = str(t[0]).strip()
    except Exception:
        pass
    if not title:
        try:
            h1 = page.css("h1::text")
            if h1:
                title = str(h1[0]).strip()
        except Exception:
            pass
    # text length check
    try:
        txt = page.text or ""
    except Exception:
        txt = ""
    return {"html": html, "links": links, "title": title, "text_len": len(txt), "elapsed": dt}

async def crawl4ai_fetch(url):
    crawler = await get_crawler()
    from crawl4ai import CrawlerRunConfig, CacheMode
    cfg = CrawlerRunConfig(
        cache_mode=CacheMode.BYPASS,
        only_text=False,
        excluded_tags=["nav", "footer", "header", "aside", "script", "style"],
        wait_until="domcontentloaded",
        page_timeout=45000,
    )
    res = await crawler.arun(url=url, config=cfg)
    if not res or not res.success:
        raise RuntimeError(f"crawl4ai failed: {getattr(res, 'error_message', 'unknown')}")
    html = res.html or ""
    md = res.markdown or ""
    # res.links: dict with internal/external
    links = []
    try:
        internal = (res.links or {}).get("internal", []) if isinstance(res.links, dict) else []
        external = (res.links or {}).get("external", []) if isinstance(res.links, dict) else []
        for l in (internal + external):
            href = l.get("href") if isinstance(l, dict) else str(l)
            if href:
                links.append(href)
    except Exception:
        pass
    title = ""
    try:
        if res.metadata and isinstance(res.metadata, dict):
            title = res.metadata.get("title", "") or ""
    except Exception:
        pass
    return {"html": html, "markdown": md, "links": links, "title": title}

async def fetch_one(url):
    """Try Scrapling -> Crawl4AI -> httpx. Returns dict with markdown, html, title, links, method."""
    # 1) Scrapling
    try:
        r = await asyncio.to_thread(scrapling_fetch_sync, url)
        html = r["html"]
        main_html, parsed_title = extract_main_content_html(html, url)
        title = r["title"] or parsed_title or url
        md_body = scrapegraph_markdown(main_html, url)
        header = f"# {title}\n\n> Source: {url}\n\n"
        md = header + md_body
        if len(md.strip()) < 800:
            raise RuntimeError(f"scrapling thin content ({len(md)} chars), fallback to crawl4ai")
        return {"url": url, "title": title, "html": html, "markdown": md, "links": r["links"], "method": "scrapling+scrapegraph"}
    except Exception as e1:
        last_err = f"scrapling: {e1}"
    # 2) Crawl4AI
    try:
        r = await crawl4ai_fetch(url)
        html = r["html"]
        md_raw = r["markdown"]
        title = r["title"]
        if not title:
            _, parsed_title = extract_main_content_html(html, url) if html else ("", "")
            title = parsed_title or url
        # run scrapegraph convert on main html too for consistency, prefer crawl4ai markdown if longer
        try:
            main_html, _ = extract_main_content_html(html, url) if html else ("", title)
            md_sg = scrapegraph_markdown(main_html, url) if main_html else ""
        except Exception:
            md_sg = ""
        md_best = md_raw if len(md_raw or "") >= len(md_sg or "") else md_sg
        header = f"# {title}\n\n> Source: {url}\n\n"
        md = header + (md_best or "")
        if len(md.strip()) < 200:
            raise RuntimeError(f"crawl4ai thin content: {last_err}")
        return {"url": url, "title": title, "html": html, "markdown": md, "links": r["links"], "method": f"crawl4ai+scrapegraph ({last_err})"}
    except Exception as e2:
        last_err2 = f"{last_err} | crawl4ai: {e2}"
    # 3) httpx fallback
    try:
        async with httpx.AsyncClient(follow_redirects=True, timeout=25, headers={"User-Agent": "Mozilla/5.0 (compatible; docs-crawler)"}) as c:
            resp = await c.get(url)
            resp.raise_for_status()
            html = resp.text
            main_html, parsed_title = extract_main_content_html(html, url)
            md_body = scrapegraph_markdown(main_html, url)
            title = parsed_title or url
            header = f"# {title}\n\n> Source: {url}\n\n"
            md = header + md_body
            soup = BeautifulSoup(html, "lxml")
            links = [a.get("href", "") for a in soup.find_all("a", href=True)]
            return {"url": url, "title": title, "html": html, "markdown": md, "links": links, "method": f"httpx+scrapegraph ({last_err2})"}
    except Exception as e3:
        raise RuntimeError(f"all fetchers failed for {url}: {last_err2} | httpx: {e3}")

# ---------- durable status + sqlite state (crash-resume safe, all under /data) ----------
import sqlite3

def status(msg):
    line = f"{datetime.now(timezone.utc).isoformat()} [crawl] {msg}"
    print(line, flush=True)
    try:
        with open(STATUS_LOG, "a") as f:
            f.write(line + "\n")
    except Exception:
        pass

def db():
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / "_meta").mkdir(parents=True, exist_ok=True)
    (OUT_ROOT / "_subdomains").mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(str(DB_FILE))
    con.execute("CREATE TABLE IF NOT EXISTS visited(url TEXT PRIMARY KEY, file TEXT, title TEXT, method TEXT, fetched_at TEXT)")
    con.execute("CREATE TABLE IF NOT EXISTS failed(url TEXT PRIMARY KEY, error TEXT)")
    con.execute("CREATE TABLE IF NOT EXISTS shards(name TEXT PRIMARY KEY, done INTEGER, total INTEGER, fetched INTEGER)")
    con.commit()
    return con

def snapshot(con, extra=None):
    try:
        v = con.execute("SELECT COUNT(*) FROM visited").fetchone()[0]
        f = con.execute("SELECT COUNT(*) FROM failed").fetchone()[0]
        done_sh = [r[0] for r in con.execute("SELECT name FROM shards WHERE done=1")]
        snap = {"phase": "crawl", "visited": v, "failed": f,
                "shards_done": len(done_sh), "updated": datetime.now(timezone.utc).isoformat()}
        try:  # merge over previous snapshot: preserves last_update block from the daily updater
            prev = json.loads(STATUS_JSON.read_text()) if STATUS_JSON.exists() else {}
        except Exception:
            prev = {}
        prev.update(snap)
        if extra:
            prev.update(extra)
        STATUS_JSON.write_text(json.dumps(prev, indent=2))
    except Exception:
        pass

def load_seed_shards():
    files = sorted(SEEDS_DIR.glob("sitemap_*.txt"))
    return files

# ---------- main crawl (shard by shard, resume-safe) ----------
async def main(concurrency=30):
    con = db()
    store = {"ok": 0, "fail": 0, "t0": time.time(), "last_snap": 0.0}
    try:
        store["ok"] = con.execute("SELECT COUNT(*) FROM visited").fetchone()[0]
    except Exception:
        pass
    idx_f = open(INDEX_FILE, "a", encoding="utf-8")
    sem = asyncio.Semaphore(concurrency)
    done_sh = {r[0] for r in con.execute("SELECT name FROM shards WHERE done=1")}
    status(f"resume: visited={store['ok']} shards_done={len(done_sh)} known")


    async def fetch_and_save(url, depth):
        async with sem:
            try:
                data = await fetch_one(url)
            except Exception as e:
                try:
                    con.execute("INSERT OR REPLACE INTO failed VALUES (?,?)", (url, str(e)[:400]))
                    con.commit()
                except Exception:
                    pass
                store["fail"] += 1
                return []
            try:
                rel = url_to_relpath(url)
                fpath = OUT_ROOT / rel
                fpath.parent.mkdir(parents=True, exist_ok=True)
                fm = f"---\nurl: {url}\ntitle: {json.dumps(data['title'])[1:-1]}\nmethod: {data['method']}\nfetched_at: {datetime.now(timezone.utc).isoformat()}\n---\n\n"
                fpath.write_text(fm + data["markdown"], encoding="utf-8")
                meta_rel = Path("_meta") / (rel.with_suffix(".json") if rel.suffix == ".md" else Path(str(rel) + ".json"))
                (OUT_ROOT / meta_rel).parent.mkdir(parents=True, exist_ok=True)
                (OUT_ROOT / meta_rel).write_text(json.dumps(
                    {"url": url, "file": str(rel), "title": data["title"], "method": data["method"],
                     "fetched_at": datetime.now(timezone.utc).isoformat()}, indent=2), encoding="utf-8")
                con.execute("INSERT OR REPLACE INTO visited VALUES (?,?,?,?,?)",
                            (url, str(rel), data["title"], data["method"], datetime.now(timezone.utc).isoformat()))
                con.commit()
                idx_f.write(json.dumps({"url": url, "file": str(rel), "title": data["title"], "method": data["method"]}) + "\n")
                store["ok"] += 1
                return data.get("links", [])
            except Exception as e:
                try:
                    con.execute("INSERT OR REPLACE INTO failed VALUES (?,?)", (url, f"save: {e}"[:400]))
                    con.commit()
                except Exception:
                    pass
                store["fail"] += 1
                return []

    async def crawl_shard(shard):
        raw = [l.strip() for l in shard.read_text().splitlines() if l.strip()]
        seeds, seen = [], set()
        for u in raw:
            n = normalize_url(u)
            if n and n not in seen:
                seen.add(n)
                seeds.append(n)
        try:
            con.execute("INSERT OR REPLACE INTO shards VALUES (?,?,?,?)", (shard.name, 0, len(seeds), 0))
            con.commit()
        except Exception:
            pass
        status(f"shard {shard.name}: {len(seeds)} seeds")
        todo = []
        for i in range(0, len(seeds), 2000):
            chunk = seeds[i:i + 2000]
            try:
                q = f"SELECT url FROM visited WHERE url IN ({','.join('?' * len(chunk))})"
                have = {r[0] for r in con.execute(q, chunk)}
            except Exception:
                have = set()
            todo.extend([(u, 0) for u in chunk if u not in have])
        status(f"shard {shard.name}: todo={len(todo)} (skipped visited)")
        queue = asyncio.Queue()
        queued = set(u for u, _ in todo)
        for item in todo:
            queue.put_nowait(item)

        async def worker():
            while True:
                try:
                    url, depth = queue.get_nowait()
                except asyncio.QueueEmpty:
                    return
                links = await fetch_and_save(url, depth)
                if store["ok"] % 500 == 0:
                    idx_f.flush()
                # link expansion: docs hosts only (depth<=1); reference google
                # hosts depth 0 only; never console/login-walled or off-google.
                # cap discovered links per shard to avoid unbounded growth.
                if links and depth < 1 and len(queued) < len(seeds) * 2:
                    for href in links[:300]:
                        n = normalize_url(href, base=url)
                        if not n or n in queued:
                            continue
                        nhost = urlparse(n).netloc
                        if nhost == "console.cloud.google.com" or nhost.endswith(".console.cloud.google.com"):
                            continue
                        if nhost != MAIN_HOST and not nhost.endswith(".cloud.google.com"):
                            if nhost != "cloud.google.com" or depth > 0:
                                continue
                        try:
                            is_new = con.execute("SELECT 1 FROM visited WHERE url=?", (n,)).fetchone() is None
                        except Exception:
                            is_new = True
                        if not is_new:
                            continue
                        queued.add(n)
                        queue.put_nowait((n, depth + 1))
                queue.task_done()

        workers = [asyncio.create_task(worker()) for _ in range(concurrency)]
        while True:
            await asyncio.sleep(2)
            if queue.empty():
                await asyncio.sleep(4)
                if queue.empty():
                    break
            el = time.time() - store["t0"]
            rate = store["ok"] / max(el, 1)
            if time.time() - store["last_snap"] > 60:
                store["last_snap"] = time.time()
                status(f"progress ok={store['ok']} fail={store['fail']} rate={rate:.1f}/s elapsed={el/3600:.1f}h shard={shard.name} q={queue.qsize()}")
                snapshot(con, {"rate_per_s": round(rate, 2)})
        for t in workers:
            t.cancel()
        await asyncio.gather(*workers, return_exceptions=True)
        try:
            con.execute("UPDATE shards SET done=1 WHERE name=?", (shard.name,))
            con.commit()
        except Exception:
            pass
        idx_f.flush()
        status(f"shard DONE {shard.name} ok={store['ok']} fail={store['fail']}")
        snapshot(con)

    idle_rounds = 0
    while True:
        pending = [s for s in load_seed_shards() if s.name not in done_sh]
        if not pending:
            try:
                done_sh = {r[0] for r in con.execute("SELECT name FROM shards WHERE done=1")}
                pending = [s for s in load_seed_shards() if s.name not in done_sh]
            except Exception:
                pass
            if not pending:
                idle_rounds += 1
                if idle_rounds >= 30:  # ~3 min with no new shards: inventory done
                    status("no pending shards — finishing")
                    break
                status(f"waiting for inventory... ({idle_rounds})")
                await asyncio.sleep(6)
                continue
        idle_rounds = 0
        await crawl_shard(pending[0])
        done_sh.add(pending[0].name)

    idx_f.close()
    global _crawler
    if _crawler is not None:
        try:
            await _crawler.close()
        except Exception:
            pass
    el = time.time() - store["t0"]
    manifest = {"base": BASE_URL, "visited": store["ok"], "failed": store["fail"],
                "elapsed_h": round(el / 3600, 2), "out_root": str(OUT_ROOT),
                "tools": ["scrapling (Fetcher)", "crawl4AI (AsyncWebCrawler fallback)", "scrapegraph-ai (convert_to_md)"],
                "generated_at": datetime.now(timezone.utc).isoformat()}
    try:  # merge: preserve updater-side fields if present
        prev = json.loads(MANIFEST_FILE.read_text()) if MANIFEST_FILE.exists() else {}
        prev.update(manifest)
        manifest = prev
    except Exception as e:
        status(f"manifest merge skipped: {e}")
    MANIFEST_FILE.write_text(json.dumps(manifest, indent=2))
    status(f"ALL DONE ok={store['ok']} fail={store['fail']} elapsed_h={el/3600:.1f}")
    snapshot(con, {"done": True})

if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--concurrency", type=int, default=30)
    args = ap.parse_args()
    asyncio.run(main(concurrency=args.concurrency))
