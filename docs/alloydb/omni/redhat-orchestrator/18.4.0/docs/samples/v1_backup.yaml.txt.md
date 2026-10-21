---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backup.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backup.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-17T10:19:17.194064+00:00
---

# https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backup.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/samples/v1_backup.yaml.txt


    Backup:
      metadata:
        name: sample-backup
      spec:
        dbclusterRef: sample-dbc
        backupPlanRef: sample-backupplan
        manual: true
        physicalBackupSpec:
          backupType: full
