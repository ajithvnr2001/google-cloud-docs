---
url: https://docs.cloud.google.com/sql/docs/mysql/optimize-cpu-usage/
title: Optimize high CPU usage in instances \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:30.403237+00:00
---

# Optimize high CPU usage in instances  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/optimize-cpu-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Optimize high CPU usage in instances Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/optimize-cpu-usage "View this page for the PostgreSQL database engine") | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-cpu-usage "View this page for the SQL Server database engine")

High CPU utilization in an instance can be caused by various reasons such as increase in workloads, heavy transactions, slow queries, and long running transactions.

The underprovisioned instance recommender analyzes CPU utilization. If the CPU utilization levels are at or over 95% for a significant amount of time within the last 30 days, the recommender alerts you and provides additional insights to help resolve the issue.

This document explains how to review and optimize a Cloud SQL for MySQL instance if that instance is identified by the underprovisioned instance recommender as having high CPU utilization.

## Use query insights to identify queries that have high CPU consumption

[Query insights](https://docs.cloud.google.com/sql/docs/mysql/using-query-insights) helps you detect, diagnose, and prevent query performance problems that might cause high CPU consumption for Cloud SQL databases.

## Use MySQL database auditing

Use [MySQL database auditing](https://docs.cloud.google.com/sql/docs/mysql/use-db-audit) to view memory and consumption of your instance.

## Recommendations

CPU utilization increases proportionally with workload. To reduce CPU utilization, check the running queries and optimize them. Here are a few steps to check the consumption of CPU.

  1. Check `Threads_running` and `Threads_connected`

Use the following query to see the number of active threads:
         
         > SHOW STATUS like 'Threads_%';
         

`Threads_running` is a subset of `Threads_connected`. The rest of the threads are idle. An increase in `Threads_running` would contribute to an increase in CPU usage. It's a good idea to check what's running on those threads.

  2. Check query states

Run the `SHOW PROCESSLIST` command to view the ongoing queries. It returns all the connected threads in order and their actively running SQL statement.
         
         mysql> SHOW [FULL] PROCESSLIST;
         

Pay attention to the state and duration columns. Check if there are many queries stuck on the same state.

     * If many threads show `Updating`, there might be record lock contention. See the next step.
     * If many threads show `Waiting` for table metadata lock, check the query to know the table and then look for a DDL (such as `ALTER TABLE`) that might hold the metadata lock. A DDL might also be waiting for table metadata lock if an early query, such as a long running `SELECT query`, is holding it.
  3. Check for record lock contention

When transactions hold locks on popular index records, they block other transactions requesting the same locks. This might get into a chained effect and cause a number of requests being stuck and an increase in the value of `Threads_running`. To diagnose lock contention, use the `information_schema.innodb_lock_waits` table.

The following query lists each blocking transaction and the numbers of associated blocked transactions.
         
         SELECT
           t.trx_id,
           t.trx_state,
           t.trx_started,
           COUNT(distinct w.requesting_trx_id) AS blocked_trxs
         FROM
           information_schema.innodb_lock_waits w
         INNER JOIN information_schema.innodb_trx t
            ON t.trx_id = w.blocking_trx_id
         GROUP BY t.trx_id,t.trx_state, t.trx_started
         ORDER BY t.trx_id;
         

Both a single large DML and many concurrent small DMLs might cause row lock contentions. You can optimize this from the application side by using the following steps:

     * Avoid long transactions because row locks are held until the transaction ends.
     * Break a single large DML to bite-sized DMLs.
     * Batch a single row DML into small chunks.
     * Minimize contention among threads; for example, if the application code uses a connection pool, assign an ID range to the same thread.
  4. Find long running transactions

     * Use `SHOW ENGINE INNODB STATUS`

In the **TRANSACTIONS** section, you can see all the open transactions ordered as earliest to oldest.
           
           mysql> SHOW ENGINE INNODB STATUS\G
           ……
           ------------
           TRANSACTIONS
           ------------
           …
           ---TRANSACTION 245762, ACTIVE 262 sec
           2 lock struct(s), heap size 1136, 1 row lock(s), undo log entries 1
           MySQL thread id 9210, OS thread handle 140262286128896, query id 202218 localhost root
           

Start with the oldest transactions and find answers to the following questions:

       * How long have these transactions been running?
       * How many lock struct(s) and row locks are present?
       * How many undo log entries are there?
       * What are the connecting hosts and users?
       * What is the ongoing SQL statement?
     * Use `information_schema.innodb_trx`

If `SHOW ENGINE INNODB STATUS` was truncated, an alternative way to examine all the open transactions is to use the `information_schema.innodb_trx` table:
           
           SELECT
            trx_id, trx_state,
            timestampdiff(second, trx_started, now()) AS active_secs,
            timestampdiff(second, trx_wait_started, now()) AS wait_secs, trx_tables_in_use,
            trx_tables_locked,
            trx_lock_structs,
            trx_rows_locked,
            trx_rows_modified,
            trx_query
           FROM information_schema.innodb_trx
           

If the transactions show the current long running statements, then you can decide to either stop these transactions to reduce the pressure on the server or wait for the critical transactions to complete. If the older transactions are not showing any activities, then go to the next step to find transaction history.

  5. Check SQL statements of the long running transactions

     * Use `performance_schema`

To use `performance_schema`, you must turn it on first. It is a change that requires an instance restart. After `performance_schema` is on, check that the instruments and consumers are enabled:
           
           SELECT * FROM setup_consumers where name like 'events_statements_history';
           SELECT * FROM setup_instruments where name like 'statement/sql/%';
           
           

If they aren't enabled, enable them:
           
           UPDATE setup_instruments SET ENABLED = 'YES', timed = 'YES' WHERE NAME LIKE 'statement/%';
           UPDATE setup_consumers SET ENABLED = 'YES' WHERE NAME LIKE 'events_statements%';
           

By default, each thread would keep the last 10 events defined by `performance_schema_events_statements_history_size`. Those are generally sufficient to locate the transaction in the application code. This parameter is not dynamic.

With the `mysql thread id`, which is `processlist_id`, query the history events:
           
           SELECT
            t.thread_id,
            event_name,
            sql_text,
            rows_affected,
            rows_examined,
            processlist_id,
            processlist_time,
            processlist_state
           FROM events_statements_history h
           INNER JOIN threads t
           ON h.thread_id = t.thread_id
           WHERE processlist_id = <mysql thread id>
           ORDER BY event_id;
           

     * Use slow query log

For debugging, you can capture all the queries that took more than `N` number of seconds into the slow query log. You can enable the slow query logs by editing the instance settings on the instance page of Google Cloud console or [`gcloud CLI`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/patch) and then see the logs using [logs viewer](https://docs.cloud.google.com/run/docs/logging) in the Google Cloud console or `gloud CLI`.

  6. Check semaphore contention

In a concurrent environment, mutex and read/write latch on shared resources might be the contention point, which slows the server performance. Moreover, if the semaphore wait time is more than 600 seconds, the system can crash to get out of the stall.

To view the semaphore contention, use the following command:
         
         mysql> SHOW ENGINE INNODB STATUS\G
         ----------
         SEMAPHORES
         ----------
         ...
           --Thread 140396021667584 has waited at row0purge.cc line 862 for 241.00 seconds the semaphore:
           S-lock on RW-latch at 0x30c03e8 created in file dict0dict.cc line 1183
           a writer (thread id 140395996489472) has reserved it in mode  exclusive
           number of readers 0, waiters flag 1, lock_word: 0
           Last time read locked in file row0purge.cc line 862
           Last time write locked in file /build/mysql-5.7-FFKPr6/mysql-5.7-5.7.22/storage/innobase/dict/dict0stats.cc line 2376
         ...
         

With each semaphore wait, the first line shows the thread that's waiting, the specific semaphore, and the length of time it has waited. If there are frequent semaphore waits when repeatedly running `SHOW ENGINE INNODB STATUS`, especially waits of more than a few seconds, it means that the system is running into concurrency bottlenecks.

There are different contention points in different workloads and configurations.

When the semaphores are often on btr0sea.c, the adaptive hash indexing might be the source of contention. Try to disable it using Google Cloud console or `gcloud CLI`.

  7. Optimize long `SELECT` queries

First, review the query. Identify the goal of the query and the best way to get the results. The best query plan is the one that minimizes data access.

     * Check the query execution plan:
    
    mysql> EXPLAIN <the query>;
    

See [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/execution-plan-information.html) to learn how to interpret the output and evaluate the query efficiency.

     * Use the right index

Check the key column to see if the expected index is used. If not, update the index statistics:
    
    mysql> analyze table <table_name>
    

Increase the number of sample pages that are used to calculate index statistics. To learn more, see the [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/innodb-performance-optimizer-statistics.html).

     * Make full use of the index

When using a multicolumn index, check the `key_len` columns to see if the index is fully leveraged to filter the records. The leftmost columns need to be equal comparisons, and the index can be used up to and including the first range condition.

     * Use optimizer hints

Another way to make sure the right index is used is to apply [index hint](https://dev.mysql.com/doc/refman/8.0/en/index-hints.html) and [hint for table join order](https://dev.mysql.com/doc/refman/8.0/en/join.html).

  8. Avoid a long history list with READ COMMITTED

The history list is the list of unpurged transactions in the undo tablespace. The default isolation level of a transaction is `REPEATABLE READ`, which requires a transaction to read the same snapshot throughout its duration. Hence, a `SELECT` query blocks the purging of undo log records that were made since the query (or transaction) started. A long history list thus slows the query performance. One way to avoid building a long history list is to change the transaction isolation level to `READ COMMITTED`. With `READ COMMITTED`, there is no longer the need to keep the history list for a consistent read view. You can change the transaction isolation level globally for all sessions, for a single session, or for the next single transaction. To learn more, see the [MySQL documentation](https://dev.mysql.com/doc/refman/5.7/en/set-transaction.html).

  9. Tune server configuration

There is a lot to say about server configuration. While the full story is beyond the scope of this document, it's worth mentioning that the server also reports various status variables that give hints on how well the related configurations are. For example:

     * Adjust `thread_cache_size` if `Threads_created/Connections` is big. A proper thread cache would reduce the thread creation time and help highly concurrent workload.
     * Adjust `table_open_cache` if `Table_open_cache_misses/Table_open_cache_hits` is not trivial. Having tables in the table cache saves query execution time and could make a difference in a highly concurrent environment.
  10. End an unwanted connection

You can stop the query if the query seems invalid or it isn't required anymore. To learn how to identify and end the MySQL thread, see [Manage database connections](https://docs.cloud.google.com/sql/docs/mysql/manage-connections#kill).




Lastly, if the CPU usage is still high and the queries form necessary traffic, then consider increasing the CPU resources in your instance to avoid database crash or downtime.

## What's next

  * [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/recommenders)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
