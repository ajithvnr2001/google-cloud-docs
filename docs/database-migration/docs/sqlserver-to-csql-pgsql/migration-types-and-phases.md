---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/migration-types-and-phases/
title: About data flow for SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:04.039704+00:00
---

# About data flow for SQL Server to Cloud SQL for PostgreSQL  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/migration-types-and-phases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  About data flow for SQL Server to Cloud SQL for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

There are two important concepts you need to understand to know how data flows from your source to the destination instance: migration types and migration phases. Database Migration Service supports two types of migration: **continuous** and **one-time**.

With **continuous** migrations, your data is migrated in two phases: full dump, and Change Data Capture (CDC). **One-time** migrations only involve a full dump phase.

## Full dump phase

The **full dump phase** is the first part of the migration process. During full dump, Database Migration Service connects to your source instance, reads the content of the tables you selected for migration, and then loads the data to the destination instance. In this phase, Database Migration Service captures actual contents of your database. For one-time migrations, changes made to data in a batch that was already read aren't migrated.

The full dump phase depends on your source database snapshot consistency. To ensure snapshot consistency, Database Migration Service requires that you enable snapshot isolation when you [ configure your source database for migration](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-source-database). Enabling snapshot isolation creates a temporary view of your database at the start of the full dump process. This ensures that the data being copied remains consistent, even if other users are making changes to the live tables at the same time. Enabling snapshot isolation might have a slight performance impact, but it's essential for reliable data extraction.

## Change Data Capture (CDC)

When the **full dump** phase is over, Database Migration Service switches to the CDC phase where it keeps monitoring your source database for changes, and then continuously replicates them on the destination instance.

In this phase, Database Migration Service doesn't copy actual data from your source database: instead, it uses the [ SQL Server change data capture mechanism](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server) to read information from dedicated _change tables_. As DML events are applied to the tables in your source database, the changes are recorded in the corresponding change tables. These change tables have the same structure as the source tables, but with extra columns to include the metadata for the changes. Only committed transactions are added to the change tables, along with the log sequence number (LSN) of the commit operation.

Database Migration Service requires that you enable the change data capture mechanism on your source database for the migration. When this feature is active, your source database is subject to certain operational limitations. For example, you can't rename columns in your schema, or you might need to adjust maximum size limits for write operations that involve Large Objects (LOBs). For more information about how the change data capture feature in SQL Server can impact your source database, see [ Known limitations](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/known-limitations#cdc-considerations).

## What's next

  * To learn more about data and feature support for heterogeneous SQL Server migrations with Database Migration Service, see [ Scenario overview](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview).

  * To get a complete, step-by-step migration walkthrough, see [ SQL Server to Cloud SQL for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
