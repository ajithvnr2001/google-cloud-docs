#!/bin/bash
# drain_kick.sh — restart the backlog drain if it stopped while work remains.
# Runs from gcp-drain-kick.timer every 4 hours. No-op while drain is active
# or when the backlog is already below threshold.
set -uo pipefail
STATUS=/data/opencode/gcpdocs/STATUS.json
b=$(python3 - <<'PY'
import json
try:
    d = json.load(open('/data/opencode/gcpdocs/STATUS.json'))
    print(max(int(d.get('last_update', {}).get('stale_backlog', 0)), 0))
except Exception:
    print(0)
PY
)
[ "${b:-0}" -le 2000 ] && exit 0
systemctl is-active --quiet gcp-drain.service && exit 0
echo "$(date -u +%FT%TZ) [kick] backlog≈$b, drain inactive -> starting" >> /data/opencode/gcpdocs/drain.log
systemctl start gcp-drain.service
