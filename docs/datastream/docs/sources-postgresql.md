---
url: https://docs.cloud.google.com/datastream/docs/sources-postgresql/
title: Stream data from PostgreSQL databases \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:49.004479+00:00
---

# Stream data from PostgreSQL databases  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/sources-postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream data from PostgreSQL databases Stay organized with collections  Save and categorize content based on your preferences. 

This section contains information about:

  * The behavior of how Datastream handles data that's being pulled from a source PostgreSQL database
  * The versions of PostgreSQL database that Datastream supports
  * An overview of how to setup a source PostgreSQL database so that data can be streamed from it to a destination
  * Known limitations for using PostgreSQL database as a source



## Behavior

The source PostgreSQL database relies upon its [logical decoding](https://www.postgresql.org/docs/current/logicaldecoding-explanation.html) feature. Logical decoding exposes all changes committed to the database and allows consuming and processing these changes in a user-friendly format using an output plugin. Datastream uses the `pgoutput` plugin, which is the standard PostgreSQL logical decoding plugin for PostgreSQL 10 and later.

  * All schemas or specific schemas from a given PostgreSQL source, as well as all tables from the schema or specific tables, can be selected.
  * All historical data is replicated.
  * All data manipulation language (DML) changes, such as inserts, updates, and deletes from the specified databases and tables, are replicated.
  * Only committed changes are replicated.
  * If you define a [REPLICA IDENTITY](https://www.postgresql.org/docs/current/sql-altertable.html#SQL-ALTERTABLE-REPLICA-IDENTITY) on a table, Datastream treats the specified columns as primary keys.
  * Datastream periodically sends heartbeat messages to the source database when it's connected to a primary instance. As a result, logical decoding message events (`op:"m"`) are inserted directly into the WAL file. These messages are required by Datastream to ensure source availability and to calculate freshness. When you use a read replica as a source, you must configure heartbeat messages externally. See Replication from read replicas for more information. We recommend taking that into consideration if other replication setups read from the same source database.



## Versions

Datastream supports PostgreSQL version 10 and later.

Datastream supports the following types of PostgreSQL database:

  * Self-hosted PostgreSQL
  * Cloud SQL for PostgreSQL
  * AlloyDB for PostgreSQL
  * AlloyDB Omni
  * Amazon RDS for PostgreSQL
  * Amazon Aurora PostgreSQL



## Free Tier

Datastream lets you stream from AlloyDB for PostgreSQL to BigQuery using the Free Tier, providing up to 100 GiB of change data capture data free every month. For more information, see [Datastream pricing](https://cloud.google.com/datastream/pricing).

## Best practices

This section describes recommended best practices for configuring your PostgreSQL source for use with Datastream.

### Use multiple streams to prevent head-of-line blocking

For PostgreSQL sources, Datastream uses a single logical replication slot for an entire stream. A large transaction or multiple updates on one high-volume table can delay data replication for all other tables in the same stream.

To prevent head-of-line blocking, create separate streams for different sets of tables. For example, you can create one stream for high-volume tables, and another stream for low-volume tables. This isolates high-churn tables and prevents them from delaying replication for other tables.

**Recommendation:** identify tables with exceptionally high write (`INSERT`/`UPDATE`/`DELETE`) rates and place them in their own dedicated Datastream stream with a separate replication slot.

### Avoid long-running transactions

Long-running transactions can lead to WAL log buildup. Because WAL is sequential, PostgreSQL can't remove old WAL files needed by the replication slot until the long transaction completes. This increases the WAL disk usage.

Furthermore, this can slow down logical decoding. The slowdown is caused by large transactions spilling changes to disk, which then requires slow, I/O-intensive reassembly upon commit, blocking the replication of all subsequent transactions. **Recommendation:** on the source database, configure the `statement_timeout` and `idle_in_transaction_session_timeout` parameters to avoid long-running transactions. For more information, see the [PostgreSQL documentation](https://www.postgresql.org/docs/current/runtime-config-client.html).

### Use table filtering when creating publications

If you're replicating changes from only a few tables, ensure that you create a `PUBLICATION` that includes only those tables. When a publication is scoped to specific tables, PostgreSQL efficiently persists changes only for those tables in the replication slot. This helps reduce the size of the replication slot and improves logical decoding performance.

### Proactively manage replication slots

Datastream uses a logical replication slot on your PostgreSQL primary instance, which ensures that WAL files are retained until Datastream confirms that they've been processed. If a stream fails, is paused or deleted without dropping the replication slot, PostgreSQL continues to retain WAL files indefinitely. This can fill up your database server disk and lead to a production outage.

**Recommendation:** Set up efficient alerting and monitor WAL disk usage on your source PostgreSQL server.

### Configure replica identity correctly

The `REPLICA IDENTITY` setting tells PostgreSQL what data to write to the WAL for `UPDATE` and `DELETE` events, allowing Datastream to identify which rows were changed.

If you use BigQuery as a destination, avoid setting `REPLICA IDENTITY` to `FULL`. Datastream uses the logged columns as a logical key for BigQuery `MERGE` operations. If `REPLICA IDENTITY` is set to `FULL` and a table has more than 16 columns, this exceeds the BigQuery 16-column limit for primary keys in `MERGE` operations and breaks the stream.

**Recommendations** (in order of preference):

  1. **Best:** use a primary key. The default setting of `REPLICA IDENTITY DEFAULT` automatically and efficiently uses the existing primary key.
  2. **Good:** if no primary key exists, create a `UNIQUE NOT NULL` index and set `REPLICA IDENTITY USING INDEX INDEX_NAME`.
  3. **Least recommended:** only use the `REPLICA IDENTITY FULL` setting on tables with no unique identifier. Be aware of the performance impact and the 16-column limit and the restriction on supported data types for primary keys if replicating to BigQuery.



## Replication from read replicas

Datastream supports replication from PostgreSQL read replica instances for PostgreSQL version 16 and later.

To replicate from a read replica, you must perform the following setup steps on the primary instance:

  1. **Create publications on the primary instance** : While Datastream connects to the read replica, the publications that define the data to be replicated must be created on the primary instance.
  2. **Configure WAL heartbeats** : Datastream relies on periodic WAL heartbeat messages for its checkpointing mechanism. When connecting to a primary instance, Datastream handles the generation of these heartbeats. However, for a read replica, these heartbeats must be generated externally.



One way to set up periodic heartbeats is to create a cron task in PostgreSQL using the `pg_cron` extension:
    
    
    SELECT cron.schedule_in_database(
        'datastream-heartbeat',             -- Job name
        '* * * * *',                        -- Every minute
        $$SELECT pg_logical_emit_message(true, 'datastream', 'cdc heartbeat')$$,
        'DATABASE_NAME',              -- Change this to your database name
        'USERNAME',                   -- Username to run as
        true                                -- Enabled
    );
    

Replace the following:

  * DATABASE_NAME: The name of the database for which you want to generate heartbeats.
  * USERNAME: The name of the user to run the task as. Typically `postgres`.



## Known limitations

**Note:** This section describes limitations for using Datastream with a PostgreSQL database as a source. In addition to these limitations, you need to familiarize yourself with PostgreSQL logical replication limitations, because they also affect how Datastream streams data from a PostgreSQL source. To learn about limitations of PostgreSQL logical replication, see [logical replication restrictions](https://www.postgresql.org/docs/10/logical-replication-restrictions.html).

Known limitations for using Datastream with a PostgreSQL database as a source include:

  * Streams are limited to 10,000 tables.
  * PostgreSQL strictly rejects NULL bytes (`0x00`) in UTF-8 string columns. Datastream doesn't strip NULL bytes. If a source string contains `0x00` null bytes, the insert batch fails and stops replication. We recommend that you clean or replace `CHAR(0)` characters on the source database before replicating.
  * You can't configure PostgreSQL streams to start from the most recent position.
  * A table that has more than 500 million rows can't be backfilled unless the following conditions are met: 
    1. The table has a unique B-tree index.
    2. The index doesn't include columns of the following types: `DOUBLE`, `FLOAT`, `MONEY`, `REAL`, `JSON`, `JSONB`, `BYTEA`, `TXID`, `XML`, [composite data types](https://www.postgresql.org/docs/current/rowtypes.html#ROWTYPES) or [geometric data types](https://www.postgresql.org/docs/current/datatype-geometric.html).
    3. None of the columns of the index are nullable.
    4. All columns of the index are in ascending order, or all columns of the index are in descending order.
    5. All columns of the index are included in the stream.
  * Tables without primary keys must have a [REPLICA IDENTITY](https://www.postgresql.org/docs/current/sql-altertable.html#SQL-CREATETABLE-REPLICA-IDENTITY). Otherwise, only `INSERT` events are replicated to the destination.
  * Tables with primary keys can't have the [REPLICA IDENTITY](https://www.postgresql.org/docs/current/sql-altertable.html#SQL-CREATETABLE-REPLICA-IDENTITY) set to `FULL` or `NOTHING`. It has to be set to `DEFAULT`.
  * Not all changes to the source schema can be detected automatically, in which case data corruption may occur. The following schema changes may cause data corruption or failure to process the events downstream: 
    * Dropping columns.
    * Adding columns to the middle of a table.
    * Changing the data type of a column.
    * Reordering columns.
    * Dropping tables (relevant if the same table is then recreated with new data added).
  * Datastream doesn't support columns of the [`geometric`](https://www.postgresql.org/docs/current/datatype-geometric.html) data types, such as `BOX`, `CIRCLE`, `LINE`, `LSEG`, `PATH`, `POINT`, and `POLYGON`. Such columns are replicated as `NULL`.
  * Datastream doesn't support columns of the [`range`](https://www.postgresql.org/docs/current/rangetypes.html) data types.
  * Datastream doesn't support arrays of unsupported data types (such as spatial types), arrays of `LTREE`, arrays of [user-defined](https://www.postgresql.org/docs/15/xtypes.html) data types (including `ENUM`) or arrays of `DATE`, `TIMESTAMP`, or `TIMESTAMP WITH TIME ZONE` (`TIMESTAMPTZ`). Datastream ignores such columns during replication.
  * For streams created before February 17, 2026: Datastream doesn't support replicating UPDATE events for rows which include TOAST values in columns that are part of the table's replica identity. Such events are discarded. Streams created after that date aren't subject to this exception.
  * Datastream doesn't support replicating rows which include `JSON` or `JSONB` values with more than 2950 nested objects. Events containing such `JSON` or `JSONB` values aren't replicated to the destination database.
  * Datastream doesn't support replicating rows which include `NaN` values in `NUMERIC (precision, scale)` columns. The values in such columns are replaced with `NULL` values.
  * Datastream doesn't support replicating columns of the [hstore](https://www.postgresql.org/docs/current/hstore.html) data type. The values in such columns are replaced with `NULL` values.
  * Datastream doesn't support replicating non-ASCII records from a SQL_ASCII encoded source database. Such records are discarded.
  * Datastream doesn't support replicating tables with Row-Level Security (RLS) policies defined. For information about how to bypass this limitation, see [PostgreSQL source behavior and limitations](https://docs.cloud.google.com/datastream/docs/faq#postgresql-source).
  * **For streaming columns with variable-length data types that use The Oversized-Attribute Storage Technique (TOAST)** : If an unchanged TOAST value is dropped from the WAL log during an `UPDATE` operation, Datastream performs an active lookup on the source database in an attempt to recover the missing value. As such, intermediate changes might not be captured in scenarios involving rapid, back-to-back updates or a quick delete after an insert. Note that `DELETE` operations don't trigger this active lookup operation. This limitation for variable-length columns that use TOAST is particularly relevant when using the append-only write mode, which expects all intermediate changes to be captured.
  * Datastream doesn't capture changes made to [generated columns](https://www.postgresql.org/docs/current/ddl-generated-columns.html).
  * Datastream might stop working or not capture any new events when a PostgreSQL major version upgrade is performed on the database. We suggest you to drop the replication slots before the upgrade, then upgrade the database, and then recreate the replication slots. If the streams fail, recover the stream by specifying the new replication slot name, and perform a backfill if data consistency is required.
  * Datastream doesn't support replicating PostgreSQL system tables when using the [automated stream setup flow](https://docs.cloud.google.com/datastream/docs/create-a-stream-automated). If you edit the stream that you created using the automated flow and add system tables, Datastream silently ignores these tables, and doesn't replicate any data or changes from them.



## What's next

  * Learn how to [configure a PostgreSQL source](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database) for use with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
