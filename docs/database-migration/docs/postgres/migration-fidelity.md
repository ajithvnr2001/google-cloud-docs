---
url: https://docs.cloud.google.com/database-migration/docs/postgres/migration-fidelity/
title: Migration fidelity \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:59.127296+00:00
---

# Migration fidelity  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/migration-fidelity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Migration fidelity Stay organized with collections  Save and categorize content based on your preferences. 

When you migrate schema, data, and metadata from a source database to a destination database, you want to ensure that all information is migrated accurately. Database Migration Service provides a high-fidelity mechanism to migrate database objects (including schema, data, and metadata) from one PostgreSQL database to another.

During the migration process, data and constraints are migrated in structured phases. Data is migrated first during the initial snapshot load, and constraints such as primary keys, foreign keys, and indexes are recreated on the destination instance after the initial load completes.

The following data, schema, and metadata components are migrated as part of the database migration:

## Data

  * All tables and schemas from databases selected for migration, excluding the following system schemas:

    * The information schema (`information_schema`)
    * Any schemas beginning with `pg_` (for example, `pg_catalog`, `pg_toast`)

For more information about these system schemas, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations).

You can add or remove databases from a migration job during an ongoing migration. Removing a database stops replication for that database without deleting the already-migrated database on the destination instance. For more information, see [Edit a migration job](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions).




## Schema

  * Object naming

  * Primary keys

  * Data types

  * Ordinal column positions

  * Default values

  * Nullability

  * Identity and serial attributes

  * Secondary indexes




## Metadata

  * Stored procedures

  * Functions

  * Triggers

  * Views

  * Foreign key constraints




## Continuous migration

Data manipulation language (DML) changes (such as `INSERT`, `UPDATE`, and `DELETE` operations on tables with a primary key or replica identity) are automatically replicated during continuous migrations.

If there are any data definition language (DDL) changes on your source database during the migration process, you have to update your destination instance so that your databases remain compatible. You can perform the DDL changes in the following ways:

  1. **Manual DDL execution** : Stop writes to the source database, run the DDL commands on the source database, and run matching DDL commands on the destination database. Before running DDL commands on the destination, grant the `cloudsqlexternalsync` role to the Cloud SQL user applying the changes.

  2. **Replicated DDL commands with`pglogical`**: You can use `pglogical.replicate_ddl_command` to run DDL on both the source and destination databases at a consistent point in the replication stream. The user executing this command must have matching credentials on both source and destination instances, and must be a superuser or the owner of the modified object.




The following tabs provide sample SQL commands for common DDL operations using `pglogical.replicate_ddl_command`:

### Tables with primary keys

#### Add a column to a table with a primary key
    
    
    SELECT pglogical.replicate_ddl_command(
      'ALTER TABLE [SCHEMA].[TABLE_NAME] ADD COLUMN surname varchar(20)',
      '{default}'
    );

#### Change the name of a table with a primary key
    
    
    SELECT pglogical.replicate_ddl_command(
      'ALTER TABLE [SCHEMA].[TABLE_NAME] RENAME TO [NEW_NAME_FOR_TABLE]',
      '{default}'
    );

#### Create a table with a primary key

Run the following commands on the source database:
    
    
    SELECT pglogical.replicate_ddl_command(
      command := 'CREATE TABLE [SCHEMA].[TABLE_NAME] (id INTEGER PRIMARY KEY, name VARCHAR);',
      replication_sets := ARRAY['default']
    );
    SELECT pglogical.replication_set_add_table('default', '[SCHEMA].[TABLE_NAME]');

### Tables without primary keys

#### Add a column to a table without a primary key
    
    
    SELECT pglogical.replicate_ddl_command(
      'ALTER TABLE [SCHEMA].[TABLE_NAME] ADD COLUMN surname varchar(20)',
      '{default_insert_only}'
    );

#### Change the name of a table without a primary key
    
    
    SELECT pglogical.replicate_ddl_command(
      'ALTER TABLE [SCHEMA].[TABLE_NAME] RENAME TO [NEW_NAME_FOR_TABLE]',
      '{default_insert_only}'
    );

#### Create a table without a primary key

Run the following commands on the source database:
    
    
    SELECT pglogical.replicate_ddl_command(
      command := 'CREATE TABLE [SCHEMA].[TABLE_NAME] (id INTEGER PRIMARY KEY, name VARCHAR);',
      replication_sets := ARRAY['default_insert_only']
    );
    SELECT pglogical.replication_set_add_table('default_insert_only', '[SCHEMA].[TABLE_NAME]');

### What isn't migrated

  * **Users and privileges** : User login credentials and roles aren't migrated. To configure users on the destination instance, use the **Users** tab in the Google Cloud console or manage them using a SQL client. For more information, see [ Create and manage users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users#creating) in the Cloud SQL documentation.

  * **Unsupported extensions** : Database Migration Service doesn't migrate extensions that are unsupported by Cloud SQL. The presence of these extensions doesn't block the migration job, but applications referencing unsupported extensions might experience errors. For the list of supported extensions, see [ PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions) in the Cloud SQL documentation.

  * **Large objects** : PostgreSQL large objects (data type `oid` referencing `pg_largeobject`) aren't replicated by logical decoding.

  * **Tables without primary keys** : Database Migration Service migrates the initial snapshot and replicates `INSERT` statements during the CDC phase. For `UPDATE` and `DELETE` statements:

    * _Standard migrations_ : Standard migrations require that your tables have primary keys to replicate `UPDATE` and `DELETE` statements.

    * _Quick-start migrations_ : With quick-start migrations, primary keys aren't required to replicate `UPDATE` and `DELETE` operations if you set the replica identity to `INDEX` or `FULL`. Configuring `REPLICA IDENTITY FULL` increases write-ahead log (WAL) volume and resource overhead. Adding a primary key is recommended where feasible. For more information, see the [ PostgreSQL Replica Identity documentation](https://www.postgresql.org/docs/current/logical-replication-publication.html#LOGICAL-REPLICATION-PUBLICATION-REPLICA-IDENTITY) and [ Quick-start migrations guide](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide).

  * **Materialized views** : Database Migration Service migrates materialized view definitions, but doesn't migrate the underlying cached data. To populate materialized views on the destination, run `REFRESH MATERIALIZED VIEW view_name` after migration.

  * **Sequence states** : The current values of sequences (such as `last_value`) on the destination instance might differ from the source during ongoing CDC. Sequence values are synchronized during the final promotion step.

  * **Custom tablespaces** : Cloud SQL doesn't support custom tablespaces. Objects defined in custom tablespaces are automatically remapped to the default `pg_default` tablespace in Cloud SQL.




## What's next

  * For complete limitation details, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations).

  * To get started with a migration walkthrough, see [Get started with Cloud SQL for PostgreSQL migrations](https://docs.cloud.google.com/database-migration/docs/postgres/get-started-with-postgres-migrations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
