---
url: https://docs.cloud.google.com/sql/docs/mysql/recommender-reconfigure-connection-settings/
title: Reconfigure connection settings \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:28.705127+00:00
---

# Reconfigure connection settings  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/recommender-reconfigure-connection-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Reconfigure connection settings Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to manage databases with a high number of simultaneous client connections and a high number of database connection threads. This [recommender](https://docs.cloud.google.com/recommender/docs/recommenders) is called **Reconfigure connection settings**.

Every day, this recommender analyzes metrics for the following:

  * The peak number of database connections by tracking the value of the `max_used_connections` flag. If the maximum number of connections since the server restarted is 80% of the value `max_connections`, **Reconfigure connection settings** recommends that you increase the value of `max_connections` .

For more information on increasing the value of `max_connections`, see [Maximum concurrent connections](https://docs.cloud.google.com/sql/docs/quotas#maximum_concurrent_connections).

  * The number of new database connection threads compared to the number of existing database connection threads. If more than 50% of connections result in new threads instead of reusing cached ones, or if the value of `thread_cache_size` is set to 0, then **Reconfigure connection settings** recommends that you increase the value of `thread_cache_size`.

For more information on increasing the value of `max_connections`, see [Optimize high CPU utilization in instances](https://docs.cloud.google.com/sql/docs/mysql/optimize-cpu-usage). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).




## Pricing

The **Reconfigure connection settings** recommender is in the _Standard_ [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

## Before you begin

[Enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enabling).

### Required roles and permissions

To get the permissions to view and work with insights and recommendations, ensure that you have the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#roles). 

Task | Role  
---|---  
View recommendations |  `recommender.cloudsqlViewer` or `cloudsql.admin`.   
Apply recommendations |  `cloudsql.editor` or `cloudsql.admin`.   
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
    --filter=recommenderSubtype=MYSQL_RECONFIG_CONNECTIONS
    

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

  * On the **Performance Recommendations** page, click the **Performance recommendations** card and then click **Reconfigure connection settings**. The recommendation panel appears, which contains insights and detailed recommendations for the instance.

  * On the **Instances** page, click **Reconfigure connection settings**. The list of instances displays only those instances for which the recommendation applies.




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
    * `MYSQL_HIGH_NUMER_OF_CONNECTIONS`: display insights for the number of database connections for your instance
    * `MYSQL_HIGH_THREAD_CACHE_MISS_RATE`: display insights for the number of new database connection threads without using the thread cache for your instance



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceInsight/insights
    
    

Replace the following:

  * PROJECT_ID: your project ID
  * LOCATION: a region where your instances are located, such as `us-central1`



## Apply the recommendation

To implement this recommendation, do one of the following:

  * To apply the recommendation for the connection thread cache size, do one of the following:

    * If the value of `thread_cache_size` is set to 0, then enable the thread cache by setting this flag to a value greater than 0.

    * If the value of `thread_cache_size` is greater than 0, then increase the value of this flag. `thread_cache_size` should be equivalent to the average number of connections to the database. Increase the value of `thread_cache_size` if the number of new threads is higher than the current setting.

  * To apply the database connection recommendation, increase the value of the `max_connections` flag. The recommendation is updated daily, so after you increase the value of this flag, wait for 24 hours before checking the recommendation again. For more information on increasing the value of `max_connections`, see [Maximum concurrent connections](https://docs.cloud.google.com/sql/docs/quotas#maximum_concurrent_connections).


**Note:** Increasing `thread_cache_size` and `max_connections` requires more memory. After increasing these flags, monitor the memory usage.

## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
