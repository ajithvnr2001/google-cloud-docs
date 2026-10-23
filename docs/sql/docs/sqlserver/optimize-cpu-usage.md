---
url: https://docs.cloud.google.com/sql/docs/sqlserver/optimize-cpu-usage/
title: Optimize high CPU usage in instances \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:05.898450+00:00
---

# Optimize high CPU usage in instances  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/optimize-cpu-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Optimize high CPU usage in instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/optimize-cpu-usage "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/optimize-cpu-usage "View this page for the PostgreSQL database engine") | SQL Server

This document explains how to review and optimize a Cloud SQL for SQL Server instance if that instance is identified by the underprovisioned instance recommender as having high CPU usage.

If an instance vCPU is not sized properly, it can become a source of contention. To check if the CPU is a bottleneck or underprovisioned, use the queries in this document.

## Use query insights to identify queries that have high CPU consumption

[Query insights](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights) helps you detect, diagnose, and prevent query performance problems for Cloud SQL databases.

## Check the average task count

Execute this query a couple times to check the average task count. If the average task count is consistently high, then the instance might be facing CPU pressure.
    
    
    SELECT AVG(current_tasks_count) AS [Avg Task Count],
    AVG(work_queue_count) AS [Avg Work Queue Count],
    AVG(runnable_tasks_count) AS [Avg Runnable Task Count],
    AVG(pending_disk_io_count) AS [Avg Pending DiskIO Count],
    GETDATE() AS [System Time]
    FROM sys.dm_os_schedulers WITH (NOLOCK)
    WHERE scheduler_id < 255 OPTION (RECOMPILE);
    

## Determine if there is a need to add more vCPUs

Under certain conditions, you might want to increase the vCPU. Use this query to determine if there is a need to add more vCPUs.
    
    
    -- Shows queries where max and average CPU time exceeds 200 ms and executed more than 1000 times
    DECLARE @cputime_threshold_microsec INT = 200*1000
    DECLARE @execution_count INT = 1000
    SELECT qs.total_worker_time/1000 total_cpu_time_ms,
          qs.max_worker_time/1000 max_cpu_time_ms,
          (qs.total_worker_time/1000)/execution_count average_cpu_time_ms,
          qs.execution_count,
          q.[text]
    FROM sys.dm_exec_query_stats qs CROSS APPLY sys.dm_exec_sql_text(plan_handle)
    AS q
    WHERE (qs.total_worker_time/execution_count > @cputime_threshold_microsec
           OR qs.max_worker_time > @cputime_threshold_microsec )
           AND execution_count > @execution_count
           ORDER BY qs.total_worker_time DESC
    

## Check for missing indexes

Check for missing indexes using the following query. Test these indexes on a non-production instance to see how they affect CPU performance.
    
    
    SELECT
    CONVERT(
      decimal(18, 2), migs.user_seeks * migs.avg_total_user_cost * (migs.avg_user_impact * 0.01))
      AS [index_advantage],
    CONVERT(nvarchar(25), migs.last_user_seek, 20) AS [last_user_seek],
    mid.[statement] AS [Database.Schema.Table],
    COUNT(1) OVER (PARTITION BY mid.[statement]) AS [missing_indexes_for_table],
    COUNT(1)
      OVER (PARTITION BY mid.[statement], mid.equality_columns)
      AS [similar_missing_indexes_for_table],
    mid.equality_columns,
    mid.inequality_columns,
    mid.included_columns,
    migs.user_seeks,
    CONVERT(decimal(18, 2), migs.avg_total_user_cost) AS [avg_total_user_cost],
    migs.avg_user_impact
    FROM sys.dm_db_missing_index_group_stats AS migs WITH(NOLOCK)
    INNER JOIN sys.dm_db_missing_index_groups AS mig WITH(NOLOCK)
    ON migs.group_handle = mig.index_group_handle
    INNER JOIN sys.dm_db_missing_index_details AS mid WITH(NOLOCK)
    ON mig.index_handle = mid.index_handle
    ORDER BY index_advantage DESC
    

## Check for indexes that have too much overhead

Adding an index can help with optimization but can also add a performance overhead contributing to higher usage in CPU and memory. Review the indexes returned that have a very high number of writes compared to a very low number of reads and consider removing them.
    
    
    SELECT
     SCHEMA_NAME(o.[schema_id]) AS [Schema Name],
     OBJECT_NAME(s.[object_id]) AS [TABLE Name],
     i.name AS [Index Name],
     i.index_id,
     i.is_disabled,
     i.is_hypothetical,
     i.has_filter,
     i.fill_factor,
     s.user_updates AS [Total Writes],
     s.user_seeks + s.user_scans + s.user_lookups AS [Total Reads],
     s.user_updates - (s.user_seeks + s.user_scans + s.user_lookups) AS [Difference]
    FROM sys.dm_db_index_usage_stats AS s WITH(NOLOCK)
    INNER JOIN sys.indexes AS i WITH(NOLOCK) ON s.[object_id] = i.[object_id]
    AND i.index_id = s.index_id
    INNER JOIN sys.objects AS o WITH(NOLOCK) ON i.[object_id] = o.[object_id]
    WHERE
     OBJECTPROPERTY(s.[object_id], 'IsUserTable') = 1
     AND s.database_id = DB_ID()
     AND s.user_updates > (s.user_seeks + s.user_scans + s.user_lookups)
     AND i.index_id > 1
     AND i.[type_desc] = N'NONCLUSTERED'
     AND i.is_primary_key = 0
     AND i.is_unique_constraint = 0
     AND i.is_unique = 0
    ORDER BY [Difference] DESC, [Total Writes] DESC, [Total Reads] ASC
    

## Find the top queries consuming most of the CPU

Review the top 20 queries by CPU usage or worker time. These are the queries based on the query execution stats that use most of the CPU. These stats are aggregated over time and are linked to the plans in the cache.
    
    
    SELECT
    top 20
    SUBSTRING(qt.TEXT, (qs.statement_start_offset/2)+1,
    ((CASE qs.statement_end_offset
    WHEN -1 THEN DATALENGTH(qt.TEXT)
    ELSE qs.statement_end_offset
    END - qs.statement_start_offset)/2)+1),
    qs.execution_count,
    qs.total_logical_reads, qs.last_logical_reads,
    qs.total_logical_writes, qs.last_logical_writes,
    qs.total_worker_time,
    qs.last_worker_time,
    qs.total_elapsed_time/1000000 total_elapsed_time_in_S,
    qs.last_elapsed_time/1000000 last_elapsed_time_in_S,
    qs.last_execution_time,
    qp.query_plan
    FROM sys.dm_exec_query_stats qs
    CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) qt
    CROSS APPLY sys.dm_exec_query_plan(qs.plan_handle) qp
    ORDER BY qs.total_worker_time DESC -- CPU time
    

## Check for implicit conversions in query plans

This operation is expensive and usually shows up as a warning in the query execution plan. The message usually has a warning that says it might affect `CardinalityEstimate` in the query plan choice. You can identify implicit conversions when viewing the query plans in [SQL Server Management Studio (SSMS)](https://docs.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms?view=sql-server-2017).

## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
