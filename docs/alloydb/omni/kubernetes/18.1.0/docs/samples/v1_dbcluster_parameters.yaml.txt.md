---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/samples/v1_dbcluster_parameters.yaml.txt
title: v1 dbcluster parameters.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:40.881427+00:00
---

# v1 dbcluster parameters.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/samples/v1_dbcluster_parameters.yaml.txt

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
  databaseVersion: "18.1.0"
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
