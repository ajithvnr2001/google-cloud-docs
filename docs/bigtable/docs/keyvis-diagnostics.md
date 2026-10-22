---
url: https://docs.cloud.google.com/bigtable/docs/keyvis-diagnostics/
title: Key Visualizer diagnostic messages \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:39.709201+00:00
---

# Key Visualizer diagnostic messages  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/keyvis-diagnostics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Key Visualizer diagnostic messages

This page describes the diagnostic messages that Key Visualizer can display above a heatmap. Some diagnostic messages identify performance issues with the Bigtable table. Other messages highlight possible inaccuracies in the performance data that you should consider as you review the Key Visualizer scan.

Before you read this page, you should be familiar with the [overview of Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-overview). 

## High read pressure

The **High read pressure** message indicates that some key ranges in the table experienced high read pressure. See [Warnings](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics#warnings) for details.

This diagnostic message normally includes a **Warning** ![Warning](https://docs.cloud.google.com/static/bigtable/img/keyvis-icon-warning-1x.png) icon. If the issue was caused by individual rows, rather than a range of rows, the message includes a **Danger** ![Danger](https://docs.cloud.google.com/static/bigtable/img/keyvis-icon-danger-1x.png) icon. 

## High write pressure

The **High write pressure** message indicates that some key ranges in the table experienced high write pressure. See [Warnings](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics#warnings) for details.

This diagnostic message normally includes a **Warning** ![Warning](https://docs.cloud.google.com/static/bigtable/img/keyvis-icon-warning-1x.png) icon. If the issue was caused by individual rows, rather than a range of rows, the message includes a **Danger** ![Danger](https://docs.cloud.google.com/static/bigtable/img/keyvis-icon-danger-1x.png) icon. 

## Large rows

The **Large rows** message indicates that some of the rows in the table contain more than 256 MB of data or that some key ranges contain an average of more than 200 MB of data per row.

## No data scanned

The **No data scanned** message indicates that Key Visualizer did not find any performance data for the table. This message normally appears if the table does not contain any data.

## Key space not to scale

The **Key space not to scale** message indicates that Key Visualizer could not evenly distribute the table's row keys into a smaller number of key buckets. See [Key buckets](https://docs.cloud.google.com/bigtable/docs/keyvis-overview#key-buckets) for details.

This message normally appears if the table contains a small number of rows.

**Note:** Key space distribution is not related to how Bigtable stores your data. It merely reflects how Key Visualizer depicts the keys vertically.

## Values per row are approximate

The **Values per row are approximate** message indicates that the heatmap may contain inaccurate data for metrics that are expressed as per-row values. For example, the **Read CPU** and **Write CPU** metrics measure the CPU usage per row, so they are affected by this message.

This message appears if data in a table is growing or changing rapidly, and if more than 5% of Key Visualizer's performance data is affected as a result.

## Not all details shown in tooltip

The **Not all details shown in tooltip** message indicates that there was a very large number of row keys or key ranges that generated warnings. As a result, details are not available for all of the warnings. Key Visualizer's tooltips will show detailed information only for the most recent warnings.

## What's next

  * [Get started with Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started).
  * Learn [how Key Visualizer displays data in heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-overview#heatmaps).
  * Find out [how to explore Key Visualizer heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
