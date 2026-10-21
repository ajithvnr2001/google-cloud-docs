---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/samples/v1_switchover.yaml.txt
title: v1 switchover.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:41.851700+00:00
---

# v1 switchover.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/samples/v1_switchover.yaml.txt

apiVersion: alloydbomni.dbadmin.goog/v1
kind: Switchover
metadata:
  name: switchover-sample
spec:
  dbclusterRef: dbcluster-sample
