---
url: https://docs.cloud.google.com/alloydb/docs/recommender-increase-cluster-storage-quota/
title: Ensure database availability by increasing cluster storage quota \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:41.257756+00:00
---

# Ensure database availability by increasing cluster storage quota  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/recommender-increase-cluster-storage-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Ensure database availability by increasing cluster storage quota Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to ensure database availability and avoid instance downtime by increasing the cluster storage quota in AlloyDB, how the cluster storage quota [recommender](https://docs.cloud.google.com/recommender/docs/overview) works, and how you can use it.

The AlloyDB cluster storage quota [recommender](https://docs.cloud.google.com/recommender/docs/overview) helps you detect productions clusters which are at risk of hitting the storage quota.

The AlloyDB cluster storage quota recommender analyzes certain storage related metrics and computes the latest storage quota utilization by the cluster. If the utilization is over a certain threshold, the cluster receives a recommendation to increase the storage quota. Recommendations are generated daily.

## Before you begin

Before you can view recommendations and insights, do the following:

  * Ensure that you [enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enabling).

  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions). 

Tasks | Roles  
---|---  
View recommendations |  `recommender.alloydbViewer` or `alloydb.viewer`.   
Apply recommendations |  `recommender.alloydbAdmin` or `alloydb.admin`.   
  
See [Grant access to other users](https://docs.cloud.google.com/alloydb/docs/user-grant-access) for more information.




## List the recommendations

You can list the cluster storage quota recommendations using the Google Cloud console, `gcloud CLI`, or the Recommender API.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

For more information, see [Find recommendations with Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

  2. In the **Resources** list table, find the cluster and click **View issues** in the **Issues** column.

A list of issues is displayed in the **Aggregated issues** panel. Select the **Nearing storage quota** recommendation card.




###  gcloud CLI 

To list the cluster storage quota recommendations using gcloud CLI, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.alloydb.cluster.ReliabilityRecommender  \
    --filter=recommenderSubtype=INCREASE_CLUSTER_STORAGE_QUOTA
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your clustres are located, such as `us-central1`.



###  API 

To list cluster storage quota recommendations using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.alloydb.cluster.ReliabilityRecommender/recommendations?filter=recommenderSubtype=INCREASE_CLUSTER_STORAGE_QUOTA

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your clusters are located, such as `us-central1`.



## View insights and detailed recommendations

You can view insights and detailed recommendations about clusters that require increasing cluster storage quota using the Google Cloud console, `gcloud CLI`, or the Recommender API.

To view insights and detailed recommendations, follow these steps:

###  Console 

On the **Clusters** page, under the **Resources** table, click **View issues** in the **Issues** column for the cluster.

The **Aggregated issues** panel appears on the right, which contains insights and detailed recommendations for **Nearing storage quota**.

###  gcloud CLI 

Run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.alloydb.cluster.ReliabilityInsight \
    --filter=insightSubtype=HIGH_STORAGE_UTILIZATION
    
    

Replace the following:

  * PROJECT_ID: Your project ID.
  * LOCATION : A region where your clusters are located, for example, `us-central1`.



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.alloydb.cluster.ReliabilityInsight/insights?filter=insightSubtype=HIGH_STORAGE_UTILIZATION

Replace the following:

  * PROJECT_ID: Your project ID.
  * LOCATION : A region where your clusters are located, for example, `us-central1`.



## Apply the recommendation

Evaluate the recommendation carefully and do the following:

###  Console 

To implement the recommendation, do the following:

  1. Click **Edit Quota** for your cluster. This automatically displays the **IAM & Admin** > **Quotas & System Limits** window.
  2. Select the entry for your cluster, and click **Edit Quotas**.
  3. In the **Edit quota** window, input the appropriate quota value as per the recommendation.
  4. Fill in the required details in the **Request description** field and click **Done**.
  5. Click **Submit Request**.



## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
