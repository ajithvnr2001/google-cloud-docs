---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/samples/v1_replication_downstream.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/samples/v1_replication_downstream.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling empty html)
fetched_at: 2026-10-14T00:06:37.101598+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/samples/v1_replication_downstream.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/samples/v1_replication_downstream.yaml.txt


    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: Replication
    metadata:
      name: replication-downstream-sample
    spec:
      dbcluster:
        name: dbcluster-sample
      downstream:
        host: "10.10.10.10"
        port: 5432
        username: alloydbreplica
        password:
          name: "ha-rep-pw-dbcluster-sample"
        replicationSlotName: "dbcluster_sample_replication_upstream_sample"
        control: setup
        # to promote downstream, change control to promote
    
