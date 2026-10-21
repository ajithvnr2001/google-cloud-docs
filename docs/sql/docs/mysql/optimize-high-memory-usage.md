---
url: https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage/
title: Optimize high memory usage in instances \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:47.925349+00:00
---

# Optimize high memory usage in instances  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Optimize high memory usage in instances Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/optimize-high-memory-usage "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-high-memory-usage "View this page for the SQL Server database engine")

It's a common problem to have instances consuming lots of memory or running into out-of-memory (OOM) events. A database instance running with high memory utilization often causes performance issues, stalls, or even database downtime.

Some MySQL memory blocks are used globally. This means that all query workloads share memory locations, are occupied all the time, and are released only when the MySQL process stops. Some memory blocks are session based, which means that as soon as the session closes, memory used by that session is also released back to the system.

Whenever there is high memory usage by a Cloud SQL for MySQL instance, Cloud SQL recommends that you identify the query or process that's using a lot of memory and release it. MySQL memory consumption is divided into three major parts:

  * Threads and process memory consumption
  * Buffer memory consumption
  * Cache memory consumption



## Threads and process memory consumption

Each user session consumes memory depending on the queries running, buffers, or cache used by that session and is controlled by the session parameters of MySQL. The major parameters include:

  * `thread_stack`
  * `net_buffer_length`
  * `read_buffer_size`
  * `read_rnd_buffer_size`
  * `sort_buffer_size`
  * `join_buffer_size`
  * `max_heap_table_size`
  * `tmp_table_size`



If there are N number of queries running at a particular time, then each query consumes memory according to these parameters during the session.

## Buffer memory consumption

This part of memory is common for all the queries and is controlled by parameters such as `innodb_buffer_pool_size`, `innodb_log_buffer_size`, and `key_buffer_size`.

The InnoDB buffer pool, which is configured by the `innodb_buffer_pool_size` flag, occupies a significant amount of memory on your Cloud SQL for MySQL instance and serves as a cache for improving performance. To reduce the risk of out-of-memory (OOM) events, you can enable managed buffer pool.

## Cache memory consumption

Cache memory includes a query cache, which is used to save the queries and their results for faster data retrieval of the same subsequent queries. It also includes the `binlog` cache to hold the changes made to the binary log while the transaction is running, and is controlled by `binlog_cache_size`.

## Other memory consumption

Memory is also used by join and sort operations. If your queries use join or sort operations, those queries use memory on the basis of `join_buffer_size` and `sort_buffer_size`.

Apart from this, if you enable the performance schema, it consumes memory. To check the memory usage by the performance schema, use the following query:
    
    
    SELECT *
    FROM
      performance_schema.memory_summary_global_by_event_name
    WHERE EVENT_NAME LIKE 'memory/performance_schema/%';
    

There are many instruments available in MySQL that you can set up to monitor the memory usage through the performance schema. To learn more, see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.4/en/performance-schema-memory-model.html).

The MyISAM-related parameter for bulk data insertion is `bulk_insert_buffer_size`.

To learn about how MySQL uses memory, see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.4/en/memory-use.html).

## Recommendations

The following sections offer some recommendations for optimal memory usage.

### Enable managed buffer pool

Enabling managed buffer pool helps you reduce the memory consumption of the InnoDB buffer pool (or `innodb_buffer_pool_size`) when instance memory is high. This reduction frees up memory that other database processes can then consume. If your instance memory usage is high, then your instance can experience out-of-memory (OOM) events. We recommend that you enable managed buffer pool on your instance to help prevent OOM events.

When memory usage stabilizes at a lower value for 10 minutes or longer, managed buffer pool increases the value of `innodb_buffer_pool_size` incrementally to its original value. You can also increase the value of the `innodb_buffer_pool_size` flag to a chosen value after memory usage has stabilized.

#### Eligibility criteria

You can't enable managed buffer pool for shared core instances, or for MySQL 5.6 or MySQL 5.7.

#### Enable the feature

To enable managed buffer pool for your instance, set the `innodb_cloudsql_managed_buffer_pool` flag to `on`. For more information about setting database flags, see [Set a database flag](https://docs.cloud.google.com/sql/docs/mysql/flags#set_a_database_flag).

Changing the value of the `innodb_cloudsql_managed_buffer_pool` flag doesn't require a restart of the Cloud SQL instance.

If you've enabled managed buffer pool and the memory consumption of your instance exceeds the default threshold percentage of its allocated memory, then Cloud SQL begins to reduce the size of its `innodb_buffer_pool_size`. This default threshold percentage varies between 90% and 97% depending on the RAM capacity of your instance. To modify the threshold, set the `innodb_cloudsql_managed_buffer_pool_threshold_pct` flag to a different percentage value. For example, to adjust the threshold to 97%, use the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
       --database-flags=EXISTING_FLAGS,innodb_cloudsql_managed_buffer_pool=on,\
         innodb_cloudsql_managed_buffer_pool_threshold_pct=97
    

You can set the `innodb_cloudsql_managed_buffer_pool_threshold_pct` flag to an integer value between 50 and 99. Changing the value of the memory usage threshold doesn't require a restart of the Cloud SQL instance.

Managed buffer pool increases the `innodb_buffer_pool_size` flag when memory usage stabilizes for 10 minutes or longer after prior reductions. By default, database memory usage must remain at 70% or lower to trigger the increase. To modify the threshold, set the `innodb_cloudsql_managed_buffer_pool_tuneup_pct` flag to a different percentage value. For example, to change the increase threshold to 80%, use the following command:
    
    
    gcloud sql instances patch INSTANCE_NAME \
       --database-flags=EXISTING_FLAGS,innodb_cloudsql_managed_buffer_pool=on,\
         innodb_cloudsql_managed_buffer_pool_tuneup_pct=80
    

**Note:** The `innodb_cloudsql_managed_buffer_pool_tuneup_pct` flag is supported on maintenance version `R20260726.00_05` or later.

#### Adjustment logic

Managed buffer pool doesn't shrink the `innodb_buffer_pool_size` to a fixed, predetermined minimum size. Instead, it reduces the size iteratively and dynamically until total instance memory utilization drops back below the configured threshold percentage (`innodb_cloudsql_managed_buffer_pool_threshold_pct`). It shrinks the buffer pool by adjusting the value of the `innodb_buffer_pool_size` flag, leveraging [InnoDB's built-in buffer pool resize functionality](https://dev.mysql.com/doc/refman/8.4/en/innodb-buffer-pool-resize.html).

To prevent the `innodb_buffer_pool_size` from shrinking to a size that would severely impact performance when memory usage remains high despite reduction, the feature uses an internal safety floor. Values represent the percentage of total instance memory that must be allocated to the buffer pool.

MySQL container size | Minimum buffer pool size  
---|---  
1025–2048 MB | 35%  
2049–6528 MB | 30%  
6529–11315 MB | 40%  
11316–22630 MB | 45%  
Other sizes (default) | 50%  
  
The amount by which `innodb_buffer_pool_size` decreases depends on the memory capacity of your database instance. The following table shows the percentage decrease for each container size:

MySQL container size | Percentage decrease  
---|---  
1025–2048 MB | 15%  
2049–6528 MB | 11%  
6529–11315 MB | 8%  
11316–22630 MB | 6%  
Other sizes (default) | 5%  
  
After calculating the new, reduced value, the managed buffer pool rounds `innodb_buffer_pool_size` to the nearest multiple of the `innodb_buffer_pool_instances` and `innodb_buffer_pool_chunk_size` values.

When managed buffer pool makes adjustments to value of `innodb_buffer_pool_size`, the changes aren't reflected in Google Cloud console. To view the current value of `innodb_buffer_pool_size` when managed buffer pool is enabled, you can use the MySQL client:
    
    
    mysql> SHOW GLOBAL VARIABLES LIKE 'innodb_buffer_pool_size';
    

#### Limitations

Reducing the buffer pool size can't prevent OOMs in all cases. For example, some workloads might consume memory unsustainably or increase at a sudden rate, some Cloud SQL instances might be under provisioned, or the buffer pool might not be warmed up. Cloud SQL might not be able to free up memory quickly enough to accommodate sudden changes in memory workload. In addition, Cloud SQL can't accommodate misconfigured values of other memory flags.

**Note:** Decreasing the value of `innodb_buffer_pool_size` can impact query latency and performance. However, enabling managed buffer pool decreases the value of `innodb_buffer_pool_size` only when the instance is at risk of an OOM event. When memory usage stabilizes for 10 minutes or longer, the value of `innodb_buffer_pool_size` is restored to its original value gradually.

#### Monitoring

You can monitor managed buffer pool in the [MySQL error log](https://docs.cloud.google.com/sql/docs/mysql/logging). In [Cloud Logging Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), you can filter the [`mysql.err`](https://docs.cloud.google.com/logging/docs/view/query-library#sql-filters) log for entries with the prefix `Managed Buffer Pool Plugin:` or `Tuner Plugin:` to find the latest adjustment events.

When managed buffer pool first starts up, it emits a log like the following:
    
    
    [Note] [MY-000000] [Server] Managed Buffer Pool Plugin: MySQL Instance memory limit: 29533, Current MySQL memory usage: 2663641088, Max Allowed MySQL memory usage: 30732730368 ...
    

The following logs show examples of automated decreases to the `innodb_buffer_pool_size`:
    
    
    [Note] [MY-000000] [Server] Managed Buffer Pool Plugin: Decreasing InnoDB Buffer Pool Size.
    [Note] [MY-000000] [Server] Managed Buffer Pool Plugin: Updated innodb_buffer_pool_size=805306368 bytes.
    

You can configure [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) to track managed buffer pool adjustment events over time.

### Use Cloud Monitoring Metrics Explorer to identify the memory usage

You can review the memory usage of an instance with the [`database/memory/components.usage`](https://docs.cloud.google.com/sql/docs/mysql/admin-api/metrics) metric in [Cloud Monitoring Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

In general, if you have less than 10% memory in `database/memory/components.cache` and `database/memory/components.free` combined, the risk of an OOM event is high. To monitor the memory usage and to prevent OOM events, we recommend that you set up an [alerting policy](https://docs.cloud.google.com/monitoring/alerts) with a metric threshold condition in `database/memory/components.usage`.

The following table shows the relationship between your instance memory and the recommended alerting threshold:

Instance memory | Recommended alerting threshold  
---|---  
Less than or equal to 16 GB | 90%  
Greater than 16 GB | 95%  
  
### Calculate memory consumption

Calculate the maximum memory usage by your MySQL database to select the appropriate instance type for your MySQL database. Use the following formula:

Maximum MySQL memory usage = `innodb_buffer_pool_size` \+ `innodb_additional_mem_pool_size` \+ `innodb_log_buffer_size` \+ `tmp_table_size` \+ `key_buffer_size` \+ ((`read_buffer_size` \+ `read_rnd_buffer_size` \+ `sort_buffer_size` \+ `join_buffer_size`) x `max_connections`)

Here are the parameters used in the formula:

  * `innodb_buffer_pool_size`: The size in bytes of the buffer pool, the memory area where InnoDB caches table and index data.
  * `innodb_additional_mem_pool_size`: The size in bytes of a memory pool InnoDB uses to store data dictionary information and other internal data structures.
  * `innodb_log_buffer_size`: The size in bytes of the buffer that InnoDB uses to write to the log files on disk.
  * `tmp_table_size`: The maximum size of internal in-memory temporary tables created by the MEMORY storage engine and, as of MySQL 8.0.28, the TempTable storage engine.
  * `key_buffer_size`: The size of the buffer used for index blocks. Index blocks for MyISAM tables are buffered and are shared by all threads.
  * `read_buffer_size`: Each thread that does a sequential scan for a MyISAM table allocates a buffer of this size (in bytes) for each table it scans.
  * `read_rnd_buffer_size`: This variable is used for reads from MyISAM tables, for any storage engine, and for Multi-Range Read optimization.
  * `sort_buffer_size`: Each session that must perform a sort allocates a buffer of this size. sort_buffer_size is not specific to any storage engine and applies in a general manner for optimization.
  * `join_buffer_size`: The minimum size of the buffer that's used for plain index scans, range index scans, and joins that don't use indexes and thus perform full table scans.
  * `max_connections`: The maximum permitted number of simultaneous client connections.

**Note:** There are many other small components consuming memory which depends on the queries so there should be room for those components as well.

### Troubleshoot high memory consumption

  * Run `SHOW PROCESSLIST` to see the ongoing queries that are consuming memory. It displays all connected threads and their running SQL statements and tries to optimize them. Pay attention to the state and duration columns.
        
        mysql> SHOW [FULL] PROCESSLIST;
        
        

  * Check `SHOW ENGINE INNODB STATUS` in the section `BUFFER POOL AND MEMORY` to see the current buffer pool and memory usage, which can help you set your buffer pool size.
        
        mysql> SHOW ENGINE INNODB STATUS \G
        ----------------------
        BUFFER POOL AND MEMORY
        ----------------------
        Total memory allocated 398063986; in additional pool allocated 0
        Dictionary memory allocated 12056
        Buffer pool size 89129
        Free buffers 45671
        Database pages 1367
        Old database pages 0
        Modified db pages 0
        

  * Use MySQL's `SHOW variables` command to check the counter values, which give you information such as number of temporary tables, number of threads, number of table caches, dirty pages, open tables, and buffer pool usage.
        
        mysql> SHOW variables like 'VARIABLE_NAME'
        




### Apply changes

After you analyze the memory usage by different components, set the appropriate flag in your MySQL database. To change the flag in Cloud SQL for MySQL instance, you can use Google Cloud console or [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch). To change the flag value using the Google Cloud console, edit the **Flags** section, select the flag, and enter the new value.

Lastly, if the memory usage is still high and you feel running queries and flag values are optimized, then consider increasing the instance size to avoid OOM.

## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
