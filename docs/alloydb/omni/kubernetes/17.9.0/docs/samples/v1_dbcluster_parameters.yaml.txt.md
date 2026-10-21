---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/samples/v1_dbcluster_parameters.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/samples/v1_dbcluster_parameters.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (733 chars), fallback to crawl4ai)
fetched_at: 2026-10-15T00:01:44.607577+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/samples/v1_dbcluster_parameters.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/samples/v1_dbcluster_parameters.yaml.txt


    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-dbcluster-sample
    type: Opaque
    data:
      dbcluster-sample: "Q2hhbmdlTWUxMjM=" # Password is ChangeMe123
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: "17.9.0"
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-dbcluster-sample
        resources:
          memory: 5Gi
          cpu: 1
          disks:
          - name: DataDisk
            size: 10Gi
        parameters:
          google_columnar_engine.enabled: "on"
          google_columnar_engine.memory_size_in_mb: "256"
    
