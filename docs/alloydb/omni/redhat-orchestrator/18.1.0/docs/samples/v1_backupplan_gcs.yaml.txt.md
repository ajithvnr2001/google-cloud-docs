---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/samples/v1_backupplan_gcs.yaml.txt
title: v1 backupplan gcs.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:41.879496+00:00
---

# v1 backupplan gcs.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.1.0/docs/samples/v1_backupplan_gcs.yaml.txt

BackupPlan:
  metadata:
    name: backupplan-sample-dbc
  spec:
    dbclusterRef: sample-dbc
    backupLocation:
      type: GCS
      gcsOptions:
        bucket: sample-backup-bucket
        key: /backups
