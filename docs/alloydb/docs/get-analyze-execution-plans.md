---
url: https://docs.cloud.google.com/alloydb/docs/get-analyze-execution-plans/
title: Get and analyze AlloyDB explain plans \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:01.549780+00:00
---

# Get and analyze AlloyDB explain plans  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/get-analyze-execution-plans/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Get and analyze AlloyDB explain plans Stay organized with collections  Save and categorize content based on your preferences. 

You can identify performance bottlenecks and optimize your AlloyDB for PostgreSQL database operations by getting and analyzing execution plans. An _execution plan_ or `EXPLAIN` plan is a detailed representation of how your AlloyDB database engine intends to execute a SQL query. The execution plan comprises a tree of nodes that outlines the sequence of operations, such as table scans, joins, sorting, and aggregations, that the AlloyDB database performs to retrieve the requested data. Each step in this plan is referred to as a _node_.

An execution plan is obtained by using the `EXPLAIN` command, which returns the plan that the AlloyDB query planner generates for a given SQL statement. A _query planner_ , also known as an optimizer, determines the most efficient way to execute a given SQL query.

Execution plans include the following components:

  * Plan nodes: these represent the different steps in the query execution, such as a scan, a join, or a sort operation.
  * Execution time: the EXPLAIN plan includes the estimated or actual execution time for each step, which helps you identify database bottlenecks.
  * Buffer usage: this shows how much data is read from disk versus the cache, which helps identify disk read issues.
  * Parameter settings: the plan shows the parameter settings that are effective during the query execution.



PostgreSQL, and by extension AlloyDB, supports execution plans for the following statements:

  * `SELECT`
  * `INSERT`
  * `UPDATE`
  * `DECLARE CURSOR`
  * `CREATE AS`
  * `CREATE MATERIALIZED VIEW`
  * `REFRESH MATERIALIZED VIEW`
  * `EXECUTE`



## Before you begin

You must have an AlloyDB cluster and instance. For more information, see [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create).

## Generate an execution plan

You generate an execution plan from a client application such as psql, pgAdmin or DBeaver. AlloyDB supports generating execution plans in text or JSON format.

To generate an execution plan, follow these steps:

  1. [Connect a psql client to an instance](https://docs.cloud.google.com/alloydb/docs/connect-psql).
  2. To generate an execution plan in text format, run the following command:
         
         SET enable_ultra_fast_cache_explain_output TO ON; /* AlloyDB Specific Command */
         EXPLAIN (analyze, verbose, columnar_engine, costs, settings, buffers, wal, timing, summary, format text)
         

  3. To generate an execution plan in JSON format, run the following command:
         
         SET enable_ultra_fast_cache_explain_output TO ON; /* AlloyDB Specific Command */
         EXPLAIN (analyze, verbose, columnar_engine, costs, settings, buffers, wal, timing, summary, format json)
         

The `EXPLAIN` command includes all available options—`analyze`, `verbose`, `columnar_engine`, `costs`, `settings`, `buffers`, `wal`, `timing`, and `summary`—to generate a detailed execution plan for a given query in text or JSON format. The `analyze` option means that the query is executed to provide actual runtime statistics as well as the query planner's estimates.




## View and analyze EXPLAIN plan data

After you get an execution plan, you view and analyze the results.

By default, `EXPLAIN` output shows server-side query activity. To measure end-to-end round trip time, use the `/timing` option in psql and dump the results to `/dev/null`.

To see the execution plan that you generated, you use the `EXPLAIN` command before your SQL query.

  * `EXPLAIN SELECT...`: shows the plan that the optimizer would choose without running the query. 
  * `EXPLAIN ANALYZE SELECT...`: executes the query and shows both the predicted plan and the actual execution statistics, including true run times and row counts.



### EXPLAIN without ANALYZE

To show the query planner's estimated query costs, execute an `EXPLAIN` statement without the `ANALYZE` option .
    
    
    (postgres@10.3.1.17:5432) [postgres] > EXPLAIN select * from public.index_advisor_test;
                                       QUERY PLAN
    ---------------------------------------------------------------------------------
     Seq Scan on index_advisor_test  (cost=0.00..1735481.00 rows=100000000 width=27)
     AlloyDB query id: 7588555592527881263
     AlloyDB plan id: 16134093550604823483
    (3 rows)
    

The plan output includes the following data:

  * **cost = 0.00..1735481.00** : the first number indicates the cost to retrieve the first row. The second number indicates the cost to retrieve the last row.
  * **rows = 100000000** : this is the estimated number of rows that the query returns.
  * **width = 27** : this is the estimated width of the returned row, which helps you understand accessed blocks.



### ANALYZE option

To display actual execution statistics as well as execution estimates, add the `ANALYZE` option 
    
    
    (postgres@10.3.1.17:5432) [postgres] > EXPLAIN (ANALYZE) select * from public.index_advisor_test;
                                       QUERY PLAN
    ---------------------------------------------------------------------------------
     Seq Scan on index_advisor_test  (cost=0.00..1735481.00 rows=100000000 width=27) (actual time=0.165..9342.424 rows=100000001 loops=1)
     Planning Time: 0.025 ms
     Execution Time: 13674.794 ms
     AlloyDB query id: 7588555592527881263
     AlloyDB plan id: 16134093550604823483
    (5 rows)
    

The plan output includes the following data:

  * **actual time (in ms) = 0.165..9342.424** : this shows the actual time to return the first row and the total time to return all rows.
  * **rows = 100000001** : this is the actual number of rows returned.
  * **loops = 1** : this value is important for nested loop nodes. It shows the average time per loop if `loops` is greater than 1.
  * **Planning Time: 0.025 ms** : this indicates the time the planner took to determine the execution path.
  * **Execution Time: 13674.794 ms** : this indicates the time execution took after the planner determined the path.
  * **Total Execution Time** : the sum of `Planning Time` and `Execution Time`. (0.025 + 13674.794 = 13674.819)



### VERBOSE option

To add more information to the execution plan, use the `VERBOSE` option. In the following example, using `VERBOSE` adds schema qualifications to table names and shows an internal query identifier that you can use to correlate your query with other monitoring tools.
    
    
    (postgres@10.3.1.17:5432) [postgres] > EXPLAIN (ANALYZE,VERBOSE) select * from public.index_advisor_test;
                                       QUERY PLAN
    ---------------------------------------------------------------------------------
    Seq Scan on public.index_advisor_test  (cost=0.00..1735481.00 rows=100000000 width=27) (actual time=0.164..6568.938 rows=100000001 loops=1)
       Output: id, value, product_id, effective_date
     Query Identifier: -5175350694118300766
     Planning Time: 0.027 ms
     Execution Time: 10875.894 ms
     AlloyDB query id: 7588555592527881263
     AlloyDB plan id: 16134093550604823483
    

The plan output includes the following data:

  * **Output Node** : lists the columns included in the query. The planner sometimes includes more columns than requested if it determines leaving them behind is more expensive.
  * **Query Identifier** : the PostgreSQL identifier that maps to `pg_stat_statements`.
  * **AlloyDB query id** : the AlloyDB query identifier that can be used to correlate query insights information



### COLUMNAR ENGINE option

To display information for the [AlloyDB columnar engine](https://docs.cloud.google.com/alloydb/docs/columnar-engine/about), add the `COLUMNAR_ENGINE` option.

If the table isn't present in the columnar engine, see the **Columnar Check** column in the following explain plan for the status.
    
    
    (postgres@10.3.1.17:5432) [postgres] > EXPLAIN (ANALYZE,VERBOSE, COLUMNAR_ENGINE) select * from public.index_advisor_test;
                                       QUERY PLAN
    ---------------------------------------------------------------------------------
    Seq Scan on public.index_advisor_test  (cost=0.00..1735481.00 rows=100000000 width=27) (actual time=0.009..6328.154 rows=100000001 loops=1)
       Output: id, value, product_id, effective_date
       Columnar Check: table is not in the columnar store
     Query Identifier: -5175350694118300766
     Planning Time: 0.027 ms
     Execution Time: 10673.310 ms
     AlloyDB query id: 7588555592527881263
     AlloyDB plan id: 16134093550604823483
    

If the table is present in the columnar engine and columnar is used, a **Custom Scan** is indicated along with stats about how the columnar engine is used.
    
    
    (postgres@10.3.1.17:5432) [postgres] > EXPLAIN (ANALYZE,VERBOSE, COLUMNAR_ENGINE) select * from public.index_advisor_test where product_id = 1;
                                       QUERY PLAN
    ---------------------------------------------------------------------------------
    Append  (cost=20.00..27438.78 rows=1166668 width=27) (actual time=0.066..377.029 rows=1000290 loops=1)
       ->  Custom Scan (columnar scan) on public.index_advisor_test  (cost=20.00..27437.66 rows=1166667 width=27) (actual time=0.065..296.904 rows=1000290 loops=1)
             Output: id, value, product_id, effective_date
             Filter: (index_advisor_test.product_id = 1)
             Rows Removed by Columnar Filter: 98999711
             Bytes fetched from storage cache: 774835915
             Columnar cache search mode: native
             Swap-in Time: 92.708 ms
       ->  Seq Scan on public.index_advisor_test  (cost=0.00..1.11 rows=1 width=27) (never executed)
             Output: id, value, product_id, effective_date
             Filter: (index_advisor_test.product_id = 1)
     Query Identifier: -4660018746142248761
     Planning Time: 0.217 ms
     Execution Time: 421.114 ms
     AlloyDB query id: 13855683355620344431
     AlloyDB plan id: 2126918133221480510
    

The plan output includes the following data:

  * **Query Filter (predicate)** : this shows the filter applied, if you use one.
  * **Rows Removed by Columnar Filter** : this indicates the number of rows that the columnar filter removed.
  * **Bytes fetched from storage cache** : this shows the number of bytes retrieved from the storage cache.
  * **Swap-in Time** : this is the time required to swap data from the columnar spill cache (SSD) if the relation doesn't fit into memory.



### SETTINGS option

To show any non-default session, database, or global settings that the planner uses, add the `SETTINGS` option.
    
    
    (postgres@10.3.1.17:5432) [postgres] > EXPLAIN (ANALYZE,VERBOSE, COLUMNAR_ENGINE,COSTS,SETTINGS) select * from public.index_advisor_test;
    
                                       QUERY PLAN
    ---------------------------------------------------------------------------------
    Seq Scan on public.index_advisor_test  (cost=0.00..1735481.00 rows=100000000 width=27) (actual time=0.007..6366.249 rows=100000001 loops=1)
       Output: id, value, product_id, effective_date
       Columnar Check: table is not in the columnar store
     Settings: effective_cache_size = '19690120kB', random_page_cost = '1.1', work_mem = '256MB'
     Query Identifier: -5175350694118300766
     Planning Time: 0.027 ms
     Execution Time: 10727.068 ms
     AlloyDB query id: 7588555592527881263
     AlloyDB plan id: 16134093550604823483
    

### BUFFERS option

To display information about the data source, use the `BUFFERS` keyword. The `BUFFERS` count accumulates from all steps, not just from a particular step in the plan.
    
    
    (postgres@10.3.1.17:5432) [postgres] > EXPLAIN (ANALYZE,VERBOSE, COLUMNAR_ENGINE,COSTS,SETTINGS, BUFFERS) select * from public.effective_io_concurrency_test;
    
                                       QUERY PLAN
    ---------------------------------------------------------------------------------
    Seq Scan on public.effective_io_concurrency_test  (cost=0.00..1844356.96 rows=100058296 width=31) (actual time=0.111..10007.193 rows=100000001 loops=1)
       Output: id, value, product_id, effective_date
       Buffers: shared hit=1185 read=842625 dirtied=1, ultra fast cache hit=842625
       I/O Timings: shared read=2588.597
       Columnar Check: table is not in the columnar store
     Settings: effective_cache_size = '19690120kB', random_page_cost = '1.1', work_mem = '256MB'
     Query Identifier: -5987221491374921441
     Planning:
       Buffers: shared hit=58 read=2, ultra fast cache hit=2
       I/O Timings: shared read=0.215
     Planning Time: 0.410 ms
     Execution Time: 14825.271 ms
     AlloyDB query id: 12754549874439071326
     AlloyDB plan id: 13656575252012920931
    

Buffer information includes the following:

  * **shared hit** : the number of 8kB data blocks found in PostgreSQL's main shared buffer cache.
  * **shared read** : the number of 8kB data blocks read from the operating system. This often indicates disk I/O.
  * **dirtied** : the number of previously unmodified blocks the query changed (visibility map changes).
  * **written** : the number of previously-dirtied blocks evicted from cache by this backend during query processing, usually due to hint bit or visibility map changes and flushed to disk.
  * **ultra fast cache hit** : the number of blocks retrieved from the ultra-fast cache.
  * **I/O Timings** : the duration of any disk or SSD I/O in milliseconds.
  * **Planning** : buffer activity during the planning phase, such as reading metadata or statistics from catalog tables.
  * **Time spent on I/O during planning** : this shows I/O time if any metadata required reading from disk.



### WAL option

To provide information about [Write-Ahead Logging](https://www.postgresql.org/docs/16/wal-intro.html) (WAL) activity, use the `WAL` option .
    
    
    (postgres@10.3.1.17:5432) [postgres] > EXPLAIN (ANALYZE,VERBOSE, COLUMNAR_ENGINE,COSTS,SETTINGS, BUFFERS, WAL) select * from public.effective_io_concurrency_test;
    
                                       QUERY PLAN
    ---------------------------------------------------------------------------------
    Seq Scan on public.effective_io_concurrency_test  (cost=0.00..1844356.96 rows=100058296 width=31) (actual time=0.010..10147.314 rows=100000001 loops=1)
       Output: id, value, product_id, effective_date
       Buffers: shared hit=1185 read=842625 dirtied=1, ultra fast cache hit=842625
       I/O Timings: shared read=2590.410
       WAL: records=18 bytes=5178
       Columnar Check: table is not in the columnar store
     Settings: effective_cache_size = '19690120kB', random_page_cost = '1.1', work_mem = '256MB'
     Query Identifier: -5987221491374921441
     Planning Time: 0.030 ms
     Execution Time: 15033.004 ms
     AlloyDB query id: 12754549874439071326
     AlloyDB plan id: 13656575252012920931
    

WAL information includes the following:

  * **WAL records** : the number of WAL records read to maintain consistency.
  * **WAL bytes** : the number of bytes read from WAL to maintain consistency.
  * **Records that have been modified but not yet checkpointed** : this indicates records that are modified but not yet checkpointed.



## What's next

  * Learn about [execution plan node types](https://docs.cloud.google.com/alloydb/docs/reference/execution-plan-nodes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
