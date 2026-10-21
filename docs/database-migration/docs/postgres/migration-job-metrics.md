---
url: https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-metrics/
title: Migration job metrics \u00a0|\u00a0 Database Migration Service for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:58.582928+00:00
---

# Migration job metrics  |  Database Migration Service for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgres/migration-job-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/postgres/scenario-overview)



Send feedback 

#  Migration job metrics Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service collects and displays migration job metrics that represent the health and progress of your data migration process. This page describes the following areas associated with migration job metrics:

  * Metrics available on the migration job details page covers the observability information you can view directly in Database Migration Service on the migration job details page.

  * Metrics available in Cloud Monitoring describes all metrics related to migration job performance, including the metrics surfaced from the Cloud SQL destination instance.




## Metrics available on the migration job details page

The migration job details page shows diagrams and tables that can help you understand the current state and progress of your migration job. You can view metrics for all databases included in your migration job or only the databases that you selected for migration.

![Example diagrams for migration job metrics
      Database Migration Service.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/hmm_mysql_pgsql_alloydb_standard_metrics.png) **Figure 1.** Sample observability diagrams in Database Migration Service. (click to enlarge) ![Example diagrams for migration job metrics
      Database Migration Service.](https://docs.cloud.google.com/static/database-migration/docs/images/hmm/hmm_mysql_pgsql_alloydb_standard_metrics.png)

Expand the following sections to learn more about each diagram and its associated metric.

#### Total destination storage usage

The **Total destination storage usage** diagram uses the Cloud SQL [`database/disk/bytes_used`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#cloudsql/database/disk/bytes_used) metric to show how much data (in bytes) is stored in all the databases in your destination Cloud SQL instance. You can use this information to estimate the progress of your migration job.

This metric is only available in the aggregated view. You can't filter the total disk usage per database.

#### Replication delay

The **Replication delay** diagram uses the Cloud SQL [`per_database/postgresql/external_sync/replication_byte_lag`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#cloudsql/per_database/postgresql/external_sync/replication_byte_lag) metric to show how many bytes the destination database is behind the source database.

Use this metric when you consider performing a promotion of a continuous migration. Replication delay should be zero at the time of the promotion in order to avoid data loss. Note that this metric is only relevant in the change data capture (CDC) phase. For more information on job promotion, see [Promote a migration](https://docs.cloud.google.com/database-migration/docs/postgres/promote-migration).

This metric is available for each database included in your migration job, and in the aggregated view where it shows a summary for all databases included in your migration job.

### View metrics on the migration job details page

To view metric diagrams on the migration job details page, perform the following steps:

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of your migration job. 

The migration job details page opens.

  3. In the **Databases** section, you can view the name and status of each database included in your migration job.
  4. Click the **Monitoring** tab to see the metrics diagrams. 
     * You can use the **View** menu to show aggregated data for all databases included in your migration job, or filter the information for specific databases.
     * You can also view each diagram directly in Cloud Monitoring. Click more_vert**More chart options > View in Metrics Explorer**.



## Metrics available in Cloud Monitoring

The following table describes migration job metrics you can use to [create charts in Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) for PostgreSQL migrations. For more information, see the [complete Database Migration Service metrics reference](https://docs.cloud.google.com/monitoring/api/metrics_gcp).

You can also use the [Cloud SQL `cloudsql/database/disk/bytes_used` metric](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#cloudsql/database/disk/bytes_used) and compare it with the total size of your source databases to estimate the migration job progress.

Metric type Launch stage  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`migration_job/initial_sync_complete` BETA  
Initial replication sync complete   
`GAUGE`, `BOOL`, ``   
[**datamigration.googleapis.com/MigrationJob**](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob) |  _Whether all databases on the destination DB instance have completed the initial sync and are replicating changes from the source._   
`database`: Database name.   
`migration_job/max_replica_bytes_lag` BETA  
Max lag bytes of the migration job data   
`GAUGE`, `INT64`, `By`   
[**datamigration.googleapis.com/MigrationJob**](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob) |  _Current replication lag, aggregated across all of the migration job's data. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`migration_job/max_replica_sec_lag` BETA  
Max lag in seconds of the migration job data   
`GAUGE`, `INT64`, `s`   
[**datamigration.googleapis.com/MigrationJob**](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob) |  _Current replication lag, aggregated across all of the migration job's data. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
