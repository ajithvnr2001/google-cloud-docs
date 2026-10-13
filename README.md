# Google Cloud Docs — End-to-End Crawler

Crawls **https://docs.cloud.google.com/** completely (1,230,913 sitemap URLs across 70 shards: guides + versioned API reference) plus in-guide reference domains. Three stacks: **Scrapling** → **Crawl4AI** → **ScrapeGraphAI** (local, no LLM key).

## Scale (measured)

- 1,230,913 URLs; 53% API reference dumps (`java` 150k, `nodejs` 127k); guides ≈ 575k.
- Median fetch 0.9 s/page → ~15–20/s at `--concurrency 30` → **~18–24 h** full pass, ~35 GB output.

## Install

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

## Run (crash-safe — just re-run to resume)

```bash
python3 inventory.py        # resumable sitemap inventory → seeds/
python3 crawl_gcp.py --concurrency 30   # shard-by-shard crawl → docs/
```

State (all under `/data`, survives crashes): `crawl_state.db` (sqlite visited/failed/shards), `docs/_index.jsonl`, `STATUS.log` (append), `STATUS.json` (rate/ETA snapshot). Resume proof: killed mid-shard, restarted, 217 rows preserved, only missing pages refetched.

## Layout

```
inventory.py  crawl_gcp.py  requirements.txt
guide_code/   # coder guide + coder_scrape.py / coder_update.py
seeds/        # git-ignored shard URL lists (regenerable)
docs/         # git-ignored output (~35GB when complete)
```

## Key findings

- `cloud.google.com/*` docs 301 → `docs.cloud.google.com/*`: single corpus.
- `console.cloud.google.com` skipped (login wall); other `*.google.com` refs fetched depth-0.

## Status

Full crawl in progress — see `STATUS.log` / `STATUS.json`. No GitHub Actions (manual durable runs).
