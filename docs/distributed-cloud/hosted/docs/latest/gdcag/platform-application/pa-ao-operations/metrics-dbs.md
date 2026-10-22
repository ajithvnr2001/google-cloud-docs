---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-dbs/
title: Database Service (DBS) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:56.693062+00:00
---

# Database Service (DBS)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-dbs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Database Service (DBS) Stay organized with collections  Save and categorize content based on your preferences. 

Name and description | Type | Emit duration | Labels  
---|---|---|---  
`dbs_container_cpu_request_milli`  
CPU request in millicores. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_container_cpu_usage_time_ms`  
Cumulative CPU usage on all cores used by the container in milliseconds. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_container_cpu_usage_time_seconds`  
Cumulative CPU usage on all cores used by the container in seconds. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_container_database_disk_read_ops_count`  
Cumulative number of read operations from the database disk. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_container_database_disk_write_ops_count`  
Cumulative number of write operations from the database disk. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_container_memory_cache_used_bytes`  
Cache memory usage in bytes. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_container_memory_limit_bytes`  
Maximum memory size in bytes. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_container_memory_usage_bytes`  
Memory usage in bytes of different types.  
  
It has two memory types:  
  
memory_type="evictable"  
memory_type="non-evictable" | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_container_memory_used_bytes`  
Memory usage in bytes. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_container_network_traffic_bytes_total`  
Network traffic in terms of ingress bytes (bytes received) and egress bytes (bytes sent) to and from the DB, respectively.  
  
It has two traffic types:  
  
Traffic="egress"  
Traffic="ingress" | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_dbcluster_mps_status`  
Show a DBCluster MetricsProxySidecar (MPS) status. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_pod_volume_files_breakdown_bytes`  
Number of disk bytes used by the pod volume break down by types of files.  
  
It has different file types:  
  
file_type="Archived_logs", volume_name="ObsDisk"  
file_type="Audit_logs", volume_name="ObsDisk"  
file_type="Data", volume_name="DataDisk"  
file_type="Diagnose_logs", volume_name="ObsDisk"  
file_type="Other", volume_name="DataDisk"  
file_type="Other", volume_name="ObsDisk"  
file_type="Tmp_data", volume_name="DataDisk"  
file_type="Wal", volume_name="DataDisk" | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_pod_volume_total_bytes`  
Total number of disk bytes available to the pod volume.  
  
It tracks different volumes:  
  
volume_name="DataDisk"  
volume_name="ObsDisk" | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_pod_volume_used_bytes`  
Number of disk bytes used by the pod volume.  
  
It tracks different volumes:  
  
volume_name="DataDisk"  
volume_name="ObsDisk" | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_system_monitor_collect_ms`  
Number of milliseconds spent to collect metrics. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_system_monitor_error_count`  
Number of errors encountered while trying to collect metrics this cycle. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_system_monitor_metric_count`  
Number of metrics collected successfully from config this cycle. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_pitr_collect_ms`  
Number of milliseconds spent to collect metrics. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_pitr_error_count`  
Number of errors encountered while trying to collect metrics this cycle. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_pitr_metric_count`  
Number of metrics collected successfully from config this cycle. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_pitr_wal_age`  
Age of the oldest Write-Ahead log segment. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_pitr_wal_size`  
Size of unarchived PostgreSQL Write-Ahead logs. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`promhttp_metric_handler_errors_total`  
Total number of internal errors encountered by the promhttp metric handler. | Counter | 1 m | 

  * **namespace_name:** shadow namespace name

  
`db_monitor_collect_ms`  
Number of milliseconds spent to collect metrics. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`db_monitor_error_count`  
Number of errors encountered while trying to collect metrics this cycle. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`db_monitor_metric_count`  
Number of metrics collected successfully from config this cycle. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_database_connections`  
Number of connections to the database. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_database_max_connections`  
Max number of connections configured to the database. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`dbs_database_uptime`  
Number of seconds since the database started.  
  
It tracks different databases:  
  
database="cloudsqladmin"  
database="postgres"  
database="template0"  
database="template1" | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_backends_application_num_backends`  
Number of connections to the database. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_backends_database_count`  
Number of connections to the database. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_backends_wait_count`  
Number of wait events. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_locks_count`  
Number of locks.  
  
It tracks different locks:  
  
mode="accessexclusivelock"  
mode="accesssharelock"  
mode="exclusivelock"  
mode="rowexclusivelock"  
mode="rowsharelock"  
mode="sharelock"  
mode="sharerowexclusivelock"  
mode="shareupdateexclusivelock"  
mode="sireadlock" | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_activity_count`  
Number of connections in this state.  
  
It tracks different states:  
  
state="active"  
state="disabled"  
state="fastpath function call"  
state="idle"  
state="idle in transaction"  
state="idle in transaction (aborted)" | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_activity_max_tx_duration`  
Max duration in seconds any active transaction has been running.  
  
It tracks different states:  
  
state="active"  
state="disabled"  
state="fastpath function call"  
state="idle"  
state="idle in transaction"  
state="idle in transaction (aborted)" | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_archiver_archived_count`  
Number of WAL files that have been successfully archived. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_archiver_failed_count`  
Number of failed attempts for archiving WAL files. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_archiver_last_archive_age`  
Time in seconds since last WAL segment was successfully archived. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_bgwriter_buffers_alloc`  
Number of buffers allocated. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_bgwriter_buffers_backend`  
Number of buffers written directly by a backend. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_bgwriter_buffers_backend_fsync`  
Number of times a backend had to execute its own fsync call (normally the background writer handles those even when the backend does its own write). | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_bgwriter_buffers_checkpoint`  
Number of buffers written during checkpoints. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_bgwriter_buffers_clean`  
Number of buffers written by the background writer. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_bgwriter_checkpoint_sync_time`  
Total amount of time that has been spent in the portion of checkpoint processing where files are synchronized to disk, in milliseconds. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_bgwriter_checkpoint_write_time`  
Total amount of time that has been spent in the portion of checkpoint processing where files are written to disk, in milliseconds. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_bgwriter_checkpoints_req`  
Number of requested checkpoints that have been performed. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_bgwriter_maxwritten_clean`  
Number of times the background writer stopped a cleaning scan because it had written too many buffers. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_bgwriter_stats_reset`  
Time at which these statistics were last reset. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_blk_read_time`  
Time spent reading data file blocks by backends in this database, in milliseconds. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_blk_write_time`  
Time spent writing data file blocks by backends in this database, in milliseconds. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_blks_hit`  
Number of times disk blocks were found already in the buffer cache, so that a read was not necessary (this only includes hits in the PostgreSQL buffer cache, not the operating system's file system cache). | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_blks_read`  
Number of disk blocks read in this database. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_conflicts`  
Number of queries canceled due to conflicts with recovery in this database. Conflicts occur only on standby servers. See `pg_stat_database_conflicts` for details. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_conflicts_confl_bufferpin`  
Number of queries in this database that have been canceled due to pinned buffers. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_conflicts_confl_deadlock`  
Number of queries in this database that have been canceled due to deadlocks. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_conflicts_confl_lock`  
Number of queries in this database that have been canceled due to lock timeouts. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_conflicts_confl_snapshot`  
Number of queries in this database that have been canceled due to old snapshots. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_conflicts_confl_tablespace`  
Number of queries in this database that have been canceled due to dropped tablespaces. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_deadlocks`  
Number of deadlocks detected in this database. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_numbackends`  
Number of backends connected to this database. This is the only column in this view that returns a value reflecting current state; all other columns return the accumulated values since the last reset. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_stats_reset`  
Time at which these statistics were last reset. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_temp_bytes`  
Total amount of data written to temporary files by queries in this database. All temporary files are counted, regardless of why the temporary file was created, and regardless of the log_temp_files setting. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_temp_files`  
Number of temporary files created by queries in this database. All temporary files are counted, regardless of why the temporary file was created (for example, sorting or hashing), and regardless of the log_temp_files setting. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_tup_deleted`  
Number of rows deleted by queries in this database. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_tup_fetched`  
Number of rows fetched by queries in this database. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_tup_inserted`  
Number of rows inserted by queries in this database. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_tup_returned`  
Number of rows returned by queries in this database. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_tup_updated`  
Number of rows updated by queries in this database. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_xact_commit`  
Number of transactions in this database that have been committed. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_stat_database_xact_rollback`  
Number of transactions in this database that have been rolled back. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_transaction_id_assigned_total`  
Number of transaction ids assigned and consumed by the dbcluster. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_transaction_id_frozen_total`  
Number of transaction IDs replenished by the VACUUM's freeze operation. | Counter | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_transaction_id_utilization`  
The fraction of unvacuumed transactions relative to the Postgres 2-billion maximum. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_vacuum_oldest_transactions_count_prepared`  
Oldest prepared transaction age, measured in number of transactions that have happened since the oldest transaction. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_vacuum_oldest_transactions_count_replica`  
Oldest transaction age on the standby instance, measured in number of transactions that have happened since the oldest transaction. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_vacuum_oldest_transactions_count_replication_slot`  
Oldest transaction age that this slot needs the database to retain, measured in number of transactions that have happened since the oldest transaction. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
`pg_vacuum_oldest_transactions_count_running`  
Oldest running transaction age, measured in number of transactions that have happened since the oldest transaction. | Gauge | 1 m | 

  * **dbcluster:** the name of the DBCluster
  * **engine_type:** PostgreSQL/AlloyDBOmni

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
