---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_backupplan.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_backupplan.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-15T09:11:20.152959+00:00
---

# https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_backupplan.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_backupplan.yaml.txt


    BackupPlan:
      metadata:
        name: sample-backupplan
      spec:
        dbclusterRef: sample-dbc
        backupRetainDays: 14
        paused: false
        backupSchedules:
          # Full backup at 00:00 on every Sunday.
          full: "0 0 * * 0"
          # Incremental backup at 21:00 every day.
          incremental: "0 21 * * *"
        backupLocation:
          type: GCS
          gcsOptions:
            bucket: sample-backup-bucket
            key: /backups
            secretRef:
              name: gcs-access-secret
