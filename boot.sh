#!/bin/bash
# boot.sh — reinstall + start the GCP crawler after a spot-VM reallocation.
# Lives on /data (survives). Idempotent: safe to run any time.
# One-time setup: make every NEW VM call this on first boot (see cloud-init.yaml).
set -e
UNIT_SRC="/data/opencode/gcpdocs/gcp-crawl.service"
UNIT_DST="/etc/systemd/system/gcp-crawl.service"

if [ ! -f "$UNIT_SRC" ]; then
  echo "FATAL: $UNIT_SRC missing (/data not attached?)" >&2
  exit 1
fi
cp -f "$UNIT_SRC" "$UNIT_DST"
systemctl daemon-reload
systemctl enable gcp-crawl.service
if ! systemctl is-active --quiet gcp-crawl.service; then
  # don't start a duplicate if a manual crawl is already running on the DB
  if pgrep -f "crawl_gcp.py" >/dev/null; then
    echo "crawl_gcp.py already running — service enabled for future boots, not starting a duplicate."
  else
    systemctl start gcp-crawl.service
    echo "gcp-crawl.service started."
  fi
else
  echo "gcp-crawl.service already active."
fi
systemctl is-enabled gcp-crawl.service
