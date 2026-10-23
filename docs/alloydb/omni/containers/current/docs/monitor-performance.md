---
url: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/monitor-performance/
title: Monitor AlloyDB Omni database performance \u00a0|\u00a0 AlloyDB Omni using containers: Current (18.4.0) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:52:06.681493+00:00
---

# Monitor AlloyDB Omni database performance  |  AlloyDB Omni using containers: Current (18.4.0)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/current/docs/monitor-performance/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/overview)



Send feedback 

#  Monitor AlloyDB Omni database performance Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/monitor-performance)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/monitor-performance)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/monitor-performance)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/monitor-performance)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/monitor-performance)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/monitor-performance)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/monitor-performance)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/monitor-performance)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/monitor-performance)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/monitor-performance)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/monitor-performance)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/monitor-performance)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/monitor-performance)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/monitor-performance)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/monitor-performance)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/monitor-performance)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/monitor-performance)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/monitor-performance)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/monitor-performance)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/monitor-performance)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/monitor-performance)

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

This page describes how to monitor your AlloyDB Omni database performance using PostgreSQL observability scripts.

## View state of connected processes and wait events

You can determine any processes connected to your AlloyDB Omni instance as well as any backends that are waiting for activity by querying the `pg_stat_activity` view.
    
    
    SELECT
        pid,
        datname,
        age(backend_xid) AS age_in_xids,
        now() - xact_start AS xact_age,
        now() - query_start AS query_age,
        state,
        wait_event_type,
        wait_event,
        query_id,
        query
    FROM
        pg_stat_activity
    WHERE
        state != 'idle'
        AND pid <> pg_backend_pid()
    ORDER BY
        4 DESC
    LIMIT 10;
    

## View largest tables

You can determine the size of your largest tables by querying the `pg_stat_user_tables` view.
    
    
    SELECT
        oid,
        oid::regclass table_name,
        pg_size_pretty(pg_relation_size(oid)),
        relpages,
        s.seq_scan,
        s.idx_scan
    FROM
        pg_class,
        pg_stat_user_tables s
    WHERE
        s.relid = oid
        AND oid > 16383
        AND relpages > 100
        AND relkind = 'r'
    ORDER BY
        relpages DESC
    LIMIT 20;
    

## View top sequential scans

You can view the top sequential scans by querying the `pg_stat_user_tables` view.
    
    
    SELECT
        relid,
        relname,
        seq_scan,
        pg_size_pretty(pg_relation_size(relid))
    FROM
        pg_stat_user_tables
    ORDER BY
        seq_scan DESC
    LIMIT 15;
    

## View top index scans

You can view the top index scans by querying the `pg_stat_user_tables` view.
    
    
    SELECT
        relid,
        relid::regclass table_name,
        idx_scan,
        pg_size_pretty(pg_relation_size(relid))
    FROM
        pg_stat_user_tables
    WHERE
        idx_scan > 10
    ORDER BY
        idx_scan DESC
    LIMIT 15;
    

## View longest running transactions

You can view the longest running transactions by querying the `pg_stat_activity` view and checking the age of the transaction.
    
    
    SELECT
        pid,
        age(backend_xid) AS age_in_xids,
        now() - xact_start AS xact_age,
        now() - query_start AS query_age,
        state,
        query
    FROM
        pg_stat_activity
    WHERE
        state != 'idle'
    ORDER BY
        2 DESC
    LIMIT 10;
    

## Check vacuum progress

You can check the progress of vacuum operations by querying the `pg_stat_progress_vacuum` view and joining it with the `pg_stat_activity` view using process IDs.
    
    
    SELECT
      p.pid,
      now() - a.xact_start AS duration,
      coalesce(wait_event_type ||'.'|| wait_event, 'f') AS waiting,
      CASE
        WHEN a.query ~*'^autovacuum.*to prevent wraparound' THEN 'wraparound'
        WHEN a.query ~*'^vacuum' THEN 'user'
      ELSE
        'regular'
      END AS mode,
      p.datname AS database,
      p.relid::regclass AS table,
      p.phase,
      pg_size_pretty(p.heap_blks_total * current_setting('block_size')::int) AS table_size,
      pg_size_pretty(pg_total_relation_size(relid)) AS total_size,
      pg_size_pretty(p.heap_blks_scanned * current_setting('block_size')::int) AS scanned,
      pg_size_pretty(p.heap_blks_vacuumed * current_setting('block_size')::int) AS vacuumed,
      round(100.0 * p.heap_blks_scanned / p.heap_blks_total, 1) AS scanned_pct,
      round(100.0 * p.heap_blks_vacuumed / p.heap_blks_total, 1) AS vacuumed_pct,
      p.index_vacuum_count,
      round(100.0 * p.dead_tuple_bytes / p.max_dead_tuple_bytes,1) AS dead_pct
    FROM pg_stat_progress_vacuum p
    JOIN pg_stat_activity a using (pid)
    ORDER BY now() - a.xact_start DESC;
    

## View asynchronous queries

To view queries that are running asynchronously, you can query the `pg_stat_activity` view and filter for queries that are not the leader process.
    
    
    SELECT
        query,
        leader_pid,
        array_agg(pid) FILTER (WHERE leader_pid != pid) AS members
    FROM
        pg_stat_activity
    WHERE
        leader_pid IS NOT NULL
    GROUP BY
        query,
        leader_pid;
    

## View blocking lock SQL

You can view activity that is blocked by querying the `pg_locks` view and joining it with the `pg_stat_activity` view.
    
    
    SELECT blocked_locks.pid     AS blocked_pid,
           blocked_activity.usename  AS blocked_user,
           blocking_locks.pid     AS blocking_pid,
           blocking_activity.usename AS blocking_user,
           blocked_activity.query    AS blocked_statement,
           blocked_activity.wait_event AS blocked_wait_event,
           blocking_activity.wait_event AS blocking_wait_event,
           blocking_activity.query   AS current_statement_in_blocking_process
     FROM  pg_catalog.pg_locks         blocked_locks
      JOIN pg_catalog.pg_stat_activity blocked_activity  ON blocked_activity.pid = blocked_locks.pid
      JOIN pg_catalog.pg_locks         blocking_locks
          ON blocking_locks.locktype = blocked_locks.locktype
          AND blocking_locks.database IS NOT DISTINCT FROM blocked_locks.database
          AND blocking_locks.relation IS NOT DISTINCT FROM blocked_locks.relation
          AND blocking_locks.page IS NOT DISTINCT FROM blocked_locks.page
          AND blocking_locks.tuple IS NOT DISTINCT FROM blocked_locks.tuple
          AND blocking_locks.virtualxid IS NOT DISTINCT FROM blocked_locks.virtualxid
          AND blocking_locks.transactionid IS NOT DISTINCT FROM blocked_locks.transactionid
          AND blocking_locks.classid IS NOT DISTINCT FROM blocked_locks.classid
          AND blocking_locks.objid IS NOT DISTINCT FROM blocked_locks.objid
          AND blocking_locks.objsubid IS NOT DISTINCT FROM blocked_locks.objsubid
          AND blocking_locks.pid != blocked_locks.pid
      JOIN pg_catalog.pg_stat_activity blocking_activity ON blocking_activity.pid = blocking_locks.pid
     WHERE NOT blocked_locks.granted;
    

## Determine `work_mem` and `temp_buffers` size effectiveness

To determine if your `work_mem` and `temp_buffers` are sized correctly for your needs, you can query `pg_stat_database` view and check the `postgres.log` file. Using `pg_stat_database`, execute the following query and if there is any growth in `temp_files` or `temp_bytes` between executions, then tuning is likely necessary for either `work_mem` or `temp_buffers`.
    
    
    SELECT
        datname,
        temp_files,
        temp_bytes
    FROM
        pg_stat_database;
    

After running this, check the `postgres.log` file to see if temporary files were used:

`LOG: [fd.c:1772] temporary file: path "base/pgsql_tmp/pgsql_tmp4640.1", size 139264`

The goal is to minimize the creation of temporary files, not completely prevent them from happening. This is because setting both `work_mem` and `temp_buffers` is a balance between available memory on the host and the number of connections that require the memory. Setting these parameters correctly requires understanding about each individual workload.

## View query performance using Query Insights

You can identify slow queries and high disk I/O statements using **Query Insights** in the AlloyDB Omni web user interface. **Query Insights** requires the `pg_stat_statements` extension to be enabled on your database. For setup instructions, see [Install the web UI](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/install-web-ui#optional-steps).

To view query performance metrics in the web UI, complete the following steps:

  1. [Connect to the web UI](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/connect-web-ui) and select your cluster.
  2. In the navigation menu, click **Query Insights**.
  3. Optional: Use the **Database** list to filter statements by a specific database or select **All databases**.
  4. Review the **Queries** table to analyze SQL execution statistics. Each row displays the following metrics along with the full SQL statement below the row: 
     * **Database name** : The logical database where the statement ran.
     * **Calls** : The total number of times the statement was executed.
     * **Rows** : The total number of rows retrieved or affected by the statement.
     * **Execution time: mean** : The average execution time per call.
     * **Execution time: total** : The cumulative execution time across all calls.
     * **Shared block hit** : The total number of shared buffer cache hits.
     * **Shared block read** : The total number of shared blocks read from disk.
     * **Query type** : Categorizes the query performance impact, such as `Slow query` or `High disk IO`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
