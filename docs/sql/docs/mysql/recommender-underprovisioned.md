---
url: https://docs.cloud.google.com/sql/docs/mysql/recommender-underprovisioned/
title: Reduce underprovisioned Cloud SQL instances \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:32.186346+00:00
---

# Reduce underprovisioned Cloud SQL instances  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/recommender-underprovisioned/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Reduce underprovisioned Cloud SQL instances Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/recommender-underprovisioned "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/recommender-underprovisioned "View this page for the SQL Server database engine")

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The underprovisioned instance [recommender](https://docs.cloud.google.com/recommender/docs/overview) helps you detect instances that have high CPU and/or memory utilization. It then provides recommendations for how to optimize the instance. This page describes how this recommender works and how to use it.

## How it works

When there is high CPU and/or memory utilization detected, you see a recommendation to increase the size of your instance to reduce CPU and/or memory utilization at peak.

**Note:** Recommendations are generated daily.

## Pricing

The underprovisioned instance recommender is in the Standard [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view recommendations and insights, do the following:

  * Ensure that you have the required [roles](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#roles) so that you have permission to view and work with insights and recommendations. Tasks | Roles  
---|---  
View recommendations |  One of these roles: `recommender.cloudsqlViewer` or `cloudsql.viewer`.   
Apply recommendations |  One of these roles: `recommender.cloudsqlAdmin`, `cloudsql.editor`, or `cloudsql.admin`.   
For more information about roles, see [understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles) and [granting IAM permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com)




## List underprovisioned instance recommendations

###  Console 

To list recommendations about underprovisioned instances, follow these steps:

  1. Go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. Click **View all** on the resize Cloud SQL instance recommender banner.




Alternatively, follow these steps:

  1. Go to the **Active Assist**.

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

For more information, see [Getting started with Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

  2. In the **Resize Cloud SQL instances to improve performance** card, click **View all**.

  3. Click the instances with the **Resize Cloud SQL instance** recommendation.




###  gcloud 

To list recommendations about underprovisioned instances, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.UnderprovisionedRecommender
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



###  API 

To list recommendations about underprovisioned instances by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/recommenders/google.cloudsql.instance.UnderprovisionedRecommender/recommendations
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



If the recommender detects underprovisioned instances, it lists them in a table. Each row shows the instance name, a brief recommendation, the current machine type, the recommended machine type, the location, and the last refresh date.

## View insights and detailed recommendations

###  Console 

To view insights and detailed recommendations about an underprovisioned instance by using the Google Cloud console, click the recommendation button in the list of instances.

###  gcloud 

To view insights and detailed recommendations about underprovisioned instances by using `gcloud`, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.INSIGHT_TYPE
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `INSIGHT_TYPE`: The ID of the insight type is `UnderprovisionedCpuUsageInsight`, `UnderprovisionedMemoryUsageInsight`, or `OomProbabilityInsight`, which provide insights about CPU usage, memory, and OOM probability, respectively.



###  API 

To view insights and detailed recommendations about underprovisioned instances by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/insightTypes/google.cloudsql.instance.INSIGHT_TYPE/insights
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `INSIGHT_TYPE`: The ID of the insight type as ``UnderprovisionedCpuUsageInsight`, `UnderprovisionedMemoryUsageInsight`, or `OomProbabilityInsight`, which provide insights about CPU usage, memory, and OOM probability, respectively.



The following table lists the insights and recommendations that the Cloud SQL underprovisioned instance recommender might generate to help you avoid bottlenecks from high CPU and memory usage and minimize the likelihood of out-of-memory events. The subtypes are visible in the `gcloud` and API results.

Insights | Recommendations  
---|---  
Based on the current CPU utilization trends, the instance is flagged as having high CPU usage.   
Subtype: `HIGH_CPU_UTILIZATION` | Increase CPU size or reduce CPU utilization.  
Subtype: `CHANGE_INSTANCE_SIZE`  
Based on the current memory utilization trends, the instance is flagged as having high memory usage.  
Subtype: `HIGH_MEMORY_UTILIZATION`. | Increase memory size or reduce memory utilization.  
Subtype: `CHANGE_INSTANCE_SIZE`  
Based on the current usage trends, the instance is flagged as being at the risk of incurring future OOM events.  
Subtype: `HIGH_OOM_PROBABILITY`. | Increase memory size or reduce memory utilization.  
Subtype: `CHANGE_INSTANCE_SIZE`  
  
## Apply recommendations

Evaluate the recommendations carefully and do any of the following:

  * To examine the recommendation, click **View instance**.

A banner appears at the top of the page providing a recommendation.

  * To dismiss the recommendation so that it's de-emphasized and appears dimmed, click **Dismiss**.

  * To close the panel without applying or dismissing the recommendation, click **Cancel**.




### Optimize the performance of your instance

To optimize your instance's performance, do the following:

  * [Optimize high memory usage](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage)

  * [Optimize high CPU usage](https://docs.cloud.google.com/sql/docs/mysql/optimize-cpu-usage)

  * [Create read replicas](https://docs.cloud.google.com/sql/docs/mysql/replication/create-replica).

**Caution:** This operation can lead to an increase in cost. 


  * [Edit](https://docs.cloud.google.com/sql/docs/mysql/edit-instance) the instance, if required, to increase the vCPUs or memory. Alternatively, switch to a machine type with more vCPUs and more memory. You don't need to rightsize the instance exactly as recommended. Use your judgement and resize based on how you intend to provision the instance. Keep in mind that the bigger the size, the greater the operational latency.

**Caution:** This operation can lead to an increase in cost. Additionally, it triggers a restart, which brings downtime to the instance.



You can also [export these recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq) and then examine them using [Data Studio](https://docs.cloud.google.com/bigquery/docs/visualize-looker-studio) or [Looker](https://docs.cloud.google.com/bigquery/docs/looker).

## What's next

  * [Monitor disk availability](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender)
  * [Reduce idle Cloud SQL instances](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-idle)
  * [Blog: Maximize your Cloud ROI](https://cloud.google.com/blog/products/management-tools/active-assist-comes-to-google-cloud)
  * [Blog: Do more with less](https://cloud.google.com/blog/products/databases/reduce-cloud-sql-costs-with-optimizations-by-active-assist)
  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
