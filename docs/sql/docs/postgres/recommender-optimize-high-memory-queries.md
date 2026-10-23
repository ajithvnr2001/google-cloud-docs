---
url: https://docs.cloud.google.com/sql/docs/postgres/recommender-optimize-high-memory-queries/
title: Optimize queries with high memory usage \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:24.664053+00:00
---

# Optimize queries with high memory usage  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/recommender-optimize-high-memory-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Optimize queries with high memory usage Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes the Cloud SQL optimize high memory queries [recommender](https://docs.cloud.google.com/recommender/docs/overview) which reports queries with high memory utilization.

This recommender reports normalized query text of the queries terminated to prevent out-of-memory errors in the past 24 hours. It then provides recommendations on how to optimize such instances and improve performance. Recommendations are generated daily.

## Pricing

The Cloud SQL optimize high memory queries recommender is in the _Standard_ [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view recommendations and insights, do the following:

  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/sql/docs/postgres/project-access-control#roles). Tasks | Roles  
---|---  
View recommendations |  One of these roles: `recommender.cloudsqlViewer` or `cloudsql.viewer`.   
Apply recommendations |  One of these roles: `recommender.cloudsqlAdmin`, `cloudsql.editor`, or `cloudsql.admin`.   
For more information about IAM roles, see [IAM basic and predefined roles reference](https://docs.cloud.google.com/iam/docs/understanding-roles) and [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com)




## List recommendations for optimizing queries with high memory usage

You can list recommendations for optimizing queries with high memory usage using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

###  Console 

To list recommendations about instance performance by using the

Google Cloud console, follow these steps:

  1. Go to the **Cloud SQL Instances** page.



[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

  1. Click **Expand Details** on the **Improve instance health by investigating issues and acting on recommendations** banner.



Alternatively, follow these steps:

  1. Go to the **Active Assist**. See also [Find and apply recommendations with the Recommendations](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

  2. Click **Performance** in the **All recommendations** card.




###  gcloud CLI 

To list optimization recommendations for queries with high memory usage using gcloud CLI, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.PerformanceRecommender \
    --filter=recommenderSubtype=POSTGRES_OPTIMIZE_HIGH_MEMORY_QUERIES
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your instances are located, such as `us-central1`.



###  API 

To list optimization recommendations for queries with high memory usage using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT-ID/locations/LOCATION/recommenders/google.cloudsql.instance.PerformanceRecommender/recommendations
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your instances are located, such as `us-central1`.



If the recommender reports instances with terminated queries, it lists them in a table. Each row shows the instance name, a brief recommendation, the current machine type, the recommended machine type, the location, and the last refresh date.

## View insights and detailed recommendations

You can view insights and detailed recommendations for optimizing queries with high memory usage using the Google Cloud console, `gcloud`, or the Recommender API.

###  Console 

Do one of the following:

  * On the **Performance Recommendations** page, click **Performance recommendations** card, click **Optimize High Memory Queries**. The recommendation panel appears, which contains insights and detailed recommendations for the instance.

  * On the **Instances** page, click **Optimize High Memory Queries**. The list of instances displays only those instances for which the recommendation applies.




###  gcloud CLI 

To view insights and detailed recommendations for optimizing queries with high memory usage using `gcloud`, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.PerformanceInsight \
    --filter=insightSubtype=POSTGRES_HIGH_MEMORY_QUERIES_TERMINATED_TO_PREVENT_OOM
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



###  API 

To view insights and detailed recommendations for optimizing queries with high memory usage using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT-ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceInsight/insights
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



## Apply recommendations

Evaluate the recommendation carefully and do any of the following:

  * For more information, see [Optimize instance high memory usage](https://docs.cloud.google.com/sql/docs/postgres/optimize-high-memory-usage).
  * To dismiss the recommendation so that it's de-emphasized and appears dimmed, click **Dismiss**.
  * To close the panel without applying or dismissing the recommendation, click **Cancel**.



## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)
  * [About database observability](https://docs.cloud.google.com/sql/docs/postgres/observability)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
