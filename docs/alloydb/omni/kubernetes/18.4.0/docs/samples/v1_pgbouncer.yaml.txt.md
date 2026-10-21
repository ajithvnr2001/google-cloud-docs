---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_pgbouncer.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_pgbouncer.yaml.txt
method: crawl4ai+scrapegraph (scrapling: scrapling thin content (654 chars), fallback to crawl4ai)
fetched_at: 2026-10-17T10:16:34.189163+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_pgbouncer.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/samples/v1_pgbouncer.yaml.txt


    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: PgBouncer
    metadata:
      name: mypgbouncer
    spec:
      allowSuperUserAccess: true
      dbclusterRef: dbcluster-sample
      replicaCount: 1
      parameters:
        pool_mode: transaction
        ignore_startup_parameters: extra_float_digits
        default_pool_size: "15"
        max_client_conn: "800"
        max_db_connections: "160"
      podSpec:
        resources:
          memory: 1Gi
          cpu: 1
        image: "gcr.io/alloydb-omni/operator/g-pgbouncer:1.7.0"
      serviceOptions:
        type: "ClusterIP"
    
