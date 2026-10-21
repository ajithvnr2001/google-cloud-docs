---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/samples/v1_replication_upstream.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/samples/v1_replication_upstream.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-15T02:19:28.106424+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/samples/v1_replication_upstream.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/samples/v1_replication_upstream.yaml.txt


    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Replication
    metadata:
      name: replication-upstream-sample
    spec:
      dbcluster:
        name: dbcluster-sample
      upstream: {}
    
