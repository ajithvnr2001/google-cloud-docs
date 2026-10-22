---
url: https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations/
title: Known limitations \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:27.403897+00:00
---

# Known limitations  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Known limitations Stay organized with collections  Save and categorize content based on your preferences. 

Before you choose to migrate your databases to Cloud SQL, consider known limitations for this migration scenario.

**Note:** You can also use Google Cloud Migration Center to discover gaps in feature support. See [ Discover and import databases](https://docs.cloud.google.com/migration-center/docs/discover-and-import-databases) in the Migration Center documentation. 

Known limitations for using a PostgreSQL database as a source include:

  * The `pglogical` extension doesn't support the replication of [ generated columns](https://www.postgresql.org/docs/current/ddl-generated-columns.html) for PostgreSQL 12+.

  * Changes to table structures (DDL) aren't replicated through standard DDL commands, but only with commands executed using the `pglogical` extension used for replication. This includes [changes to `enum` types](https://www.postgresql.org/docs/current/sql-altertype.html).

    * For example, `pglogical` provides the `pglogical.replicate_ddl_command` function that allows DDL to be run on both the source database and replica at a consistent point.
    * In order to replicate data for newly created tables, you must use the `pglogical.replication_set_add_table` command to add new tables to existing replication sets.
    * To learn more about DDL replication while the migration is in progress, see [Migration fidelity](https://docs.cloud.google.com/database-migration/docs/postgres/migration-fidelity).
  * For tables that don't have primary keys, Database Migration Service supports migration of the **initial snapshot and`INSERT` statements during the change data capture (CDC) phase**. Migrating `UPDATE` and `DELETE` statements is different for:

    * _Standard migrations_ : `UPDATE` and `DELETE` statements aren't migrated for tables without primary keys. You have to add primary keys for your columns before you migrate, or migrate `UPDATE` and `DELETE` statements manually.
    * _Quick-start migrations_ : With quick-start migrations, primary keys aren't required to replicate `UPDATE` and `DELETE` operations if you set the replica identity to `INDEX` or `FULL`. Configuring `REPLICA IDENTITY FULL` increases write-ahead log (WAL) volume and resource overhead. Adding a primary key is recommended where feasible. For more information, see the [ PostgreSQL Replica Identity documentation](https://www.postgresql.org/docs/current/logical-replication-publication.html#LOGICAL-REPLICATION-PUBLICATION-REPLICA-IDENTITY) and [ Quick-start migrations guide](https://docs.cloud.google.com/database-migration/docs/postgres/quick-start-migrations-guide).
  * Database Migration Service doesn't migrate data from materialized views, just the view schema. To populate the views on the destination database, run: `REFRESH MATERIALIZED VIEW view_name`.

  * The `SEQUENCE` states (for example, `last_value`) on the destination might vary from the source during ongoing CDC. Sequence values are synchronized during the final promotion step.

  * `UNLOGGED` and `TEMPORARY` tables aren't and can't be replicated.

  * Large Object data type (`oid` referencing `pg_largeobject`) isn't supported by PostgreSQL logical decoding.

  * Only extensions that Cloud SQL supports for PostgreSQL can be migrated. Database Migration Service doesn't migrate extensions that are unsupported by Cloud SQL. The presence of these extensions doesn't block the migration, but to ensure a smooth migration verify that your applications don't reference unsupported extensions. For the list of supported extensions, see [ PostgreSQL extensions](https://docs.cloud.google.com/sql/docs/postgres/extensions) in the Cloud SQL documentation.

  * The [`pg_cron`](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_cron) extension (or any cron jobs configured within the extension) isn't migrated by Database Migration Service, but is supported in Cloud SQL for PostgreSQL destinations. If you use `pg_cron` in your source databases, reinstall the extension and configure your cron jobs on the destination instance after the migration is complete.

  * Database Migration Service doesn't support migrating from read replicas that are in recovery mode.

  * Database Migration Service doesn't support Amazon RDS sources where the AWS SCT extension pack is applied.

  * User-defined functions written in C can't be migrated, except for functions that are installed when creating extensions supported by Cloud SQL.

  * If other extensions exist in the source database and their versions aren't supported by Cloud SQL, testing or starting the migration job will fail.

  * Databases that are added to the source instance after the migration job has started aren't migrated.

  * You can select specific databases when you migrate by using Database Migration Service. All tables and schemas from the selected databases are migrated, excluding:

    * The information schema (`information_schema`).
    * Any schemas beginning with `pg_` (for example, `pg_catalog`, `pg_toast`, `pg _temp_ *`). For the full list of PostgreSQL catalogs that begin with `pg_`, see [ PostgreSQL system catalogs](https://www.postgresql.org/docs/current/catalogs.html) in the PostgreSQL documentation.
    * User login credentials and roles.
  * If encrypted databases require customer-managed encryption keys (CMEK) to decrypt data, and Database Migration Service doesn't have access to the keys, the databases can't be migrated. However, data encrypted with the [ `pgcrypto` extension](https://docs.cloud.google.com/sql/docs/postgres/extensions#miscellaneous-extensions) can be migrated because Cloud SQL supports `pgcrypto`. Database Migration Service also supports migrating from encrypted Amazon Aurora or Amazon RDS databases because AWS handles decryption transparently. For more information, see [ Encrypting Amazon Aurora resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Overview.Encryption.html) and [Encrypting Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html).

  * **Destination database operational behavior during migration** :

    * **Writable destination database** : Cloud SQL for PostgreSQL doesn't run the destination database in read-only mode during migration. The destination instance isn't demoted when created by Database Migration Service.

    * **Avoid write operations on migrating data** : Don't perform write operations (such as `INSERT`, `UPDATE`, `DELETE`, or DDL schema changes) on tables or databases participating in the migration. Executing writes on migrating data can result in replication conflicts with the incoming change data capture (CDC) stream.

    * **Manage database users** : You can create and manage database users at any time using standard `psql` commands or through Cloud SQL in the Google Cloud console. For more information, see [Manage users](https://docs.cloud.google.com/sql/docs/postgres/create-manage-users) in the Cloud SQL documentation.

    * **Suspended features** : Automated backups and point-in-time recovery (PITR) are suspended during continuous replication. In addition, you can't create Cloud SQL read replicas from the destination instance until the migration job is promoted.

  * Trigger behavior depends on trigger configuration. By default, triggers don't fire on the replica during replication unless configured with `ALTER EVENT TRIGGER` or `ALTER TABLE ... ENABLE ALWAYS TRIGGER`.

  * Functions defined with `SECURITY DEFINER` are created by `cloudsqlexternalsync` on the destination Cloud SQL instance, which holds elevated privileges. Restrict execution privileges on sensitive `SECURITY DEFINER` functions by revoking public permissions and granting access selectively.

  * Cloud SQL doesn't support custom tablespaces. All objects inside custom tablespaces are migrated to the default `pg_default` tablespace in Cloud SQL.

  * The [ Private Service Connect interfaces connectivity method](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods#psc-interfaces) is only supported for migrating to existing destination instances. If you want to use private IP connectivity and migrate to a new destination instance, use VPC peering.




### Limitations for migrations to existing destination instances

  * **Destination instance demotion for standard migrations** : For standard migrations to existing Cloud SQL instances, Database Migration Service demotes the standalone instance to configure it as an external replica of the source database. 
    * Demoting the instance doesn't place the PostgreSQL engine into read-only mode, but you must avoid write operations on migrating tables to prevent replication conflicts. 
    * Demoting the instance suspends automated backups and point-in-time recovery (PITR) and prevents adding Cloud SQL read replicas until promotion. 
    * You must confirm demotion when creating the migration job in the Google Cloud console by entering the destination instance ID (or by running `gcloud database-migration migration-jobs demote-destination`). 
    * [ Quick-start migrations](https://docs.cloud.google.com/database-migration/docs/about-quick-start-migrations) use PostgreSQL `pgnative` logical replication and don't require or perform destination instance demotion. 
  * Your existing destination instance can only contain default system databases that are set up automatically when you create the destination instance. Migrating to existing destination instances that contain user data isn't supported. 

If you encounter issues due to extra data in your existing destination instance, clear the databases in your destination instance and retry the migration job. See [ Clear extra data from your existing destination instance](https://docs.cloud.google.com/database-migration/docs/postgres/diagnose-issues#clear-ext-instance-data-steps).

  * You can configure only one migration job per destination instance.
  * You can only migrate to standalone Cloud SQL instances. Migrating to [ external server replicas](https://docs.cloud.google.com/sql/docs/postgres/replication/configure-external-replica) isn't supported. 
  * After you promote an instance, you must turn on [point-in-time recovery](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/restore#tips-pitr). 
  * If your instance has customized backup settings (for example, a [ custom backup location](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/backing-up#locationbackups)), you have to restore your backup settings again after promotion. During the promotion process, Cloud SQL resets backup settings to their default values. 
  * **For Terraform users** : Database Migration Service modifies the backup and recovery settings of your destination instance. This might cause the destination instance settings to differ from the Terraform configuration used for provisioning. If you experience this issue, see the guidance in [ Diagnose issues](https://docs.cloud.google.com/database-migration/docs/postgres/diagnose-issues#existing-instance-terraform-config-drift). 



### Quotas

  * Up to 2,000 connection profiles and 1,000 migration jobs can exist at any given time. To create space for more, delete unused migration jobs and connection profiles.



### PostgreSQL extension version compatibility during major version upgrades

When you migrate to a higher PostgreSQL major version, Database Migration Service uses the `pg_restore` utility, which installs the default extension version of the target PostgreSQL major version. You can't specify an exact extension version for the `pg_restore` utility.

If your source database uses an extension version that is schema-incompatible with the default version installed on the target PostgreSQL major version, the migration might fail due to a schema mismatch or internal errors.

To avoid migration failures, verify schema compatibility. Before you migrate, upgrade the extensions on your source database to a version compatible with the target PostgreSQL major version.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
