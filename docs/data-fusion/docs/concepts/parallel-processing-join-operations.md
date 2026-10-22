---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/parallel-processing-join-operations/
title: Parallel processing for JOIN operations \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:00.080953+00:00
---

# Parallel processing for JOIN operations  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/parallel-processing-join-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Parallel processing for JOIN operations Stay organized with collections  Save and categorize content based on your preferences. 

This page explains performance tuning for `JOIN` operations in Cloud Data Fusion.

`JOIN` operations can be the most expensive part of a pipeline. Like everything else in a pipeline, operations are executed in parallel. The first step of a `JOIN` is to shuffle data so that every record with the same `JOIN` key is sent to the same executor. After all of the data is shuffled, it's joined, and the output continues through the pipeline.

## Example of parallel processing in `JOIN` operations

For example, suppose you perform a `JOIN` operation on datasets called `Purchases` and `Items`. Each purchase record contains an item name and number purchased. Each item record contains the item name and the price of that item. A `JOIN` is performed on the item name to calculate the total price of each purchase. When the data is joined, data is shuffled across the cluster such that records with the same ID end up on the same executor.

When the `JOIN` keys are fairly evenly distributed, `JOIN` operations perform well because they can be executed in parallel.

Like any shuffle, data skew negatively impacts performance. In the preceding example, eggs are purchased much more frequently than chicken or milk, which means the executor joining the egg purchases does more work than the other executors. If you notice that a `JOIN` is skewed, there are two ways to improve performance.

### Automatically split up skewed partitions

With adaptive query execution, really heavy skews will be handled automatically. As soon as a `JOIN` produces some partitions much larger than others, they are split into smaller ones. To confirm you have adaptive query execution enabled, see [Autotuning](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/818544644/Parallel+Processing#Autotuning).

### Use an in-memory `JOIN`

An in-memory `JOIN` can be performed if one side of the `JOIN` is small enough to fit in memory. In this situation, the small dataset is loaded into memory, and then gets broadcasted to every executor. The large dataset isn't shuffled at all, removing the uneven partitions that are generated when shuffling on the `JOIN` key.

In the previous example, the items dataset is first loaded into memory of the Spark driver. It is then broadcast to each executor. Executors can now join the data without shuffling any of the purchase dataset.

This approach requires you to give enough memory to both the Spark driver and executors to allow them to store the broadcast dataset in memory. By default, Spark reserves slightly less than 30% of its memory for storing this type of data. When using in-memory `JOIN`s, multiply the size of the dataset by four and set that as the executor and driver memory. For example, if the items dataset was 1 GB in size, we would need to set the executor and driver memory to at least 4 GB. Datasets larger than 8 GB cannot be loaded into memory.

## Key distribution

When both sides of the `JOIN` are too large to fit in memory, a different technique can be used to break up each `JOIN` key into multiple keys to increase the level of parallelism. This technique can be applied to `INNER JOIN` and `LEFT OUTER JOIN`operations. It cannot be used for `FULL OUTER JOIN` operations.

In this approach, the skewed side is salted with a new integer column with a random number from 1 to N. The unskewed side is exploded, with each existing row generating `N` new rows. A new column is added to the exploded side, populated with each number from 1 to N. A normal `JOIN` is then performed, except the new column is added as part of the `JOIN` key. In this way, all the data that used to go to a single partition is now spread out to up to `N` different partitions.

In the preceding example, the distribution factor `N` is set to `3`. The original datasets are shown on the left. The salted and exploded versions of the dataset are shown in the middle. The shuffled data is shown on the right, with three different executors joining egg purchases, instead of one.

Greater parallelism is achieved by increasing distributions. However, this comes at the cost of exploding one side of the `JOIN`, resulting in more data shuffled across the cluster. Because of this, the benefit diminishes as distribution increases. In most situations, set it to 20 or less.

## What's next

  * Learn more about [parallel processing](https://docs.cloud.google.com/data-fusion/docs/concepts/parallel-processing) in Cloud Data Fusion.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
