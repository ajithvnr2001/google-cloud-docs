---
url: https://docs.cloud.google.com/sql/docs/mysql/recommender-high-number-of-open-tables/
title: Increase the table open cache size \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:45.601936+00:00
---

# Increase the table open cache size  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/recommender-high-number-of-open-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Increase the table open cache size Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Cloud SQL high-number-of-open-tables [recommender](https://docs.cloud.google.com/recommender/docs/overview) helps you detect instances whose number of concurrently opened tables is equal to the value of `table_open_cache`. It then provides recommendations on how to optimize such instances to improve performance.

This page describes how the high-number-of-open-tables recommender works and how you can use it.

## How it works

MySQL is multi-threaded, and clients can simultaneously issue a query on the same table from multiple threads. Thus, MySQL can have independently open tables for each session. The number of simultaneously opened tables is managed by `table_open_cache`. If the cache is full and additional tables are opened, MySQL closes the least recently used table. If all the tables in cache are currently being used, MySQL extends the cache temporarily and closes the tables as soon as they become unused.

If the number of open tables exceeds the`table_open_cache` value, database performance can be adversely affected during high workload. This is because more threads are created and table handlers have to open and close the tables more frequently.

The Cloud SQL high-number-of-open-tables recommender analyzes metrics for the number of opened tables on a Cloud SQL MySQL instance daily. If the number of opened tables increases by 1 every 2 seconds or faster in the preceding 24 hours, and the number of open tables exceeds the `table_open_cache` value, the recommender advises you to adjust the `table_open_cache` flag. 

**Note:** Recommendations are generated daily.

## Pricing

The Cloud SQL high-number-of-open-tables recommender is in the _Standard_ [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view recommendations and insights, do the following:

  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [roles](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#roles). Tasks | Roles  
---|---  
View recommendations |  One of these roles: `recommender.cloudsqlViewer` or `cloudsql.viewer`.   
Apply recommendations |  One of these roles: `recommender.cloudsqlAdmin`, `cloudsql.editor`, or `cloudsql.admin`.   
For more information about roles, see [understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles) and [granting IAM permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com)




## List instance performance recommendations

You can list the instance performance recommendations by using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

The improve instance performance recommendations are shown only if you have instances that are nearing performance threshold limits.

###  Console 

To list recommendations about instance performance by using the Google Cloud console, follow these steps:

  1. Go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. Click **View all** on the Increase table open cache recommendations banner.




Alternatively, follow these steps:

  1. Go to the **Active Assist**. See also [Getting started with Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

  2. In the **Improve Cloud SQL Instance Performance** card, click **View all**.

  3. Select the instances with **Increase table open cache** recommendation.




###  gcloud CLI 

To list Improve Instance Performance recommendations by using `gcloud CLI`, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.PerformanceRecommender \
    --filter=recommenderSubtype=MYSQL_HIGH_NUMBER_OF_OPEN_TABLES_BEST_PRACTICE
    

Replace the following:

  * `PROJECT_ID`: Your project ID
  * `LOCATION`: A region, such as `us-central1`



###  API 

To list Improve Instance Performance recommendations by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/recommenders/google.cloudsql.instance.PerformanceRecommender.MySqlHighNumberOfTablesBestPractice/recommendations
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



If the recommender detects instances that have a high-number-of-open-tables, it lists them in a table with other performance recommendations. Each row shows the instance ID, a brief recommendation, database engine, the location, and the last refresh date.

## View insights and detailed recommendations

You can view insights and detailed recommendations about instances that have a high-number-of-open-tables by using the Google Cloud console, `gcloud CLI`, or the Recommender API.

###  Console 

To view insights and detailed recommendations about instances that are close to the performance threshold by using the Google Cloud console, click the recommendation link in the list of instances.

###  gcloud CLI 

To view insights and detailed recommendations about instances that are close to the performance threshold by using `gcloud CLI`, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.PerformanceInsight \
    --filter=insightSubtype=MYSQL_HIGH_NUMBER_OF_OPEN_TABLES
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



###  API 

To view insights and detailed recommendations about instances that have a high-number-of-open-tables by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceRecommender.MySqlHighNumberOfOpenTables/insights
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



The following table lists the insight and recommendation that the Cloud SQL high-number-of-open-tables recommender generates to help you improve performance. The subtypes are visible in the `gcloud CLI` and API results.

Insight | Recommendation  
---|---  
Number of open tables exceeds the `table_open_cache` flag value.  
Subtype: `MYSQL_HIGH_NUMBER_OF_OPEN_TABLES` | Increase the `table_open_cache` setting to raise the maximum number of tables that can be simultaneously kept open within a single cache. Increasing this flag protects performances during periods of high usage, but it can also increase memory usage.  
Subtype: `MYSQL_HIGH_NUMBER_OF_OPEN_TABLES_BEST_PRACTICE`  
  
## Apply recommendations

Evaluate the recommendations carefully and do any of the following:

  * To examine the instance, click **View instance**. See Optimize the performance of your instance and follow the recommendations.

  * To dismiss the recommendation so that it's de-emphasized and appears dimmed, click **Dismiss**.

  * To close the panel without applying or dismissing the recommendation, click **Cancel**.




### Optimize the performance of your instance

To optimize your instance's performance, do any of the following:

  1. Increase the value of `table_open_cache` by 1000 until the recommendation disappears. The recommendation is updated daily, so after you increase the value of `table_open_cache`, wait for 24 hours before checking it again.

  2. During peak workload, check the value of `open_tables`. If the value of `open_tables` is more than `table_open_cache`, then increase the value of `table_open_cache` to the value of `open_tables`.




For information on how MySQL uses `table_open_cache`, see [How MySQL Opens and Closes Tables](https://dev.mysql.com/doc/refman/8.0/en/table-cache.html).

For information on how to update a database flag, see [Configure database flags](https://docs.cloud.google.com/sql/docs/mysql/flags#config).

**Note:** Don't set the value of `table_open_cache` to be more than `524288`, which is [the maximum allowed value for this flag](https://docs.cloud.google.com/sql/docs/mysql/flags#table-open-cache).

## What's next

  * [Manage high number of tables](https://docs.cloud.google.com/sql/docs/mysql/recommender-high-number-of-tables)
  * [Monitor disk availability](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender)
  * [Identify idle Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-idle)
  * [Reduce overprovisioned Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-overprovisioned)
  * Explore [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
