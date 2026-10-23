---
url: https://docs.cloud.google.com/alloydb/docs/recommender-optimize-underprovisioned-cluster/
title: Optimize underprovisioned clusters \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:59:59.767917+00:00
---

# Optimize underprovisioned clusters  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/recommender-optimize-underprovisioned-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Optimize underprovisioned clusters Stay organized with collections  Save and categorize content based on your preferences. 

To prevent performance bottlenecks caused by high CPU or memory utilization, you can use the AlloyDB for PostgreSQL underprovisioned cluster [recommender](https://docs.cloud.google.com/recommender/docs/whatis-activeassist). The recommender detects clusters with elevated resource utilization and provides recommendations to rightsize your cluster configuration.

## How the underprovisioned cluster recommender works

When there is high CPU or memory utilization detected, you see a recommendation to increase the size of the affected instance in the cluster to reduce CPU or memory utilization at peak. Recommendations are generated daily.

## Before you begin

Before you can view recommendations and insights, do the following:

  * Ensure that you [enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enable-api).

  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions). 

Tasks | Roles  
---|---  
View recommendations |  `roles/recommender.alloydbViewer` or `roles/alloydb.viewer`  
Apply recommendations |  `roles/recommender.alloydbAdmin` or `roles/alloydb.admin`  
  
See [Grant access to other users](https://docs.cloud.google.com/alloydb/docs/user-grant-access) for more information.




## List underprovisioned cluster recommendations

You can list recommendations for underprovisioned clusters using the Google Cloud console, gcloud CLI, or the Recommender API.

###  Console 

To list recommendations about underprovisioned clusters, complete the following steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

For more information, see [Find recommendations with Active Assist](https://docs.cloud.google.com/recommender/docs/quickstart-active-assist).

  2. In the **Resources** list table, find the cluster and click **View issues** in the **Issues** column.

A list of issues is displayed in the **Aggregated issues** panel. Select the **Underprovisioned primary instance** recommendation card.




###  gcloud CLI 

To list recommendations about underprovisioned clusters using gcloud CLI, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.alloydb.cluster.PerformanceRecommender \
    --filter=recommenderSubtype=INCREASE_PRIMARY_INSTANCE_SIZE
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: a region where your clusters are located, such as `us-central1`.



###  API 

To list recommendations for underprovisioned clusters using the [Recommender API](https://docs.cloud.google.com/recommender/docs/use-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.alloydb.cluster.PerformanceRecommender/recommendations?filter=recommenderSubtype=INCREASE_PRIMARY_INSTANCE_SIZE
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: a region where your clusters are located, such as `us-central1`.



## View insights and detailed recommendations

You can view insights and detailed recommendations about underprovisioned clusters that require optimization using the Google Cloud console, gcloud CLI, or the Recommender API.

###  Console 

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Under the **Resources** table, click **View issues** in the **Issues** column for the cluster.

The **Aggregated issues** panel appears on the right, which contains insights and detailed recommendations about an underprovisioned cluster.




###  gcloud CLI 

Run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.alloydb.cluster.PerformanceInsight \
    --filter=insightSubtype=INSIGHT_SUBTYPE
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: a region where your clusters are located, such as `us-central1`.
  * `INSIGHT_SUBTYPE`: set this parameter to one of the following: 
    * `HIGH_INSTANCE_CPU_UTILIZATION`: display insights about CPU usage
    * `HIGH_INSTANCE_MEMORY_UTILIZATION`: display insights about memory



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.alloydb.cluster.PerformanceInsight/insights?filter=insightSubtype=INSIGHT_SUBTYPE

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: a region where your clusters are located, for example, `us-central1`.
  * `INSIGHT_SUBTYPE`: set this parameter to one of the following: 
    * `HIGH_INSTANCE_CPU_UTILIZATION`: display insights about CPU usage
    * `HIGH_INSTANCE_MEMORY_UTILIZATION`: display insights about memory



The following table lists the insights and recommendations that the AlloyDB for PostgreSQL underprovisioned cluster recommender might generate to help you avoid bottlenecks from high CPU and memory usage and minimize the likelihood of out-of-memory events. The subtypes are visible in the `gcloud` and API results.

Insights | Recommendations  
---|---  
Based on the current CPU utilization trends, the cluster is flagged as having high CPU usage.   
Subtype: `HIGH_INSTANCE_CPU_UTILIZATION` | Increase CPU size or reduce CPU utilization.  
Subtype: `INCREASE_PRIMARY_INSTANCE_SIZE`  
Based on the current memory utilization trends, the cluster is flagged as having high memory usage.  
Subtype: `HIGH_INSTANCE_MEMORY_UTILIZATION` | Increase memory size or reduce memory utilization.  
Subtype: `INCREASE_PRIMARY_INSTANCE_SIZE`  
  
## Apply recommendations using the Google Cloud console

Evaluate the recommendations carefully and do the following in the Google Cloud console to implement the recommendation:

  1. Click **Edit** on your cluster.
  2. In the **Edit primary instance** window, switch to a machine type with more vCPUs and more memory. You don't need to rightsize the cluster exactly as recommended. Use your judgment and resize based on how you intend to provision the cluster.

  3. Click **Update instance**.

**Note:** You must carefully evaluate before you update the cluster. Applying recommendations might impact your pricing.



## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
