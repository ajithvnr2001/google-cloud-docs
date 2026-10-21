---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/migration-job-statuses/
title: Migration job status codes \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:24:40.939823+00:00
---

# Migration job status codes  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/migration-job-statuses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  Migration job status codes Stay organized with collections  Save and categorize content based on your preferences. 

The following table lists, describes, and provides user actions for migration job statuses for Database Migration Service.

Migration job status | Description | Possible substatus | Possible user actions  
---|---|---|---  
**Not started** | The migration job is ready but still not running. This status is relevant if the migration job was created but wasn't started. | None. | Start. Delete.  
**Starting...** | The migration job is in the process of being started. This is an intermediate status that occurs when a migration job is started. Starting the migration job takes between a few seconds and a few minutes. The status changes to `Running`. | None. | Delete.  
**Running** | The migration job is actively running. | Full dump, Change Data Capture (CDC) | Stop. Delete.  
**Running with errors** | This status means that Database Migration Service encountered errors with your migration. Faulty operations will be retried, and errors clear automatically once the underlying issue is resolved. Database Migration Service continues migrating data unaffected by the error. | Full dump, Change Data Capture(CDC) | Stop. Restart. Promote.  
**Completed** | The migration job is completed. In the continuous migration type, this occurs after a successful finalization.  | None. | Delete.  
**Failed** | The migration job failed because of an error. Based on the error type, the migration job may resume automatically after the issue is fixed. Otherwise, the failure is unrecoverable, and the migration job needs to be restarted.  | The last status before the migration job failed. Failed in Incremental load. | Restart. Delete.  
**Restarting** | The migration job is in the process of being restarted. | None. | Delete.  
**Stopped** | The migration job is stopped. | The last status before the migration job has stopped: Stopped in incremental load.  | If in the incremental load phase, then the migration job can be resumed, finalized, or deleted.   
**Resuming** | The migration job is in the process of being resumed. | None. | Delete.  
**Stopping...** | The migration job is in the process of stopping after `Stop` was invoked. This is an intermediate status that occurs when a user stops a migration job. Stopping the job takes around a minute, during which the status is `Stopping`. Subsequently, the status changes to `Stopped`. | None. | Delete.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
