---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-data-flow/
title: About data flow for Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:33.535824+00:00
---

# About data flow for Oracle to Cloud SQL for PostgreSQL  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-data-flow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  About data flow for Oracle to Cloud SQL for PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

There are two important concepts you need to understand to know how data flows from your source to the destination instance: migration types and migration phases. Database Migration Service supports two types of migration: **continuous** and **one-time**.

With **continuous** migrations, your data is migrated in two phases: full dump, and Change Data Capture (CDC). **One-time** migrations only involve a full dump phase.

## Full dump phase

The **full dump phase** is the first part of the migration process. During full dump, Database Migration Service connects to your source instance, reads the content of the databases you selected for migration, and then loads the data to the Cloud SQL for PostgreSQL destination instance. In this phase, Database Migration Service captures actual contents of your database. For one-time migrations, changes made to data in a batch that was already read aren't migrated.

During the full dump phase, Database Migration Service can open multiple connections to your source databases for improved performance. You can configure the number of concurrent connections when you [ create a migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/create-migration-job).

For granular control over your data movement, you can also perform the full dump and load the data to the destination instance on your own, outside of Database Migration Service. If you choose to perform this phase manually, your migration job will start with the CDC phase instead and Database Migration Service will expect that you provide the System Change Number (SCN) of your redo log files as the starting point.

## Change Data Capture (CDC)

When the **full dump** phase is over (or if you choose to perform the full dump yourself and start with the CDC phase), Database Migration Service switches to the CDC phase where it keeps monitoring your source databases for changes, and then continuously replicates them on the destination instance. In this phase, Database Migration Service doesn't copy actual data from your source databases: instead it reads log files to replicate changes in the destination.

Database Migration Service uses the Oracle LogMiner API to access and parse archived Oracle redo log files in your source database. Before you migrate your Oracle databases to Cloud SQL for PostgreSQL with Database Migration Service, we recommend that you adjust your Oracle redo log files settings for optimal performance and data fidelity. For more information, see [ Work with Oracle redo log files](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/work-with-oracle-database-redo-log-files).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
