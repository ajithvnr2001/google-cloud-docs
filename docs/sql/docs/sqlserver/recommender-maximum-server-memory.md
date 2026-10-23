---
url: https://docs.cloud.google.com/sql/docs/sqlserver/recommender-maximum-server-memory/
title: Optimize maximum server memory usage \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:34.237670+00:00
---

# Optimize maximum server memory usage  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/recommender-maximum-server-memory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Optimize maximum server memory usage Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

Database instances running with an allocation of memory that's either too low or too high might experience performance issues. Instances can sometimes run into out-of-memory (OOM) issues.

The [`max server memory (mb)`](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/server-memory-server-configuration-options) flag limits the amount of memory that Cloud SQL can allocate for its internal pools. You can manually set a value for this flag, or omit the flag and let Cloud SQL manage memory limits for you automatically.

  * If you don't enable the flag, then Cloud SQL manages the instance's memory limits for you automatically, based on the size of the RAM for your instance.

  * If you enable the flag and manually set a value for it, and later resize the instance, then Cloud SQL disables the flag, overrides the value previously given, and automatically manages the memory limits of the instance for you until a new `max server memory (mb)` value is provided.




Insufficient values for the flag can cause performance issues, while over-allocation can lead to instability, performance degradation, and database crashes.

Users are strongly encouraged to let Cloud SQL manage the instance's memory limits.

For more information, see [SQL Server settings](https://docs.cloud.google.com/sql/docs/sqlserver/best-practices#sqlserver_settings_global).

## Pricing

The **Maximum server memory** recommender is in the _Standard_ [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

## Before you begin

[Enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enabling).

### Required roles and permissions

To get the permissions to view and work with insights and recommendations, ensure that you have the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/sql/docs/sqlserver/project-access-control#roles). 

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

  1. Go to the **Active Assist**. See also [Find and applyrecommendations with the Recommendations](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

  2. In the **All recommendations** card, click **Performance** .




###  gcloud 

Run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.PerformanceRecommender \
    --filter=RECOMMENDER_SUBTYPE=SQLSERVER_USE_AUTOMATIC_MAX_SERVER_MEMORY_MANAGEMENT
    

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

  * On the **Performance Recommendations** page, click the **Performance recommendations** card and then click **Create indexes or reconfigure join settings**. The recommendation panel appears, which contains insights and detailed recommendations for the instance.

  * On the **Instances** page, click **Create indexes or reconfigure join settings**. The list of instances displays only those instances for which the recommendation applies.




###  gcloud 

Run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.PerformanceInsight \
    --filter=INSIGHT_SUBTYPE=INSIGHT_SUBTYPE
    

Replace the following:

  * PROJECT_ID: your project ID
  * LOCATION: a region where your instances are located, such as `us-central1`
  * INSIGHT_SUBTYPE: the subtype used to verify whether allocated memory is too low or too high. Acceptable values include `SQLSERVER_MAX_SERVER_MEMORY_TOO_LOW` and `SQLSERVER_MAX_SERVER_MEMORY_TOO_HIGH`.



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceInsight/insights
    
    

Replace the following:

  * PROJECT_ID: your project ID
  * LOCATION: a region where your instances are located, such as `us-central1`



## Apply the recommendation

###  Console 

To implement this recommendation, do the following:

  * Locate the instance with the recommendation **Server memory misconfigured**. Click the recommendation to open it.

  * In the recommendation window, click **Edit instance**.

  * In the **Flags and parameters** section, locate and delete the **Max server memory (mb)** flag. Removing the flag lets Cloud SQL manage instance memory limits for you.




## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
