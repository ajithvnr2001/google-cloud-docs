---
url: https://docs.cloud.google.com/alloydb/docs/cluster-upgrade/
title: Upgrade a cluster's major server version \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:14.469871+00:00
---

# Upgrade a cluster's major server version  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/cluster-upgrade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Upgrade a cluster's major server version Stay organized with collections  Save and categorize content based on your preferences. 

Upgrading your AlloyDB for PostgreSQL cluster to a later major version of PostgreSQL lets you use the latest database features, performance enhancements, and security updates. You can upgrade a cluster's major version in place or by migrating your data to a cluster that runs a later PostgreSQL version.

For more information about how to create a cluster, see [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create).

## Clusters and PostgreSQL version compatibility

When you create an AlloyDB cluster, you choose the major version of PostgreSQL that's compatible with the instances in the cluster. By default, this is 17.

AlloyDB performs automatic minor database version upgrades during periodic maintenance. For example, if you created a cluster with 17 compatibility, then AlloyDB keeps the database servers upgraded to the latest minor version of 17.

However, a major version upgrade of the PostgreSQL version requires you to plan, test, and perform the upgrade yourself.

**Note:** For details on AlloyDB versioning policy, refer to [Database version policies](https://docs.cloud.google.com/alloydb/docs/db-version-policies).

There are several methods to perform major version upgrades of your cluster:

  1. An [in-place major version upgrade](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version) that we recommend to use.
  2. Migrating the data with a file-based data export.
  3. Using Database Migration Service. 



Each upgrade solution offers different advantages and disadvantages. See the following table for a brief comparison to help you choose the right approach for your scenario.

In-place major version upgrade | File-based data export | Migration with Database Migration Service  
---|---|---  
Your cluster, including read instances, gets upgraded to the chosen higher major version. | File-based exports move a one-time snapshot of your databases. | Database Migration Service offers continuous replication capabilities during the migration process, lowering the chance of missing data in your new cluster.  
You can continue to work on your cluster during the pre-upgrade stage. | Your application experiences a longer downtime that starts when you export the data. You can't accept database writes in your original cluster until the new cluster is fully operational. | Your application experiences a shorter downtime that starts when you want to switch the application to use the new cluster.  
You can expect roughly 20 minutes or higher downtime during the upgrade process depending on your schema. Post upgrade, you can access the cluster with the same IP address. | You have greater granular control over what data to include in your export and can choose to not migrate certain tables or other entities. | Database Migration Service automatically migrates all databases present in your instances, and all instances in your cluster. You can't choose to exclude certain tables or views from your migration data.  
Your cluster can have the SSL enforcement mode enabled. | Your cluster can have the SSL enforcement mode enabled. | For migration purposes, Database Migration Service requires that you disable the SSL enforcement mode on the source cluster.  
  
  
The next section details the process of performing a major version upgrade, including migrating your data.

## In-place major version upgrade

An in-place upgrade updates your existing cluster without requiring you to set up any additional clusters. For more information, see [Upgrade a database in-place major version](https://docs.cloud.google.com/alloydb/docs/upgrade-db-inplace-major-version).

## Migrate by using file-based data export

To use a database server compatible with a higher major version of PostgreSQL, you need to create a functionally identical cluster in the same region, and then migrate your data into it.

Follow these steps:

  1. [Create a cluster that's configured with the major version of PostgreSQL compatibility that you want to use.](https://docs.cloud.google.com/alloydb/docs/cluster-create) Create the cluster in the same region as your current cluster.

  2. Set up the new cluster with the new major version to match the current cluster's configuration:

     1. [Create additional read pool instances as needed.](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create)

     2. [Create secondary clusters as needed.](https://docs.cloud.google.com/alloydb/docs/cross-region-replication/work-with-cross-region-replication#secondary-cluster-instance)

When you create secondary clusters, you don't need to specify a PostgreSQL major version number. AlloyDB applies the primary cluster's PostgreSQL version to all of its secondary clusters.

     3. [Update the new cluster's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags) to match the current cluster's flag settings.

     4. [Enable any extensions that your applications need.](https://docs.cloud.google.com/alloydb/docs/instance-configure-extensions)

  3. [Export your data from the old cluster into files using `psql` or `pg_dump`.](https://docs.cloud.google.com/alloydb/docs/migration-overview#export)

  4. [Import your data from the files into the new cluster.](https://docs.cloud.google.com/alloydb/docs/migration-overview#import-files)




Your applications can [connect to the new cluster's instances](https://docs.cloud.google.com/alloydb/docs/connection-overview) at their new IP addresses.

## Migrate by using Database Migration Service

You can use [Database Migration Service](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb) to move data from PostgreSQL databases to AlloyDB clusters. Database Migration Service doesn't provide configuration dedicated specifically for AlloyDB data sources, but AlloyDB is PostgreSQL-compatible so you can use configuration intended for generic PostgreSQL sources.

This migration path isn't an in-place upgrade and results in the creation of a new cluster with a different IP address. We recommend you first [clone your cluster](https://docs.cloud.google.com/alloydb/docs/cluster-create#clone) and perform a test migration to verify if your application is compatible with this approach.

### Important considerations

Before you prepare to migrate with Database Migration Service, carefully consider the following limitations to make sure this migration path fits your upgrade scenario.

Limitations
    

  * AlloyDB instances configured with [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) are not supported.
  * You can't perform instance updates or failover requests on the source cluster during the migration. These operations can cause the migration job to fail.
  * All standard limitations for PostgreSQL to AlloyDB migrations apply to this scenario. For the full list of other limitations, see [ Known limitations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/known-limitations) in the Database Migration Service documentation. 


Migration fidelity
    Certain data types, such as [large objects](https://www.postgresql.org/docs/17/largeobjects.html), aren't migrated. For the full list of supported data, see [ Migration fidelity](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-fidelity) in Database Migration Service documentation. 
Source database lockout and downtime
    

Database Migration Service uses continuous migrations to move data to AlloyDB clusters. This type of migration incurs a short (under 10 seconds) lockout on the source database tables, one at a time, as the initial data dump is created.

When the migration is complete, you need to stop all writes on the source database before you can switch your application to the new cluster. This procedure requires some downtime. For a more detailed overview, see [ Continuous migrations](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-types#continuous-migration) in the Database Migration Service documentation. 

Replication limitations
    

After the migration job moves into the change data capture (CDC) phase, Database Migration Service continuously replicates new data written to your source databases. 

**For tables that don't have primary keys** , only `INSERT` statements are replicated during the CDC phase. Any `CREATE`, `UPDATE`, or `DELETE` actions performed on tables that don't have primary keys during the CDC phase need to be re-created on the destination database manually to avoid data loss. 

### Before you begin

  1. Enable the Database Migration Service API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=datamigration.googleapis.com)

  2. Make sure that you have the following role or roles on the project: 

     * One of the following: 
       * AlloyDB > AlloyDB Admin
       * Basic > Owner
       * Basic > Editor
     * You must also have the `compute.networks.list` permission in the Google Cloud project you are using. To gain this permission while following the principle of least privilege, ask your administrator to grant you the Compute Engine > Compute Network User role (`roles/compute.networkUser`). 
     * Database Migration Admin

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 
  3. Make sure that the Virtual Private Cloud (VPC) network in the Google Cloud project that you are using is [configured for private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity) to AlloyDB. 
  4. Decide in which region you want to create your destination cluster. All the Database Migration Service entities (connection profiles, migration jobs) must be created in the same region as your destination cluster. 
  5. Prepare a database user that you want to connect to your cluster and execute migration statements on your source databases. This database user requires a specific set of permissions and roles. We recommend that you [ create a new database user](https://docs.cloud.google.com/alloydb/docs/database-users/manage-roles#create) and designate it specifically for the purpose of performing the migration. 



### Configure your source instances

Database Migration Service requires specific configuration to be able to connect and copy data from your source cluster to the new destination cluster.

To configure your AlloyDB source instances, perform these steps:

  1. [ Configure database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags) on every instance in your source cluster. Use the following values: Flag | Value  
---|---  
[ `alloydb.logical_decoding`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#alloydb.logical_decoding) | Set to `on`.  
[ `alloydb.enable_pglogical`](https://docs.cloud.google.com/alloydb/docs/reference/alloydb-flags#alloydb.enable_pglogical) | Set to `on`.  
[ `max_replication_slots`](https://www.postgresql.org/docs/17/runtime-config-replication.html#GUC-MAX-REPLICATION-SLOTS) | This flag defines the maximum number of replication slots the source instance can support. The **minimum value** for this flag is `50`. Calculate the minimum value by using the following formula: ` (the number of databases in your instance) * (the number of simultaneous migration jobs you want to perform) + (slots reserved for table synchronization) + (the number of replication slots that you use for your read replicas)` Consider an example where the following are true:
     * You don't have read replicas in your source.
     * You have 30 databases on the primary source instance.
     * You want to create 2 migration jobs for the source cluster.
     * You want to use 10 slots for table replication.
In such a case, the number of `max_replication_slots` must be at least `70`, calculated as `30 * 2 + 10 + 0`.   
[ `max_wal_senders`](https://www.postgresql.org/docs/17/runtime-config-replication.html#GUC-MAX-WAL-SENDERS) | Set this flag to at least 10 more than the `max_replication_slots` value plus the number of senders already used on your instance. For example, if you set the `max_replication_slots` flag to `70` and you already use 2 senders, then `max_wal_senders` should be at least `82` (calculated as `70 + 10 + 2 = 82`).   
[ `max_worker_processes`](https://www.postgresql.org/docs/17/runtime-config-resource.html#GUC-MAX-WORKER-PROCESSES) | Set this flag to at least the number of databases in your instance plus the number of `max_worker_processes` you already use. For example, if you have 30 databases on your source instance and don't use any worker processes, set this flag to `30`.  
  2. [Disable SSL enforcement mode](https://docs.cloud.google.com/alloydb/docs/instance-ssl) on every instance in your source cluster. 



### Configure your source databases

You must install the `pglogical` extension and grant the required permissions to the database user you designate as the migration user on every database in your instances.

To configure your databases, perform these steps:

  1. [Connect to the default `postgres` database by using the `psql` client](https://docs.cloud.google.com/alloydb/docs/connect-psql).
  2. Install the `pglogical` extension by running the following command:
         
         CREATE EXTENSION IF NOT EXISTS pglogical;
         

  3. Grant permissions to the migration database user on all schemas **except for** the `information` schema and schemas whose names start with the `pg_` prefix. Execute the following statements:
         
         GRANT USAGE on SCHEMA SCHEMA_NAME to USER_NAME;
         GRANT SELECT on ALL TABLES in SCHEMA SCHEMA_NAME to USER_NAME;
         GRANT SELECT on ALL SEQUENCES in SCHEMA SCHEMA_NAME to USER_NAME;
         

Replace the following:

     * `SCHEMA_NAME`: the name of a schema present in your database
     * `USER_NAME`: the name of the database user you prepared in the Before you begin section

Repeat this step for every schema in your database **except for** the `information` schema, and schemas whose names start with the `pg_` prefix. You can list all database schemas with the [`\dn`](https://www.postgresql.org/docs/17/app-psql.html#APP-PSQL-META-COMMANDS) meta-command.

  4. Grant the remaining required permissions. Execute the following statements:
         
         GRANT USAGE on SCHEMA pglogical to PUBLIC;
         GRANT SELECT on ALL TABLES in SCHEMA pglogical to USER_NAME;
         ALTER USER USER_NAME with REPLICATION;
         

Replace `USER_NAME` with the name of the database user you prepared in the Before you begin section.

  5. Connect to every other database in your instance and repeat steps 2, 3, and 4.

     * You can list all databases in your instance with the [`\list`](https://www.postgresql.org/docs/17/app-psql.html#APP-PSQL-META-COMMANDS) meta-command.

     * You can switch to another database without resetting your `psql` client connection by using the [`\connect DATABASE_NAME`](https://www.postgresql.org/docs/17/app-psql.html#APP-PSQL-META-COMMAND-C-LC) command.

  6. Repeat this procedure for every instance in your source AlloyDB cluster.




### Run the migration in Database Migration Service

Follow these steps:

  1. [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-source-connection-profile) for your AlloyDB cluster. Use the following values:

     * **Database engine** : Select **PostgreSQL**.
     * **Hostname/IP** : Use the IP address of the primary instance in your cluster.
     * **Username/password** : Enter the credentials for the database user you prepared in the Before you begin section.
     * **Port** : Enter `5432`.
     * **Region** : Select the region where your destination cluster is located.
     * **Encryption type** : Select **None**.
  2. Create and run the migration job.

You can create your new AlloyDB cluster ahead of time, or have Database Migration Service create the cluster for you during migration job configuration. For more information, see [Migration jobs overview](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-intro) in the Database Migration Service documentation.

If you want Database Migration Service to create the destination cluster for you during the migration job configuration, follow the steps in the [Create a migration job to a new destination instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job) procedure.

If you want to create the destination cluster outside Database Migration Service, follow the steps in the [Create a migration job to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-migration-job-existing-instance) procedure.

  3. When the status of your migration job changes to **CDC** , [promote the migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/promote-migration). You can check the migration job status on the migration overview page. See [Reviewing a migration job](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/review-migration-job) in the Database Migration Service documentation.

This action causes your destination cluster to exit bootstrapping mode (that is, your destination AlloyDB cluster is no longer in read-only state).

  4. **(Optional)** Check for missing statements in tables that don't have primary keys.

If your source AlloyDB databases contain tables that don't have primary keys, you might need to manually migrate any missing `UPDATE` or `DELETE` statements. See [Migrate UPDATE and DELETE operations for non-primary key tables](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/debugging-tools#find_tables_without_primary_keys_pks) in the Database Migration Service documentation.

  5. Switch your application to the new cluster. Your applications can [connect to the new cluster's instances](https://docs.cloud.google.com/alloydb/docs/connection-overview) at their new IP addresses.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
