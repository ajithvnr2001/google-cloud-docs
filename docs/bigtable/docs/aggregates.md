---
url: https://docs.cloud.google.com/bigtable/docs/aggregates/
title: Aggregating values at write time \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:15.695128+00:00
---

# Aggregating values at write time  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/aggregates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Aggregating values at write time

This document provides an overview of the ways that you can aggregate your Bigtable data at write time. Before you read this document, make sure that you're familiar with the [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview).

Many applications track operational metrics that drive use cases including in-app reporting, real-time recommendations, and rate limiting. Examples of such operational metrics include the following:

  * Weekly active users
  * Number of ad impressions
  * Views or shares of social content
  * Number of media streams



You can use these metrics in user-facing applications or as inputs to machine learning models, and their uses typically require low latency and high throughput. Because computing these types of metrics at query time is impractical at scale, pre-aggregation during data ingestion is the preferred approach for real-time systems.

Bigtable offers multiple ways of aggregating data at write time, including conflict-free replicated data types, `ReadModifyWriteRow` requests, and continuous materialized views.

Aggregating your Bigtable data at write time removes the need for extract, transform, and load (ETL) or streaming processing software to aggregate your data before or after you write it to Bigtable. If your application uses Dataflow to aggregate streaming data before writing it to Bigtable, you can send the data directly to aggregate cells in Bigtable.

## Conflict-free replicated data types

Bigtable lets you create column families that contain only cells of type _aggregate_. Aggregate cells are [conflict-free replicated data type](https://en.wikipedia.org/wiki/Conflict-free_replicated_data_type) structures that are optimized for incremental updates.

If you're migrating to Bigtable from databases such as Apache Cassandra, Redis, or Valkey, similar structures in those systems are referred to as _counters_.

The following table lists the supported operations and how newly written values are handled.

  
**Operation** |   
**Description**  
---|---  
  
Sum |   
The cell value is replaced with the sum of the newly added value and the current cell value.  
  
Minimum |   
The cell value is replaced with the lower value between the newly added value and the current cell value.  
  
Maximum |   
The cell value is replaced with the higher value between the newly added value and the current cell value.  
  
HyperLogLog |   
The written value is added to a probabilistic set of all values added since the most recent reset. The cell value represents the state of that set. For more general information about the HLL algorithm, see [HyperLogLog](https://en.wikipedia.org/wiki/HyperLogLog).  
  
You can read HLL values using the [Zetasketch Library](https://github.com/google/zetasketch).   
  
The mutation types that you can send to create and update aggregate cells are [`AddToCell`](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#google.bigtable.v2.Mutation.AddToCell) and [`MergeToCell`](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#mergetocell).

To get started with counting in Bigtable, see the [Create and update counters in Bigtable](https://docs.cloud.google.com/bigtable/docs/create-update-counters) quickstart.

## Read then write

Another way to aggregate your data at write time is by using a [ReadModifyWriteRow](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#readmodifywriterowrequest) request, which lets you manipulate the value of a cell by incrementing or appending to the value transactionally. For more information about when to use this approach, see [Appends](https://docs.cloud.google.com/bigtable/docs/writes#appends).

## Continuous materialized views

A continuous materialized view is a pre-computed result of a SQL query that aggregates data in a source table. The view continuously processes data as it's ingested into the source table and batches the updates. This includes updates and deletes. Using continuous materialized views can increase performance and efficiency. For more information, see [Continuous materialized views](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views).

## What's next

  * [See code samples showing how to add a value to an aggregate cell](https://docs.cloud.google.com/bigtable/docs/writing-data#increments-appends).
  * [Review concepts related to schema design.](https://docs.cloud.google.com/bigtable/docs/schema-design)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
