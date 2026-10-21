#!/bin/bash
# gcp_git_ship.sh — daily commit + push of the tracked GCP product documentation
# (guides/quickstarts; the versioned API reference stays in Release delta assets).
# Runs from gcp-git-ship.timer (08:20 UTC) and after the backlog drain finishes.
#
# IMPORTANT: the crawler/drain rewrites docs/ continuously, so the working tree
# is never guaranteed clean. Push first (remote only moves via this VM); only
# pull/rebase if the push is actually rejected, using --autostash.
set -uo pipefail
cd /data/opencode/gcpdocs
: "${GH_TOKEN:?GH_TOKEN missing — unit EnvironmentFile}"
URL="https://ajithvnr2001:${GH_TOKEN}@github.com/ajithvnr2001/google-cloud-docs.git"

# prevent timer / manual / drain-end runs from overlapping
exec 9>/data/opencode/gcpdocs/.git_ship.lock
flock -n 9 || { echo "[git-ship] another ship already running"; exit 0; }

git add -A -- docs || { echo "[git-ship] add failed"; exit 1; }
if git diff --cached --quiet; then
  echo "[git-ship] no doc changes"
  exit 0
fi

git commit -q -m "chore: daily docs update $(date -u +%F)" || { echo "[git-ship] commit failed"; exit 1; }
echo "[git-ship] committed $(git rev-parse --short HEAD): $(git diff-tree --shortstat --no-commit-id HEAD)"

for i in 1 2 3 4 5; do
  if git push "$URL" main >/dev/null 2>&1; then
    echo "[git-ship] pushed $(git rev-parse --short HEAD)"
    exit 0
  fi
  # only reached when the remote moved: rebase onto it, tolerating live writes
  if git -c rebase.autoStash=true pull --rebase -q "$URL" main >/dev/null 2>&1; then
    echo "[git-ship] rebased onto remote; retrying push"
  else
    git rebase --abort >/dev/null 2>&1 || true
    echo "[git-ship] pull/rebase attempt $i failed"
  fi
  sleep 15
done
echo "[git-ship] push failed after 5 attempts"
exit 1
