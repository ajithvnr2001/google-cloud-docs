---
url: https://docs.cloud.google.com/alloydb/docs/recommender-enable-automated-backups/
title: Enable backup plans \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T06:00:11.737042+00:00
---

# Enable backup plans  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/recommender-enable-automated-backups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Enable backup plans Stay organized with collections  Save and categorize content based on your preferences. 

To protect against data loss and support point-in-time or backup recovery, you can use the AlloyDB for PostgreSQL enable backup plans [recommender](https://docs.cloud.google.com/recommender/docs/whatis-activeassist) to identify instances where both [continuous backup and recovery](https://docs.cloud.google.com/alloydb/docs/backup/overview#continuous-backup) and [automated backup plans](https://docs.cloud.google.com/alloydb/docs/backup/overview#on-demand-or) are disabled.

The enable backup plans recommender analyzes instance metadata and, if neither backup method is enabled, recommends that you enable at least one of these backup methods.

**Note:** Google Cloud recommends using continuous backup and recovery because it offers more granular recovery capabilities and reduces potential data loss compared to automated backups.

Recommendations are generated daily.

## Pricing

The AlloyDB enable backup plans recommender is available free of cost to all Google Cloud customers. For more information, see [Recommender pricing](https://docs.cloud.google.com/recommender/docs/pricing).

## Before you begin

Before you can view recommendations and insights, you must do the following:

  * Ensure that you [enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enable-api).
  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions). Tasks | Roles  
---|---  
View recommendations |  One of these roles: `roles/recommender.alloydbViewer` or `roles/alloydb.viewer`.   
Apply recommendations |  One of these roles: `roles/recommender.alloydbAdmin` or `roles/alloydb.admin`.   



See [Grant access to other users](https://docs.cloud.google.com/alloydb/docs/user-grant-access) for more information.

## List reliability recommendations for enabling automated backups

You can list the enable automated backups recommendations by using the Google Cloud console, gcloud CLI, or the Recommender API.

###  Console 

To list enable automated backups recommendations using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

For more information, see [Getting started with Active Assist](https://docs.cloud.google.com/recommender/docs/quickstart-active-assist).

  2. In the **Resources** list table, find the cluster and click **View issues** in the **Issues** column.

  3. In the **Event data** panel, select the **No backup policy enabled** recommendation.




###  gcloud CLI 

To list enable automated backups recommendations using gcloud CLI, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.alloydb.cluster.ReliabilityRecommender \
    --filter=recommenderSubtype=ENABLE_CLUSTER_BACKUP_POLICY
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the region where your instances are located, such as `us-central1`.



###  API 

To list enable automated backups recommendations using the [Recommender API](https://docs.cloud.google.com/recommender/docs/use-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.alloydb.cluster.ReliabilityRecommender/recommendations?filter=recommenderSubtype=ENABLE_CLUSTER_BACKUP_POLICY
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the region where your instances are located, such as `us-central1`.



## View insights and detailed recommendations

You can view insights and detailed recommendations about instances that require enabling automated backups using the Google Cloud console, gcloud CLI, or the Recommender API.

###  Console 

To view insights and detailed recommendations about instances that require enabling automated backups, click the recommendation link in the list of instances on the **Clusters** page.

###  gcloud CLI 

To view insights and detailed recommendations about instances that require enabling automated backups, run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.alloydb.cluster.ReliabilityInsight \
    --filter=insightSubtype=CLUSTER_BACKUP_POLICY_NOT_ENABLED
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the region where your instances are located, such as `us-central1`.



###  API 

To view insights and detailed recommendations about instances that require enabling automated backups, use the [Recommender API](https://docs.cloud.google.com/recommender/docs/use-api), call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.alloydb.cluster.ReliabilityInsight/insights?filter=insightSubtype=CLUSTER_BACKUP_POLICY_NOT_ENABLED
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: the region where your instances are located, such as `us-central1`.



## Apply recommendation

To implement this recommendation, do the following:

  1. In the **Resources** list table, click **View issues** in the **Issues** column for the cluster.
  2. In the **Aggregated issues** panel, select the **No backup policy enabled** recommendation card.
  3. Click **View backup policy**.
  4. In the **Data protection** window, depending on the recommended backup policy, do one of the following:

     * To enable continuous backups and recovery, click **Edit** in the **Continuous backups & recovery** field.
     * To enable automated backups, click **Edit** in the **Automated backups** field.
  5. Set up a backup plan of your choice.

For more information, see [Automated backup configuration attributes](https://docs.cloud.google.com/alloydb/docs/backup/configure#attributes).




## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
