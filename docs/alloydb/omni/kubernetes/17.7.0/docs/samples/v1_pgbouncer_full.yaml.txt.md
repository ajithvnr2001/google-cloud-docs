---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/samples/v1_pgbouncer_full.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/samples/v1_pgbouncer_full.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:52:15.022511+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/samples/v1_pgbouncer_full.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/samples/v1_pgbouncer_full.yaml.txt

apiVersion: alloydbomni.dbadmin.goog/v1 kind: PgBouncer metadata: name: mypgbouncer spec: allowSuperUserAccess: true dbclusterRef: dbcluster-sample replicaCount: 2 parameters: pool_mode: transaction ignore_startup_parameters: extra_float_digits default_pool_size: "15" max_client_conn: "800" max_db_connections: "160" podSpec: resources: memory: 1Gi cpu: 1 image: "gcr.io/alloydb-omni-staging/g-pgbouncer:1.4.0" schedulingconfig: nodeaffinity: requiredDuringSchedulingIgnoredDuringExecution: nodeSelectorTerms: \- matchExpressions: \- key: nodetype operator: In values: \- pgbouncer serviceOptions: type: "LoadBalancer" loadBalancerSourceRanges: \- "11.0.0.0/8" annotations: networking.gke.io/load-balancer-type: "internal" 
