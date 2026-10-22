---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/known-limitations/
title: Known limitations and recommendations \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:55.038860+00:00
---

# Known limitations and recommendations  |  Database Migration Service for heterogeneous SQL Server to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/known-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for AlloyDB ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

#  Known limitations and recommendations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes known limitations (including special considerations for  enabling CDC on the source database, or handling entities like  primary keys or  foreign keys and triggers), as well as recommended practices for heterogeneous SQL Server migrations with Database Migration Service.

## What isn't migrated

  * Objects (tables, stored procedures, and so on) that are created after the migration job has started aren't migrated. 
  * Instance-level objects such as jobs, logons, encryption certificates, or permissions aren't migrated. 
  * Schema changes that occur during an active migration job aren't automatically migrated. If you change your schema during the migration, you need to first update the conversion workspace with schema changes, and then refresh the relevant migration jobs. For more information, see [ Add updated schema or tables to the migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/manage-migration-jobs#edit-non-draft-job). 
  * Database Migration Service doesn't replicate changes made using the `WRITETEXT` or `UPDATETEXT` statements. 
  * Changes to system tables aren't replicated during the CDC phase.



## Database, transactions and data consistency

  * For heterogeneous SQL Server migrations, Database Migration Service can only migrate one database per migration job.
  * Adding new databases to the source instance during an active migration job isn't supported, and it can cause the subsequent migration job restart to fail. 
  * The destination database must have the same name as the user name that's used to connect to the database. 
  * Databases with delayed durability or accelerated database recovery (ADR) enabled aren't supported.
  * Any transactions that are rolled back in your source database during the migration process might be visible in the destination temporarily (when the transaction is long enough). 
  * Windows Active Directory (AD) authentication isn't supported.
  * Always-On cluster failovers aren't supported. Database Migration Service supports connecting to the primary Always-On instance only and doesn't support failovers. 



## Tables, schemas, and other objects

  * Indexed view definitions are migrated, but their data isn't. After you finish migrating, refresh your indexed views in order to populate them with data from the migrated tables. 
  * Renaming tables and columns using `sp_rename` isn't supported.
  * Database Migration Service doesn't support data masking. Data is replicated without masking. 
  * Database Migration Service doesn't support replicating changes applied to the database using the Data Tier Application Package (DACPAC) package. 
  * Database Migration Service doesn't support `PAGE`, `COLUMNSTORE` or `COLUMNSTORE ARCHIVE` compression types. 
  * Sparse columns aren't supported, Database Migration Service populates such columns with `NULL` values. 
  * `LOB` (Large Object) columns are supported only for tables with primary keys. 
  * Objects with dependencies and metadata, such as stored procedures and functions containing the `EXECUTE AS` clause, cause the replication to fail. 
  * Sequence values are migrated, but their values in the source database might keep advancing before the migration is completed. After complete the migration, update the sequence values on the destination cluster to match those in the source database. 
  * Column-level encryption isn't supported. Data in these columns is replaced `with NULL values`. 
  * Migration jobs are limited to 10,000 tables.
  * Rows have a size limitation of 100 MB. Rows that exceed the 100 MB limit are not migrated, and show up as errors in the migration job. 
  * Each table that has more than 500 million rows must have a unique index. No column in the index can be nullable. 
  * Any tables that are created after the migration has started aren't be migrated automatically. First, you need to pull their schema in the conversion workspace, apply converted definitions to the destination, and update the migration job. 
  * The following objects aren't replicated: 
    * [ Temporal tables](https://docs.microsoft.com/en-us/sql/relational-databases/tables/temporal-tables)
    * [ Memory-optimized tables](https://docs.microsoft.com/en-us/sql/relational-databases/in-memory-oltp/introduction-to-memory-optimized-tables)
    * Tables with a clustered columnstore index
    * Modules that are compiled within SQL Server



### Considerations for enabling CDC on the source database

Database Migration Service requires that you enable the change data capture mechanism on your source database for the migration. When this feature is active, your source database is subject to certain operational limitations, for example:

  * You can't rename columns in your schema when CDC is active.
  * Performing other schema changes (such as adding or removing columns, changing their data types) is possible, but requires additional permissions (the `sysadmin`, `db_owner` or `db_ddladmin` roles).
  * By default, the maximum size of Large Objects (LOBs) that you can write to tables with CDC enabled is `65536 bytes`. If your application needs to write bigger objects to your tables during the migration, you might need to adjust the default limit by modifying the [ `max text repl size` parameter with the `sp_configure` stored procedure](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/configure-the-max-text-repl-size-server-configuration-option).



There are many other limitations you need to consider before you enable CDC on your source database. We recommend you carefully go through all known limitations before you enable CDC. See [ Known limitations, issues and errors with CDC](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/known-issues-and-errors-change-data-capture) in the Microsoft documentation.

### Source tables without primary keys

Tables without primary keys don't promise consistent replication. Database Migration Service migrates only tables that have primary keys. If your source database includes tables that don't have primary keys, Database Migration Service conversion workspaces automatically create any missing primary keys in the destination tables when you [ convert your source code and schema](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/convert-sql).

Database Migration Service generates the primary keys based on all columns in each row. The key is then added to the table in a new column named `md5_hash`. This impacts the migration behavior for the migration:

  * Duplicate rows are migrated as a single row to preserve uniqueness.
  * Updates to rows without primary keys in the source database are captured as new rows in the destination database during CDC.



You can also disable the automatic primary key generation with the [ `GENERATE_MISSING_PK` conversion directive](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/about-conversion-workspaces#conversion-directives-reference).

### Considerations for foreign keys and triggers

Foreign keys and triggers present in your source database might lead to data integrity issues, or even cause the migration job to fail. You can prevent these issues if you skip foreign keys and triggers [ by using the `REPLICATION` option for the migration user](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-destination-database). Alternatively, you can also drop all foreign keys and triggers in the destination database and re-create them when the migration is complete.

#### Triggers

Data replicated by Database Migration Service already incorporates any changes made by triggers on the source database. If triggers are enabled on the destination, they can fire again and potentially manipulate data, resulting in data integrity or duplication issues.

#### Foreign keys

Database Migration Service doesn't replicate data in a transactional manner, so tables might be migrated out of order. If foreign keys are present, and a child table that uses a foreign key is migrated before its parent, you might encounter replication errors.

## Supported data types for syntax conversion

When you [ create a conversion workspace](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/create-conversion-workspace), Database Migration Service automatically performs the initial schema conversion. Automatic schema conversion supports a very specific subset of available PostgreSQL data types. To enhance the automatic conversion mechanism, you can use a custom conversion mapping file. For more information on supported conversion mechanisms, see [Conversion workspaces](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/about-conversion-workspaces).

Regardless of whether you only use the automatic schema conversion or create an additional conversion mappings file, there are certain data type limitations that always apply:

  * Change data capture (CDC) isn't supported for large object columns (`TEXT`, `NTEXT`, `XML`, `IMAGE`) or maximum variable length columns (`VARCHAR(MAX)`, `VARBINARY(MAX)`, `NVARCHAR(MAX)`) in tables without a unique index. 
  * The following data types aren't supported, and aren't replicated to the destination: 
    * `SQL_VARIANT`
    * `HIERARCHYID`
    * `GEOMETRY`
    * `GEOGRAPHY`



## Recommendations

  * When you [ create your destination AlloyDB for PostgreSQL database](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/configure-destination-database), make sure that you use enough compute and memory resources to cover your migration needs. We recommend a machine type with at least a dual-core CPU. 
  * The destination AlloyDB for PostgreSQL database is writable during the migration to allow Data Manipulation Language (DML) changes to be applied if needed. Take care not to make any changes to the database configuration or table structures which might break the migration process or impact data integrity. 



## Quotas

  * Up to 2,000 connection profiles and 1,000 migration jobs can exist at any given time. To create space for more, migration jobs (including completed ones) and connection profiles can be deleted. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
