---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_backup.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_backup.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-15T21:54:59.379589+00:00
---

# https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_backup.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/samples/v1_backup.yaml.txt


    Backup:
      metadata:
        name: sample-backup
      spec:
        dbclusterRef: sample-dbc
        backupPlanRef: sample-backupplan
        manual: true
        physicalBackupSpec:
          backupType: full
