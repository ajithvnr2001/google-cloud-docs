---
url: https://docs.cloud.google.com/database-migration/docs/mysql/guide-to-new-instance/
title: Migrate to a new Cloud SQL destination instance \u00a0|\u00a0 Database Migration Service for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:14.419209+00:00
---

# Migrate to a new Cloud SQL destination instance  |  Database Migration Service for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/mysql/guide-to-new-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ MySQL ](https://docs.cloud.google.com/database-migration/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview)



Send feedback 

#  Migrate to a new Cloud SQL destination instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to migrate your databases to a new Cloud SQL instance that Database Migration Service creates on your behalf when you configure the migration job. If your migration has different requirements, consider following a different migration flow. For more information, See [ Guide: Migrate to an existing Cloud SQL instance](https://docs.cloud.google.com/database-migration/docs/mysql/guide-to-existing-instance).

At a high level, the migration follows these steps:

  1. Configure the source database to allow Database Migration Service to move your data to the new databases.
  2. Create the connection profile and the migration job.
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
     * [ Supported sources and destinations](https://docs.cloud.google.com/database-migration/docs/mysql/scenario-overview#supported-src-and-dest) on the _Scenario overview_ page lists all supported source and destination versions. 
     * [ Known limitations](https://docs.cloud.google.com/database-migration/docs/mysql/known-limitations) describes supported data types, database sizes, and other limitations. 
     * Different network connectivity methods are available for different source databases. Consider and plan your network connectivity before you begin the migration procedures. For more information, see [ Networking overview](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods). 

Migrating to a new destination instance doesn't support Private Service Connect interfaces connectivity. If you want to use Private Service Connect interfaces connectivity, consider pre-creating your destination instance directly in Cloud SQL. See [ Guide: Migrate to an existing Cloud SQL instance](https://docs.cloud.google.com/database-migration/docs/mysql/guide-to-existing-instance). 

  2. _For one-time migrations_ : Consider the schedule for your migration. One-time migrations perform only a full dump and load operation without subsequent change data capture. We recommend that you disable writes on your source database for the migration process to avoid losing data. 
  3. Consider in which region you want to create the destination database. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region. 
  4. In the Google Cloud console, on the project selector page, select or [ create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. Enable the Database Migration Service and Cloud SQL Admin APIs. 

[ Enable the APIs](https://console.cloud.google.com/flows/enableapi?apiid=datamigration.googleapis.com,sqladmin.googleapis.com)




### Required roles

To get the permissions that you need to perform homogeneous MySQL migrations with Database Migration Service, ask your administrator to grant you the required IAM roles on your project:

  * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * [ Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation. 

These predefined roles contain the permissions required to perform homogeneous MySQL migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform homogeneous MySQL migrations with Database Migration Service: 

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

  1. Consider if you want to provide your own dump files or have Database Migration Service perform the full dump automatically: 
     * **Automatic dump (default)** : Database Migration Service connects to your source database and performs the initial schema and data dump automatically when the migration job starts. You don't need to prepare anything before you begin the migration. 
     * **Manual dump** : You can generate your own dump files and upload them to a Cloud Storage bucket. This approach can be useful if you want to reduce the initial load on your primary instance and take the full dump from a replica, run the dump during a specific maintenance window, or pass custom export flags. See [ Export a MySQL database with `mysqldump`](https://docs.cloud.google.com/database-migration/docs/mysql/mysql-dump). 
  2. [ Choose and configure your source network connectivity method](https://docs.cloud.google.com/database-migration/docs/mysql/networking-methods). 
  3. **For public IP allowlist connectivity** : At a later point, after Database Migration Service creates the destination instance, you might need to add the Cloud SQL public IP address to your firewall allowlist. Consult your network administrator on how to best schedule such configuration changes. 
  4. Configure your source database instance. 
     * For **continuous** migrations, see [ Configure source database for continuous migrations](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database-continuous). 
     * For **one-time** migrations, see [ Configure source database for one-time migrations](https://docs.cloud.google.com/database-migration/docs/mysql/configure-source-database). 
  5. [ Create the source connection profile](https://docs.cloud.google.com/database-migration/docs/mysql/create-connection-profiles). 



## Create and run the migration job

To configure and run your migration, perform the following steps:

  1. Optional: If you want to manage your own certificates for the migration job, [ prepare the necessary encryption keys](https://docs.cloud.google.com/sql/docs/mysql/configure-cmek). 
  2. [ Create and run the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job). 

You can monitor the migration progress, as well as your destination instance health with Database Migration Service observability features. See [ Migration job metrics](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-metrics). 




## Finalize the migration

When you decide to switch your application to the new Cloud SQL for MySQL instance, finalize the migration by following these steps:

### Continuous migrations

  1. Stop all write operations on your source database. You can switch them to read-only mode to retain operational functionality.
  2. [ Promote the migration job](https://docs.cloud.google.com/database-migration/docs/mysql/promote-migration).
  3. Optional: [ Verify migration data](https://docs.cloud.google.com/database-migration/docs/mysql/verify-migration) for completeness.



### One-time migrations

When Database Migration Service completes the full dump phase, the destination instance is automatically promoted to a standalone instance. To finalize the migration, follow these steps: 

  1. Optional: [ Verify migration data](https://docs.cloud.google.com/database-migration/docs/mysql/verify-migration) for completeness.
  2. Switch your application to connect to the new Cloud SQL for MySQL instance.



## What's next

Learn more about Google Cloud features for Cloud SQL. See [ Cloud SQL for MySQL features](https://docs.cloud.google.com/sql/docs/mysql/features).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
