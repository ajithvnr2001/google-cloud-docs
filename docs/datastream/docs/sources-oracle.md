---
url: https://docs.cloud.google.com/datastream/docs/sources-oracle/
title: Stream data from Oracle databases \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:03.425430+00:00
---

# Stream data from Oracle databases  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/sources-oracle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream data from Oracle databases Stay organized with collections  Save and categorize content based on your preferences. 

This section contains information about:

  * The behavior of how Datastream handles data that's being pulled from a source Oracle database
  * The versions of Oracle database that Datastream supports
  * An overview of how to setup a source Oracle database so that data can be streamed from it to a destination
  * Known limitations for using Oracle database as a source



## Behavior

Datastream supports two methods of extracting changes to the data from online redo log files: the Oracle binary log reader ([Preview](https://cloud.google.com/products/#product-launch-stages)) and the Oracle LogMiner.

With the binary log reader method ([Preview](https://cloud.google.com/products/#product-launch-stages)), the following behavior is observed:

  * If there's a read lag when extracting the changes from the online log files, Datastream extracts the changes from archived log files.

  * Datastream replicates only committed changes into the destination. Uncommitted or rolled back transactions aren't replicated.

  * The binary reader supports replicating Oracle `VARCHAR2` columns longer than 4000 characters.




Datastream also supports the [Oracle LogMiner](https://docs.oracle.com/en/database/oracle/oracle-database/18/sutil/oracle-logminer-utility.html#GUID-3417B738-374C-4EE3-B15C-3A66E01AE2B5) feature for exposing changes to the data. The method has the following behavior:

  * All schemas or specific schemas from a given database, as well as all tables from the schemas or specific tables, can be selected.
  * All historical data is replicated.
  * All data manipulation language (DML) changes, such as inserts, updates, and deletes from the specified databases and tables, are replicated.
  * Datastream replicates both committed and, in some cases, uncommitted changes into the destination. Datastream reads uncommitted changes. In case of a rollback, the Datastream output records also include the opposite operation. For example, if there's a rolled-back `INSERT` operation, then the output records will also contain a corresponding `DELETE` operation. In this case, the event will appear as a `DELETE` event with only the `ROWID`.



### `ROWID` based backfill

In Oracle, `ROWID` is a pseudocolumn that stores unique identifiers for rows in a table. Datastream uses the `ROWID` values for its backfill operations. Because of this, we recommend that you don't perform any actions that could change the `ROWID` values in your source Oracle database until the backfill operation completes.

The actions that can change the `ROWID` values include:

  * Physical movement of rows:

    * Export and import operations: when you export a table, and then you import it back, the physical location of rows might change, resulting in new `ROWID` values.
    * `ALTER TABLE (...) MOVE` command: moving a table to a different tablespace can change the physical storage and lead to `ROWID` changes.
    * `ALTER TABLE (...) SHRINK SPACE` command: this command compresses the table, potentially moving rows and affecting their `ROWID` values.
    * Partitioning operations: splitting, merging, or moving partitions can change the physical placement of rows and their `ROWID` values.
  * Flashback operations:

    * `FLASHBACK TABLE` command: restoring a table to a previous state involves deleting and re-inserting rows, thus creating new `ROWID` values.
    * `FLASHBACK_TRANSACTION_QUERY`: Similar to `FLASHBACK TABLE`. Rolling back a transaction can cause `ROWID` changes if rows were deleted or updated within the transaction.



### Troubleshoot Oracle 11.2.0.4 partition table backfill

If backfill fails for a partitioned table on Oracle 11.2.0.4 with an unexpected fetch error (index out of bounds), this is because of an Oracle metadata bug where queries to `ALL_OBJECTS` fail to return sub-partitions.

  * **Workaround** : temporarily revoke the `SELECT ON DBA_EXTENTS` privilege from the Datastream user (for example, `REVOKE SELECT ON sys.dba_extents FROM USER_NAME;`). This forces Datastream to use index-based backfilling, bypassing the metadata issue.



### Standby databases

When you use an Oracle Active Data Guard standby database as a source, Datastream reads the archived redo logs. To ensure that Datastream processes only redo logs that have been successfully applied to the standby database, you must filter standard Oracle views, such as `V$ARCHIVED_LOG` and `GV$ARCHIVED_LOG`, to include only records with the `APPLIED = 'YES'` filter.

You can accomplish this by creating custom views. Ensure that you grant the appropriate access to these views for your Datastream user. For example:
    
    
    CREATE OR REPLACE VIEW USER_NAME.local_v$archived_log AS 
    SELECT * FROM sys.v_$ARCHIVED_LOG
    WHERE RESETLOGS_CHANGE# = (SELECT resetlogs_change# FROM v$database)
      AND APPLIED = 'YES';
    
    CREATE OR REPLACE VIEW USER_NAME.local_gv$archived_log AS 
    SELECT * FROM sys.gv_$ARCHIVED_LOG
    WHERE RESETLOGS_CHANGE# = (SELECT resetlogs_change# FROM v$database)
      AND APPLIED = 'YES';
    
    CREATE SYNONYM USER_NAME.v$archived_log FOR USER_NAME.local_v$archived_log;
    CREATE SYNONYM USER_NAME.gv$archived_log FOR USER_NAME.local_gv$archived_log;
    

Using the `APPLIED = 'YES'` filter has an implication on data freshness. Datastream waits until the standby database's Managed Recovery Process (MRP) applies the logs and updates the `APPLIED` column to `YES` before extracting changes. If the MRP process is delayed or paused, for example, if you suspend the standby apply process, this directly impacts the freshness of the replicated data. Datastream enters a retry loop and delays processing until the newly applied archived logs become available.

This configuration is highly relevant when replicating tables that include large object (LOB) columns. For `UPDATE` operations, the detailed values of LOB columns aren't present in the redo logs; therefore, Datastream must query the database to fetch the associated row. If Datastream processes an unapplied redo log and tries to fetch the LOB value from the standby database, it might fetch an incorrect, outdated value. By filtering the logs to ensure they're fully applied first, Datastream retrieves the correct data.

## Versions

Datastream supports the following versions of Oracle database:

  * Oracle 11g, Version 11.2.0.4 (supported only with the Logminer CDC method)
  * Oracle 12c, Version 12.1.0.2
  * Oracle 12c, Version 12.2.0.1
  * Oracle 18c
  * Oracle 19c
  * Oracle 21c



Datastream supports the following types of Oracle database:

  * Self-hosted on-premises or on any cloud provider
  * Amazon RDS for Oracle
  * Oracle Cloud
  * Oracle Exadata
  * Oracle RAC
  * Oracle Active Data Guard standby database



## Setup

To set up a source Oracle database so that data from it can be streamed into a destination, you must configure the database to grant access, set up logging, and define a retention policy.

See [Configure a source Oracle database](https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database) to learn how to configure this database so that Datastream can pull data from it into a destination.

## Best practices

This section describes recommended best practices for configuring your Oracle source for use with Datastream.

### Case sensitivity for binary reader

When configuring an Oracle source with the binary reader CDC method and specifying directory names for redo and archive logs, be aware that the names are case-sensitive. Ensure that the directory names that you provide in the Datastream connection profile match the exact case of the directory names in your Oracle database.

### CDC concurrency

To minimize replication lag, ensure that Datastream can process redo logs as fast as your Oracle source creates them. When using the binary reader CDC method, the Datastream concurrency is at the redo log file level: each task defined by `maxConcurrentCdcTasks` processes one file at a time.

We recommend that you use the following methodology:

  * **Tune concurrency in Datastream:** Identify the average number of redo log switches during your peak business hours and configure the `maxConcurrentCdcTasks` parameter accordingly. For more information, see [Maximum number of CDC tasks](https://docs.cloud.google.com/datastream/docs/stream-concurrency-controls#maxcdctasks).
  * **Configure Oracle log switching:** Configure Oracle to switch logs frequently, for example, every 10-20 minutes. This creates a steady stream of smaller work units, allowing the Datastream concurrent tasks to work in parallel effectively.



We recommend that you optimize your settings so that there are enough concurrent tasks in Datastream to handle the frequent creation of smaller redo logs from Oracle. For more information, see [stream concurrency controls](https://docs.cloud.google.com/datastream/docs/stream-concurrency-controls).

## Known limitations

Known limitations for using Oracle database as a source include:

  * Streams are limited to 10,000 tables. If a stream includes more than 10,000 tables, then it might run into errors.
  * Datastream supports Oracle multi-tenant architecture (CDB/PDB), however, you can only replicate a single pluggable database in a stream.
  * Oracle Autonomous Database isn't supported.
  * For tables that don't have a primary key, Datastream uses the row's [`ROWID`](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/ROWID-Pseudocolumn.html) to perform a merge operation on the consumer side. Note that the `ROWID` might not be unique. If you delete and reinsert a row with [Oracle's Export/Import utility](https://docs.oracle.com/en/database/other-databases/nosql-database/21.2/admin/using-export-and-import-utilities.html), for example, then the row's `ROWID` might change. If you delete a row, then Oracle can reassign its `ROWID` to a new row inserted later.
  * Index-organized tables (IOTs) aren't supported.
  * Temporary tables aren't supported.
  * The following Oracle data types are **not supported** and aren't replicated. Columns of these types are replicated as `NULL` values in the destination: 
    * `ANYDATA`, `ANYDATASET`, `ANYTYPE`
    * `VARRAY` (Oracle Arrays)
    * `BFILE`, `BFILENAME`
    * `INTERVAL DAY TO SECOND`, `INTERVAL YEAR TO MONTH`
    * `LONG`, `LONG RAW`
    * `UROWID`
    * `UDT`
    * Media and spatial types: `ORDAUDIO`, `ORDDATASOURCE`, `ORDDICOM`, `ORDDOC`, `ORDIMAGE`, `ORDVIDEO`, `SDO_GEOMETRY` (and all other `MDSYS.SDO_*` types).
  * To stream columns of large object data types, such as `XMLTYPE`, binary large objects (`BLOB`), character large objects (`CLOB`) and national character large objects (`NCLOB`), you need to include the `streamLargeObjects` flag in your stream configuration. If you don't include the flag, Datastream doesn't stream such columns and they're replaced with `NULL` values in the destination. For more information, see [Enable streaming of large objects for Oracle sources](https://docs.cloud.google.com/datastream/docs/manage-streams#streamlargeobjects). When streaming these data types, Datastream must query the source database to fetch missing LOB values point-in-time (in an active lookup process called supplementation). This occurs in the following scenarios:

    * When unchanged LOB payloads are dropped from the redo log during an `UPDATE`
    * During any DML operations involving binary XML types
    * During any parsed DML on a table containing LOBs if the stream uses the LogMiner method

Because Datastream streams these columns by querying the database, intermediate changes might not be captured in scenarios involving rapid, back-to-back updates or a quick delete after an insert. Note that `DELETE` operations don't trigger supplementation. This limitation is particularly relevant when using the append-only write mode, which expects all intermediate changes to be captured.

  * For Oracle 11g, tables that have columns of data types `ANYDATA` or `UDT` aren't supported, and the entire table won't be replicated.

  * Oracle Label Security (OLS) isn't replicated.

  * Datastream periodically fetches the latest schema from the source as events are processed. If a schema changes, then some events from the new schema might be read while the old schema is still applied. In this case, Datastream detects the schema change, triggers a schema fetch, and reprocesses the failed events.

  * Not all changes to the source schema can be detected automatically, in which case data corruption may occur. The following schema changes may cause data corruption or failure to process the events downstream:

    * Dropping columns
    * Adding columns to the middle of a table
    * Changing the data type of a column
    * Reordering columns
    * Dropping tables (relevant if the same table is then recreated with new data added)
    * Truncating tables
  * Datastream doesn't support replicating views.

  * Datastream supports materialized views. However, new views created while the stream is running aren't backfilled automatically.

  * When using the Oracle LogMiner method, [`SAVEPOINT` statements](https://docs.oracle.com/cd/B19306_01/server.102/b14200/statements_10001.htm) aren't supported and can cause data discrepancy in case of a rollback.

  * When using the binary reader method, dynamically partitioned tables aren't supported.

  * When using the Oracle LogMiner method, Datastream doesn't support replicating tables and columns whose names exceed 30 characters.

  * Datastream supports the following character set encodings for Oracle databases:

    * `AL16UTF16`
    * `AL32UTF8`
    * `IN8ISCII`
    * `IW8ISO8859P8`
    * `JA16SJIS`
    * `JA16SJISTILDE`
    * `KO16MSWIN949`
    * `US7ASCII`
    * `UTF8`
    * `WE8ISO8859P1`
    * `WE8ISO8859P9`
    * `WE8ISO8859P15`
    * `WE8MSWIN1252`
    * `ZHT16BIG5`
  * Datastream doesn't support replicating zero date values. Such dates are replaced with `NULL` values.

  * Datastream doesn't support direct connectivity to databases using the Single Client Access Name (SCAN) feature in Oracle Real Application Clusters (RAC) environments. For information about potential solutions, see [Oracle source behavior and limitations](https://docs.cloud.google.com/datastream/docs/faq#oracle-source).

  * If the source is an Oracle Active Data Guard standby database, Datastream supports tablespace-level encryption only and doesn't support column-level encryption.




## Additional limitations when using the binary reader

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Supplemental logging and column name length**

Although Oracle 12.2+ supports column names of up to 128 characters, Oracle's internal redo writer enforces a 30-character limit when processing supplemental logging in active memory. If you use the binary reader CDC method and perform UPDATE operations on tables with column names exceeding 30 characters:

  * Oracle silently aborts supplemental logging for that row.
  * Datastream receives incomplete data. Unchanged columns, including primary keys, arrive at the destination as `NULL`.

**Recommendation** : Ensure that all column names in the replication scope are 30 characters or less, or exclude columns with names exceeding 30 characters from supplemental logging. 




  * The high-performance binary reader method is supported only for Oracle 12c and later. For Oracle 11g and earlier versions, you must use LogMiner.

  * Binary reader doesn't support the following features:

    * Transparent Database Encryption (TDE)
    * Hybrid Columnar Compression
    * Secure files
    * ASM isn't supported for Amazon RDS sources.
    * The binary reader CDC method doesn't support Oracle 11g and earlier versions.



## What's next

  * Learn how to [configure an Oracle source](https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database) for use with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
