# Google Cloud Docs — End-to-End Crawler

Crawls **https://docs.cloud.google.com/** completely (1,230,844 raw sitemap URLs → **601,023 unique canonical pages** across 70 shards: guides + versioned API reference) plus in-guide reference domains. Three stacks: **Scrapling** → **Crawl4AI** → **ScrapeGraphAI** (local, no LLM key).

## Status: COMPLETE (2026-10-17)

- **607,307 pages crawled** (= 601,023 sitemap canonicals + link-discovered extras; only 364 sitemap gap URLs found by audit, fetched via `final_gapfill.py`; 64 PDFs are binary assets, recorded not converted).
- 70/70 shards done — see `STATUS.json` (`"done": true`) / `STATUS.log`.
- **Corpus is too large for git pushes** (GitHub pre-receive rejects >~5GB pushes / >100MB files), so `docs/` is intentionally **not in git**. **Full-corpus snapshots are published as GitHub Release assets** (tar.gz, ≤2GB each): see [Releases](https://github.com/ajithvnr2001/google-cloud-docs/releases).

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
docs/         # git-ignored output (~12GB; published via Releases)
releases/     # local staging for release tar.gz assets
```

## Key findings

- `cloud.google.com/*` docs 301 → `docs.cloud.google.com/*`: single corpus.
- `console.cloud.google.com` skipped (login wall); other `*.google.com` refs fetched depth-0.

## Status

Crawl complete — 70/70 shards, `"done": true` in `STATUS.json`. Full-corpus snapshots published as GitHub Release assets. No GitHub Actions (manual durable runs, by design).
