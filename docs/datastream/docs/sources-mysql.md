---
url: https://docs.cloud.google.com/datastream/docs/sources-mysql/
title: Stream data from MySQL databases \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:03.255706+00:00
---

# Stream data from MySQL databases  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/sources-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream data from MySQL databases Stay organized with collections  Save and categorize content based on your preferences. 

This section contains information about:

  * The behavior of how Datastream handles data that's being pulled from a source MySQL database
  * The versions of MySQL database that Datastream supports
  * Known limitations for using MySQL database as a source
  * An overview of how to setup a source MySQL database so that data can be streamed from it to a destination



## Behavior

This section describes the behavior of MySQL sources when you replicate data using Datastream. When you ingest data from MySQL databases, you can use binlog-based replication or global transaction identifier (GTID)-based replication. You select your CDC method when you [create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream).

### Binlog-based replication

Datastream can use [binary log](https://dev.mysql.com/doc/refman/5.6/en/binary-log.html) files to keep a record of data changes in MySQL databases. The information contained in these log files is then replicated to the destination to reproduce the changes made on the source.

The key characteristics of binlog-based replication in Datastream are:

  * All databases or specific databases from a given MySQL source, as well as all tables from the databases or specific tables, can be selected.
  * All historical data is replicated.
  * All data manipulation language (DML) changes, such as inserts, updates, and deletes from the specified databases and tables, are replicated.
  * Only committed changes are replicated.



### Global transaction identifier (GTID)-based replication

Use GTID-based replication for seamless failover support on high availability setups.

Datastream also supports global identifier (GTID)-based replication.

Global transaction identifier (GTID) is a unique identifier created and associated with each transaction committed on a MySQL source. This identifier is unique not only to the source on which it originated, but also across all servers in a given replication topology, as opposed to the binary log-based replication where each node in the database cluster maintains its own binlog files, with its own numbering. Maintaining separate binlog files and numbering might become an issue in the event of a failure or planned downtime, because the binlog continuity is broken and the binlog-based replication fails.

GTID-based replication supports failovers, self-managed database clusters, and continues to work irrespective of changes in the database cluster.

The key characteristics of GTID-based replication in Datastream are:

  * All databases or specific databases from a given MySQL source, as well as all tables from the databases or specific tables, can be selected.
  * All historical data is replicated.
  * All data manipulation language (DML) changes, such as inserts, updates, and deletes from the specified databases and tables, are replicated.
  * Only committed changes are replicated.
  * Seamless support for failovers.



### Switch from binlog-based to GTID-based replication

If you want to update your stream and switch from binlog-based to GTID-based replication without the need to do a backfill, perform the following steps:

**Note:** These steps require database downtime. Similar steps might also be useful when you want to upgrade the major version of your MySQL source.

  1. Ensure that all requirements for GTID-based replication are satisfied. For more information, see [Configure a source MySQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-mysql-database).
  2. Optionally, create and run a _test_ GTID-based stream. For more information, see [Create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#expandable-2).
  3. Create a GTID-based stream. Don't start it yet.
  4. Stop application traffic to the source database.
  5. Pause the existing binlog-based stream. For more information, see [Pause the stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#pauseastream).
  6. Wait for a few minutes to ensure that Datastream has caught up with the database. You can check this using the metrics in the **Monitoring** tab, on the **Stream details** page for your stream. The values for _Data freshness_ and _Throughput_ need to be `0`.
  7. Start the GTID-based stream. For more information, see [Start the stream](https://docs.cloud.google.com/datastream/docs/run-a-stream#startstream).
  8. Resume traffic to the source database.



If performing a backfill isn't an issue, you can truncate your tables in BigQuery, delete the old stream, and start a new one with backfill. For more information about managing backfill, see [Manage backfill for the objects of a stream](https://docs.cloud.google.com/datastream/docs/manage-backfill-for-the-objects-of-a-stream).

## Versions

Datastream supports the following versions of MySQL database:

  * MySQL 5.6
  * MySQL 5.7
  * MySQL 8.0
  * MySQL 8.4 (supported only for GTID-based replication)

Global transaction identifier (GTID)-based replication is only supported for versions 5.7 and later.



Datastream supports the following types of MySQL database:

  * [Self-hosted MySQL](https://docs.cloud.google.com/datastream/docs/configure-self-managed-mysql)
  * [Cloud SQL for MySQL](https://docs.cloud.google.com/datastream/docs/configure-cloudsql-mysql) Cloud SQL for MySQL Enterprise Plus sources are supported when using the GTID-based replication.
  * [Amazon RDS for MySQL](https://docs.cloud.google.com/datastream/docs/configure-amazon-rds-mysql)
  * [Amazon Aurora MySQL](https://docs.cloud.google.com/datastream/docs/configure-amazon-aurora-mysql)
  * [MariaDB](https://docs.cloud.google.com/datastream/docs/configure-self-managed-mysql)
  * [Alibaba Cloud PolarDB](https://docs.cloud.google.com/datastream/docs/configure-self-managed-mysql)
  * [Percona Server for MySQL](https://docs.cloud.google.com/datastream/docs/configure-self-managed-mysql)



## Best practices

This section describes recommended best practices for configuring your MySQL source for use with Datastream.

### Use GTID for high availability setups

If your production MySQL source uses replicas or any other high availability configuration, use GTID-based replication.

Binlog file and position-based replication can break during a database failover because when the primary fails, the new primary has a different binlog history. In such a case, Datastream loses its position and it can't resume.

GTID assigns a unique ID to every transaction across your entire replication topology (primary and replicas). After a failover, Datastream can resume from the last GTID logged on the new primary, without needing to know the binlog file or the position.

**Recommendation:** for any production MySQL source with a replica or high availability configuration, using the GTID CDC method is mandatory for resilient and reliable data replication.

### Properly size your read replica

If you configure Datastream to replicate from a read replica, you can encounter a _double lag_ , which is a combination of MySQL replication lag (from primary to replica) and Datastream replication lag (from replica to destination). Read replicas are often provisioned with fewer resources (CPU, RAM, IOPS) than primaries to save costs, which can cause them to lag behind the primary during high-write periods.

**Recommendation:** when using a read replica as a source for Datastream, provision it with resources comparable to the primary, so that the replica can keep up with the primary's write throughput.

### Increase throughput for the binlog CDC method

If you are using binlog-based replication and experience high latency due to large source write volumes generating binlog files faster than a single task can process, increase throughput by tuning the `maxConcurrentCdcTasks` parameter. This parameter controls the number of CDC tasks a stream runs in parallel. Increasing the value for this parameter allows Datastream to process more binlog files concurrently.

**Recommendation:** To determine the appropriate value for data freshness, monitor your MySQL server's binlog generation rate during peak hours. You can do this by observing the rate at which new binlog files are created and rotated in the MySQL data directory, or by using MySQL monitoring tools to track the growth of binary logs. If, for example, your source generates 10 binlog files per minute during peak times, setting `maxConcurrentCdcTasks` to a value like `10-15` allows Datastream to process these files in parallel, preventing a backlog.

You can increase `maxConcurrentCdcTasks` up to the maximum supported value of 50, provided that the load on the source database remains under control. For more information, see [Stream concurrency controls](https://docs.cloud.google.com/datastream/docs/stream-concurrency-controls).

### Correctly size the `max_allowed_packet` parameter

The default `max_allowed_packet` setting in MySQL (for example, 16MB-64MB) might be too small. If a single row with large `BLOB`, `JSON`, or `TEXT` type fields, or a single large transaction exceeds this size, MySQL terminates the Datastream connection, causing the stream to fail with errors such as `Packet for query is too large` or `Got a packet bigger than 'max_allowed_packet' bytes`.

**Recommendation:** set the `max_allowed_packet` parameter on your MySQL server to its maximum allowed value of 1G. This ensures that the server can handle any large row or transaction that Datastream needs to read from the binlog.

## Known limitations

Known limitations for using MySQL database as a source include:

  * Streams are limited to 10,000 tables.
  * Replicated tables must use the `InnoDB` storage engine. Tables using the `MyISAM` storage engine aren't supported and fail stream validation.
  * Tables that have a primary key defined as `INVISIBLE` can't be backfilled.
  * A table that has more than 500 million rows can't be backfilled unless the following conditions are met: 
    1. The table has a unique index.
    2. None of the columns of the index are nullable.
    3. The index isn't [descending](https://dev.mysql.com/doc/refman/8.0/en/descending-indexes.html).
    4. All columns of the index are included in the stream.
  * Datastream periodically fetches the latest schema from the source as events are processed. If a schema changes, Datastream detects the schema change and triggers a schema fetch. However, some events might get processed incorrectly or get dropped between the schema fetches, which can cause data discrepancies.
  * Not all changes to the source schema can be detected automatically, in which case data corruption may occur. The following schema changes may cause data corruption or failure to process the events downstream: 
    * Dropping columns
    * Adding columns to the middle of a table
    * Changing the data type of a column
    * Reordering columns
    * Dropping tables (relevant if the same table is then recreated with new data added)
    * Truncating tables
  * Datastream doesn't support replicating views.
  * Datastream doesn't support columns of [spatial data types](https://dev.mysql.com/doc/refman/8.0/en/spatial-type-overview.html), for example, `GEOMETRY`, `POINT`, `LINESTRING`, `POLYGON`. The values in these columns are replaced with `NULL` values.
  * Datastream doesn't support the zero value (`0000-00-00 00:00:00`) in columns of the `DATETIME`, `DATE`, or `TIMESTAMP` data types. The zero value is replaced with the `NULL` value.
  * Datastream doesn't support replicating rows which include the following values in `JSON` columns: `DECIMAL`, `NEWDECIMAL`, `TIME`, `TIME2` `DATETIME`, `DATETIME2`, `DATE`, `TIMESTAMP` or `TIMESTAMP2`. Events containing such values are discarded.
  * Datastream doesn't support [binary log transaction compression](https://dev.mysql.com/doc/refman/8.0/en/binary-log-transaction-compression.html).
  * Datastream doesn't support binary log files larger than 4 GiB. Because MySQL writes each transaction to a single binary log file, keep individual transactions under 4 GiB so that binary log files don't exceed this limit.
  * Datastream doesn't support SSL certificate chains in the source MySQL connection profiles. Only single, x509 PEM-encoded certificates are supported.
  * Datastream doesn't support cascading operations: `ON UPDATE CASCADE` and `ON DELETE CASCADE`. Such events aren't written to the binary log, and as a result, aren't propagated to the destination. As a workaround, you can replace cascading operations with database triggers.
  * Datastream doesn't support `DROP PARTITION` operations. Such operations are metadata only operations and aren't replicated. Other events aren't affected and the stream runs successfully.
  * You might experience connectivity issues when replicating `FEDERATED` tables. If that happens, remove all `FEDERATED` tables from the source database configuration and increase the values for `connect_timeout`, `net_read_timeout` and `max_allowed_packet` parameters to mitigate timeout issues during backfill.
  * Cloud SQL Enterprise Plus instances must use GTID-based replication because they are subject to [near-zero downtime maintenance](https://docs.cloud.google.com/sql/docs/mysql/maintenance#nearzero). Binary log-based replication breaks on failovers, hence we recommend using GTID-based replication for high availability use cases.
  * For MySQL versions 8.0 and later, the `binlog_row_value_options` variable must be set to an empty value. This is the default for most versions, but for some, for example MySQL sources on Oracle Cloud Infrastructure (OCI), you must set it explicitly. For more information, see [Configure a self-managed MySQL database](https://docs.cloud.google.com/datastream/docs/configure-self-managed-mysql).
  * **MariaDB limitations:**
    * GTID-based replication is **not** supported for MariaDB. You must configure MariaDB streams to use binlog-based replication.
    * For MariaDB versions 11.4 to 12.2, you must enable the `binlog_legacy_event_pos` system variable on the source database to ensure compatibility with Datastream.
    * Datastream doesn't support the `UUID` data type (introduced in MariaDB 10.7). You must exclude columns of the `UUID` data type from the stream configuration.



## Additional limitations for the GTID-based replication

  * Recovering streams that use GTID-based replication is only available when using the Datastream API.
  * Creating tables from other tables using the `CREATE TABLE ... SELECT` statements isn't supported.
  * Datastream doesn't support tagged GTIDs.
  * For MySQL restrictions that apply to GTID-based replication, see [MySQL documentation](https://dev.mysql.com/doc/mysql-replication-excerpt/5.7/en/replication-gtids-restrictions.html).



## What's next

  * Learn how to [configure a MySQL source](https://docs.cloud.google.com/datastream/docs/configure-your-source-mysql-database) for use with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
