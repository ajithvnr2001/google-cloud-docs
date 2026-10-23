---
url: https://docs.cloud.google.com/sql/docs/sqlserver/using-ood-recommender/
title: Monitor disk availability \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:14.136522+00:00
---

# Monitor disk availability  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/using-ood-recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Monitor disk availability Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/using-ood-recommender "View this page for the PostgreSQL database engine") | SQL Server

The Cloud SQL out-of-disk [recommender](https://docs.cloud.google.com/recommender/docs/overview) proactively generates recommendations that help you reduce the risk of downtime that might be caused by your instances running out of disk space. You can apply these recommendations when a Cloud SQL instance is trending toward a storage limit. This page describes how this recommender works and how to use it.

## How it works

The Cloud SQL out-of-disk recommender analyzes the storage utilization trend over the last 30 days. When an instance is trending toward a limit where it's likely to run out of space within the next 1 to 30 days, the recommender generates related recommendations to manually increase the storage capacity, set the storage capacity to automatically increase, or free up space.

## Pricing

The Cloud SQL out-of-disk recommender is included in the [Standard Google Cloud support package](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view recommendations and insights, do the following:

  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [roles](https://docs.cloud.google.com/sql/docs/sqlserver/project-access-control#roles). Tasks | Roles  
---|---  
View recommendations |  One of these roles: `recommender.cloudsqlViewer` or `cloudsql.viewer`.   
Apply recommendations |  One of these roles: `recommender.cloudsqlAdmin`, `cloudsql.editor`, or `cloudsql.admin`.   
For more information about roles, see [understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles) and [granting IAM permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com)




## List out-of-disk recommendations

You can list out-of-disk instance recommendations by using the Google Cloud console, `gcloud`, or the Recommender API.

Out-of-disk recommendations are shown only if you have instances that are nearing disk capacity.

###  Console 

To list out-of-disk recommendations by using the Google Cloud console, follow these steps:

  1. Go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  2. Click **View all** on the out-of-disk recommendations banner.




Alternatively, follow these steps:

  1. Go to the **Active Assist**. See also [Getting started with Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

  2. In the **Prevent Downtime for SQL instances** card, click **View all**.




###  gcloud 

To list out-of-disk recommendations by using `gcloud`, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.RECOMMENDER
    

Replace the following:

  * `PROJECT_ID`: Your project ID
  * `LOCATION`: A region, such as `us-central1`
  * `RECOMMENDER`: The ID of the recommender as `OutOfDiskRecommender`.



###  API 

To list out-of-disk recommendations by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/recommenders/google.cloudsql.instance.RECOMMENDER/recommendations
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `RECOMMENDER`: The ID of the recommender as `OutOfDiskRecommender`.



## View insights and detailed recommendations

You can view insights and detailed recommendations about instances that are nearly out of disk space by using the Google Cloud console, `gcloud`, or the Recommender API.

###  Console 

To view insights and detailed recommendations about instances that are nearly out of disk space by using the Google Cloud console, click the recommendation button in the list of instances.

###  gcloud 

To view insights and detailed recommendations about instances that are nearly out of disk space by using `gcloud`, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.INSIGHT_TYPE
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `INSIGHT_TYPE`: The ID of the insight type as `DiskUsageTrendInsight`.



###  API 

To view insights and detailed recommendations about instances that are nearly out of disk space by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/insightTypes/google.cloudsql.instance.INSIGHT_TYPE/insights
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.
  * `INSIGHT_TYPE`: The ID of the insight type as `DiskUsageTrendInsight`.



The following table lists the insight and recommendation that the Cloud SQL out-of-disk recommender generates. The subtypes are visible in the `gcloud` and API results.

Insight | Recommendation  
---|---  
Based on the current storage use trend, the instance is likely to run out of disk space, which can result in downtime.   
Subtype: `TRENDING_OUT_OF_DISK` | Enable auto grow, manually increase storage capacity, or free up disk space.  
Subtype: `ENABLE_AUTO_STORAGE_INCREASE`  
  
## Apply recommendations

Evaluate the recommendations carefully and do any of the following:

  * To examine the recommendation, click **View instance**.

A banner appears at the top of the page providing a recommendation.

[Edit](https://docs.cloud.google.com/sql/docs/sqlserver/edit-instance) the instance, if required, to [manually increase](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#storage-capacity-2ndgen) the storage capacity and set the storage capacity to [automatically increase](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings#storage-capacity-2ndgen). Alternatively, delete data to free up space.

  * To dismiss the recommendation so that it's de-emphasized and appears dimmed, click **Dismiss**.

  * To close the panel without applying or dismissing the recommendation, click **Cancel**.




## What's next

  * [Reduce idle Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/recommender-sql-idle)
  * [Reduce overprovisioned Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/recommender-sql-overprovisioned)
  * [Blog: Maximize your Cloud ROI](https://cloud.google.com/blog/products/management-tools/active-assist-comes-to-google-cloud)
  * [Blog: Do more with less](https://cloud.google.com/blog/products/databases/reduce-cloud-sql-costs-with-optimizations-by-active-assist)
  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
