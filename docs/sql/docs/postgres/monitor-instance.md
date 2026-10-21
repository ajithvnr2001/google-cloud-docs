---
url: https://docs.cloud.google.com/sql/docs/postgres/monitor-instance/
title: Monitor Cloud SQL instances \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:48.736616+00:00
---

# Monitor Cloud SQL instances  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/monitor-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Monitor Cloud SQL instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/monitor-instance "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-instance "View this page for the SQL Server database engine")

This page describes how you can monitor Cloud SQL instances in the following ways:

  * [Use the Cloud SQL System Insights dashboard](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights)


  * Monitor an instance by using the Cloud Monitoring dashboard
  * View metrics on the Cloud SQL instance Overview page
  * Compare metrics from multiple instances



## Use the Cloud SQL System Insights dashboard

The Cloud SQL System Insights dashboard helps you detect and analyze system performance problems.

For more information, see [Use System Insights to improve system performance](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights). 

## Monitor an instance by using the Cloud Monitoring dashboard

Cloud Monitoring offers predefined dashboards for several Google Cloud products, including a default Cloud SQL [monitoring dashboard](https://console.cloud.google.com/monitoring/dashboards/resourceList/cloudsql_database). You can use this dashboard to monitor the general health of your primary and replica instances. You can also create your own [custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards) to display data that's of interest to you.

### Set up alerts

You can use Cloud Monitoring to [set up alerts](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#viewing_policies) for a project or a specified instance.

For example, you can set up an alert for a message to be sent to specific email IDs when the **Memory usage** metric for a Cloud SQL instance exceeds the threshold of 80%.

## View metrics on the Cloud SQL instance Overview page

View some of the key metrics for a Cloud SQL instance on its Overview page as follows:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 

The default metrics chart appears at the top of the page. 

  3. Optional: Select another metric from the **Chart** drop-down list. 

The chart shows the data for the selected metric. 

**Note:** If you select a database-specific metric, then any instances with more than 500 databases report only a single aggregated value.




### Available metrics

The usage charts help you respond proactively as your application needs change. From these metrics, you can gain insights into issues of throughput and latency as well as instance usage costs.

Metric| Description  
---|---  
Storage usage (GB) | You can use the storage usage metric to help you understand your storage costs. For more information about storage usage charges, see [Storage and Networking Pricing](https://cloud.google.com/sql/pricing#2nd-gen-storage-networking-prices).  [Point-in-time recovery](https://docs.cloud.google.com/sql/docs/postgres/backup-recovery/pitr) uses [write-ahead logging (WAL)](https://www.postgresql.org/docs/current/wal-intro.html) archiving. For new Cloud SQL instances that have point-in-time recovery enabled or for existing instances that enable point-in-time recovery after this feature for storing WAL logs in Cloud Storage is available, logs are no longer stored on disk; instead they're stored in [Cloud Storage](https://docs.cloud.google.com/storage/docs) in the same region as the instances. To see whether an instance's logs are stored in Cloud Storage, check the [bytes_used_by_data_type](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics) metric for the instance. If the value for the `archived_wal_log` data type is `0`, the instance's logs are stored in Cloud Storage. After you use a PostgreSQL client such as `[psql](https://www.postgresql.org/docs/current/app-psql.html)` or `[pgAdmin](https://www.pgadmin.org/)` to connect to a database of the instance, run the following command: `show archive_command`. If any WALs are archived in Cloud Storage, then you see `-async_archive -remote_storage`. All other existing instances that have point-in-time recovery enabled continue to have their logs stored on disk. The change to storing logs in Cloud Storage is available at a later time. The write-ahead logs used in point-in-time recovery are deleted automatically with their associated automatic backup, which generally happens after the value set for [transactionLogRetentionDays](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/instances) is met. This is the number of days of transaction logs that Cloud SQL retains for point-in-time recovery, from 1 to 35 for Cloud SQL Enterprise Plus edition and 1 to 7 for Cloud SQL Enterprise edition. When you restore a backup on a Cloud SQL instance before enabling point-in-time recovery, you lose the WAL logs that allow the operability of point-in-time recovery.  For instances that have write-ahead logs stored in Cloud Storage, the logs are stored in the same region as the primary instance. This log storage (up to seven days, the maximum length for point-in-time recovery) generates no additional cost per instance. If your instance has point-in-time recovery enabled, and if the size of your write-ahead logs on disk is causing an issue for your instance, then deactivate point-in-time recovery and re-enable it to ensure that new logs are stored in Cloud Storage in the same region as the instance. This deletes existing write-ahead logs, so you can't perform a point-in-time-restore earlier than the time that you re-enabled point-in-time recovery. However, although the existing logs are deleted, the disk size remains the same. To avoid unexpected storage issues, we recommend enabling [automatic storage increases](https://docs.cloud.google.com/sql/docs/postgres/instance-settings#automatic-storage-increase-2ndgen) for all instances when using point-in-time recovery. This recommendation applies only if your instance has point-in-time recovery enabled and your logs are stored on disk. To delete the logs and recover storage, you can deactivate point-in-time recovery. Note, however, that decreasing the write-ahead logs used doesn't shrink the size of the disk provisioned for the instance. Data usage is included in the storage usage metric. As part of data usage, when a transaction modifies a database, before Cloud SQL modifies the original data, a copy is made of this data. The copy of the data is _undo data_.  
CPU usage | You can use this metric to monitor whether your instance has sufficient CPU for your application needs. If this value is running too high, you can increase the size of your machine type to give your instance more CPU capability.  
Memory usage | The amount of memory being used by your instance.  
Read/write operations | The Number of Reads metric is the number of read operations served from disk that do not come from cache. You can use this metric to help you understand whether your instance is correctly sized for your environment. If needed, you can move to a larger machine type to serve more requests from cache and reduce latency. The Number of Writes metric is the number of write operations to disk. Write activity is generated even if your application is not active, because Cloud SQL instances write to a system table approximately every second (except for replicas).   
Ingress/Egress bytes (bytes/sec) | The amount of network traffic coming into or leaving the instance.  
  
## Compare metrics from multiple instances

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. From the Cloud SQL **Instances** page, choose up to five instances to compare by selecting the checkbox to the left of the instance name. 
  3. On the **Info Panel** on the right, select the **Monitoring** tab. 
  4. From the metrics drop-down, select the metric to use for comparing instances. 

You can see the data for a specific moment by holding the pointer over the chart.




## What's next

  * [Instance settings](https://docs.cloud.google.com/sql/docs/postgres/instance-settings)
  * [Cloud SQL metrics](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
