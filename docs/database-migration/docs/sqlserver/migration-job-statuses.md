---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-statuses/
title: Migration job status codes \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:39.676661+00:00
---

# Migration job status codes  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-job-statuses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Migration job status codes Stay organized with collections  Save and categorize content based on your preferences. 

The following table lists and describes existing migration job statuses:

Migration job status | Description | Possible substatus | Possible user actions  
---|---|---|---  
**Not started** | The migration job is ready but still not running. This status is relevant if the migration job was created but wasn't started. | None | Start. Delete.  
**Starting...** | The migration job is in the process of being started. This is an intermediate status that occurs when a migration job is started. Starting the migration job takes between a few seconds and a few minutes. The status changes to `Running`. | None | Delete.  
**Running** | The migration job is actively running.  
**Running with errors** | This status means that Database Migration Service encountered errors with your migration. Faulty operations will be retried, and errors clear automatically once the underlying issue is resolved. Database Migration Service continues migrating data unaffected by the error. | Incremental load. | Stop. Restart. Promote.  
**Completed** |  | None | Delete.  
**Failed** | The migration job failed because of an error. You need to restart the migration job after the issue is fixed.  
**Restarting** | The migration job is in the process of being restarted. | None | Delete.  
**Stopped** | The migration job is stopped. | The last status before the migration job has stopped. |   
**Resuming** | The migration job is in the process of being resumed. | None | Delete.  
**Stopping...** | The migration job is in the process of stopping after `Stop` was invoked. This is an intermediate status that occurs when a user stops a migration job. Stopping the job takes around a minute, during which the status is `Stopping`. Subsequently, the status changes to `Stopped`. | None | Delete  
**Ready to promote** | Database Migration Service stops continuous load when it detects a transaction log file whose name ends in the `.final` suffix (see [ naming convention associated with the final transaction log file](https://docs.cloud.google.com/database-migration/docs/sqlserver/export-backup-files). Once that transaction log file is replicated to the destination Cloud SQL instance, the migration job status changes to **Ready to promote**. This status doesn't occur if you just stop uploading transaction log backup files instead of using a file with the `.final` suffix in the name. | None | [ Promote](https://docs.cloud.google.com/database-migration/docs/sqlserver/finalize-migration)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
