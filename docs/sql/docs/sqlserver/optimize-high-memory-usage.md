---
url: https://docs.cloud.google.com/sql/docs/sqlserver/optimize-high-memory-usage/
title: Optimize high memory usage in instances \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:18.038565+00:00
---

# Optimize high memory usage in instances  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/optimize-high-memory-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Optimize high memory usage in instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/optimize-high-memory-usage "View this page for the PostgreSQL database engine") | SQL Server

This document explains how to review and optimize a Cloud SQL for SQL Server instance if that instance is identified by the underprovisioned instance recommender as having high memory consumption.

## SQL Server memory

SQL Server memory can be divided into the following:

  * [Caches](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-high-memory-usage#cache)
  * [Fixed memory](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-high-memory-usage#fixed-memory)
  * [SQL Server overhead](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-high-memory-usage#sql-server-overhead)
  * [In-Memory online transactional processing (OLTP)](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-high-memory-usage#oltp)



### Caches

These are objects on a disk that can be reloaded, such as database pages and stored procedures. As a result, the SQL Server can grow and shrink these objects based on memory utilization. Caches include buffer pools and plan caches.

### Fixed memory

Fixed memory can grow and shrink. It only shrinks when not in use; for example, when the number of connections drops or the number of queries executing decreases. It's different from caches. If there is not enough fixed memory, SQL Server can run out of memory. Fixed memory includes connection memory and memory grants.

### SQL Server overhead

SQL Server overhead includes threads and stacks.

### In-Memory OLTP

In-Memory OLTP includes In-Memory tables and In-Memory filegroups.

The memory consumption by SQL Server is controlled by setting `maximum server memory` and `memory.memory.limitmb`. The `memory.memory.limitmb` parameter is set by Cloud SQL automatically.

To learn more about `memory.memory.limitmb`, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-configure-mssql-conf?view=sql-server-ver16#memorylimit).

## Memory optimization options

To determine if an instance needs more memory tuning, do the following:

  * [Check the value of the `max server memory (mb)`](https://docs.cloud.google.com/sql/docs/sqlserver/flags#special-flags) flag. 

We recommend you let Cloud SQL manage the value of this flag. If you must manually manage this value, use the `max_server_memory (mb)` usage formula outlined on [Best practices](https://docs.cloud.google.com/sql/docs/sqlserver/best-practices#sqlserver_settings) to help prevent SQL Server from consuming all memory.

For more information, see [Special flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags#special-flags).

  * Monitor the `Page life expectancy` flag. 

`Page life expectancy` indicates the amount of time, in seconds, that the oldest page stays in the buffer pool. This value should be more than 300 as recommended by Microsoft. If it consistently falls under 300, it could be an indication that the instance is facing high memory utilization. Run the following query to monitor `Page life expectancy`.
        
        SELECT
              [object_name],
              [counter_name],
              [cntr_value]
            FROM
              sys.dm_os_performance_counters
            WHERE
              [object_name]
            LIKE
              '%Manager%'
            AND
              [counter_name] = 'Page life expectancy'
            

  * Check the `Memory Grants Pending` flag. 

`Memory Grants Pending` specifies the total number of processes waiting for a workspace memory grant. Run the following query to check `Memory Grants Pending`. If this query consistently shows grants pending, then it indicates high memory utilization. You can reduce it by querying the database waits and tuning any statement that's waiting on memory.
        
        SELECT
              @@SERVERNAME AS [Server Name],
              RTRIM([object_name]) AS [Object Name],
              cntr_value AS [Memory Grants Pending]
            FROM
              sys.dm_os_performance_counters WITH(NOLOCK)
            WHERE
              [object_name]
            LIKE
              N'%Memory Manager%'  -- Handles named instances
            AND
              counter_name = N'Memory Grants Pending'
            




## Use Metrics Explorer to identify the memory usage

You can review memory usage of the instance with the [`database/memory/components.usage`](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/metrics) metric in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

**Note:** If you have less than 10% memory in `database/memory/components.cache` and `database/memory/components.free` combined, the risk of an out-of-memory (OOM) event is high. To monitor the memory usage and to prevent OOM events, we recommend that you set up an [alerting policy](https://docs.cloud.google.com/monitoring/alerts) with a metric threshold condition of 90% in `database/memory/components.usage`.

## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
