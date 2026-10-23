---
url: https://docs.cloud.google.com/sql/docs/mysql/recommender-create-indexes-join-settings/
title: Create indexes or reconfigure join settings \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:02.343255+00:00
---

# Create indexes or reconfigure join settings  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/recommender-create-indexes-join-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Create indexes or reconfigure join settings Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to manage the number of joins without indexes in your instance's join buffer. This [recommender](https://docs.cloud.google.com/recommender/docs/recommenders) is called **Create indexes or reconfigure join settings**.

Every day, this recommender monitors the number of joins without indexes in the join buffer. The join buffer is a per-connection memory buffer used for storing data during join operations that cannot use indexes. If the aggregated number of joins without indexes is greater than 500 per hour, then it recommends to create an index or increase the value of `join_buffer_size`.

For more information on increasing the value of `join_buffer_size`, see [Other memory consumption](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage#other_memory_consumption).

## Pricing

The **Create indexes or reconfigure join settings** recommender is in the _Standard_ [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

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

  1. Go to the **Active Assist**. See also [Find and applyrecommendations with the Recommendations](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

  2. In the **All recommendations** card, click **Performance** .




###  gcloud 

Run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.PerformanceRecommender \
    --filter=recommenderSubtype=MYSQL_CREATE_INDEX_OR_RECONFIG_JOIN_BUFFER
    

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
    --filter=insightSubtype=MYSQL_HIGH_JOINS_WITHOUT_INDEXES
    
    

Replace the following:

  * PROJECT_ID: your project ID
  * LOCATION: a region where your instances are located, such as `us-central1`



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceInsight/insights
    
    

Replace the following:

  * PROJECT_ID: your project ID
  * LOCATION: a region where your instances are located, such as `us-central1`



## Apply the recommendation

To implement this recommendation, do the following:

  * Create appropriate indexes in your instance to prevent a large number of joins without indexes.

  * If you are not able to create indexes for the joins, increase the value of `join_buffer_size` until the recommendation disappears. The join buffer can be increased by session or globally. We recommend that you increase the join buffer in the session where there are a large number of joins.

For more information on increasing the value of `join_buffer_size`, see [Other memory consumption](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage#other_memory_consumption).

**Note:** Increasing `join_buffer_size` requires more memory. After increasing this flag, monitor the memory usage.



## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
