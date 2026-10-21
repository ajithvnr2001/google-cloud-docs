---
url: https://docs.cloud.google.com/bigtable/docs/schema-design-steps/
title: Design a schema \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:12.258176+00:00
---

# Design a schema  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/schema-design-steps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Design a schema

The ideal schema for a Bigtable table is highly dependent on a number of factors, including use case, data access patterns, and the data you plan to store. This page provides an overview of the Bigtable schema design process.

Before you read this page, you should understand [schema design](https://docs.cloud.google.com/bigtable/docs/schema-design) concepts and best practices. If applicable, also read [Schema design for time series data](https://docs.cloud.google.com/bigtable/docs/schema-design-time-series).

## Before you begin

**[Create](https://docs.cloud.google.com/bigtable/docs/creating-instance) or identify a Bigtable instance** that you can use to test your schema.

## Gather information

  1. **Identify the data that you plan to store in Bigtable**. Questions to ask include: 
     * What format does the data use? Possible formats include raw bytes, strings, protobufs, and json.
     * What constitutes an _entity_ in your data? For example, are you storing page views, stock prices, ad placements, device measurements, or some other type of entity? What are the entities composed of?
     * Is the data time-based?
  2. **Identify and rank the queries that you use to get the data you need**. Considering the entities you will be storing, think about how you will want the data to be sorted and grouped when you use it. Your schema design might not satisfy all your queries, but ideally it satisfies the most important or most frequently used queries. Examples of queries might include the following: 
     * A month's worth of temperature readings for IoT objects.
     * Daily ad views for an IP address.
     * The most recent location of a mobile device.
     * All application events per day per user.



## Design

**Decide on an initial schema design**. This means planning the pattern that your row keys will follow, the column families your table will have, and the column qualifiers for the columns you want within those column families. Follow the general [schema design guidelines](https://docs.cloud.google.com/bigtable/docs/schema-design). If your data is time-based, also follow the [guidelines for time series data](https://docs.cloud.google.com/bigtable/docs/schema-design-time-series).

If you plan to query your table using SQL instead of the Bigtable Data API `ReadRows` method, consult the following documents:

  * [GoogleSQL for Bigtable overview](https://docs.cloud.google.com/bigtable/docs/googlesql-overview)
  * [Manage row key schemas](https://docs.cloud.google.com/bigtable/docs/manage-row-key-schemas)



If you want to use SQL to query views of your table as well as the table itself, review [Tables and views](https://docs.cloud.google.com/bigtable/docs/tables-and-views).

## Test

  1. **Create a table** using the column families and column qualifiers that you came up with for your schema.
  2. **[Load the table](https://github.com/GoogleCloudPlatform/PerfKitBenchmarker/tree/master/tutorials/bigtable_walkthrough) with at least 30 GB of test data**, using row keys that you identified in your draft plan. **Stay below the[storage utilization per node](https://docs.cloud.google.com/bigtable/quotas#storage-per-node) limits.**
  3. **Run a heavy load test for several minutes.** This step gives Bigtable a chance to balance data across nodes based on the access patterns that it observes.
  4. **Run a one-hour simulation** of the reads and writes you would normally send to the table.
  5. **Review the results of your simulation using Key Visualizer and Cloud Monitoring**.

     * The [Key Visualizer tool for Bigtable](https://docs.cloud.google.com/bigtable/docs/keyvis-overview) provides scans that show the usage patterns for each table in a cluster. Key Visualizer helps you check whether your schema design and usage patterns are causing undesirable results, such as hotspots on specific rows.

     * [Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance) helps you check metrics, such as CPU utilization of the hottest node in a cluster, to help you determine if the schema design is causing problems.




## Refine

  1. **Revise your schema design** as necessary, based on what you learned with Key Visualizer. For instance: 
     * If you see evidence of hotspotting, use different row keys.
     * If you notice latency, find out whether your rows exceed the 100 MB per row limit.
     * If you find that you have to use filters to get the data you need, consider normalizing the data in a way that allows simpler (and faster) reads: reading a single row or ranges of rows by row key.
  2. **After you've revised your schema, test and review the results again**.
  3. **Continue modifying your schema design and testing** until an inspection in Key Visualizer tells you that the schema design is optimal.



## What's next

  * Watch a presentation on the [iterative design process](https://docs.cloud.google.com/bigtable/docs/media#visualizing-cloud-bigtable-access-patterns-at-twitter-for-optimizing-analytics-google-cloud-next-18) that Twitter used for Bigtable.
  * Learn more about [Bigtable performance](https://docs.cloud.google.com/bigtable/docs/performance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
