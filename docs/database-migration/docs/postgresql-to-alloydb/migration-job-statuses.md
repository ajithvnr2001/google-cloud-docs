---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-statuses/
title: Migration job status codes \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:23.190806+00:00
---

# Migration job status codes  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-statuses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Reference ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/apis)



Send feedback 

#  Migration job status codes Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-statuses "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-statuses "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  
  


The following table lists, describes, and provides user actions for migration job statuses for Database Migration Service.

Migration job status | Description | Possible substatus | Possible user actions  
---|---|---|---  
**Not started** | The migration job is ready but still not running. This status is relevant if the migration job was created but wasn't started. | None. | Start. Delete.  
**Starting...** | The migration job is in the process of being started. This is an intermediate status that occurs when a migration job is started. Starting the migration job takes between a few seconds and a few minutes. The status changes to `Running`. | None. | Delete.  
**Running** | The migration job is actively running. | CDC, Promote in progress. | Stop. Promote. Delete.  
**Running with errors** | This status means that Database Migration Service encountered errors with your migration. Faulty operations will be retried, and errors clear automatically once the underlying issue is resolved. Database Migration Service continues migrating data unaffected by the error. | CDC. | Stop. Restart. Promote (when the job is in the CDC phase).  
**Completed** | The migration job is completed. In the continuous migration type, this occurs after a successful promotion.  | None. | Delete.  
**Failed** | The migration job failed because of an error. Based on the type of error, the migration job may resume automatically, after the issue is fixed. Otherwise, the failure is unrecoverable, and the migration job needs to be restarted. When you migrate specific databases, Database Migration Service displays the **Failed** status separately for each database. You can view errors that are specific to that database. If you need to progress the migration but can't resolve the issues, you can remove the failed database from the migration. | The last status before the migration job failed. Failed in CDC, Failed in full dump. | Restart. Delete. Promote.  
**Restarting** | The migration job is in the process of being restarted. | None. | Delete.  
**Stopped** | The migration job is stopped. | The last status before the migration job has stopped: Stopped in CDC.  | If in the CDC phase, then the migration job can be resumed, promoted, or deleted.   
**Resuming** | The migration job is in the process of being resumed. | None. | Delete.  
**Stopping...** | The migration job is in the process of stopping after `Stop` was invoked. This is an intermediate status that occurs when a user stops a migration job. Stopping the job takes around a minute, during which the status is `Stopping`. Subsequently, the status changes to `Stopped`. | None. | Delete.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


