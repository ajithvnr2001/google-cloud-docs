---
url: https://docs.cloud.google.com/sql/docs/postgres/optimize-high-memory-usage/
title: Optimize high memory usage in instances \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:08.735973+00:00
---

# Optimize high memory usage in instances  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/optimize-high-memory-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Optimize high memory usage in instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/optimize-high-memory-usage "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-high-memory-usage "View this page for the SQL Server database engine")

This document covers how to identify high memory usage for Cloud SQL instances and provides recommendations on how to solve memory-related issues.

To learn how to configure memory usage for a Cloud SQL instance, see [Best practices for managing memory usage](https://docs.cloud.google.com/sql/docs/postgres/manage-memory-usage-best-practices).

## Identify high memory usage

The following sections discuss high memory usage scenarios.

### Use Metrics Explorer to identify the memory usage

You can review memory usage of the instance with the [`database/memory/components`](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics) metric in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer):

  * **`usage`** : memory actively used by PostgreSQL processes, including `shared_buffers` and other in-database caches.
  * **`cache`** : memory used by the operating system page cache, which is generally reclaimable. High `cache` values don't necessarily indicate memory pressure.
  * **`free`** : unused memory available to database processes or the operating system page cache.

**Note:** If you have less than 10% memory in `database/memory/components.cache` and `database/memory/components.free` combined, the risk of an OOM event is high. To monitor the memory usage and to prevent OOM events, we recommend that you set up an [alerting policy](https://docs.cloud.google.com/monitoring/alerts) with a metric threshold condition of 90% in `database/memory/components.usage`.

### Use Query insights to analyse the explain plan for queries that are consuming high resources

[Query insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights) helps you detect, diagnose, and prevent query performance problems for Cloud SQL databases. Query insights gives you a list of long running queries along with their [explain plan (PostgreSQL documentation)](https://www.postgresql.org/docs/current/sql-explain.html). Review the explain plan and identify the part of the query that has a high memory usage scan method. Regardless of the query run time, query insights gives you the explain plan for all queries. Identify the complex queries that are taking more time so that you know which queries are blocking the memory for longer durations.

Common PostgreSQL scan methods that use high memory include the following:

  * Bitmap heap scan
  * Quick sort
  * Hash join or Hash



## High memory usage and relevant logs for Gemini-enabled instances

**Preview —[Gemini in Databases](https://docs.cloud.google.com/gemini/docs/overview) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you have [Gemini](https://docs.cloud.google.com/gemini/docs/overview) enabled, instead of an OOM failure which leads to database downtime, a connection executing a query with high memory usage is terminated thereby preventing database downtime. To identify the defaulting query, you can check the database logs for the following entries:
    
    
      (...timestamp….) db=postgres, user=customer FATAL: terminating connection due to administrator command
    

The following Cloud SQL for PostgreSQL database log is displayed which captures the high memory usage query that was terminated to prevent OOM. The query is a normalized version of the original query:
    
    
      db=postgres,user=customer LOG:  postgres process with PID 1734 for the query "SELECT COUNT(product) AS item_count FROM test_table WHERE product_type = $1 AND product LIKE $2 AND c6_2 IN ($3,$4,$5,$6,$7)" has been cancelled.
    

Notifications are also displayed on the **Cloud SQL Instances** page for the following events:

  * Memory utilization of the instance over the last 24 hours.
  * List of normalized queries that have been canceled within the past 24 hours.
  * A link to Google documentation about optimizing memory usage.



## High Memory Usage - Recommendations

The following recommendations address the common memory-related problems. If the instance continues to use a high amount of memory, chances are high that it eventually gets an `out of memory` issue. If the memory demands of either PostgreSQL or another process cause the system to run out of memory, you see an `Out of Memory` kernel message in PostgreSQL logs and the PostgreSQL instance is eventually stopped. For example:
    
    
    Out of Memory: Killed process 12345 (postgres)
    

The most common instance where you see an OOM issue is with a higher value of `work_mem` with a high number of active connections. Therefore, if you are getting frequent OOMs or to avoid OOMs in your Cloud SQL for PostgreSQL instance, you should consider following these recommendations:

  * Set `work_mem`

Queries that use quick sort are faster than the ones using external merge sort. However, the former may lead to memory exhaustion. To resolve this issue, set the `work_mem` value reasonable enough such that it balances both, the sort operations happening in the memory and disk. You can also consider setting `work_mem` on a session level rather than setting it for an entire instance.

  * Monitor the active sessions

Each connection uses a certain amount of memory. Use the following query to check the active connections count:
        
        SELECT
            state,
            usename,
            count(1)
          FROM
            pg_stat_activity
          WHERE
            pid <> pg_backend_pid()
          GROUP BY
            state,
            usename
          ORDER BY
            1;
        

If you have a large number of active sessions, analyze the root cause for a high number of active sessions; for example, transaction locks.

  * Set `shared_buffers`

If `shared_buffers` is set to a higher value, consider decreasing the `shared_buffers` value so that the memory can be used for other operations, such as `work_mem`, or for establishing new connections.

**Cache hit ratio**

PostgreSQL generally tries to keep the data you access most often in the cache. When the data is requested by a client, if it's already cached in shared buffers, it's directly given to the client. This is called a _cache hit_. If the data is not present in shared buffers, the data is first fetched to shared buffers from a disk and then given to the client. This is called a _cache miss_. Cache hit ratio measures how many content requests the cache has handled compared to the requests received. Run the following query to check the cache hit ratio for the table requests in the PostgreSQL instance:
        
        SELECT
          sum(heap_blks_read) as heap_read,
          sum(heap_blks_hit)  as heap_hit,
          sum(heap_blks_hit) / (sum(heap_blks_hit) + sum(heap_blks_read)) as ratio
        FROM
          pg_statio_user_tables;
        

Run the following query to check the cache hit ratio for the index requests in the PostgreSQL instance:
        
        SELECT
            sum(idx_blks_read) as idx_read,
            sum(idx_blks_hit)  as idx_hit,
            (sum(idx_blks_hit) - sum(idx_blks_read)) / sum(idx_blks_hit) as ratio
          FROM
            pg_statio_user_indexes;
        

Generally, 95 to 99% of cache hit ratio is considered to be a good value.

  * In Cloud SQL for PostgreSQL, the `huge_pages` flag is enabled by default for better memory management. To learn more about `huge_pages`, see [PostreSQL documentation](https://www.postgresql.org/docs/current/runtime-config-resource.html#GUC-HUGE-PAGES).

  * Set `max_locks_per_transaction`

The `max_locks_per_transaction` value indicates the number of database objects that can be locked simultaneously. In most cases, the default value of 64 is sufficient. However, if you are dealing with a large dataset, you may end up with OOMs. Consider increasing the value of `max_locks_per_transaction` high enough to avoid OOMs.

**Note:** The object-level locking happens in memory on an ongoing transaction, Increasing the `max_prepared_transactions` value unreasonably high can cause the database instance to request more shared memory.

The `max_locks_per_transaction` value should be `max_locks_per_transaction` * (`max_connections` \+ `max_prepared_transactions`) objects. This means that if you have 300 thousand objects, and if the value of `max_connections` is 200, then `max_locks_per_transaction` should be 1500.

  * Set `max_pred_locks_per_transaction`

The transaction might fail if you have clients that touch many different tables in a single serializable transaction. In that scenario, consider increasing `max_pred_locks_per_transaction` to a reasonably high value. Like `max_locks_per_transaction`, `max_pred_locks_per_transaction` also uses shared memory so don't set an unreasonable high value.

  * If the memory usage is still high and you feel those queries are legitimate traffic, then consider increasing the number of memory resources in your instance to avoid database crash or downtime.




## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
