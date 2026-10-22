---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/replication-isolation-levels/
title: Isolation levels in replication \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:59.157939+00:00
---

# Isolation levels in replication  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/replication-isolation-levels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Isolation levels in replication Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable _transaction isolation_ in Microsoft SQL Server and MySQL database snapshots in Cloud Data Fusion replication jobs.

When you set up a replication job for a database, the job takes an initial snapshot of the source tables. To ensure data consistency, place locks on those tables.

After the initial snapshot, incremental changes at the source are captured and applied to the BigQuery target as part of the ongoing replication process.

### SQL Server

To capture changes in the source tables in a SQL Server database, the replication job uses a Debezium connector. During the [`snapshotting`](https://docs.cloud.google.com/data-fusion/docs/concepts/replication#table_states) phase, Debezium acquires locks according to the configured [`snapshot.isolation.mode`](https://debezium.io/documentation/reference/1.3/connectors/sqlserver.html#sqlserver-property-snapshot-isolation-mode).

The following table compares the supported isolation modes for replication jobs.

Isolation mode | Acquired locks | Data consistency  
---|---|---  
`read_uncommitted` | None | No.  
`read_committed` | Shared locks on a batch of rows at a time | Partial. An added record can appear twice: once in the initial snapshot and once in the streaming phase.  
`repeatable_read`  
(default) | Shared locks on all rows | Partial. An added record can appear twice: once in the initial snapshot and once in the streaming phase.  
`snapshot` | None | Full.  
`exclusive` | Exclusive lock on all tables | Full.  
  
For more information about isolation modes, see [Set transaction isolation level](https://learn.microsoft.com/en-us/sql/t-sql/statements/set-transaction-isolation-level-transact-sql).

By default, the snapshot isolation mode is `repeatable_read`. This mode takes shared locks on all data that's read during the snapshotting phase. It prevents other transactions from modifying the existing rows, and can potentially allow insertion of new records (see [lock escalation](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide?view=sql-server-ver16#lock-escalation)).

Replication with snapshot isolation is recommended if it's already enabled on the source database because it provides full data consistency without locking the tables. If it's not enabled, learn more about the impact of [row versioning-based isolation levels in the SQL Server Database Engine](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide#Row_versioning) before you enable it.

As an alternative, use the `read_committed` isolation mode, which doesn't lock the tables during the snapshotting phase.

**Warning:** If you use `read_committed` mode, ensure that no schema changes are applied on the database during the snapshotting phase, as it may cause data inconsistency in replication.

## Enable snapshot isolation in a replication job

  1. Enable snapshot isolation in the SQL Server database:
         
         ALTER DATABASE DATABASE_NAME
         SET ALLOW_SNAPSHOT_ISOLATION ON
         

Replace `DATABASE_NAME` with the name of the SQL Server database.

  2. Set the runtime argument `snapshot.isolation.mode` to `snapshot`. For more information, see [Pass a runtime argument to a replication job](https://docs.cloud.google.com/data-fusion/docs/how-to/pass-runtime-args-in-replication).




### MySQL

To capture changes in the source tables in a MySQL database, the replication job uses a Debezium connector. During the [`snapshotting`](https://docs.cloud.google.com/data-fusion/docs/concepts/replication#table_states) phase, Debezium acquires locks according to the configured [`snapshot.locking.mode`](https://debezium.io/documentation/reference/1.3/connectors/mysql.html#mysql-property-snapshot-locking-mode).

By default, the snapshot locking mode is `minimal`. In this mode, the connector holds the global read lock for the initial portion of the snapshot as it reads the database schemas and other metadata. Then the connector fetches all rows through a consistent read, using the `REPEATABLE READ` transaction, which doesn't lock the tables.

To prevent any locks, set the mode to `none`.

**Warning:** If you use `none`, ensure that no schema changes are applied on the database during the snapshotting phase, as it may cause data inconsistency in replication.

As an alternative, to prevent locks on MySQL databases running on Cloud SQL, replicate from the [Replica](https://debezium.io/documentation/reference/1.3/connectors/mysql.html#mysql-supported-topologies_debezium) instead of the transactional database.

## Change the locking behavior during the snapshot for MySQL

  * To change snapshot locking behavior in the MySQL database, set the runtime argument, `snapshot.locking.mode` property, to an appropriate [locking mode](https://debezium.io/documentation/reference/1.3/connectors/mysql.html#mysql-property-snapshot-locking-mode) value.

**Note:** Tables defined with the MyISAM engine continue to be locked despite the property being set to `none`.

For more information, see [Pass a Debezium argument to a replication job](https://docs.cloud.google.com/data-fusion/docs/how-to/pass-runtime-args-in-replication#debezium-arguments).

## Limitations

  * Replication in Cloud Data Fusion supports Debezium Connector version 1.3.



## Oracle sources in Cloud Data Fusion

Replication from Oracle sources in Cloud Data Fusion is powered by Datastream. Datastream [doesn't lock tables](https://docs.cloud.google.com/datastream/docs/faq#general-source).

## What's next

  * Learn more about [Replication](https://docs.cloud.google.com/data-fusion/docs/concepts/replication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
