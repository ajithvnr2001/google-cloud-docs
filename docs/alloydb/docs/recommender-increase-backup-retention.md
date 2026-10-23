---
url: https://docs.cloud.google.com/alloydb/docs/recommender-increase-backup-retention/
title: Prevent data loss for your instance by increasing backup retention \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T06:00:15.774894+00:00
---

# Prevent data loss for your instance by increasing backup retention  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/recommender-increase-backup-retention/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Prevent data loss for your instance by increasing backup retention Stay organized with collections  Save and categorize content based on your preferences. 

To reduce the risk of data loss and extend your recovery window, you can use the AlloyDB for PostgreSQL increase backup retention [recommender](https://docs.cloud.google.com/recommender/docs/whatis-activeassist), which detects instances that need longer backup retention periods.

The AlloyDB increase backup retention recommender analyzes cluster metadata and recommends that you increase backup retention for primary clusters that have automated backups or continuous backups enabled with fewer than 14 retained backups.

Recommendations are generated daily.

## Pricing

The AlloyDB increase backup retention recommender is available free of cost to all Google Cloud customers. For more information, see [Recommender pricing](https://docs.cloud.google.com/recommender/docs/pricing).

## Before you begin

Before you can view recommendations and insights, you must do the following:

  * Ensure that you [enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enable-api).

  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions). 

Tasks | Roles  
---|---  
View recommendations |  One of these roles: `roles/recommender.alloydbViewer` or `roles/alloydb.viewer`.   
Apply recommendations |  One of these roles: `roles/recommender.alloydbAdmin` or `roles/alloydb.admin`.   



See [Grant access to other users](https://docs.cloud.google.com/alloydb/docs/user-grant-access) for more information.

## List reliability recommendations for increasing backup retention

You can list the increase backup retention recommendations using the Google Cloud console, gcloud CLI, or the Recommender API.

###  Console 

To list increase backup retention recommendations using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

For more information, see [Getting started with Active Assist](https://docs.cloud.google.com/recommender/docs/quickstart-active-assist).

  2. In the **Resources** list table, find the cluster and click **View issues** in the **Issues** column.

  3. In the **Aggregated issues** panel, select the **Short backup retention** recommendation.




###  gcloud CLI 

To list increase backup retention recommendations using gcloud CLI, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.alloydb.cluster.ReliabilityRecommender \
    --filter=recommenderSubtype=INCREASE_CLUSTER_BACKUP_RETENTION
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: a region where your instances are located, such as `us-central1`.



###  API 

To list increase backup retention recommendations using the [Recommender API](https://docs.cloud.google.com/recommender/docs/use-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.alloydb.cluster.ReliabilityRecommender/recommendations?filter=recommenderSubtype=INCREASE_CLUSTER_BACKUP_RETENTION
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: a region where your instances are located, such as `us-central1`.



## View insights and detailed recommendations

You can view insights and detailed recommendations about instances that require increasing their backup retention using the Google Cloud console, gcloud CLI, or the Recommender API.

###  Console 

To view insights and detailed recommendations about instances that require increasing their backup retention, click the recommendation link in the list of instances.

###  gcloud CLI 

To view insights and detailed recommendations about instances that require increasing their backup retention, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.alloydb.cluster.ReliabilityInsight \
    --filter=insightSubtype=CLUSTER_INSUFFICIENT_BACKUP_RETENTION
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: a region where your instances are located, such as `us-central1`.



###  API 

To view insights and detailed recommendations about instances that require increasing their backup retention, use the [Recommender API](https://docs.cloud.google.com/recommender/docs/use-api), call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.alloydb.cluster.ReliabilityInsight/insights?filter=insightSubtype=CLUSTER_INSUFFICIENT_BACKUP_RETENTION
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: a region where your instances are located, such as `us-central1`.



## Apply recommendation

To increase backup retention, do the following:

  1. In the **Resources** list table, click **View issues** in the **Issues** column for the cluster.
  2. In the **Aggregated issues** panel, select the **Short backup retention** recommendation card.
  3. Click **View backup policy**.
  4. In the **Data protection** window, depending on the recommended backup policy, do one of the following:

     * To increase the number of days covered, click **Edit** in the **Continuous backups and recovery** field.
     * To increase backup frequency, follow instructions in [Enable and configure automated backups](https://docs.cloud.google.com/alloydb/docs/backup/configure#set).

For more information, see [Backup retention and deletion](https://docs.cloud.google.com/alloydb/docs/backup/overview#backup-retention).




## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
