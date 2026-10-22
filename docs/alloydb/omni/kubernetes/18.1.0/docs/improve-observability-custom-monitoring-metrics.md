---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/improve-observability-custom-monitoring-metrics/
title: Improve observability using custom monitoring metrics \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:41:20.313378+00:00
---

# Improve observability using custom monitoring metrics  |  AlloyDB Omni using the container orchestrator: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/improve-observability-custom-monitoring-metrics/

This page documents AlloyDB Omni version **18.1.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/overview)



Send feedback 

#  Improve observability using custom monitoring metrics Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/improve-observability-custom-monitoring-metrics)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/improve-observability-custom-monitoring-metrics)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/improve-observability-custom-monitoring-metrics)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/improve-observability-custom-monitoring-metrics)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/improve-observability-custom-monitoring-metrics)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/improve-observability-custom-monitoring-metrics)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/improve-observability-custom-monitoring-metrics)



You can use custom metrics in the AlloyDB Omni Kubernetes operator to define and collect application-specific metrics by executing SQL queries against your databases. Custom metrics use the `ObservabilityConfig` Custom Resource (CR) to define the metrics collection rules.

**Note:** You must have AlloyDB Omni operator version 1.7.0 or later. 

## Configure custom metrics using ObservabilityConfig

The `ObservabilityConfig` CR consists of two main sections, `dbClusterRefs` and `customMetrics`.

### `dbClusterRefs`

This section contains a list of references to the `DBCluster` resources that this configuration applies to. Each `ObservabilityConfig` must target one `DBCluster` in the same namespace.

### `customMetrics`

This section defines the core configuration for custom metrics collection, including resource limits and query definitions.

#### Resource limits (`resourceLimits`)

To protect the database, the system enforces limits on custom queries. If you don't specify these limits in the manifest, the system uses the default values listed in the following table.

Parameter | Description | Default | Max | Units  
---|---|---|---|---  
`workMemory` | Specifies the [work_mem](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-WORK-MEM) for the specific database connection used by the monitoring agent to collect these metrics. This setting is local to the metric collection process and doesn't affect the global `work_mem` parameter configured in the `DBCluster` spec. | `4MB` | N/A | `KB`, `MB` (Default: `KB`)  
`maxParallelWorkers` | Specifies the [max_parallel_workers_per_gather](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS-PER-GATHER) for the specific database connection used by the monitoring agent. Set this to 0 to disable parallel query execution and minimize CPU impact. This setting is local to the metric collection process and doesn't affect the global database configuration. | `0` | N/A | Integer  
`statementTimeout` | Specifies the [statement_timeout](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-STATEMENT-TIMEOUT) for the specific database connection used by the monitoring agent. This limits the maximum time allowed for any single metric query to run. This setting is local to the metric collection process and doesn't affect the global database configuration. | `2s` | `30s` | `ms`, `s` (Default: `ms`)  
  
#### Custom metric definitions (`definitions`)

Each entry in the `definitions` list defines a query and describes how to interpret its results.

  * **`metricGroup`** : a unique name (lowercase, numbers, underscores) used for metric naming.
  * **`database`** : the target database name for the query. The monitoring agent establishes a connection to this specific database to execute the query; therefore, the schema being queried must exist in it.
  * **`query`** : a valid SQL `SELECT` statement. Only `SELECT` queries are permitted.
  * **`metrics`** : a list mapping SQL result columns to Prometheus types: 
    * **`usage: label`** : uses the column value as a Prometheus label.
    * **`usage: gauge`** : exports the value as a [prometheus gauge](https://prometheus.io/docs/concepts/metric_types/#gauge) metric.
    * **`usage: counter`** : exports the value as a [prometheus counter](https://prometheus.io/docs/concepts/metric_types/#counter) metric.



## Security and permissions

The AlloyDB Omni operator uses `alloydbmonitor` user to collect metrics. By default, AlloyDB Omni operator creates this user with the [`LOGIN` attribute](https://www.postgresql.org/docs/current/role-attributes.html#ROLE-ATTRIBUTES) and grants it the [`pg_monitor` role](https://www.postgresql.org/docs/current/predefined-roles.html#PREDEFINED-ROLE-PG-MONITOR) in the `postgres` database.

When you add custom metrics, make sure that this user has the appropriate additional permissions:

  * **User responsibility** : database administrators must manually grant `SELECT` privileges to the `alloydbmonitor` user for any specific application tables, views, or schemas used in your custom queries.
  * **Write privilege safety check** : to ensure system integrity and prevent accidental data modification, the AlloyDB Omni operator performs a safety check. If the system finds that the `alloydbmonitor` user has any write privileges—for example, `INSERT`, `UPDATE`, and `DELETE`—on a target database, the system logs an error and refuses to collect custom metrics from that database.



### Granting permissions example

To grant read-only access to all tables in the `public` schema of a database named `warehousedb`, you must run the following command:
    
    
    psql -h <var>DB_CLUSTER_ENDPOINT</var> -U <var>DB_ADMIN_USER</var> -d warehousedb
    warehousedb=# GRANT SELECT ON ALL TABLES IN SCHEMA public TO alloydbmonitor;
    

## Sample manifest

The following example manifest configures the monitoring agent to connect to the `postgres` database and track transaction statistics using the `pg_stat_database` system view.
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: ObservabilityConfig
    metadata:
      name: obs-metrics
    spec:
      dbClusterRefs:
        - dbcluster-sample
      customMetrics:
        resourceLimits:
          workMemory: "4MB"
          maxParallelWorkers: 0
        definitions:
          - metricGroup: database
            database: "postgres"
            query: |
              SELECT
                curr_db, xact_commit, xact_rollback
              FROM pg_stat_database WHERE datname IS NOT NULL
            metrics:
              - name: curr_db
                desc: "Database name"
                usage: label
              - name: xact_commit
                desc: "Transactions committed"
                usage: counter
              - name: xact_rollback
                desc: "Transactions rolled back"
                usage: counter
    

## Metrics reference

This section references the metrics that the custom metrics feature generates.

### Generated metrics output

This Sample manifest exports metrics in the following Prometheus format:
    
    
    # HELP alloydb_omni_custom_database_xact_commit_total Transactions committed
    # TYPE alloydb_omni_custom_database_xact_commit_total counter
    alloydb_omni_custom_database_xact_commit_total{database="postgres",curr_db="testdb1",dbcluster="dbcluster-sample",dbcluster_type="Primary",dbinstance="n/a",dbinstance_type="n/a",dbnamespace="mc",dbnode="76d3-dbcluster-sample",dbnode_type="Primary"} 382069 1774388549568
    # HELP alloydb_omni_custom_database_xact_rollback_total Transactions rolled back
    # TYPE alloydb_omni_custom_database_xact_rollback_total counter
    alloydb_omni_custom_database_xact_rollback_total{database="postgres",curr_db="testdb1",dbcluster="dbcluster-sample",dbcluster_type="Primary",dbinstance="n/a",dbinstance_type="n/a",dbnamespace="mc",dbnode="76d3-dbcluster-sample",dbnode_type="Primary"} 4364 1774388549568
    

### Standard labels

Every custom metric automatically includes the following standard labels: `database`, `dbcluster`, `dbcluster_type`, `dbinstance`, `dbinstance_type`, `dbnamespace`, `dbnode`, and `dbnode_type`. For more information about these labels, see [AlloyDB Omni metric labels](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/omni-metrics#labels)

### Metrics collection metrics

These metrics indicate the status of each metric collection cycle. You can find detailed error messages, including which specific query timed out or failed, in the monitoring agent container logs.
    
    
    # HELP alloydb_omni_monitor_custom_metrics_errors_total Total number of errors encountered during execution of the custom query
    # TYPE alloydb_omni_monitor_custom_metrics_errors_total counter
    alloydb_omni_monitor_custom_metrics_errors_total{metricGroup="database",dbcluster="dbcluster-sample",dbnode="...",...} 0 1773703411350
    

## Before you use custom metrics, consider the following:

  * Only `SELECT` statements are allowed. The system rejects any statements that attempt to modify data. Manually execute and verify your query results and performance before you include them in the custom metrics configuration.
  * Design each SQL query to return a minimal number of result rows. We recommend that you specify fewer than five rows and a single row. This makes sure that the metrics and labels derived from the query results don't lead to excessive cardinality, which can negatively impact the performance of the monitoring system.
  * Optimize queries and make sure that they don't require excessive resources. Use `resourceLimits` to safeguard your database.
  * Each query must return rows with a unique combination of label values.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
