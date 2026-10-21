---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/samples/v1_dbcluster_lb.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/samples/v1_dbcluster_lb.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (783 chars), fallback to crawl4ai)
fetched_at: 2026-10-15T02:41:59.229821+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/samples/v1_dbcluster_lb.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/samples/v1_dbcluster_lb.yaml.txt


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
      databaseVersion: "15.15.0"
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
    
