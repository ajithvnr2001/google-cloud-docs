---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/guide/
title: Migrate your Oracle database to AlloyDB for PostgreSQL \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:30.620507+00:00
---

# Migrate your Oracle database to AlloyDB for PostgreSQL  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Migrate your Oracle database to AlloyDB for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to convert your Oracle database to PostgreSQL syntax and migrate the data to AlloyDB for PostgreSQL with Database Migration Service.

The migration process involves the following tasks:

  1. Configuring your source database for migration connectivity and preparing the data for conversion to PostgreSQL.

  2. Creating the destination AlloyDB for PostgreSQL instance.

  3. Converting your Oracle schema and other objects to PostgreSQL syntax with a Database Migration Service conversion workspace.

  4. Creating and running the migration job in Database Migration Service.

  5. Monitoring the migration job progress with Database Migration Service observability features.

  6. Promoting the migration job after the data is fully migrated.




## Costs

In this document, you use the following billable components of Google Cloud: 

  * AlloyDB for PostgreSQL (See [ AlloyDB for PostgreSQL pricing](https://docs.cloud.google.com/alloydb/pricing).)
  * If used for storing Customer-managed Encryption Keys (CMEK): Cloud Storage (See [ Cloud Storage pricing](https://docs.cloud.google.com/storage/pricing).) 



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

## Before you begin

  1. Verify if this migration path can fully support your scenario. See the following pages: 
     * [ Supported sources and destinations](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview#supported-src-and-dest) on the _Scenario overview_ page lists all supported source and destination versions. 
     * [ Known limitations](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/known-limitations) describes supported data types, database sizes, and other limitations.
     * [ Networking overview](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-overview) describes available network connectivity solutions. 

To migrate your data, Database Migration Service needs to establish a network connection to your source and destination instances. Depending on your architecture, you might need additional preparation to facilitate network connectivity. 

  2. _For one-time migrations_ : Consider the schedule for your migration. One-time migrations perform only a full dump and load operation without subsequent change data capture. We recommend that you disable writes on your source database for the migration process to avoid losing data. 
  3. Consider in which region you want to create the destination database. Database Migration Service is a fully-regional product, meaning all entities related to your migration (source and destination connection profiles, migration jobs, destination databases, conversion workspaces) must be saved in a single region. 
  4. In the Google Cloud console, on the project selector page, select or [ create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. Enable the Database Migration Service, Compute Engine, Cloud Storage, and Cloud SQL Admin APIs. 

[ Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,datamigration.googleapis.com,sqladmin.googleapis.com,storage.googleapis.com)




### Required roles

To get the permissions that you need to perform heterogeneous SQL Server migrations with Database Migration Service, ask your administrator to grant you the required IAM roles on your project:

  * [ Database Migration Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/datamigration#datamigration.admin) (`roles/datamigration.admin`) 
  * [ AlloyDB Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`) 



For more information about granting roles, see [ Manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) in the Identity and Access Management documentation. 

These predefined roles contain the permissions required to perform heterogeneous SQL Server migrations with Database Migration Service. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to perform heterogeneous SQL Server migrations with Database Migration Service: 

  * `datamigration.*`
  * `cloudaicompanion.entitlements.get`

This permission is included in the `roles/datamigration.admin` role. It is required for the [ Gemini-enhanced conversion features](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/code-conversion-with-gemini). 

  * `alloydb.clusters.create`
  * `alloydb.clusters.get`
  * `alloydb.clusters.list`
  * `alloydb.clusters.update`
  * `alloydb.clusters.delete`
  * `alloydb.instances.create`
  * `alloydb.instances.get`
  * `alloydb.instances.list`
  * `alloydb.instances.update`
  * `alloydb.instances.delete`
  * `alloydb.operations.get`
  * `alloydb.users.list`
  * `alloydb.users.get`
  * `alloydb.users.create`
  * `alloydb.users.update`
  * `alloydb.users.delete`



## Step 1. Prepare your source database

To prepare your source data for migration, follow these steps:

  1. Set up source database connectivity. Do the following: 
     1. Optional: Consider if you want to use SSL/TLS certificates to secure the source network connection. For more information, see [ Secure network connections with TLS](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/encrypt-connections-with-certificates). 

SSL/TLS encryption is supported for Oracle version 12 and later. Database Migration Service supports only the TLS encryption method. Depending on your SSL/TLS configuration, you might need to perform additional configuration steps on your source database. 

     2. [ Choose and configure your source network connectivity method](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source). 
  2. Configure your source database instance. 
     * For **continuous** migrations, see [ Configure source database for continuous migrations](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-source-database). 
     * For **one-time** migrations, see [ Configure source database for a one-time migration](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-source-database-one-time). 

In this step, you create a dedicated migration database user account and enable the necessary replication features. 

  3. Optional: [ Optimize your log file configuration](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/work-with-oracle-database-redo-log-files). 

Accessing archived log files inherently adds some latency to the migration process. You can adjust certain log file settings to control the latency impact. 

  4. [ Create a source connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-source-connection-profile). 

Connection profiles contain information necessary for Database Migration Service to establish the connection to your source database. Connection details vary depending on which [ source network connectivity method](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-source) you use. 




## Step 2. Prepare your AlloyDB for PostgreSQL destination instance

To configure your destination Cloud SQL instance, perform the following steps:

  1. [ Choose and configure your destination network connectivity method](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-destination). 
  2. [ Create and configure your AlloyDB for PostgreSQL destination instance](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/configure-destination-database). 

Make sure you use enough compute and memory resources to cover your migration needs. For more information, see [ Migration recommendations](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/known-limitations#recommendations). 

  3. [ Create a destination connection profile](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-destination-connection-profile). 

Connection profiles contain information necessary for Database Migration Service to establish the connection to your destination database. Connection details vary depending on which [ destination network connectivity method](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/networking-methods-destination) you use. 




## Step 3. Convert Oracle objects to PostgreSQL syntax

Databases can often have thousands of objects. Converting them all in a single session might be a challenging process. With conversion workspaces, you can divide the conversion process into multiple phases where you add new objects to the conversion, fix the issues, and then test them in your destination database.

To convert objects from your source database, do the following:

  1. [ Create the conversion workspace and run the initial conversion](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-conversion-workspace). 
  2. [ Fix conversion issues and apply the schema to your destination database](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/convert-sql). **Tip:** You can use [ Gemini-assisted conversion features](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces#ai-conversion) to expedite the conversion process. 



## Step 4. Create and run the migration job

To configure and run your migration, perform the following steps:

  1. Optional: If you want to manage your own certificates for the migration job, [ prepare the necessary encryption keys](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/cmek-for-migration-jobs). 
  2. Optional: If you want to perform the **full dump** phase yourself, you can export all your data from the Oracle source database and load it to the destination AlloyDB for PostgreSQL instance outside Database Migration Service. 

If you decide to perform the full dump outside the migration job flow, make sure you record the System Change Number (SCN) where Database Migration Service should begin the CDC replication. 

  3. [ Create and run the migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-migration-job). 

The destination database is writable during the migration to allow DML changes to be applied if needed. Take care not to make any changes to the database configuration or table structures which might break the migration process or impact data integrity. 

You can monitor the migration progress, as well as your destination instance health with Database Migration Service observability features. See [ Migration job metrics](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/migration-job-metrics). 




## Step 5. Finalize the migration

When you decide to switch your application to the new AlloyDB for PostgreSQL instance, finalize the migration by following these steps:

### One-time migrations

When Database Migration Service completes the full dump phase, your migration job status changes to **Ready for promote**. 

  1. Optional: [ Verify migration data](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/verify-migration) for completeness. 
  2. [ Promote the migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/finalize-migration).



### Continuous migrations

  1. Stop all write operations on your source database. You can switch them to read-only mode to retain operational functionality.
  2. Optional: [ Verify migration data](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/verify-migration) for completeness.
  3. [ Promote the migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/finalize-migration).



You can now clean up all Database Migration Service entities such as connection profiles, migration jobs, and conversion workspaces. You can also choose to retain them and reuse these entities for another migration.

## What's next

Learn more about Google Cloud features for AlloyDB for PostgreSQL. See [ AlloyDB for PostgreSQL features](https://docs.cloud.google.com/alloydb/docs/overview#features).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
