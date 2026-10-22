---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/migration-job-metrics/
title: Migration job metrics \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:02.141101+00:00
---

# Migration job metrics  |  Database Migration Service for heterogeneous Oracle to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/migration-job-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/scenario-overview)



Send feedback 

#  Migration job metrics Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service collects and displays migration job metrics that represent the health and progress of your data migration process. This page describes the following areas associated with migration job metrics:

  * Metrics available on the migration job details page covers the observability information you can view directly in Database Migration Service on the migration job details page.

  * Metrics available in Cloud Monitoring describes all metrics related to migration job performance, including the metrics surfaced from the PostgreSQL destination cluster.




## Metrics available on the migration job details page

The migration job details page shows several diagrams that can help you understand the current state and progress of your migration job. Some diagrams provide database-level information, while others focus on table-level data.

![Example diagrams for migration job metrics
      Database Migration Service.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_migration_job_metrics.png) **Figure 1.** Sample observability diagrams in Database Migration Service. (click to enlarge) ![Example diagrams for migration job metrics
      Database Migration Service.](https://docs.cloud.google.com/static/database-migration/docs/images/htm/htm_migration_job_metrics.png)

Expand the following sections to learn more about each diagram and its associated metric.

#### Throughput

The **Throughput** diagram uses the [ `migration_job/write_bytes_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#datamigration/migration_job/write_bytes_count) metric to represent how much data (in bytes) Database Migration Service has written to your destination database. This metric is sampled every 60 seconds. You can use it to observe the write speed of your migration. 

This metric is available in the aggregated view, as well as separately for each table included in your migration job. 

#### Full dump volume

The **Full dump volume** diagram shows the progress of the full dump phase expressed as the percentage of total full dump data migrated. This metric is available in the aggregated view, as well as separately for each table included in your migration job. 

  * The aggregated view diagram uses the `migration_job/fulldump_progress_percentage` metric. 
  * The table-level diagrams use the `migration_job/fulldump_progress_percentage_per_object` metric. 



#### Storage usage in total bytes

The **Storage usage in total bytes** diagram uses the Cloud SQL for PostgreSQL [ `database/disk/bytes_used`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#cloudsql/database/disk/bytes_used) metric to show how much data (in bytes) is stored in the migrated database in your destination Cloud SQL for PostgreSQL instance. You can use this information to estimate the progress of your migration job. 

#### Replication delay

**Note:** This metric isn't available for one-time migrations.

The **Replication delay** diagram uses the [ `migration_job/max_replica_sec_lag`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#datamigration/migration_job/max_replica_sec_lag) metric to represent the time difference between the moment when Database Migration Service starts reading Change Data Capture (CDC) information in your source, and the moment when that information is fully replicated in your destination. You can use this information to estimate when to [ promote the migration job](https://docs.cloud.google.com/database-migration/docs/oracle-to-postgresql/finalize-migration) (you want to begin the cutoff process when replication lag is the lowest). 

### View metrics on the migration job details page

To view metric diagrams on the migration job details page, perform the following steps:

  1. In the Google Cloud console, go to the **Migration jobs** page. 

[ Go to Migration jobs](https://console.cloud.google.com/dbmigration/migrations)

  2. In the **Jobs** tab, click the display name of your migration job. 

The migration job details page opens.

  3. In the **Monitoring** section, use the **View** menu to adjust which diagrams you want to display: 

     * To view metrics aggregated for the whole migration job, click **View** > **Aggregated**. 
     * To view table-level metrics, click **View** > **Tables** , and then select your tables. 



## Metrics available in Cloud Monitoring

The following table describes all migration job metrics you can use to [create charts in Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) for heterogeneous Oracle migrations. The [ complete metrics Database Migration Service metrics reference](https://docs.cloud.google.com/monitoring/api/metrics_gcp) lists several additional metrics, but they are not available for heterogeneous Oracle migrations.

You can also use the [ Cloud SQL for PostgreSQL `database/disk/bytes_used` metric](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#cloudsql/database/disk/bytes_used) and compare it with the total size of your source databases to estimate the migration job progress.

Metric type Launch stage  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`migration_job/fulldump_progress_percentage` BETA ** _(project)_**   
Fulldump progress percentage   
`GAUGE`, `DOUBLE`, `%`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Progress percentage of the initial fulldump of the migration job.. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`migration_job/fulldump_progress_percentage_per_object` BETA ** _(project)_**   
Fulldump progress percentage per object   
`GAUGE`, `DOUBLE`, `%`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Progress percentage of the initial fulldump of a single table in a migration job. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
`migration_job/write_bytes_count` BETA  
Write Bytes Count   
`DELTA`, `INT64`, `By`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Number of bytes written to the destination. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`migration_job/max_replica_bytes_lag` BETA  
Max lag bytes of the migration job data.   
`GAUGE`, `INT64`, `By`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Current replication lag, aggregated across all of the migration job's data. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`migration_job/max_replica_sec_lag` BETA  
Max lag in seconds of the migration job data   
`GAUGE`, `INT64`, `s`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** | _Current replication lag, aggregated across all of the migration job's data. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`database`: Database name.   
`migration_job/unsupported_events_count` BETA ** _(project)_**   
Unsupported Events Count   
`DELTA`, `INT64`, `By`   
**[datamigration.googleapis.com/MigrationJob](https://docs.cloud.google.com/monitoring/api/resources#tag_datamigration.googleapis.com/MigrationJob)** |  _Number of unsupported events per migration and per table. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
