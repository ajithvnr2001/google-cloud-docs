---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_dbcluster_debian.yaml.txt
title: v1 dbcluster debian.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:38.998853+00:00
---

# v1 dbcluster debian.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_dbcluster_debian.yaml.txt

# This is a minimal DBCluster spec. See v1_dbcluster_full.yaml for more configurations.
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
  databaseVersion: "15.17.0"
  databaseImageOSType: Debian
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
