---
url: https://docs.cloud.google.com/sql/docs/sqlserver/replication/replication-lag/
title: Replication lag \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:14.529121+00:00
---

# Replication lag  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/replication/replication-lag/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Replication lag Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/replication/replication-lag "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/replication/replication-lag "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to troubleshoot and fix replication lag for Cloud SQL read replicas.

## Overview

Cloud SQL read replicas use [SQL Server Always-On Availability Groups](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/overview-of-always-on-availability-groups-sql-server?view=sql-server-linux-ver15) for replication. Changes are written to the transaction log in the primary instance. The primary instance forwards transactions to any secondary replica instances, where the changes are applied. The availability mode used is [Asynchronous-commit mode](https://learn.microsoft.com/en-us/sql/database-engine/availability-groups/windows/availability-modes-always-on-availability-groups?view=sql-server-ver16#SupportedAvModes). 

Replication lag can happen in a few scenarios, such as:

  * The primary instance can't send the changes fast enough to the replica.
  * The replica can't receive the changes quickly enough.
  * The replica can't apply the changes quickly enough.

The first two listed scenarios can be monitored with the `network_lag metric`. For more information about the metric, see Monitor replication lag. 

## Ensure replica is adequately provisioned

A replica instance that is smaller than the primary instance (for example, with less vCPUs and memory) can experience replication lag. A smaller replica might also have different default configuration flags compared to a larger primary instance. We recommend that the replica instance is at least as large as the primary instance to have enough resources to handle the replication load.

High CPU utilization on the replica can also cause replication lag. If the replica's CPU utilization is high (for example, over 90%), consider increasing the replica's CPU capacity.

## Optimize queries and schema

This section suggests some common query and schema optimizations you can make to improve replication performance.

### Long-running queries in the read replica

Long-running queries in the replica might block replication for Cloud SQL. You might want to have separate replicas for online transaction processing (OLTP) and online analytical processing (OLAP) purposes and only send long-running queries to the OLAP replica. 

### Exclusive locks due to DDL

Data definition language (DDL) commands, such as `ALTER TABLE` and `CREATE INDEX`, can cause replication lag in the replica due to exclusive locks. To avoid lock contention, consider scheduling DDL execution during times when the query load is lower on the replicas.

Additionally, DDL statements such as `CREATE INDEX`, `ALTER INDEX`, and `INDEX MAINTENANCE` can cause replication lag due to the large number of transaction log records that these statements can generate. 

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
Network lag  
(`cloudsql.googleapis.com/database/replication/network_lag`) |  The difference between the timestamp of the last received log entry on the replica and the last sent log entry on the primary. Because `network_lag` is rounded up to the nearest second, a reported value of 1 second can represent an underlying lag of anything from a millisecond or two up to a full second.  
  
## Verify replication

To verify that replication is working, check the value of the `cloudsql.googleapis.com/database/replication/state` metric on the primary instance. If the state is `Running`, then replication is healthy. 

## What's next:

  * [Promote replicas for regional migration or disaster recovery](https://docs.cloud.google.com/sql/docs/sqlserver/replication/cross-region-replicas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
