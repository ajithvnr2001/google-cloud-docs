---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/overview/
title: Columnar engine overview \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:54:49.054553+00:00
---

# Columnar engine overview  |  AlloyDB Omni using the RPM orchestrator: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/overview/

This page documents AlloyDB Omni version **18.4.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/overview)



Send feedback 

#  Columnar engine overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/columnar-engine/overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/columnar-engine/overview)

This document provides instructions for using the AlloyDB Omni columnar engine and assumes that you're familiar with PostgreSQL. 

The AlloyDB Omni columnar engine accelerates SQL query processing of scans, joins, and aggregates by providing the following components:

  * A column store that contains table and materialized-view data for selected columns, reorganized into a column-oriented format.

  * A columnar query planner and execution engine that supports use of the column store in queries.




You can use the columnar engine on the primary instance, a read pool instance or read replica, or both. You can also use [auto-columnarization](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/manage-content-recommendations#default-schedule) to analyze your workload and automatically populate the column store with the columns that provide the best performance gain.

To use the columnar engine with a specific query, all columns referenced in the query, such as in joins and scans, must be in the column store.

By default, the columnar engine is set to use 1 GB of your instance's memory. Depending on your workload, memory usage, and if you have a read pool instance or read replica configured, you can choose to reduce the columnar engine memory allocation on your primary instance and allocate more memory to the read pool instance or read replica.

To view and monitor memory usage by the columnar engine, see [View column store memory usage](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/monitor#usage). To modify the memory size used by the column store, see [Configure the size of the column store](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/configure#configure). To find the recommended columnar engine memory size for your instance, see [Recommend column store memory size](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/manage-content-recommendations#recommend-populate).

## Query types that benefit from the columnar engine

Certain queries can benefit from the columnar engine. The following is a list of operations and their query patterns that benefit most from the columnar engine:

Operation | Query patterns  
---|---  
Table scan | Selective filters, such as `WHERE` clauses.  
A small number of columns from a larger table or materialized view.   
Expressions such as `LIKE`, `SUBSTR`, or `TRIM`.  
Aggregation functions | Only expressions such as `SUM`, `MIN`, `MAX`, `AVG`, and `COUNT`.  
At the beginning of the query of a columnar scan.  
Ungrouped or grouped by columns.  
`ORDER BY` | Only if the operator is at the beginning of the query of a columnar scan.  
`SORT` | Only if the operator is at the beginning of the query of a columnar scan and sorts only on the base columns of the table or the materialized view.  
`LIMIT` | Only if the operator is at the beginning of the query of a columnar scan and is before any `SORT` or `GROUP BY` operators.  
`INNER HASH JOIN` | Only if the keys used are columns and no join qualifiers are used.  
Selective joins | Only if the joins are at the beginning of the query of a columnar scan.  
  
For more information on which queries work best with the columnar engine, whether the columnar engine was used by a query, and how it was used, see [Verify usage of the columnar engine using `EXPLAIN`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/monitor#explain).

## How to use the columnar engine in an AlloyDB Omni instance

To use the columnar engine in an AlloyDB Omni instance, you perform these high-level steps:

  1. [Enable the engine](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/configure#enable) on the instance.

Enabling the engine is a one-time operation and requires a database restart.

  2. Add columns to the column store.

To add columns to the column store, use one of the following methods:

     * [Use auto-columnarization](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/manage-content-recommendations), which analyzes your workload and automatically adds columns.

     * [Add the columns manually](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/manage-content-manually) based on your knowledge of the workload on the databases in the instance.

  3. You can track what's in the column store using [the `g_columnar_relations` view](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/monitor#relations-view), and, after columns have been added, you can use [the `EXPLAIN` statement](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/monitor#explain) to verify usage of the columnar engine in SQL queries.




For detailed instructions on how to use the columnar engine, see [Configure the columnar engine](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/configure).

## What data you can add to the column store

There are some limitations on the data types and data sources you can use when adding columns to the column store.

### Supported data types

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
  * `uuid`
  * `varchar`



The columnar engine ignores any attempts to manually add columns with unsupported data types to the column store.

### Unsupported data sources

The columnar engine doesn't support tables or materialized views with the following attributes as data sources:

  * Non-leaf partitioned tables

  * Foreign tables

  * Tables or views with fewer than 5,000 rows




## Columnar engine limitations

  * If you're running an analytical query on a column that has an index, the AlloyDB Omni optimizer might choose to use row-store.
  * Columns added manually to the column store aren't automatically removed. To force remove manually added columns, use [`google_columnar_engine_drop`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/manage-content-manually#drop-by-function) on your instance.
  * Auto-columnarization might dynamically add and remove columns based on query usage.
  * Not all data types are supported by the columnar engine. To see supported data types, see supported data types.
  * Frequent updates to rows invalidate columnar data. To validate a table or a materialized view in the columnar store, you can either reduce the update frequency, or [schedule the columnar engine refreshes more frequently](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/manage-content-recommendations#auto-schedule).

You can compare the `invalid_block_count` and `total_block_count` columns in [`g_columnar_relations`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/monitor#relations-view) to check if your table or view is impacted. If you have frequent or high-volume changes to your table or view, the `invalid_block_count` is high.




## What's next

  * [Configure the columnar engine on AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/columnar-engine/configure)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
