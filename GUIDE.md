# GUIDE — Google Cloud docs: full redo + incremental updates (end to end)

Everything below was executed as written on an Azure spot VM with a 250GB `/data` disk. Follow it top-to-bottom to **redo the whole crawl from zero**, or skip to §3 to keep an existing corpus up to date.

## 0. Architecture (what runs where)

```
inventory.py  → seeds/sitemap_N_of_70.txt   (resumable shard inventory)
crawl_gcp.py  → docs/<path>.md              (shard-by-shard crawl, sqlite state, rescan loop)
final_gapfill.py → fills any audit gap      (missing_urls.txt)
verify_coverage.py → proves 100% coverage
update_gcp.py → incremental: new + lastmod-stale pages only  (daily systemd timer)
build_final_release.sh → releases/*.tar.gz  (corpus is too big for git; published as Release assets)
```

Stack per page: **Scrapling** (`Fetcher.get`, stealthy headers) → **Crawl4AI** (headless Chromium fallback) → **ScrapeGraphAI** `convert_to_md` (HTML→markdown, local, no LLM key) → **httpx** last resort. See `crawl_gcp.py::fetch_one`.

State (all under `/data`, survives VM crashes/evictions):
- `crawl_state.db` — sqlite: `visited(url, file, title, method, fetched_at)`, `failed(url, err)`, `shards(done)`
- `docs/_index.jsonl` — one row per saved page
- `STATUS.log` / `STATUS.json` — heartbeat + `"done": true` flag

## 1. Prerequisites

```bash
pip3 install -r requirements.txt          # pins scrapling/crawl4ai/scrapegraphai/extras
python3 -m playwright install chromium    # crawl4ai fallback needs it
# scrapegraph-ai 1.36.0 quirk: langchain import paths are stale → patch once:
python3 - <<'EOF'
import scrapegraphai.utils, pathlib
p = pathlib.Path(scrapegraphai.utils.__file__).parent / "convert_to_md.py"
print("loaded", p)   # our repos carry the patched clone under tools/
EOF
```

On our VMs the patched clones live in `/data/opencode/cloudflare/tools/` and are symlinked; `crawl_gcp.py` also falls back to pip-installed packages if the symlinks are missing.

## 2. Full crawl redo, step by step

**Step 1 — inventory (resumable).** Discovers all 70 `sitemap_N_of_70.xml` shards live from the index and writes one `.txt` per shard under `seeds/`.

```bash
python3 inventory.py
# crash/reboot? just re-run — finished shards are skipped (seeds/_progress.json)
```

**Step 2 — crawl (crash-safe).**

```bash
python3 crawl_gcp.py --concurrency 30      # ~18–24h for all 70 shards on a 2–4 CPU box
```

- Resumable: rerun any time; visited rows are skipped per shard ("todo=N (skipped visited)").
- Progress: `tail -f STATUS.log` (per-shard lines + rate) or `cat STATUS.json`.
- The crawler loops: any shard that finishes with failures/initerrupted pages gets rescanned until quiet before moving on.
- Binary assets (.pdf/.png/...) are intentionally skipped and recorded, not converted.

**Step 3 — coverage audit (prove completeness).**

```bash
python3 verify_coverage.py
# → prints visited/failed-recorded/missing counts + coverage %
# → writes missing_urls.txt
```

**Step 4 — gap-fill anything missing.**

```bash
python3 final_gapfill.py        # fetches missing_urls.txt with the same stack + same save format
python3 verify_coverage.py      # re-run: expect missing = PDF binaries only (recorded by design)
```

**Step 5 — publish the corpus (Release assets, NOT git — important).**

GitHub rejects pushes with files >100MB and repos >~5GB; this corpus is ~12GB. So `docs/` is **git-ignored by design** and snapshots ship as Release assets:

```bash
bash build_final_release.sh     # rebuilds 4 integrity-checked tar.gz trees under releases/
export GH_TOKEN=...             # authorized token of the repo owner
gh auth login --with-token <<<"$GH_TOKEN"
gh release create docs-complete-$(date +%F) \
  --title "Google Cloud docs — complete corpus $(date +%F)" \
  --notes "607,607 pages; see README layout. java/sdks/meta/core trees." \
  releases/docs-java.tar.gz releases/docs-sdks.tar.gz releases/docs-meta.tar.gz releases/docs-core.tar.gz
```

Downloaders: `tar -xzf` all four archives into one directory = the full `docs/` tree.

## 3. Incremental updates (what used to need months = a daily job)

`update_gcp.py` mirrors the cloudflare/copilotkit/ai-docs updater:

1. reads the live sitemap index → all 70 shards + `lastmod` timestamps
2. canonicalizes via `crawl_gcp.normalize_url` (same dedupe as the original crawl)
3. **new** = sitemap URLs missing from sqlite `visited` → crawled
4. **stale** = `lastmod` newer than our `fetched_at` → refreshed newest-first, capped (`--refresh-cap 200/day`; soft-aborts if >5000 so a site overhaul triggers a full redo instead of a hundred-thousand-page run)
5. saves with the same frontmatter/_meta/_index format; updates sqlite + `STATUS.json`
6. optional `--publish-delta`: tars only changed pages into `releases/docs-delta-<date>.tar.gz`

```bash
python3 update_gcp.py --check-only         # pure diff, no writes
python3 update_gcp.py --concurrency 20     # one incremental pass
```

### Automation (installed on the VM by boot.sh)

- `gcp-update.service` (oneshot) + `gcp-update.timer` — daily 05:30 UTC, `Persistent=true` (catches up after downtime).
- Re-check manually: `systemctl list-timers gcp-update.timer` · logs: `journalctl -u gcp-update.service`.

## 4. VM eviction / disaster recovery

- `/data` is a separate disk — pages, state, releases all survive reboot & reallocation.
- `boot.sh` (idempotent): reinstalls unit files, starts the crawl if one isn't running, enables the update timer.
- One-time: attach `cloud-init.yaml` to the VM template → every freshly allocated VM bootstraps itself:
  `runcmd: [bash, /data/opencode/aidocs/boot.sh]`-style (see file).

## 5. Troubleshooting (things that actually bit us)

| Symptom | Cause / fix |
|---|---|
| `git push` → pre-receive declined | Files >100MB (`_index.jsonl` was 235MB) / total >~5GB. Corpus lives in Releases, not git — never force-add `docs/`. |
| Wall-clock git commands ~forever | 600k-file tree; prefer `git add <specific files>` and never bare `git status` on the corpus. |
| Sudden 0–5 pages/s | Wrote read/write hotspot; check `iostat`, drop `--concurrency` to 20 |
| Stuck shard for >30min | `kill` the crawler and rerun — sqlite makes every page resumable. |
| `scrapegraphai` ImportError `langchain.prompts` | Use the patched clone (`tools/scrapegraph-ai`) or sed the import to `langchain_core.prompts`. |
| GitHub 402 on release upload | Asset >2GB per file — the split (`java`/`sdks`/`meta`/`core`) keeps each under the cap. |

## 6. Numbers to expect (for comparison when redoing)

- 1,230,844 raw sitemap URLs → **601,023 unique canonical** (rest are locale/dup/version pairs that normalize away)
- final: **607,607 visited pages** (601,023 canonical + link-discovered extras + 300 gapfill), 64 PDF binaries recorded
- corpus ~12GB, 4 release archives ~800MB compressed total
- full crawl ~18–24h on a 2-CPU VM; incremental daily pass typically <10min
