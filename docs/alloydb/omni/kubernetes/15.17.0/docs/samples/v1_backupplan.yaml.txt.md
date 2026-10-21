---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_backupplan.yaml.txt
title: v1 backupplan.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:37.925785+00:00
---

# v1 backupplan.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_backupplan.yaml.txt

apiVersion: alloydbomni.dbadmin.goog/v1
kind: BackupPlan
metadata:
  name: backupplan1
spec:
  dbclusterRef: dbcluster-sample
  backupRetainDays: 14
  paused: false
  backupSchedules:
    # Full backup at 00:00 on every Sunday.
    full: "0 0 * * 0"
    # Incremental backup at 21:00 every day.
    incremental: "0 21 * * *"
