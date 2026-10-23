---
url: https://docs.cloud.google.com/sql/docs/mysql/recommender-reconfigure-logs/
title: Reconfigure log settings \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:50.994091+00:00
---

# Reconfigure log settings  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/recommender-reconfigure-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Reconfigure log settings Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to manage temporary binary log files and InnoDB redo log files. This [recommender](https://docs.cloud.google.com/recommender/docs/recommenders) is called **Reconfigure log settings**.

Every day, this recommender analyzes the following:

  * Disk usage in the binary log and binary log statement caches. If more than 10% of your transactions and non-transactional statements write to temporary files on disk, then **Reconfigure log settings** recommends that you should increase the value of `binlog_cache_size` or `binlog_stmt_cache_size` to improve performance.

For more information on increasing the value of `binlog_cache_size`, see [Cache memory consumption](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage#cache_memory_consumption). For more information on increasing the value of `binlog_stmt_cache_size`, see [`binlog_stmt_cache_size`](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-b).

  * The ratio of wait time versus write time for the InnoDB redo logs. This recommender advises increasing the value of `innodb_log_buffer_size` if transactions are waiting for the log buffer to flush.

For more information on increasing the value of `innodb_log_buffer_size`, see [Buffer memory consumption](/sql/docs/mysql/




## Pricing

The **Reconfigure log settings** recommender is in the _Standard_ [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

## Before you begin

[Enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enabling).

### Required roles and permissions

To get the permissions to view and work with insights and recommendations, ensure that you have the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#roles). 

Task | Role  
---|---  
View recommendations |  `recommender.cloudsqlViewer` or `cloudsql.admin`  
Apply recommendations |  `cloudsql.editor` or `cloudsql.admin`  
For more information about IAM roles, see [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles) and [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

## List the recommendations

To list the recommendations, follow these steps:

###  Console 

To list recommendations about instance performance, follow these steps:

  1. Go to the **Cloud SQL Instances** page.



[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  1. On the **Improve instance health by investigating issues and acting on recommendations** banner, click **Expand Details**.



Alternatively, follow these steps:

  1. Go to the **Active Assist**. See also [Find and apply recommendations with the Recommendations](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

  2. In the **All recommendations** card, click **Performance** .




###  gcloud 

Run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.PerformanceRecommender \
    --filter=recommenderSubtype=MYSQL_RECONFIG_TRANS_LOGS
    

Replace the following:

  * PROJECT_ID: your project ID
  * LOCATION: a region where your instances are located, such as `us-central1`



###  API 

Call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.cloudsql.instance.PerformanceRecommender/recommendations
    

Replace the following:

  * PROJECT_ID: your project ID
  * LOCATION: a region where your instances are located, such as `us-central1`



## View insights and detailed recommendations

To view insights and detailed recommendations, follow these steps:

###  Console 

Do one of the following:

  * On the **Performance Recommendations** page, click the **Performance recommendations** card and then click **Reconfigure log settings**. The recommendation panel appears, which contains insights and detailed recommendations for the instance.

  * On the **Instances** page, click **Reconfigure log settings**. The list of instances displays only those instances for which the recommendation applies.




###  gcloud 

Run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.PerformanceInsight \
    --filter=insightSubtype=INSIGHT_SUBTYPE
    
    

Replace the following:

  * PROJECT_ID: your project ID
  * LOCATION: a region where your instances are located, such as `us-central1`
  * INSIGHT_SUBTYPE: set this parameter to one of the following: 
    * `MYSQL_LOW_BINLOG_CACHE_SIZE`: display insights for the number of transactional binary logs using the on-disk cache for your instance
    * `MYSQL_LOW_BINLOG_STMT_CACHE_SIZE`: display insights for the number of non-transactional statement binary logs using the on-disk cache for your instance
    * `MYSQL_LOW_INNODB_LOG_BUFFER_SIZE`: display insights for the wait time compared to the write time for InnoDB redo logs



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceInsight/insights
    
    

Replace the following:

  * PROJECT_ID: your project ID
  * LOCATION: a region where your instances are located, such as `us-central1`



## Apply the recommendation

To implement this recommendation, do one of the following:

  * Increase the value of either `binlog_stmt_cache_size` or `binlog_cache_size`.

For more information on increasing the value of `binlog_stmt_cache_size`, see [`binlog_stmt_cache_size`](https://docs.cloud.google.com/sql/docs/mysql/flags#mysql-b). For more information on increasing the value of `binlog_cache_size`, see [Cache memory consumption](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage#cache_memory_consumption).

  * Design your transactions to be small and use less of the binary log and binary log statement caches.

  * Increase the value of `innodb_log_buffer_size`. For more information on increasing the value of `innodb_log_buffer_size`, see [Buffer memory consumption](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage#buffer_memory_consumption).

  * Increase the persistent disk size so that you have enough parallel I/O requests to improve ratio of read operations to write operations for the log files.


**Note:** Increasing `binlog_stmt_cache_size`, `binlog_cache_size`, and `innodb_log_buffer_size` requires more memory. After increasing these flags, monitor the memory usage.

## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
