---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide/
title: Migrate your SQL Server database to Cloud SQL for PostgreSQL \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:07.230262+00:00
---

# Migrate your SQL Server database to Cloud SQL for PostgreSQL  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  Migrate your SQL Server database to Cloud SQL for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to convert your SQL Server database to PostgreSQL syntax and migrate the data to Cloud SQL for PostgreSQL with Database Migration Service.

The migration process involves the following tasks:

  1. Configuring your source database for migration connectivity and preparing the data for conversion to PostgreSQL.

  2. Creating the destination Cloud SQL for PostgreSQL instance.

  3. Converting your SQL Server schema and other objects to PostgreSQL syntax with a Database Migration Service conversion workspace.

  4. Creating and running the migration job in Database Migration Service.

  5. Monitoring the migration job progress with Database Migration Service observability features.

  6. Promoting the migration job after the data is fully migrated.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * Cloud SQL (See [ Cloud SQL pricing](https://docs.cloud.google.com/sql/pricing).)
  * If used for storing Customer-managed Encryption Keys (CMEK): Cloud Storage (See [ Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).) 



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

## Before you begin

  1. Verify if this migration path can fully support your scenario. See the following pages: 
     * [ Supported sources and destinations](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview#supported-src-and-dest) on the _Scenario overview_ page lists all supported source and destination versions. 
     * [ Known limitations](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/known-limitations) describes supported data types, database sizes, and other limitations.
     * [ Networking overview](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-overview) describes available network connectivity solutions. 

To migrate your data, Database Migration Service needs to establish a network connection to your source and destination instances. Depending on your architecture, you might need additional preparation to facilitate network connectivity. 

  2. _Optional_ : Database Migration Service supports failback replication. Consider if you want to run failback replication after you complete the standard migration job. You can prepare for failback replication as you plan your migration job, or do it before you promote the standard migration job. For more information on failback migrations, see the following pages: 

     * [ Failback migrations overview](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/failback-migration). 
     * [ Failback migrations guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide-failback-migration). 
  3. _For one-time migrations_ : Consider the schedule for your migration. One-time migrations perform only a full dump and load operation without subsequent change data capture. We recommend that you disable writes on your source database for the migration process to avoid losing data. 
  4. Consider in which region you want to create the destination database. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region. 
  5. In the Google Cloud console, on the project selector page, select or [ create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. Enable the Database Migration Service, Compute Engine, Cloud Storage, and Cloud SQL Admin APIs. 

[ Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,datamigration.googleapis.com,sqladmin.googleapis.com,storage.googleapis.com)




### Required roles

To get the permissions that you need to perform heterogeneous SQL Server migrations with Database Migration Service, ask your administrator to grant you the required IAM roles on your project:

  * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * [ Cloud SQL Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation. 

These predefined roles contain the permissions required to perform heterogeneous SQL Server migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform heterogeneous SQL Server migrations with Database Migration Service: 

  * `datamigration.*`
  * `cloudaicompanion.entitlements.get`

This permission is included in the `roles/datamigration.admin` role. It is required for the [ Gemini-enhanced conversion features](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/code-conversion-with-gemini). 

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

## Step 1. Prepare your source database

To prepare your source data for migration, follow these steps:

  1. Set up source database connectivity. Do the following: 
     1. Optional: Consider if you want to use SSL/TLS certificates to secure the source network connection. For more information, see [ Secure network connections with TLS](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/encrypt-connections-with-certificates). 

Database Migration Service offers different TLS variants to secure network connections: basic or TLS. Depending on which variant you want to use, you might need to perform additional configuration steps on your source database. 

     2. [ Choose and configure your source network connectivity method](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-methods-source). 
  2. [ Configure your source database instance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-source-database). 

In this step, you create a dedicated migration database user account and enable the necessary replication features: snapshot isolation, and table-level change data capture (CDC). 

  3. [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-source-connection-profile). 

Connection profiles contain information necessary for Database Migration Service to establish the connection to your source database. Connection details vary depending on which [ source network connectivity method](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-methods-source) you use. 




## Step 2. Prepare your Cloud SQL for PostgreSQL destination instance

To configure your destination Cloud SQL instance, perform the following steps:

  1. [ Choose and configure your destination network connectivity method](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-methods-destination). 
  2. [ Create and configure your Cloud SQL for PostgreSQL destination instance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-destination-database). 

Make sure you use enough compute and memory resources to cover your migration needs. For more information, see [ Migration recommendations](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/known-limitations#recommendations). 

  3. [ Create a destination connection profile](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-destination-connection-profile). 

Connection profiles contain information necessary for Database Migration Service to establish the connection to your destination database. Connection details vary depending on which [ destination network connectivity method](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-methods-destination) you use. 




## Step 3. Convert SQL Server objects to PostgreSQL syntax

Databases can often have thousands of objects. Converting them all in a single session might be a challenging process. With conversion workspaces, you can divide the conversion process into multiple phases where you add new objects to the conversion, fix the issues, and then test them in your destination database.

To convert objects from your source database, do the following:

  1. [ Create the conversion workspace and run the initial conversion](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-conversion-workspace). 
  2. [ Fix conversion issues and apply the schema to your destination database](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/convert-sql). **Tip:** You can use [ Gemini-assisted conversion features](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/about-conversion-workspaces#ai-conversion) to expedite the conversion process. 



## Step 4. Create and run the migration job

To configure and run your migration, perform the following steps:

  1. Optional: If you want to manage your own certificates for the migration job, [ prepare the necessary encryption keys](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/cmek-for-migration-jobs). 
  2. [ Create and run the migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/create-migration-job). 

The destination Cloud SQL database is writable during the migration to allow DML changes to be applied if needed. Take care not to make any changes to the database configuration or table structures which might break the migration process or impact data integrity. 

You can monitor the migration progress, as well as your destination instance health with Database Migration Service observability features. See [ Migration job metrics](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/migration-job-metrics). 




## Step 5. Finalize the migration

When you decide to switch your application to the new Cloud SQL for PostgreSQL instance, finalize the migration by following these steps:

### One-time migrations

When Database Migration Service completes the full dump phase, your migration job status changes to **Ready for promote**. 

  1. Optional: [ Verify migration data](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/verify-migration) for completeness. 
  2. [ Promote the migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/finalize-migration).



### Continuous migrations

  1. _Optional_ : Database Migration Service supports failback replication. We recommend that you configure and run the failback migration before you promote the standard migration job. For more information on failback migrations, see the following pages: 

     * [ Failback migrations overview](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/failback-migration). 
     * [ Failback migrations guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide-failback-migration). 
  2. Stop all write operations on your source database. You can switch them to read-only mode to retain operational functionality.
  3. Optional: [ Verify migration data](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/verify-migration) for completeness.
  4. [ Promote the migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/finalize-migration).



You can now clean up all Database Migration Service entities such as connection profiles, migration jobs, and conversion workspaces. You can also choose to retain them and reuse these entities for another migration.

## What's next

  * Learn more about Google Cloud features for Cloud SQL for PostgreSQL. See [ Cloud SQL for PostgreSQL features](https://docs.cloud.google.com/sql/docs/postgres/features). 
  * Consider configuring a failback migration job. See [ Failback migrations overview](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/failback-migration). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
