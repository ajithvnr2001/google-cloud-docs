---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/adaptive-filtering/
title: Activate adaptive filtering in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:40:13.829425+00:00
---

# Activate adaptive filtering in AlloyDB Omni  |  AlloyDB Omni for containers: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/adaptive-filtering/

This page documents AlloyDB Omni version **15.7.1** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)



Send feedback 

#  Activate adaptive filtering in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/adaptive-filtering)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/adaptive-filtering)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/adaptive-filtering)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/adaptive-filtering)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/ai/adaptive-filtering)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/adaptive-filtering)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/adaptive-filtering)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/adaptive-filtering)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/ai/adaptive-filtering)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/adaptive-filtering)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/adaptive-filtering)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/adaptive-filtering)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/adaptive-filtering)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/adaptive-filtering)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/adaptive-filtering)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/adaptive-filtering)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/adaptive-filtering)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/adaptive-filtering)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/adaptive-filtering)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/adaptive-filtering)



**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to use adaptive filtering in AlloyDB Omni. This page describes how to use adaptive filtering in AlloyDB Omni.

**Note:** Inline filtering is supported only when you use the ScaNN algorithm. Inline filtering is not compatible with the Inverted File (IVF), Inverted File Flat (IVFFlat), or Hierarchical Navigable Small Worlds (HNSW) algorithms.

Adaptive filtering analyzes query patterns and data distributions during query execution to dynamically choose the most efficient filtering strategy such as inline or pre-filtering.

The AlloyDB Omni query optimizer uses cost-based analysis to determine whether inline filtering or pre-filtering provides the best performance at any given point during query execution.

Such optimization is beneficial for AlloyDB Omni's filtered vector searches, where adaptive filtering automatically switches between vector and metadata index usage to ensure efficient and accurate results without your manual intervention.

## Enable adaptive filtering

To enable adaptive filtering, use the [`scann.enable_preview_features`](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/reference/alloydb-flags#scann.enable_preview_features) flag.

When adaptive filtering triggers a switch from inline filtering to pre-filtering during execution, the query plan dynamically changes.

For example, the plan can show `Bitmap assisted pre-filtering` in the **Execution Strategy** field when the optimizer determines that pre-filtering is more efficient at that point in the query. This dynamic change occurs as the system adapts to the actual data that it encounters during the query's execution.
    
    
    Limit (actual rows=10 loops=1)
      ->  Custom Scan (vector scan) on t1 (actual rows=10 loops=1)
            Execution Strategy: Bitmap assisted pre-filtering
            Order By: (vec_col <=> '[...]'::vector)
            Limit: 10
            Num Requalifications: 0
            Num filtered: 1000
            ->  Bitmap Index Scan on btree_idx (actual rows=10000 loops=1)
                  Index Cond: (int_col <= 100000000)
    

## What's next

  * [Filtered vector search in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/filtered-vector-search-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
