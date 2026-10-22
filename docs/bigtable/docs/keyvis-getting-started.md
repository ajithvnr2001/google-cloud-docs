---
url: https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started/
title: Use Key Visualizer \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:42.859553+00:00
---

# Use Key Visualizer  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use Key Visualizer

This page describes how to use Key Visualizer to check for performance issues that are related to your Bigtable usage patterns. If you haven't used Key Visualizer before, it's a good idea to complete this check at least once.

Before you read this page, you should be familiar with the [overview of Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-overview). 

## View a scan for a time period

Key Visualizer is available for tables that contain at least 1 GB of data per cluster. It can take up to an hour after a table reaches that size for scans to be available. 

To launch Key Visualizer:

  1. In the Google Cloud console, open the list of Bigtable instances. 

[ Open the instance list ](https://console.cloud.google.com/bigtable/instances)

  2. Click the instance whose metrics you want to view. 

  3. In the left-hand navigation pane, click **Key Visualizer**.

  4. Choose the table and cluster you wish to visualize, then click **Select**.

Key Visualizer opens and displays data for the time period beginning the last time the table's [key buckets were recalculated](https://docs.cloud.google.com/bigtable/docs/keyvis-overview#key-buckets) and ending at the current time.




To change the time period:

  1. Select **Resource** > **Key Visualizer**.

  2. Use the slider paddles to select the start and end time for the time span you want to see a heatmap for.

When you release the paddles, they "snap" to the nearest available time.

![Key Visualizer time span slider](https://docs.cloud.google.com/bigtable/img/keyvis-edit-slider.png)

  3. Click **Update**.

Depending on the time span length, it may take a few moments for the data to load.




As you review the scan, keep in mind that Key Visualizer heatmaps group metrics into key buckets, or contiguous ranges of rows, rather than showing metrics for each individual row. See [Key buckets](https://docs.cloud.google.com/bigtable/docs/keyvis-overview#key-buckets) for details.

If you want to compare metrics or look for data correlations, you can display several Key Visualizer metrics together at the same time for the scan you've chosen. See [Finding connections between different metrics](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps#finding-connections) for instructions.

## Check for performance issues

The following sections explain how to complete an initial check for performance issues.

### View an activity overview

As a first step, review the heatmap for the **Ops** metric, which measures the number of operations per row per minute. This metric is roughly equal to the combined number of reads and writes. Key Visualizer shows this metric by default when you open a heatmap.

The following example shows a heatmap where there are major differences in the usage pattern for different key ranges:

  * Ranges shown in dark colors have little or no activity.
  * Ranges in bright colors have significantly more activity.
  * The glowing white range in the middle has very high activity.



![Example of a Key Visualizer scan](https://docs.cloud.google.com/bigtable/img/keyvis-scan-example.png)

In the example, some of these patterns repeat every 24 hours, possibly because a large batch job runs every day at the same time.

As you look at the heatmap for the **Ops** metric, keep in mind that brightly colored areas do not necessarily indicate poor performance. In many cases, Bigtable can perform well even if reads and writes are not perfectly balanced across a table.

### Review Warnings metrics

The presence of **Warnings** metrics usually indicates that there is a performance issue. For **Warnings** metrics, Key Visualizer provides details about the row keys or key ranges that caused the metric to appear. [Learn more about the **Warnings** metrics](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics#warnings).

If any of the **Warnings** metrics include high values, a diagnostic message appears above the heatmap to identify the issue. [Learn more about diagnostic messages](https://docs.cloud.google.com/bigtable/docs/keyvis-diagnostics).

To review a **Warnings** metric, find the **Metric** drop-down list above the heatmap, then select one of the following metrics:

  * **Read pressure index**
  * **Write pressure index**
  * **Large rows**



If an item in this list is disabled, there are no warnings in that category. Otherwise, you should view the metric and drill down into the issue that it identifies. See [exploring heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps) for details.

If the heatmap shows only low values for a **Warnings** metric, or if there are high values that occur for less than 30 minutes, it's likely that you do not need to take any action. If you see high values for long periods of time, it's a good idea to investigate further.

If the **Read pressure index** metric for a key bucket is 100 or greater for a long period of time, you can take the following actions to lower the index:

  * Use [filters](https://docs.cloud.google.com/bigtable/docs/filters) to reduce the amount of data that you read. 
  * Change your [schema design](https://docs.cloud.google.com/bigtable/docs/schema-design) or your application so that the data in a heavily used row, or in an excessively large row, is spread across multiple rows. 
  * Update your application to cache the results of reads from Bigtable. 



If the **Write pressure index** metric for a key bucket is 100 or greater for a long period of time, you can take the following actions to lower the index:

  * Change your [schema design](https://docs.cloud.google.com/bigtable/docs/schema-design) or your application so that the data in a heavily used row, or in an excessively large row, is spread across multiple rows. 
  * Update your application to batch and deduplicate writes to Bigtable. 



If the **Large rows** metric is present for a key bucket, examine the rows in the highlighted key bucket, then change your [schema design](https://docs.cloud.google.com/bigtable/docs/schema-design) or your application so that less data is stored in those rows.

## Continue your investigation

If you complete the initial check for performance issues, and you don't see any major warnings or unexpected access patterns, you can close Key Visualizer and move on. Otherwise, continue your investigation by looking at other metrics and focusing more closely on key ranges that might be causing problems. [Learn more](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps).

## What's next

  * Learn to recognize [common patterns in heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-patterns).
  * Find out how to [explore a heatmap in depth](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps).
  * Read about the [metrics you can view in a heatmap](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics).
  * Understand the [diagnostic messages that Key Visualizer can display](https://docs.cloud.google.com/bigtable/docs/keyvis-diagnostics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
