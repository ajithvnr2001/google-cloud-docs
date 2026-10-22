---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-fidelity/
title: Migration fidelity \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:23.560116+00:00
---

# Migration fidelity  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-fidelity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Migration fidelity Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-fidelity "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/migration-fidelity "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


## Overview

When you're migrating your schema, data, and metadata from a source database to a destination database, you want to ensure that all of this information is migrated accurately. Database Migration Service provides a high-fidelity way to migrate database objects (including the schema, data, and metadata) from one database to another.

All of the following data, schema, and metadata components are migrated as part of the database migration:

### Data

  * All tables and schemas from databases selected for migration, excluding the following system databases:

    * The information schema `information_schema`
    * Any schemas beginning with `pg` (for example, `pg_catalog`)

For more information about these schemas, see [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations).




### Schema

  * Naming

  * Primary key

  * Data type

  * Ordinal position

  * Default value

  * Nullability

  * Auto-increment attributes

  * Secondary indexes




### Metadata

  * Stored procedures

  * Functions

  * Triggers

  * Views

  * Foreign key constraints




### Continuous migration

Only data manipulation language (DML) changes are updated automatically during continuous migrations. Managing data definition language (DDL) changes so that the source and destination databases remain compatible is the responsibility of the user, and can be achieved in two ways:

  1. Stopping writes to the source and running the DDL commands in both source and destination. Before running DDL commands on the destination, grant `alloydbexternalsync` to the AlloyDB user applying the DDL changes. To enable querying or changing the data, grant the `alloydbexternalsync` role to the relevant AlloyDB users. 
  2. Using the `pglogical.replicate_ddl_command` to allow DDL to be run on the source and destination at a consistent point. The user running this command must have the same username on both the source and the destination, and should be the superuser or the owner of the artifact being migrated (for example, the table, sequence, view, or database). 

Here are a few examples of using the `pglogical.replicate_ddl_command`.

Replace:

     * `[SCHEMA]` with the name of the table schema you want to use
     * `[TABLE_NAME]` with the table name
     * `[NEW_NAME_FOR_TABLE]` with the new name for the table when when performing the rename operation

#### Add a column to a database table with a primary key
    
    select pglogical.replicate_ddl_command(
      'ALTER TABLE [SCHEMA].[TABLE_NAME] add column surname varchar(20)',
      '{default}'
    );

#### Add a column to a database table without a primary key
    
    select pglogical.replicate_ddl_command(
      'ALTER TABLE [SCHEMA].[TABLE_NAME] add column surname varchar(20)',
      '{default_insert_only}'
    );

#### Change the name of a database table with a primary key
    
    select pglogical.replicate_ddl_command(
      'ALTER TABLE [SCHEMA].[TABLE_NAME] RENAME TO [NEW_NAME_FOR_TABLE]',
      '{default}'
    );

#### Change the name of a database table without a primary key
    
    select pglogical.replicate_ddl_command(
      'ALTER TABLE [SCHEMA].[TABLE_NAME] RENAME TO [NEW_NAME_FOR_TABLE]',
      '{default_insert_only}'
    );

#### Create a database table with a primary key

Run the following commands:

     1. select pglogical.replicate_ddl_command(
              command := 'CREATE TABLE [SCHEMA].[TABLE_NAME]
                (id INTEGER PRIMARY KEY, name VARCHAR);',
              replication_sets := ARRAY['default']
            );

     2. select pglogical.replication_set_add_table('default', '[SCHEMA].[TABLE_NAME]');

#### Create a database table without a primary key

Run the following commands:

     1. select pglogical.replicate_ddl_command(
              command := 'CREATE TABLE [SCHEMA].[TABLE_NAME]
               (id INTEGER PRIMARY KEY, name VARCHAR);',
              replication_sets := ARRAY['default_insert_only']
            );

     2. select pglogical.replication_set_add_table(
              'default_insert_only', '[SCHEMA].[TABLE_NAME]'
            );




### What isn't migrated

  * [Large objects](https://www.postgresql.org/docs/current/largeobjects.html) can't be replicated, as PostgreSQL's logical decoding facility does not support decoding changes to large objects. For tables that have column type [`oid`](https://www.postgresql.org/docs/current/datatype-oid.html) referencing large objects, the rows are synced, and new rows are replicated. However, trying to access the large object on the destination database (read using [`lo_get`](https://www.postgresql.org/docs/current/lo-funcs.html), export using [`lo_export`](https://www.postgresql.org/docs/current/lo-funcs.html), or check the catalog `pg_largeobject` for the given `oid`), fails with a message saying that the large object does not exist.

  * For tables that don't have primary keys, Database Migration Service supports migration of the **initial snapshot and`INSERT` statements during the change data capture (CDC) phase**. You should migrate `UPDATE` and `DELETE` statements manually.

  * Database Migration Service doesn't migrate data from materialized views, just the view schema. To populate the views, run the following command: `REFRESH MATERIALIZED VIEW view_name`.

  * The `SEQUENCE` states (for example, `last_value`) on the new destination might vary from the source `SEQUENCE` states.

  * Customized tablespaces aren't supported in the destination Cloud SQL instance. All the data inside customized tablespaces is migrated to the default `pg_default` tablespace in Cloud SQL.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


