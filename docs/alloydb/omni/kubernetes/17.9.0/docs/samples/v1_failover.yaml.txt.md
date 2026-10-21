---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/samples/v1_failover.yaml.txt
title: v1 failover.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:40.889977+00:00
---

# v1 failover.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/samples/v1_failover.yaml.txt

apiVersion: alloydbomni.dbadmin.goog/v1
kind: Failover
metadata:
  name: failover-sample
spec:
  dbclusterRef: dbcluster-sample
