# Google Cloud Docs — End-to-End Crawler

Crawls **https://docs.cloud.google.com/** completely (1,230,844 raw sitemap URLs → **601,023 unique canonical pages** across 70 shards: guides + versioned API reference) plus in-guide reference domains. Three stacks: **Scrapling** → **Crawl4AI** → **ScrapeGraphAI** (local, no LLM key).

## Status: COMPLETE (2026-10-17)

- **607,307 pages crawled** (= 601,023 sitemap canonicals + link-discovered extras; only 364 sitemap gap URLs found by audit, fetched via `final_gapfill.py`; 64 PDFs are binary assets, recorded not converted).
- 70/70 shards done — see `STATUS.json` (`"done": true`) / `STATUS.log`.
- **Docs are split by size:** product documentation (`docs/<product>/docs/...`, 82k guides/quickstarts) **is tracked in git and committed daily** at 08:20 UTC (see `gcp-git-ship.timer`). The versioned API reference (`/docs/reference/`, 1.06M files / 7.4 GB) and crawler sidecars are **not in git** — GitHub rejects >2 GB pushes and 1M+ files would make commits unusable. Full-corpus and reference updates are published as **GitHub Release assets** (tar.gz deltas): see [Releases](https://github.com/ajithvnr2001/google-cloud-docs/releases).

## Scale (measured)

- 1,230,844 raw sitemap URLs (duplicates/locale-version pairs) → 601,023 unique canonical after normalization.
- `java` 150k, `nodejs` 127k pages dominate (54% is versioned API reference); guides ≈ rest.
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
inventory.py  crawl_gcp.py  final_gapfill.py  requirements.txt
guide_code/   # coder guide + coder_scrape.py / coder_update.py
seeds/        # git-ignored shard URL lists (regenerable)
docs/         # product docs tracked in git + committed daily; API reference (~7.4GB) via Releases
releases/     # local staging for release tar.gz assets (git-ignored)
```

## Key findings

- `cloud.google.com/*` docs 301 → `docs.cloud.google.com/*`: single corpus.
- `console.cloud.google.com` skipped (login wall); other `*.google.com` refs fetched depth-0.

## Status

Crawl complete — 70/70 shards, `"done": true` in `STATUS.json`. Product docs are committed to git daily (`gcp-git-ship.timer`); full-corpus snapshots and reference deltas are published as GitHub Release assets. No GitHub Actions (manual durable runs, by design).
