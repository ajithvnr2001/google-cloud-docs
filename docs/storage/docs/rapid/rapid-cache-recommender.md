---
url: https://docs.cloud.google.com/storage/docs/rapid/rapid-cache-recommender/
title: Rapid Cache recommendations and insights \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:28:36.254335+00:00
---

# Rapid Cache recommendations and insights  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/rapid/rapid-cache-recommender/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Rapid Cache recommendations and insights Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Anywhere Cache is now renamed Rapid Cache. When using Rapid Cache with certain tools, you might still see the name Anywhere Cache being referenced in the tool's interface or surface. 

The Rapid Cache recommender analyzes your data usage and storage to provide recommendations that help you identify bucket-zone pairs in which it might be beneficial to create a cache using [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache). Rapid Cache also provides insights to show evidence for the recommendations. This page provides an overview of the Rapid Cache recommender and describes how to view recommendations and view insights.

## Overview

Rapid Cache provides an SSD-backed zonal read cache for Cloud Storage buckets. To help you decide where to set up a cache and what time to live (TTL) to use, the Rapid Cache recommender provides recommendations for creating caches in bucket-zone pairs.

Reviewing and taking actions on cache recommendations can help you save on [network data transfer fees](https://docs.cloud.google.com/storage/pricing#network-buckets), improve latencies, and avoid exceeding [bandwidth quotas](https://docs.cloud.google.com/storage/quotas#bandwidth).

## How it works

The Rapid Cache recommender simulates the existence of a cache and analyzes the cacheability and cost of your data over the past seven days by using the following insights:

  * **Cache hit rate** : the percentage of bytes that would have been served from the simulated cache.

  * **Peak cache throughput** : the amount of throughput that the simulated cache would serve, which represents extra bandwidth over what would be allowed without the simulated cache.

  * **Net cache cost** : the cost of the simulated cache, which is the sum of the cache cost, Class B operations cost difference, network data transfer cost difference, and data retrieval cost difference. A negative value for net cache cost indicates that using caching would save money.

This value is calculated using the following data:

    * **Cache cost** : the cost of using the simulated cache, which includes cache ingestion fees, storage fees, data transfer out fees, and read operation fees.

    * **Class B operation difference** : the cost of performing Class B operations on objects within the cache, minus the cost of performing the same Class B operations without caching.

    * **Network data transfer difference** : the cost of transferring data out of a multi-region bucket with caching, minus the cost of performing the same data transfer out of a multi-region bucket without caching.

    * **Data retrieval cost difference** : the cost of retrieving data from the cache, minus the cost of retrieving the same data from a non-cached bucket.




The Rapid Cache recommender recommends a zone-bucket pair when the maximum cache size exceeds 100 GiB and one or more of the following three criteria are met:

  * The cache hit rate exceeds 80%

  * Net savings on multi-region data transfer out fees exceed $700 per week, based on negotiated price

  * The peak cache throughput limit exceeds 800 Gbps




These criteria are set so you only get recommendations for creating caches that are likely to provide significant benefit. Workloads that don't meet these criteria might also have significant benefits from having a cache, so you might want to set your own criteria. You can set your own criteria by [exporting the recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq) and then querying the data using the values you want.

Recommendations include the zone name, the recommended time to live (TTL) of the cache, and the data ingestion behavior of the cache.

## Pricing

Refer to [Recommender pricing](https://docs.cloud.google.com/recommender/pricing).

## Before you begin

Before you begin, complete the following steps.

### Enable the Recommender API

[Enable the Recommender API](https://docs.cloud.google.com/recommender/docs/enabling).

### Get required roles

To view recommendations and insights for Rapid Cache, ask your administrator to grant you the Storage Admin (`roles/storage.admin`) role on the bucket or project.

This role provides a set of permissions that let you view recommendations and insights for Rapid Cache. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `recommender.storageBucketAnywhereCacheRecommendations.get`
  * `recommender.storageBucketAnywhereCacheRecommendations.list`
  * `recommender.storageBucketAnywhereCacheSimulationInsights.get`
  * `recommender.storageBucketAnywhereCacheSimulationInsights.list`



For instructions on granting roles, see [Use IAM with buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) or [Managing access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## View Rapid Cache recommendations

### Console

To view recommendations for a specific bucket, complete the following steps:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

In the list of buckets that appear, available recommendations appear in the **Cache** column. If recommendations are available, a lightbulb **Recommended** button is displayed.

If the **Cache** column doesn't appear by default, see [Show columns](https://docs.cloud.google.com/storage/docs/cloud-console#show-columns) for instructions on making the **Cache** column appear.

  2. To view details about a recommendation, click lightbulb **Recommended** from the **Cache** column.

A pane appears showing details about how enabling caching could affect performance and costs for the bucket, as well as the recommended cache settings for the bucket.

To view all available recommendations for buckets within a project, filter the list of buckets by the **Cache** column. For instructions, see [Filtering](https://docs.cloud.google.com/storage/docs/cloud-console#sort-filter).

In addition to viewing recommendations in the Cloud Storage portion of the Google Cloud console, you can also find Rapid Cache recommendations in the Active Assist. For details, see [Find recommendations with the Active Assist](https://docs.cloud.google.com/recommender/docs/quickstart-recommendation-hub).




### REST API

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To list recommendations for the project where you've enabled the Recommender API, use [`cURL`](http://curl.haxx.se/) to call the [Recommender API](https://docs.cloud.google.com/recommender/docs/reference/rest) with a `recommendations.list` request.


**Note:** When listing recommendations for a project that you don't own, you might be required to set a quota project. For instructions setting a quota project, see [Set the quota project](https://docs.cloud.google.com/docs/authentication/rest#set-billing-project).
    
    
      curl \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/\
    recommenders/google.storage.bucket.AnywhereCacheRecommender/recommendations"
    

Replace the following:

  * `PROJECT_ID` with your project ID. For information on how to find your project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of your bucket. For example, `us-east4`.




You can export recommendations to BigQuery using the BigQuery Data Transfer Service. For more information, see [Export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

## View Rapid Cache insights

The Rapid Cache recommender generates recommendations based on resource insights.

### Console

To view insights for a specific bucket, complete the following steps:

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Click the name of the bucket you want to view the insights of.

  3. In the **Bucket details** page, click the **Configuration** tab.

In the **Anywhere Cache** section, a lightbulb **Recommended** button appears when there are available recommendations to view. A **Configure Cache** button appears when there are no available recommendations to view and a cache is yet to be created for the bucket.

  4. In the **Anywhere Cache** section, click lightbulb **Recommended** or **Configure Cache**.

The **Configure cache** page appears. In the **Recommendation** column, a **View insight** button is displayed when there are available insights to view.

  5. In the **Recommendation** column, click **View insight** to view available insights for a cache-zone pair.

The **Caching analysis** pane appears and displays insights for the cache-zone pair.




### Command line

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. In your development environment, list Rapid Cache insights by using the `gcloud recommender insights list` command:
         
         gcloud recommender insights list --project=PROJECT_ID \
         --location=LOCATION --insight-type=INSIGHT_TYPE
         

Replace the following:

     * `PROJECT_ID` with your project ID. For information on how to find your project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

     * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of your bucket. For example, `us-east4`.

     * `INSIGHT_TYPE` with the value `google.storage.bucket.AnywhereCacheSimulationInsight`.




### REST API

### JSON API

  1. Have gcloud CLI [installed and initialized](https://docs.cloud.google.com/sdk/docs/install), which lets you generate an access token for the `Authorization` header.

  2. To list insights for the project where you've enabled the Recommender API, use [`cURL`](http://curl.haxx.se/) to call the [Recommender API](https://docs.cloud.google.com/recommender/docs/reference/rest) with an `insights.list` request.



    
    
      curl \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://recommender.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/\
    insightTypes/google.storage.bucket.AnywhereCacheSimulationInsight/insights"
    

Replace the following:

  * `PROJECT_ID` with your project ID. For information on how to find your project ID, see [Identifying projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

  * `LOCATION` with the [location](https://docs.cloud.google.com/storage/docs/locations) of your bucket. For example, `us-east4`.




## What's next

  * [Export recommendations to BigQuery](https://docs.cloud.google.com/recommender/docs/bq-export/export-recommendations-to-bq).

  * [Create caches](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache) using Rapid Cache.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
