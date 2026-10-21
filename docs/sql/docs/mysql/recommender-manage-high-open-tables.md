---
url: https://docs.cloud.google.com/sql/docs/mysql/recommender-manage-high-open-tables/
title: Manage open tables and open table definitions \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:07.717291+00:00
---

# Manage open tables and open table definitions  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/recommender-manage-high-open-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Manage open tables and open table definitions Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview —[Gemini in Databases](https://docs.cloud.google.com/gemini/docs/overview) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to manage instances with a high number of open tables and a high number of open table definitions. This [recommender](https://docs.cloud.google.com/recommender/docs/recommenders) is called **Manage open tables**.

Every day, this recommender analyzes metrics for the following:

  * The number of open tables or open table definitions for an instance as follows: 
    * If the number of opened tables or opened table definitions increases by 1 table every 2 seconds, or faster, during the previous 24 hours.
    * If the number of open tables or open table definitions is equal to or more than the value of `table_open_cache` and `table_definition_cache`, respectively. If either of these are true, then the recommender advises you to increase the value of `table_open_cache` or `table_definition_cache`.



For more information on increasing the value of `table_open_cache` and `table_definition_cache`, see [Table limit](https://docs.cloud.google.com/sql/docs/quotas#table_limit).

## Pricing

The **Manage open tables** recommender is in the _Standard_ [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

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

  1. On the **Improve instance health by investigating issues and acting on recommendations** banner, click **Expand Details** .



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
    --filter=recommenderSubtype=MYSQL_RECONFIG_OPEN_TABLES
    

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

  * On the **Performance Recommendations** page, click the **Performance recommendations** card and then click **Manage open tables**. The recommendation panel appears, which contains insights and detailed recommendations for the instance.

  * On the **Instances** page, click **Manage open tables**. The list of instances displays only those instances for which the recommendation applies.




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
    * `MYSQL_HIGH_NUMBER_OF_OPEN_TABLES`: display insights for the number of open tables for your instance
    * `MYSQL_HIGH_NUMBER_OF_OPEN_TABLE_DEFINITIONS`: display insights for the number of open table definitions for your instance



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceInsight/insights
    
    

Replace the following:

  * PROJECT_ID: your project ID
  * LOCATION: a region where your instances are located, such as `us-central1`



## Apply the recommendation

To implement this recommendation, do one of the following:

  * For a high number of open tables, increase the value of `table_open_cache` by 1000 until the recommendation disappears, or check the value of `open_tables` at peak usage, and increase the value of `table_open_cache` to above the value of `open_tables`.

  * For a high number of open table definitions, increase the value of `table_definition_cache` by 500 until the recommendation disappears, or check the value of `open_table_definitions` at peak usage, and increase the value of `table_definition_cache` to above the value of `open_table_definitions`.


**Note:** Increasing `table_open_cache` or`table_definition_cache` requires more memory. After increasing these flags, monitor the memory usage .

This recommendation is updated daily, so after you increase the value of either `table_open_cache` or `table_definition_cache`, wait for 24 hours before checking the recommendation again. For more information on increasing the value of `table_open_cache` and `table_definition_cache`, see [Table limit](https://docs.cloud.google.com/sql/docs/quotas#table_limit).

## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
