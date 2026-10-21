---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/samples/v1_restore.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/samples/v1_restore.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-15T20:47:52.685959+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/samples/v1_restore.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/samples/v1_restore.yaml.txt


    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Restore
    metadata:
      name: restore1
    spec:
      sourceDBCluster: dbcluster-sample
      backup: backup1
    
