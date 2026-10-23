---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/columnar-engine/monitor/
title: Monitor the columnar engine \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:52:26.676444+00:00
---

# Monitor the columnar engine  |  AlloyDB Omni for containers: 15.7.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/columnar-engine/monitor/

This page documents AlloyDB Omni version **15.7.1** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/overview)



Send feedback 

#  Monitor the columnar engine Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.1keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/columnar-engine/monitor)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/columnar-engine/monitor)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/columnar-engine/monitor)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/columnar-engine/monitor)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/columnar-engine/monitor)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/columnar-engine/monitor)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/columnar-engine/monitor)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/columnar-engine/monitor)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/columnar-engine/monitor)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/columnar-engine/monitor)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/columnar-engine/monitor)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/columnar-engine/monitor)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/columnar-engine/monitor)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/columnar-engine/monitor)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/columnar-engine/monitor)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/columnar-engine/monitor)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/columnar-engine/monitor)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/columnar-engine/monitor)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/columnar-engine/monitor)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/columnar-engine/monitor)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/columnar-engine/monitor)

This page describes how to monitor utilization of the columnar engine. 

## Verify usage of the columnar engine using `EXPLAIN`

To observe the new columnar operators that appear in a query's generated query plan, you can verify the usage of the columnar engine by using the `EXPLAIN` statement.
    
    
    EXPLAIN (ANALYZE,COSTS OFF,BUFFERS,TIMING OFF,SUMMARY OFF)
      SELECT l_returnflag, l_linestatus, l_quantity, l_extendedprice,
             l_discount, l_tax
        FROM lineitem
       WHERE l_shipdate <= date '1992-08-06'
    ;
                                     QUERY PLAN
    -----------------------------------------------------------------------------
     Append (actual rows=3941797 loops=1)
       Buffers: shared hit=9
       ->  Custom Scan (columnar scan) on lineitem (actual rows=3941797 loops=1)
             Filter: (l_shipdate <= '1992-08-06'::date)
             Rows Removed by Columnar Filter: 56054083
             Columnar cache search mode: columnar filter only
             Buffers: shared hit=9
       ->  Seq Scan on lineitem (never executed)
      Filter: (l_shipdate <= '1992-08-06'::date)
    

  * `Custom Scan (columnar scan)` indicates that columnar-engine scanning is included in the query plan.
  * `Rows Removed by Columnar Filter` lists the number of rows filtered out by the columnar vectorized execution.
  * `Columnar cache search mode` can be `columnar filter only`, `native`, or `row store scan`. The planner chooses the search mode automatically based on costing and pushdown evaluation capability.



When the planner chooses the `native` mode, it pushes down some of the columnar operators to the scan:

  * `Rows Aggregated by Columnar Scan` lists the number of rows that are aggregated.
  * `Rows Sorted by Columnar Scan` lists the number of rows that are sorted.
  * `Rows Limited by Columnar Scan` lists the limited number of rows that were scanned.



With joins, columnar scan operators can also use the `Late Materialization` mode.
    
    
    EXPLAIN (ANALYZE,COSTS OFF,BUFFERS,TIMING OFF,SUMMARY OFF)
      SELECT l_shipmode, o_orderpriority
        FROM orders, lineitem
       WHERE o_orderkey = l_orderkey
             AND l_shipmode in ('AIR', 'FOB')
             AND l_receiptdate >= date '1995-01-01'
    ;
                                     QUERY PLAN
    -----------------------------------------------------------------------------
     Hash Join (actual rows=9865288 loops=1)
       Hash Cond: (lineitem.l_orderkey = orders.o_orderkey)
       Buffers: temp read=127738 written=127738
       ->  Append (actual rows=9865288 loops=1)
             ->  Custom Scan (columnar scan) on lineitem (actual rows=9865288 loops=1)
                   Filter: ((l_shipmode = ANY ('{AIR,FOB}'::bpchar[])) AND
                   (l_receiptdate >= '1995-01-01'::date))
                   Rows Removed by Columnar Filter: 50130592
                   Columnar cache search mode: native
             ->  Index Scan using idx_lineitem_orderkey_fkidx on lineitem
                 (never executed)
                   Filter: ((l_shipmode = ANY ('{AIR,FOB}'::bpchar[])) AND
                   (l_receiptdate >= '1995-01-01'::date))
       ->  Hash (actual rows=15000000 loops=1)
             Buckets: 1048576  Batches: 32  Memory Usage: 37006kB
             Buffers: temp written=83357
             ->  Append (actual rows=15000000 loops=1)
                   ->  Custom Scan (columnar scan) on orders (actual rows=15000000
                       loops=1)
                         Rows Removed by Columnar Filter: 0
                         Columnar projection mode: late materialization
                         Columnar cache search mode: native
                   ->  Seq Scan on orders (never executed)
    

`Columnar projection mode` can be `late materialization`. Columnar operators choose this mode automatically when the planner optimizes the projection by deferring the materialization of some column values.

## View columnar engine vectorized join usage

You can verify the new vectorized join operator by using `EXPLAIN` statement to observe the new `Vectorized Hash Join` operator that appears in a query's generated query plan.
    
    
    EXPLAIN (ANALYZE,COSTS OFF,BUFFERS,TIMING OFF,SUMMARY OFF)
      SELECT l_quantity, l_extendedprice, l_discount, l_tax
        FROM lineitem, orders
        WHERE l_shipdate <= date '2022-08-06'
        AND  l_orderkey = o_orderkey
        AND  o_orderdate <= date '2025-03-07';
                                          QUERY PLAN
    ---------------------------------------------------------------------------------------
     Vectorized Hash Join (actual rows=3934686 loops=1)
       Vectorized partitioning, Partitions: 16 (Disk usage: 208MB)
       (Peak Memory Usage: 27MB, Threads: 1)
       Hash Cond: (lineitem.l_orderkey = orders.o_orderkey)
       Rows Removed by Bloom Filter: 0
       Buffers: temp read=26728 written=26728
       ->  Append (actual rows=3934686 loops=1)
             ->  Custom Scan (columnar scan) on lineitem (actual rows=3934686 loops=1)
                   Filter: (l_shipdate <= '2022-08-06'::date)
                   Rows Removed by Columnar Filter: 56051366
                   Columnar cache search mode: native
             ->  Seq Scan on lineitem (never executed)
                   Filter: (l_shipdate <= '2022-08-06'::date)
       ->  Vectorized Hash (actual rows=7245824 loops=1)
             Build bloom filter, Memory Usage: 1024kB
             ->  Append (actual rows=7245824 loops=1)
                   ->  Custom Scan (columnar scan) on orders (actual rows=7245824 loops=1)
                         Filter: (o_orderdate <= '2025-03-07'::date)
                         Rows Removed by Columnar Filter: 7754176
                         Columnar cache search mode: native
                   ->  Seq Scan on orders (never executed)
                         Filter: (o_orderdate <= '2025-03-07'::date)
    

  * `Vectorized Hash Join ` indicates that the join between the two relations used the vectorized hash join.
  * `Vectorized partitioning, Partitions: ` lists the number of partitions the data was split into.



## View information about tables with columns in the column store

You can view information about the tables or the materialized views with columns in the column store by querying the `g_columnar_relations` view.
    
    
    SELECT * FROM g_columnar_relations;
    
    ┌─[ RECORD 1 ]────────┬───────────────────┐
    │ relation_name       │ tbl_parallel_test │
    │ schema_name         │ public            │
    │ database_name       │ advisor           │
    │ status              │ Usable            │
    │ size                │ 581431259         │
    │ columnar_unit_count │ 3                 │
    │ invalid_block_count │ 0                 │
    │ total_block_count   │ 8337              │
    ├─[ RECORD 2 ]────────┼───────────────────┤
    │ relation_name       │ lineitem          │
    │ schema_name         │ public            │
    │ database_name       │ advisor           │
    │ status              │ Usable            │
    │ size                │ 423224944         │
    │ columnar_unit_count │ 29                │
    │ invalid_block_count │ 0                 │
    │ total_block_count   │ 115662            │
    ├─[ RECORD 3 ]────────┼───────────────────┤
    
    

## View information about the columns in the column store

You can view information about the columns in the column store by querying the `g_columnar_columns` view, including those columns' size and the last access time.
    
    
    SELECT database_name, schema_name, relation_name, column_name, size_in_bytes, last_accessed_time FROM g_columnar_columns;
    

## View columnar engine execution statistics for recent queries

You can view columnar engine execution statistics for recent queries using the `g_columnar_stat_statements` view. This view adds columnar engine statistics to the `pg_stat_statements` view provided by the `pg_stat_statements` extension. To use this view, you must first enable the `pg_stat_statements` extension.

  1. Enable the `pg_stat_statements` extension: 
         
         CREATE EXTENSION pg_stat_statements;
         

  2. Run the queries whose statistics you want to view. You can do this manually, or you can let enough time pass so that your applications run these queries with `pg_stat_statements` enabled.
  3. Query the `g_columnar_stat_statements` and `pg_stat_statements` views. Note the following query retrieves all the columnar execution statistics including those that were collected before the extension `pg_stat_statements` was created. The `10` value of `userid` indicates that the statistics were collected before the extension `pg_stat_statements` was created. 
         
         SELECT *
         FROM pg_stat_statements(TRUE) AS pg_stats
              FULL JOIN g_columnar_stat_statements AS g_stats
              ON pg_stats.userid = g_stats.user_id AND
                 pg_stats.dbid = g_stats.db_id AND
                 pg_stats.queryid = g_stats.query_id
         WHERE columnar_unit_read > 0;
         
         ┌─[ RECORD 1 ]────────┬───────────────────────────────
         │ userid              │ 10                            │
         │ dbid                │ 33004                         │
         │ queryid             │ 6779068104316758833           │
         │ query               │ SELECT  l_returnflag,        ↵│
         │                     │         l_linestatus,        ↵│
         │                     │         l_quantity,          ↵│
         │                     │         l_extendedprice,     ↵│
         │                     │         l_discount,          ↵│
         │                     │         l_tax                ↵│
         │                     │FROM  lineitem                ↵│
         │                     │WHERE  l_shipdate <= date $1│
         │ calls               │ 1                             │
         │ total_time          │ 299.969983                    │
         │ min_time            │ 299.969983                    │
         │ max_time            │ 299.969983                    │
         │ mean_time           │ 299.969983                    │
         │ stddev_time         │ 0                             │
         │ rows                │ 392164                        │
         │ shared_blks_hit     │ 0                             │
         │ shared_blks_read    │ 0                             │
         │ shared_blks_dirtied │ 0                             │
         │ shared_blks_written │ 0                             │
         │ local_blks_hit      │ 0                             │
         │ local_blks_read     │ 0                             │
         │ local_blks_dirtied  │ 0                             │
         │ local_blks_written  │ 0                             │
         │ temp_blks_read      │ 0                             │
         │ temp_blks_written   │ 0                             │
         │ blk_read_time       │ 0                             │
         │ blk_write_time      │ 0                             │
         │ user_id             │ 10                            │
         │ db_id               │ 33004                         │
         │ query_id            │ 6779068104316758833           │
         │ columnar_unit_read  │ 29                            │
         │ page_read           │ 115662                        │
         │ rows_filtered       │ 0                             │
         │ columnar_scan_time  │ 0                             │
         └─────────────────────┴───────────────────────────────┘
         




## View column store memory usage

To see the amount of unused RAM available to the columnar engine, you can query the `google_columnar_engine_memory_available` function. The output integer shows the available memory in megabytes (MB).
    
    
    SELECT google_columnar_engine_memory_available();
    

## View columnar engine storage cache

To view and monitor data about the storage cache of the columnar engine, you can use the following commands:

Command | Description  
---|---  
`SELECT google_columnar_engine_storage_cache_used();` | Returns the size of the used columnar engine storage cache.  
`SELECT google_columnar_engine_storage_cache_available();` | Returns the size of the unused columnar engine storage cache.  
`SHOW google_columnar_engine.storage_cache_size;` | Returns the total amount of the configured size of storage cache for the columnar engine.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
