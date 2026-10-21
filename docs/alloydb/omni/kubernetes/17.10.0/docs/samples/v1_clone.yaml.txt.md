---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/samples/v1_clone.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/samples/v1_clone.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-17T10:21:01.087478+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/samples/v1_clone.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/samples/v1_clone.yaml.txt


    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Restore
    metadata:
      name: clone1
    spec:
      sourceDBCluster: dbcluster-sample
      pointInTime: "2024-02-23T19:59:43Z"
      clonedDBClusterConfig:
        dbclusterName: new-dbcluster-sample
    
