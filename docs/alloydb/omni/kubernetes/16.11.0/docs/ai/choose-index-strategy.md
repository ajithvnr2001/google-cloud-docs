---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/choose-index-strategy/
title: Choose a vector index \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.11.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:34.100493+00:00
---

# Choose a vector index  |  AlloyDB Omni using the container orchestrator: 16.11.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/choose-index-strategy/

This page documents AlloyDB Omni version **16.11.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/overview)



Send feedback 

#  Choose a vector index Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.11.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/choose-index-strategy)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/choose-index-strategy)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/choose-index-strategy)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/choose-index-strategy)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/ai/choose-index-strategy)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/choose-index-strategy)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/choose-index-strategy)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/ai/choose-index-strategy)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/ai/choose-index-strategy)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/ai/choose-index-strategy)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/choose-index-strategy)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/choose-index-strategy)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/ai/choose-index-strategy)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/choose-index-strategy)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/ai/choose-index-strategy)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/choose-index-strategy)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/choose-index-strategy)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/ai/choose-index-strategy)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/ai/choose-index-strategy)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/ai/choose-index-strategy)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/ai/choose-index-strategy)

You must select an index type for your vector search that gives you a balance between query latency and accuracy of your results. Effective indexing directly impacts query speed and the ability to retrieve truly relevant matches that are measured by recall. 

## Key terms

Before you decide an index strategy, you must know the following terms:

  * _Recall_ : It defines how effectively a search retrieves all relevant items for a given query. For example, if you have 100 images and 10 are cats, which is true match, and your search for "cat" returns 6 cat images, your recall is 6 out of 10, which is 60%. In approximate nearest neighbors (ANN) search for vector indexes, recall is measured by comparing the results obtained with the ANN index to the true match results obtained through a brute-force search.
  * _Query latency_ : It defines how fast the search results are generated. For example, latency is calculated based on the time spent on a search to return the 6 cat images after you submit a query.



## Search strategy

You must select one of the following search strategies. Consider an example table with customer data that includes details such as purchase history, preferences, and demographics to understand how both algorithms differ:

  * **K-Nearest Neighbors (KNN)** is an algorithm that finds the k-nearest data points to a given query data point. For the previous example, to run a query that recommends products to new customers based on preferences of similar customers, KNN calculates the distance between the new customer data points and the data points of each customer in the table using a distance metric. KNN would identify k customers that match the criteria based on the distance, and then recommend products that the identified customers (k) like to the new customer.

A KNN query with distance metric, such as Euclidean distance or cosine similarity, is recommended for smaller datasets. If your use case requires 100% accuracy and you can tolerate a higher query latency, then we recommend using KNN. For more information about performing a KNN search, see [Perform similarity search](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/work-with-embeddings#generate-embeddings-similarity-search).

  * **Approximate Nearest Neighbors (ANN)** algorithm-based indexes help queries run faster, but might compromise on query accuracy or recall. For the earlier example, to run a query that recommends products to new customers based on preferences of similar customers, ANN divides existing customer data points into small groups based on similarities. When a new customer data point is added, ANN first identifies a group, out of multiple groups, that the data point belongs to, and then only calculates distance using a distance metric within the group. This filtering reduces the number of calculations required to show recommendations.

Google recommends creating a vector index that implements the ANN index when you have a large dataset since it finds similarities faster and is less resource-intensive, but compromises on accuracy. For more information about how the ANN index is used for similarity searches, see [Create indexes and query vectors using ScaNN](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/store-index-query-vectors?resource=scann). To achieve KNN accuracy with a vector index, set the search parameters equal to the number of partitions. This strategy helps to achieve KNN accuracy with a balance of query latency.




Use the following flowchart as a guidance to decide which index type is optimal based on your dataset and requirements.

![Choose an index strategy](https://docs.cloud.google.com/static/alloydb/omni/kubernetes/16.11.0/docs/images/choose-index-strategy.png)

## What's next

  * [Create indexes and query vectors using ScaNN](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/store-index-query-vectors?resource=scann)
  * [Tune vector query performance](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/tune-indexes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
