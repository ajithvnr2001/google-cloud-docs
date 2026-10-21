---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/configure-source-database-csql/
title: Configure your source Cloud SQL for SQL Server instance \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:31.897321+00:00
---

# Configure your source Cloud SQL for SQL Server instance  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/configure-source-database-csql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Configure your source Cloud SQL for SQL Server instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure a Cloud SQL for SQL Server source for for continuous homogeneous SQL Server migrations.

In this migration path, Database Migration Service automatically handles all the required backup file exports to a Cloud Storage bucket when you migrate between two Cloud SQL for SQL Server instances.

To prepare your Cloud SQL for SQL Server instance for a homogeneous migration with Database Migration Service, do the following:

  1. Create a dedicated migration user account in your instance. See [ Create a user](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users) in the Cloud SQL documentation. 
  2. Assign the necessary privileges to the dedicated migration user account. Run the following commands: 

### SQL Server 2019 and earlier

For SQL Server 2019 and earlier versions, grant the `VIEW SERVER STATE` permission. 
         
         USE [master];
         GO
         
         GRANT VIEW SERVER STATE TO MIGRATION_USER;
         GO

Replace MIGRATION_USER with the name of the migration user account.

### SQL Server 2022 and later

For SQL Server 2022 and later versions, grant the `VIEW SERVER STATE` permission. 
         
         USE [master];
         GO
         
         GRANT VIEW SERVER PERFORMANCE STATE TO MIGRATION_USER;
         GO

Replace MIGRATION_USER with the name of the migration user account.

  3. [ Enable point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/configure-pitr) on your source instance. 



## What's next

Continue with your migration. See [ Migration guide for Cloud SQL for SQL Server sources](https://docs.cloud.google.com/database-migration/docs/sqlserver/csql-sql-server-src-guide).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
