---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/choose-index-strategy/
title: Choose a vector index in AlloyDB AI \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:46:26.479553+00:00
---

# Choose a vector index in AlloyDB AI  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/choose-index-strategy/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)



Send feedback 

#  Choose a vector index in AlloyDB AI Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/choose-index-strategy)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/ai/choose-index-strategy)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/ai/choose-index-strategy)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/ai/choose-index-strategy)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/choose-index-strategy)

This page describes AlloyDB AI vector search strategies and explains when to use each strategy. By default, AlloyDB Omni uses k-nearest neighbors search (KNN) to find vectors that are similar to a query. Vector indexes implement a search strategy called Approximate Nearest Neighbor (ANN). When you create a vector index, AlloyDB AI uses ANN, which provides better performance than KNN. Keep in mind that, when you select a vector index, you need to balance query latency and recall. 

_Recall_ measures how effectively a search retrieves all relevant items for a given query. For example, imagine you have 100 embeddings, each one representing an entity in your database. You query your embeddings with a target vector and limit it to 10 results. A KNN vector search finds the 10 exact closest vectors using a brute force calculation method, which results in 100% recall. AlloyDB AI uses this method by default if no vector search index is created or chosen. When you create a vector index in AlloyDB Omni, it typically uses ANN, which might partition vectors according to similarity to facilitate faster retrieval. As a result, using ANN, the 10 vectors returned in the earlier example might not be exactly the 10 vectors that are closest in distance. If 9 out of the 10 retrieved vectors are the closest in space to your query vector, then your recall is 90%. For more information, see [Measure vector query recall](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/measure-vector-query-recall).

_Query latency_ defines how fast the search results are generated. For example, latency is calculated based on the time spent on a search to return the vectors after you submit a query.

## Choose your search strategy

When you perform vector search in AlloyDB Omni, choose one of the following search strategies:

Search Strategy | Description | Use Cases  
---|---|---  
K-nearest neighbors (KNN) |  An algorithm that finds the k-nearest neighbors data points to a given query data point. When you perform a vector search without creating an index, a KNN search is performed by default.  To further improve the performance of KNN search, add your embedding column, and other columns related to your query, to the column store in the [columnar engine](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/columnar-engine/overview). You can [add the columns manually](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/columnar-engine/manage-content-manually) or [add the columns using auto-columnarization](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/columnar-engine/manage-content-recommendations).  | 

  * Your application is very sensitive to accuracy and you need the exact closest matches. 
  * You have tens of thousands of vectors

  
Approximate Nearest Neighbors (ANN) | An algorithm that finds approximately the closest data points. ANN divides existing customer data points into small groups based on similarities. | 

  * Your application requires low latency.
  * You have more than 100,000 vectors.

  
  
The two common ANN-based vector index types for AlloyDB Omni are ScaNN and HNSW. Use the following guidelines to decide which index type would be best for your use case:

Index Type | When to Use | Benefits | Columnar Engine Acceleration  
---|---|---|---  
ScaNN |  Usually well suited for low-dimensional data or massive datasets that exceed memory. Scales well to 10B vectors. |  Offers several benefits over HNSW on standard PostgreSQL:

  * Up to 6 times faster vector queries and up to 10 times faster filtered vector search queries
  * Up to 16 times faster index creation
  * Up to 24 times higher write throughput
  * Uses up to 4 times less memory

| Vector search with the ScaNN index can be accelerated by AlloyDB Omni columnar engine. For more information, see [Accelerate vector search with the columnar engine](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/accelerate-with-ce).  
HNSW |  Usually well suited for higher-dimensional data that fits largely within the in-memory cache. Scales well to 10-20 million vectors. | The pgvector columnar engine accelerated HNSW index in AlloyDB Omni offers up to 4 times faster vector queries than standard PostgreSQL | Vector search with the HNSW index can be accelerated by AlloyDB Omni columnar engine. For more information, see [Accelerate vector search with the columnar engine](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/accelerate-with-ce).  
  
Google recommends that you create a vector index to optimize performance on your vector search queries. For more information about how the ANN index is used for similarity searches, see [Create indexes using ScaNN](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/create-scann-index).

To accelerate your filtered KNN search, use the [columnar engine](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/columnar-engine/configure).

## What's next

  * [Create indexes and query vectors using ScaNN](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/create-scann-index)
  * [Create indexes using HNSW](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/create-hnsw-index)
  * [Tune vector query performance](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/tune-indexes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
