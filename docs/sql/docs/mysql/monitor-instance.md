---
url: https://docs.cloud.google.com/sql/docs/mysql/monitor-instance/
title: Monitor Cloud SQL instances \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:51.565924+00:00
---

# Monitor Cloud SQL instances  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/monitor-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Monitor Cloud SQL instances Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/monitor-instance "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-instance "View this page for the SQL Server database engine")

This page describes how you can monitor Cloud SQL instances in the following ways:

  * [Use the Cloud SQL System Insights dashboard](https://docs.cloud.google.com/sql/docs/mysql/use-system-insights)


  * Monitor an instance by using the Cloud Monitoring dashboard
  * View metrics on the Cloud SQL instance Overview page
  * Compare metrics from multiple instances



## Use the Cloud SQL System Insights dashboard

The Cloud SQL System Insights dashboard helps you detect and analyze system performance problems.

For more information, see [Use System Insights to improve system performance](https://docs.cloud.google.com/sql/docs/mysql/use-system-insights). 

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


The list includes the following options: 
  * CPU utilization
  * Active connections
  * Storage usage
  * Memory usage
  * Read/write operations
  * Ingress/Egress bytes
  * MySQL queries
  * MySQL questions
  * Read/write InnoDB pages
  * InnoDB data fsyncs
  * InnoDB log fsyncs
  * Replication lag (for read replicas)



### Available metrics

The usage charts help you respond proactively as your application needs change. From these metrics, you can gain insights into issues of throughput and latency as well as instance usage costs.

Metric| Description  
---|---  
Storage usage (GB) | You can use the storage usage metric to help you understand your storage costs. For more information about storage usage charges, see [Storage and Networking Pricing](https://cloud.google.com/sql/pricing#2nd-gen-storage-networking-prices).  Binary logs use storage space. Binary logs are automatically deleted with their associated automatic backup, which generally happens after about 7 days. You cannot manually delete binary logs, nor change the 7-day period. If the size of your binary logs are causing an issue for your instance, you can increase your storage size, but the binary log size increase in disk usage might be temporary. To avoid unexpected storage issues, we recommend enabling [ automatic storage increases](https://docs.cloud.google.com/sql/docs/mysql/instance-settings#automatic-storage-increase-2ndgen) for all instances. You can deactivate and then re-enable binary logging, which deletes binary logs. Note, however, that decreasing the write-ahead logs used doesn't shrink the size of the disk provisioned for the instance. Temp data is included in the storage usage metric. Temp data is removed as part of maintenance and is allowed to increase beyond user-defined capacity limits to avoid a disk full event, at no charge to the user. Data usage is also included in the storage usage metric. As part of data usage, when a transaction modifies a database, before Cloud SQL modifies the original data, a copy is made of this data. The copy of the data is _undo data_. For more information, see [Undo Logs](https://dev.mysql.com/doc/refman/8.4/en/innodb-undo-logs.html) in the MySQL Reference Manual. A newly created database uses several hundred MB for system tables and files. |   
CPU usage | You can use this metric to monitor whether your instance has sufficient CPU for your application needs. If this value is running too high, you can increase the size of your machine type to give your instance more CPU capability.  
Memory usage | The amount of memory being used by your instance.  
Read/write operations | The Number of Reads metric is the number of read operations served from disk that do not come from cache. You can use this metric to help you understand whether your instance is correctly sized for your environment. If needed, you can move to a larger machine type to serve more requests from cache and reduce latency. The Number of Writes metric is the number of write operations to disk. Write activity is generated even if your application is not active, because Cloud SQL instances write to a system table approximately every second (except for replicas).   
Active connections | Number of open connections to the Cloud SQL instance.   
Ingress/Egress bytes (bytes/sec) | The amount of network traffic coming into or leaving the instance.  
MySQL queries (queries/sec) | The number of statements executed by the server. To see what statements are measured as queries, see [ Server Status Variables](https://dev.mysql.com/doc/refman/8.4/en/server-status-variables.html#statvar_Queries) in the MySQL Reference Manual.   
MySQL questions (questions/sec) | The number of statements executed by the server sent by clients. To see what statements are measured as questions, see [ Server Status Variables](https://dev.mysql.com/doc/refman/8.4/en/server-status-variables.html#statvar_Questions) in the MySQL Reference Manual.   
Read/write InnoDB pages (pages/sec) | The number of InnoDB pages read and written. For more information, see [InnoDB Startup Options and System Variables](https://dev.mysql.com/doc/refman/8.4/en/innodb-parameters.html) in the MySQL Reference Manual.   
InnoDB data fsyncs (operations/sec) | The number of InnoDB fsync() calls. For more information, see [InnoDB Startup Options and System Variables](https://dev.mysql.com/doc/refman/8.4/en/innodb-parameters.html) in the MySQL Reference Manual.   
InnoDB log fsyncs (operations/sec) | The number of InnoDB fsync() calls to the log file. For more information, see [InnoDB Startup Options and System Variables](https://dev.mysql.com/doc/refman/8.4/en/innodb-parameters.html) in the MySQL Reference Manual.   
Instance state | The state of your instance is indicated by the status icon, next to the instance name. You can also monitor the [`cloudsql.googleapis.com/database/instance_state`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-cloudsql) metric.   
  
## Compare metrics from multiple instances

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. From the Cloud SQL **Instances** page, choose up to five instances to compare by selecting the checkbox to the left of the instance name. 
  3. On the **Info Panel** on the right, select the **Monitoring** tab. 
  4. From the metrics drop-down, select the metric to use for comparing instances. 

You can see the data for a specific moment by holding the pointer over the chart.




## What's next

  * [Instance settings](https://docs.cloud.google.com/sql/docs/mysql/instance-settings)
  * [Cloud SQL metrics](https://docs.cloud.google.com/sql/docs/mysql/admin-api/metrics)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
