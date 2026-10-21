---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backupplan_s3.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backupplan_s3.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (660 chars), fallback to crawl4ai)
fetched_at: 2026-10-17T10:21:01.737491+00:00
---

# https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backupplan_s3.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backupplan_s3.yaml.txt


    BackupPlan:
      metadata:
        name: sample-backupplan-s3
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
          type: S3
          s3Options:
            bucket: sample-backup-bucket-s3
            key: /backups
            region: "us-east-1"
            endpoint: "https://s3.storage.com"
            secretRef:
              name: s3-access-secret
