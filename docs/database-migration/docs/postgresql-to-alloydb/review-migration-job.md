---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/review-migration-job/
title: Review a migration job \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:19:00.586738+00:00
---

# Review a migration job  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/review-migration-job/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-src-and-dest)



Send feedback 

#  Review a migration job Stay organized with collections  Save and categorize content based on your preferences. 

  


[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/review-migration-job "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/review-migration-job "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


To review details about the migration job, follow these steps:

  1. In the Google Cloud console, go to the **Migration jobs** page.

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. On the **Jobs** tab, click the name of your migration job.

The migration job details page opens.

  3. View the migration job metadata, such as the migration job name, ID, migration type, source connection profile, source database engine, destination, connectivity method, date and time that the migration job was created, and how long the migration job is running. 
  4. On the **Databases** tab, when the migration job is running, you can view the following information for each database that you selected for migration: 
     * **Name**. The name of your migration job.
     * **Status**. For more information, see Migration job statuses.
     * **Phase**. The migration phase indicates whether the migration job is performing a full dump or a change data capture (CDC) operation.
     * **Replication delay**. For more information, see Migration job metrics.
     * **Errors**. The errors that occurred during the migration job.
     * **View logs**. Links to the logs for the migration job.
  5. On the **Monitoring** tab, from the **View** list, select one of the following options to view the metrics: 
     * **Aggregated** shows the metrics diagrams for all databases included in your migration job.
     * **Databases** shows the metrics diagrams for databases that you selected for migration. 

For more information about metrics, see Migration job metrics.




### Migration job statuses

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
  
### Migration job metrics

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-metrics "View this page for the MySQL version of Database Migration Service.") | [PostgreSQL](https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-metrics "View this page for the PostgreSQL version of Database Migration Service.") | PostgreSQL to AlloyDB

  


  


Database Migration Service collects and displays migration job metrics that represent the health and progress of your data migration process.

The following table lists and describes the migration job metrics that you can view on the migration job details page. You can view the following metrics for all databases included in your migration job or only the databases that you selected for migration: 

Migration metric | Description  
---|---  
**Replication delay** | Use this metric when you consider performing a promotion of a continuous migration. Replication delay should be zero at the time of the promotion in order to avoid data loss. Note this metric is only relevant in the change data capture (CDC) phase. For more information on job promotion, see [Promote a migration](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/promote-migration).  
**Storage usage in total bytes** | Reflects how many GB are being used by the destination AlloyDB for PostgreSQL instance. Use this metric to get a rough indication of migration job progress.   
You can view all [Database Migration Service Cloud Monitoring metrics that relate to migration job performance](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-datamigration) in the Metrics Explorer. To view each diagram directly in Cloud Monitoring, click more_vert**More chart options > View in Metrics Explorer**. 

You can use the following metrics to monitor your migrations:

  * The [`migration_job/initial_sync_complete`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#datamigration/migration_job/initial_sync_complete) metric indicates when the full dump phase is complete for a specific database or the entire migration job. You can view this metric on a migration level or a database level by applying the `database` label. If the database label is present, the metric value is for that particular database. If the label is not populated, the metric value is for the entire migration job.
  * The [`migration_job/max_replica_bytes_lag`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#datamigration/migration_job/max_replica_bytes_lag) metric shows the size of log data that are not yet replicated to the destination. You can view this metric on a migration level or a database level by applying the `database` label. If the database label is present, the metric value is for that particular database. If the label is not populated, the metric value is for the entire migration job.
  * The [`migration_job/max_replica_sec_lag`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#datamigration/migration_job/max_replica_sec_lag) metric shows the time (in seconds) that the destination database is behind the source database. You can view this metric only at the migration level.



For more information about the Metrics Explorer, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

[ Previous arrow_back  Create a source connection profile  ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/create-source-connection-profile)

[ Next Manage migration jobs  arrow_forward  ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-actions)

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


