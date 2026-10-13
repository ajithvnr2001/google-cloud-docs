---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/scann-index-reference/
title: ScaNN Index reference \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:32.354029+00:00
---

# ScaNN Index reference  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/scann-index-reference/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  ScaNN Index reference Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/scann-index-reference)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/scann-index-reference)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/scann-index-reference)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/scann-index-reference)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/scann-index-reference)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/scann-index-reference)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/scann-index-reference)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/scann-index-reference)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/scann-index-reference)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/reference/scann-index-reference)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/scann-index-reference)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/scann-index-reference)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/scann-index-reference)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/scann-index-reference)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/scann-index-reference)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/scann-index-reference)

This page provides reference material for the ScaNN Index. 

## Tuning parameters

The following index parameters and database flags are used together to find the right balance of recall and QPS.

Option typeIndex creationQuery runtime

Tuning parameter | Description | Option type  
---|---|---  
`max_num_levels` | The maximum number of centroid levels of the K-means clustering tree.  


  * **Two-level tree index** : Set to `1` by default for a two-level tree (1 centroid level + bottom leaf level).
  * **Three-level tree index** : Set to `2` by default for a three-level tree (2 centroid levels + bottom leaf level)
  * Set the value to `2` if the number of vector rows exceeds 100 million rows.
  * Set the value to `1` if the number of vector rows are less than 10 million rows.
  * Set to either `1` or `2` if the number of vector rows lie between 10 million and 100 million rows to optimize for index build time (set to 2) or optimize for search recall (set to 1).

| Index creation   
(optional)  
`num_leaves` | The number of partitions to apply to this index. The number of partitions you apply to when creating an index affects the index performance. By increasing partitions for a set number of vectors, you create a more fine-grained index, which improves recall and query performance. However, this comes at the cost of longer index creation times.  
  
Since three-level trees build faster than two-level trees, you can increase the `num_leaves_value` when creating a three-level tree index to achieve better performance.  


  * **Two-level index** : Set this value to any value between `1` and `1048576`.  
  
For an index that balances fast index build and good search performance, use `sqrt(ROWS)` as a starting point, where `ROWS` is the number of vector rows. The number of vectors that each partition holds is calculated by   
`ROWS/sqrt(ROWS) = sqrt(ROWS)`.  
  
Since a two-level tree index can be created on a dataset with less than 10 million vector rows, each partition will hold less than (`sqrt(10M)`) vectors, which is `3200` vectors. For optimal vector search quality, it's recommended to minimize the number of vectors in each partition. The recommended partition size is about 100 vectors per partition, so set `num_leaves` to `ROWS/100`. If you have 10 million vectors you would set `num_leaves` to 100,000.
  * **Three-level index** : Set this value to any value between `1` and `1048576`.  
  
If you are unsure about selecting the exact value, use `power(ROWS, 2/3)` as a starting point, where `ROWS` is the number of vector rows. The number of vectors that each partition holds is calculated by   
`ROWS/power(ROWS, 2/3) = power(ROWS, 1/3)`.  
  
Since a three-level tree index can be created on a dataset with vector rows more than 100 million, each partition will hold more than   
(`power(100M, 1/3)`) vectors, which is `465` vectors. For optimal vector search quality, it's recommended to minimize the number of vectors in each partition. The recommended partition size is about 100 vectors per partition, so set `num_leaves` to `ROWS/100`. If you have 100 million vectors you would set `num_leaves` to 1 million.

| Index creation   
(required)  
`quantizer` | The type of quantizer you want to use for the K-means tree. The default value is set to `SQ8` which provides better query performance with minimal recall loss (typically less than 1-2%).  
  
Set it to `FLAT` if a recall of 99% or higher is required. | Index creation   
(optional)  
`scann.enable_inline_filtering` | Enables inline filtering support that queries your data and applies filters directly within a vector similarity search operation. These vector similarity queries use filters on the same database tables and complete filter evaluation while computing the distance for nearest neighbor identification. This option is disabled by default.  
  
To enable inline filtering, set this parameter to `true`. If you observe deterioration in performance, then set to `false`.  
  
This option is available in [Preview](https://cloud.google.com/products#product-launch-stages). | Query runtime   
(optional)  
`scann.enable_pca` | Enables Principal Component Analysis (PCA), which is a dimension reduction technique used to automatically reduce the size of the embedding when possible. This option is enabled by default.  
  
Set to `false` if you observe deterioration in recall. | Index creation   
(optional)  
`scann.num_leaves_to_search` | This database flag controls the absolute number of leaves or partitions to search which lets you trade off between recall and QPS. The default value is 1% of the value set in `num_leaves`.   
  
A higher value will result in better recall but lower QPS. Similarly, a lower value will result in lower recall but higher QPS. | Query runtime   
(optional)  
`scann.pre_reordering_num_neighbors` | The database flag, when set, specifies the number of candidate neighbors to consider during the reordering stages after the initial search identifies a set of candidates. Set this parameter to a value higher than the number of neighbors you want the query to return.   
  
A higher value results in better recall, but a lower QPS. Set this value to `0` to disable reordering. The default is `0` if PCA is not enabled during index creation. Otherwise, the default is `50 x K`, where `K` is the LIMIT specified in the query.  | Query runtime   
(optional)  
`scann.num_search_threads` | The number of searcher threads for multi-thread search. This can help reduce single query latency by using more than one thread for ScaNN ANN search in latency-sensitive applications. This setting doesn't improve single query latency if the database is already cpu-bound. The default value is `2`. | Query runtime   
(optional)  
  
## What's next

  * [Get started with vector embeddings using AlloyDB AI](https://codelabs.developers.google.com/alloydb-ai-embedding#0).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
