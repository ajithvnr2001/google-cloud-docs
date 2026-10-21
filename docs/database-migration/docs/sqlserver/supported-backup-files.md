---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/supported-backup-files/
title: Supported types of backup files \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:50.035816+00:00
---

# Supported types of backup files  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/supported-backup-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Supported types of backup files Stay organized with collections  Save and categorize content based on your preferences. 

For Cloud SQL for SQL Server sources, Database Migration Service can automatically export the relevant source files directly from your source instance. When you migrate from self-managed or Amazon RDS sources, you need to manually export backup files to a Cloud Storage bucket. For migrations from self-managed or Amazon RDS sources, Database Migration Service supports the following backup types:

Full backups
    Full backups are the backbone of the migration process. They contain all the data in your database at the point in time when you export them. **The full backup file is required for migration.**
Differential backups
    Differential backups contain all the source data that appeared in your database since the last full backup file. Differential backups are useful if you have a lot of data to replicate and want to handle it in bulk rather than upload multiple transaction log files. **The differential backup file is optional for migration.**
Transaction log files
    These files contain a list of change operations that take place in your database. Database Migration Service uses this information to replicate data updates in your destination database during the Change Data Capture (CDC) phase. 

For homogeneous SQL Server migrations, Database Migration Service supports only the continuous migration type (for more information see [ Continuous migrations data flow](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview#data-flow-migration-types)). This means that migration jobs always proceed to the CDC phase, but you don't get errors if you don't upload any transaction log files. If you don't upload any transaction log files, you need to promote the migration job when the initial load phase is over. See [ Promote a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/finalize-migration). 

As you prepare the backup files for your migration, make sure you consider the following:

  * Naming conventions: Each backup file type needs to use a specific naming convention. See [ Prepare your backup files](https://docs.cloud.google.com/database-migration/docs/sqlserver/export-backup-files).

  * Folder structure: Each backup file type needs to be stored in a separate folder in the Cloud Storage bucket you use for migration. See [ Store backup files in a Cloud Storage bucket](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets).

  * Encryption: You can use encrypted backups for your migration. If you want to encrypt the backup files, you need to encrypt all types of backup files you use for a specific database included in your migration. See [ Use encrypted backup files](https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption).

  * Migration job configuration: If you use a differential backup file for any database included in your migration, you need to configure the migration job so that Database Migration Service can recognize the differential backup files in your Cloud Storage bucket. See [ Create a migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/create-migration-job)




## What's next

For a detailed step-by-step migration guide, see [ Cloud SQL for SQL Server migration guide for self-managed and Amazon RDS sources](https://docs.cloud.google.com/database-migration/docs/sqlserver/guide).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
