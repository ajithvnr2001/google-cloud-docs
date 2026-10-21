---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_dbcluster_debian.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_dbcluster_debian.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (747 chars), fallback to crawl4ai)
fetched_at: 2026-10-15T02:48:36.023606+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_dbcluster_debian.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/samples/v1_dbcluster_debian.yaml.txt


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
      databaseVersion: "16.13.0"
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
    
