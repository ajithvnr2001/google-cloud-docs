---
url: https://docs.cloud.google.com/alloydb/docs/columnar-engine/about/
title: About the AlloyDB columnar engine \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T06:00:16.232642+00:00
---

# About the AlloyDB columnar engine  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/columnar-engine/about/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  About the AlloyDB columnar engine Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the columnar engine that AlloyDB for PostgreSQL offers and shows how to use it.

The AlloyDB columnar engine accelerates SQL query processing of scans, joins, and aggregates by providing these components:

  * A column store that contains table and materialized-view data for selected columns, reorganized into a column-oriented format. You can also add [frequently used expressions](https://docs.cloud.google.com/alloydb/docs/columnar-engine/add-frequent-expressions) to the column store.

  * A columnar query planner and execution engine to support use of the column store in queries.




The columnar engine can be used on the primary instance, a read pool instance, or both. When the columnar engine is enabled on a read pool instance, you can optionally enable [transparent query forwarding](https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding) to automatically route read-only traffic to it.

You can also use [auto-columnarization](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-recommendations#default-schedule) to analyze your workload and automatically populate the column store with the columns that provide the best performance gain.

To use the columnar engine with a specific query, all columns in that query fragments, such as joins and scans, must be in the column store.

By default, the columnar engine is set to use 30% of your instance's memory (or 10% on a 1-vCPU instance). Depending on your workload, memory usage, and if you have a read pool configured, you may choose to reduce the columnar engine memory allocation on your primary instance and allocate more memory to the read pool instance. To view and monitor memory usage by the columnar engine, see [View column store memory usage](https://docs.cloud.google.com/alloydb/docs/columnar-engine/monitor-tune#usage). To modify the memory size used by the column store, see [Configure the size of the column store](https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure#configure). To find the recommended columnar engine memory size for your instance, see [Recommend column store memory size](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-recommendations#recommend-populate).

## Query types that benefit from the columnar engine

Certain queries can benefit from the columnar engine. The following is a list of operations and their query patterns that benefit most from the columnar engine:

  * **Table scans**

    * It has selective filters, such as `WHERE` clauses.
    * It uses a small number of columns from a larger table or materialized view.
    * It uses expressions such as `LIKE`, `ILIKE`, `SUBSTR`, and `TRIM`.
  * **Aggregation functions**

    * They only use the following expressions: `SUM`, `MIN`, `MAX`, `AVG`, and `COUNT`.
    * They are at the beginning of the query of a columnar scan.
    * They are ungrouped, or are grouped-by columns.
  * **`ORDER-BY`** and **`SORT`** : only when the `ORDER-BY` or `SORT` is on the scan results of columns accessed from the columnar engine.

  * **`LIMIT`** : only if the operator is at the beginning of the query of a columnar scan and is before any `SORT` or `GROUP BY` operators.

  * **`INNER HASH JOIN`** only if the keys used are columns and no join qualifiers are used.

  * **Selective joins** only if the joins are at the beginning of the query of a columnar scan.

  * **Filter queries** with JSON expressions.




For more information on which queries work best with the columnar engine, whether the columnar engine was used by a query, and how it was used, see [Verify usage of the columnar engine using `EXPLAIN`](https://docs.cloud.google.com/alloydb/docs/columnar-engine/monitor-tune#explain).

## How to use the columnar engine

To use the columnar engine in an AlloyDB instance, you perform these high-level steps:

  1. [Enable the engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure#enable) on the instance.

Enabling the engine is a one-time operation and requires a restart.

  2. Add columns to the column store.

To add columns to the column store, use one of the following methods:

     * [Use auto-columnarization](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-recommendations), which analyzes your workload and automatically adds columns.

     * [Add the columns manually](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-manually) or [add frequently used expressions to the column store](https://docs.cloud.google.com/alloydb/docs/columnar-engine/add-frequent-expressions) ([Preview](https://cloud.google.com/products#product-launch-stages)) based on your knowledge of the workload on the databases in the instance.

  3. You can track what's in the column store using [the `g_columnar_relations` view](https://docs.cloud.google.com/alloydb/docs/columnar-engine/monitor-tune#relations-view), and, after columns have been added, you can use [the `EXPLAIN` statement](https://docs.cloud.google.com/alloydb/docs/columnar-engine/monitor-tune#explain) to verify usage of the columnar engine in SQL queries.




For detailed instructions on how to use the columnar engine, see [Configure the columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure).

## What data you can add to the column store

There are some limitations on the data types and data sources you can use when adding columns to the column store.

### Supported data types

The columnar engine can populate and refresh supported columns in a table even if some columns have unsupported data types. Columns with unsupported data types are skipped during the population process.

When executing a query, the columnar engine processes a table if all the specific columns referenced in that part of the query have supported data types and are present in the columnar engine.

In queries involving multiple tables, such as `JOIN` operations, you can use the columnar engine for any table on an individual basis. As long as all the columns accessed from the specific table in the query have supported data types and are in the columnar engine, that table can be processed by the columnar engine, even if other tables in the join have unsupported columns.

The columnar engine supports only columns with the following built-in data types:

  * `array`
  * `bigint`
  * `boolean`
  * `bytea`
  * `char`
  * `date`
  * `decimal`
  * `double precision`
  * `enum`
  * `float4`
  * `float8`
  * `integer`
  * `json`
  * `jsonb`
  * `numeric`
  * `real`
  * `serial`
  * `short`
  * `smallint`
  * `text`
  * `timestamp`
  * `timestamptz`
  * `uuid`
  * `varchar`
  * `vector`



The columnar engine ignores any attempts to manually add columns with unsupported data types to the column store.

### Unsupported data sources

The columnar engine does not support tables or materialized views with the following attributes as data sources:

  * Non-leaf partitioned tables

  * Foreign tables




## Columnar engine limitations

  * If you're running an analytical query on a column that has an index, the AlloyDB optimizer may choose to use row-store.
  * Columns added manually to the column store aren't automatically removed. To force remove manually added columns, use [`google_columnar_engine_drop()`](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-manually#drop-by-function) on your instance.
  * Auto-columnarization may dynamically add and remove columns based on query usage.
  * Not all data types are supported by the columnar engine. To see supported data types, see supported data types.
  * Frequent updates to rows invalidate columnar data. To validate a table or a materialized view in the columnar store, you can either reduce the update frequency, or [schedule the columnar engine refreshes more frequently](https://docs.cloud.google.com/alloydb/docs/columnar-engine/manage-content-recommendations#auto-schedule).

You can compare the `invalid_block_count` and `total_block_count` columns in [g_columnar_relations](https://docs.cloud.google.com/alloydb/docs/columnar-engine/monitor-tune#relations-view) to check if your table or view is impacted. If you have a frequent or high-volume changes to your table or view, the `invalid_block_count` will be high.

  * A partitioned table can't be directly populated into the columnar engine. To use the columnar engine, you must individually populate each of the table's leaf partitions.

  * For tables or views with a small number of rows, typically fewer than 5,000, the query planner might choose to use the row-store instead of the column store for better performance, even if the data is successfully loaded into the columnar engine.




## What's next

  * [Configure the columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/configure).

  * [Configure the columnar engine on AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/columnar-engine/configure).

  * Learn how to [accelerate analytical queries using the AlloyDB columnar engine](https://www.cloudskillsboost.google/paths/22/course_templates/642/labs/501234).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
