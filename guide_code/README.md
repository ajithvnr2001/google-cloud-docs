# Guide: scrape + update Google Cloud docs (coder end-to-end)

Base: `/data/opencode/gcpdocs/` · Target: `https://docs.cloud.google.com/` (1,230,913 sitemap URLs, 70 shards)

## 0. Scale estimate (measured, not guessed)

- Single page: median **0.9 s** via Scrapling (255–270 KB HTML).
- Full crawl at `--concurrency 30`: ~15–20 pages/s → **~18–24 h** for 1.23M pages.
- Disk: ~30 KB/page markdown+meta → **~35 GB**. 210 GB free confirmed.
- 53% of URLs are versioned API reference dumps (`java` 150k, `nodejs` 127k…); guides ≈ 575k.

## 1. Scrape one page (all 3 libs)

```bash
python3 guide_code/coder_scrape.py https://docs.cloud.google.com/compute/docs /tmp/compute.md
```

Flow (`coder_scrape.py`): `Fetcher.get(stealthy_headers=True)` → keep `<main>/<article>` → `scrapegraph-ai/utils/convert_to_md.py::convert_to_md` → fallback `AsyncWebCrawler(CacheMode.BYPASS)` on thin/fail.

## 2. Full crawl (running)

```bash
# 1) inventory first (resumable per-shard, logs to STATUS.log)
python3 inventory.py
# 2) crawl (resume-safe: sqlite visited DB + per-shard completion + file-exists skip)
python3 crawl_gcp.py --concurrency 30
# crash? just re-run the same command — it resumes from STATUS.json/crawl_state.db
```

Design (`crawl_gcp.py`):
- **Seeds**: `seeds/sitemap_N_of_70.txt` (70 shards, one per sitemap file), processed shard-by-shard so RAM stays flat.
- **State** (all under `/data`, survives crashes): `crawl_state.db` (sqlite: `visited`, `failed`, `shards`), `docs/_index.jsonl` (appended), `STATUS.log` (appended lines), `STATUS.json` (snapshot every 60 s with rate + ETA).
- **Fetch per URL**: Scrapling → Crawl4AI → httpx; markdown via ScrapeGraphAI; saved `docs/<path>.md` + `_meta/*.json` with frontmatter.
- **Link expansion**: `docs.cloud.google.com`/`*.cloud.google.com` depth ≤ 1, reference `*.google.com` depth 0 only, never `console.*` (login-walled), discovered capped at 2× seeds per shard (sitemap already covers everything).
- **Resume proof**: killed mid-shard and restarted — 217 visited rows preserved, `todo = seeds − visited`.

## 3. Update without recrawling

```bash
python3 guide_code/coder_update.py --check-only
python3 guide_code/coder_update.py --run --concurrency 10
```

Live sitemap set − indexed set = targets; existing files never touched.

## 4. Verify

```bash
tail -n 5 STATUS.log && cat STATUS.json
find docs -name '*.md' | wc -l
python3 -c "import sqlite3; c=sqlite3.connect('crawl_state.db'); print(c.execute('SELECT COUNT(*) FROM visited').fetchone())"
```

## 5. Notes / limits

- `cloud.google.com/*` docs 301-redirect to `docs.cloud.google.com/*` (same host canonical) — one corpus, not two.
- External reference domains in guides (`github.com`, `console.cloud.google.com`, `developers.google.com`): console skipped (login wall); other google hosts fetched depth-0 into `docs/_subdomains/`.
- No GitHub Actions (per request); run on a durable box. Push docs in batches — full `docs/` (~35 GB) exceeds practical git hosting limits.

## Tools (shared clones)

- D4Vinci/Scrapling, unclecode/crawl4AI, ScrapeGraphAI/Scrapegraph-ai (`tools/`, symlinked; pip fallback built into resolver).
