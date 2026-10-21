---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/samples/v1_dbcluster_ha.yaml.txt
title: v1 dbcluster ha.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:40.352158+00:00
---

# v1 dbcluster ha.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/samples/v1_dbcluster_ha.yaml.txt

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
  databaseVersion: "16.11.0"
  availability:
    numberOfStandbys: 1
    enableStandbyAsReadReplica: true
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
