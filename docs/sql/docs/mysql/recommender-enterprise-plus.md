---
url: https://docs.cloud.google.com/sql/docs/mysql/recommender-enterprise-plus/
title: Improve performance with Cloud SQL Enterprise Plus edition \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:23.453448+00:00
---

# Improve performance with Cloud SQL Enterprise Plus edition  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/recommender-enterprise-plus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Improve performance with Cloud SQL Enterprise Plus edition Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/recommender-enterprise-plus "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/recommender-enterprise-plus "View this page for the SQL Server database engine")

This page describes the following types of Cloud SQL Enterprise Plus edition recommenders:

  * Upgrade to Cloud SQL Enterprise Plus edition for near-zero maintenance downtime
  * Upgrade to Cloud SQL Enterprise Plus edition and enable data cache to improve read performance
  * Upgrade to Cloud SQL Enterprise Plus edition with enabling data cache
  * Enable data cache to improve read performance



The following sections describe how these recommenders work and how to use them.

## Pricing

The recommenders described on this page are all in the standard [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view recommendations and insights, do the following:

  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [roles](https://docs.cloud.google.com/sql/docs/mysql/project-access-control#roles). Tasks | Roles  
---|---  
View recommendations |  One of these roles: `recommender.cloudsqlViewer` or `cloudsql.viewer`.   
Apply recommendations |  One of these roles: `recommender.cloudsqlAdmin`, `cloudsql.editor`, or `cloudsql.admin`.   
For more information about roles, see [understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles) and [granting Identity and Access Management (IAM) permissions](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  * Enable the Recommender API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=recommender.googleapis.com)




## Upgrade to Cloud SQL Enterprise Plus edition for near-zero maintenance downtime

The Cloud SQL Enterprise Plus edition for near-zero maintenance downtime [recommender](https://docs.cloud.google.com/recommender/docs/overview) helps you detect instances that are either critical and take a long time to stop during maintenance or their maintenance has been deferred. It analyzes instance metadata and data about maintenance.

If your instance is a production instance and takes a long time to stop during maintenance or its maintenance has been deferred, it is recommended to upgrade to Cloud SQL Enterprise Plus edition so that you instances will have near-zero maintenance downtime. Recommendations are generated daily.

### List near-zero downtime recommendations

You can list upgrade to Cloud SQL Enterprise Plus edition for near-zero maintenance downtime recommendations using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

###  Console 

To list upgrade to Cloud SQL Enterprise Plus edition recommendations, follow these steps:

  1. Go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

On the **Improve instance health by investigating issues and acting on recommendations** banner, click **Expand Details**.




Alternatively, follow these steps:

  1. Go to the **Active Assist**. See also [Find and apply recommendations with the Recommendations](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

For more information, see [Getting started with the Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

  2. In the **All recommendations** card, click **Performance**.




###  gcloud 

Run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.PerformanceRecommender \
    --filter=recommenderSubtype=UPGRADE_TO_ENTERPRISE_PLUS
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.cloudsql.instance.PerformanceRecommender/recommendations
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



If the recommender detects instances that can be upgraded to Cloud SQL Enterprise Plus edition, they are listed in a table showing the instance name, a brief recommendation, the current machine type, the recommended machine type, the location, and the last refresh date.

### View insights and detailed recommendations

You can view insights and detailed recommendations about instances that can be upgraded to Cloud SQL Enterprise Plus edition using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

###  Console 

Do one of the following:

  * On the **Performance Recommendations** page, click the **Performance recommendations** card and then click **Not optimized with Enterprise Plus**. The recommendation panel appears, which contains insights and detailed recommendations for the instance.

  * On the **Instances** page, click **Not optimized with Enterprise Plus**. The list of instances displays only those instances for which the recommendation applies.




###  gcloud 

Run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.PerformanceInsight \
    --filter=insightSubtype=INSIGHT_SUBTYPE
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `LOCATION`: a region, such as `us-central1`.
  * `INSIGHT_SUBTYPE`: set this parameter to one of the following: 
    * `CRASH_RECOVERY_CAUSED_HIGH_MAINTENANCE_DOWNTIME`: display insights for the total number of crash recoveries for your instance
    * `MAINTENANCE_DEFERRED_MULTIPLE_TIMES`: display insights for the total number of maintenances deferred for your instance



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceInsight/insights
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



A panel appears showing insights about metrics or information that the Insights highlight.

### Apply recommendations

To implement this recommendation, do the following:

  * To upgrade to Cloud SQL Enterprise Plus edition, click **Not optimized with Enterprise Plus edition** in the **Issues** column. An **Upgrade to Enterprise Plus edition** window displays providing a recommendation. To proceed with an upgrade, click **Edit** > **Upgrade**. For more information on upgrading your instance, see [Upgrade an instance to Cloud SQL Cloud SQL Enterprise Plus edition by using in-place upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place). For more information on zero downtime, see [data cache](https://docs.cloud.google.com/sql/docs/mysql/data-cache).



## Upgrade to Cloud SQL Enterprise Plus edition and enable data cache to improve read performance

The upgrade to Cloud SQL Enterprise Plus edition and enable data cache to improve read performance [recommender](https://docs.cloud.google.com/recommender/docs/overview) helps you detect instances which are critical and whose buffer pool spills pages.

The upgrade to Cloud SQL Enterprise Plus edition and enable data cache to improve read performance recommender analyzes instance metadata and metrics about buffer pool. If the instance is a production instance and its buffer pool spills pages, it is recommended to upgrade to Cloud SQL Enterprise Plus edition and enable the data cache to improve read performance. Recommendations are generated daily.

### List instances that can be upgraded to Cloud SQL Enterprise Plus edition with enabling data cache to improve read performance recommendations

You can list upgrade to Cloud SQL Enterprise Plus edition with enabling data cache to improve read performance recommendations using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

###  Console 

To list upgrade to Cloud SQL Enterprise Plus edition recommendations, follow these steps:

  1. Go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

On the **Improve instance health by investigating issues and acting on recommendations** banner, click **Expand Details**.




Alternatively, follow these steps:

  1. Go to the **Active Assist**. See also [Find and apply recommendations with the Recommendations](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

For more information, see [Getting started with the Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

  2. In the **All recommendations** card, click **Performance**.




###  gcloud 

To list upgrade to Cloud SQL Enterprise Plus edition with enabling data cache to improve read performance recommendations, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.PerformanceRecommender \
    --filter=recommenderSubtype=UPGRADE_TO_ENTERPRISE_PLUS_AND_ENABLE_DATA_CACHE
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `LOCATION`: a region where your instances are located, such as `us-central1`



###  API 

To list upgrade to Cloud SQL Enterprise Plus edition with enabling data cache to improve read performance recommendations, call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.cloudsql.instance.PerformanceRecommender/recommendations
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `LOCATION`: a region where your instances are located, such as `us-central1`



If the recommender detects instances that can be upgraded to Cloud SQL Enterprise Plus edition, they are listed in a table showing the instance name, a brief recommendation, the current machine type, the recommended machine type, the location, and the last refresh date.

### View insights and detailed recommendations

You can view insights and detailed recommendations about instances that can be upgraded to Cloud SQL Enterprise Plus edition using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

###  Console 

Do one of the following:

  * On the **Performance Recommendations** page, click the **Performance recommendations** card and then click **Not optimized with Enterprise Plus edition**. 



The recommendation panel appears, which contains insights and detailed recommendations for the instance.

  * On the **Instances** page, click **Not optimized with Enterprise Plus edition**. 



The list of instances displays only those instances for which the recommendation applies.

###  gcloud 

To view insights and detailed recommendations about an instance that can be upgraded, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.PerformanceInsight \
    --filter=insightSubtype=READ_HEAVY_WORKLOAD
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `LOCATION`: a region where your instances are located, such as `us-central1`



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceInsight/insights
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `LOCATION`: a region where your instances are located, such as `us-central1`



A panel appears showing insights about metrics or information that the Insights highlight.

### Apply recommendations

To implement this recommendation, do the following:

  * To upgrade to Cloud SQL Enterprise Plus edition, click **Not optimized with Enterprise Plus edition** in the **Issues** column. An **Upgrade to Enterprise Plus edition** window displays providing a recommendation. To proceed with an upgrade, click **Edit** > **Upgrade**. For more information on upgrading your instance, see [Upgrade an instance to Cloud SQL Cloud SQL Enterprise Plus edition by using in-place upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place). For more information on zero downtime, see [data cache](https://docs.cloud.google.com/sql/docs/mysql/data-cache).



## Upgrade to Cloud SQL Enterprise Plus edition with enabling data cache

The upgrade to Cloud SQL Enterprise Plus edition with enabling data cache [recommender](https://docs.cloud.google.com/recommender/docs/overview) helps you detect instances which are critical and take a long time to stop during maintenance or their maintenance has been deferred and their buffer pool spills pages.

The Cloud SQL Enterprise Plus edition with enabling data cache recommender analyzes instance metadata and metrics.

If your instance is a production instance and takes a long time to stop during maintenance or its maintenance has been deferred and its buffer pool spills pages, it is recommended to upgrade to Cloud SQL Enterprise Plus edition and enable data cache so that your instances have near-zero maintenance downtime and improved read performance. Recommendations are generated daily.

### List Cloud SQL instances that can be upgraded to Cloud SQL Enterprise Plus edition with enabling data cache recommendations

You can list upgrades to Cloud SQL Enterprise Plus edition when enabling data cache recommendations using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

###  Console 

To list upgrade to Cloud SQL Enterprise Plus edition recommendations, follow these steps:

  1. Go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

On the **Improve instance health by investigating issues and acting on recommendations** banner, click **Expand Details**.




Alternatively, follow these steps:

  1. Go to the **Active Assist**. See also [Find and apply recommendations with the Recommendations](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

For more information, see [Getting started with the Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

  2. In the **All recommendations** card, click **Performance**.




###  gcloud 

To list upgrade to Cloud SQL Enterprise Plus edition with enabling data cache recommendations, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.PerformanceRecommender \
    --filter=recommenderSubtype=UPGRADE_TO_ENTERPRISE_PLUS_AND_ENABLE_DATA_CACHE
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



###  API 

To list upgrade to Cloud SQL Enterprise Plus edition with enabling data cache recommendations, call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.cloudsql.instance.PerformanceRecommender/recommendations
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `LOCATION`: a region where your instances are located, such as `us-central1`



If the recommender detects instances that can be upgraded to Cloud SQL Enterprise Plus edition with enabling data cache, they are listed in a table showing the instance name, a brief recommendation, the current machine type, the recommended machine type, the location, and the last refresh date.

### View insights and detailed recommendations

You can view insights and detailed recommendations about instances that can be upgraded to Cloud SQL Enterprise Plus edition using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

###  Console 

Do one of the following:

  * On the **Performance Recommendations** page, click the **Performance recommendations** card and then click **Not optimized with Enterprise Plus**. The recommendation panel appears, which contains insights and detailed recommendations for the instance.

  * On the **Instances** page, click **Not optimized with Enterprise Plus**. The list of instances displays only those instances for which the recommendation applies.




###  gcloud 

To view insights and detailed recommendations about an instance that can be upgraded, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.PerformanceInsight \
    --filter=insightSubtype=INSIGHT_SUBTYPE
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `LOCATION`: a region where your instances are located, such as `us-central1`
  * `INSIGHT_SUBTYPE`: set this parameter to one of the following: 
    * `CRASH_RECOVERY_CAUSED_HIGH_MAINTENANCE_DOWNTIME`: display insights for the total number of crash recoveries for your instance
    * `MAINTENANCE_DEFERRED_MULTIPLE_TIMES`: display insights for the total number of maintenances deferred for your instance
    * `READ_HEAVY_WORKLOAD`: display insights about CPU usage



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceInsight/insights
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



A panel appears showing insights about metrics or information that the Insights highlight.

### Apply recommendations

To implement this recommendation, do the following:

  * To upgrade to Cloud SQL Enterprise Plus edition, click **Not optimized with Enterprise Plus edition** in the **Issues** column. An **Upgrade to Enterprise Plus edition** window displays providing a recommendation. To proceed with an upgrade, click **Edit** > **Upgrade**. For more information on upgrading your instance, see [Upgrade an instance to Cloud SQL Cloud SQL Enterprise Plus edition by using in-place upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place). For more information on data cache, see [data cache](https://docs.cloud.google.com/sql/docs/mysql/data-cache). For more information on near-zero downtime, see [near-zero downtime](https://docs.cloud.google.com/sql/docs/mysql/maintenance#nearzero).



## Enable data cache to improve read performance

The enable data cache to improve read performance [recommender](https://docs.cloud.google.com/recommender/docs/overview) helps you detect instances which are critical and whose buffer pool spills pages.

The Cloud SQL Enterprise Plus edition with enabling data cache to improve read performance recommender analyzes instance metadata and metrics about the buffer pool.

If your instance is a production instance and its buffer pool spills pages, it is recommended to enable the data cache to improve read performance. Recommendations are generated daily.

## List Cloud SQL instances qualifying for Enable data cache to improve read performance recommendations

You can list enable data cache to improve read performance recommendations by using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

###  Console 

To list upgrade to Cloud SQL Enterprise Plus edition recommendations, follow these steps:

  1. Go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql/instances)

On the **Improve instance health by investigating issues and acting on recommendations** banner, click **Expand Details**.




Alternatively, follow these steps:

  1. Go to the **Active Assist**. See also [Find and apply recommendations with the Recommendations](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

For more information, see [Getting started with the Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

  2. In the **All recommendations** card, click **Performance**.




###  gcloud 

To list enable data cache to improve read performance recommendations, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.PerformanceRecommender \
    --filter=recommenderSubtype=ENABLE_DATA_CACHE
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `LOCATION`: a region where your instances are located, such as `us-central1`



###  API 

To list enable data cache to improve read performance recommendations, call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.cloudsql.instance.PerformanceRecommender/recommendations
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `LOCATION`: a region where your instances are located, such as `us-central1`



If the recommender detects instances whose data cache can be enabled, they are listed in a table showing the instance name, a brief recommendation, the current machine type, the recommended machine type, the location, and the last refresh date.

### View insights and detailed recommendations

You can view insights and detailed recommendations about instances that can be upgraded to Cloud SQL Enterprise Plus edition using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

###  Console 

Do one of the following:

  * On the **Performance Recommendations** page, click the **Performance recommendations** card and then click **Not optimized with Enterprise Plus**. The recommendation panel appears, which contains insights and detailed recommendations for the instance.

  * On the **Instances** page, click **Not optimized with Enterprise Plus**. The list of instances displays only those instances for which the recommendation applies.




###  gcloud 

To view insights and detailed recommendations about an instance that can be upgraded, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.PerformanceInsight \
    --filter=insightSubtype=READ_HEAVY_WORKLOAD
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `LOCATION`: a region where your instances are located, such as `us-central1`



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.cloudsql.instance.PerformanceInsight/insights
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region, such as `us-central1`.



A panel appears showing insights about metrics or information that the Insights highlight.

### Apply recommendations

To implement this recommendation, do the following:

  * To upgrade to Cloud SQL Enterprise Plus edition, click **Not optimized with Enterprise Plus edition** in the **Issues** column. An **Upgrade to Enterprise Plus edition** window displays providing a recommendation. To proceed with an upgrade, click **Edit** > **Upgrade** > **Customize your instance** > **Enable data cache**. For more information on upgrading your instance, see [Upgrade an instance to Cloud SQL Cloud SQL Enterprise Plus edition by using in-place upgrade](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-to-enterprise-plus-in-place).



## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)
  * [About database observability](https://docs.cloud.google.com/sql/docs/mysql/observability)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
