---
url: https://docs.cloud.google.com/alloydb/docs/improve-select-insert-performance-parallel-select/
title: Improve INSERT SELECT performance with parallel SELECT \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:17.547505+00:00
---

# Improve INSERT SELECT performance with parallel SELECT  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/improve-select-insert-performance-parallel-select/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Improve INSERT SELECT performance with parallel SELECT Stay organized with collections  Save and categorize content based on your preferences. 

Using parallel execution for the `SELECT` portion of an `INSERT INTO ... SELECT` query can improve AlloyDB for PostgreSQL query performance, especially for partitioned tables and complex queries.

By parallelizing the `SELECT` subplan, the database uses multiple worker processes to retrieve data. The database then inserts the retrieved data into the target table. This division of labor can lead to database performance improvements.

## How parallel query plans work in PostgreSQL

In PostgreSQL, the query optimizer can create a parallel plan for an entire query or part of a query. When a parallel plan is generated, it adds a `Gather` or `Gather Merge` node to the top of the plan.

This node coordinates multiple parallel worker processes. Each worker executes a part of the task, for example, scanning a portion of a table. The `Gather` node then collects the results from all workers and passes them on to the next stage of the query, or back to the client.

For example, the following query plan shows a `Gather` node that plans to use five worker processes for a parallel sequential scan on table `t1`.
    
    
    EXPLAIN SELECT * FROM t1;
    
                      QUERY PLAN
    -------------------------------------------------------------
     Gather  (cost=0.00..143359.76 rows=9999878 width=60)
       Workers Planned: 5
       ->  Parallel Seq Scan on t1  (cost=0.00..143359.76 rows=1999976 width=60)
    (3 rows)
    

## Parallel execution for INSERT...SELECT statements

AlloyDB improves `INSERT INTO ... SELECT` performance by using multiple worker processes to parallelize the `SELECT` statement. This division of labor can lead to database performance improvements. The query must be parallel-safe and there must be no conditions that prevent parallelization.

Many database operations use `INSERT INTO ... SELECT` statements to add new rows to a table. Often, the `SELECT` part of the statement is the most resource-intensive part of the query.

The functionality is controlled by the following configuration parameters:

  * `enable_parallel_select_for_insert_select`: enables or disables the feature . This parameter is on by default in PostgreSQL 14 and later.
  * `enable_parallel_select_for_insert_select_into_part_table`: enables or disables the feature that lets you insert into partitioned tables. This parameter is off by default in PostgreSQL 16 and later.



For the query planner to consider a parallel plan, the `INSERT SELECT` statement must be _parallel-safe_. This means that no part of the operation can contain functions or expressions that cannot be safely executed in parallel. If any part of the query is determined to be parallel unsafe, the optimizer falls back to a non-parallel plan. For more information, see [parallel-safety](https://www.postgresql.org/docs/current/parallel-safety.html#PARALLEL-SAFETY).

### Conditions that prevent parallel execution

The query optimizer doesn't use a parallel plan if the `INSERT SELECT` statement is considered parallel unsafe. The following conditions prevent parallelization:

  * The target table is a foreign table.
  * The query uses a modifiable Common Table Expression (CTE) that contains a data modification statement, for example, `DELETE`.
  * An index on the target table uses a parallel unsafe expression or function.
  * A column on the target table has a default value that uses a parallel unsafe function.
  * A trigger on the target table uses a parallel unsafe expression or function.
  * The target table has a DOMAIN column with a `CHECK` constraint that uses a parallel unsafe function.
  * A `CHECK` constraint on the target table contains a parallel unsafe expression or function.
  * The target table is a partitioned table and `enable_parallel_select_for_insert_select_into_part_table` is disabled.



## Before you begin

This document assumes that you have an AlloyDB database. To create a database, see [Create a cluster and its primary instance](https://docs.cloud.google.com/alloydb/docs/cluster-create) and [Create and manage a database](https://docs.cloud.google.com/alloydb/docs/database-create).

### Required roles

To get the permissions that you need to change database flags at the session level, ask your administrator to grant you the AlloyDB Database User ([`roles/alloydb.databaseUser`](https://docs.cloud.google.com/alloydb/docs/reference/iam-roles-permissions#roles)) Identity and Access Management (IAM) role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Enable parallel execution parameters

To enable parallel execution for partitioned target tables, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Select a cluster from the list.

  3. In the navigation menu, click **AlloyDB Studio**.

  4. Sign into AlloyDB Studio using the name of your database, username, and password.

  5. Set the `enable_parallel_select_for_insert_select_into_part_table` GUC to `on`.
         
         SET enable_parallel_select_for_insert_select_into_part_table = on;
         

After you enable the GUC parameter, the query planner automatically considers parallel plans for `INSERT INTO ... SELECT` statements where the target is a partitioned table, provided that the query is determined to be parallel-safe.

The following example results in an EXPLAIN plan that shows a Gather node, which indicates that the `SELECT` from `source_table` is executed in parallel.
         
         -- Create a partitioned table
         CREATE TABLE part_table (a INT, b TEXT) PARTITION BY RANGE (a);
         CREATE TABLE part_table_1 PARTITION OF part_table FOR VALUES FROM (MINVALUE) TO (1000);
         CREATE TABLE part_table_2 PARTITION OF part_table FOR VALUES FROM (1000) TO (MAXVALUE);
         
         -- Create a source table
         CREATE TABLE source_table (c1 INT, c2 TEXT);
         INSERT INTO source_table SELECT i, 'value_' || i FROM generate_series(1, 2000) i;
         ANALYZE source_table;
         
         -- Enable the feature
         SET enable_parallel_select_for_insert_select_into_part_table = on;
         -- Optional for parallelizing the query with a small amount of data
         SET parallel_setup_cost=0;
         SET parallel_tuple_cost=0;
         SET min_parallel_table_scan_size=0;
         
         -- Run the insert with a parallelizable select
         EXPLAIN INSERT INTO part_table SELECT * FROM source_table;
         

This returns the following output:
         
         EXPLAIN (COSTS OFF) INSERT INTO part_table SELECT * FROM source_table;
                         QUERY PLAN                   
         -----------------------------------------------
         Insert on part_table
         ->  Gather
                 Workers Planned: 2
                 ->  Parallel Seq Scan on source_table
         (4 rows)
         




## Disable parallel execution parameters

To disable the parameters, follow these steps:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. Select a cluster from the list.

  3. In the navigation menu, click **AlloyDB Studio**.

  4. Sign into AlloyDB Studio using the name of your database, username, and password.

  5. To disable the `enable_parallel_select_for_insert_select` parameter, run the following SQL command:
         
         SET enable_parallel_select_for_insert_select = OFF;
         

  6. To disable the `enable_parallel_select_for_insert_select_into_part_table` parameter, run the following SQL command:
         
         SET enable_parallel_select_for_insert_select_into_part_table = OFF;
         




## Verify a parallel plan

You can verify that the optimizer is using a parallel plan by using the `EXPLAIN` command. Look for a `Gather` node and the `Workers Planned` or `Workers Launched` attributes in the query plan.

### Standard table example

In the following plan example, six worker processes are launched for a parallel hash join to execute the `SELECT` statement.
    
    
    EXPLAIN (ANALYZE)
    INSERT INTO t1 SELECT t2.* FROM t1, t2 WHERE t1.c1 != t2.c1 AND t1.c2 = t2.c2;
    
                                     QUERY PLAN
    ------------------------------------------------------------------------------------
     Insert on t1  (cost=1209138.00..12801765.49 rows=0 width=0) (actual time=16812.677..19337.150 rows=0 loops=1)
       ->  Gather  (cost=1209138.00..12801765.49 rows=99995407 width=24) (actual time=16812.674..19337.144 rows=0 loops=1)
             Workers Planned: 6
             Workers Launched: 6
             ->  Parallel Hash Join  (...)
    (...)
    

### Partitioned table example

The following example shows that, after you enable the feature for partitioned tables, the plan shows a `Gather` node with four planned workers for the `SELECT`.
    
    
    -- First, enable the feature for partitioned tables
    SET enable_parallel_select_for_insert_select_into_part_table = ON;
    
    -- Then, explain the query
    EXPLAIN (COSTS OFF) INSERT INTO part_table SELECT * FROM source_table;
                      QUERY PLAN                   
    -----------------------------------------------
     Insert on part_table
       ->  Gather
             Workers Planned: 2
             ->  Parallel Seq Scan on source_table
    (4 rows)
    

## What's next

  * Learn more about [parallel-safety](https://www.postgresql.org/docs/17/parallel-safety.html).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
