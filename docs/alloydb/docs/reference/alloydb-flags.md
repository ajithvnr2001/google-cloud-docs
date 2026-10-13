---
url: https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags/
title: AlloyDB flags \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:00.453380+00:00
---

# AlloyDB flags  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Reference ](https://docs.cloud.google.com/alloydb/docs/reference/rest)



Send feedback 

#  AlloyDB flags Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the database flags that AlloyDB for PostgreSQL uses to enable and manage various service features unique to AlloyDB. For a list of all database flags that AlloyDB supports, see [Supported database flags](https://docs.cloud.google.com/alloydb/docs/reference/database-flags).

Flags marked with **Instance restarts** mean that AlloyDB restarts an instance whenever you set, remove, or modify this flag on that instance. The flag's value persists for the instance until you modify it again.

### alloydb_ai_nl.enabled

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls whether the AlloyDB AI natural language features are enabled.

### alloydb.enable_anon

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls the availability of the `anon` (PostgreSQL Anonymizer) extension in an AlloyDB instance. Set this parameter to `on` and restart the instance. Then, add the `anon` extension to individual databases in the instance by using the `CREATE EXTENSION` command. Before you can install the `anon` extension, you must first install the [`pgcrypto`](https://www.postgresql.org/docs/17/pgcrypto.html) extension.

The [`anon`](https://postgresql-anonymizer.readthedocs.io/) extension lets you hide or replace personally identifiable information (PII) or commercially sensitive data within your database.

### alloydb.enable_auto_explain

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls the availability of the `auto_explain` extension in an AlloyDB instance. Set the parameter to `on` and restart the instance.

The [`auto_explain`](https://www.postgresql.org/docs/17/auto-explain.html) extension enables automatic logging of execution plans of slow statements, for troubleshooting and more. It provides an automated way to perform the functionality of the `EXPLAIN` command.

### alloydb.enable_cache_aware_costing

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Lets the AlloyDB query planner adjust the estimated IO cost of index scans based on how many index and table pages may be already available in the shared buffer when execution starts.

For more information, see [Enable cache awareness for index scan query plans](https://docs.cloud.google.com/alloydb/docs/cache-aware-costs).

### alloydb.enable_pg_bigm

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls the availability of the `pg_bigm` extension in an AlloyDB instance. Set the parameter to `on` and restart the instance. Then add the `pg_bigm` extension to individual databases in the instance by using the `CREATE EXTENSION` command.

The [`pg_bigm`](https://pgbigm.osdn.jp/pg_bigm_en-1-2.html) extension provides full text search capability in PostgreSQL using 2-gram (bigram) indexes for faster full text searches.

### alloydb.enable_pg_cron

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls the availability of the `pg_cron` extension in an AlloyDB instance. Set the parameter to `on` and restart the instance. Then add the `pg_cron` extension to individual databases in the instance by using the `CREATE EXTENSION` command.

The [`pg_cron`](https://github.com/citusdata/pg_cron/#readme) extension provides a cron-based job scheduler for PostgreSQL that runs inside the database as an extension. It uses the same syntax as regular `cron`, and it lets you schedule PostgreSQL commands directly from the database.

### alloydb.enable_pg_hint_plan

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls the availability of the `pg_hint_plan` extension in an AlloyDB instance. Set the parameter to `on` and restart the instance. Then add the `pg_hint_plan` extension to individual databases in the instance by using the `CREATE EXTENSION` command.

The [`pg_hint_plan`](https://pghintplan.osdn.jp/pg_hint_plan.html) extension lets you to improve PostgreSQL execution plans using hints, which are descriptions in SQL comments.

### alloydb.enable_pg_wait_sampling

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Enables AlloyDB to collect sampling statistics of wait events. Set the parameter to `on` and restart the instance. Then, add the `pg_wait_sampling` extension to individual databases in the instance by using the `CREATE EXTENSION` command.

The [`pg_wait_sampling`](https://github.com/postgrespro/pg_wait_sampling) extension aggregates and summarizes the wait event data. You can query these views to gain insights into wait times, frequencies, and relative importance of different wait events.

### alloydb.enable_pgaudit

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls the availability of the `pgaudit` extension in an AlloyDB instance. Set the parameter to `on` and restart the instance. Then add the `pgaudit` extension to individual databases in the instance by using the `CREATE EXTENSION` command.

The [`pgaudit`](https://www.pgaudit.org/) extension provides detailed session and object audit logging using the standard logging facility provided by PostgreSQL.

**Warning:** In AlloyDB Omni only, enabling this extension and the PostgreSQL `logging_collector` parameter might result in loss of audit logs. To enable the PostgreSQL and audit logs, set `logging_collector` to `off` and `alloydb.enable_pgaudit` to `true`. To enable the PostgreSQL log, set `logging_collector` to `on` and `allobydb.enable_pgaudit` to `false`. 

### alloydb.enable_pglogical

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls the availability of the `pglogical` extension in an AlloyDB instance. Set the parameter to `on` and restart the instance. Then add the `pglogical` extension to individual databases in the instance by using the `CREATE EXTENSION` command.

The [`pglogical`](https://github.com/2ndQuadrant/pglogical#readme) extension provides logical streaming replication for PostgreSQL using a publish-subscribe model.

### alloydb.enable_named_hints

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Enables the AlloyDB [named hints](https://docs.cloud.google.com/alloydb/docs/create-manage-query-plan-patches) feature. Set the parameter to `on`.

### alloydb.iam_authentication

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Enables the use of Identity and Access Management (IAM) (Identity and Access Management) authentication with an AlloyDB instance.

### alloydb.iam_group_authentication

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

IAM group authentication is available in [Preview](https://cloud.google.com/products#product-launch-stages) for new AlloyDB clusters. To enable this feature on an existing cluster, contact your Google Cloud account team.

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Enables the use of Identity and Access Management (IAM) (Identity and Access Management) group authentication with an AlloyDB instance.

### alloydb_sync.enabled

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Enables or disables the `alloydb_sync` extension. Requires a database restart to take effect.

### bigquery_fdw.enabled

Type| `boolean`  
---|---  
Default| `on`  
Instance restarts| Yes  
  
Enables or disables the `bigquery_fdw` extension. Requires a database restart to take effect.

### bigquery_fdw.enable_vector_downcasting

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Supports the automatic downcasting of `ARRAY<FLOAT64>` from BigQuery to `float4[]` values used by the vector data type in PostgreSQL. Precision loss is expected in this process.

### scann.enable_preview_features

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Enables the use of the following features that are available in [Preview](https://cloud.google.com/products#product-launch-stages):

  * [Automatic index maintenance](https://docs.cloud.google.com/alloydb/docs/ai/maintain-vector-indexes#maintain-index-automatically) incrementally manages the index such that when your dataset grows, AlloyDB splits large outlier partitions and tries to provide better QPS and search results.
  * [Deferred index creation](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index#deferred-index-creation-for-empty-or-nearly-empty-tables) defers index creation for empty rows or tables with insufficient rows.
  * [Four-level tree indexes](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index#create-scann-index-granular) support tables with more than one billion vector rows.



### scann.enable_index_with_insufficient_data

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Controls whether deferred index creation is explicitly enabled for empty tables or tables with insufficient rows, without enabling other preview features. For more information, see [Deferred index creation](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index#deferred-index-creation-for-empty-or-nearly-empty-tables).

### scann.enable_index_maintenance

Type| `boolean`  
---|---  
Default| `on`  
Instance restarts| Yes  
  
Controls whether the [automatic vector index maintenance](https://docs.cloud.google.com/alloydb/docs/ai/maintain-vector_indexes) features are enabled.

### scann.max_background_workers

Type| `integer`  
---|---  
Default| `1`  
Instance restarts| Yes  
  
Controls the number of background workers used for automatic vector index maintenance. For more information, see [Increase automatic maintenance throughput](https://docs.cloud.google.com/alloydb/docs/ai/maintain-vector-indexes#increase-auto-maintenance-throughput).

### scann.maintenance_background_naptime_s

Type| `integer`  
---|---  
Default| `1`  
Instance restarts| Yes  
  
Controls the minimum delay between background worker runs for automatic vector index maintenance. The default value is `1` minute.

### scann.max_allowed_num_levels

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Type | `integer`  
---|---  
Default | `2`  
Minimum value | `1`  
Maximum value | `3`  
Instance restarts | No  
  
Determines the highest value you can set for [`max_num_levels`](https://docs.cloud.google.com/alloydb/docs/ai/scann-index-reference) when [creating a ScaNN index](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index#create-scann-index-granular).

### alloydb.logical_decoding

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Enables the PostgreSQL logical decoding infrastructure in an AlloyDB instance.

[Logical decoding](https://www.postgresql.org/docs/17/logicaldecoding.html) provides the infrastructure necessary to stream data modifications to external consumers.

### alloydb.log_throttling_window

Type| `integer`  
---|---  
Default| `0`  
Instance restarts| No  
  
Controls whether AlloyDB records duplicate log messages received during a specified time window.

If set to a value greater than `0`, then AlloyDB starts a timer that many seconds long whenever it records a log message. If AlloyDB receives the identical log message before the timer expires, it does not record the message. After the timer expires, AlloyDB appends a count of any skipped messages to the next occurrence of the same log message that it records.

If set to `0`, then AlloyDB records all duplicate log messages.

### alloydb.promote_cancel_to_terminate

Type| `boolean`  
---|---  
Default| `on`  
Instance restarts| No  
  
If set to `true`, then any query cancellation requests due to issues such as lock timeouts, statement timeouts, and recovery (replay) conflicts that AlloyDB encounters, are promoted to forced backend termination requests.

By promoting the cancellation requests, AlloyDB helps prevent stuck backends from blocking log replay and other backends.

### alloydb.pg_authid_select_role

Type| `string`  
---|---  
Default| An empty string  
Instance restarts| No  
  
Name of the PostgreSQL role used to grant permission to query the `pg_authid` catalog table. You need this flag to perform operations, such as exporting roles during migrations or setting up connection proxies, that require reading authentication identifiers.

### alloydb.pg_shadow_select_role

Type| `string`  
---|---  
Default| An empty string  
Instance restarts| No  
  
Name of the PostgreSQL role that is to be used to grant permission to query the `pg_shadow` view.

### alloydb.enable_auditlog_volume_reduction

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Enables a mechanism to reduce the volume of audit logs generated by the instance. Setting this flag to `on` requires an instance restart.

### alloydb.enable_pg_squeeze

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Set to `on` to reduce table and index bloat in a more efficient and less disruptive way as compared to other PostgreSQL bloat reduction methods such as `VACUUM`.

### google_storage.log_replay_throttle_read_transactions

Type| `boolean`  
---|---  
Default| `on`  
Instance restarts| No  
  
Controls whether lag-based throttling of read transactions is enabled on read nodes. If the parameter is set to `on`, then when replication lag exceeds one second, new read transactions are prevented from starting until lag is under one second or until `google_storage.log_replay_max_backend_throttle_duration` expires.

### google_storage.log_replay_max_backend_throttle_duration

Type| `integer`  
---|---  
Default| `60000`  
Instance restarts| No  
  
The maximum time a backend is throttled when lag is high. Unit is milliseconds. This only takes effect when `google_storage.log_replay_throttle_read_transactions` is `on`.

### google_ml_integration.enable_ai_function_acceleration

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Controls whether the query executor is allowed to offload eligible AI operations to the AI function apply node for acceleration.

### google_ml_integration.enable_cost_optimized_ai_functions

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Controls whether cost-optimized AI functions are enabled for the `google_ml_integration` extension.

### google_ml_integration.enable_faster_embedding_generation

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Controls whether faster generation of embeddings is enabled.

### google_ml_integration.enable_forecasting

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Controls whether time series forecasting features are enabled.

### google_ml_integration.enable_model_support

Type| `boolean`  
---|---  
Default| `on`  
Instance restarts| No  
  
Controls whether support for registering and querying ML models (model endpoints) is enabled.

### google_ml_integration.runtime_accuracy_check

Type| `boolean`  
---|---  
Default| `on`  
Instance restarts| No  
  
Controls whether runtime accuracy checks are enabled for cost-optimized AI functions to ensure fallback when precision drops.

### google_ml_integration.enable_preview_ai_functions

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Controls whether preview AI functions are available for the `google_ml_integration` extension.

### google_ml_integration.max_memory_usage_mb

Type| `integer`  
---|---  
Default| Dynamically adjusted based on VM size  
Instance restarts| No  
  
Lets you tune performance for the ML integration at the cost of higher memory usage.

### google_ml_integration.enable_ai_query_engine

Type| `boolean`  
---|---  
Default| `on`  
Instance restarts| No  
  
Controls whether the AI query engine is enabled.

### google_ml_integration.optimized_ml_agent

Type| `boolean`  
---|---  
Default| `on`  
Instance restarts| No  
  
Controls whether the optimized ML agent is enabled.

### parameterized_views.enabled

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| Yes  
  
Controls whether the parameterized view features are enabled.

The `parameterized_views.enabled` flag setting isn't replicated automatically and must be replicated manually on each instance. You must enable the `parameterized_views.enabled` flag on each replica instance before you query parameterized views on the replica. For more information, see [Manage application data security using AlloyDB parameterized secure views](https://docs.cloud.google.com/alloydb/docs/manage-application-data-security-parameterized-secure-views#before-you-begin).

### parameterized_views.json_results_max_rows

Type| `integer`  
---|---  
Default| `1,000,000`  
Instance restarts| No  
  
Sets the maximum number of rows for JSON results from the [`execute_parameterized_query()`](https://docs.cloud.google.com/alloydb/docs/manage-application-data-security-parameterized-secure-views#create-parameterized-secure-view) function.

### parameterized_views.json_results_max_size

Type| `integer`  
---|---  
Default| `1,048,576`  
Instance restarts| No  
  
Sets the maximum JSON results size in kilobytes (KB) from the [`execute_parameterized_query()`](https://docs.cloud.google.com/alloydb/docs/manage-application-data-security-parameterized-secure-views#create-parameterized-secure-view) function.

### parameterized_views.max_parallel_workers_per_gather

Type| `integer`  
---|---  
Default| `-1`  
Instance restarts| No  
  
Sets the maximum number of parallel processes per executor node when a query is run using the parameterized views API. `-1` means no limit. This limit applies only if it's more restrictive than [`max_parallel_workers_per_gather`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-MAX-PARALLEL-WORKERS-PER-GATHER).

### parameterized_views.statement_timeout

Type| `integer`  
---|---  
Default| `0`  
Instance restarts| No  
  
Sets the maximum allowed duration in milliseconds of statements run using the parameterized views API. `0` means no limit. This limit applies only if it's more restrictive than [`statement_timeout`](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-STATEMENT-TIMEOUT).

### parameterized_views.temp_file_limit

Type| `integer`  
---|---  
Default| `-1`  
Instance restarts| No  
  
Limits the total size in kB of all temporary files used by each process when run using the parameterized views API. `-1` means no limit. This limit applies only if it's more restrictive than [`temp_file_limit`](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-TEMP-FILE-LIMIT).

### parameterized_views.work_mem

Type| `integer`  
---|---  
Default| `0`  
Instance restarts| No  
  
Sets the maximum memory in kB to be used for query workspaces when it's run using the parameterized views API. `0` means no limit. This limit applies only if it's more restrictive than [`work_mem`](https://www.postgresql.org/docs/current/runtime-config.html#GUC-WORK-MEM).

### perfsnap.enable_auto_snapshots

Type| `boolean`  
---|---  
Default| `off`  
Instance restarts| No  
  
Controls whether automatic performance snapshots are enabled for the instance. These snapshots provide historical performance data for troubleshooting and analysis.

### perfsnap.interval

Type| `integer`  
---|---  
Default| `86400`  
Instance restarts| No  
  
Sets the interval in seconds for automatic performance snapshots.

### perfsnap.retention

Type| `string`  
---|---  
Default| `7 days`  
Instance restarts| No  
  
Sets the retention period for automatic performance snapshots.

## vector_assist.enabled

**Preview — Vector assist**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Type| `boolean`  
---|---  
Default| `on`  
Instance restarts| no  
  
Controls whether [Vector assist](https://docs.cloud.google.com/alloydb/docs/ai/vector-assist-overview) features are enabled.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
