---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview/
title: Oracle to AlloyDB for PostgreSQL migration overview \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:23.707998+00:00
---

# Oracle to AlloyDB for PostgreSQL migration overview  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Oracle to AlloyDB for PostgreSQL migration overview Stay organized with collections  Save and categorize content based on your preferences. 

With Database Migration Service, you can convert your Oracle database schema, tables, and code objects to PostgreSQL syntax, and then migrate data from your Oracle databases to AlloyDB for PostgreSQL. Database Migration Service offers support for multiple different Oracle offerings, including Bare Metal Solution, Oracle Real Application Clusters (RAC), and self-managed instances.

This page provides an overview of the key Database Migration Service features for heterogeneous Oracle to AlloyDB for PostgreSQL migrations:

  * Supported source and destination lists all Oracle versions supported by Database Migration Service.

  * Code and schema conversion describes how Database Migration Service can help you convert your schemas, tables, and other objects from Oracle syntax to PostgreSQL syntax.

  * Continuous migrations data flow provides an end-to-end overview of how your data moves in Google Cloud during the migration process.

  * Monitoring gives an introduction for logs and metrics that can help you observe the progress and health of your migration job.

  * Migration security looks at encryption features offered by Database Migration Service.




## Supported source and destination databases

Database Migration Service supports the following Oracle databases as migration sources:

  * Amazon RDS for Oracle
  * Self-hosted deployments, including: 
    * Oracle Single Instance Database Deployment
    * Oracle Exadata
    * Oracle Active Data Guard
    * Oracle Real Application Clusters (RAC)



Full support also depends on your source Oracle version. The following table lists all supported versions for heterogeneous Oracle migrations: 

Source databases | Destination databases  
---|---  
Oracle 11g, Version 11.2.0.4  |  AlloyDB for PostgreSQL 12, 13, 14, 15, 16, 17, 18.  
Oracle 12c, Version 12.1.0.2  
Oracle 12c, Version 12.2.0.1  
Oracle 18c  
Oracle 19c  
Oracle 21c  
  
## Unsupported source databases

Database Migration Service doesn't support migrating from Oracle Autonomous Database.

## Code and schema conversion

Database Migration Service conversion workspaces provide an interactive editor experience where you can convert your schemas, tables, and other objects from Oracle syntax to PostgreSQL syntax. Interactive conversion workspaces also provide support for Gemini-assisted workflows with code explainability and conversion issue fixing.

To learn more, see [ Conversion workspaces](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-conversion-workspaces).

## Migration data flow

For heterogeneous Oracle migrations to PostgreSQL, Database Migration Service supports _continuous_ and _one-time_ migration flows. With continuous migrations, your data is first loaded from a full dump, and then continuously updated based on data change information surfaced from [ database log files](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-data-flow#cdc). One-time migrations only involve the full dump phase.

![Data flow diagram for Oracle to AlloyDB for PostgreSQL migration using Database Migration Service, showing continuous replication from source to destination.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/oracle-to-alloydb/oracle_alloydb_htm_data_flow_v0.svg) **Figure 1.** Continuous data movement during a Database Migration Service heterogeneous migration from Oracle to AlloyDB for PostgreSQL. (click to enlarge) ![Data flow diagram for Oracle to AlloyDB for PostgreSQL migration using Database Migration Service, showing continuous replication from source to destination.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/oracle-to-alloydb/oracle_alloydb_htm_data_flow_v0.svg)

At a high level, your data moves through the migration phases as follows:

### One-time migrations

  1. You use Database Migration Service conversion workspace to convert your schemas, tables, and other objects from Oracle syntax to PostgreSQL syntax. 

Oracle databases can often have several thousand objects whose schema you need to convert. With Database Migration Service, you can divide your work into multiple phases. Database Migration Service can connect to your source databases and pull the required schema information when needed. 

  2. When you finish translating all your entities to PostgreSQL syntax, you apply the schema to the databases in the destination instance. 

The goal of this stage is to prepare your destination databases so that Database Migration Service can later replicate the data from source tables to their correct equivalents in AlloyDB for PostgreSQL. 

Once your schema is applied, you can begin the data migration.

  3. The **full dump phase** is the only part of the one-time migration process. During this phase, Database Migration Service connects to your source instance, reads the contents of the tables you selected for migration, and then loads the data to the AlloyDB for PostgreSQL destination instance. 

For one-time migrations, we recommend that you disable writes on the source database during the full dump phase. This way you can avoid avoid losing data created after the migration process starts. 

  4. When the full dump phase is over, you can promote the destination database and switch your application to use the new destination database. 




### Continuous migrations

  1. You use Database Migration Service conversion workspace to convert your schemas, tables, and other objects from Oracle syntax to PostgreSQL syntax. 

Oracle databases can often have several thousand objects whose schema you need to convert. With Database Migration Service, you can divide your work into multiple phases. Database Migration Service can connect to your source databases and pull the required schema information when needed. 

  2. When you finish translating all your entities to PostgreSQL syntax, you apply the schema to the databases in the destination instance. 

The goal of this stage is to prepare your destination databases so that Database Migration Service can later replicate the data from source tables to their correct equivalents in AlloyDB for PostgreSQL. 

Once your schema is applied, you can begin the data migration.

  3. The **full dump phase** is the first part of the migration process. There are two ways in which you can complete full dump: 

     * Automatic: Database Migration Service connects to your source instance, reads the contents of the tables you selected for migration, and then loads the data to the AlloyDB for PostgreSQL destination instance. 

In this phase, Database Migration Service captures actual contents of your database. 

     * Manual: You can skip the full dump phase and perform it yourself outside Database Migration Service. If you do, you can start the migration process with the change data capture (CDC) phase by providing an Oracle System Change Number as the starting point for replication. 
  4. For continuous migrations, when the full dump phase is over, Database Migration Service switches to the **CDC phase**. During CDC, Database Migration Service keeps monitoring your source databases for changes, and then continuously replicates them on the destination instance. 

In the CDC phase, Database Migration Service doesn't copy actual data from your source tables: instead, it reads information extracted from [ database log files](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-data-flow#cdc) to replicate changes in the destination. For more information about this mechanism, see [ Change Data Capture](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/about-data-flow#cdc). You can stop the ongoing replication and promote the migration job when you want to switch your application so that it uses the AlloyDB for PostgreSQL destination instance as the production database. 




For a detailed, step-by-step migration guide, see [ Oracle to AlloyDB for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/guide).

## Monitoring

![Example chart showing replication delay metrics for an Oracle to AlloyDB for PostgreSQL migration job in Database Migration Service.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_migration_job_metrics.png) **Figure 2.** Sample observability chart displaying replication delay in a Database Migration Service migration job. (click to enlarge) ![Example chart showing replication delay metrics for an Oracle to AlloyDB for PostgreSQL migration job in Database Migration Service.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_migration_job_metrics.png)

Database Migration Service provides extensive logging and observability capabilities to help you monitor the migration progress. These features include real-time diagnostics for replication delay and CDC progress, as well as detailed logs for AlloyDB for PostgreSQL destination instance health and migration job state.

For more details, see [Migration job metrics](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/migration-job-metrics).

## Migration security

Database Migration Service provides multiple encryption mechanisms you can use for additional security during the migration process. These mechanisms include:

  * SSL/TLS certificates for encrypting the network connections between Database Migration Service and source databases. For more details, see [ Encryption overview](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/encrypt-connections-with-certificates).

  * Encryption certificates for securing data movement during full dump and CDC phases. For more details, see [ CMEK for migration jobs](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/cmek-for-migration-jobs).




## What's next

  * To learn more about Oracle data type and feature support in Database Migration Service, see [ Known limitations](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/known-limitations).

  * To get a complete, step-by-step migration walkthrough, see [ Oracle to AlloyDB for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
