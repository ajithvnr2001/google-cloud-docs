---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics/
title: Cloud SQL metrics \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:52:08.513342+00:00
---

# Cloud SQL metrics  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  Cloud SQL metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page shows reference information for Cloud SQL metrics. You access these metrics through Google Cloud Observability.

To quickly see graphs of metric data, use the Metrics Explorer. For information on using this tool, see [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

Note: This page lists metrics for all database engines that Cloud SQL supports. The database path indicates, where applicable, if a metric is specific to a database engine.

The "metric type" strings in this table must be prefixed with `cloudsql.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`client/connector/closed_connection_count` BETA ** _(project)_**   
Connectors Closed Connections   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql.googleapis.com/InstanceClient](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql.googleapis.com/InstanceClient)** |  _The total number of closed connections to Cloud SQL instances._   
`instance_auth_type`: Authentication type used, one of [built_in, iam].   
`instance_ip_type`: IP address type of the connection, one of [public, psa, psc].   
`status`: Close connections status [success, error].   
`client/connector/connect_latencies` BETA ** _(project)_**   
Connectors Connect Latencies   
`CUMULATIVE`, `DISTRIBUTION`, `ms`   
**[cloudsql.googleapis.com/InstanceClient](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql.googleapis.com/InstanceClient)** |  _Distribution of the Cloud SQL connector connect latencies._   
`instance_auth_type`: Authentication type used, one of [built_in, iam].   
`instance_ip_type`: IP address type of the connection, one of [public, psa, psc].   
`client/connector/connection_durations` BETA ** _(project)_**   
Connectors Connection Duration   
`CUMULATIVE`, `DISTRIBUTION`, `s`   
**[cloudsql.googleapis.com/InstanceClient](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql.googleapis.com/InstanceClient)** |  _Distribution of connection duration in seconds between connection open and close._   
`instance_auth_type`: Authentication type used, one of [built_in, iam].   
`instance_ip_type`: IP address type of the connection, one of [public, psa, psc].   
`client/connector/open_connection_count` BETA ** _(project)_**   
Connectors Connection Attempt Count   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql.googleapis.com/InstanceClient](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql.googleapis.com/InstanceClient)** |  _Total count of connection attempts made by the connector._   
`instance_auth_type`: Authentication type used, one of [built_in, iam].   
`instance_ip_type`: IP address type of the connection, one of [public, psa, psc].   
`connection_part`: If status is not success, which part of the connection errors out, one of [client_to_proxy, proxy_to_server].   
`status`: Status of the dial attempt, one of [success, user_error, cache_error, tcp_error, tls_error, auth_error, refresh_failed_error, refresh_expired_error, dns_lookup_error, unkown_error].   
`client/connector/open_connections` BETA ** _(project)_**   
Connectors Open Connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql.googleapis.com/InstanceClient](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql.googleapis.com/InstanceClient)** |  _Number of currently open connections per language connector client instance._   
`instance_auth_type`: Authentication type used, one of [built_in, iam].   
`instance_ip_type`: IP address type of the connection, one of [public, psa, psc].   
`database/active_directory/domain_reachable` GA ** _(project)_**   
Active Directory domain reachable   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the instance is able to ping a domain controller from the connected Managed Active Directory domain. If false, Windows Authentication may not work as expected. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/active_directory/instance_available` GA ** _(project)_**   
Windows Authentication available   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the instance is currently available using Windows Authentication. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/auto_failover_request_count` GA ** _(project)_**   
Auto-failover Requests   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta of number of instance auto-failover requests. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/available_for_failover` GA ** _(project)_**   
Available for failover   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _This is > 0 if the failover operation is available on the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/cpu/reserved_cores` GA ** _(project)_**   
CPU reserved cores   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of cores reserved for the database. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/cpu/usage_time` GA ** _(project)_**   
CPU usage   
`DELTA`, `DOUBLE`, `s{CPU}`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Cumulative CPU usage time in seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/cpu/utilization` GA ** _(project)_**   
CPU utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current CPU utilization represented as a percentage of the reserved CPU that is currently in use. Values are typically numbers between 0.0 and 1.0 (but might exceed 1.0). Charts display the values as a percentage between 0% and 100% (or more). Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/data_cache/bytes_used` GA ** _(project)_**   
Data cache used   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Data cache usage in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/data_cache/quota` GA ** _(project)_**   
Data cache quota   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Maximum data cache size in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/bytes_used` GA ** _(project)_**   
Bytes used   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Data utilization in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/bytes_used_by_data_type` GA ** _(project)_**   
Bytes used   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Data utilization in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`data_type`: A breakdown of instance disk usage per data_type, for example, 'data', 'tmp_data' or 'slow_log'.   
`database/disk/provisioning/iops` GA ** _(project)_**   
Provisioned IOPS   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Provisioned IOPS for the data disk. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/provisioning/throughput` GA ** _(project)_**   
Provisioned throughput   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Provisioned throughput for the data disk. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`io_type`: Direction of the throughput.   
`database/disk/quota` GA ** _(project)_**   
Disk quota   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Maximum data disk size in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/read_bytes_count` GA ** _(project)_**   
Disk read bytes   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk read IO bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/read_ops_count` GA ** _(project)_**   
Disk read IO   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk read IO operations. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/utilization` GA ** _(project)_**   
Disk utilization   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The fraction of the disk quota that is currently in use. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/write_bytes_count` GA ** _(project)_**   
Disk write bytes   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk write IO bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/disk/write_ops_count` GA ** _(project)_**   
Disk write IO   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk write IO operations. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/instance_state` GA ** _(project)_**   
Instance state   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The current serving state of the Cloud SQL instance. Because there are seven possible states, seven data points are returned. Each of them has a different field value representing each state. Only the one that matches the current state of the instance is TRUE. All the others are FALSE. The state can be one of the following: RUNNING: The instance is running, or is ready to run when accessed. SUSPENDED: The instance is not available, for example due to problems with billing. RUNNABLE: The instance has been stopped by owner. It is not currently running, but it's ready to be restarted. PENDING_CREATE: The instance is being created. MAINTENANCE: The instance is down for maintenance. FAILED: The instance creation failed. UNKNOWN_STATE: The state of the instance is unknown. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: The state of the instance.   
`database/memory/components` BETA ** _(project)_**   
Memory components   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Memory stats components in percentage as usage, cache and free memory for the database. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`component`: Name of the component, one of [usage, cache and free].   
`database/memory/quota` GA ** _(project)_**   
Memory quota   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Maximum RAM size in bytes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/memory/total_usage` GA ** _(project)_**   
Total memory usage   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total RAM usage in bytes. This metric reports the RAM usage of the database process, including the buffer/cache. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/memory/usage` GA ** _(project)_**   
Memory usage   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _RAM usage in bytes. This metric reports the RAM usage of the server, excluding the buffer/cache. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/memory/utilization` GA ** _(project)_**   
Memory utilization   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The fraction of the memory quota that is currently in use. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/aborted_clients_count` GA ** _(project)_**   
MySQL Aborted Clients Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Connections that were aborted because the client died without closing the connection properly, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/aborted_connects_count` GA ** _(project)_**   
MySQL Aborted Connects Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Failed attempts to connect to the MySQL server, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/conn_pool/avg_wait_time` GA ** _(project)_**   
MySQL Connection Pool Average Wait Time   
`GAUGE`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Average time spent by the connection on the work queue in milliseconds. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/conn_pool/pending_connections` GA ** _(project)_**   
MySQL Connection Pool Pending Connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections presently enqueued in the work queue. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/conn_pool/threads` GA ** _(project)_**   
MySQL Connection Pool Threads   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of threads in the connection pool. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`status`: Status of the connection pool threads e.g. 'active' or 'idle'.   
`database/mysql/connections_count` GA ** _(project)_**   
MySQL Connections Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Connection attempts (successful or not) to the MySQL server, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/ddl_operations_count` GA ** _(project)_**   
MySQL DDL Operations Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _MySQL DDL operations, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of DDL operations, one of [create_table, drop_table, alter_table, rename_table, truncate_table].   
`database/mysql/dml_operations_count` GA ** _(project)_**   
MySQL DML Operations Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _MySQL DML operations, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of DML operations, one of [insert, insert_select, update, delete, replace, replace_select].   
`database/mysql/external_sync/replica_lag` GA ** _(project)_**   
Replica lag   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _An approximation of the lag (seconds behind primary) between the Cloud SQL MySQL external replica and its primary. Only applicable to Cloud SQL MySQL external replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`channel_name`: Name of the channel on which the replica is connected to the external server.   
`database/mysql/handler_operations_count` GA ** _(project)_**   
MySQL Handler Operations Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _MySQL handler operations, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of operation handler type, one of [delete, read_first, read_key, read_last, read_next, read_prev, read_rnd, read_rnd_next, update, write].   
`database/mysql/innodb/active_transactions` GA ** _(project)_**   
InnoDB Active Transactions   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of active Transaction details(trx which are in progress), Values in bracket are meant for innodb_transaction_state (Total/running/lock_wait/rolling_back/committing). Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: Values in bracket are meant for innodb_transaction_state, one of [Total, running, lock_wait, rolling_back, committing].   
`database/mysql/innodb/active_trx_longest_time` GA ** _(project)_**   
InnoDB Active TRX Longest Time   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Largest transaction time from currently active innodb transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/active_trx_rows_locked` GA ** _(project)_**   
InnoDB Active TRX Rows Locked   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of rows locked by currently active innodb transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/active_trx_rows_modified` GA ** _(project)_**   
InnoDB Active TRX Rows Modified   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of rows modified by currently active innodb transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/active_trx_total_time` GA ** _(project)_**   
InnoDB Active TRX Total Time   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Duration of currently active innodb transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/adaptive_hash_operation_count` GA ** _(project)_**   
Innodb AHI operations   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total internal row operations (rows added, updated, removed) performed to maintain the AHI since last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: AHI operation type.   
`database/mysql/innodb/ahi_search_count` GA ** _(project)_**   
AHI or Btree searches   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total search operations on the InnoDB AHI and its efficiency since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Operation type.   
`database/mysql/innodb/buffer_flush_sync_waits_count` GA ** _(project)_**   
Innodb sync flushing waits   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of times InnoDB has performed synchronous buffer flush operations and blocking the user transactions since last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/buffer_pool_pages` GA ** _(project)_**   
InnoDB Buffer Pool Pages   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of InnoDB buffer pool pages, innodb_page_type field stores count of InnoDB pages in each state. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`innodb_page_type`: Kind of InnoDB page, one of [dirty, free, Total]   
`database/mysql/innodb/buffer_pool_read_requests_count` GA ** _(project)_**   
Innodb Buffer Pool Read Requests Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Logical read requests from InnoDB buffer pool, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/buffer_pool_reads_count` GA ** _(project)_**   
Innodb Buffer Pool Reads Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Logical reads that InnoDB could not satisfy from the buffer pool, and had to read directly from disk, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/buffer_pool_write_requests_count` GA ** _(project)_**   
InnoDB Buffer Pool Write Requests Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Writes done to the InnoDB buffer pool, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_cache/cache_hit_count` GA ** _(project)_**   
MySQL data cache hit count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache hit read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_cache/cache_miss_count` GA ** _(project)_**   
MySQL data cache miss count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache miss read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_cache/pages` GA ** _(project)_**   
Innodb Pages in Data Cache   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of Innodb pages in Mysqls E+ Data cache feature. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`page_type`: Page types in data cache.   
`database/mysql/innodb/data_fsyncs_count` GA ** _(project)_**   
Innodb Data Fsyncs Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _InnoDB fsync() calls, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_pending_fsyncs` GA ** _(project)_**   
InnoDB Data Pending Fsyncs   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of pending fsync() operations in the MySQL server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_pending_reads` GA ** _(project)_**   
InnoDB Data Pending Reads   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of pending reads in the MySQL Server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/data_pending_writes` GA ** _(project)_**   
InnoDB Data Pending Writes   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of pending writes in the MySQL Server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/deadlocks_count` GA ** _(project)_**   
InnoDB Deadlocks Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Deadlocks, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/dictionary_memory` GA ** _(project)_**   
MySQL InnoDB dictionary cache   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Memory allocated for InnoDB dictionary cache. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/history_list_length` GA ** _(project)_**   
InnoDB History List Length   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates the size of undo logs which are used to store modifications made to older versions of rows. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/ibuf_merge_operation_count` GA ** _(project)_**   
InnoDB merged records operation wise   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of records type merged by the change buffering operation since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of merge operation. One of ibuf_merges_insert,ibuf_merges_delete_mark,ibuf_merges_delete.   
`database/mysql/innodb/ibuf_merges_count` GA ** _(project)_**   
InnoDB change buffer merges.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of change buffer merges since the last sample. This shows the efficiency of all change buffer operations. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/innodb_log_waits_count` GA ** _(project)_**   
Transaction waits for Innodb logbuffer flush   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of transactions wait for space to become available in the InnoDB log buffer, to help tune innodb_log_buffer_size configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/lock_timeout_count` GA ** _(project)_**   
Innodb Row Lock Wait Timeout Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Row lock wait timeouts, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/lsn` GA ** _(project)_**   
InnoDB LSN   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Value of Innodb current/flushed/last_checkpoint log sequence number. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`lsn_type`: Type of LSN being reported out of current/flushed/last_checkpoint.   
`database/mysql/innodb/operation_disk_io_count` GA ** _(project)_**   
Disk IO performed by InnoDB.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Disk IO operations performed by InnoDB since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of Disk IO operation. One of innodb_data_reads, innodb_data_writes, innodb_log_writes, innodb_dblwr_writes.   
`database/mysql/innodb/os_log_fsyncs_count` GA ** _(project)_**   
Innodb OS Log Fsyncs Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _InnoDB fsync() calls to the log file, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/os_log_pending_fsyncs` GA ** _(project)_**   
InnoDB OS Log Pending Fsyncs   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of pending fsync() operations for the InnoDB redo log files in the MySQL server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/os_log_pending_writes` GA ** _(project)_**   
InnoDB OS Log Pending Writes   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of pending writes to the InnoDB redo log files in the MySQL server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/pages_read_count` GA ** _(project)_**   
Innodb Pages Read Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _InnoDB pages read, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/pages_written_count` GA ** _(project)_**   
Innodb Pages Written Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _DInnoDB pages written, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/row_lock_time` GA ** _(project)_**   
InnoDB Row Lock Time   
`GAUGE`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The total time spent in acquiring row locks for InnoDB tables. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/row_lock_waits_count` GA ** _(project)_**   
InnoDB Row Lock Waits Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Times operations on InnoDB tables had to wait for a row lock, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb/row_operations_count` GA ** _(project)_**   
InnoDB Row Operations Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _InnoDB row operations, operation_type field stores the count of InnoDB row operations, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Kind of InnoDB row operations, one of [delete, insert, read, update]   
`database/mysql/innodb_buffer_pool_pages_dirty` GA ** _(project)_**   
InnoDB dirty pages   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of unflushed pages in the InnoDB buffer pool. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_buffer_pool_pages_free` GA ** _(project)_**   
InnoDB free pages   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of unused pages in the InnoDB buffer pool. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_buffer_pool_pages_total` GA ** _(project)_**   
InnoDB total pages   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of pages in the InnoDB buffer pool. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_data_fsyncs` GA ** _(project)_**   
InnoDB fsync calls   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of InnoDB fsync() calls. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_os_log_fsyncs` GA ** _(project)_**   
InnoDB log fsync calls   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of InnoDB fsync() calls to the log file. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_pages_read` GA ** _(project)_**   
InnoDB pages read   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of InnoDB pages read. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/innodb_pages_written` GA ** _(project)_**   
InnoDB pages written   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of InnoDB pages written. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/max_connections` GA ** _(project)_**   
MySQL Max Connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Value of the MySQL max_connections configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/memory/by_code_area` GA ** _(project)_**   
Memory allocated by code area   
`GAUGE`, `DOUBLE`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Memory allocated to each code area, reported by mysql performance_schema. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`code_area_group`: Kind of Mysql code area, one of [innodb_engine,sql,performance_schema,temptable_engine,memory_engine,mysys]   
`database/mysql/memory/by_event` GA ** _(project)_**   
Memory allocated by events   
`GAUGE`, `DOUBLE`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Memory allocated by each event, reported by performance_schema. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`event_type`: Kind of Mysql event, one of [innodb_hash0hash,innodb_memory,innodb_row0sel,sql_table,sql_thd_main,sql_dd,sql_string,mysys_iocache]   
`database/mysql/memory/global` GA ** _(project)_**   
Global memory allocated   
`GAUGE`, `DOUBLE`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The total allocated memory, reported by performance_schema. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/open_table_definitions` GA ** _(project)_**   
MySQL open table definitions   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of table definitions that are currently cached. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/open_tables` GA ** _(project)_**   
MySQL open tables   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of tables that are currently open. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/opened_table_count` GA ** _(project)_**   
MySQL opened table count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of tables that have been opened since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/opened_table_definitions_count` GA ** _(project)_**   
MySQL opened table definitions count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of table definitions that have been cached since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/queries` GA ** _(project)_**   
Queries   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of statements executed by the server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/questions` GA ** _(project)_**   
Questions   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of statements executed by the server sent by the client. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/received_bytes_count` GA ** _(project)_**   
Network bytes received by MySQL   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of bytes received by MySQL process. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/available_for_failover` DEPRECATED ** _(project)_**   
Available for failover (Deprecated)   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _This is > 0 if the failover operation is available on the master instance.master. The metric is deprecated. Please use cloudsql.googleapis.com/database/available_for_failover instead. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/last_io_errno` GA ** _(project)_**   
Last I/O thread error number.   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The error number of the most recent error that caused the I/O thread to stop. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/last_sql_errno` GA ** _(project)_**   
Last SQL thread error number.   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The error number of the most recent error that caused the SQL thread to stop. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/seconds_behind_master` GA ** _(project)_**   
Replication lag   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of seconds the read replica is behind its primary (approximation). A negative value indicates that replication is inactive. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/slave_io_running` GA ** _(project)_**   
Slave I/O thread running   
`GAUGE`, `STRING`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the I/O thread for reading the primary's binary log is running. Possible values are Yes, No and Connecting. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/slave_io_running_state` GA ** _(project)_**   
Slave I/O thread running state   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the I/O thread for reading the primary's binary log is running. Possible values are Yes, No and Connecting, and the values are exposed through the 'state' field. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: The slave_io_running state of the slave.   
`database/mysql/replication/slave_sql_running` GA ** _(project)_**   
Slave SQL thread running   
`GAUGE`, `STRING`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the SQL thread for executing events in the relay log is running. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/replication/slave_sql_running_state` GA ** _(project)_**   
Slave SQL thread running state   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates whether the SQL thread for executing events in the relay log is running. Possible values are Yes / No, and the values are exposed through the 'state' field. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: The slave_sql_running state of the slave.   
`database/mysql/sent_bytes_count` GA ** _(project)_**   
Network bytes sent by MySQL   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of bytes sent by MySQL process. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/slow_queries_count` GA ** _(project)_**   
MySQL slow queries count.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The total number of queries that took longer than long_query_time seconds. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/thread_cache_size` GA ** _(project)_**   
MySQL Thread Cache Size   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Value of the MySQL thread_cache_size configuration. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/thread_state` GA ** _(project)_**   
MySQL threads state   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The state of running threads by querying information_schema.processlist table, this information helps to understand the locking or contention issues. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: Thread state.   
`database/mysql/threads` GA ** _(project)_**   
MySQL Thread   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of Threads. threads_cached indicates threads in the thread cache, threads_connected indicates currently open connections, threads_running indicates threads that are not sleeping. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`thread_kind`: Kind of the threads counted (threads_cached, threads_connected, threads_running).   
`database/mysql/threads_created_count` GA ** _(project)_**   
MySQL Threads Created Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Threads created to handle connections, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/tmp_disk_tables_created_count` GA ** _(project)_**   
MySQL Temporary Disk Tables Created Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Internal on-disk temporary tables created by the MySQL server while executing statements, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/tmp_files_created_count` GA ** _(project)_**   
MySQL Temporary Files Created Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Temporary files created by the MySQL server, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/mysql/tmp_tables_created_count` GA ** _(project)_**   
MySQL Temporary Tables Created Count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _MySQL temporary tables created, since the last sample. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/network/connection_attempt_count` GA ** _(project)_**   
Cloud SQL Connection Attempts   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of connection attempts to the Cloud SQL instance, with information about anomaly detection. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`login_status`: Login status, one of [succeeded, failed].   
`anomaly_detected`: Connection related anomaly, for example, "no anomaly detected", "brute-force login".   
`anomalous_connection_throttled`: (BOOL) Whether the connection is throttled if it's anomalous.   
`database/network/connections` GA ** _(project)_**   
Cloud SQL Connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections to databases on the Cloud SQL instance. Only applicable to MySQL and SQL Server. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/network/received_bytes_count` GA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of bytes received through the network. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/network/sent_bytes_count` GA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of bytes sent through the network. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`destination`: Deprecated and not populated.   
`database/postgresql/backends_in_wait` GA ** _(project)_**   
PostgreSQL backends in wait   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of backends in wait in postgres instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`backend_type`: Type of the backend, one of [autovacuum launcher, autovacuum worker, logical replication launcher, logical replication worker, parallel worker, background writer, client backend, checkpointer, archiver, startup, walreceiver, walsender, walwriter].   
`wait_event`: Name of the wait event, such as AutoVacuumMain, ClientRead.   
`wait_event_type`: Type of wait event, one of [Activity, BufferPin, Extension, IO, IPC, Lock, LWLock, Timeout].   
`database/postgresql/blocks_read_count` GA ** _(project)_**   
Number of disk blocks read.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of disk blocks read by this database. The source field distingushes actual reads from disk versus reads from buffer cache. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`source`: Type of data block, one of [disk, buffer_cache].   
`database/postgresql/checkpoint_count` GA ** _(project)_**   
Checkpoint count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total checkpoints occurred. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`checkpoint_type`: Type of checkpoint, can be one of [scheduled, requested].   
`database/postgresql/data_cache/hit_count` GA ** _(project)_**   
PostgreSQL data cache hit count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache hit read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/data_cache/hit_ratio` GA ** _(project)_**   
PostgreSQL data cache hit ratio   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Ratio of data cache hit read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/data_cache/miss_count` GA ** _(project)_**   
PostgreSQL data cache miss count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache miss read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/deadlock_count` GA ** _(project)_**   
Deadlocks count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of deadlocks detected for this database. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/disk/read_bytes_count` GA ** _(project)_**   
Bytes read by PostgreSQL   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta number of bytes read by PostgreSQL. Only available for PostgreSQL 16 and higher. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`backend_type`: Type of backend.   
`object`: Target object of the read operation.   
`context`: The context of the read operation.   
`database/postgresql/disk/write_bytes_count` GA ** _(project)_**   
Bytes written by PostgreSQL   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta number of bytes written by PostgreSQL. Only available for PostgreSQL 16 and higher. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`backend_type`: Type of backend.   
`object`: Target object of the write operation.   
`context`: The context of the write operation.   
`database/postgresql/external_sync/initial_sync_complete` ALPHA ** _(project)_**   
Initial sync complete   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Whether all databases on the Postgres External Server (ES) replica have completed the initial sync and are replicating changes from the source. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/external_sync/max_replica_byte_lag` ALPHA ** _(project)_**   
Max lag bytes   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Replication lag in bytes for Postgres External Server (ES) replicas. Aggregated across all DBs on the replica. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/insights/aggregate/execution_time` GA ** _(project)_**   
Execution time   
`CUMULATIVE`, `INT64`, `us{CPU}`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated query execution time per user per database. This is the sum of cpu time, io wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`database/postgresql/insights/aggregate/io_time` GA ** _(project)_**   
IO time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated IO time per user per database._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`io_type`: The IO type (read/write).   
`database/postgresql/insights/aggregate/latencies` GA ** _(project)_**   
Latency   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Query latency distribution per user per database._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`database/postgresql/insights/aggregate/lock_time` GA ** _(project)_**   
Aggregated lock time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated lock wait time per user per database._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`lock_type`: The lock type (lw/hw/buffer_pin).   
`database/postgresql/insights/aggregate/row_count` GA ** _(project)_**   
Affected rows   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of rows affected during query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`database/postgresql/insights/aggregate/shared_blk_access_count` GA ** _(project)_**   
Shared blocks cache access.   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Shared blocks (regular tables & indexed) accessed by statement execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`access_type`: The block access type (hit/miss).   
`database/postgresql/insights/perquery/execution_time` GA ** _(project)_**   
Per query execution times   
`CUMULATIVE`, `INT64`, `us{CPU}`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated execution times per user per database per query.This is the sum of cpu time, io wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/io_time` GA ** _(project)_**   
Per query IO time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated IO time per user per database per query._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`io_type`: The IO type (read/write).   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/latencies` GA ** _(project)_**   
Per query latency   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Query latency distribution per user per database per query._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/lock_time` GA ** _(project)_**   
Per query lock time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated lock wait time per user per database per query._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`lock_type`: The lock type (lw/hw/buffer_pin).   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/row_count` GA ** _(project)_**   
Per query affected rows   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of rows affected during query execution._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/perquery/shared_blk_access_count` GA ** _(project)_**   
Per query Shared blocks cache access   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Shared blocks (regular tables & indexed) accesssed by statement execution._   
`querystring`: The normalized query.   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`access_type`: The block access type (hit/miss).   
`query_hash`: A unique hash of the query string.   
`database/postgresql/insights/pertag/execution_time` GA ** _(project)_**   
Per tag execution time   
`CUMULATIVE`, `INT64`, `us{CPU}`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated execution times per user per database per tag.This is the sum of cpu time, io wait time, lock wait time, process context switch, and scheduling for all the processes involved in the query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/io_time` GA ** _(project)_**   
Per tag IO time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated IO write time per user per database per tag._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`io_type`: The IO type (read/write).   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/latencies` GA ** _(project)_**   
Per tag latency   
`CUMULATIVE`, `DISTRIBUTION`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Query latency distribution per user per database per tag._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/lock_time` GA ** _(project)_**   
Per tag lock time   
`CUMULATIVE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Accumulated lock wait time per user per database per tag._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`lock_type`: The lock type (lw/hw/buffer_pin).   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/row_count` GA ** _(project)_**   
Per tag affected rows   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total number of rows affected during query execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/insights/pertag/shared_blk_access_count` GA ** _(project)_**   
Per tag shared blocks cache accessed   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Shared blocks (regular tables & indexed) accessed by statement execution._   
`user`: The user of the database.   
`client_addr`: The IP address of the database client.   
`action`: The name of the action.   
`application`: The name of the application.   
`controller`: The name of the controller.   
`db_driver`: The name of the db_driver.   
`framework`: The name of the framework.   
`route`: The name of the route.   
`access_type`: The block access type (hit/miss).   
`tag_hash`: A unique hash of the tag string.   
`database/postgresql/new_connection_count` GA ** _(project)_**   
PostgreSQL new connections count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Count of new connections added to the postgres instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database, such as testdb.   
`database/postgresql/num_backends` GA ** _(project)_**   
PostgreSQL Connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections to the Cloud SQL PostgreSQL instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/num_backends_by_application` GA ** _(project)_**   
PostgreSQL connections by application   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections to the Cloud SQL PostgreSQL instance, grouped by applications. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`application`: Name of the application.   
`database/postgresql/num_backends_by_state` GA ** _(project)_**   
PostgreSQL Connections by State   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections to the Cloud SQL PostgreSQL instance, grouped by its state. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`state`: Connection state, one of [idle, active, idle_in_transaction, idle_in_transaction_aborted, disabled or fastpath_function_call].   
`database/postgresql/replication/replica_byte_lag` GA ** _(project)_**   
Lag bytes   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Replication lag in bytes. Reported from the master per replica. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`replica_name`: Name of the replica.   
`replica_lag_type`: Type of lag. This can be either replay_location, flush_location, write_location or sent_location.   
`database/postgresql/statements_executed_count` GA ** _(project)_**   
Statements executed count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total count of statements executed in postgresql instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`operation_type`: Type of the operation performed.   
`database/postgresql/temp_bytes_written_count` GA ** _(project)_**   
Data (in bytes) written to temporary   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total amount of data (in bytes) written to temporary files by the queries per database. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/temp_files_written_count` GA ** _(project)_**   
Temporary files used for writing data   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of temporary files used for writing data while performing algorithms such as join and sort. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/transaction_count` GA ** _(project)_**   
Number of transactions   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of number of transactions. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`transaction_type`: transaction_type can be commit or rollback.   
`database/postgresql/transaction_id_count` GA ** _(project)_**   
Transaction ID count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of transaction ID. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`action`: Type of action, one of ["assigned" - count of transaction IDs assigned and consumed by the instance; "frozen" - count of transaction IDs replenished by the VACUUM`s freeze operation].   
`database/postgresql/transaction_id_utilization` GA ** _(project)_**   
Transaction ID utilization   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current utilization represented as a percentage of transaction IDs consumed by the Cloud SQL PostgreSQL instance. Values are typically numbers between 0.0 and 1.0. Charts display the values as a percentage between 0% and 100%. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/tuple_size` GA ** _(project)_**   
Number of tuples (rows) in the database.   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of tuples (rows) in the database. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`tuple_state`: Type of tuple state, one of [live, dead].   
`database/postgresql/tuples_fetched_count` GA ** _(project)_**   
Number of tuples fetched   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of rows fetched as a result of queries per database in the PostgreSQL instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/tuples_processed_count` GA ** _(project)_**   
Number of rows processed   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of tuples(rows) processed for a given database for operations like insert, update or delete. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation_type`: Type of database operation, one of [insert, update, delete].   
`database`: Name of the database.   
`database/postgresql/tuples_returned_count` GA ** _(project)_**   
Number of tuples returned   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of rows scanned while processing the queries per database in the PostgreSQL instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Name of the database.   
`database/postgresql/vacuum/oldest_transaction_age` GA ** _(project)_**   
Oldest transaction age   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Age of the oldest transaction yet to be vacuumed in the Cloud SQL PostgreSQL instance, measured in number of transactions that have happened since the oldest transaction. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`oldest_transaction_type`: oldest transaction type can be one of [running, prepared, replication_slot, replica].   
`database/postgresql/write_ahead_log/flushed_bytes_count` GA ** _(project)_**   
PostgreSQL WAL flushed bytes count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total size (bytes) of WAL flushed for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/write_ahead_log/inserted_bytes_count` GA ** _(project)_**   
PostgreSQL WAL inserted bytes count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total size (bytes) of WAL inserted for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/write_ahead_log/redo_size` GA ** _(project)_**   
PostgreSQL redo size metric   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The size (bytes) of WAL to redo in case of recovery. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/postgresql/write_ahead_log/written_bytes_count` GA ** _(project)_**   
PostgreSQL WAL written bytes count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total size (bytes) of WAL written for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/readpool/expected_pool_nodes` GA ** _(project)_**   
Expected Read Pool Nodes   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of nodes in the read pool. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/replication/log_archive_failure_count` GA ** _(project)_**   
Number of log archival failures.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of failed attempts for archiving replication log files. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/replication/log_archive_success_count` GA ** _(project)_**   
Number of log archival successes.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of successful attempts for archiving replication log files. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/replication/network_lag` GA ** _(project)_**   
Network lag   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates time taken from primary binary log to IO thread on replica. Only applicable to replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/replication/replica_lag` GA ** _(project)_**   
Replication lag   
`GAUGE`, `DOUBLE`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of seconds the read replica is behind its primary (approximation). A negative value indicates that replication is inactive. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/replication/state` BETA ** _(project)_**   
Replication state   
`GAUGE`, `BOOL`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The current serving state of replication. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: State of replication:"Running" - Replication is active and running;"Stopped" - Replication is inactive and stopped;"Error" - There is an error happening and replication is stopped.   
`database/sqlserver/audits_size` GA ** _(project)_**   
Size of stored audit files.   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Tracks the size in bytes of stored SQLServer audit files on an instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/audits_upload_count` GA ** _(project)_**   
Total number of successfully uploaded audits.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Counts total number of SQLServer audit file uploads to a GCS bucket and whether or not an upload was successful. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`upload_status`: Upload status of latest audit file.   
`database/sqlserver/connections/connection_reset_count` GA ** _(project)_**   
Connection resets   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of logins started from the connection pool since the last restart of SQL Server service. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/connections/login_attempt_count` GA ** _(project)_**   
Login attempts   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of login attempts since the last restart of SQL Server service. This does not include pooled connections. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/connections/logout_count` GA ** _(project)_**   
Logouts   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of logout operations since the last restart of SQL Server service. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/connections/processes_blocked` GA ** _(project)_**   
Processes blocked   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of blocked processes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/data_cache/hit_count` GA ** _(project)_**   
SQL Server data cache hit count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache hit read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/data_cache/hit_ratio` GA ** _(project)_**   
SQL Server data cache hit ratio   
`GAUGE`, `DOUBLE`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Ratio of successful data cache hit read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/data_cache/miss_count` GA ** _(project)_**   
SQL Server data cache miss count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of data cache miss read operations for this instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/databases` GA ** _(project)_**   
SQL Server Databases   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of databases on the instance excluding system databases. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`state`: Database state, for example, 'ONLINE' or 'SUSPECT'.   
`recovery_model`: Database recovery model, one of [FULL, BULK_LOGGED, SIMPLE].   
`is_cdc_enabled`: (BOOL) Indicates whether CDC is enabled.   
`is_published`: (BOOL) Indicates whether a database is published.   
`auto_close`: (BOOL) Indicates whether auto-close is enabled on a database.   
`database/sqlserver/memory/buffer_cache_hit_ratio` GA ** _(project)_**   
Buffer cache hit ratio   
`GAUGE`, `DOUBLE`, `%`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current percentage of pages found in the buffer cache without having to read from disk. The ratio is the total number of cache hits divided by the total number of cache lookups. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/checkpoint_page_count` GA ** _(project)_**   
Checkpoint pages   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of pages flushed to disk by a checkpoint or other operation that requires all dirty pages to be flushed. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/committed_kb` GA ** _(project)_**   
SQL Server committed memory   
`GAUGE`, `INT64`, `kBy`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Represents the actual amount of memory committed in the memory manager. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/committed_target_kb` GA ** _(project)_**   
SQL Server committed target memory   
`GAUGE`, `INT64`, `kBy`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Represents the desired amount of memory SQL Server wants to have available. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/free_list_stall_count` GA ** _(project)_**   
Free list stalls   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of requests that had to wait for a free page. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/lazy_write_count` GA ** _(project)_**   
Lazy writes   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of buffers written by the buffer manager's lazy writer. The lazy writer is a system process that flushes out batches of dirty, aged buffers (buffers that contain changes that must be written back to disk before the buffer can be reused for a different page) and makes them available to user processes. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/memory_clerk` GA ** _(project)_**   
SQL Server memory clerk allocations   
`GAUGE`, `INT64`, `MiBy`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Specifies the amount of page memory allocated for each memory clerk. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`clerk_type`: The memory clerk type.   
`clerk_name`: The name of the memory clerk.   
`database/sqlserver/memory/memory_grants_pending` GA ** _(project)_**   
Memory grants pending   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of processes waiting for a workspace memory grant. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/page_life_expectancy` GA ** _(project)_**   
Page life expectancy   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of seconds a page will stay in the buffer pool without references. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/memory/page_operation_count` GA ** _(project)_**   
Page operations   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of physical database page reads or writes. This statistic counts physical page reads or writes across all databases. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`operation`: Page operation, one of [Read, Write].   
`database/sqlserver/replication/bytes_sent_to_replica_count` GA ** _(project)_**   
Bytes sent to replica   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of bytes sent to the remote availability replica. Before compression for async replica. Actual number of bytes for sync replica which has no compression. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`database/sqlserver/replication/log_apply_pending_queue` GA ** _(project)_**   
Log apply pending queue   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of log blocks that are waiting to be applied to all database replicas. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/replication/log_bytes_received_count` GA ** _(project)_**   
Log bytes received   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total amount of log records received by the secondary replica for all databases. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/replication/recovery_queue` GA ** _(project)_**   
Recovery queue   
`GAUGE`, `INT64`, `kBy`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current amount of log records in kilobytes in the log files of the secondary replica that have not been redone. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/replication/redone_bytes_count` GA ** _(project)_**   
Redone bytes   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total amount of log records redone on all secondary databases. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/replication/resent_message_count` GA ** _(project)_**   
Resent messages   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of Always On messages resent. A resent message is a message that was attempted to be sent but was unable to complete and must be attempted to be sent again. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`database/sqlserver/schedulers/active_workers` GA ** _(project)_**   
Number of active workers per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of workers that are active. An active worker is never preemptive, must have an associated task, and is either running, runnable, or suspended. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/schedulers/by_status` GA ** _(project)_**   
Number of schedulers   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of schedulers reporting a particular status. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`status`: Scheduler status, one of [HIDDEN ONLINE, HIDDEN OFFLINE, VISIBLE ONLINE, VISIBLE OFFLINE, VISIBLE ONLINE (DAC), HOT_ADDED].   
`is_internal`: (BOOL) Indicates whether the scheduler is internal.   
`database/sqlserver/schedulers/current_tasks` GA ** _(project)_**   
Number of current tasks per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of current tasks that are associated with a scheduler. This count includes tasks that are waiting for a worker to execute them and tasks that are currently waiting or running (in SUSPENDED or RUNNABLE state). Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/schedulers/current_workers` GA ** _(project)_**   
Number of workers per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of workers that are associated with a scheduler. It includes workers that are not assigned any task. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/schedulers/pending_disk_io` GA ** _(project)_**   
Number of pending I/O operations per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of pending I/Os that are waiting to be completed. Each scheduler has a list of pending I/Os that are checked to determine whether they have been completed every time there is a context switch. The count is incremented when the request is inserted. This count is decremented when the request is completed. This number does not indicate the state of the I/Os. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/schedulers/runnable_tasks` GA ** _(project)_**   
Number of workers with assigned tasks per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of workers, with tasks assigned to them, that are waiting to be scheduled on the runnable queue. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/schedulers/work_queue` GA ** _(project)_**   
Number of pending tasks per scheduler   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of tasks in the pending queue. These tasks are waiting for a worker to pick them up. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`scheduler_id`: Identifier of the scheduler, for example, '3' or 'Internal'.   
`database/sqlserver/server_principals` GA ** _(project)_**   
Server principals   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of server principals on the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`type`: Server principal type, one of [SQL_LOGIN, WINDOWS_LOGIN, WINDOWS_GROUP, SERVER_ROLE, CERTIFICATE_MAPPED_LOGIN, EXTERNAL_LOGIN, EXTERNAL_GROUP, ASYMMETRIC_KEY_MAPPED_LOGIN].   
`is_enabled`: (BOOL) Indicates whether a server principal is enabled.   
`database/sqlserver/sql_agent/jobs` GA ** _(project)_**   
SQL Server agent jobs   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of SQL Server agent jobs on the instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`is_enabled`: (BOOL) Indicates whether a job is enabled.   
`last_run_outcome`: Last outcome of a job run, one of [Fail, Succeed, Retry, Cancel, In progress, Unknown].   
`database/sqlserver/transactions/batch_request_count` GA ** _(project)_**   
Batch requests   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of Transact-SQL command batches received. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/batch_requests_cpu_time` GA ** _(project)_**   
SQL Server batch requests CPU time   
`DELTA`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total CPU time for completed batch requests, bucketed by CPU time. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`bucket`: Bucket.   
`database/sqlserver/transactions/batch_requests_cpu_time_count` GA ** _(project)_**   
SQL Server batch requests CPU time count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Count of completed batch requests, bucketed by CPU time. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`bucket`: Bucket.   
`database/sqlserver/transactions/batch_requests_elapsed_time` GA ** _(project)_**   
SQL Server batch requests elapsed time   
`DELTA`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total elapsed time for completed batch requests, bucketed by the elapsed time of each batch statement. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`bucket`: Bucket.   
`database/sqlserver/transactions/batch_requests_elapsed_time_count` GA ** _(project)_**   
SQL Server batch requests elapsed time count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Count of completed batch requests bucketed by elapsed time. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`bucket`: Bucket.   
`database/sqlserver/transactions/deadlock_count` GA ** _(project)_**   
Deadlocks   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of lock requests that resulted in a deadlock. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`database/sqlserver/transactions/forwarded_record_count` GA ** _(project)_**   
Forwarded records   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of records fetched through forwarded record pointers. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/full_scan_count` GA ** _(project)_**   
Full scans   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of unrestricted full scans. These can be either base-table or full-index scans. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/lock_wait_count` GA ** _(project)_**   
Lock waits   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of lock requests that required the caller to wait. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`database/sqlserver/transactions/lock_wait_time` GA ** _(project)_**   
Lock wait time   
`DELTA`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total time lock requests were waiting for locks. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`database/sqlserver/transactions/log_bytes_flushed_count` GA ** _(project)_**   
Log bytes flushed   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of log bytes flushed. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Database name, one of [tempdb, model, msdb, mssqlsystemresource, master, other].   
`database/sqlserver/transactions/page_split_count` GA ** _(project)_**   
Page splits   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of page splits that occur as the result of overflowing index pages. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/probe_scan_count` GA ** _(project)_**   
Probe scans   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of probe scans that are used to find at most one single qualified row in an index or base table directly. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/sql_compilation_count` GA ** _(project)_**   
SQL compilations   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of SQL compilations. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/sql_recompilation_count` GA ** _(project)_**   
SQL recompilations   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of SQL recompilations. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/transactions/transaction_count` GA ** _(project)_**   
Transactions started   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of transactions started. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`database`: Database name, one of [tempdb, model, msdb, mssqlsystemresource, master, other].   
`database/sqlserver/wait_count` GA ** _(project)_**   
SQL Server wait count   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The number of waits for each wait type. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`wait_type`: Wait type.   
`wait_category`: Wait category.   
`database/sqlserver/wait_time` GA ** _(project)_**   
SQL Server wait time   
`DELTA`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The accumulated wait time for each wait type. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`wait_type`: Wait type.   
`wait_category`: Wait category.   
`database/sqlserver/xevents_size` GA ** _(project)_**   
Size of stored XEvents files.   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Tracks the size in bytes of stored SQLServer XEvents files on an instance. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/sqlserver/xevents_upload_count` GA ** _(project)_**   
Total number of successfully uploaded XEvents.   
`DELTA`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Counts total number of SQLServer XEvents file uploads to a GCS bucket and whether or not an upload was successful. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._   
`upload_status`: Upload status of latest XEvents file.   
`database/state` DEPRECATED ** _(project)_**   
State   
`GAUGE`, `STRING`, ``   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _The current serving state of the Cloud SQL instance. This can be one of the following: RUNNING: The instance is *expected* to be running. If an instance experiences unplanned (non-maintenance) downtime, the state will still be RUNNING, but the database/up metric will report 0. SUSPENDED: The instance is not available, for example due to problems with billing. RUNNABLE: The instance has been stopped by owner. It is not currently running, but it's ready to be restarted. PENDING_CREATE: The instance is being created. MAINTENANCE: The instance is down for maintenance. FAILED: The instance creation failed or an operation left the instance in an unknown bad state. UNKNOWN_STATE: The state of the instance is unknown. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/swap/bytes_used` GA ** _(project)_**   
Swap space usage   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Swap space used by the database container. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/swap/pages_swapped_in_count` GA ** _(project)_**   
Pages Swapped In Count   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total count of pages swapped in of disk since the system was booted. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/swap/pages_swapped_out_count` GA ** _(project)_**   
Pages Swapped Out Count   
`DELTA`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total count of pages swapped out of disk since the system was booted. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/up` GA ** _(project)_**   
Server up   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Indicates if the server is up or not. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`database/uptime` GA ** _(project)_**   
Uptime   
`DELTA`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of the time in seconds the instance has been running. Sampled every 60 seconds. After sampling, data is not visible for up to 165 seconds._  
`per_database/conn_pool/client_connections` GA ** _(project)_**   
Client connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Number of client connections per database grouped by status._   
`status`: Status of the client connection e.g. 'active' or 'waiting'.   
`per_database/conn_pool/client_connections_attempts_count` GA ** _(project)_**   
Client connection attempts count   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Number of client connection attempts received per database._  
`per_database/conn_pool/client_connections_avg_wait_time` GA ** _(project)_**   
Average wait time   
`GAUGE`, `INT64`, `us`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Average wait time spent by clients waiting for a server connection per database in microseconds._  
`per_database/conn_pool/client_connections_error_count` GA ** _(project)_**   
Error count   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Count of errors that cause client disconnection including auth error, client connection setup error, server connection error and timeout errors._  
`per_database/conn_pool/num_pools` GA ** _(project)_**   
Number of connection pools   
`GAUGE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Number of connection pools per database._  
`per_database/conn_pool/server_connections` GA ** _(project)_**   
Server connections   
`GAUGE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Number of server connections per database grouped by status._   
`status`: Status of the server connection e.g. 'active' or 'idle'.   
`per_database/postgresql/external_sync/initial_sync_complete` GA ** _(project)_**   
External server migration phase   
`GAUGE`, `BOOL`, ``   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Migration phase of each database on the external server (ES) replica. This only applies to instances that are replicating from an external server._  
`per_database/postgresql/external_sync/replication_byte_lag` GA ** _(project)_**   
Exernal server replication byte lag   
`GAUGE`, `INT64`, `1`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Replication lag in bytes of each database on the external server (ES) replica. This only applies to instances that are replicating from an external server._  
`per_database/sqlserver/replication/delay` GA ** _(project)_**   
SQL Server replication delay   
`GAUGE`, `INT64`, `s`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _The time difference in seconds between the most recent transaction committed on the primary replica and the commit time of the most recent transaction redone on the secondary replica._   
`replica_instance_name`: Instance name of the replica.   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`availability_mode`: Availability mode of the replica.   
`per_database/sqlserver/replication/logsend_queue_size` GA ** _(project)_**   
SQL Server logsend queue size   
`GAUGE`, `INT64`, `By`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _Total size of log records in the log files of the primary database that haven't been sent to the secondary replica._   
`replica_instance_name`: Instance name of the replica.   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`per_database/sqlserver/replication/redo_queue_size` GA ** _(project)_**   
SQL Server redo queue size   
`GAUGE`, `INT64`, `By`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _The number of log records in the log files of the secondary replica that aren't yet redone._   
`replica_instance_name`: Instance name of the replica.   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`per_database/sqlserver/replication/seconds_behind_master` GA ** _(project)_**   
SQL Server seconds behind primary   
`GAUGE`, `INT64`, `s`   
**[cloudsql_instance_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_instance_database)** |  _The number of seconds since the hardening of the earliest hardened LSN on the primary replica that is yet to be hardened on the secondary replica._   
`replica_instance_name`: Instance name of the replica.   
`replica_name`: Replica name, for example, 'ag:0975ec5e220191d' or 'ag:58cb483ac3f7083'.   
`semi_managed/database/cpu/utilization` GA ** _(project)_**   
CPU utilization (Semi-managed)   
`GAUGE`, `DOUBLE`, `10^2.%`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current CPU utilization represented as a percentage ' + 'of the reserved CPU that is currently in use. Values ' + 'are typically numbers between 0.0 and 1.0 (but ' + 'might exceed 1.0). Charts display the values as a ' + 'percentage between 0% and 100% (or more)._  
`semi_managed/database/disk/bytes_used` GA ** _(project)_**   
Bytes used (Semi-managed)   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Data utilization in bytes._   
`data_type`: A breakdown of disk usage by type of usage.   
`semi_managed/database/disk/quota` GA ** _(project)_**   
Disk quota (Semi-managed)   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Maximum data disk size in bytes._  
`semi_managed/database/disk/read_ops_count` GA ** _(project)_**   
Disk read IO (Semi-managed)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk read IO operations._  
`semi_managed/database/disk/write_ops_count` GA ** _(project)_**   
Disk write IO (Semi-managed)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Delta count of data disk write IO operations._  
`semi_managed/database/memory/total_usage` GA ** _(project)_**   
Total memory usage (Semi-managed)   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total RAM usage in bytes including buffer cache._  
`semi_managed/database/memory/usage` GA ** _(project)_**   
Memory usage (Semi-managed)   
`GAUGE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _RAM usage in bytes._  
`semi_managed/database/network/connections` GA ** _(project)_**   
Cloud SQL Connections (Semi-managed)   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Number of connections to databases on the Cloud SQL instance._  
`semi_managed/database/network/received_bytes_count` GA ** _(project)_**   
Received bytes (Semi-managed)   
`CUMULATIVE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Cumulative count of bytes received through the network._  
`semi_managed/database/network/sent_bytes_count` GA ** _(project)_**   
Sent bytes (Semi-managed)   
`CUMULATIVE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Cumulative count of bytes sent through the network._  
`semi_managed/database/sqlserver/connections/connection_reset_count` GA ** _(project)_**   
Connection resets (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of logins started from the connection pool since the last restart of SQL Server service._  
`semi_managed/database/sqlserver/connections/login_attempt_count` GA ** _(project)_**   
Login attempts (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of login attempts since the last restart of SQL Server service. This does not include pooled connections._  
`semi_managed/database/sqlserver/connections/logout_count` GA ** _(project)_**   
Logouts (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of logout operations since the last restart of SQL Server service._  
`semi_managed/database/sqlserver/connections/processes_blocked` GA ** _(project)_**   
Processes blocked (Semi-managed SQL Server)   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of blocked processes._  
`semi_managed/database/sqlserver/memory/buffer_cache_hit_ratio` GA ** _(project)_**   
Buffer cache hit ratio (Semi-managed SQL Server)   
`GAUGE`, `DOUBLE`, `%`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current percentage of pages found in the buffer cache without having to read from disk. The ratio is the total number of cache hits divided by the total number of cache lookups._  
`semi_managed/database/sqlserver/memory/checkpoint_page_count` GA ** _(project)_**   
Checkpoint pages (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of pages flushed to disk by a checkpoint or other operation that requires all dirty pages to be flushed._  
`semi_managed/database/sqlserver/memory/free_list_stall_count` GA ** _(project)_**   
Free list stalls (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of requests that had to wait for a free page._  
`semi_managed/database/sqlserver/memory/lazy_write_count` GA ** _(project)_**   
Lazy writes (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of buffers written by the buffer manager's lazy writer. The lazy writer is a system process that flushes out batches of dirty, aged buffers (buffers that contain changes that must be written back to disk before the buffer can be reused for a different page) and makes them available to user processes._  
`semi_managed/database/sqlserver/memory/memory_grants_pending` GA ** _(project)_**   
Memory grants pending (Semi-managed SQL Server)   
`GAUGE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of processes waiting for a workspace memory grant._  
`semi_managed/database/sqlserver/memory/page_life_expectancy` GA ** _(project)_**   
Page life expectancy (Semi-managed SQL Server)   
`GAUGE`, `INT64`, `s`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Current number of seconds a page will stay in the buffer pool without references._  
`semi_managed/database/sqlserver/memory/page_operation_count` GA ** _(project)_**   
Page operations (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of physical database page reads or writes. This statistic counts physical page reads or writes across all databases._   
`operation`: Page operation, one of [Read, Write].   
`semi_managed/database/sqlserver/transactions/batch_request_count` GA ** _(project)_**   
Batch requests (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of Transact-SQL command batches received._  
`semi_managed/database/sqlserver/transactions/deadlock_count` GA ** _(project)_**   
Deadlocks (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of lock requests that resulted in a deadlock._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`semi_managed/database/sqlserver/transactions/full_scan_count` GA ** _(project)_**   
Full scans (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of unrestricted full scans. These can be either base-table or full-index scans._  
`semi_managed/database/sqlserver/transactions/lock_wait_count` GA ** _(project)_**   
Lock waits (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of lock requests that required the caller to wait._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`semi_managed/database/sqlserver/transactions/lock_wait_time` GA ** _(project)_**   
Lock wait time (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `ms`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total time lock requests were waiting for locks._   
`locked_resource`: Locked resource, for example, 'Page' or 'Database'.   
`semi_managed/database/sqlserver/transactions/page_split_count` GA ** _(project)_**   
Page splits (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of page splits that occur as the result of overflowing index pages._  
`semi_managed/database/sqlserver/transactions/sql_compilation_count` GA ** _(project)_**   
SQL compilations (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of SQL compilations._  
`semi_managed/database/sqlserver/transactions/sql_recompilation_count` GA ** _(project)_**   
SQL recompilations (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of SQL recompilations._  
`semi_managed/database/sqlserver/transactions/transaction_count` GA ** _(project)_**   
Transactions started (Semi-managed SQL Server)   
`CUMULATIVE`, `INT64`, `1`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total number of transactions started._   
`database`: Database name, one of [tempdb, model, msdb, mssqlsystemresource, master, other].   
`database_names_hash`: Unique identifier hash of the databases that are part of the database metric field.   
`semi_managed/database/swap/pages_swapped_in_count` GA ** _(project)_**   
Pages Swapped In Count (Semi-managed)   
`CUMULATIVE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total count of pages swapped in of disk since the system was booted._  
`semi_managed/database/swap/pages_swapped_out_count` GA ** _(project)_**   
Pages Swapped Out Count (Semi-managed)   
`CUMULATIVE`, `INT64`, `By`   
**[cloudsql_database](https://docs.cloud.google.com/monitoring/api/resources#tag_cloudsql_database)** |  _Total count of pages swapped out of disk since the system was booted._  
  
Table generated at 2026-10-16 17:31:47 UTC.

## What's next

  * Learn how monitoring works in Google Cloud with the [Introduction to Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).
  * Learn how to use [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).
  * See the complete [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics) for all Google Cloud products.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
