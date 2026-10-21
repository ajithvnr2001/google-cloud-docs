---
url: https://docs.cloud.google.com/sql/docs/mysql/replication/replication-lag/
title: Replication lag \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:19.282098+00:00
---

# Replication lag  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/replication/replication-lag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Replication lag Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/replication-lag "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/replication/replication-lag "View this page for the SQL Server database engine")

This page describes how to troubleshoot and fix replication lag for Cloud SQL read replicas.

## Overview

Cloud SQL read replicas use MySQL row-based replication using global transaction identifiers (GTIDs). Changes are written to the binary log of the primary instance and sent to the replica, where they are received and then applied to the database. 

Replication lag can happen in a few scenarios, such as:

  * The primary instance can't send the changes fast enough to the replica.
  * The replica can't receive the changes quickly enough.
  * The replica can't apply the changes quickly enough.

Use the `network_lag` metric to monitor the first two scenarios when the primary instance can't send changes fast enough or the replica can't receive changes quickly enough. 

The total lag is observed with the `replica_lag` metric. The difference between `replica_lag` and the `network_lag` can indicate the third reason when the replica can't apply replication changes fast enough. For more information about these metrics, see Monitor replication lag. 

## Faster replica configuration

We have two ways to make a MySQL replica apply changes faster. Users can configure their replicas with the following options: 

  * **Parallel replication**
  * **High performance flushing**



### Parallel replication

Parallel replication might help replication lag by configuring the replica to use multiple threads acting in parallel to apply changes on the replica. For information about using parallel replication, see [ Configuring parallel replication](https://docs.cloud.google.com/sql/docs/mysql/replication/manage-replicas#configuring-parallel-replication).

When you enable parallel replication by setting the `replica_parallel_workers` (or `slave_parallel_workers`) flag, consider the following: 

  * We recommend setting the `replica_parallel_workers` flag value to a number that matches the vCPU count of the replica instance. Setting it to a very high value can cause lock waits, lock wait timeouts, and deadlocks. If you observe lock wait spikes aligned with replication lag, consider reducing parallelism.
  * If your MySQL version supports the `binlog_transaction_dependency_tracking` flag, consider setting it to `WRITESET` for the primary instance. This is the default behavior for 8.0.34 and earlier.



### High performance flushing

By default, Cloud SQL for MySQL flushes the redo logs to disk after each transaction for durability. High performance flushing reduces the frequency with which the redo logs are flushed to the disk to once per second. Doing so can help improve write performance on the replica by reducing disk I/O.

Set the [`innodb_flush_log_at_trx_commit`](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-i) flag on the read replica to 2. If binary logging is enabled for the replica, to help make the `innodb_flush_log_at_trx_commit` flag effective, we recommend setting the `sync_binlog` flag to a high value, for example, 10,000.

See [Tips for working with flags](https://docs.cloud.google.com/sql/docs/mysql/flags#tips) for more information about this flag.

When the [innodb_flush_log_at_trx_commit](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-i) flag is set on the read replica and Cloud SQL detects that a crash might have occurred, Cloud SQL automatically recreates the replica. 

## Ensure replica is adequately provisioned

A replica instance that is smaller than the primary instance (for example, with less vCPUs and memory) can experience replication lag. A smaller replica might also have different default configuration flags compared to a larger primary instance. We recommend that the replica instance is at least as large as the primary instance to have enough resources to handle the replication load.

High CPU utilization on the replica can also cause replication lag. If the replica's CPU utilization is high (for example, over 90%), consider increasing the replica's CPU capacity.

You can use the `SHOW VARIABLES` command to see replica and primary instance configuration and compare them for differences. For example, a smaller replica can't configure the `innodb_buffer_pool_size` to be the same value as the primary and it might impact the replica's performance. 

## Optimize queries and schema

This section suggests some common query and schema optimizations you can make to improve replication performance.

### Query isolation level in the read replica

The `REPEATABLE READ` and `SERIALIZABLE` transaction isolation levels acquire locks that might block the replication changes. Consider reducing the isolation level for your queries in the replica. The `READ COMMITTED` transaction isolation level might perform better.

**Note:** The MySQL default transaction isolation level is `REPEATABLE READ` for historical reasons.

### Long-running transactions in the primary database

Long-running transactions on the primary instance can cause replication lag. The binary log is not sent to the replica until the transaction is committed.

If a large number of rows are updated in a single transaction, it can cause a sudden spike in the number of changes that need to be applied to the primary instance and then sent to the replica. This applies to single-statement updates or deletes that affect many rows at once. Changes are sent to the replica after they are committed. Applying a sudden spike of changes in the replica can increase the possibility of lock contention in the replica if the query load on the replica is also high, leading to replication lag.

Consider breaking large transactions into multiple smaller transactions. You can monitor for long-running transactions by checking the `cloudsql.googleapis.com/database/mysql/innodb/active_trx_longest_time` metric on the primary. 

### Missing primary keys

Cloud SQL read replicas use row-based replication, which performs poorly if the MySQL tables that are replicated don't have primary keys. We recommend that all of the replicated tables have primary keys.

For MySQL 8 or later, we recommend that you set the flag [`sql_require_primary_key`](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-i) to `ON` to require tables in your database to have primary keys.

### Long-running transactions in the read replica

Long-running transactions on the replica, such as `SELECT` statements, can block or slow down replication. Table scan is a common problem. Investigate any long-running queries and consider optimizing them. These queries can lead to `InnoDB` history list size growth.

### Excessive `InnoDB` history length

A very large `InnoDB` history list can cause performance problems and slow down replication. You can monitor the history list length using the `cloudsql.googleapis.com/database/mysql/innodb/history_list_length` metric. This metric can be high in the primary as well and might be causing performance issues already. If, after initial startup, your replica shows signs of high replication lag, this might be the cause.

A large history list can be caused by the following: 

  * **Long-running transactions.** Long-running or idle transactions prevent purging of old undo log entries.
  * **Slow disk performance.** Purging is an I/O-intensive operation.
  * **`REPEATABLE READ` isolation level.** This can contribute to history list growth.
  * **Insufficient purge configuration.** The `innodb_purge_threads` parameter, which controls the number of threads dedicated to purging, might be set too low for the workload.



To help address this, try the following: 

  * **Breakdown large transaction to smaller ones.** Allow quicker purging of old logs.
  * **Use a larger instance.** Larger instances have more CPU and memory.
  * **Tune purge settings.** Increase `innodb_purge_threads`, `innodb_io_capacity`, and `innodb_io_capacity_max`.
  * **Use`READ COMMITTED` isolation level.**
  * **Ensure tables have primary keys.** Tables without primary keys can cause table scans which can slow down replication and contribute to history list growth.



### High amount of lock waits

A high number of lock waits on the replica can slow down replication, especially with parallel replication enabled. You can monitor for lock waits and deadlocks using the following [metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-cloudsql): 

  * `cloudsql.googleapis.com/database/mysql/innodb/row_lock_waits_count`
  * `cloudsql.googleapis.com/database/mysql/innodb/row_lock_time`
  * `cloudsql.googleapis.com/database/mysql/innodb/lock_timeout_count`
  * `cloudsql.googleapis.com/database/mysql/innodb/deadlocks_count`



If these lock metrics are too high and seem to be correlated with replication lag, consider reducing the value of the `replica_parallel_workers` flag. Isolation level might also impact locks. 

### Exclusive locks due to DDL

Data definition language (DDL) commands, such as `ALTER TABLE` and `CREATE INDEX`, can cause replication lag in the replica due to exclusive locks. To avoid lock contention, consider scheduling DDL execution during times when the query load is lower on the replicas.

Consider utilizing the MySQL 8.0 Online DDL feature. 

### Overloaded replica

If a read replica is receiving too many queries, replication could be blocked. Consider splitting the reads among multiple replicas to reduce the load on each one.

To avoid query spikes, consider throttling replica read queries in your application logic or in a proxy layer if you use one.

If there are spikes of activity on the primary instance, consider spreading out updates.

### Monolithic primary database

Consider sharding the primary database vertically (or horizontally) to prevent one or more lagging tables from holding back all the other tables.

## Monitor replication lag

You can use the `replica_lag` and `network_lag` metrics to monitor replication lag and identify whether the cause of the lag is in the primary database, the network, or the replica.

Metric| Description  
---|---  
Replication lag  
(`cloudsql.googleapis.com/database/replication/replica_lag`) |  The number of seconds that the replica's state is lagging behind the state of the primary instance. This is the difference between the current time and the original timestamp at which the primary database committed the transaction that is currently being applied on the replica. In particular, writes might be counted as lagging even if they have been received by the replica, if the replica hasn't yet applied the write to the database. This metric reports the value of `Seconds_Behind_Master` when `SHOW SLAVE STATUS` is run on the replica. For more information, see [Checking Replication Status](https://dev.mysql.com/doc/refman/8.4/en/replication-administration-status.html) in the MySQL Reference Manual.  
Last I/O thread error number  
(`cloudsql.googleapis.com/database/mysql/replication/last_io_errno`) |  Indicates the last error that caused the I/O thread to fail. If this is non-zero, replication is broken. This is rare, but it might happen. Check MySQL documentation to understand what the error code indicates. For example, binlog files in the primary instance might have been deleted before the replica received them. Cloud SQL usually automatically recreates the replica if replication is broken. This `last_io_errno` metric might tell you the reason why.   
Last SQL thread error number  
(`cloudsql.googleapis.com/database/mysql/replication/last_sql_errno`) |  Indicates the last error that caused the SQL thread to fail. If this is non-zero, replication is broken. This is rare, but it might happen. Check MySQL documentation to understand what the error code indicates. Cloud SQL will usually automatically recreate the replica if replication is broken. This `last_sql_errno` metric can tell you the reason why.   
Network lag  
(`cloudsql.googleapis.com/database/replication/network_lag`) |  The length of time, in seconds, that it takes from writing the binlog in the primary database to reaching the IO thread in the replica. If the `network_lag` is zero, or negligible, but the `replica_lag` is high, it indicates that the SQL thread is not able to apply replication changes fast enough. Because `network_lag` is rounded up to the nearest second, a reported value of 1 second can represent an underlying lag of anything from a millisecond or two up to a full second.  
  
## Verify replication

To verify that replication is working, run the following statement against the replica:
    
    
    mysql> SHOW SLAVE STATUS\G;
    *************************** 1. row ***************************
                   Slave_IO_State: Queueing master event to the relay log
                      Master_Host: xx.xxx.xxx.xxx
                      Master_User: cloudsqlreplica
                      Master_Port: 3306
                    Connect_Retry: 60
                  Master_Log_File: mysql-bin.199927
              Read_Master_Log_Pos: 83711956
                   Relay_Log_File: relay-log.000025
                    Relay_Log_Pos: 24214376
            Relay_Master_Log_File: mysql-bin.199898
                 Slave_IO_Running: Yes
                Slave_SQL_Running: Yes
                  Replicate_Do_DB:
              Replicate_Ignore_DB:
               Replicate_Do_Table:
           Replicate_Ignore_Table:
          Replicate_Wild_Do_Table:
      Replicate_Wild_Ignore_Table:
                       Last_Errno: 0
                       Last_Error:
                     Skip_Counter: 0
              Exec_Master_Log_Pos: 24214163
                  Relay_Log_Space: 3128686571
                  Until_Condition: None
                   Until_Log_File:
                    Until_Log_Pos: 0
               Master_SSL_Allowed: Yes
               Master_SSL_CA_File: master_server_ca.pem
               Master_SSL_CA_Path: /mysql/datadir
                  Master_SSL_Cert: replica_cert.pem
                Master_SSL_Cipher:
                   Master_SSL_Key: replica_pkey.pem
            Seconds_Behind_Master: 2627
    Master_SSL_Verify_Server_Cert: No
                    Last_IO_Errno: 0
                    Last_IO_Error:
                   Last_SQL_Errno: 0
                   Last_SQL_Error:
      Replicate_Ignore_Server_Ids:
                 Master_Server_Id: 321071839
                      Master_UUID: 437d04e9-8456-11e8-b13d-42010a80027b
                 Master_Info_File: mysql.slave_master_info
                        SQL_Delay: 0
              SQL_Remaining_Delay: NULL
          Slave_SQL_Running_State: System lock
               Master_Retry_Count: 86400
                      Master_Bind:
          Last_IO_Error_Timestamp:
         Last_SQL_Error_Timestamp:
                   Master_SSL_Crl:
               Master_SSL_Crlpath:
               Retrieved_Gtid_Set: 437d04e9-8456-11e8-b13d-42010a80027b:52111095710-52120776390
                Executed_Gtid_Set: 437d04e9-8456-11e8-b13d-42010a80027b:1-52113039508
                    Auto_Position: 1
             Replicate_Rewrite_DB:
                     Channel_Name:
               Master_TLS_Version:
    1 row in set (0.00 sec)
    

If replication is happening, the first column, `Slave_IO_State`, shows `Waiting for master to send event` or a similar message. Also, the `Last_IO_Error` field is empty.

If replication is not happening, the `Slave_IO_State` column shows the status `Connecting to master` and the `Last_IO_Error` column shows the status `error connecting to master cloudsqlreplica@x.x.x.x:3306`.

According to the [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/show-slave-status.html), a few other interesting fields that relate to replication lag include the following:

Field| Description  
---|---  
`Master_Log_File`  
| The name of the source binary log file that the I/O thread is currently reading from.   
`Read_Master_Log_Pos`  
| The position in the current source binary log file the I/O thread has read up to.   
`Relay_Log_File`  
| The name of the relay log file the SQL thread is currently reading and executing from.   
`Relay_Log_Pos`  
| The position in the current relay log file the SQL thread has read and executed up to.   
`Relay_Master_Log_File`  
| The name of the source binary log file containing the most recent event executed by the SQL thread.   
  
In the previous example `Relay_Master_Log_File` has the value `mysql-bin.199898`. `Master_Log_File` has the value `mysql-bin.199927`. The numeric suffix 199898 is less than 199927. This means that even though the replica has received a newer `mysql-bin.199927` log file, it's still applying the older `mysql-bin.199898`.

In this case, the SQL thread is lagging in the replica.

You can also connect to the primary database and execute:
    
    
      SHOW MASTER STATUS;
    

This command shows you which binlog file is being written in the primary database.

If the primary database binary log file is newer than the `Master_Log_File` in the replica, it means that the I/O thread is lagging. The replica is still reading an older binary log file from the primary database.

When the I/O thread is lagging, the `network_lag` metric is also high. When the SQL thread is lagging, but the I/O thread is not, then the `network_lag` metric isn't as high, but the `replica_lag` is high.

The previous commands let you observe lag details while the lag is happening, but the metrics `network_lag` and `replica_lag` provide you a way to look into the past occurrences of the lag.

## Recreate lagging replica

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Recreate a lagging replica when replication falls behind an acceptable length of time.

With Cloud SQL, you can configure your read replica to recreate itself if replication lags (or is delayed) beyond an acceptable length of time, _and_ that delay persists for at least five minutes.

If you define an acceptable replication delay as being less than 360 seconds (six minutes), and a replication delay of at least 361 seconds persists for more than five minutes, then after five minutes, the primary instance creates a new snapshot of itself and the read replica is recreated using this snapshot.

Recreating a lagging read replica provides the following benefits:

  * You control what's considered an acceptable range for replication delay.
  * You can reduce the time spent troubleshooting replication delay by hours or even days.



Additional feature details apply:

  * Compatible with the following versions: 
    * MySQL 5.7
    * MySQL 8.0
    * MySQL 8.4
    * MySQL 9.7
  * An acceptable range for replication lag or delay must be defined in seconds.
  * The minimum acceptable value is 300 seconds or five minutes.
  * The maximum acceptable value is 31,536,000 seconds or one year. 
    * If you enable recreate lagging replica for an instance but don't set the maximum acceptable replication delay, then Cloud SQL uses the default value of one year.
  * Types of instances that are supported: 
    * Read replica
    * Cross-region read replica
    * Cascading replica
  * The value set for the `replicationLagMaxSeconds` field is specific to each replica instance. If a primary instance has multiple replica instances, then you can set each replica with a different value.
  * When a replica is recreated, users can expect some downtime while the following operations are completed: 
    * Replication is stopped.
    * The replica is deleted.
    * A snapshot of the primary instance is created.
    * The replica is recreated from this latest snapshot. The new replica uses the same name and IP address as the previous replica. As a result, MySQL must stop and restart.
    * The new replica starts replicating data.
  * The `replicationLagMaxSeconds` is an instance level field. Each instance has its own value.
  * If you have multiple read replicas for the same primary instance, you can set a unique value for the `replicationLagMaxSeconds` field for each replica.

Defining different time thresholds for different replicas can help you avoid a scenario where all replicas go down at the same time.




### Enable recreate lagging replica

The recreate lagging replica feature is disabled by default. To enable it when you create an instance, use one of the following methods:

###  gcloud 

Use the [`gcloud sql instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/create) command to create a new read replica instance with the  
`--replication-lag-max-seconds-for-recreate` flag:
    
    
    gcloud beta sql instances create REPLICA_INSTANCE_NAME \
      --master-instance-name=PRIMARY_INSTANCE_NAME \
      --database-version=DATABASE_VERSION \
      --tier=TIER \
      --edition=EDITION \
      --region=REGION \
      --root-password=PASSWORD \
      --replication-lag-max-seconds-for-recreate=REPLICATION_LAG_MAX_SECONDS

Where:

  * `REPLICA_INSTANCE_NAME` is the name of the replica instance.
  * `PRIMARY_INSTANCE_NAME` is the name of the primary instance.
  * `DATABASE_VERSION` is the database version of the instance. For example, `MYSQL_8_0_31`.
  * `TIER` is the machine type you want to use for the replica instance. For example, `db-perf-optimized-N-4`. For more information, see [Custom instance configurations](https://docs.cloud.google.com/sql/docs/mysql/create-instance#machine-types).
  * `EDITION` is the edition you want to use for the replica instance. For example, `ENTERPRISE_PLUS`. For more information, see [Create an instance](https://docs.cloud.google.com/sql/docs/mysql/create-instance#gcloud).
  * `REGION` is the region you want to use for the replica instance. For example, `us-central1`.
  * `PASSWORD` is the root password for the instance.
  * `REPLICATION_LAG_MAX_SECONDS` is the maximum acceptable replication lag or delay in seconds. For example, `600`. The minimum acceptable value is 300 seconds or five minutes. The maximum acceptable value is 31,536,000 seconds or one year.



###  REST API 

The `replicationLagMaxSeconds` field is located in the [`DatabaseInstance`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances) resource. Add this field to the request body:
    
    
    {
      "settings": {
      "replicationLagMaxSeconds" :REPLICATION_LAG_MAX_SECONDS,
      }
      ...
    }

Where:

  * `REPLICATION_LAG_MAX_SECONDS` is the maximum acceptable replication lag or delay in seconds. For example, `600`.



### Update the recreate timeframe for replication lag

To view an instance's settings, use any of the methods described in [View instance summary information](https://docs.cloud.google.com/sql/docs/mysql/instance-info#gcloud).

With this information, you can choose whether or not to update the replication lag timeframe you specified as being acceptable before the replica is recreated.

###  gcloud 

Use the [`gcloud sql instances patch`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) command to update the timeframe for recreating the instance based on replication lag:
    
    
    gcloud beta sql instances patch INSTANCE_NAME \
      --replication-lag-max-seconds-for-recreate=REPLICATION_LAG_MAX_SECONDS

Where:

  * `INSTANCE_NAME` is the name of the instance.
  * `REPLICATION_LAG_MAX_SECONDS` is the maximum acceptable replication lag or delay in seconds. For example, `700`. If you want to revert to the default value of one year, enter `31536000`. The minimum acceptable value is 300 seconds or five minutes. The maximum acceptable value is 31,536,000 seconds or one year.



###  REST API 

The policy can be updated using the [`instances.patch`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch) and [`instance.insert`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert).

To see an example of how to update the setting using the REST API, see [Edit an instance](https://docs.cloud.google.com/sql/docs/mysql/edit-instance#rest-v1).

### Limitations

The following limitations apply to recreating lagging replicas:

  * Values for `replicationLagMaxSeconds` can only be set in seconds.
  * [Indexes](https://docs.cloud.google.com/sql/docs/mysql/replication/read-replica-indexes) created on the read replica prior to a recreate operation won't persist. If an index exists, then create a secondary index after the replica is recreated.
  * To avoid frequent downtimes on read replicas, recreations are limited to one per day per instance.
  * Replicas of external servers are not supported with this feature.
  * If you enable recreation of lagging replicas on a cascading replica, then Cloud SQL recreates the leaf replicas first in order to maintain replication consistency.
  * Recreating a cross-region replica incurs additional [cost](https://docs.cloud.google.com/sql/docs/mysql/replication#billing).
  * You can't enable recreation of lagging replicas in the Google Cloud console.



## What's next:

  * [Promote replicas for regional migration or disaster recovery](https://docs.cloud.google.com/sql/docs/mysql/replication/cross-region-replicas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
