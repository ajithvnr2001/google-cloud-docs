---
url: https://docs.cloud.google.com/bigtable/docs/keyvis-overview/
title: Overview of Key Visualizer \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:27.327637+00:00
---

# Overview of Key Visualizer  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/keyvis-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Overview of Key Visualizer

Key Visualizer is an interactive diagnostic tool that lets you analyze Bigtable access patterns and usage across your tables. You can use its visual heatmaps to detect performance bottlenecks, identify hotspots, and optimize your schema design.

## What is Key Visualizer?

Key Visualizer is a tool that helps you analyze your Bigtable usage patterns. It generates visual reports for your tables that break down your usage based on the row keys that you access.

Key Visualizer can provide insights into usage patterns at scale that are difficult to understand otherwise. Uses for Key Visualizer include the following:

  * Iteratively designing a schema or improving the design of an existing schema. In each iteration, you check Key Visualizer to spot problems your schema may be causing, then tweak your schema and check again.
  * Troubleshooting performance issues.
  * Getting a better understanding of how you access the data that you store in Bigtable.



To accomplish these goals, Key Visualizer can help you complete the following tasks:

  * Check whether your reads or writes are creating hotspots on specific rows
  * Find rows that contain too much data
  * Look at whether your access patterns are balanced across all of the rows in a table



Although Key Visualizer shows a variety of metrics, it doesn't display every single metric that can affect the performance of Bigtable. For example, if there are network issues between your application and Google Cloud, those network issues might not be visible, or they might appear as vertical bands across all keys in Key Visualizer, which only gives you hints about _when_ the problems occurred. If you can't identify the cause of a performance issue by looking at your Key Visualizer scans, you'll need to do additional troubleshooting.

## Key Visualizer scans

The following image shows a Key Visualizer scan. Each scan includes a few different types of information:

  * A large heatmap, which shows access patterns for a group of row keys over time.
  * Aggregate values along each axis of the heatmap, including average values and either total or maximum values.



![Example of a Key Visualizer scan](https://docs.cloud.google.com/bigtable/img/keyvis-scan-example.png)

Key Visualizer also provides tools to help you understand the data in each scan. If you haven't used Key Visualizer before, see [Getting Started with Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started) for instructions. If you're a more experienced user, see [Exploring Heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps) for details.

## Heatmaps

The core of a Key Visualizer scan is the heatmap, which shows the value of a metric over time, broken down into contiguous ranges of row keys. The x-axis of the heatmap represents time, and the y-axis represents row keys. If the metric had a low value for a group of row keys at a point in time, the metric is "cold," and it appears in a dark color. A high value is "hot," and it appears in a bright color; the highest values appear in white.

Different types of usage result in different visual patterns within the heatmap, which can make it possible to diagnose issues at a glance. See [Heatmap Patterns](https://docs.cloud.google.com/bigtable/docs/keyvis-patterns) for examples of some common patterns.

By default, a Key Visualizer heatmap shows the **Ops** metric, which represents the combined number of reads and writes. You can switch to the heatmap for a different metric at any time. See [Switching metrics](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps#switching-metrics) for details.

You can also [view more than one metric at a time](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps#finding-connections), which can help you find connections between different metrics.

### Hierarchical row keys

Row keys are often composed of a hierarchy of values, with each value separated by a delimiter. For example, the row key `memusage#1423523569918` contains an identifier for all rows that capture memory usage, followed by a timestamp that identifies a specific set of data within that group. 

Key Visualizer automatically recognizes this type of row key and breaks it down into a hierarchy of tabs, as shown on the left side of the earlier example. This feature helps you understand how your data and access patterns are distributed across the table's rows. It also lets you to drill down into the data for specific ranges of row keys more quickly.

If your row keys are not composed of multiple values, Key Visualizer still displays tabs on the left side of the scan, but the tabs might split up your row keys in unexpected ways rather than presenting a clear hierarchy.

### Key buckets

A Bigtable table can have trillions of rows, so it's not always practical to report metrics for each individual row. Instead, Key Visualizer divides all of the row keys into 1,000 contiguous ranges, with roughly the same number of row keys in each range. These ranges are known as _key buckets_. 

Key Visualizer reports most metrics as averages over each key bucket, or as maximum values within each key bucket. For [**Warnings** metrics](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics#warnings) and [**Performance** metrics](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics#performance), Key Visualizer provides higher precision by reporting metrics for individual row keys or for specific key ranges within the key bucket. 

Behind the scenes, Key Visualizer generates new scan data every 15 minutes. In order to be able to concatenate data in contiguous time periods, Key Visualizer tries to keep the same key buckets as the previous 15-minute period. It is also possible that keys that are deleted still show up as bucket boundaries. Because tables change over time as data is added and removed, key buckets are sometimes recalculated so that they are balanced.

**Note:** If the keys in the table change rapidly, expect to see many bucket boundaries. This effect may go away over time as the key space grows in size.

Key Visualizer also generates a new set of key buckets every two weeks, even if the table has not changed a lot, just to remove any residual bucket boundaries from deleted keys. As a result, even if your table is stable, you will notice that your key buckets are updated occasionally.

## Aggregate values

In addition to the heatmap, a Key Visualizer scan includes aggregate values in bar charts along the bottom and right sides of the heatmap. When you hover over the aggregate values, Key Visualizer highlights a narrow area in the heatmap and shows the following information:

  * For the x-axis, Key Visualizer shows the average value for the current metric, along with either the total or maximum value. These values appear for all of the visible key ranges in 15-minute intervals.
  * For the y-axis, Key Visualizer shows the average value for the current metric across the visible time range, broken down into key ranges.



## Limitations

Key Visualizer has the following limitations:

### Minimum table size for scans

Key Visualizer is available for tables that contain at least 1 GB of data per cluster. It can take up to an hour after a table reaches that size for scans to be available. 

### Time spans

  * **Minimum** : The shortest time span you can view in Key Visualizer is 15 minutes.
  * **Maximum** : The longest time span you can view is 14 days.
  * **Increment size** : Key Visualizer data is available in 15-minute increments.



### Data duration

Key Visualizer data is available for the last 14 days. For example, if you launch Key Visualizer on December 19 at 12:45 PM, the earliest start time you can choose for a time span is December 5 at 12:45 PM.

This limit also means that if you bookmark or share the URL for a Key Visualizer scan, the URL has a maximum life of 14 days.

### Initial data availability

When you create a new table, Key Visualizer data is not immediately available. Background processes must first run to populate the data Key Visualizer requires. This process typically takes a few days but can take up to a week.

## What's next

  * Learn how to [get started with Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-getting-started).
  * Understand the [patterns you might see in Key Visualizer heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-patterns).
  * Find out how to [explore a heatmap in detail](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps).
  * Read about the [metrics you can view in a heatmap](https://docs.cloud.google.com/bigtable/docs/keyvis-metrics).
  * Watch a video about how [Twitter used Key Visualizer](https://youtu.be/3QHGhnHx5HQ) to design its Bigtable schema.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
