---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/samples/v1_backup.yaml.txt
title: v1 backup.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:39.987505+00:00
---

# v1 backup.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/samples/v1_backup.yaml.txt

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
