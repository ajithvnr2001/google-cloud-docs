---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/failback-migration/
title: Failback migrations \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:47.475643+00:00
---

# Failback migrations  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/failback-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  Failback migrations Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Failback migrations (sometimes referred to as _failback replication_), let you push CDC updates back to your original SQL Server source from the destination Cloud SQL for PostgreSQL instance after you complete the migration. This feature keeps your original source database alive and up to date in case you need to switch your application back to the SQL Server database.

In Database Migration Service, failback migrations use a very similar flow to the standard migrations: you configure your source and destination, create the connection profiles, and then run a migration job. The biggest difference is that the failback migration jobs require access to your original migration job and the conversion workspace. At a high-level, setting up failback replication is a two-step process:

  1. First, migrate your SQL Server with Database Migration Service to Cloud SQL for PostgreSQL. See [ SQL Server to Cloud SQL for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide).

  2. Before you promote the new Cloud SQL for PostgreSQL instance, you begin setting up the failback replication migration job. In this scenario, your original SQL Server now becomes the _destination_ , and your migrated Cloud SQL for PostgreSQL instance is the _source_. You need to configure the user accounts and network connectivity to match this role reversal. See [ Failback migrations guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide-failback-migration).

  3. Once the failback migration job is prepared, promote the original migration job. After the promotion is complete, you can start the failback migration process.




## Known limitations

  * Failback migrations only support Private Service Connect for connectivity to your original source SQL Server instance. Depending on your database type, this connectivity method might require additional networking components.
  * Failback migration jobs aren't supported for instance instances that require [ instance Auth Proxy](https://docs.cloud.google.com/sql/docs/postgres/sql-proxy).
  * You can create failback migration jobs only with Google Cloud CLI.
  * The original and the failback migration jobs must be in the same project and it must be a project that hosts the destination Cloud SQL for PostgreSQL instance.
  * To delete the original migration job, you first need to delete any existing failback migration jobs.
  * Failback migration jobs perform only Change Data Capture (CDC) operations. Full backfills aren't supported by failback migration jobs.
  * Failback migration jobs replicate data only for tables that are part of the original migration job. Tables created in the destination Cloud SQL for PostgreSQL instance aren't replicated back to the original source database.
  * For SQL Server tables without primary keys or unique indexes, failback migration jobs replicate data in append-only mode. That is, `INSERT` and `UPDATE` operations are performed as `INSERT`.
  * Schema changes for the replicated tables are unsupported during failback replication.
  * Similar to other heterogeneous migrations, point-in-time consistency is not maintained by failback migration jobs on the SQL Server instance. SQL Server writer will bypass foreign key validations to avoid integrity errors.
  * Failback migration jobs don't fire the `NOT FOR REPLICATION` triggers on the SQL Server instance.
  * You can't perform major version upgrades for Cloud SQL for PostgreSQL instances during the failback migration jobs.
  * You can't create a failback migration job to read data from a Cloud SQL read replica.
  * Database Migration Service doesn't consume replication slots when you stop the failback migration job. Stopping a migration job for longer periods of time might cause significant WAL file growth, potentially causing instance failure. We recommend that you stop active migration jobs for short periods of time to avoid disruptions. The `max_slot_wal_keep_size` setting on your instance to can help you estimate how quickly your log files can fill up available disk space.



## What's next

  * To learn more about SQL Server data type and feature support in Database Migration Service, see [ Known limitations](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/known-limitations).

  * To get a complete, step-by-step migration walkthrough for standard migrations, see [ SQL Server to Cloud SQL for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide).

  * To see the full guide for failback migrations, see [ Failback migrations guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide-failback-migration).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
