---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_backup.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_backup.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-15T11:24:47.396970+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_backup.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_backup.yaml.txt


    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Backup
    metadata:
      name: backup1
    spec:
      dbclusterRef: dbcluster-sample
      backupPlanRef: backupplan1
      manual: true
      physicalBackupSpec:
        backupType: full
    
