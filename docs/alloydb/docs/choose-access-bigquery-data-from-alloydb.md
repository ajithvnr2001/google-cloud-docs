---
url: https://docs.cloud.google.com/alloydb/docs/choose-access-bigquery-data-from-alloydb/
title: Choose how to access BigQuery data from AlloyDB \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:52.413850+00:00
---

# Choose how to access BigQuery data from AlloyDB  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/choose-access-bigquery-data-from-alloydb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Choose how to access BigQuery data from AlloyDB Stay organized with collections  Save and categorize content based on your preferences. 

To access BigQuery data from AlloyDB for PostgreSQL, you can use the `bigquery_fdw` (foreign data wrapper) and `alloydb_sync` extensions. Together, these extensions provide methods for integrating your analytical and operational data: real-time data access (lakehouse federation), one-time data operations, and periodic synchronization. This document describes the options to access BigQuery data from AlloyDB.

## Lakehouse federation

Lakehouse federation provides real-time access to your BigQuery data directly from AlloyDB for PostgreSQL without moving or duplicating the data. To bridge the two systems, this method uses the `bigquery_fdw` extension, which lets you query live datasets in place. Because you query the source data directly, you gain insights from the most current data available, bypassing the latency and maintenance overhead of data pipelines or synchronization intervals.

To optimize performance, AlloyDB pushes standard filters, limits, and aggregations down to BigQuery, streaming only the relevant, pre-filtered results back to your instance. For more information, see [AlloyDB access to real-time data in BigQuery overview](https://docs.cloud.google.com/alloydb/docs/access-real-time-data-overview).

### Use cases

Lakehouse federation supports the following use cases:

  * Real-time operational analytics: you need access to the freshest analytical data available in BigQuery to make instant business decisions, without waiting for batch processing.
  * Hybrid transactional analytical processing (HTAP): you need to run analytics that join live, "hot" operational data residing in AlloyDB with massive volumes of historical, "cold" data stored in BigQuery.
  * Ad hoc and exploratory data analysis: you want to run immediate queries on BigQuery data without building, maintaining, or waiting for complex extract, transform, and load (ETL) pipelines.
  * Zero-copy architecture: you want to minimize storage costs and data governance overhead by keeping your analytical data in one place while maintaining access through PostgreSQL semantics.



## One-time table synchronization

A one-time operation moves or accesses data from BigQuery once, rather than on an ongoing schedule. You can perform a one-time operation using sync tables or by importing foreign tables.

### Sync tables

You can perform a one-time sync using the `alloydb_sync.import_bq_table()` function in the `alloydb_sync` extension. This function streams data from BigQuery into local AlloyDB storage.

The result is a fully independent, writable PostgreSQL table in your AlloyDB cluster. Because the synced table is writable, you can freely execute `INSERT`, `UPDATE`, and `DELETE` operations on the local data. For more information, see [Sync BigQuery data to AlloyDB](https://docs.cloud.google.com/alloydb/docs/sync-bigquery-data-to-alloydb#one-time-using-psql).

### Import tables

You can perform a one-time import using the `bigquery_fdw` extension. This method uses `IMPORT FOREIGN SCHEMA` or `CREATE FOREIGN TABLE` to map the BigQuery dataset into AlloyDB.

Foreign tables created with `bigquery_fdw` are read-only references to the remote BigQuery data. To create a local copy of the data, you can run a `CREATE TABLE local_table AS (SELECT * FROM foreign_table)` query. For more information, see [Import BigQuery data to AlloyDB](https://docs.cloud.google.com/alloydb/docs/import-bigquery-data#import-data).

### Use cases

One-time data operations support the following use cases:

  * Data enrichment: pull pre-computed analytical outputs (such as customer segmentation buckets or machine learning predictions) from BigQuery into AlloyDB to enrich your operational database.
  * Low-latency application serving: provide immediate access to a subset of historical data where the overhead or latency of querying BigQuery remotely is unacceptable.
  * Isolated data modification: obtain a local copy of analytical data to process, modify, or index independently of the source dataset (for example, generating vector embeddings with AlloyDB AI).



## Periodic table synchronization

Periodic operations refresh data on a recurring schedule—for example, hourly or daily. You can set up periodic operations using sync tables or by scheduling queries on imported tables.

### Sync tables

You can establish an automated refresh schedule using the `alloydb_sync.create_bq_sync_table()` function in the `alloydb_sync` extension. This function configures background workers to periodically pull updated data from BigQuery and refresh your local AlloyDB table to mirror the source.

Periodic sync tables created with `alloydb_sync` are managed, read-only tables. This ensures data integrity while allowing applications to query the data locally with high performance and scale horizontally across read pools. For more information, see [Sync BigQuery data to AlloyDB](https://docs.cloud.google.com/alloydb/docs/sync-bigquery-data-to-alloydb#periodic-sync) and [Data synchronization overview](https://docs.cloud.google.com/alloydb/docs/data-synchronization-overview).

### Import tables

You can set up periodic imports by combining the `bigquery_fdw` extension with the PostgreSQL `pg_cron` extension. In this approach, `bigquery_fdw` provides the read-only foreign table definition, and `pg_cron` periodically executes SQL queries (such as `TRUNCATE` and `INSERT INTO ... SELECT` or recreating the table) to refresh a local table.

Unlike sync tables, this approach requires you to manually manage and maintain the `pg_cron` schedules and SQL refresh scripts. For more information, see [Set up a schedule to periodically import data](https://docs.cloud.google.com/alloydb/docs/import-bigquery-data#set-up-schedule).

### Use cases

Periodic operations support the following use cases:

  * High-concurrency serving: serve analytical insights to thousands of concurrent users. By maintaining local data in AlloyDB and scaling out with read pools, you can bypass the concurrent connection limits inherent in BigQuery.
  * Performance acceleration: process data using the AlloyDB columnar engine and local buffer cache for maximum query performance, where your application can tolerate data updated on a schedule.
  * Automated data mirroring: keep your operational applications supplied with fresh data from your data warehouse on a set-it-and-forget-it schedule.



## What's next

  * Learn more about [querying live data in BigQuery from AlloyDB](https://docs.cloud.google.com/alloydb/docs/access-real-time-data-overview).
  * [Configure access to real-time data](https://docs.cloud.google.com/alloydb/docs/configure-access-real-time-data).
  * [Data synchronization overview](https://docs.cloud.google.com/alloydb/docs/data-synchronization-overview).
  * [Sync BigQuery data to AlloyDB](https://docs.cloud.google.com/alloydb/docs/sync-bigquery-data-to-alloydb).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
