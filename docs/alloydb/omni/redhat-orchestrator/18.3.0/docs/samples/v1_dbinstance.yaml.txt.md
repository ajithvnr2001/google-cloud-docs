---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/samples/v1_dbinstance.yaml.txt
title: v1 dbinstance.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:41.944517+00:00
---

# v1 dbinstance.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/samples/v1_dbinstance.yaml.txt

DBInstance:
  metadata:
    name: sample-readpool
  spec:
    instanceType: ReadPool
    dbcParent:
      name: alloydb-prod
    nodeCount: 2
