---
url: https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-metrics/
title: Migration job metrics \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:54:44.309186+00:00
---

# Migration job metrics  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/database-migration/docs/postgres/apis)



Send feedback 

#  Migration job metrics Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/database-migration/docs/mysql/migration-job-metrics "View this page for the MySQL version of Database Migration Service.") | PostgreSQL | [PostgreSQL to AlloyDB](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/migration-job-metrics "View this page for the PostgreSQL to AlloyDB version of Database Migration Service.")

  


  


Database Migration Service collects and displays migration job metrics that represent the health and progress of your data migration process.

The following table lists and describes the migration job metrics that you can view on the migration job details page. You can view the following metrics for all databases included in your migration job or only the databases that you selected for migration: 

Migration metric | Description  
---|---  
**Replication delay** | Represents how many bytes the destination database is behind the source database. Use this metric when you consider performing a promotion of a continuous migration. Replication delay should be zero at the time of the promotion in order to avoid data loss. Note this metric is only relevant in the change data capture (CDC) phase. For more information on job promotion, see [Promote a migration](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration).  
**Storage usage** | Reflects how many GB are being used by the destination Cloud SQL instance. Use this metric to get a rough indication of migration job progress.   
You can view all [Database Migration Service Cloud Monitoring metrics that relate to migration job performance](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-datamigration) in the Metrics Explorer. To view each diagram directly in Cloud Monitoring, click more_vert**More chart options > View in Metrics Explorer**. 

You can use the following metrics to monitor your migrations:

  * The [`migration_job/initial_sync_complete`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#datamigration/migration_job/initial_sync_complete) metric indicates when the full dump phase is complete for a specific database or the entire migration job. You can view this metric on a migration level or a database level by applying the `database` label. If the database label is present, the metric value is for that particular database. If the label is not populated, the metric value is for the entire migration job.
  * The [`migration_job/max_replica_bytes_lag`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#datamigration/migration_job/max_replica_bytes_lag) metric shows the size of log data that are not yet replicated to the destination. You can view this metric on a migration level or a database level by applying the `database` label. If the database label is present, the metric value is for that particular database. If the label is not populated, the metric value is for the entire migration job.
  * The [`migration_job/max_replica_sec_lag`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#datamigration/migration_job/max_replica_sec_lag) metric shows the time (in seconds) that the destination database is behind the source database. You can view this metric only at the migration level.



For more information about the Metrics Explorer, see [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

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


