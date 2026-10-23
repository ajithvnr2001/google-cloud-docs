---
url: https://docs.cloud.google.com/sql/docs/sqlserver/recommender-enable-ha/
title: Improve instance reliability by enabling high availability \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:08.463362+00:00
---

# Improve instance reliability by enabling high availability  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/recommender-enable-ha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Improve instance reliability by enabling high availability Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/recommender-enable-ha "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/recommender-enable-ha "View this page for the PostgreSQL database engine") | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Cloud SQL enable-high-availability [recommender](https://docs.cloud.google.com/recommender/docs/overview) proactively generates recommendations that help you bring your important instances within SLA by providing data redundancy. This might be helpful during a zonal outage or when an instance runs out of memory.

This page describes the Cloud SQL enable-high-availability recommender, how this recommender works, and how to use it.

## How it works

The Cloud SQL enable-high-availability recommender analyzes the instance metadata. If the instance is configured similar to instances that support important workloads but doesn't have high availability enabled, then Cloud SQL recommends that you enable high availability for 99.95% availability SLA.

**Note:** Recommendations are generated daily.

## Pricing

The Cloud SQL enable-high-availability recommender is available free of cost to all Google Cloud customers. For more information, see [Recommender pricing](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view recommendations and insights, do the following:

  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/sql/docs/sqlserver/project-access-control#roles). Tasks | Roles  
---|---  
View recommendations |  One of these roles: `recommender.cloudsqlViewer` or `cloudsql.viewer`.   
Apply recommendations |  One of these roles: `recommender.cloudsqlAdmin`, `cloudsql.editor`, or `cloudsql.admin`.   
For more information about IAM roles, see [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles) and [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com)




## List enable-high-availability recommendations

###  Console 

To list enable-high-availability recommendations by using the Google Cloud console, follow these steps:

  1. Go to the **Active Assist**.

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

For more information, see [Getting started with Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

  2. In the **Improve reliability on Cloud SQL instances** card, click **View all**.




###  gcloud 

To list enable-high-availability recommendations by using gcloud CLI, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.ReliabilityRecommender \
    --filter=recommenderSubtype=ENABLE_HIGH_AVAILABILITY
    
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A [region](https://docs.cloud.google.com/docs/geography-and-regions) where your instances are located, such as `us-central1`.



###  API 

To list enable-high-availability recommendations by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/recommenders/google.cloudsql.instance.ReliabilityRecommender/recommendations
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your instances are located, such as `us-central1`.



## View insights and detailed recommendations

###  Console 

To view insights and detailed recommendations about instances that are configured similar to instances that support important workloads but don't have high availability enabled, click the recommendation link in the list of instances.

###  gcloud 

To view insights and detailed recommendations about instances that are configured similar to instances that support important workloads but don't have high availability enabled, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.ReliabilityInsight \
    --filter=insightSubtype=CRITICAL_INSTANCE_HIGH_AVAILABILITY_NOT_ENABLED
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your instances are located, such as `us-central1`.



###  API 

To view insights and detailed recommendations about instances that are configured similar to instances that support important workloads but don't have high availability enabled by using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/insightTypes/google.cloudsql.instance.ReliabilityInsight/insights
    
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your instances are located, such as `us-central1`.



The following table lists the insight and recommendation that the Cloud SQL enable-high-availability recommender generates. The subtypes are visible in the gcloud CLI and API results.

Insight | Recommendation  
---|---  
This instance isn't highly available, even though it's configured similarly to instances that support important workloads. Single zone instances are more susceptible to downtime.  
Subtype: `CRITICAL_INSTANCE_HIGH_AVAILABILITY_NOT_ENABLED` | Enable high availability for 99.95% availability SLA. Enabling high availability will make your instance multi-zonal, which replicates your data within a region to protect against zonal outages, limit downtime and improve recovery time.  
Subtype: `ENABLE_HIGH_AVAILABILITY`  
  
## Apply the recommendation

Evaluate the recommendation carefully and do any of the following:

  * To examine the instance, click **View instance** and do any of the following:

    * Configure high availability on your instance. For more information, see [Enable and disable high availability](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ha#console_1).

**Caution:** Once you start the high availability configuration on an instance, you can't stop it. This operation restarts the instance and can lead to an increase in cost and a brief downtime. It typically takes only a few minutes for the configuration and the restart operation to complete. However, if the instance has a large disk or load, then it might take up to an hour.
    * Migrate to the Cloud SQL Enterprise Plus edition. For more information, see [Introduction to Cloud SQL editions](https://docs.cloud.google.com/sql/docs/editions-intro).

  * To dismiss the recommendation, click **Dismiss**.

  * To close the panel without applying or dismissing the recommendation, click **Cancel**.




## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)
  * [Blog: Maximize your Cloud ROI](https://cloud.google.com/blog/products/management-tools/active-assist-comes-to-google-cloud)
  * [Blog: Do more with less](https://cloud.google.com/blog/products/databases/reduce-cloud-sql-costs-with-optimizations-by-active-assist)
  * View all the [Google Cloud services available in locations worldwide](https://cloud.google.com/about/locations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
