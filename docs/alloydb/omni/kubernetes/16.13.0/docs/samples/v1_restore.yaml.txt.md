---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_restore.yaml.txt
title: v1 restore.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:39.980545+00:00
---

# v1 restore.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_restore.yaml.txt

apiVersion: alloydbomni.dbadmin.goog/v1
kind: Restore
metadata:
  name: restore1
spec:
  sourceDBCluster: dbcluster-sample
  backup: backup1
