---
url: https://docs.cloud.google.com/sql/docs/mysql/migrate-data-to-cloud-sql-instance/
title: About data migration in Cloud SQL \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:54.432327+00:00
---

# About data migration in Cloud SQL  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/migrate-data-to-cloud-sql-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  About data migration in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/migrate-data-to-cloud-sql-instance "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/migrate-data-to-cloud-sql-instance "View this page for the SQL Server database engine")

This page describes data migration options in Cloud SQL.

## Database Migration Service

When you use Database Migration Service, you can create the destination Cloud SQL instance when you create a migration job. Database Migration Service uses migration jobs to migrate data from your source database instance to the destination Cloud SQL instance. For more information, see [ Create a migration job to a new destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job).

However, you might want to create your destination Cloud SQL instance outside of Database Migration Service. For example, you can use Terraform or other Infrastructure-As-Code (IaC) tools. In that case, after creating the Cloud SQL instance, you can still use Database Migration Service to migrate data to it. For more information, see [ Create a migration job to an existing destination instance](https://docs.cloud.google.com/database-migration/docs/mysql/create-migration-job-existing-instance).

## Replicate from an external server

Another option for migrating data from an external server into Cloud SQL is to use replication. Cloud SQL supports various replication modes to migrate data into your instance.

For more information, see [About replicating from an external server](https://docs.cloud.google.com/sql/docs/mysql/replication/external-server).

To set up Cloud SQL for data migration by using replication, see [Configure Cloud SQL and the external server for replication](https://docs.cloud.google.com/sql/docs/mysql/replication/configure-replication-from-external).

Cloud SQL for MySQL also supports the migration of external MySQL databases from Percona XtraBackup physical files. By using physical files to set up replication instead of logical dump files, you can migrate your external MySQL databases into Cloud SQL for MySQL instances up to 3 times faster than using logical dump files in a parallel migration and up to 10 times faster than using logical dump files in a single-threaded migration. 

For more information, see [Migrate to Cloud SQL from an XtraBackup physical file](https://docs.cloud.google.com/sql/docs/mysql/migrate-xtrabackup-physical-file). 

## Limitations

  * If your instance has customized backup settings (for example, a [custom backup location](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/backing-up#locationbackups)), then after you promote the instance, we recommend that you customize your backup settings again. During the promotion process, Cloud SQL resets your backup settings to their default values.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
