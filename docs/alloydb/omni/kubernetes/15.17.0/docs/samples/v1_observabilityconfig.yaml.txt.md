---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_observabilityconfig.yaml.txt
title: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_observabilityconfig.yaml.txt
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:41:54.346769+00:00
---

# https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_observabilityconfig.yaml.txt

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/samples/v1_observabilityconfig.yaml.txt

apiVersion: alloydbomni.dbadmin.goog/v1 kind: ObservabilityConfig metadata: name: my-custom-metrics spec: dbClusterRefs: \- dbcluster-sample customMetrics: resourceLimits: workMemory: "4MB" maxParallelWorkers: 0 #limits to 1 CPU core definitions: \- metricGroup: querygroup_postgres database: "postgres" query: | SELECT datname, pg_database_size(datname) as db_size_bytes, (SELECT count(*) FROM pg_stat_activity WHERE datname = d.datname) as active_connections FROM pg_database d WHERE datname = 'postgres' metrics: \- name: datname desc: "Database name" usage: label \- name: db_size_bytes desc: "Size of the current database in bytes" usage: gauge \- name: active_connections desc: "Number of active connections to the database" usage: gauge 
