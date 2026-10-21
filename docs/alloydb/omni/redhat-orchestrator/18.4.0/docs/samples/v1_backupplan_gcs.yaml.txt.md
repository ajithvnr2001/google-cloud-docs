---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backupplan_gcs.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backupplan_gcs.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-17T10:18:43.103106+00:00
---

# https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backupplan_gcs.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backupplan_gcs.yaml.txt


    BackupPlan:
      metadata:
        name: sample-backupplan-gcs
      spec:
        dbclusterRef: sample-dbc
        backupRetainDays: 14
        paused: false
        backupSchedules:
          # Full backup at 00:00 every Sunday.
          full: "0 0 * * 0"
          # Incremental backup at every day at 21:00.
          incremental: "0 21 * * *"
        backupLocation:
          type: GCS
          gcsOptions:
            bucket: sample-backup-bucket
            key: /backups
            secretRef:
              name: gcs-access-secret
    
