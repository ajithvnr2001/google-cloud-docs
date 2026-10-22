---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations/
title: Known limitations \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:24.275711+00:00
---

# Known limitations  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Resources ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/resources)



Send feedback 

#  Known limitations Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


  


Known limitations for using a PostgreSQL database as a source include:

  * The `pglogical` extension doesn't support the replication of [generated columns](https://www.postgresql.org/docs/current/ddl-generated-columns.html) for PostgreSQL 12+.

  * Changes to table structures (DDL) aren't replicated through standard DDL commands, but only with commands executed using the `pglogical` extension used for replication. This includes [ changes to `enum` types](https://www.postgresql.org/docs/current/sql-altertype.html).

    * For example, `pglogical` provides a function `pglogical.replicate_ddl_command` that allows DDL to be run on both the source database and replica at a consistent point. The user running this command on the source must already exist on the replica.

    * In order to replicate data for new tables, you must use the `pglogical.replication_set_add_table` command to add the new tables to existing replication sets.

    * To learn more about DDL replication while the migration is in progress, see the section on [migration fidelity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-fidelity).

  * For tables that don't have primary keys, Database Migration Service supports migration of the **initial snapshot and`INSERT` statements during the change data capture (CDC) phase**. You should migrate `UPDATE` and `DELETE` statements manually.

  * Database Migration Service doesn't migrate data from materialized views, just the view schema. To populate the views, run the following command: `REFRESH MATERIALIZED VIEW view_name`.

  * The `SEQUENCE` states (for example, `last_value`) on the new AlloyDB destination might vary from the source `SEQUENCE` states.

  * `UNLOGGED` and `TEMPORARY` tables aren't and can't be replicated.

  * Large Object data type isn't supported. More details in the section on [migration fidelity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-fidelity).

  * Only [extensions and procedural languages](https://docs.cloud.google.com/alloydb/docs/reference/extensions) that AlloyDB supports for PostgreSQL can be migrated.

  * Database Migration Service doesn't support migrating from read replicas that are in recovery mode.

  * Database Migration Service doesn't support Amazon RDS sources where the AWS SCT extension pack is applied.

  * User-defined functions written in C can't be migrated, except for functions that are installed in the PostgreSQL database when you're installing [extensions](https://docs.cloud.google.com/alloydb/docs/reference/extensions) that are supported by AlloyDB.

  * If other extensions and procedural languages exist in the source database, or if their versions aren't supported, then when you test or start the migration job, it will fail.

  * Databases that are added after the migration job has started aren't migrated.

  * You can select specific databases when you migrate by using Database Migration Service. However, you can't select specific tables or schemas within those databases. Database Migration Service migrates all tables and schemas from the selected databases, except for the following:

    * The information schema (`information_schema`).
    * Any schemas that begin with `pg_` (for example, `pg_catalog`, `pg_toast`, `pg _temp_ *`). For the full list of PostgreSQL catalogs that begin with `pg_`, see [PostgreSQL system catalogs](https://www.postgresql.org/docs/current/catalogs.html) in the PostgreSQL documentation.
    * Information about users and user roles isn't migrated.
  * If encrypted databases require customer-managed encryption keys to decrypt the databases, and if Database Migration Service doesn't have access to the keys, then the databases can't be migrated.

However, if customer data is encrypted by the [`pgcrypto` extension](https://docs.cloud.google.com/sql/docs/postgres/extensions#miscellaneous-extensions), then the data can be migrated with Database Migration Service (because AlloyDB for PostgreSQL supports the extension).

Database Migration Service also supports migrating data from encrypted Amazon Aurora or Amazon RDS databases because these databases handle decryption transparently in their services. For more information, see [Encrypting Amazon Aurora resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html) and [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html).

  * The destination AlloyDB for PostgreSQL database is writable during the migration to allow DDL changes to be applied if needed. Take care not to make any changes to the database configuration or table structures which might break the migration process or impact data integrity.

  * Trigger behavior depends on how they were configured. The default behavior is they won't trigger, but if they were configured using the `ALTER EVENT TRIGGER` or `ALTER TABLE` statement and the trigger state is set to either replica or always, then they will trigger on the replica during replication.

  * Functions with security definer will be created by `alloydbexternalsync` in AlloyDB primary. When it's executed by any users, it will be executed with the privileges of `alloydbexternalsync` which has `alloydbsuperuser` and `alloydbreplica` roles. It's better to restrict use of a security definer function to only some users. To do that, the user should revoke the default PUBLIC privileges and then grant execute privilege selectively.

  * [ Private Service Connect interfaces connectivity method](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/networking-methods#psc-interfaces) is only supported for migrating to existing destination instances. If you want to use private IP connectivity and migrate to a new destination instance, use VPC peering.




### Limitations for migrations to existing destination clusters

  * You can configure only one active migration job per destination cluster.
  * Your existing destination cluster must be empty or contain only system configuration data. Migrating to existing destination cluster that contain user data (such as tables) isn't supported. 
  * Migrating to clusters with read pool instances **is supported**. 

For more information on AlloyDB for PostgreSQL clusters and instances, see [AlloyDB for PostgreSQL overview](https://docs.cloud.google.com/alloydb/docs/overview). 




### Quotas

  * Up to 2,000 connection profiles and 1,000 migration jobs can exist at any given time. To create space for more, migration jobs (including completed ones) and connection profiles can be deleted.



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


