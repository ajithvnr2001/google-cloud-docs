---
url: https://docs.cloud.google.com/sql/docs/mysql/use-system-insights/
title: Use system insights to improve system performance \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:06.291164+00:00
---

# Use system insights to improve system performance  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/use-system-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Use system insights to improve system performance Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/use-system-insights "View this page for the SQL Server database engine")

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how you can use the Cloud SQL System insights dashboard. The System insights dashboard displays metrics for the resources that your instance uses and helps you detect and analyze system performance problems.

You can use Gemini in Databases assistance to help you observe and troubleshoot your Cloud SQL for MySQL resources. For more information, see [Observe and troubleshoot with Gemini assistance](https://docs.cloud.google.com/sql/docs/mysql/observe-troubleshoot-with-gemini). 

## View the System insights dashboard

To view the System insights dashboard, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Click the name of an instance.
  3. Select the **System insights** tab from the SQL navigation panel on the left. 




The System insights dashboard opens.

![Dashboard image showing metrics and events timeline.](https://docs.cloud.google.com/static/sql/images/mysql-insights.png)**Figure 1.** Dashboard image showing events timeline and summary cards.

The System insights dashboard shows the following information:

  1. Your instance details

  2. [Events timeline](https://docs.cloud.google.com/sql/docs/mysql/use-system-insights#events_timeline): shows the system events, in a chronological order. This information helps you evaluate the impact of system events on the health and performance of the instance.

  3. [Summary cards](https://docs.cloud.google.com/sql/docs/mysql/use-system-insights#summary): provide an overview of the instance health and performance by displaying the latest and aggregated values for the CPU utilization, disk utilization, and log errors metrics.

  4. [Metrics charts](https://docs.cloud.google.com/sql/docs/mysql/use-system-insights#metrics): show the information about the operating system and database metrics that help you gain insight into several issues, such as throughput, latency, and cost.




The dashboard offers the following high-level options:

  * To create a customized dashboard, click **Customize dashboard**.


  * To keep the dashboard up to date, enable the ![](https://docs.cloud.google.com/sql/images/autorefresh.png)**Auto Refresh** option. When you enable **Auto Refresh** , the dashboard data updates every minute. This feature isn't compatible with customized time periods.

  * The time selector shows `1 day` selected by default. To change the period, select one of the other predefined periods or click **Custom** and define a start and end time. Data is available for the last 30 days.

  * To create an absolute link to the dashboard, click the **Copy Link** button. You can share this link with other Cloud SQL users who have the same permissions.

  * To create an alert for a specific event, click  notifications  **Notification**.

  * To display specific alerts, click **Annotations**.




## Summary cards

The following table describes the summary cards displayed at the top of the System Insights dashboard. These cards provide a brief overview of the instance's health and performance during the chosen time period.

Summary card| Description  
---|---  
CPU utilization - P50 | The P50 CPU utilization values.  
CPU utilization - P99  | The P99 CPU utilization values.  
Disk utilization | The latest disk utilization value.  
Log errors | The number of errors that were logged.  
  
## Metrics charts

The toolbar on each chart card provides the following set of standard options:

  * To view metric values for a specific moment in the selected period, move the cursor over the chart.

  * To zoom in on a chart, click the chart and drag horizontally along the x-axis or vertically along the y-axis. To revert the zoom operation, click **Reset zoom**. Or, click one of the predefined time periods at the top of the dashboard. Zoom operations apply at the same time to all charts on a dashboard.

  * To view additional options, click _more_vert_ **More chart options**. Most charts offer these options:

    * To view a chart in full-screen mode, click **View in full screen**. To exit full-screen mode, click **Cancel**.

    * Hide or collapse the legend.

    * Download a PNG or CSV file of the chart.

    * **View in Metrics Explorer**. View the metric in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer). You can view other Cloud SQL metrics in the Metrics Explorer after selecting the **Cloud SQL Database** resource type.

  * To create a custom dashboard, click _edit_ **Customize dashboard** and give it a name. Or, expand the **Predefined** menu and select an existing custom dashboard.

  * To view a metric chart's data in detail, click _query_stats_ **Explore data**. Here, you can filter specific metrics and choose how the chart displays:

![Customizable view of Cloud SQL metric data.](https://docs.cloud.google.com/static/sql/images/explore-data.png)

To save this customized view as a metric chart, click **Save to dashboard**.




## Default metrics

The following table describes the Cloud SQL metrics that appear by default on the Cloud SQL System insights dashboard.

**Note:** Cloud SQL for MySQL instances with more than 500 databases report a single aggregated value for database metrics.Metric name and type| Description  
---|---  
Query latency  
`dbinsights.googleapis.com/  
aggregate/latencies` | The aggregated query latency distribution by P99, P95, and P50 per user and database. Only available for instances with [ query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights) enabled.   
Database load per database/user/client address  
`dbinsights.googleapis.com/  
aggregate/execution_time` | The accumulated query execution time per database, user, or client address. This is the sum of CPU time, I/O wait time, lock wait time, process context switch, and scheduling for all processes involved in query execution.  Only available for instances with [ query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights) enabled.   
CPU utilization  
`cloudsql.googleapis.com/  
database/cpu/utilization` | The current CPU utilization represented as a percentage of the reserved CPU that's currently in use.   
MySQL connections  
`cloudsql.googleapis.com/  
database/network/connections` | The number of connections held by the database instance.  
Ingress/egress bytes  
  
`cloudsql.googleapis.com/  
database/network/received_bytes_count`  
  
`cloudsql.googleapis.com/  
database/network/sent_bytes_count` | The network traffic in terms of the number of ingress bytes (bytes received) and egress bytes (bytes sent) to and from the instance, respectively.  
Memory components  `cloudsql.googleapis.com/  
database/memory/components` | The memory components available to the database as usage, cache, and free memory. The value for each memory component is calculated as the percentage of the total memory available to the database.   
MySQL queries  
`cloudsql.googleapis.com/  
database/mysql/queries` | The number of statements executed by the server. This includes statements executed within stored programs, such as stored procedures and functions.   
MySQL questions  
`cloudsql.googleapis.com/  
database/mysql/questions` | The number of statements executed by the server. This includes only the statements sent to the server by the clients and not the statements executed within stored programs.   
MySQL network traffic  
`cloudsql.googleapis.com/  
database/mysql/received_bytes_count`  
`cloudsql.googleapis.com/  
database/mysql/sent_bytes_count` | The number of bytes received from and sent to the clients.   
InnoDB pages 

  * InnoDB dirty pages   
`cloudsql.googleapis.com/  
database/mysql/innodb_buffer_pool_pages_dirty`
  * InnoDB free pages   
`cloudsql.googleapis.com/  
database/mysql/innodb_buffer_pool_pages_free`
  * InnoDB total pages   
`cloudsql.googleapis.com/  
database/mysql/innodb_buffer_pool_pages_total`

| The number of dirty, free, and total pages in the InnoDB buffer pool. A dirty page in the InnoDB buffer pool is a page that's modified in the memory but isn't written back to the disk. A free page in InnoDB buffer pool is a page that doesn't contain any data and is unused.   
InnoDB fsync calls  `cloudsql.googleapis.com/  
database/mysql/innodb_data_fsyncs` | The number of InnoDB fsync operations.   
InnoDB log fsync calls  `cloudsql.googleapis.com/  
database/mysql/innodb_os_log_fsyncs` | The number of fsync operations performed on the InnoDB redo log files.   
InnoDB pages read/written  
  
`cloudsql.googleapis.com/  
database/mysql/innodb_pages_read`  
  
`cloudsql.googleapis.com/  
database/mysql/innodb_pages_written` | The number of InnoDB pages read and written.  
  
MySQL table open cache  
  
`cloudsql.googleapis.com/  
database/mysql/open_tables`  
  
`cloudsql.googleapis.com/  
database/mysql/opened_table_count` | `open_tables` is the number of tables currently open.   
`opened_table_count` is the number of tables that the database has opened since the last sample.  
If the value of `opened_table_count` is consistently high, we recommend that you increase the value of `table_open_cache`.   
  
MySQL table definition cache  
  
`cloudsql.googleapis.com/database/  
mysql/open_table_definitions`  
  
`cloudsql.googleapis.com/database/  
mysql/opened_table_definitions_count` | `open_table_definitions` is the number of table definitions that are currently open. `opened_table_definitions_count` is the number of times the database has opened a table definition since the last sample. If the value of `opened_table_definitions_count` is consistently high, we recommend that you increase the value of `table_definition_cache`.   
InnoDB data dictionary memory usage `cloudsql.googleapis.com/  
database/mysql/innodb/dictionary_memory` |  Memory usage for the InnoDB data dictionary cache. InnoDB has its own cache for storing information about database objects such as tables, columns, indexes, and foreign keys. `table_definition_cache` sets a soft limit on the number of tables in this cache. However, tables with foreign key relationships are kept in cache until the database shuts down or restarts. This cache can consume a significant amount of memory if your instance has many tables with foreign key relationships.   
  
Disk storage by type  
`cloudsql.googleapis.com/  
database/disk/bytes_used_by_data_type` |  The breakdown of instance disk usage by data types, such as `data`, `binlog`, and `tmp_data`. This metric helps you understand your storage costs. For more information about storage usage charges, see [Storage and networking pricing](https://cloud.google.com/sql/pricing#storage-networking-prices).  
  
[Point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr) uses binary logs. Cloud SQL generates new logs regularly and these logs use storage space. Cloud SQL automatically deletes the binary logs and their associated automatic backups. This generally happens after the retention value set for [`transactionLogRetentionDays`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/instances#BackupConfiguration.FIELDS.transaction_log_retention_days) is met. `transactionLogRetentionDays` is the number of days for which Cloud SQL retains the transaction logs. Its value ranges from `1` to `7`.  
  
To avoid unexpected storage issues while using PITR, we recommend that you enable [automatic storage increases](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen).   
  
Disk read/write ops  
  
`cloudsql.googleapis.com/  
database/disk/read_ops_count`  
  
`cloudsql.googleapis.com/  
database/disk/write_ops_count` |  `read_ops_count` indicates the delta count of disk read I/O operations. You can use this metric to understand whether your instance is correctly sized for your environment. If required, you can switch to a larger machine type to serve more requests from cache and reduce latency.  
  
`write_ops_count` indicates the delta count of disk write I/O operations. Cloud SQL instances, barring replicas, write to a system table, approximately, every second.   
  
Cloud Logging  
  
`logging.googleapis.com/  
log_entry_count` |  Shows the total number of log entries for errors and warnings.   
  
For more information, see [Cloud SQL metrics](https://docs.cloud.google.com/sql/docs/mysql/admin-api/metrics).

## Events timeline

The dashboard provides the details of the following events:

Event name| Description| Operation type  
---|---|---  
`Instance restart` | Restarts the Cloud SQL instance | `RESTART`  
`Instance failover` | Initiates a manual failover of a high availability (HA) primary instance to a standby instance, which becomes the primary instance. | `FAILOVER`  
`Instance maintenance` | Indicates that the instance is currently in maintenance. Maintenance typically causes the instance to be unavailable for 1 to 3 minutes. | `MAINTENANCE`  
`Instance backup` | Performs an instance backup. | `BACKUP_VOLUME`  
`Instance update` | Updates the settings of a Cloud SQL instance. | `UPDATE`  
`Promote replica` | Promotes a Cloud SQL replica instance. | `PROMOTE_REPLICA`  
`Start replica` | Starts replication on a Cloud SQL read replica instance. | `START_REPLICA`  
`Stop replica` | Stops replication on a Cloud SQL read replica instance. | `STOP_REPLICA`  
`Recreate replica` | Recreates resources for a Cloud SQL replica instance. | `RECREATE_REPLICA`  
`Create replica` | Creates a Cloud SQL replica instance. | `CREATE_REPLICA`  
`Data import` | Imports data into a Cloud SQL instance. | `IMPORT`  
`Instance export` | Exports data from a Cloud SQL instance to a Cloud Storage bucket. | `EXPORT`  
`Restore backup` | Restores a backup of a Cloud SQL instance. This operation might cause your instance to restart. | `RESTORE_VOLUME`  
  
## What's next

  * [About instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings)
  * [Cloud SQL metrics](https://docs.cloud.google.com/sql/docs/mysql/admin-api/metrics)
  * [REST Resource: instances](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
