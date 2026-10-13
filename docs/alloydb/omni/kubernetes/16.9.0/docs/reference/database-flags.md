---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/database-flags/
title: Supported database flags \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:31.302030+00:00
---

# Supported database flags  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/database-flags/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  Supported database flags Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/database-flags)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/database-flags)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/database-flags)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/database-flags)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/database-flags)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/database-flags)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/database-flags)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/database-flags)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/database-flags)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/database-flags)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/database-flags)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/reference/database-flags)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/database-flags)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/database-flags)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/database-flags)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/database-flags)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/database-flags)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/database-flags)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/database-flags)

AlloyDB Omni supports all database flags provided by standard [PostgreSQL](https://www.postgresql.org/docs/16/index.html) versions. This page lists the database flags that AlloyDB Omni provides in addition to the standard database flags. 

You use database flags for many operations, including adjusting PostgreSQL parameters, adjusting options, and configuring and tuning instances.

For more information about setting database flags in AlloyDB Omni, see [Configure AlloyDB Omni database flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/configure-database-flags).

## AlloyDB Omni flags

The table's other columns contain additional information about each AlloyDB Omni flag:pG_

  * Click a flag name to see its usage instructions.

  * The **Default value** column displays the value that AlloyDB Omni sets for this flag in a new instance, unless you specify a different value when creating the instance.

**Standard default** indicates that the flag has a default value that's not set by AlloyDB Omni. To learn more, click the flag's name.

  * In the **Restart required** column, **Yes** indicates that you need to restart AlloyDB Omni when you set, remove, or modify the flag on the instance. The flag's value persists for the instance until you modify it again.

  * In the **Replica restrictions** column, **Yes** indicates the following restrictions on how you can use the flag:

    * Before setting this flag on your cluster's primary instance, set the flag on each of your cluster's replica instances.

    * If the primary instance has this flag set, then the value of this flag on any replica instance must be equal to or greater than the primary instance's value for this flag.




A | C | D | E | F | G | H | I | J | L | M | O | P | R | S | T | V | W

AlloyDB Omni flag | Default value | Restart required | Replica restrictions  
---|---|---|---  
[alloydb.audit_log_line_prefix](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/alloydb-flags#alloydb.audit_log_line_prefix) | `%m [%p]: [%l-1] db=%d,user=%u` | Yes | No  
[alloydb.enable_pgaudit](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/alloydb-flags#alloydb.enable_pgaudit) | `off` | Yes | No  
[alloydb.log_throttling_window](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/alloydb-flags#alloydb.log_throttling_window) | No | No  
[alloydb.promote_cancel_to_terminate](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/alloydb-flags#alloydb.promote_cancel_to_terminate) | `off` | No | No  
[alloydb.pg_shadow_select_role](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/alloydb-flags#alloydb.pg_shadow_select_role) | An empty string | No | No  
[enable_google_adaptive_autovacuum](https://docs.cloud.google.com/alloydb/docs/adaptive-autovacuum) | `on` | No | No  
[google_columnar_engine.auto_columnarization_schedule](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#auto-columnarization-schedule) | `'EVERY 1 HOUR'` | No | No  
[google_columnar_engine.enable_auto_columnarization](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#enable-auto-columnarization) | `on` | No | No  
[google_columnar_engine.enable_columnar_scan](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#enable-columnar-scan) | `on` | No | No  
[google_columnar_engine.enabled](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#enabled) | `off` | Yes | No  
[google_columnar_engine.memory_size_in_mb](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#memory-size-in-mb) | 30% of instance RAM | Yes | No  
[google_columnar_engine.omni_storage_cache_directory](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#omni-storage-cache-directory) | An empty string | Yes | No  
[google_columnar_engine.refresh_threshold_percentage](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#refresh-threshold-percentage) | `50` | No | No  
[google_columnar_engine.refresh_threshold_scan_count](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#refresh-threshold-scan-count) | `5` | No | No  
[google_columnar_engine.relations](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#relations) | An empty string | No | No  
[google_db_advisor.auto_advisor_max_time_in_seconds](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/index-advisor-flags#auto_advisor_max_time_in_seconds) | `1800` | No | No  
[google_db_advisor.auto_advisor_schedule](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/index-advisor-flags#auto_advisor_schedule) | `'EVERY 24 HOURS'` | No | No  
[google_db_advisor.enable_auto_advisor](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/index-advisor-flags#enable_auto_advisor) | `on` | No | No  
[google_db_advisor.enabled](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/index-advisor-flags#enabled) | `on` | Yes | No  
[google_db_advisor.max_index_width](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/index-advisor-flags#max_index_width) | `2` | No | No  
[google_db_advisor.max_num_indexable_columns](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/index-advisor-flags#max_num_indexable_columns) | `1000` | No | No  
[google_db_advisor.max_statement_length](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/index-advisor-flags#max_statement_length) | `102400` | No | No  
[google_db_advisor.max_storage_size_in_mb](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/index-advisor-flags#%0A%20%20max_storage_size_in_mb) | `0` | No | No  
[google_db_advisor.recommendation_max_time_in_seconds](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/index-advisor-flags#recommendation_max_time_in_seconds) | `600` | No | No  
[google_db_advisor.recommend_indexes_on_partitions](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/index-advisor-flags#recommend_indexes_on_partitions) | `off` | No | No  
[google_db_advisor.top_k_slowest_statements](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/index-advisor-flags#%0A%20%20top_k_slowest_statements) | `100` | No | No  
[google_job_scheduler.maintenance_cpu_percentage](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#maintenance-cpu-percentage) | `20` | No | No  
[google_job_scheduler.max_parallel_workers_per_job](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/columnar-engine-flags#max-parallel-workers-per-job) | `2` | No | No  
[google_ml_integration.enable_model_support](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/model-endpoint-reference) | `off` | No |   
[google_storage.log_replay_throttle_read_transactions](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/alloydb-flags#google_storage.log_replay_throttle_read_transactions) | `on` | No | No  
[password.enforce_password_does_not_contain_username](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#enforce_password_does_not_contain_username) | `OFF` | No | No  
[password.enforce_expiration](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#enforce-expiration) | `OFF` | No | No  
[password.enforce_complexity](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#enforce-complexity) | `OFF` | No | No  
[password.expiration_in_days](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#expiration-in-days) | `90` | No | No  
[password.min_uppercase_letters](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#min-uppercase-letters) | `0` | No | No  
[password.max_uppercase_letters](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#max-uppercase-letters) | `1000` | No | No  
[password.min_lowercase_letters](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#min-lowercase-letters) | `0` | No | No  
[password.max_lowercase_letters](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#max-lowercase-letters) | `1000` | No | No  
[password.min_numerical_chars](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#min-numerical-chars) | `0` | No | No  
[password.max_numerical_chars](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#max-numerical-chars) | `1000` | No | No  
[password.min_special_chars](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#min-special-chars) | `0` | No | No  
[password.max_special_chars](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#max-special-chars) | `1000` | No | No  
[password.min_pass_length](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#min-pass-length) | `0` | No | No  
[password.max_pass_length](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#max-pass-length) | `1000` | No | No  
[password.notify_expiration_in_days](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/password-policy-flags#notify-expiration-in-days) | `30` | No | No  
[squeeze.worker_autostart](https://github.com/cybertec-postgresql/pg_squeeze#enable--disable-table-processing) | Standard default | No | No  
[squeeze.worker_role](https://github.com/cybertec-postgresql/pg_squeeze#enable--disable-table-processing) | Standard default | No | No  
[squeeze.workers_per_database](https://github.com/cybertec-postgresql/pg_squeeze#running-multiple-workers-per-database) | Default value is `1` | No | No  
[squeeze.max_xlock_time](https://github.com/cybertec-postgresql/pg_squeeze#control-the-impact-on-other-backends) | Default value is `1`. Set to any value between `1` and `2147483647` | No | No  
  
## Standard PostgreSQL flags that need restart

The following standard PostgreSQL flags require a restart of AlloyDB Omni when you set, remove, or modify the flag on the instance. The flag's value persists for the instance until you modify it again.

  * [autovacuum_freeze_max_age](https://www.postgresql.org/docs/16/runtime-config-autovacuum.html#GUC-AUTOVACUUM-FREEZE-MAX-AGE)
  * [autovacuum_max_workers](https://www.postgresql.org/docs/16/runtime-config-autovacuum.html#GUC-AUTOVACUUM-MAX-WORKERS)
  * [autovacuum_multixact_freeze_max_age](https://www.postgresql.org/docs/16/runtime-config-autovacuum.html#GUC-AUTOVACUUM-MULTIXACT-FREEZE-MAX-AGE)
  * [cron.database_name](https://github.com/citusdata/pg_cron#what-is-pg_cron)
  * [cron.log_run](https://github.com/citusdata/pg_cron/blob/main/src/pg_cron.c)
  * [cron.log_statement](https://github.com/citusdata/pg_cron/blob/main/src/pg_cron.c)
  * [cron.max_running_jobs](https://github.com/citusdata/pg_cron/blob/main/src/pg_cron.c)
  * [max_connections](https://www.postgresql.org/docs/16/runtime-config-connection.html#GUC-MAX-CONNECTIONS)
  * [max_locks_per_transaction](https://www.postgresql.org/docs/16/runtime-config-locks.html#GUC-MAX-LOCKS-PER-TRANSACTION)
  * [max_logical_replication_workers](https://www.postgresql.org/docs/16/runtime-config-replication.html#GUC-MAX-LOGICAL-REPLICATION-WORKERS)
  * [max_pred_locks_per_page](https://www.postgresql.org/docs/16/runtime-config-locks.html#GUC-MAX-PRED-LOCKS-PER-PAGE)
  * [max_pred_locks_per_relation](https://www.postgresql.org/docs/16/runtime-config-locks.html#GUC-MAX-PRED-LOCKS-PER-RELATION)
  * [max_pred_locks_per_transaction](https://www.postgresql.org/docs/16/runtime-config-locks.html#GUC-MAX-PRED-LOCKS-PER-TRANSACTION)
  * [max_prepared_transactions](https://www.postgresql.org/docs/16/runtime-config-resource.html#GUC-MAX-PREPARED-TRANSACTIONS)
  * [max_replication_slots](https://www.postgresql.org/docs/16/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS)
  * [max_wal_senders](https://www.postgresql.org/docs/16/runtime-config-replication.html#GUC-MAX-WAL-SENDERS)
  * [max_worker_processes](https://www.postgresql.org/docs/16/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES)
  * [old_snapshot_threshold](https://www.postgresql.org/docs/16/runtime-config-resource.html#GUC-OLD-SNAPSHOT-THRESHOLD)
  * [pg_stat_statements.max](https://www.postgresql.org/docs/16/pgstatstatements.html#id-1.11.7.38.8)
  * [pglogical.batch_inserts](https://github.com/2ndQuadrant/pglogical#configuration-options)
  * [pglogical.synchronous_commit](https://github.com/2ndQuadrant/pglogical#synchronous-replication)
  * [pglogical.use_spi](https://github.com/2ndQuadrant/pglogical#configuration-options)
  * [shared_buffers](https://www.postgresql.org/docs/16/runtime-config-resource.html#GUC-SHARED-BUFFERS)
  * [track_activity_query_size](https://www.postgresql.org/docs/16/runtime-config-statistics.html#GUC-TRACK-ACTIVITY-QUERY-SIZE)
  * [track_commit_timestamp](https://www.postgresql.org/docs/16/runtime-config-replication.html#GUC-TRACK-COMMIT-TIMESTAMP)
  * [wal_buffers](https://www.postgresql.org/docs/16/runtime-config-wal.html#GUC-WAL-BUFFERS)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
