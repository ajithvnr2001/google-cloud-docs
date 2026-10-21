---
url: https://docs.cloud.google.com/sql/docs/postgres/optimize-cpu-usage/
title: Optimize high CPU usage in instances \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:14.526352+00:00
---

# Optimize high CPU usage in instances  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/optimize-cpu-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Optimize high CPU usage in instances Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/optimize-cpu-usage "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-cpu-usage "View this page for the SQL Server database engine")

High CPU utilization adversely affects the performance of your instance. Any activity that's performed on the instance uses CPU. Hence, if there's a high CPU utilization notice, you should first identify the root cause of the issue, whether that's poorly written queries, long running transactions, or any other database activity.

This document describes the ways to identify CPU bottlenecks in an instance and mitigate the CPU utilization issues in the instance.

## Identify the CPU bottlenecks

The following sections discuss different CPU scenarios.

### Use query insights to identify queries that have high CPU consumption

[Query insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights) helps you detect, diagnose, and prevent query performance problems for Cloud SQL databases.

### Use the `pg_proctab` extension

Use the [pg_proctab](https://docs.cloud.google.com/sql/docs/postgres/extensions#pg_proctab) extension with the combination of the `pg_top` utility to get operating system outputs that give per process CPU utilization information.

### Use queries

The following sections discuss different queries you can use.

#### Identify the active connections by state

Each active connection to the database takes some amount of CPU, so if the instance has a high number of connections, cumulative utilization could be high. Use the following query to get the information about the number of connections by state.
    
    
    SELECT
      state,
      usename,
      count(1)
    FROM
      pg_stat_activity
    WHERE
      pid <> pg_backend_pid()
    group by
      state,
      usename
    order by
      1;
    

The output looks similar to the following:
    
    
            state        |    usename    | count
    ---------------------+---------------+-------
     active              | ltest         |   318
     active              | sbtest        |    95
     active              |               |     2
     idle                | cloudsqladmin |     2
     idle in transaction | ltest         |    32
     idle in transaction | sbtest        |     5
                         | cloudsqladmin |     3
                         |               |     4
    (8 rows)
    
    

If the active connections count is high, check for long running queries or wait events that are blocking the queries from executing.

If the idle connection count is high, execute the following query to terminate the connections, after taking the necessary approvals.
    
    
    SELECT
      pg_terminate_backend(pid)
    FROM
      pg_stat_activity
    WHERE
      usename = 'sbtest'
      and pid <> pg_backend_pid()
      and state in ('idle');
    

You can also terminate the connections individually with `pg_terminate_backend` using the following query:
    
    
    SELECT pg_terminate_backend (<pid>);
    

Here, you can obtain the PID from `pg_stat_activity`.

#### Identify the long running connections

Here's an example of a query that returns long running queries. In this case, you can identify the queries that have been active for more than 5 minutes.
    
    
    SELECT
      pid,
      query_start,
      xact_start,
      now() - pg_stat_activity.query_start AS duration,
      query,
      state
    FROM
      pg_stat_activity
    WHERE
      (
        now() - pg_stat_activity.query_start
      ) > interval '5 minutes' order by 4 desc;
    
    

#### Review the explain plan to identify poorly written queries

Use the EXPLAIN PLAN to investigate a poorly written query and rewrite the query, if necessary. Optionally, consider cancelling the long running query with the following command with necessary approvals.
    
    
    SELECT pg_cancel_backend(<pid>);
    

#### Monitor VACUUM activity

The AUTOVACUUM activity that clears the dead tuples is a CPU-intensive operation. If your instance uses PostgreSQL version 11 or later, use the following query to check if there's any active AUTOVACUUM or VACUUM activity in progress.
    
    
    SELECT
      relid :: regclass,
      pid,
      phase,
      heap_blks_total,
      heap_blks_scanned,
      heap_blks_vacuumed,
      index_vacuum_count,
      max_dead_tuples,
      num_dead_tuples
    FROM
      pg_stat_progress_vacuum;
    

Check if there's an ongoing VACUUM activity in an instance using the following query:
    
    
    SELECT
      pid,
      datname,
      usename,
      query
    FROM
      pg_stat_activity
    WHERE
      query like '%vacuum%';
    

Additonally, you can [optimize and troubleshoot VACUUM operations in PostgreSQL](https://cloud.google.com/solutions/optimizing-monitoring-troubleshooting-vacuum-operations-postgresql).

#### Add pg_stat_statements extension

Set up the `pg_stat_statements` extension to get enhanced dictionary information about instance activity.

#### Frequent checkpoints

Frequent checkpoints degrade performance. Consider adjusting the `checkpoint_timeout` flag if the PostgreSQL alert log reports the `checkpoint occurring too frequently` warning.

#### Gather statistics

Ensure that the query planner has the latest statistics about tables to choose the best plan for queries. The ANALYZE operation collects statistics about the contents of tables in the database, and stores the results in the pg_statistic system catalog. Subsequently, the query planner uses these statistics to help determine the most efficient execution plans for queries. The AUTOVACUUM process automatically analyzes the tables periodically, so run the following command to check if all the tables have been analyzed and have the latest metadata available to the planner.
    
    
    SELECT
      relname,
      last_autovacuum,
      last_autoanalyze
    FROM
      pg_stat_user_tables;
    
    

#### Inadequate system settings

There are other factors and flag settings or system factors that influence the performance of your query. Run the following query to check the wait events and wait event type to get the insights about the performance of other system settings.
    
    
    SELECT
      datname,
      usename,
      (
        case when usename is not null then state else query end
      ) AS what,
      wait_event_type,
      wait_event,
      backend_type,
      count(*)
    FROM
      pg_stat_activity
    GROUP BY
      1,
      2,
      3,
      4,
      5,
      6
    ORDER BY
      1,
      2,
      3,
      4 nulls first,
      5,
      6;
    

The output looks similar to this:
    
    
     ..  | .. | what           | wait_event_type |      wait_event      | ..    | count
    -..--+-..-+----------------+-----------------+----------------------+-..----+------
     ..
     ..  | .. | active         | IO              | CommitWaitFlush      | ..    |   750
     ..  | .. | idle           | IO              | CommitWaitFlush      | ..    |   360
     ..  | .. | active         | LWLock          | BufferMapping        | ..    |   191
    
    

#### Monitor sequential scans

Frequent sequential scans over tables of more than a few tens of rows usually indicate a missing index. When the scans touch thousands or even hundreds of thousands of rows, it can cause excessive CPU usage.

Frequent sequential scans on tables with hundreds of thousands of rows can cause excessive CPU usage. Avoid sequential scans on such tables by creating necessary indexes.

Run the following query to check the number of times sequential scans are initiated on any table.
    
    
    SELECT
      relname,
      idx_scan,
      seq_scan,
      n_live_tup
    FROM
      pg_stat_user_tables
    WHERE
      seq_scan > 0
    ORDER BY
      n_live_tup desc;
    

Lastly, if the CPU is still high and you feel those queries are legitimate traffic then consider increasing the CPU resources in your instance to avoid database crash or downtime.

## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
