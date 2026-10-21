#!/bin/bash
# drain_until_done.sh — GCP lastmod-backlog drain in 4,000-page batches until done.
# Robustness model:
#   * runs as gcp-drain.service → survives session close; auto-restarts on failure
#   * enabled at boot → resumes automatically after a VM reboot/reprovision
#   * every batch writes state per page (resumable at any instant)
#   * every batch's delta tarball+manifest is uploaded to one GitHub release
#   * the nightly gcp-update.timer is paused while draining (no duplicate work),
#     and re-enabled on exit
set -uo pipefail
cd /data/opencode/gcpdocs
: "${GH_TOKEN:?GH_TOKEN missing — unit EnvironmentFile}"
REPO="ajithvnr2001/google-cloud-docs"
TAG="docs-backlog-drain-2026-10-20"
CAP=4000
THRESHOLD=2000
MAX_BATCHES=80
LOG=/data/opencode/gcpdocs/drain.log
log() { echo "$(date -u +%FT%TZ) [drain] $*" | tee -a "$LOG"; }

# singleton (two batches against the same sqlite = wasted work)
exec 9>/data/opencode/gcpdocs/.drain.lock
flock -n 9 || { log "another drain already running"; exit 0; }

backlog() {
  python3 - <<'PY'
import json
try:
    d = json.load(open('/data/opencode/gcpdocs/STATUS.json'))
    print(max(int(d.get('last_update', {}).get('stale_backlog', 0)), 0))
except Exception:
    print(10**9)
PY
}

cur=$(backlog)
if [ "$cur" -le "$THRESHOLD" ]; then
  log "backlog already low ($cur); nothing to do"
  exit 0
fi

gh release view "$TAG" --repo "$REPO" >/dev/null 2>&1 || \
  gh release create "$TAG" --repo "$REPO" \
    --title "GCP backlog drain (Oct 2026)" \
    --notes "Batch deltas for the GCP lastmod-backlog drain. Each asset pair = 4,000 refreshed pages + manifest (newest lastmod first)." \
    >>"$LOG" 2>&1 || log "release create failed (uploads will retry each batch)"

systemctl disable --now gcp-update.timer >/dev/null 2>&1 || true
log "start: backlog≈$cur; nightly timer paused; cap=$CAP/run"
trap 'systemctl enable --now gcp-update.timer >/dev/null 2>&1 || true; log "exit: nightly timer re-enabled"' EXIT

for i in $(seq 1 "$MAX_BATCHES"); do
  log "batch $i starting"
  if ! python3 update_gcp.py --refresh-cap "$CAP" --publish-delta --concurrency 20 >>"$LOG" 2>&1; then
    log "batch $i FAILED; retry after 300s"
    sleep 300
    continue
  fi
  ts=$(date -u +%Y-%m-%d_%H%M%S)
  tar=$(ls -t releases/docs-delta-*.tar.gz 2>/dev/null | head -n1 || true)
  man=$(ls -t releases/docs-delta-*.manifest.txt 2>/dev/null | head -n1 || true)
  if [ -n "$tar" ] && [ -n "$man" ]; then
    cp "$tar" "releases/drain_${ts}.tar.gz"
    cp "$man" "releases/drain_${ts}.manifest.txt"
    if gh release upload "$TAG" "releases/drain_${ts}.tar.gz" "releases/drain_${ts}.manifest.txt" \
         --repo "$REPO" >>"$LOG" 2>&1; then
      log "batch $i uploaded (drain_${ts}.tar.gz + manifest)"
      rm -f "releases/drain_${ts}.tar.gz" "releases/drain_${ts}.manifest.txt"
    else
      log "batch $i upload FAILED (local copies kept: drain_${ts}.*)"
    fi
  else
    log "batch $i produced no delta files"
  fi
  cur=$(backlog)
  log "batch $i done; backlog≈$cur"
  [ "$cur" -le "$THRESHOLD" ] && break
  sleep 30
done

./gcp_git_ship.sh >>"$LOG" 2>&1 || true
./vm-ship.sh "$REPO" README.md GUIDE.md >>"$LOG" 2>&1 || true
log "drain finished (backlog≈$(backlog))"
