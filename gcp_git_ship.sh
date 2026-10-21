#!/bin/bash
# gcp_git_ship.sh — daily commit + push of the tracked GCP product documentation
# (guides/quickstarts; the versioned API reference stays in Release delta assets).
# Runs from gcp-git-ship.timer (08:20 UTC) and after the backlog drain finishes.
set -uo pipefail
cd /data/opencode/gcpdocs
: "${GH_TOKEN:?GH_TOKEN missing — unit EnvironmentFile}"
URL="https://ajithvnr2001:${GH_TOKEN}@github.com/ajithvnr2001/google-cloud-docs.git"

git add -A -- docs || { echo "[git-ship] add failed"; exit 1; }
if git diff --cached --quiet; then
  echo "[git-ship] no doc changes"
  exit 0
fi

git commit -q -m "chore: daily docs update $(date -u +%F)" || { echo "[git-ship] commit failed"; exit 1; }
echo "[git-ship] committed $(git rev-parse --short HEAD): $(git diff-tree --shortstat --no-commit-id HEAD)"

for i in 1 2 3 4 5; do
  if git pull --rebase -q "$URL" main >/dev/null 2>&1 && git push "$URL" main >/dev/null 2>&1; then
    echo "[git-ship] pushed $(git rev-parse --short HEAD)"
    exit 0
  fi
  git rebase --abort >/dev/null 2>&1 || true
  echo "[git-ship] push attempt $i failed; retrying in 20s"
  sleep 20
done
echo "[git-ship] push failed after 5 attempts"
exit 1
