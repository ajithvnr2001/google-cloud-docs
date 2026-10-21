---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/known-limitations/
title: Known limitations and recommendations \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:00:08.849210+00:00
---

# Known limitations and recommendations  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/known-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Known limitations and recommendations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes known limitations (including special considerations for handling entities like  primary keys or  foreign keys and triggers), as well as  recommended practices for heterogeneous Oracle migrations with Database Migration Service.

## What isn't migrated

  * Users and permissions aren't migrated.
  * Schema changes that occur during an active migration job aren't automatically migrated. If you change your schema during the migration, you need to first update the conversion workspace with schema changes, and then refresh the relevant migration jobs. For more information, see [ Add updated schema or tables to the migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/manage-migration-jobs#edit-non-draft-job). 
  * [ `SAVEPOINT` statements](https://docs.oracle.com/en/database/oracle/oracle-database/19/sqlrf/SAVEPOINT.html) aren't supported and can cause data discrepancy in case of a rollback. 
  * Database Migration Service replicates user-defined data types, but only stores the base data type from which you derive your user-defined types. For example, if you define a `USERNAME` data type based on the `VARCHAR2` data type, the data is stored in the destination as `VARCHAR`. 



## Database, transactions and data consistency

  * The migration is eventually consistent, as Database Migration Service doesn't replicate each transaction as it happens. The migration brings in data from multiple tables. The order in which data is loaded into the destination may vary, but re-aligns with the source after writes on the source are stopped and the migration buffer is cleared. 
  * For heterogeneous Oracle migrations, Database Migration Service can only migrate one database per migration job. 
  * Database Migration Service supports Oracle multi-tenant architecture (CDB/PDB), but you can only migrate a single pluggable database per migration job. 
  * Oracle Label Security (OLS) isn't replicated.
  * Any transactions that are rolled back in your source database during the migration process might be visible in the destination temporarily (when the transaction is long enough). 
  * Database Migration Service doesn't support direct connectivity to databases using the Single Client Access Name (SCAN) feature in Oracle Real Application Clusters (RAC) environments. For potential solutions to using public IP allowlist connectivity with such environments, see [ Troubleshoot Oracle SCAN errors](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/diagnose-issues#troubleshoot-scan). 



## Data encoding

  * Database Migration Service supports only `UTF8` set encodings for the destination database. Schema and table names that include characters which aren't part of the `UTF8` encoding set are not supported. 
  * Database Migration Service supports the following character set encodings for Oracle databases: 
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



## Tables, schemas, and other objects

  * During a migration, data definition language (DDL) changes to data, schemas, and metadata aren't supported. If you update your schema during the migration, you need to pull the changes to your conversion workspace, convert the code, clean your destination and run the migration job again. 
  * Table column names that include characters other than alphanumeric characters or an underscore (`_`) aren't supported. 
  * Maximum name length for tables or columns is 30 characters. Database Migration Service can't replicate tables that exceed this limit, or tables that contain columns whose names exceed this limit. 
  * Index-organized tables (IOTs) aren't supported.
  * Global temporary tables require the `pgtt` PostgreSQL extension installed and created on the destination. 
  * For columns of type `BFILE`, only the path to the file will be replicated. The contents of the file won't be replicated. 
  * For Oracle 11g, tables that have columns of data types `ANYDATA` or `UDT` aren't supported, and the entire table won't be replicated. 
  * Jobs that are scheduled by using [ `dbms_job`](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_JOB.html) or [ `dbms_scheduler`](https://docs.oracle.com/en/database/oracle/oracle-database/19/arpls/DBMS_SCHEDULER.html) aren't migrated.
  * Materialized views definitions are migrated, but their materialized data isn't. After you finish migrating, refresh your materialized views in order to populate them with data from the migrated tables. 
  * Sequence values are migrated, but their values in the source database might keep advancing before the migration is completed. After complete the migration, update the sequence values on the destination instance to match those in the source database. 
  * Migration jobs are limited to 10,000 tables.
  * Rows have a size limitation of 100 MB. Rows that exceed the 100 MB limit are not migrated, and show up as errors in the migration job. 
  * Any tables that are created after the migration has started aren't be migrated automatically. First, you need to pull their schema in the conversion workspace, apply converted definitions to the destination, and update the migration job. 
  * Source tables that contain binary columns and don't have primary keys are unsupported for data migration in continuous migrations. 



### Data type limitations

The following data types are unsupported for Oracle migrations:

  * `ANYDATA` (For Oracle 11g, tables with `ANYDATA` are completely unsupported and not replicated.) 
  * `BFILE`
  * `INTERVAL DAY TO SECOND`
  * `INTERVAL YEAR TO MONTH`
  * `LONG/LONG RAW`
  * `SDO_GEOMETRY`
  * `UDT`
  * `UROWID`
  * `XMLTYPE`
  * **Zero dates** in `TIMESTAMP`



### Considerations for primary keys

Tables without primary keys don't promise consistent replication. Database Migration Service migrates only tables that have primary keys. If your source database includes tables that don't have primary keys, Database Migration Service conversion workspaces automatically create any missing primary keys in the destination tables when you [ convert your source code and schema](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/convert-sql). This automated process requires that your source tables:

  * Don't already have primary keys.
  * Don't have a `UNIQUE` constraint with no nullable columns.
  * Don't have a `UNIQUE` index with no nullable columns.



If your tables don't meet these requirements, you need to [ manually add missing primary keys to the tables in the converted PostgreSQL schema](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/migrate-tables-without-pks#add-keys-manually). You can also disable the automatic primary key generation with the [ `GENERATE_MISSING_PK` conversion directive](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/about-conversion-workspaces#conversion-directives-reference).

**For continuous migrations** : Source tables that contain binary columns and don't have primary keys are unsupported for data migration in continuous migrations.

If you use legacy conversion workspaces, you need to manually create primary key constraints in the converted tables in the destination database before you start the migration. For more information, see [ Legacy conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/legacy-conversion-workspaces).

### Considerations for foreign keys and triggers

Foreign keys and triggers present in your source database might lead to data integrity issues, or even cause the migration job to fail. You can prevent these issues if you skip foreign keys and triggers [ by using the `REPLICATION` option for the migration user](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-your-destination-postgresql-database). Alternatively, you can also drop all foreign keys and triggers in the destination database and re-create them when the migration is complete.

#### Triggers

Data replicated by Database Migration Service already incorporates any changes made by triggers on the source database. If triggers are enabled on the destination, they can fire again and potentially manipulate data, resulting in data integrity or duplication issues.

#### Foreign keys

Database Migration Service doesn't replicate data in a transactional manner, so tables might be migrated out of order. If foreign keys are present, and a child table that uses a foreign key is migrated before its parent, you might encounter replication errors.

## Recommendations

  * When you [ create your destination Cloud SQL database](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/configure-your-destination-postgresql-database), make sure that you use enough compute and memory resources to cover your migration needs. We recommend a machine type with at least a dual-core CPU. 

For example, if your machine name is `db-custom`, and it has 2 CPUs and 3840 MB of RAM, then the format for the machine type name is `db-custom-2-3840`. 

  * The destination Cloud SQL database is writable during the migration to allow Data Manipulation Language (DML) changes to be applied if needed. Take care not to make any changes to the database configuration or table structures which might break the migration process or impact data integrity. 



## Quotas

  * Up to 2,000 connection profiles and 1,000 migration jobs can exist at any given time. To create space for more, migration jobs (including completed ones) and connection profiles can be deleted. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
