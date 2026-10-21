---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/samples/v1_clone.yaml.txt
title: v1 clone.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:40.166566+00:00
---

# v1 clone.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/samples/v1_clone.yaml.txt

apiVersion: alloydbomni.dbadmin.goog/v1
kind: Restore
metadata:
  name: clone1
spec:
  sourceDBCluster: dbcluster-sample
  pointInTime: "2024-02-23T19:59:43Z"
  clonedDBClusterConfig:
    dbclusterName: new-dbcluster-sample
