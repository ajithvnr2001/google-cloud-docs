---
url: https://docs.cloud.google.com/database-migration/docs/overview/
title: Database Migration Service overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:25.017561+00:00
---

# Database Migration Service overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/overview)



Send feedback 

#  Database Migration Service overview Stay organized with collections  Save and categorize content based on your preferences. 

Migration is a process of moving data and metadata from a source database to a destination database. After your migration is completed, the destination database becomes the primary database that dependent applications can read and write to, and the source database can be shut down.

Database Migration Service helps you migrate your data to Google Cloud. The service supports database migrations into Cloud SQL and AlloyDB for PostgreSQL instances. Database Migration Service streamlines networking, manages the initial snapshot and ongoing replication, and provides status updates throughout the migration process.

With Database Migration Service, you can:

  * Perform different types of migrations.
  * Move your databases to Google Cloud with minimal downtime.
  * Use Gemini-powered conversion features in heterogeneous migrations.
  * Migrate encrypted data securely.
  * Monitor your migration job with observability metrics.



The following diagram shows the key features of Database Migration Service in the context of Google Cloud architecture:

![Architecture diagram showing data flow from on-premises or other clouds to Google Cloud using Database Migration Service, highlighting key features like homogeneous and heterogeneous migrations, minimal downtime, and Gemini-powered conversion.](https://docs.cloud.google.com/static/database-migration/docs/images/overview_dms_data_flow.svg) **Figure 1.** Database Migration Service architecture and data flow (click to enlarge).![](https://docs.cloud.google.com/static/database-migration/docs/images/overview_dms_data_flow.svg)

## Migration types

Migrations can be categorized into the following types:

### Continuous migration

Continuous (sometimes referred to as ongoing or online) migration is a continuous flow of changes from your source to your destination that follows an initial full dump and load. When the destination is ready for reads and writes, you finalize replication between the source and the destination. The destination Cloud SQL instance or AlloyDB for PostgreSQL cluster is then ready to be used as a standalone primary instance. Doing the switch when the source and destination are in sync gives you minimal downtime.

### One-time migration

A one-time migration is a single point-in-time snapshot of the database. Database Migration Service takes the snapshot from the source and applies it to the destination. This process is a dump and load, where the destination is ready to be used when the load completes. Any applications that depend on the source database can experience downtime during the migration process because there can be no new writes to this database while the migration is in progress.

### Homogeneous migrations

Homogeneous migrations take place when you migrate data between the same database technology. For example, from MySQL to Cloud SQL for MySQL.

For more information, see [ Homogeneous migrations](https://docs.cloud.google.com/database-migration/docs/homogeneous-migrations).

### Heterogeneous migrations

Unlike homogeneous migrations, in heterogeneous migrations, such as Oracle to Cloud SQL for PostgreSQL, the database technology of the source and destination are different.

For more information, see [ Heterogeneous migrations](https://docs.cloud.google.com/database-migration/docs/heterogeneous-migrations).

## Minimal downtime

Database Migration Service supports low downtime, continuous, serverless migrations for both homogeneous and heterogeneous migrations. The serverless architecture of Database Migration Service takes an initial snapshot of the source database to capture the current state of the data. Once the snapshot is complete, Database Migration Service loads the snapshot onto the destination database, and continuous data replication begins. Data replication is a continuous operation because it tracks and copies any changes made to the original database in real-time. It's based on Change Data Capture (CDC), a process that identifies and captures only the changes, such as inserts, updates, deletes that you made to the database after the initial snapshot is taken.

Such an approach minimises downtime for the following reasons:

  * Continuous replication is more efficient than replicating the entire database frequently, as it only focuses on modifications.
  * Data migrates while the source database remains operational.
  * Serverless migrations perform highly at scale.



## Accelerate code and schema conversion with Gemini

For heterogeneous migrations, Database Migration Service converts the schema and objects from your source database into a format that is compatible with your destination database. Conversion workspaces offer the following features:

  * Initial schema conversion that happens automatically, once you create your conversion workspace.
  * The interactive SQL editor that helps you fix conversion issues or adjust the schema to better fit your needs.
  * Assistance of Gemini conversion features.
  * Customization directives that you can use to override the rules of automated schema conversion.



For more information, see [ Gemini-powered conversion](https://docs.cloud.google.com/database-migration/docs/convert-sql-with-dms#gemini-conversion).

## Security and encryption

Database Migration Service migrates data securely by using SSL/TLS certificates to encrypt network connections and customer-managed encryption keys (CMEK) for continuous migrations.

For more information, see [ Security and encryption](https://docs.cloud.google.com/database-migration/docs/security-and-encryption).

## Observability metrics

Database Migration Service shows several diagrams that can help you understand the current state and progress of your migration job. Most migration scenarios let you filter the information in these diagrams for each database included in your migration job.

![Example charts showing migration job metrics in Database Migration Service, including storage usage and replication delay.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_migration_job_metrics.png) **Figure 1.** Sample observability charts for a migration job in Database Migration Service (click to enlarge). ![Example charts showing migration job metrics in Database Migration Service, including storage usage and replication delay.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/sqlserver-to-csql-pgsql/htm_sqlserver_migration_job_metrics.png)

For more information, see the migration job metrics pages that apply to your migration scenario.

## Use cases

Database Migration Service enables the following use cases:

Lift-and-shift migration to a managed service
    As part of an organization's move to Google Cloud, you can move from VM-based self-hosted databases to managed database cloud services. This lets you focus on the high availability, disaster recovery, and performance of running databases on managed services, instead of managing the infrastructure.
Multi-cloud continuous replication
    Much like the read replicas across regions, if data exists in another cloud provider, a migration job can continuously replicate the database into Google Cloud for multi-cloud read-availability. Database Migration Service doesn't support a dual-write scenario, that is writing to and reading from both the source and destination.

## What's next

Learn more about available migration scenarios:

Homogeneous migrations
    

  * [ Migrate to Cloud SQL for MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-src-and-dest)
  * [ Migrate to Cloud SQL for SQL Server](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)
  * [ Migrate to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest)
  * [ Migrate to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)


Heterogeneous migrations
    

  * [ Migrate from Oracle to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)
  * [ Migrate from Oracle to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)
  * [ Migrate from SQL Server to Cloud SQL for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)
  * [ Migrate from SQL Server to AlloyDB for PostgreSQL](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-alloydb/scenario-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
