---
url: https://docs.cloud.google.com/alloydb/docs/recommender-enable-ha/
title: Improve instance reliability by enabling high availability \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:52.136907+00:00
---

# Improve instance reliability by enabling high availability  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/recommender-enable-ha/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Improve instance reliability by enabling high availability Stay organized with collections  Save and categorize content based on your preferences. 

The AlloyDB enable-high-availability [recommender](https://docs.cloud.google.com/recommender/docs/overview) proactively generates recommendations that help you bring your important instances within a service-level agreement (SLA) by providing data redundancy. This might be helpful during a zonal outage or when an instance runs out of memory.

This page describes the AlloyDB enable-high-availability recommender, how this recommender works, and how to use it.

## How it works

The AlloyDB enable-high-availability recommender analyzes the instance metadata. If the instance doesn't have high availability enabled, then AlloyDB recommends that you enable high availability for 99.99% (*) availability.

(*) See [AlloyDB Service Level Agreement (SLA)](https://cloud.google.com/alloydb/sla) for more information.

**Note:** Recommendations are generated daily.

## Pricing

The AlloyDB enable-high-availability recommender is available free of cost to all Google Cloud customers. For more information, see [Recommender pricing](https://cloud.google.com/recommender/pricing).

## Before you begin

Before you can view recommendations and insights, you must do the following:

  * Ensure that you [enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enabling).

  * To get the permissions to view and work with insights and recommendations, ensure that you have the required [Identity and Access Management (IAM) roles](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions). 

Tasks | Roles  
---|---  
View recommendations |  One of these roles: `recommender.alloydbViewer` or `alloydb.viewer`.   
Apply recommendations |  One of these roles: `recommender.alloydbAdmin` or `alloydb.admin`.   



See [Grant access to other users](https://docs.cloud.google.com/alloydb/docs/user-grant-access) for more information.

## List enable-high-availability recommendations

You can list the enable-high-availability recommendations using the Google Cloud console, `gcloud CLI`, or the Recommender API.

###  Console 

To list enable-high-availability recommendations by using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

For more information, see [Getting started with Recommendation Hub](https://docs.cloud.google.com/recommender/docs/recommendation-hub/identify-configuration-problems).

  2. In the **Resources** list table, find the cluster and click **View issues** in the **Issues** column.

A list of issues is displayed in the **Aggregated issues** panel. Select the **Not failover protected** recommendation card.




###  gcloud 

To list enable-high-availability recommendations using gcloud CLI, run the [`gcloud recommender recommendations list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/recommendations/list) command as follows:
    
    
    gcloud recommender recommendations list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --recommender=google.alloydb.cluster.ReliabilityRecommender \
    --filter=recommenderSubtype=ENABLE_INSTANCE_HIGH_AVAILABILITY
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: a [region](https://docs.cloud.google.com/docs/geography-and-regions) where your instances are located, such as `us-central1`.



###  API 

To list enable-high-availability recommendations using the [Recommendations API](https://docs.cloud.google.com/recommender/docs/using-api), call the [`recommendations.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1/projects.locations.recommenders.recommendations/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/recommenders/google.alloydb.cluster.ReliabilityRecommender/recommendations?filter=recommenderSubtype=ENABLE_INSTANCE_HIGH_AVAILABILITY
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `LOCATION`: a region where your instances are located, such as `us-central1`.



## View insights and detailed recommendations

You can view insights and detailed recommendations about instances that require enabling high availability using the Google Cloud console, `gcloud CLI`, or the Recommender API.

To view insights and detailed recommendations, follow these steps:

###  Console 

On the **Clusters** page, under the **Resources** table, click **View issues** in the **Issues** column for the cluster.

The **Aggregated issues** panel appears on the right, which contains insights and detailed recommendations for **Not failover protected**.

###  gcloud 

Run the [`gcloud recommender insights list`](https://docs.cloud.google.com/sdk/gcloud/reference/recommender/insights/list) command as follows:
    
    
    gcloud recommender insights list \
    --project=PROJECT_ID \
    --location=LOCATION \
    --insight-type=google.alloydb.cluster.ReliabilityInsight \
    
    --filter=insightSubtype=INSTANCE_HIGH_AVAILABILITY_NOT_ENABLED
    

Replace the following:

  * `PROJECT_ID`: Your project ID.
  * `LOCATION`: A region where your instances are located, such as `us-central1`.



###  API 

Call the [`insights.list`](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/projects.locations.insightTypes.insights/list) method as follows:
    
    
    GET https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/insightTypes/google.alloydb.cluster.ReliabilityInsight/insights?filter=insightSubtype=INSTANCE_HIGH_AVAILABILITY_NOT_ENABLED

Replace the following:

  * PROJECT_ID: Your project ID.
  * LOCATION: A region where your instances are located, such as `us-central1`.



## Apply the recommendation

Evaluate the recommendation carefully and do any of the following:

###  Console 

To implement the recommendation, do the following:

  1. Click **Edit** on your cluster.
  2. In the **Edit primary instance** pane, under **Zonal availability** , select **Multiple zones (Highly available)**.
  3. Click **Update instance**.



###  gcloud CLI 

To implement the recommendation, follow the instructions in [Upgrade a basic instance to an HA instance](https://docs.cloud.google.com/alloydb/docs/basic-instance#gcloud_2).

**Note:** You must carefully evaluate before you update the instance. Applying recommendations impacts your pricing.

## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
