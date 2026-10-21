---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/improve-observability-custom-monitoring-metrics/
title: Improve observability using custom monitoring metrics \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:12.496298+00:00
---

# Improve observability using custom monitoring metrics  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/improve-observability-custom-monitoring-metrics/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Improve observability using custom monitoring metrics Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/improve-observability-custom-monitoring-metrics)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/improve-observability-custom-monitoring-metrics)

You can use custom metrics in AlloyDB Omni to define and collect application-specific metrics by executing SQL queries against your databases. Custom metrics use the `ObservabilityConfig` resource to define the metrics collection rules. 

For a full list of supported metrics, see [AlloyDB Omni metrics](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/reference/omni-metrics).

## Configure custom metrics using ObservabilityConfig

The `ObservabilityConfig` resource consists of two main sections, `dbClusterRefs` and `customMetrics`.

### `dbClusterRefs`

This section contains a list of references to the `DBCluster` resources that this configuration applies to. 

### `customMetrics`

This section defines the core configuration for custom metrics collection, including resource limits and query definitions.

#### Resource limits (`resourceLimits`)

To protect the database, the system enforces limits on custom queries. If you don't specify these limits in the manifest, the system uses the default values listed in the following table.

Parameter | Description | Default | Max | Units  
---|---|---|---|---  
`workMemory` | Specifies the [work_mem](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-WORK-MEM) for the specific database connection used by the monitoring agent to collect these metrics. This setting is local to the metric collection process and doesn't affect the global `work_mem` parameter configured in the `DBCluster` spec. | Global database setting | N/A | `KB`, `MB` (Default: `KB`)  
`maxParallelWorkers` | Specifies the [max_parallel_workers_per_gather](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS-PER-GATHER) for the specific database connection used by the monitoring agent. Set this to 0 to disable parallel query execution and minimize CPU impact. This setting is local to the metric collection process and doesn't affect the global database configuration. | Global database setting | N/A | Integer  
`statementTimeout` | Specifies the [statement_timeout](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-STATEMENT-TIMEOUT) for the specific database connection used by the monitoring agent. This limits the maximum time allowed for any single metric query to run. This setting is local to the metric collection process and doesn't affect the global database configuration. | Global database setting | `30s` | `ms`, `s` (Default: `ms`)  
  
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

The system uses the `alloydbmonitor` user to collect metrics. By default, the system creates this user with the [`LOGIN` attribute](https://www.postgresql.org/docs/current/role-attributes.html#ROLE-ATTRIBUTES) and grants it the [`pg_monitor` role](https://www.postgresql.org/docs/current/predefined-roles.html#PREDEFINED-ROLE-PG-MONITOR) across the database instance.

When you add custom metrics, make sure that this user has the appropriate additional permissions:

  * **User responsibility** : database administrators must manually grant `SELECT` privileges to the `alloydbmonitor` user for any specific application tables, views, or schemas used in your custom queries.
  * **Write privilege safety check** : to ensure system integrity and prevent accidental data modification, the monitoring agent performs a safety check. If the system finds that the `alloydbmonitor` user has any write privileges—for example, `INSERT`, `UPDATE`, and `DELETE`—on a target database, the system logs an error and refuses to collect custom metrics from that database.



### Granting permissions example

To grant read-only access to all tables in the `public` schema of a database named `warehousedb`, you must run the following command:
    
    
    psql -h <var>DB_CLUSTER_ENDPOINT</var> -U <var>DB_ADMIN_USER</var> -d warehousedb
    warehousedb=# GRANT SELECT ON ALL TABLES IN SCHEMA public TO alloydbmonitor;
    

## Sample manifest

The following example manifest configures the monitoring agent to connect to the `postgres` database and track transaction statistics using the `pg_stat_database` system view.
    
    
    ObservabilityConfig:
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
    

## Apply the configuration

To apply the custom metrics configuration, select the tab that matches your environment and follow the instructions.

###  Ansible 

To apply the configuration using Ansible, complete the following:

  1. Create a playbook named `custom_metrics.yml`:
         
         - name: Apply custom metrics for AlloyDB Omni DB
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
             - role: google.alloydbomni_orchestrator.monitor
         

  2. Execute the playbook using `ansible-playbook`. Specify the path to your observability configuration file as `resource_spec`.
         
         ansible-playbook custom_metrics.yml -i "DEPLOYMENT_SPEC" \
           -e "resource_spec=OBSERVABILITY_CONFIG_FILE"




###  `alloydbctl`

To apply the configuration using `alloydbctl`, run the following command:
    
    
    alloydbctl apply -d "DEPLOYMENT_SPEC" \
      -r "OBSERVABILITY_CONFIG_FILE"

### Read, update, and delete configuration

You can also read, update, or delete the configuration using Ansible or `alloydbctl`.

###  Ansible 

**Read:**

  1. Create a playbook named `get_obs_config.yml`:
         
         - name: Get status of custom metrics for AlloyDB Omni DB
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
             - role: google.alloydbomni_orchestrator.status
         

  2. Execute the playbook:
         
         ansible-playbook get_obs_config.yml -i "DEPLOYMENT_SPEC" \
           -e resource_type=ObservabilityConfig -e resource_name=OBSERVABILITY_CONFIG_NAME




**Update:**

Repeat the steps to Apply the configuration with the updated observability configuration file.

**Delete:**

  1. Create a playbook named `delete_obs_config.yml`:
         
         - name: Delete custom metrics configuration
           hosts: localhost
           vars:
             ansible_user: ANSIBLE_USER
             ansible_ssh_private_key_file: ANSIBLE_SSH_PRIVATE_KEY_FILE
           roles:
             - role: google.alloydbomni_orchestrator.delete
         

  2. Execute the playbook:
         
         ansible-playbook delete_obs_config.yml -i "DEPLOYMENT_SPEC" \
           -e resource_type=ObservabilityConfig -e resource_name=OBSERVABILITY_CONFIG_NAME




###  `alloydbctl`

**Read:**
    
    
    alloydbctl get -d "DEPLOYMENT_SPEC" \
      -t ObservabilityConfig -n OBSERVABILITY_CONFIG_NAME -o yaml

**Update:**

Repeat the steps to Apply the configuration with the updated observability configuration file.

**Delete:**
    
    
    alloydbctl delete -d "DEPLOYMENT_SPEC" \
      -t ObservabilityConfig -n OBSERVABILITY_CONFIG_NAME

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

Every custom metric automatically includes the following standard labels: `database`, `dbcluster`, `dbcluster_type`, `dbinstance`, `dbinstance_type`, `dbnamespace`, `dbnode`, and `dbnode_type`. For more information about these labels, see [AlloyDB Omni metric labels](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/reference/omni-metrics#labels)

### Metrics collection metrics

These metrics indicate the status of each metric collection cycle. You can find detailed error messages, including which specific query timed out or failed, in the monitoring agent logs.
    
    
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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
