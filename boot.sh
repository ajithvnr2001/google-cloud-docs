#!/bin/bash
# boot.sh — reinstall + start the GCP crawler after a spot-VM reallocation.
# Lives on /data (survives). Idempotent: safe to run any time.
# One-time setup: make every NEW VM call this on first boot (see cloud-init.yaml).
set -e
UNIT_SRC="/data/opencode/gcpdocs/gcp-crawl.service"
UNIT_DST="/etc/systemd/system/gcp-crawl.service"
UPDATE_UNIT_SRC="/data/opencode/gcpdocs/gcp-update.service"
UPDATE_TIMER_SRC="/data/opencode/gcpdocs/gcp-update.timer"
DRAIN_UNIT_SRC="/data/opencode/gcpdocs/gcp-drain.service"
KICK_UNIT_SRC="/data/opencode/gcpdocs/gcp-drain-kick.service"
KICK_TIMER_SRC="/data/opencode/gcpdocs/gcp-drain-kick.timer"

if [ ! -f "$UNIT_SRC" ]; then
  echo "FATAL: $UNIT_SRC missing (/data not attached?)" >&2
  exit 1
fi
cp -f "$UNIT_SRC" "$UNIT_DST"
cp -f "$UPDATE_UNIT_SRC" /etc/systemd/system/gcp-update.service
cp -f "$UPDATE_TIMER_SRC" /etc/systemd/system/gcp-update.timer
if [ -f "$DRAIN_UNIT_SRC" ]; then
  cp -f "$DRAIN_UNIT_SRC" /etc/systemd/system/gcp-drain.service
  cp -f "$KICK_UNIT_SRC" /etc/systemd/system/gcp-drain-kick.service
  cp -f "$KICK_TIMER_SRC" /etc/systemd/system/gcp-drain-kick.timer
fi
systemctl daemon-reload
systemctl enable gcp-crawl.service
# daily incremental update: enabled always (cheap when nothing changed)
systemctl enable --now gcp-update.timer
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
if [ -f "$DRAIN_UNIT_SRC" ]; then
  # backlog drain loop: no-ops when backlog is small, drains 4k batches otherwise
  systemctl enable gcp-drain.service
  systemctl start gcp-drain.service || true
  systemctl enable --now gcp-drain-kick.timer
  echo "gcp-drain.service enabled/started."
fi
systemctl is-enabled gcp-crawl.service
