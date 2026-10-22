---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/known-limitations/
title: Known limitations \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:39.927604+00:00
---

# Known limitations  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/known-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Known limitations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the known limitations for migrating from SQL Server to Cloud SQL for SQL Server with Database Migration Service.

## General limitations

  * Database Migration Service can migrate up to a maximum of 20 databases per migration job.

  * You can run only one migration job for a single destination Cloud SQL for SQL Server instance.

  * Database Migration Service doesn't migrate the [ SQL Server `master` database](https://learn.microsoft.com/en-us/sql/relational-databases/databases/master-database), user information (such as user logins), or jobs that aren't a part of a specific database.

  * [ Point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr) can't be enabled on your destination Cloud SQL instance during migration. You can enable this feature after the migration is complete.




## Limitations for Cloud SQL for SQL Server sources

  * For Cloud SQL for SQL Server sources, you can only create the source connection profile and migration job with Google Cloud CLI. You can use the Google Cloud console to monitor migration progress and metrics.

  * For Cloud SQL for SQL Server sources, Database Migration Service automatically handles all necessary backup file creation and uploads them to a Cloud Storage bucket. Database Migration Service first performs the full dump backup with stripe count set to `13`, and then continuously creates and exports transaction log backup files.

  * Database Migration Service doesn't remove any automatically exported backup files from your Cloud Storage bucket. We recommend that you configure a data retention period between `14` and `30` days for your backup files.

  * Database Migration Service doesn't encrypt the backup files that are automatically created for this migration flow. If you need to use encrypted backup files from your Cloud SQL for SQL Server instance, we recommend that you use the [ standard migration flow dedicated for self-managed or Amazon RDS sources](https://docs.cloud.google.com/database-migration/docs/sqlserver/guide).

  * Your source Cloud SQL for SQL Server must have point-in-time recovery (PITR) enabled so that Database Migration Service can create transaction log backup files.




## Limitations for self-managed or Amazon RDS sources

  * Database Migration Service migrates all data from the backup files you upload to the Cloud Storage bucket, but not all features present in your source database might be available in Cloud SQL for SQL Server. Database Migration Service migration jobs don't restore data that falls under an unsupported feature, but your destination Cloud SQL for SQL Server instance might produce warnings or errors in the logs.

Before you choose to migrate your SQL Server databases to Cloud SQL for SQL Server, make sure you consider [ SQL Server features unavailable for Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/features#general_sql_server_features_unavailable_for) in Cloud SQL for SQL Server documentation. You can also use Google Cloud Migration Center to discover possible limitations or gaps in feature support for your specific scenario. See [ Discover and import databases](https://docs.cloud.google.com/migration-center/docs/discover-and-import-databases) in the Migration Center documentation.

  * Your backup files can have a maximum size of 5 TB.

  * You can stripe your full backup file into smaller files if your database size exceeds 5 TB. Each stripe can have a maximum size of 5 TB.

  * You can use encrypted backup and transaction log files for your migration. If you want to use encrypted backup files, you must encrypt **every backup file** (full, differential, transaction log) you use for a specific database included in your migration. See [ Use encrypted backups](https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption).

  * Your source SQL Server instance can't use the **simple recovery model**. For more information on recovery models, see See [ Recovery Models (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server) in Microsoft documentation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
