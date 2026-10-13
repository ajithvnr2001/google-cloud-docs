---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/reference/omni-metrics/
title: AlloyDB Omni metrics \u00a0|\u00a0 AlloyDB Omni using RPM: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:12.709826+00:00
---

# AlloyDB Omni metrics  |  AlloyDB Omni using RPM: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/reference/omni-metrics/

This page documents AlloyDB Omni version **18.3.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/reference/database-flags)



Send feedback 

#  AlloyDB Omni metrics Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down


AlloyDB Omni provides metrics for monitoring the health and performance of the database. These metrics are exposed in a format suitable for scraping by [Prometheus](https://prometheus.io/). 

## Labels

AlloyDB Omni exposes the following types of labels.

### Resource labels

AlloyDB Omni exposes the following resource labels that uniquely identify the database container that the metrics belong to. 

Label key | Label value  
---|---  
dbnamespace | Namespace of the dbcluster CR  
dbcluster | Name of the dbcluster CR  
dbinstance | Name of the dbinstance CR. Only the dbinstance of ReadPool type is supported. If the database container does not belong to a ReadPool dbinstance, this value is `n/a`  
dbnode | Name of the instance CR. Every instance CR has a one-to-one mapping to a database container.   
  
### System metadata labels

System metadata labels changes dynamically when the `roles` of the database instance changes. For example, when your database cluster is promoted from secondary to primary, `dbcluster_type` changes from `Secondary` to `Primary`.

Label key | Label value  
---|---  
dbcluster_type | Disaster recovery (DR) role of the dbcluster CR. Can be `Primary` or `Secondary`  
dbinstance_type | Type of the dbinstance CR. If the container belongs to a ReadPool dbinstance, this value is `ReadPool`, otherwise this value is `n/a`  
dbnode_type | HA role of the dbnode, can be `Primary` or `Standby`  
  
### Metric labels

The specific labels of each metric are listed in the following tables. For example, `database` means the name of a Postgres database hosted inside the AlloyDB Omni database instance.

## Metrics

AlloyDB Omni exposes the following metrics. The metrics list mentions only metrics labels. All metrics start with `alloydb_omni`. To learn more about metric types, see [Metric types](https://prometheus.io/docs/concepts/metric_types/).

Name | Description | Label | Unit | Type  
---|---|---|---|---  
alloydb_omni_database_postgresql_backends |  The number of active and idle connections to the AlloyDB Omni instance. |  |  |  gauge  
alloydb_omni_database_postgresql_chill_cache_get_entry_calls_total | The total number of calls to retrieve data entries from the ultra fast disk cache. |  |  | counter  
alloydb_omni_database_postgresql_chill_cache_num_hits_total | The total number of successful retrievals of data entries from the ultra fast disk cache. | `prewarm`: the hits that occur during the prewarm phase |  | counter  
alloydb_omni_database_postgresql_max_connections |  The current value of the Postgres max_connections runtime parameter. |  |  |  gauge  
alloydb_omni_database_postgresql_up |  Whether the Postgres main process is running, 1 if running, 0 if down. |  |  |  gauge  
alloydb_omni_database_postgresql_uptime_second |  Time elapsed since the Postgres main process started. |  |  second |  gauge  
alloydb_omni_database_postgresql_vacuum_oldest_transaction_age |  The current age of the oldest uncommitted transaction that is blocking vacuum operation. It's measured in the number of transactions that started after the oldest transaction. |  `type`: one of [running, prepared, replication_slot, replica] |  |  gauge  
alloydb_omni_database_postgresql_vacuum_transaction_id_utilization_percentage |  The ratio of transaction ID space consumed. 1 means 100%. |  |  |  gauge  
alloydb_omni_instance_postgresql_backends_by_state |  Current number of connections. |  `state`: state of the connections that is one of [idle, active, idle_in_transaction, idle_in_transaction_aborted, disabled, fastpath_function_call] |  |  gauge  
alloydb_omni_instance_postgresql_backends_for_top_applications |  Current number of connections per application. |  `application_name`: name of the application |  |  gauge  
alloydb_omni_instance_postgresql_blks_hit_count_total |  Total number of times Postgres found the requested block in the buffer cache. |  |  |  counter  
alloydb_omni_instance_postgresql_blks_read_count_total |  Total number of blocks read by Postgres that were not in the Postgres buffer cache. |  |  |  counter  
alloydb_omni_instance_postgresql_committed_transactions_count_total |  Total number of transactions committed. |  |  | counter  
alloydb_omni_instance_postgresql_deadlock_count_total |  Number of deadlocks detected. |  |  |  counter  
alloydb_omni_instance_postgresql_new_connections_count_total |  Total number of new connections. |  |  |  counter  
alloydb_omni_instance_postgresql_rolledback_transactions_count_total |  Total number of transactions rolled back. |  |  |  counter  
alloydb_omni_instance_postgresql_temp_bytes_written_count_total |  Total amount of data written to temporary files by queries. |  |  byte |  counter  
alloydb_omni_instance_postgresql_temp_files_written_count_total |  Total number of temporary files used for writing data while performing internal algorithms. |  |  |  counter  
alloydb_omni_instance_postgresql_tuples_deleted_count_total |  Total number of rows deleted. |  |  |  counter  
alloydb_omni_instance_postgresql_tuples_fetched_count_total |  Total number of rows fetched. |  |  |  counter  
alloydb_omni_instance_postgresql_tuples_inserted_count_total |  Total number of rows inserted. |  |  |  counter  
alloydb_omni_instance_postgresql_tuples_returned_count_total |  Total number of rows returned. |  |  |  counter  
alloydb_omni_instance_postgresql_tuples_updated_count_total |  Total number of rows updated. |  |  |  counter  
alloydb_omni_instance_postgresql_version |  The version of the PostgreSQL database. In `MAJOR.MINOR` format, for example, `16.3` |  |  |  gauge  
alloydb_omni_instance_postgresql_wait_count_total |  Total wait count for a wait event. | 

  * `wait_event_name`: name of the wait event
  * `wait_event_type`: type of the wait event

|  |  counter  
alloydb_omni_instance_postgresql_wait_time_us_total |  Total time elapsed for a wait event.  | 

  * `wait_event_name`: name of the wait event
  * `wait_event_type`: type of the wait event

|  us |  counter  
alloydb_omni_instance_postgresql_replication_flush_lag_ms |  Time elapsed between flushing recent WAL locally and receiving notification that the replica server has written and flushed it (but not yet applied it). | 

  * `application_name`: application_name in the replica's connection string to the primary that matches the name of the replica instance CR.
  * `client_addr`: IP address of the replica instance.

|  ms |  gauge  
alloydb_omni_instance_postgresql_replication_replay_lag_ms |  Time elapsed between flushing recent WAL locally and receiving notification that the replica server has written, flushed and applied it. | 

  * `application_name`: application_name in the replica's connection string to the primary. It matches the name of the replica instance CR.
  * `client_addr`: IP address of the replica instance.

|  ms |  gauge  
alloydb_omni_instance_postgresql_replication_state |  State of each replica connected to the primary. Its value is always `1`. | 

  * `application_name`: application_name in the replica's connection string to the primary. It matches the name of the replica instance CR.
  * `client_addr`: IP address of the replica instance.
  * `state`: one of [startup, catchup, streaming, backup, stopping]

|  | gauge  
alloydb_omni_instance_postgresql_replication_write_lag_ms |  Time elapsed between flushing recent WAL locally and receiving notification that the replica server has written it (but not yet flushed it or applied it). | 

  * `application_name`: application_name in the replica's connection string to the primary. It matches the name of the replica instance CR.
  * `client_addr`: IP address of the replica instance.

|  ms |  gauge  
alloydb_omni_memory_available_byte |  Estimate of the amount of memory available for allocation. |  |  byte |  gauge  
alloydb_omni_memory_limit_byte |  Memory limit of the database instance that's specified in the `primarySpec` section of `spec` portion of the database cluster manifest file. |  |  byte |  gauge  
alloydb_omni_memory_postgresql_shared_buffers_active_byte | Current size of the PostgreSQL shared buffers, in bytes. The [automatic memory management](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/automatic-memory-management) module automatically adjusts this based on memory pressure. |  | byte | gauge  
alloydb_omni_memory_postgresql_shared_buffers_byte | Upper limit for the size of the PostgreSQL shared buffers, as configured with the `shared_buffers` parameter, in bytes. |  | byte | gauge  
alloydb_omni_memory_postgresql_shared_buffers_min_byte | Lower limit for the size of PostgreSQL shared buffers, in bytes. |  | byte | gauge  
alloydb_omni_memory_postgresql_terminated_backends_count_total | Total number of PostgreSQL backends terminated by the [automatic memory management](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/automatic-memory-management) module due to memory pressure. |  |  | counter  
alloydb_omni_memory_used_byte |  Estimate of the used database instance memory that can't be freed. |  |  byte |  gauge  
alloydb_omni_node_cpu_mcpu |  Number of mCPUs allocated. 1000 mCPU = 1 CPU |  |  mCPU |  gauge  
alloydb_omni_node_cpu_usage_second_total |  Total CPU seconds used. |  |  second |  counter  
alloydb_omni_node_network_received_bytes_count_total |  Network received bytes count on the AlloyDB Omni instance. |  |  byte |  counter  
alloydb_omni_node_network_sent_bytes_count_total |  Network sent bytes count on the AlloyDB Omni instance. |  |  byte |  counter  
alloydb_omni_node_storage_limit_per_disk_byte |  Storage limit in byte. |  `disk`: name of the disk |  byte |  gauge  
alloydb_omni_node_storage_read_bytes_count_total |  Number of bytes read from disk. |  |  byte |  counter  
alloydb_omni_node_storage_read_ops_count_total |  Number of disk read IO operations. |  |  |  counter  
alloydb_omni_node_storage_usage_per_disk_byte |  Storage used in bytes per disk. |  `disk`: name of the disk |  byte |  gauge  
alloydb_omni_node_storage_write_bytes_count_total |  Number of bytes written to disk. |  |  byte |  counter  
alloydb_omni_node_storage_write_ops_count_total |  Number of disk write IO operations. |  |  |  counter  
  
### Database-level metrics

These metrics are collected on a per AlloyDB Omni database instance per Postgres database level. You can create multiple Postgres databases in one database instance. All these metrics have resource, system metadata, and "database" labels. The database label is the name of the Postgres database that the metric belongs to.

The presence of certain labels and metrics is conditional:

  * The `client_addr` metrics label starting with `alloydb_omni_database_postgresql_insights` is present only when you set `google_insights.track_client_address` to `on` in your database cluster parameters.

  * Metrics starting with `alloydb_omni_database_postgresql_insights_pertag` are enabled only if the following conditions are met:

    * You set `google_insights.track_comment` to `on` in your database cluster parameters.
    * You [add tags to your SQL queries](https://docs.cloud.google.com/alloydb/docs/using-query-insights#adding-tags-to-sql-queries).

Name | Description | Label | Unit | Type  
---|---|---|---|---  
alloydb_omni_database_postgresql_backends_for_top_databases | The current number of connections per database. |  |  | gauge  
alloydb_omni_database_postgresql_blks_hit_for_top_databases_count_total | Total number of times Postgres found the requested block in the buffer cache per database. |  |  | counter  
alloydb_omni_database_postgresql_blks_read_for_top_databases_count_total | Total number of blocks read by Postgres that were not in the Postgres buffer cache per database. |  |  | counter  
alloydb_omni_database_postgresql_committed_transactions_for_top_databases_count_total | Total number of transactions committed per database. |  |  | counter  
alloydb_omni_database_postgresql_deadlock_for_top_databases_count_total | The number of deadlocks per database. |  |  | counter  
alloydb_omni_database_postgresql_insights_aggregate_execution_time_us_total | Accumulated query execution time per user per database. This is the sum of CPU time, I/O wait time, lock wait time, process context switch, and scheduling for all of the processes involved in the query execution. | 

  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.

| us | counter  
alloydb_omni_database_postgresql_insights_aggregate_io_time_us_total | Accumulated I/O time per user per database. | 

  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `io_type`: `read` or `write`

| us | counter  
alloydb_omni_database_postgresql_insights_aggregate_lock_time_us_total | Accumulated lock wait time per user per database. | 

  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `lock_type`: `lw` or `hw` or `buffer_pin`

| us | counter  
alloydb_omni_database_postgresql_insights_aggregate_row_count_total | Total number of rows affected during query execution. | 

  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.

|  | counter  
alloydb_omni_database_postgresql_insights_aggregate_shared_blk_access_count_total | Shared blocks (regular tables & indexed) accessed by statement execution. | 

  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `access_type`: `hit` or `miss`

|  | counter  
alloydb_omni_database_postgresql_insights_perquery_execution_time_us_total | Accumulated execution times per user, per database, per query. This is the sum of CPU time, I/O wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution. | 

  * `querystring`: the normalized query.
  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `query_hash`: a unique hash of the query string.

| us | counter  
alloydb_omni_database_postgresql_insights_perquery_io_time_us_total | Accumulated I/O time per user per database per query. | 

  * `querystring`: the normalized query.
  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `io_type`: `read` or `write`
  * `query_hash`: a unique hash of the query string.

| us | counter  
alloydb_omni_database_postgresql_insights_perquery_lock_time_us_total | Accumulated lock wait time per user per database per query. | 

  * `querystring`: the normalized query.
  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `lock_type`: `lw` or `hw` or `buffer_pin`
  * `query_hash`: a unique hash of the query string.

| us | counter  
alloydb_omni_database_postgresql_insights_perquery_row_count_total | Total number of rows affected during query execution. | 

  * `querystring`: the normalized query.
  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `query_hash`: a unique hash of the query string.

|  | counter  
alloydb_omni_database_postgresql_insights_perquery_shared_blk_access_count_total | Shared blocks (regular tables & indexed) accessed by statement execution per query. | 

  * `querystring`: the normalized query.
  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `access_type`: `hit` or `miss`
  * `query_hash`: a unique hash of the query string.

|  | counter  
alloydb_omni_database_postgresql_insights_pertag_execution_time_us_total | Accumulated execution times per user, per database, per tag. This is the sum of CPU time, I/O wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution. | 

  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `action`: the name of the action.
  * `application`: the name of the application.
  * `controller`: the name of the controller.
  * `db_driver`: the name of the db_driver.
  * `framework`: the name of the framework.
  * `route`: the name of the route.
  * `tag_hash`: a unique hash of the tag string.

| us | counter  
alloydb_omni_database_postgresql_insights_pertag_io_time_us_total | Accumulated I/O time per user per database per tag. | 

  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `action`: the name of the action.
  * `application`: the name of the application.
  * `controller`: the name of the controller.
  * `db_driver`: the name of the db_driver.
  * `framework`: the name of the framework.
  * `route`: the name of the route.
  * `io_type`: `read` or `write`
  * `tag_hash`: a unique hash of the tag string.

| us | counter  
alloydb_omni_database_postgresql_insights_pertag_lock_time_us_total | Accumulated lock wait time per user per database per tag. | 

  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `action`: the name of the action.
  * `application`: the name of the application.
  * `controller`: the name of the controller.
  * `db_driver`: the name of the db_driver.
  * `framework`: the name of the framework.
  * `route`: the name of the route.
  * `lock_type`: `lw` or `hw` or `buffer_pin`
  * `tag_hash`: a unique hash of the tag string.

| us | counter  
alloydb_omni_database_postgresql_insights_pertag_row_count_total | Total number of rows affected during query execution. | 

  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `action`: the name of the action.
  * `application`: the name of the application.
  * `controller`: the name of the controller.
  * `db_driver`: the name of the db_driver.
  * `framework`: the name of the framework.
  * `route`: the name of the route.
  * `tag_hash`: a unique hash of the tag string.

|  | counter  
alloydb_omni_database_postgresql_insights_pertag_shared_blk_access_count_total | Shared blocks (regular tables & indexed) accessed by statement execution per tag. | 

  * `user`: the user of the database.
  * `client_addr`: the IP address of the database client.
  * `action`: the name of the action.
  * `application`: the name of the application.
  * `controller`: the name of the controller.
  * `db_driver`: the name of the db_driver.
  * `framework`: the name of the framework.
  * `route`: the name of the route.
  * `access_type`: `hit` or `miss`
  * `tag_hash`: a unique hash of the tag string.

|  | counter  
alloydb_omni_database_postgresql_new_connections_for_top_databases_count_total | The number of new connections per database. |  |  | counter  
alloydb_omni_database_postgresql_rolledback_transactions_for_top_databases_count_total | Total number of transactions rolled back per database. |  |  | counter  
alloydb_omni_database_postgresql_size_byte | Size of the database. |  | byte | gauge  
alloydb_omni_database_postgresql_statements_executed_count_total | Total count of statements executed per database. | `operation_type`: name of the operation, one of [SELECT, UPDATE, INSERT, DELETE, MERGE, UTILITY, NOTHING, UNKNOWN] |  | counter  
alloydb_omni_database_postgresql_temp_bytes_written_for_top_databases_count_total | Total amount of data written to temporary files by queries per database. |  | byte | counter  
alloydb_omni_database_postgresql_temp_files_written_for_top_databases_count_total | Total number of temporary files used for writing data while performing internal algorithms per database. |  |  | counter  
alloydb_omni_database_postgresql_tuples | Number of rows in the database. | `state`: one of [live, dead] |  | gauge  
alloydb_omni_database_postgresql_tuples_deleted_for_top_databases_count_total | The total number of rows deleted per database. |  |  | counter  
alloydb_omni_database_postgresql_tuples_fetched_for_top_databases_count_total | The total number of rows fetched per database. |  |  | counter  
alloydb_omni_database_postgresql_tuples_inserted_for_top_databases_count_total | The total number of rows inserted per database. |  |  | counter  
alloydb_omni_database_postgresql_tuples_returned_for_top_databases_count_total | The total number of rows returned per database. |  |  | counter  
alloydb_omni_database_postgresql_tuples_updated_for_top_databases_count_total | The total number of rows updated per database. |  |  | counter  
  
### Metrics collection metrics

These metrics indicate the status of each metric collection cycle. They have the resource labels mentioned in Labels.

Name | Description | Unit | Type  
---|---|---|---  
alloydb_omni_monitor_collect_ms |  Number of milliseconds spent to collect metrics. |  ms |  gauge  
alloydb_omni_monitor_error_count |  Number of errors encountered while trying to collect metrics this cycle. |  |  gauge  
alloydb_omni_monitor_metric_count |  Number of metrics collected successfully this cycle. |  |  gauge  
  
## Prometheus metric handler metrics

These metrics are automatically generated by Prometheus for each collection cycle.

Name | Description | Cause | Type  
---|---|---|---  
promhttp_metric_handler_errors_total | Total number of internal errors encountered by the promhttp metric handler. | Cause of the error | counter  
  
## What's next

  * To learn how to use metrics for monitoring, see [Monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/manage#monitor).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
