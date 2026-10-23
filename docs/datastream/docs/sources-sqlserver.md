---
url: https://docs.cloud.google.com/datastream/docs/sources-sqlserver/
title: Stream data from SQL Server databases \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:30.987678+00:00
---

# Stream data from SQL Server databases  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/sources-sqlserver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream data from SQL Server databases Stay organized with collections  Save and categorize content based on your preferences. 

To keep your analytics and downstream databases synchronized, you can use Datastream to replicate historical data and ongoing changes from a SQL Server database.

For SQL Server sources in Datastream, review the replication behavior and change data capture (CDC) methods, supported versions and editions, and known limitations.

## Behavior

Datastream tracks data manipulation language (DML) changes using one of the following CDC methods:

  * Change tables
  * Transaction logs



### Change tables

The change tables CDC method lets users retain logs for a shorter time, and thus save storage space, but supports lower throughput compared to the transaction logs method. The method has fewer limitations than transaction logs. For example, it eliminates the risk of log truncation leading to streams failing permanently, and supports replication of encrypted tables. For more information, see Known limitations.

When using this CDC method, changes to the source are tracked using dedicated change tables. Transaction logs are still used, but to a limited extent, and you don't need to retain them for longer periods. As DML events are applied to the source tables, the changes are replicated to the corresponding change tables. The change tables have the same structure as the source tables, but with extra columns to include the metadata for the changes. Only committed transactions are added to the change tables, along with the log sequence number (LSN) of the commit operation.

**Note:** When a stream starts, Datastream selects the latest [capture instance](https://learn.microsoft.com/en-us/sql/relational-databases/system-tables/cdc-capture-instance-ct-transact-sql?view=sql-server-ver16) to replicate changes from. If a new capture instance is created after the stream starts, Datastream doesn't automatically switch to it. If the selected capture instance is deleted, Datastream skips reading the corresponding change table.

#### How Datastream handles DDL changes to the source schema

When you use the change tables CDC method, capture instances are created for each change table. Each capture instance is associated with a list of columns it captures and tracks. By default, when a data definition language (DDL) change happens in the source after the capture instance is created, the instance ignores the change. However, you can configure your SQL Server stream to replicate columns added to the source schema after the stream and the capture instance are created.

##### Before you begin

  * Make sure that your Datastream user has the `db_owner` permission assigned.



#### Replicate columns added to the source schema

To have Datastream support replicating columns added to the source schema after a stream was created, you need to add the `enable_ddl_support_for_ct` label to your stream:

  1. Go to the **Streams** page in the Google Cloud Console.

[Go to the Streams page](https://console.cloud.google.com/datastream/streams)

  2. Click the SQL Server stream that you want to edit.

  3. On the **Streams details** page, click **Pause**.

  4. Click **Edit** > **Edit stream settings**.

  5. Click **Add label**.

  6. In the **Key** field, type `enable_ddl_support_for_ct`.

  7. In the **Value** field, type `true`.

  8. Click **Save**.

  9. Click **Start** to resume your stream.




Datastream checks the [`cdc.ddl_history`](https://learn.microsoft.com/en-us/sql/relational-databases/system-tables/cdc-ddl-history-transact-sql?view=sql-server-ver16) table for new DDLs every five minutes. If there's a new column added to a table included in the stream configuration, Datastream verifies whether the table has two capture instances:

  * If it doesn't, then Datastream creates a new capture instance, reads the original capture instance data until the moment when the DDL happened, and then starts reading from the new capture instance.

**Note:** After Datastream creates the new capture instance, delete the original one. SQL Server supports a maximum of two capture instances per table, so deleting the old instance is required to allow for future DDL changes.
  * If it does, a log entry is added that the DDL change can't be handled because the maximum number of capture instances is reached.




### Transaction logs

When using this CDC method, Datastream reads changes in the source directly from transaction logs. This method requires fewer resources and allows for faster data retrieval, but has more limitations. 

To prevent data loss, it's important that the logs aren't truncated before Datastream reads them. On the other hand, if you keep the log files for too long, they take up storage space, which might eventually cause the database instance to enter read-only mode.

To make sure that the CDC reader has enough time to read the logs while allowing log truncation to free up storage space, you need to apply additional configuration steps, such as changing polling intervals and setting up a truncation safeguard. These steps provide an additional layer of protection to ensure that Datastream can read the data even if there's downtime on the Datastream side or a connectivity issue between the source database and Datastream.

For detailed instructions on how to apply these additional measures, see the [Configure a source SQL Server database](https://docs.cloud.google.com/datastream/docs/configure-your-source-sql-server-database) page and select your database type.

## Versions

Datastream supports the following versions and editions of SQL Server databases:

  * Self-managed (on-premise or cloud-hosted) using the following versions: 
    * Enterprise: 2008 and later
    * Standard: 2016 SP1 and later
    * Developer: 2008 and later
  * Amazon RDS for SQL Server
  * Azure SQL Database (tier S3 and above).

**Note:** Only supported when using the change tables CDC method.
  * Cloud SQL for SQL Server




Datastream doesn't support the following versions of SQL Server databases:

  * SQL Server Standard edition from version 2008 to 2014
  * SQL Server Express
  * SQL Server Web



## Known limitations

Known limitations for using SQL Server database as a source include:

  * Streams are limited to 10,000 tables.
  * A table that has more than 500 million rows can't be backfilled unless the following conditions are met: 
    1. The table has a unique index.
    2. None of the index columns are nullable.
    3. All columns of the index are included in the stream.
  * Databases with delayed durability or accelerated database recovery (ADR) enabled aren't supported.
  * Streaming changes to system tables isn't supported.
  * Windows Active Directory (AD) authentication isn't supported.
  * Datastream supports all SQL Server collations except for those with code page `0`. To check the code page of a specific collation, run the following query on your SQL Server instance:
        
        SELECT *, CAST(COLLATIONPROPERTY(name, 'CodePage') AS INT) FROM sys.fn_helpcollations() WHERE name = COLLATION_NAME;
        

  * The following data types aren't supported and aren't replicated to the destination:

    * `SQL_VARIANT`
    * `HIERARCHYID`
**Note:** For streams created before Datastream introduced support for spatial data types, `GEOMETRY` and `GEOGRAPHY` columns aren't replicated by default. To enable replication of `GEOMETRY` and `GEOGRAPHY` columns for an existing stream, add the `enable_sqlserver_spatial_types` label with the value `true` to your stream.
  * Datastream replicates user-defined data types, however it's the base data type from which you derive your user-defined type that is stored in the destination. For example, if you define a `USERNAME` data type based on the `VARCHAR(50)` data type, the data is stored in the destination as `VARCHAR(50)`.

  * Datastream doesn't support CDC for large object columns (`TEXT`, `NTEXT`, `XML`, `IMAGE`, `GEOMETRY`, `GEOGRAPHY`) and maximum variable-length columns (`VARCHAR(MAX)`, `VARBINARY(MAX)`, `NVARCHAR(MAX)`) in tables without a unique index.

If large object columns aren't included in the stream, CDC is supported.

  * Replicating the following source schema changes isn't supported when using the change tables CDC method, and might cause data corruption or failure to process events:

    * Dropping columns: data in these columns is replaced with `NULL` values.
    * Renaming columns: not supported for SQL Server when CDC is enabled.
    * Modifying data types: the SQL Server CDC capture job propagates only the following data type changes:

      * Changing the maximum length for strings: for example, changing the `VARCHAR(50)` data type to `VARCHAR(100)`. The BigQuery `STRING` column doesn't have a fixed length and accepts the longer string.
      * Increasing the integer value range: for example, changing the `INT` data type to `BIGINT`. The BigQuery `INT64` data type accommodates the new type without requiring a schema change.
      * Changing the precision and scale for numeric values: for example, changing the `DECIMAL(10, 2)` data type to `DECIMAL(18, 4)`. The BigQuery `NUMERIC` type has a large fixed precision (`38`) and scale (`9`), and such a change is supported.

For other data type modifications, Datastream tries to insert the data to the destination and raises an error if the data is rejected.

  * Datastream doesn't support replicating tables that include columns with data masking. Data is replicated without masking.

  * Datastream doesn't support replicating changes applied to the database using the Data Tier Application Package (DACPAC) package.

  * Datastream doesn't replicate changes made using the `WRITETEXT` or `UPDATETEXT` statements.

  * If you use the `enable_ddl_support_for_ct` label to replicate columns added to the source schema, then you can't have multiple streams attached to the same SQL Server source table. Because SQL Server supports a maximum of two capture instances per table, schema changes might cause race conditions where Datastream attempts to create capture instances, and this might cause streams to fail.

  * Datastream doesn't support replicating [computed columns](https://learn.microsoft.com/en-us/sql/relational-databases/tables/specify-computed-columns-in-a-table) unless the column is marked `PERSISTED`.

  * Datastream doesn't support `PAGE`, `COLUMNSTORE` or `COLUMNSTORE ARCHIVE` compression types.




### Additional limitations when using the transaction logs method

If you use the transaction logs CDC method, the following additional limitations apply:

  * Transparent Data Encryption (TDE) isn't supported.
  * Column Level Encryption isn't supported. Data in these columns is replaced with `NULL` values.
  * When using the transaction logs CDC method, Datastream doesn't support replicating columns added to the source schema after a stream is created. The new columns aren't replicated to the destination.
  * Datastream doesn't support the `ROLLBACK TO SAVEPOINT` statement. Such rollback events are ignored and aren't replicated to the destination.
  * Datastream doesn't support CDC for rows greater than 8 KB in the following types of tables: 
    * Tables without a unique index
    * Tables containing only a unique, non-clustered index with one or more variable-length columns (`VARCHAR`, `VARBINARY`, `NVARCHAR`, `GEOMETRY`, `GEOGRAPHY`)
  * Datastream doesn't support CDC for large object columns (`TEXT`, `NTEXT`, `XML`, `IMAGE`, `GEOMETRY`, `GEOGRAPHY`) in the following types of tables:

    * Tables without a unique index
    * Tables containing only a unique, non-clustered index with one or more variable-length columns (`VARCHAR`, `VARBINARY`, `NVARCHAR`, `GEOMETRY`, `GEOGRAPHY`)

If large object columns aren't included in the stream, CDC is only supported for such tables if they have valid indexes.

  * When using the transaction logs method, Datastream queries the source database to fetch missing values point-in-time in an active lookup process called supplementation. Supplementation applies to `XML`, `TEXT`, `NTEXT`, `IMAGE`, `GEOMETRY`, and `GEOGRAPHY` data types, and to variable-length types such as `VARCHAR(MAX)` or `VARBINARY` when rows exceed the 8 KB page limit. Because Datastream supplements these columns by querying the database, intermediate changes might not be captured in scenarios involving rapid, back-to-back updates or a quick delete after an insert. `DELETE` operations don't trigger supplementation. This limitation is particularly relevant when using the append-only write mode, which expects all intermediate changes to be captured.




## What's next

  * Learn how to [configure a SQL Server source](https://docs.cloud.google.com/datastream/docs/configure-your-source-sql-server-database) for use with Datastream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
