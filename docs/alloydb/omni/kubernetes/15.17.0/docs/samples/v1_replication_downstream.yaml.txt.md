---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_replication_downstream.yaml.txt
title: v1 replication downstream.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:39.668640+00:00
---

# v1 replication downstream.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_replication_downstream.yaml.txt

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
