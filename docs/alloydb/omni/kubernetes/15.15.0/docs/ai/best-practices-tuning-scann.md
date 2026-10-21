---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/best-practices-tuning-scann/
title: Best practices for tuning ScaNN indexes \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.15.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:40:12.042125+00:00
---

# Best practices for tuning ScaNN indexes  |  AlloyDB Omni using the container orchestrator: 15.15.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/best-practices-tuning-scann/

This page documents AlloyDB Omni version **15.15.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/overview)



Send feedback 

#  Best practices for tuning ScaNN indexes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.15.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/best-practices-tuning-scann)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/best-practices-tuning-scann)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/best-practices-tuning-scann)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/best-practices-tuning-scann)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/ai/best-practices-tuning-scann)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/best-practices-tuning-scann)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/best-practices-tuning-scann)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/ai/best-practices-tuning-scann)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/ai/best-practices-tuning-scann)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/ai/best-practices-tuning-scann)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/best-practices-tuning-scann)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/best-practices-tuning-scann)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/ai/best-practices-tuning-scann)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/best-practices-tuning-scann)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/ai/best-practices-tuning-scann)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/best-practices-tuning-scann)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/best-practices-tuning-scann)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/ai/best-practices-tuning-scann)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/ai/best-practices-tuning-scann)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/ai/best-practices-tuning-scann)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/ai/best-practices-tuning-scann)

This page provides recommendations about how to tune AlloyDB Omni index parameters for optimal balance between recall and QPS. The recommended parameters for the Scalable Nearest Neighbor (ScaNN) index differ depending on whether you choose to build a two-level or a three-level tree index. 

## ScaNN index creation

For more information, see the [ScaNN Index reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/scann-index-reference).

### Two-level tree index

To apply recommendations to help you find the optimal values of `num_leaves` and `num_leaves_to_search` for your dataset, follow these recommended steps:

  1. To create the `ScaNN` index optimized for the following cases set the `num_leaves` parameter to the following value, where rows is the number of rows in the indexed table: 
     * **balanced index build time and quality** set `num_leaves` to `sqrt(rows)`.
     * **quality** set num_leaves to rows/100.
  2. Run your test queries, increasing the value of `scann.num_of_leaves_to_search`, until you achieve your target recall range–for example, 95%. For more information about analyzing your queries, see [Analyze your queries](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes?resource=scann#explain-analyze).
  3. Take note of the ratio between `scann.num_leaves_to_search` and `num_leaves` that will be used in subsequent steps. This ratio provides an approximation around the dataset that will help you achieve your target recall.  
  
If you are working with high dimension vectors (500 dimensions or higher) and want to improve recall, then try tuning the value of `scann.pre_reordering_num_neighbors`. The default value is set to the value `500 * K` where `K` is the limit that you set in your query.
  4. If your QPS is too low after your queries achieve a target recall, then follow these steps: 
     1. Recreate the index, increasing the value of `num_leaves` and `scann.num_leaves_to_search` according to the following guidance: 
        * Set `num_leaves` to a larger factor of the square root of your row count. For example, if the index has `num_leaves` set to the square root of your row count, try setting it to double the square root. If the value is already double, then try setting it to triple the square root.
        * Increase `scann.num_leaves_to_search` as needed to maintain its ratio with `num_leaves`, which you noted in Step 3.
        * Set `num_leaves` to a value less than or equal to the row count divided by 100.
     2. Run the test queries again. While you're running the test queries, experiment with reducing `scann.num_leaves_to_search`, finding a value that increases QPS while keeping your recall high. Try different values of `scann.num_leaves_to_search` without rebuilding the index.
  5. Repeat Step 4 until both the QPS and the recall range have reached acceptable values.



### Three-level tree index

In addition to the recommendations for the two-level tree `ScaNN` index, use the following guidance.

To apply recommendations to find the optimal value of `num_leaves` and `max_num_levels` index parameters, follow these steps:

  1. Create the `ScaNN` index with the following `num_leaves` and `max_num_levels` combinations based on your performance goals:

     * **balance index build time & quality**: Set `max_num_levels` as `2` and `num_leaves` as `power(rows, ⅔)`.
     * **optimize for quality** : Set `max_num_levels` as `2` and `num_leaves` as `rows/100`.
  2. Run your test queries. For more information about analyzing queries, see [Analyze your queries](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/tune-indexes?resource=scann#explain-analyze).

  3. Take note of the ratio between `scann.num_leaves_to_search` and `num_leaves` that will be used in subsequent steps. This ratio provides an approximation around the dataset that will help you achieve your target recall.




If you are working with high dimension vectors (500 dimensions or higher) and want to improve recall, then try tuning the value of `scann.pre_reordering_num_neighbors`. The default value is set to the value `500 * K` where `K` is the limit that you set in your query.

  1. If your QPS is too low after your queries achieve a target recall, then follow these steps:

     * Recreate the index, increasing the value of `num_leaves` and `scann.num_leaves_to_search` according to the following guidance:
     * Set `num_leaves` to a larger factor of the `power(rows, ⅔)`. For example, if the index has `num_leaves` set to the `power(rows, ⅔)`, try setting it to double the `power(rows, ⅔)`. If the value is already double, then try setting it to triple the `power(rows, ⅔)`.
     * Increase `scann.num_leaves_to_search` as needed to maintain its ratio with `num_leaves`, which you noted in Step 3.
     * Set `num_leaves` to a value less than or equal to `rows/100`.
     * Run the test queries again. While you're running the test queries, experiment with reducing `scann.num_leaves_to_search`, finding a value that increases QPS while keeping your recall high. Try different values of `scann.num_leaves_to_search` without rebuilding the index.
  2. Repeat Step 4 until both the QPS and the recall range have reached acceptable values.




## Index maintenance

If your table is prone to frequent updates or insertions, then we recommend periodically reindexing the existing `ScaNN` index in order to improve the recall accuracy. You can monitor index metrics to view changes in vector distributions or vector mutations since the index was built, and then reindex accordingly. For more information about metrics, see [Vector index metrics](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/vector-index-metrics).

## What's next

  * [Get started with vector embeddings using AlloyDB AI](https://codelabs.developers.google.com/alloydb-ai-embedding#0).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
