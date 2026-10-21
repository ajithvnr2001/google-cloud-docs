---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_backupplan.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_backupplan.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-14T10:11:26.437958+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_backupplan.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_backupplan.yaml.txt


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
    
