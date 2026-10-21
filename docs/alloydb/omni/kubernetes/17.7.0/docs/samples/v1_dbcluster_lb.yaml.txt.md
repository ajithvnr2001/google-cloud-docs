---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/samples/v1_dbcluster_lb.yaml.txt
title: v1 dbcluster lb.yaml
method: httpx-raw-text
fetched_at: 2026-10-17T08:51:41.286929+00:00
---

# v1 dbcluster lb.yaml

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/samples/v1_dbcluster_lb.yaml.txt

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
  databaseVersion: "17.7.0"
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
    dbLoadBalancerOptions:
      annotations:
        # Creates internal LoadBalancer in GKE.
        networking.gke.io/load-balancer-type: "internal"
  allowExternalIncomingTraffic: true
