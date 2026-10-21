---
url: https://docs.cloud.google.com/bigtable/docs/keyvis-metrics/
title: Key Visualizer metrics \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:24:27.642684+00:00
---

# Key Visualizer metrics  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/keyvis-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Key Visualizer metrics

This page describes the metrics that you can view in Key Visualizer heatmaps.

Most Key Visualizer metrics represent a quantity per row. For example, the **Ops** metric measures the number of operations per row per minute.

A Bigtable table can have trillions of rows, so it's not always practical to report metrics for each individual row. Instead, Key Visualizer divides all of the row keys into 1,000 contiguous ranges, with roughly the same number of row keys in each range. These ranges are known as _key buckets_. 

Key Visualizer reports most metrics as averages over each key bucket, or as maximum values within each key bucket. For [**Warnings** metrics](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics#warnings) and [**Performance** metrics](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics#performance), Key Visualizer provides higher precision by reporting metrics for individual row keys or for specific key ranges within the key bucket. 

Before you read this page, you should be familiar with the [overview of Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-overview). 

## Activity

The Activity category includes the **Ops** metric, which measures the number of operations per row per minute. This metric is roughly equal to the combined number of reads and writes and can indicate which keys received more requests at a given time. Color indicates values relative to all observed values; therefore, yellow or white do not necessarily imply a hotspot.

## Warnings

The Warnings category includes metrics that identify possible performance issues with a table. This category includes the following metrics: 

  * **Read pressure index** : An opaque, composite index for a row key or key range that incorporates the CPU utilization and latency for reads.

This index reflects all of the values that were observed during a 15-minute interval. A value of 100 or greater generally indicates poor performance for a key range. Poor performance can occur when you access a single row or a small range of rows very frequently, or when a row contains more than 256 MB of data. 

  * **Write pressure index** : An opaque, composite index for a row key or key range that incorporates the CPU utilization and latency for writes.

This index reflects all of the values that were observed during a 15-minute interval. A value of 100 or greater generally indicates poor performance for a key range. Poor performance can occur when you access a single row or a small range of rows very frequently, or when a row contains more than 256 MB of data. 

  * **Large rows** : The amount of data stored in rows that each contain more than 256 MB of data, or in key ranges with an average of more than 200 MB per row.

Storing more than 256 MB of data per row can cause performance issues and read errors, and is not recommended.




For these metrics, when you move your cursor over the heatmap, Key Visualizer does not display aggregated information for a key bucket. Instead, it displays information about specific row keys or key ranges in your table, so that you can pinpoint the source of the issue. See [Reviewing warning metrics](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started#reviewing-warning-metrics) to learn how to view and act on these metrics. 

## Reads

The Reads category includes metrics related to reading data from a table. This category includes the following metrics: 

  * **Read CPU** : The average CPU utilization, expressed as the number of nodes that were used to read a row. Color indicates values relative to all observed values; therefore, yellow or white do not necessarily imply a hotspot.
  * **Read bytes client** : The number of bytes read by the client per minute per row. Color indicates values relative to all observed values; therefore, yellow or white do not necessarily imply a hotspot.



## Writes

The Writes category includes metrics related to writing data to a table. This category includes the following metrics: 

  * **Write CPU** : The average CPU utilization, expressed as the number of nodes that were used to write a row. Color indicates values relative to all observed values; therefore, yellow or white do not necessarily imply a hotspot.
  * **Write bytes client** : The number of bytes written by the client per minute per row. Color indicates values relative to all observed values; therefore, yellow or white do not necessarily imply a hotspot.



## Performance

The Performance category includes metrics related to latency. This category includes the following metrics: 

  * **Latency** : The latency for read and write operations. One second (shown as orange) can be considered high.
  * **Latency (max)** : The maximum latency for reads or writes. One second (shown as orange) can be considered high.



For these metrics, when you move your cursor over the heatmap, Key Visualizer does not display aggregated information for a key bucket. Instead, it displays information about specific row keys or key ranges in your table, so that you can pinpoint the source of the issue. 

## Size

  * **Data stored:** The amount of data stored per row. This metric reflects the fact that Bigtable compresses your data when it is stored. 
  * **Rows:** The approximate number of rows in each key bucket.

The **Rows** heatmap typically appears mostly yellow. Horizontal stripes increasing in brightness from left to right, going from a darker color to a lighter color, indicate the addition of rows. Stripes that decrease in brightness from left to right indicate the deletion of rows.

![Number of rows in a Key Visualizer bucket](https://docs.cloud.google.com/bigtable/img/keyvis-rows-in-bucket.png)

To see the total number of rows for a given key prefix, click on that prefix in the key hierarchy, then inspect the tooltips over the horizontal bar chart along the bottom.




## What's next

  * [Get started with Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started).
  * Learn [how Key Visualizer displays data in heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-overview#heatmaps).
  * Find out [how to explore Key Visualizer heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
