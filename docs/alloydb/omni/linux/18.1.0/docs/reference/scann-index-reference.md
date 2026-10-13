---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/reference/scann-index-reference/
title: AlloyDB Omni ScaNN index reference \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:46:54.454323+00:00
---

# AlloyDB Omni ScaNN index reference  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/reference/scann-index-reference/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/reference/database-flags)



Send feedback 

#  AlloyDB Omni ScaNN index reference Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://forms.gle/zxuHekMtV67Bw9Av9). 

Select a documentation version: 18.1.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/reference/scann-index-reference)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/reference/scann-index-reference)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/reference/scann-index-reference)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/reference/scann-index-reference)

This page provides a detailed reference for the tuning parameters available for Scalable Nearest Neighbors (ScaNN) indexes in AlloyDB Omni. 

For a step-by-step tutorial on how to implement vector search from start to finish, see the guide on how to [Perform a vector search](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/perform-vector-search).

**Note:** Before creating a ScaNN index, you must install the `alloydb_scann` and `vector` extensions. For details on the `CREATE INDEX` command, refer to [Create indexes](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/store-index-query-vectors?resource=scann).

## Tuning parameters

The following index and query parameters are used to find the right balance of recall and queries per second (QPS).

Option typeIndex creationQuery runtime

Tuning parameter | Description | Option type  
---|---|---  
`mode` |  Defines the ScaNN index as either an automatically-tuned or manually-tuned index. The available options are as follows: 

  * `AUTO`: automatically-tuned index
  * `MANUAL`: manually-tuned index

For more information, see [Create a ScaNN index](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/create-scann-index).  |  Index creation (optional)  
`max_num_levels` |  Maximum number of centroid levels of the K-means clustering tree. For guidance on setting this value, see [Tune a ScaNN index](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/tune-indexes#tune-scann-indexes). The available values are as follows:

  * `1`: Two-level ScaNN index
  * `2`: Three-level ScaNN index
  * `3`: Four-level ScaNN index ([Preview](https://cloud.google.com/products#product-launch-stages))

If you set `max_num_levels` to `3`, you must also set `scann.max_allowed_num_levels` to `3`. For more information, see [Best practices for tuning ScaNN indexes](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/best-practices-tuning-scann).  |  Index creation (optional)  
`num_leaves` |  Number of partitions to apply to this index. The maximum value is `30000000`. For more information on choosing this value, see [Tune a ScaNN index](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/tune-indexes#tune-scann-indexes) and [Best practices for tuning ScaNN indexes](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/best-practices-tuning-scann).  |  Index creation (required for [manually-tuned](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/create-scann-index#create-scann-index-manual) indexes)   
`quantizer` | The type of quantizer you want to use for the K-means tree. The default value is set to `SQ8` which provides better query performance with minimal recall loss (typically less than 1-2%).  
  
Set it to `FLAT` if a recall of 99% or higher is required. | Index creation   
(optional)  
`scann.enable_pca` | Enables Principal Component Analysis (PCA), which is a dimension reduction technique used to automatically reduce the size of the embedding when possible. This option is enabled by default.  
  
Set to `false` if you observe deterioration in recall. | Index creation   
(optional)  
`auto_maintenance` |  Automatically maintain a ScaNN index so that as your dataset grows, AlloyDB Omni analyzes and updates centroids, and splits large outlier partitions. This automatically improves QPS and search results. For more information, see [Maintain indexes automatically](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/maintain-vector-indexes#maintain-index-automatically).  |  Index creation (optional)  
`scann.pct_leaves_to_search` |  Automatically manage the number of partitions that a vector index searches. For more information, see [Search percentage of partitions](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/maintain-vector-indexes#maintain-index-automatically).  |   
`scann.num_leaves_to_search` |  Absolute number of partitions to search. This lets you trade off between query recall and QPS. The default value is 1% of `num_leaves`.  Higher values result in better query recall, but lower QPS. Similarly, lower values result in worse query recall, but better QPS.  |  Query runtime (optional)  
`scann.pre_reordering_num_neighbors` |  Specifies the number of candidate neighbors to consider during the reordering stages once the initial search identifies a set of candidates. Set this parameter to a value higher than the number of neighbors you want the query to return. Higher values result in better recall, but lower QPS.  The default is `0`, which disables reordering. If PCA is enabled during index creation, the default is `50 x K`, where `K` is the LIMIT specified in the query.  |  Query runtime (optional)  
`scann.num_search_threads` | The number of searcher threads for multi-thread search. This can help reduce single query latency by using more than one thread for ScaNN ANN search in latency-sensitive applications. This setting doesn't improve single query latency if the database is already cpu-bound. The default value is `2`. | Query runtime   
(optional)  
`scann.satisfy_limit` ([Preview](https://cloud.google.com/products#product-launch-stages)) | When set to `relaxed_order`, the database flag addresses insufficient recall. Insufficient recall can occur when a query's observed recall falls below the target recall, which is more likely when using filters. This setting helps achieve the target recall by allowing the vector scan to continue searching beyond the `num_leaves_to_search` limit until a sufficient number of results are found. | Query runtime   
(optional)  
`scann.max_pct_leaves_to_search` ([Preview](https://cloud.google.com/products#product-launch-stages)) | This database flag sets an upper bound on the percentage of total leaves that can be visited for queries that you run with `scann.satisfy_limit` enabled. This is the only upper bound GUC available and applies to both auto and manual search modes. It prevents the search from overshooting, which might significantly degrade performance. This is applicable when `scann.satisfy_limit` is turned on.  
You can set this parameter to any value between `0` to `100`. The default value is `15%`. This default value is based on the rationale that if a search needs to examine more than 15% of the leaves, the filter is likely selective enough that approximate nearest neighbor (ANN) search doesn't provide a benefit, making pre-filtering k-nearest neighbor (KNN) a more suitable choice. | Query runtime   
(optional)  
  
## What's next

  * [Get started with vector embeddings using AlloyDB AI](https://codelabs.developers.google.com/alloydb-ai-embedding#0).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
