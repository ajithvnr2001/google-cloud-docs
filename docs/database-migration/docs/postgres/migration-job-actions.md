---
url: https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions/
title: Manage migration jobs \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:40.363108+00:00
---

# Manage migration jobs  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/migration-src-and-dest)



Send feedback 

#  Manage migration jobs Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-actions "View this page for the MySQL version of Database Migration Service.") | PostgreSQL | [PostgreSQL to AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions "View this page for the PostgreSQL to AlloyDB version of Database Migration Service.")

  


## Overview

You can perform actions from the migration jobs list, from the single migration page, or directly from the destination instance page in Cloud SQL . You can perform an action on multiple jobs simultaneously on migration jobs that all have the same status.

You can perform some of the actions on migration jobs only, while other actions can be performed also on selected databases in a migration job. User action | Description  
---|---  
**Edit** | To make the following changes, edit the migration job:

  * Change between migrating all databases and specific databases.
  * Add or remove databases in any migration state or phase, as many times as you need. When you remove a database, Database Migration Service stops the replication process on that database but doesn't remove it from the destination. You must save the job after each change.
  * Edit the [data dump parallelism](https://docs.cloud.google.com/database-migration/docs/postgres/create-migration-job#specify-source-connection-profile-info) level of a running migration job. You must save and restart the job after you make the changes.

  
**Start** | Start migration jobs that were created without being started.  
**Stop** |  Stop a running migration job at any time. During either the full dump phase or the CDC phase, the data migration is halted, and the migration job status changes to `Stopping` and subsequently to `Stopped`.

  * If the migration job is stopped during the full dump phase, then you can delete or restart the job. However, **WAL logs will continue to accumulate in the replication slots** , eventually leading to your source database running out of disk space. In addition, Database Migration Service will keep pulling a replication delay, which means that Database Migration Service will continue to consume network traffic.
  * If the migration job is stopped during the change data capture (CDC) phase, then you can promote or delete the job.

Monitor the replication slot and disk size of your database server. You can choose to delete the migration job, which will clean all replication slots and network traffic.  
**Resume** | If a migration was stopped during the CDC phase, then it can be resumed. Resuming the migration job resumes replication of the events that were accumulated during the stopped time.  
**Restart** |  If the migration failed and isn't recoverable, or was stopped during a full dump, then it can be restarted from the beginning. If the replication has failed because of an error on one or more source or destination databases, then restarting the migration will wipe all data from any destination databases that are impacted by the errors.  If new databases were created on the source PostgreSQL server since starting the migration, then restarting the migration will also replicate the new databases into the destination instance.  
**Delete** | A migration job can be deleted. The outcome depends on the status of the job: 

  * If the migration job status was `Completed`, then the record is deleted from the migration job list.
  * If the migration job was in any other status, then there's an option to choose to delete the destination Cloud SQL instance/primary pair.

  
**Promote** | See [Promote a migration](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration).  
  
[ Previous arrow_back  Review a migration job  ](https://docs.cloud.google.com/database-migration/docs/postgres/review-migration-job)

[ Next Verify a migration  arrow_forward  ](https://docs.cloud.google.com/database-migration/docs/postgres/verify-migration)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

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
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v097103d8ccd7b257790809ea4cc5e5fee6daa6e24890a4af388296e58364bc31/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

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


