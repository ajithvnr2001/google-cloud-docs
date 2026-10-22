---
url: https://docs.cloud.google.com/database-migration/docs/postgres/guide-to-new-instance/
title: Migrate to a new destination instance \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:27.302026+00:00
---

# Migrate to a new destination instance  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/guide-to-new-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Migrate to a new destination instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to migrate your databases to a new Cloud SQL for PostgreSQL instance that Database Migration Service creates on your behalf when you configure the migration job. If your migration has different requirements, consider following a different migration flow. For more information, see [ Guide: Migrate to an existing Cloud SQL instance](https://docs.cloud.google.com/database-migration/docs/postgres/guide-to-existing-instance).

At a high level, the migration follows these steps:

  1. Configure the source database to allow Database Migration Service to move your data to the new databases.
  2. Create the source connection profile and the migration job.
  3. Depending on your connectivity configuration, you might need to adjust the firewall settings.
  4. Start and monitor the migration job.
  5. Promote the migration job and move your application to use the new databases.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud SQL (See [ Cloud SQL pricing](https://docs.cloud.google.com/sql/pricing).)
  * If used for storing Customer-managed Encryption Keys (CMEK): Cloud Storage (See [ Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).) 



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

## Before you begin

  1. Verify if this migration path can fully support your scenario. See the following pages: 
     * [ Supported sources and destinations](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview#supported-src-and-dest) on the _Scenario overview_ page lists all supported source and destination versions. 
     * [Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations) describes supported data types, database sizes, and other limitations. 
     * Different network connectivity methods are available for different source databases. Consider and plan your network connectivity before you begin the migration procedures. For more information, see [ Networking overview](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods). 

Migrating to a new destination instance doesn't support Private Service Connect interfaces connectivity. If you want to use Private Service Connect interfaces connectivity, consider pre-creating your destination instance directly in Cloud SQL. See [ Guide: Migrate to an existing Cloud SQL instance](https://docs.cloud.google.com/database-migration/docs/postgres/guide-to-existing-instance). 

  2. Consider in which region you want to create the destination database. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region. 
  3. In the Google Cloud console, on the project selector page, select or [ create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

[Go to project selector](https://console.cloud.google.com//projectselector2/home/dashboard)

  4. Enable the Database Migration Service and Cloud SQL Admin APIs. 

[ Enable the APIs](https://console.cloud.google.com//flows/enableapi?apiid=datamigration.googleapis.com,sqladmin.googleapis.com)




### Required roles

To get the permissions that you need to perform homogeneous PostgreSQL migrations with Database Migration Service, ask your administrator to grant you the required IAM roles on your project:

  * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * [ Cloud SQL Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.editor) (`roles/cloudsql.editor`) 
  * [ Cloud SQL Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser) (`roles/cloudsql.studioUser`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation. 

These predefined roles contain the permissions required to perform homogeneous PostgreSQL migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform homogeneous PostgreSQL migrations with Database Migration Service: 

  * `datamigration.*`
  * `cloudsql.instances.create`
  * `cloudsql.instances.get`
  * `cloudsql.instances.list`
  * `cloudsql.instances.update`
  * `cloudsql.instances.delete`
  * `cloudsql.operations.get`
  * `cloudsql.users.list`
  * `cloudsql.users.get`
  * `cloudsql.users.create`
  * `cloudsql.users.update`
  * `cloudsql.users.delete`



You might also be able to get these permissions with [ custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [ predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions). 

## Prepare your source database

To prepare your source data for migration, follow these steps:

  1. [ Choose and configure your source network connectivity method](https://docs.cloud.google.com/database-migration/docs/postgres/networking-methods). 

**For public IP allowlist connectivity** : At a later point, after Database Migration Service creates the destination instance, you might need to add the Cloud SQL public IP address to your firewall allowlist. Consult your network administrator on how to best schedule such configuration changes. 

  2. Configure your source database instance. At a high level, this includes the following steps: 
     1. Install the `pglogical` PostgreSQL extension (version 2.2.1 or later) on the source database and on all databases to be migrated.
     2. Configure PostgreSQL parameters: set `wal_level = logical`, and ensure adequate values for `max_replication_slots`, `max_wal_senders`, and `max_worker_processes`. 
     3. Grant replication privileges to your migration user, and configure `pg_hba.conf` to permit connections from the destination Cloud SQL instance. 

For detailed instructions, see [ Configure your source database](https://docs.cloud.google.com/database-migration/docs/postgres/configure-source-database). 

  3. [ Create the source connection profile](https://docs.cloud.google.com/database-migration/docs/postgres/create-connection-profiles). 



## Create and run the migration job

**Note:** When Database Migration Service creates your destination Cloud SQL instance, the instance isn't demoted and doesn't run in read-only mode. But you must avoid performing write operations on tables or databases included in the migration to prevent replication conflicts. Automated backups, point-in-time recovery (PITR), and creating read replicas are suspended until you promote the migration job. For more information, see [ Known limitations](https://docs.cloud.google.com/database-migration/docs/postgres/known-limitations). 

To configure and run your migration, perform the following steps:

  1. Optional: If you want to manage your own encryption keys for the destination instance, [ prepare Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/sql/docs/postgres/configure-cmek). 
  2. [ Create and run the migration job](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job). 

You can monitor the migration progress, as well as your destination instance health with Database Migration Service observability features. See [ Migration job metrics](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-metrics). 




## Finalize the migration

When you decide to switch your application to the new Cloud SQL for PostgreSQL instance, finalize the migration by following these steps:

  1. _Optional_ : [ Set up cascading read replicas](https://docs.cloud.google.com/database-migration/docs/postgres/set-up-cascading-replica). If you want to use cascading read replicas, you can configure them when the migration job enters the CDC phase. 
  2. Stop all write operations on your source database. You can switch them to read-only mode to retain operational functionality.
  3. [ Promote the migration job](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration).
  4. Optional: [ Verify migration data](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration) for completeness.



## What's next

Learn more about Google Cloud features for Cloud SQL for PostgreSQL. See [ Cloud SQL for PostgreSQL features](https://docs.cloud.google.com/sql/docs/postgres/features).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
