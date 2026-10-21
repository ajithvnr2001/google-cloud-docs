---
url: https://docs.cloud.google.com/sql/docs/sqlserver/migrate-data-to-cloud-sql-instance/
title: About data migration in Cloud SQL \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:53.982160+00:00
---

# About data migration in Cloud SQL  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/migrate-data-to-cloud-sql-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  About data migration in Cloud SQL Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/migrate-data-to-cloud-sql-instance "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/migrate-data-to-cloud-sql-instance "View this page for the PostgreSQL database engine") | SQL Server

This page describes data migration options in Cloud SQL.

## Database Migration Service

You can migrate SQL Server databases to Cloud SQL for SQL Server instances with Database Migration Service by using a backup and restore flow. You first upload the full database backup and transaction log files to a Cloud Storage bucket. Database Migration Service then actively monitors your bucket and continuously replicates your data to the destination Cloud SQL for SQL Server instance. For more information, see [SQL Server migrations overview](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview) in the Database Migration Service documentation.

## Replicate from an external server

Another option for migrating data from an external server into Cloud SQL is to use replication. Cloud SQL supports various replication modes to migrate data into your instance.

For more information, see [About replicating from an external server](https://docs.cloud.google.com/sql/docs/sqlserver/replication).

## Limitations

  * If your instance has customized backup settings (for example, a [custom backup location](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backing-up#locationbackups)), then after you promote the instance, we recommend that you customize your backup settings again. During the promotion process, Cloud SQL resets your backup settings to their default values.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
