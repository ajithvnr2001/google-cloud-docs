---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_restore.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_restore.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-17T10:20:08.199556+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_restore.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/samples/v1_restore.yaml.txt


    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Restore
    metadata:
      name: restore1
    spec:
      sourceDBCluster: dbcluster-sample
      backup: backup1
    
