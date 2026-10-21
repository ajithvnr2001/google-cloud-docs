---
url: https://docs.cloud.google.com/sql/docs/sqlserver/recommender-enable-automated-backups/
title: Prevent data loss for your instance by enabling automated backups \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:37.872333+00:00
---

# Prevent data loss for your instance by enabling automated backups  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/recommender-enable-automated-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Prevent data loss for your instance by enabling automated backups Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/recommender-enable-automated-backups "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/recommender-enable-automated-backups "View this page for the PostgreSQL database engine") | SQL Server

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes the Cloud SQL enable automated backups [recommender](https://docs.cloud.google.com/recommender/docs/overview) which helps you detect instances which are critical and have a risk of data loss.

The Cloud SQL enable automated backups recommender analyzes instance metadata and recommends to configure automated backups for production instances that have no automated backups enabled.

Recommendations are generated daily.

## Pricing

The Cloud SQL enable automated backups recommender is in the _Standard_ [Recommender pricing tier](https://cloud.google.com/recommender/pricing).

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




## List reliability recommendations for enabling automated backups

You can list the enable automated backups recommendations by using the Google Cloud console, `[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud)`, or the Recommender API.

###  Console 

To list enable automated backups recommendations using the Google Cloud console, follow these steps:

  1. Go to the **Active Assist**.

[Go to the Active Assist](https://console.cloud.google.com/home/recommendations/)

For more information, see [Getting started with Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

  2. In the **Increase Cloud SQL instance reliability** card, click **View all**.

  3. Select instances with the **Enable automated backups** recommendation.




###  gcloud CLI 

To list enable automated backups recommendations using gcloud CLI, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.cloudsql.instance.ReliabilityRecommender \
    --filter=recommenderSubtype=ENABLE_AUTO_BACKUP
    
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your instances are located, such as `us-central1`.



###  API 

To list enable automated backups recommendations using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/recommenders/google.cloudsql.instance.ReliabilityRecommender/recommendations
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your instances are located, such as `us-central1`.



If the recommender detects instances for the enable automated backups recommendation, it lists them in a table. Each row shows the instance name, a brief recommendation, the current machine type, the recommended machine type, the location, and the last refresh date.

## View insights and detailed recommendations

You can view insights and detailed recommendations about instances that require enabling automated backups using the Google Cloud console, `gcloud CLI`, or the Recommender API.

###  Console 

To view insights and detailed recommendations about instances that require enabling automated backups, click the recommendation link in the list of instances.

###  gcloud CLI 

To view insights and detailed recommendations about instances that require enabling automated backups, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT-ID \
    --location=LOCATION \
    --insight-type=google.cloudsql.instance.ReliabilityInsight \
    --filter=insightSubtype=CRITICAL_INSTANCE_AUTO_BACKUP_NOT_ENABLED
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your instances are located, such as `us-central1`.



###  API 

To view insights and detailed recommendations about instances that require enabling automated backups, use the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1beta1/projects/PROJECT-ID/locations/LOCATION/insightTypes/google.cloudsql.instance.ReliabilityInsight/insights
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your instances are located, such as `us-central1`.



## Apply recommendation

To apply this recommendation, do the following:

  * Click **Enable automated backups** in the **Issues** column. An **Enable automated backups** window displays providing a recommendation.
  * Click **Edit instance** > **Data Protection** > **Automate daily backups** to proceed.

For more information, see [Automated backup and transaction log retention](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups#automated-backups).




## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)
  * [About database observability](https://docs.cloud.google.com/sql/docs/sqlserver/observability)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
