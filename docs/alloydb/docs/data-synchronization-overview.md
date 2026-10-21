---
url: https://docs.cloud.google.com/alloydb/docs/data-synchronization-overview/
title: Data synchronization overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:26.280266+00:00
---

# Data synchronization overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/data-synchronization-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Data synchronization overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Data synchronization lets you create a managed, writable copy of your BigQuery analytical data directly in your AlloyDB for PostgreSQL cluster. This feature automatically and periodically refreshes the data from your data warehouse into your operational database on a schedule that you define.

By syncing tables directly into AlloyDB, you eliminate the need to build, manage, and maintain complex custom data pipelines to transfer analytical data from BigQuery to your operational database.

## How data synchronization works

Data synchronization uses the `alloydb_sync` extension to automate data replication. When you create a synced table, AlloyDB sets up a local read-only table and schedules background workers to periodically pull updated data from the source in BigQuery.

Your client applications query the local synced table directly in AlloyDB, benefiting from low query latency, the AlloyDB columnar engine, and horizontal scale-out across read pools without sending queries across the network to BigQuery.

## Use cases

Sync tables when you need to serve analytical data from BigQuery to applications that require the high throughput, low latency, and interactive performance of an operational database.

Common use cases include the following:

  * High-concurrency application serving: serve analytical insights to thousands of concurrent users. By syncing data to AlloyDB and scaling out with read pools, you bypass the concurrent query and connection limits of BigQuery.
  * Performance acceleration: process data using the AlloyDB columnar engine and local buffer cache for sub-second query response times.
  * Automated data mirroring: maintain an automated, scheduled refresh of analytical data from BigQuery without manually orchestrating batch ETL jobs.
  * Enabling AI and operational workflows: materialize analytical data into AlloyDB to generate vector embeddings, run similarity searches, and power agentic workflows using AlloyDB AI.



## Architecture and data flow

The `alloydb_sync` extension uses background workers to periodically stream data from BigQuery into a local table in your AlloyDB cluster according to your configured schedule. Applications then query the local table with low latency.

The following diagram illustrates the data synchronization architecture.

![A flowchart diagram showing how data moves from BigQuery to AlloyDB via scheduled sync jobs.](https://docs.cloud.google.com/static/alloydb/images/synced-tables-architecture.png)**Figure 1.** Architecture and data flow for synced tables 

## Data type mapping

When you sync data from BigQuery to AlloyDB, AlloyDB maps BigQuery data types to corresponding PostgreSQL data types.

Before you create a synced table, verify that your source BigQuery columns use supported data types. For a full list of mappings and supported types, see [Supported data type mappings](https://docs.cloud.google.com/alloydb/docs/sync-bigquery-data-to-alloydb#data-type-mappings).

## Pricing

When you use data synchronization, Google Cloud bills you based on the following components. For more information, see [Sync BigQuery data to AlloyDB](https://docs.cloud.google.com/alloydb/docs/sync-bigquery-data-to-alloydb#pricing).

  * AlloyDB: standard pricing applies for your AlloyDB instances and the storage used by the local synced tables.
  * BigQuery: queries and data streams executed during `alloydb_sync` refresh jobs incur standard BigQuery analysis and BigQuery Storage API charges.
  * Cloud Storage: when you sync data from Apache Iceberg tables in Cloud Storage, standard storage and data retrieval rates apply.



## Limitations

Data synchronization has the following limitations:

  * **Data freshness:** data in synced tables reflects the state of the source BigQuery table since the last completed refresh.
  * **PostgreSQL version:** data synchronization using the `alloydb_sync` extension is supported for PostgreSQL version 18 only.
  * **Data type compatibility:** source columns must map to supported PostgreSQL data types. Unsupported complex types (such as `ARRAY`, `BYTES`, `VECTOR`, and `GEOGRAPHY`) require you to convert or cast the column in a BigQuery view before syncing.



## What's next

  * [Sync BigQuery data using `alloydb_sync`](https://docs.cloud.google.com/alloydb/docs/sync-bigquery-data-to-alloydb).
  * [Discover AlloyDB AI features](https://docs.cloud.google.com/alloydb/docs/ai/what-is-alloydb-ai).
  * [Choose how to access BigQuery data](https://docs.cloud.google.com/alloydb/docs/choose-access-bigquery-data-from-alloydb).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
