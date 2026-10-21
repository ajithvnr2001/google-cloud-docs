---
url: https://docs.cloud.google.com/alloydb/docs/columnar-engine/monitor-tune/
title: Monitor the columnar engine \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:23.755137+00:00
---

# Monitor the columnar engine  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/columnar-engine/monitor-tune/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Monitor the columnar engine Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor utilization of the columnar engine.

## Verify usage of the columnar engine using `EXPLAIN`

You can verify the usage of the columnar engine by using the `EXPLAIN` statement to observe the new columnar operators that appear in a query's generated query plan.

### psql Client
    
    
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
    

  * `Custom Scan (columnar scan)` indicates that columnar-engine scanning is being included in the query plan.
  * `Rows Removed by Columnar Filter` lists the number of rows filtered out by the columnar vectorized execution.
  * `Columnar cache search mode` can be `columnar filter only`, `native`, or `row store scan`. The planner chooses the search mode automatically based on costing and pushdown evaluation capability.



When the planner chooses the `native` mode, it pushes down some of the columnar operators to the scan:

  * `Rows Aggregated by Columnar Scan` lists the number of rows that are aggregated.
  * `Rows Sorted by Columnar Scan` lists the number of rows that are sorted.
  * `Rows Limited by Columnar Scan` lists the limited number of rows that were scanned.



With joins, columnar scan operators can also use the `Late Materialization` mode.

### psql Client
    
    
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



### Use the `COLUMNAR_ENGINE` option for `EXPLAIN`

The `EXPLAIN` command supports the `COLUMNAR_ENGINE` option. When specified, the command prints out `Columnar Check` messages in the EXPLAIN plan to show what might have led the planner or executor to make certain columnar engine related choices for the plan. The command also prints out additional details that are specific to the columnar engine. The message is associated with the non-columnar scan node. It typically indicates the first cause that prevents a columnar scan from being chosen for a scan. Some example causes are `the table is too small`, `a needed column of the table is not in the CE store`, or `a needed column has a CE unsupported data type`.

The following example output of the command prints out a `Columnar Check` message:

### psql Client
    
    
    EXPLAIN (COLUMNAR_ENGINE, COSTS OFF)
    SELECT * FROM sample_small_table
    WHERE col1 > 10000;
                  QUERY PLAN
    --------------------------------------
     Seq Scan on sample_small_table
       Filter: (col1 > 10000)
       Columnar Check: table is too small
    

Based on the message, the user can do one of the following:

  * Address the specific cause and then rerun the command to confirm the columnar plan.
  * Iterate over the same process. There can be more than one cause, and the clause only tries to list the first one.



The following example shows additional details being printed that are specific to the columnar engine:

### psql Client
    
    
    EXPLAIN (ANALYZE, COLUMNAR_ENGINE, COSTS OFF, TIMING OFF, SUMMARY OFF, VERBOSE) SELECT SUM(c1) FROM counter_table WHERE c2 > 0 and c2 < 80000;
                                             QUERY PLAN
    ---------------------------------------------------------------------------------------------
     Aggregate (actual rows=1 loops=1)
       Output: sum(c1)
       ->  Append (actual rows=79999 loops=1)
             ->  Custom Scan (columnar scan) on public.counter_table (actual rows=79999 loops=1)
                   Output: c1
                   Filter: ((counter_table.c2 > 0) AND (counter_table.c2 < 80000))
                   Rows Removed by Columnar Filter: 1
                   Rows Aggregated by Columnar Scan: 79999
                   **Bytes fetched from storage cache: 1392655**
                   Columnar cache search mode: native
             ->  Seq Scan on public.counter_table (never executed)
                   Output: c1
                   Filter: ((counter_table.c2 > 0) AND (counter_table.c2 < 80000))
    (13 rows)
    

## View information about tables with columns in the column store

You can view information about the tables or the materialized views with columns in the column store by querying the `g_columnar_relations` view.

### psql Client
    
    
    SELECT * FROM g_columnar_relations;
    
    -[ RECORD 1 ]------------------+---------------------
    database_name                  | postgres
    schema_name                    | public
    relation_name                  | uuid_mod_test_stored
    status                         | Usable
    size                           | 700672237
    invalid_block_count            | 0
    block_count_in_cc              | 123907
    total_block_count              | 123907
    auto_refresh_trigger_count     | 0
    auto_refresh_failure_count     | 0
    auto_refresh_trigger_timestamp | NULL
    auto_refresh_start_timestamp   | NULL
    auto_refresh_end_timestamp     | NULL
    auto_refresh_recent_status     | NONE YET
    

## View information about the columns in the column store

You can view information about the columns in the column store by querying the `g_columnar_columns` view, including those columns' size and the last access time.

### psql Client
    
    
    SELECT database_name, schema_name, relation_name, column_name, size_in_bytes, last_accessed_time FROM g_columnar_columns;
    

## View columnar engine execution statistics for recent queries

You can view columnar engine execution statistics for recent queries using the `g_columnar_stat_statements` view. This view provides columnar engine-specific statistics and requires the `pg_stat_statements` extension to be enabled.

### psql Client

To view these statistics, follow these steps:

  1. Enable the `pg_stat_statements` extension: 
         
         CREATE EXTENSION pg_stat_statements;
         

  2. Run the queries for which you want to see statistics. You can do this manually, or you can let your applications run for a while to generate data.
  3. Query the `g_columnar_stat_statements` view to see the collected statistics. 
         
         SELECT * FROM g_columnar_stat_statements WHERE page_read > 0;
         

The output is similar to the following:
         
         -[ RECORD 1 ]--------------------------+--------------------
         user_id                              | 16391
         db_id                                | 1008530
         query_id                             | 6672321263128921833
         columnar_unit_read                   | 32
         page_read                            | 128003
         rows_filtered                        | 0
         columnar_scan_time                   | 0
         vectorized_join_time                 | 0
         vectorized_aggregation_time          | 0
         vectorized_aggregation_vj_time       | 0
         -[ RECORD 2 ]--------------------------+--------------------
         user_id                              | 16391
         db_id                                | 1008530
         query_id                             | -816808861243589285
         columnar_unit_read                   | 30
         page_read                            | 119811
         rows_filtered                        | 0
         columnar_scan_time                   | 0
         vectorized_join_time                 | 0
         vectorized_aggregation_time          | 0
         vectorized_aggregation_vj_time       | 0
         




## View column store memory usage

To see the amount of unused RAM available to the columnar engine, you can query the `google_columnar_engine_memory_available()` function. The resulting integer shows the available memory in megabytes (MB).
    
    
    SELECT google_columnar_engine_memory_available();
    

## View information about indexes in the column store

You can view information about the status, size, and various performance-related metrics of columnar indexes by querying the `g_columnar_indexes` view.

### psql Client
    
    
    SELECT
         database_name, schema_name, index_name, status, size,
         total_partition_count, non_leaf_partition_count, leaf_partition_count,
         invalid_block_count, block_count_in_cc, total_block_count,
         creation_time, auto_refresh_trigger_count,
         auto_refresh_failure_count, auto_refresh_trigger_timestamp,
         auto_refresh_start_timestamp, auto_refresh_end_timestamp,
         auto_refresh_recent_status
    FROM g_columnar_indexes;
    

The following table describes the fields of the `g_columnar_indexes` view.

Field | Data type | Description  
---|---|---  
database_name | NAME |   
schema_name | NAME | Name of the schema to which index belongs  
index_name | NAME | Name of the index  
status | NAME | Status of the index in the columnar engine  
size | BIGINT | Size of the index in the columnar engine  
total_partition_count | BIGINT | Total number of index's partitions in columnar engine  
non_leaf_partition_count | BIGINT | Total number of index's non-leaf partitions in columnar engine  
leaf_partition_count | BIGINT | Total number of index's leaf partitions in columnar engine  
invalid_block_count | BIGINT | Total number of invalid blocks in columnar engine for the index  
block_count_in_cc | BIGINT | Total number of index's blocks in columnar engine  
total_block_count | BIGINT | Total number of index's blocks  
creation_time | BIGINT | Index creation time in columnar engine  
auto_refresh_trigger_count | BIGINT | Total number of auto refreshes triggered since the postgres startup.  
auto_refresh_failure_count | BIGINT | Total number of auto refresh failures since the postgres startup  
auto_refresh_trigger_timestamp | BIGINT | Timestamp of the most recent auto refresh that was triggered  
auto_refresh_start_timestamp | BIGINT | Timestamp of the most recent auto refresh that was started  
auto_refresh_end_timestamp | BIGINT | Timestamp of the most recent auto refresh that was completed.  
auto_refresh_recent_status | TEXT | Status of the most recent auto refresh  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
