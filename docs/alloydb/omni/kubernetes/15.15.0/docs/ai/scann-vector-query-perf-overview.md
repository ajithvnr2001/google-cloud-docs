---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/scann-vector-query-perf-overview/
title: ScaNN vector query performance overview \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.15.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:52:11.532235+00:00
---

# ScaNN vector query performance overview  |  AlloyDB Omni using the container orchestrator: 15.15.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/scann-vector-query-perf-overview/

This page documents AlloyDB Omni version **15.15.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/overview)



Send feedback 

#  ScaNN vector query performance overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.15.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/scann-vector-query-perf-overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/scann-vector-query-perf-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/scann-vector-query-perf-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/scann-vector-query-perf-overview)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/ai/scann-vector-query-perf-overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/scann-vector-query-perf-overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/scann-vector-query-perf-overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/ai/scann-vector-query-perf-overview)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/ai/scann-vector-query-perf-overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/ai/scann-vector-query-perf-overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/scann-vector-query-perf-overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/scann-vector-query-perf-overview)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/ai/scann-vector-query-perf-overview)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/scann-vector-query-perf-overview)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/ai/scann-vector-query-perf-overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/scann-vector-query-perf-overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/scann-vector-query-perf-overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/ai/scann-vector-query-perf-overview)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/ai/scann-vector-query-perf-overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/ai/scann-vector-query-perf-overview)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/ai/scann-vector-query-perf-overview)

This page provides a conceptual overview of improving vector query performance using the AlloyDB AI Scalable Nearest Neighbor (ScaNN) index. For more information, see [Create a ScaNN index](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/create-scann-index). 

The ScaNN index uses tree-quantization-based indexing, in which indexes learn a search tree together with a quantization (or hashing) function. When you run a query, the search tree is used to prune the search space, while quantization is used to compress the index size. This pruning speeds up the scoring of the similarity—in other words, the distance—between the query vector and the database vectors.

To achieve both a high query-per-second rate (QPS) and a high recall with your nearest-neighbor queries, you must partition the tree of your ScaNN index in a way that is most appropriate to your data and your queries.

High-dimensional embedding models can retain much of the information at much lower dimensionality. For example, you can retain 90% of the information with only 20% of the embedding's dimensions. To help speed up such datasets, the AlloyDB AI ScaNN index automatically performs dimension reduction using [Principal Component Analysis](https://en.wikipedia.org/wiki/Principal_component_analysis) (PCA) on the indexed vectors, which further reduces CPU and memory usage for the vector search. For more information, see [`scann.enable_pca`](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/scann-index-reference).

Because dimension reduction causes minor recall loss in the index, the AlloyDB AI ScaNN index compensates for recall loss by first performing a ranking step with a larger number of PCAed vector candidates from the index. Then, ScaNN re-ranks the PCAed vector candidates by the original vectors. For more information, see [`scann.pre_reordering_num_neighbors`](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/scann-index-reference).

## What's next

  * Learn [best practices for tuning ScaNN indexes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/best-practices-tuning-scann).

  * [Get started with vector embeddings using AlloyDB AI](https://codelabs.developers.google.com/alloydb-ai-embedding#0).

  * Learn more about the [AlloyDB AI ScaNN index](https://cloud.google.com/blog/products/databases/understanding-the-scann-index-in-alloydb).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
