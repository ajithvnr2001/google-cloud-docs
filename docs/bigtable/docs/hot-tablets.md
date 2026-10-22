---
url: https://docs.cloud.google.com/bigtable/docs/hot-tablets/
title: Hot tablets \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:30.069651+00:00
---

# Hot tablets  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/hot-tablets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Hot tablets

To help you troubleshoot performance issues, Bigtable provides the ability to identify and observe hot tablets in a cluster. This page describes hot tablets, tells you how to get a list of hot tablets, and discusses situations when identifying hot tablets is helpful. Before you read this page, you should read the [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview#load-balancing).

The name of the method that you use to get a list of hot tablets varies depending on the language used. For simplicity, in this document the method is referred to by its RPC Cloud Bigtable Admin API name, `ListHotTablets`. You are able to get a list of hot tablets by using the following:

  * [The Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list)
  * [The Cloud Bigtable Admin API](https://docs.cloud.google.com/bigtable/docs/reference/admin/rpc)
  * [The Cloud Bigtable client libraries](https://docs.cloud.google.com/bigtable/docs/reference/libraries)



Identifying hot tablets can help you with the following tasks:

  * Identifying problematic row keys
  * Observing hotspots with minute-level granularity
  * Identifying problematic tables within a cluster



## Understand hot tablets

A Bigtable table is sharded into blocks of contiguous rows, called _tablets_ , to help balance the workload of queries. Each tablet is associated with a node, and operations on these rows are performed on the node. To optimize performance, tablets are split or moved to a different node depending on access patterns. Based on user access patterns — read, write, and scan operations — tablets are rebalanced across the nodes. For details on load balancing, see [How Bigtable optimizes your data over time](https://docs.cloud.google.com/bigtable/docs/performance#optimization).

A _hot tablet_ is a tablet that exhibits overutilization of the node CPU because the tablet uses a disproportionately large percentage of CPU compared to other tablets. This imbalanced node usage can cause latency and replication delays.

Among the most frequent causes of hot tablets are hotspots, which occur when your application frequently accesses rows that are near each other in the table. Hotspots are often the result of a schema design that is not optimized to spread your application's access patterns across the table. To learn how to design your row keys so that hotspots don't occur, see [Schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design).

To get a list of hot tablets, you must be assigned to a role that has the `bigtable.viewer` permission.

## Output

The `ListHotTablets` method returns the following data for a given cluster in an instance.

  * **Tablet name.** The unique ID assigned by Bigtable to the hot tablet. This field is not displayed by the gcloud CLI.
  * **Table.** The ID of the table associated with the hot tablet.
  * **CPU usage.** The average CPU utilization of the node associated with the hot tablet, expressed as a percentage, during that one-minute interval. This percentage is the average of the sum of Write CPU and Read CPU from start time to end time.
  * **Start time.** The start time of the hot tablet period.
  * **End time.** The end time of the hot tablet period.
  * **Start key.** The first row key in the hot tablet.
  * **End key.** The last row key in the hot tablet. A suffix of `\000` is appended when the start and end key are the same, indicating that the tablet spans a single row.



Keys are lexicographically sorted within a tablet, so any key between the start key and end key is contained in that hot tablet.

Hotspots are calculated on a one-minute resolution, and a tablet might reappear in the output. In other words, a single tablet might be considered hot for multiple minutes.

By default, `ListHotTablets` searches the past 24 hours. To search within a specific time range, provide a start time and end time.

The maximum number of hot tablets returned is 50. To change this, provide a page size.

The method returns an empty list if none of the tablets in the cluster are hot.

## Example using the gcloud CLI

Before you copy this example, [install the `gcloud` CLI](https://docs.cloud.google.com/bigtable/docs/installing-cloud-sdk).

To view a list of hot tablets for a given cluster, run the [`hot-tablets list`](https://docs.cloud.google.com/sdk/gcloud/reference/bigtable/hot-tablets/list) command in the Cloud Shell or your local terminal window.
    
    
      gcloud bigtable hot-tablets list CLUSTER_ID --instance INSTANCE_ID
    

Replace the following:

  * `CLUSTER_ID`: the permanent identifier for the cluster
  * `INSTANCE_ID`: the permanent identifier for the instance



If any tablets in the cluster are hot, the terminal displays output similar to the following. Hot tablets in a cluster are listed in descending order of CPU usage.
    
    
    TABLE      CPU_USAGE  START_TIME                 END_TIME                   START_KEY            END_KEY
    test-data  89.3       2021-12-14T01:19:57+00:00  2021-12-14T01:20:57+00:00  user29333893046…    user29333893046…
    test-data  22.8       2021-12-14T01:04:59+00:00  2021-12-14T01:06:59+00:00  user29333893046…    user29345657428…
    test-data  20.9       2021-12-14T01:18:56+00:00  2021-12-14T01:20:56+00:00  user54519105346…    user545293
    test-data  16.5       2021-12-14T01:18:56+00:00  2021-12-14T01:20:56+00:00  user49196524328…    user49206

## Use cases for hot tablets data

Identifying hot tablets in a cluster can help you troubleshoot performance issues. You can use the `ListHotTablets` method in combination with other monitoring tools, such as the [Key Visualizer](https://docs.cloud.google.com/bigtable/docs/keyvis-overview) diagnostic tool for Bigtable.

### Identifying problematic row keys

You can use `ListHotTablets` to identify specific row keys and row ranges. This can provide observability into access patterns that might be causing hotspots.

For example, suppose that a table's row key schema is `[user_id]#[event_timestamp]`, user IDs and timestamps separated by a hash symbol. Getting a list of hot tablets can help you determine if specific user IDs or event timestamps are causing hotspots. Identifying the access patterns lets you take further action, such as redesigning row keys or tables to spread usage more evenly across the key space. In this example, if user IDs are monotonically increasing and causing hotspots for that reason, you might assign user IDs in a different order or use universally unique identifiers (UUID) instead.

When the start and end row key are the same, and the end row key is appended with a `\000` suffix, it creates a single row tablet. When this tablet receives a disproportionately large amount of traffic, it leads to hotspots.

**Note:** Hot tablets output is available for tables that contain at least 1 GB of data per cluster. It can take up to an hour after a table reaches that size for lists of hot tablets to be available.

### Observing hotspots with minute-level granularity

You can use a list of hot tablets in combination with Key Visualizer's [heatmaps](https://docs.cloud.google.com/bigtable/docs/keyvis-exploring-heatmaps). While Key Visualizer is a good tool to observe the larger picture of key-space access patterns, `ListHotTablets` provides greater granularity.

After inspecting heatmaps in Key Visualizer, you can further explore specific hotspots. Because Key Visualizer runs over a period of weeks, its data for hotspots is aggregated in 15-minute intervals. Additionally, multiple tablets might be combined in the same Key Visualizer key space.

After you've used Key Visualizer to identify the time range that the hotspots occurred, you can run `ListHotTablets` for greater granularity in both key and time space. Greater granularity is particularly useful for [periodic usage](https://docs.cloud.google.com/bigtable/docs/keyvis-patterns). `ListHotTablets` can identify short-lived hotspots that KeyVisualizer cannot.

### Identifying problematic tables within a cluster

Because Key Visualizer operates at the table level, it's not always the best choice for troubleshooting an issue in a cluster that has multiple tables. `ListHotTablets` operates at the cluster level, so you can use it to identify tables with high CPU usage and narrow down the problem.

## What's next

  * [Understand Bigtable performance.](https://docs.cloud.google.com/bigtable/docs/performance)
  * [Learn more about Bigtable monitoring.](https://docs.cloud.google.com/bigtable/docs/monitoring-instance)
  * [Work through a tutorial on performance benchmarking.](https://github.com/GoogleCloudPlatform/PerfKitBenchmarker/tree/master/tutorials/bigtable_walkthrough)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
