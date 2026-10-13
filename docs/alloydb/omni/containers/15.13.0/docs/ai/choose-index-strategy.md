---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/choose-index-strategy/
title: Choose a vector index in AlloyDB AI \u00a0|\u00a0 AlloyDB Omni for containers: 15.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:37.647541+00:00
---

# Choose a vector index in AlloyDB AI  |  AlloyDB Omni for containers: 15.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/choose-index-strategy/

This page documents AlloyDB Omni version **15.13.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/overview)



Send feedback 

#  Choose a vector index in AlloyDB AI Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.13.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/choose-index-strategy)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/choose-index-strategy)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/choose-index-strategy)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/choose-index-strategy)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/choose-index-strategy)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/choose-index-strategy)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/choose-index-strategy)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/choose-index-strategy)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/choose-index-strategy)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/choose-index-strategy)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/choose-index-strategy)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/choose-index-strategy)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/choose-index-strategy)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/choose-index-strategy)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/choose-index-strategy)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/choose-index-strategy)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/choose-index-strategy)

This page describes AlloyDB AI vector search strategies and explains when to use each strategy. By default, AlloyDB uses k-nearest neighbors search (KNN) to find vectors that are similar to a query. Vector indexes implement a search strategy called Approximate Nearest Neighbor (ANN). When you create a vector index, AlloyDB AI uses ANN, which provides better performance than KNN. Keep in mind that, when you select a vector index, you need to balance query latency and recall. 

_Recall_ measures how effectively a search retrieves all relevant items for a given query. For example, imagine you have 100 embeddings, each one representing an entity in your database. You query your embeddings with a target vector and limit it to 10 results. A KNN vector search finds the 10 exact closest vectors using a brute force calculation method, which results in 100% recall. AlloyDB AI uses this method by default if no vector search index is created or chosen. When you create a vector index in AlloyDB for PostgreSQL, it typically uses ANN, which might partition vectors according to similarity to facilitate faster retrieval. As a result, using ANN, the 10 vectors returned in the earlier example might not be exactly the 10 vectors that are closest in distance. If only 8 out of the 10 retrieved vectors are the closest in space to your query vector, then your recall is 80%.

_Query latency_ defines how fast the search results are generated. For example, latency is calculated based on the time spent on a search to return the vectors after you submit a query.

## Choose your search strategy

When you perform vector search in AlloyDB, choose one the following search strategies:

Search Strategy  | Description  | Use Cases   
---|---|---  
K-nearest neighbors (KNN)  | An algorithm that finds the k-nearest neighbors data points to a given query data point. When you perform a vector search without creating an index, a KNN search is performed by default.  | 

  * Your application is very sensitive to accuracy and you need the exact closest matches. 
  * You have fewer than 100,000 vectors.

  
Approximate Nearest Neighbors (ANN)  | An algorithm that finds approximately the closest data points. ANN divides existing customer data points into small groups based on similarities.  | 

  * Your application requires low latency.
  * You have more than 100,000 vectors.

  
  
Google recommends that you create a vector index to optimize performance on your vector search queries. For more information about how the ANN index is used for similarity searches, see [Create indexes and query vectors using ScaNN](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/store-index-query-vectors?resource=scann).

## What's next

  * [Create indexes and query vectors using ScaNN](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/store-index-query-vectors?resource=scann)
  * [Tune vector query performance](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/tune-indexes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
