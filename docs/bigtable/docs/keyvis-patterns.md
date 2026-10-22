---
url: https://docs.cloud.google.com/bigtable/docs/keyvis-patterns/
title: Heatmap patterns \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:55:22.531024+00:00
---

# Heatmap patterns  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/keyvis-patterns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Heatmap patterns

This page shows examples of patterns that you might see in the heatmap for a Key Visualizer scan, then explains the meaning of each pattern. Use this information to help you diagnose performance issues with Bigtable.

  * To learn how to open a Key Visualizer scan, see [Viewing the scan for a time period](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started#viewing-scan).
  * To find out how to explore a Key Visualizer scan in detail, see [Exploring Heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps).



Before you read this page, you should be familiar with the [overview of Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-overview). 

## Overview of common patterns

This page explains how to interpret the following Key Visualizer patterns.

![](https://docs.cloud.google.com/bigtable/img/keyvis-patterns-ideal-thumb.png)Even distribution ![](https://docs.cloud.google.com/bigtable/img/keyvis-patterns-periodic-thumb.png)Periodic usage ![](https://docs.cloud.google.com/bigtable/img/keyvis-patterns-hot-ranges-thumb.png)Hot key ranges   
  
![](https://docs.cloud.google.com/bigtable/img/keyvis-patterns-inflection-thumb.png)Sudden increases ![](https://docs.cloud.google.com/bigtable/img/keyvis-patterns-sequential-thumb.png)Sequential reads/writes

## Evenly distributed reads and writes

![Heatmap showing evenly distributed reads and writes](https://docs.cloud.google.com/bigtable/img/keyvis-patterns-ideal-thumb.png)

If a heatmap shows a fine-grained mix of dark and bright colors, then reads and writes are evenly distributed throughout the table. This heatmap represents an effective usage pattern for Bigtable, so you do not need to take any action.

## Periodic usage

![Heatmap showing a periodic usage pattern](https://docs.cloud.google.com/bigtable/img/keyvis-patterns-periodic-thumb.png)

If a heatmap shows alternating bands of dark and bright colors within a key range, then you are accessing that key range during certain periods but not others. For example, you might be running a batch job that accesses the key range at specific times of day.

This usage pattern is not a problem as long as it does not result in excessive CPU utilization or latency, and as long as you intended to access your data in this way. If this pattern results in excessive CPU usage, you might need to [add nodes to your cluster](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes) during peak usage periods. If you did not intend to access your data much more heavily during specific periods of time, examine your applications to find out which ones are not behaving correctly.

## Hot key ranges

![Heatmap showing hot key ranges](https://docs.cloud.google.com/bigtable/img/keyvis-patterns-hot-ranges-thumb.png)

If a heatmap shows horizontal bands of bright color, separated by dark colors, then the brightly colored key ranges have one of the following issues:

  * If you are viewing the **Read pressure index** or **Write pressure index** metrics, the hot key range might be causing high CPU utilization or high latency. These issues can occur if you perform a large number of reads or writes, or if you store more than 256 MB in a row. Pay special attention if this warning is triggered by a single row, rather than a range of rows.
  * If you are viewing the **Large rows** metric, the key range includes rows that contain more than 256 MB of data or an average of more than 200 MB per row.
  * If you are viewing another metric, it's likely that you are accessing rows in that key range much more heavily than other rows.



Take at least one of the following actions to address the issue:

  * Use [filters](https://docs.cloud.google.com/bigtable/docs/filters) to reduce the amount of data that you read. 
  * Change your [schema design](https://docs.cloud.google.com/bigtable/docs/schema-design) or your application so that the data in a heavily used row, or in an excessively large row, is spread across multiple rows. 
  * Update your application to cache the results of reads from Bigtable. 
  * Update your application to batch and deduplicate writes to Bigtable. 



## Sudden increases

![Heatmap showing a sudden increase](https://docs.cloud.google.com/bigtable/img/keyvis-patterns-inflection-thumb.png)

If a heatmap shows a key range that suddenly changes from dark to bright, then one of the following changes occurred:

  * If you are viewing the **Large rows** metric, you added a large amount of data to rows in that key range during a short period of time.

Delete data from the large rows, or change your [schema design](https://docs.cloud.google.com/bigtable/docs/schema-design) so that less data is stored in those rows.

  * If you are viewing another metric, it's likely that you started to access those rows much more heavily than usual at a specific point in time.

This usage pattern is not a problem as long as it does not result in excessive CPU utilization or latency, and as long as you intended to access your data in this way. If this pattern results in excessive CPU usage, you might need to [add nodes to your cluster](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes) during peak usage periods. If you did not intend to start accessing your data much more heavily at a specific point in time, examine your applications to find out which ones are not behaving correctly.




## Sequential reads and writes

![Heatmap showing sequential reads and writes within a key range](https://docs.cloud.google.com/bigtable/img/keyvis-patterns-sequential-thumb.png)

If a heatmap shows a bright diagonal line, then you are accessing contiguous key ranges within a table in sequential order. For example, you might have run a batch job that iterates over the table's row keys.

This usage pattern is not a problem as long as it does not result in excessive CPU utilization or latency, and as long as you intended to access your data in this way. If this pattern results in excessive CPU usage, you might need to [add nodes to your cluster](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes) during peak usage periods. If you did not intend to access rows within your table in sequential order, examine your applications to find out which ones are not behaving correctly.

## What's next

  * Learn how to [get started with Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started).
  * Find out how to [explore a heatmap in detail](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps).
  * Read about the [metrics you can view in a heatmap](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
