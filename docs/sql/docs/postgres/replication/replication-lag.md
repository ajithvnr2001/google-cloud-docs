---
url: https://docs.cloud.google.com/sql/docs/postgres/replication/replication-lag/
title: Replication lag \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:50.285817+00:00
---

# Replication lag  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/replication/replication-lag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Replication lag Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-lag "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/replication/replication-lag "View this page for the SQL Server database engine")

This page describes how to troubleshoot and fix replication lag for Cloud SQL read replicas.

## Overview

Cloud SQL read replicas use [ PostgreSQL streaming replication](https://www.postgresql.org/docs/current/warm-standby.html#STREAMING-REPLICATION). Changes are written to Write-Ahead Log (WAL) in the primary instance. The WAL sender sends the WAL to the WAL receiver in the replica, where they are applied. 

Replication lag can happen in a few scenarios, such as:

  * The primary instance can't send the changes fast enough to the replica.
  * The replica can't receive the changes quickly enough.
  * The replica can't apply the changes quickly enough.

The first two listed scenarios can be monitored with the `network_lag` metric. The third is observed using the `replica_lag` metric. High `replica_lag` means that the replica can't apply replication changes fast enough. The total lag can be observed using the `replica_byte_lag` metric, which has labels to indicate further details. For more information about these metrics, see Monitor replication lag. 

## Ensure replica is adequately provisioned

A replica instance that is smaller than the primary instance (for example, with less vCPUs and memory) can experience replication lag. A smaller replica might also have different default configuration flags compared to a larger primary instance. We recommend that the replica instance is at least as large as the primary instance to have enough resources to handle the replication load.

High CPU utilization on the replica can also cause replication lag. If the replica's CPU utilization is high (for example, over 90%), consider increasing the replica's CPU capacity.

You can use the `SHOW ALL` command to see replica and primary instance configuration and compare them for differences. 

## Optimize queries and schema

This section suggests some common query and schema optimizations you can make to improve replication performance.

### Long-running queries in the read replica

Long-running queries in the replica might block replication for Cloud SQL. This can happen when replication is trying to apply changes (like from a `VACUUM` operation) to rows that are being read by a query on the replica.

You might want to have separate replicas for online transaction processing (OLTP) and online analytical processing (OLAP) purposes and only send long-running queries to the OLAP replica.

To help address replication delays or blockages caused by long-running transactions, we recommend the following: 

  * **Adjust standby delay flags.** The `max_standby_archive_delay` and `max_standby_streaming_delay` flags control how long a replica will wait before canceling standby queries that conflict with replication. Reasonable values are often around 30 to 60 seconds. You can check the `pg_stat_database_conflicts` view for insights about query conflicts. 
  * **Enable the`hot_standby_feedback` flag.** Setting the `hot_standby_feedback` flag to `on` in the replica can help by delaying vacuum operations on the primary. However, this can cause table bloat on the primary, so it's a trade-off. 



Review [ PostgreSQL documentation](https://www.postgresql.org/docs/current/hot-standby.html#HOT-STANDBY-CONFLICT) for more information.

### High network lag

High network lag indicates that WAL records are not being sent by the primary or received by the replica fast enough. This can be caused by the following: 

  * **Cross-region replication.** Replicating between different regions can introduce higher network latency.
  * **High primary CPU utilization.** If the primary's CPU is over 90%, the WAL sender process might not get enough CPU time. Consider reducing load on the primary or increasing its CPU.
  * **High replica CPU utilization.** If the replica's CPU is over 90%, the WAL receiver process might not get enough CPU time. Consider reducing load on the replica or increasing its CPU.
  * **Network bandwidth issues or disk I/O bottlenecks.** A closer region or a higher throughput disk configuration might help. Consider modifying the `wal_compression` flag value in the primary instance to help reduce cross-region traffic.

You can monitor network lag with the `cloudsql.googleapis.com/database/replication/network_lag` metric. This metric has a maximum limit of 25 seconds, even if the actual lag is higher. **Note:** Because `network_lag` is rounded up to the nearest second, a reported value of 1 second can represent an underlying lag of anything from a millisecond or two up to a full second.

This `network_lag` metric is similar to the `cloudsql.googleapis.com/database/postgresql/replication/replica_byte_lag` metric which measures the `sent_location` lag in terms of bytes indicated by its `replica_lag_type` label.

### Exclusive locks due to DDL

Data definition language (DDL) commands, such as `ALTER TABLE` and `CREATE INDEX`, can cause replication lag in the replica due to exclusive locks. To avoid lock contention, consider scheduling DDL execution during times when the query load is lower on the replicas.

Review [ PostgreSQL documentation](https://www.postgresql.org/docs/current/hot-standby.html#HOT-STANDBY-CONFLICT) for more information. 

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
(`cloudsql.googleapis.com/database/replication/replica_lag`) |  The number of seconds that the replica's state is lagging behind the state of the primary instance. This is the difference between the current time and the original timestamp at which the primary database committed the transaction that is currently being applied on the replica. In particular, writes might be counted as lagging even if they have been received by the replica, if the replica hasn't yet applied the write to the database. This metric is calculated using `now() - pg_last_xact_replay_timestamp()` in the replica. This is an approximation. If replication is broken, the replica won't know how far ahead the primary database is and this metric won't indicate total lag.  
Lag bytes  
(`cloudsql.googleapis.com/database/postgres/replication/replica_byte_lag`) |  The amount of bytes by which the replica's state is lagging behind the state of the primary database. `replica_byte_lag` exports 4 time series, and the `replica_lag_type` label can indicate any of the following:

  * **sent_location:** Indicates how many bytes of WAL have been generated, but haven't yet been sent to the replica.
  * **write_location:** Write minus sent lag shows WAL bytes in the network, that have been sent out but not yet written in the replica.
  * **flush_location:** Flush minus write lag shows WAL bytes written in the replica but not yet flushed in the replica.
  * **replay_location:** Shows total lag in bytes. Replay minus flush lag indicates replay delay.

  
Network lag  
(`cloudsql.googleapis.com/database/replication/network_lag`) |  The amount of time in, seconds that it takes from commit in the primary database to reach the WAL receiver in the replica. If the `network_lag` is zero, or negligible, but the `replica_lag` is high, it indicates that the WAL receiver is not able to apply replication changes fast enough. Because `network_lag` is rounded up to the nearest second, a reported value of 1 second can represent an underlying lag of anything from a millisecond or two up to a full second.  
  
## Verify replication

To verify that replication is working, run the following statement against the replica: 
    
    
      select status, last_msg_receipt_time from pg_stat_wal_receiver;
    

If replication is happening, you see the status `streaming` and a recent last_msg_receipt_time:
    
    
      postgres=> select status, last_msg_receipt_time from pg_stat_wal_receiver;
        status   |     last_msg_receipt_time
      -----------+-------------------------------
      streaming | 2020-01-21 20:19:51.461535+00
      (1 row)
    

If replication is not happening, an empty result is returned:
    
    
      postgres=> select status, last_msg_receipt_time from pg_stat_wal_receiver;
      status | last_msg_receipt_time
      --------+-----------------------
      (0 rows)
    

## What's next:

  * [Promote replicas for regional migration or disaster recovery](https://docs.cloud.google.com/sql/docs/postgres/replication/cross-region-replicas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
