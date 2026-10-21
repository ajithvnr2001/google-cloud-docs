---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/samples/v1_dbcluster_ha.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/samples/v1_dbcluster_ha.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (687 chars), fallback to crawl4ai)
fetched_at: 2026-10-14T22:51:08.807634+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/samples/v1_dbcluster_ha.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/samples/v1_dbcluster_ha.yaml.txt


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
      databaseVersion: "18.3.0"
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
    
