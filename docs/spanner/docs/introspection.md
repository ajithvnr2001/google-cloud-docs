---
url: https://docs.cloud.google.com/spanner/docs/introspection/
title: Spanner built-in statistics tables overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:24.505307+00:00
---

# Spanner built-in statistics tables overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/introspection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Spanner built-in statistics tables overview Stay organized with collections  Save and categorize content based on your preferences. 

Built-in statistics tables for Spanner help you investigate issues in your database. You can query these tables to gain insight about queries, transactions, and reads. The following list of built-in statistics tables (or introspection tools) are available in Spanner:

  * Active partitioned DML statistics
  * Column operations statistics
  * Lock statistics
  * Oldest active queries statistics
  * Query statistics
  * Read statistics
  * Split statistics
  * Table operations statistics
  * Table sizes statistics
  * Transaction statistics
  * Vector index statistics



These tables access `SPANNER_SYS` data, which is available only through the following Spanner SQL interfaces:

  * A database's Spanner Studio page in the Google Cloud console.
  * The [`gcloud spanner databases execute-sql`](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql) command.
  * The [`executeSql`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql) or the [`executeStreamingSql`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeStreamingSql) method.



You can't use other single read methods to query the `SPANNER_SYS` tables.

## API methods included for each tool

In Spanner there is some overlap between [transactions](https://docs.cloud.google.com/spanner/docs/transactions), [reads](https://docs.cloud.google.com/spanner/docs/reads) and [queries](https://docs.cloud.google.com/spanner/docs/reads#single_read_methods). Therefore, it might not be clear which API methods are included when compiling results for each introspection tool. The following table lists the main API methods and their relationship to each tool.

API Methods | Transaction Modes | Query statistics | Oldest active queries | Read statistics | Transaction statistics | Lock statistics  
---|---|---|---|---|---|---  
Read, StreamingRead | Read-only transaction1 | No | No | **Yes** | No | No  
Read-write transaction | No | No | **Yes** | **Yes** | **Yes**  
ExecuteSql, ExecuteStreamingSql | Read-only transaction1 | **Yes 2** | **Yes 2** | No | No | No  
Read-write transaction | **Yes** | **Yes** | No | **Yes** | **Yes**  
ExecuteBatchDml | Read-write transactions | **Yes** 3 | **Yes** 4 | No | **Yes** | **Yes**  
Commit | Read-write transactions (DML5, Mutations6) | No | No | No | **Yes** | **Yes**  
  
Notes:

1 Read-only transactions are not included in transaction statistics or lock statistics. Only read-write transactions are included in transaction statistics and lock statistics.

2 Queries run with the PartitionQuery API aren't included in [oldest active queries statistics](https://docs.cloud.google.com/spanner/docs/introspection/oldest-active-queries).

3 A batch of DML statements appear in the query statistics as a single entry.

4 Statements within the batch will appear in oldest active queries, rather than the entire batch.

5 Uncommitted DML operations are not included in transaction statistics.

6 Empty mutations that are effectively no-op are not included in transaction statistics.

## Active partitioned DML statistics

[Active partitioned data manipulation language (DML) statistics](https://docs.cloud.google.com/spanner/docs/introspection/active-partitioned-dmls) provide real time progress for the partitioned DMLs that are active in your database.

## Column operations statistics

You can use [Column operations statistics](https://docs.cloud.google.com/spanner/docs/introspection/column-operations-statistics) to do the following:

  * Monitor the statistics of columns in your table.
  * Find trends in how your table columns are used.



## Lock statistics

[Lock statistics](https://docs.cloud.google.com/spanner/docs/introspection/lock-statistics) can be used to investigate lock conflicts in your database. Used with transactions statistics, you can find transactions that are causing lock conflicts by trying to acquire locks on the same cells at the same time.

You can visualize these metrics on a time series by using the [Lock insights](https://docs.cloud.google.com/spanner/docs/use-lock-and-transaction-insights#lock-insights) dashboard. The pre-built dashboard helps you view the lock wait time and confirm if latencies are due to lock contentions with high lock wait time.

## Oldest active queries statistics

Sometimes you want to look at the current workload on the system by examining running queries. Use the [Oldest active queries](https://docs.cloud.google.com/spanner/docs/introspection/oldest-active-queries) tool to investigate long running queries that may be having an impact on database performance. This tool tells you what the queries are, when they started running and to which session they belong.

Change stream queries are not included in oldest active queries.

## Query statistics

When investigating issues in your database, it is helpful to know which queries are expensive, run frequently or scan a lot of data.

[Query statistics](https://docs.cloud.google.com/spanner/docs/introspection/query-statistics) are aggregated statistics for queries (including DML statements and [change stream](https://docs.cloud.google.com/spanner/docs/change-streams) queries), gathered in 1, 10, and 60 minute intervals. Statistics are collected for statements that completed successfully as well as those that failed, timed out, or were canceled by the user.

The statistics include highest CPU usage, total query execution counts, average latency, most data scanned, and additional basic query statistics. Use these statistics to help identify expensive, frequently run or data-intensive queries.

You can visualize these metrics on a time series by using [Query insights](https://docs.cloud.google.com/spanner/docs/using-query-insights#the_dashboard) dashboards. These pre-built dashboards help you view spikes in CPU utilization and identify inefficient queries.

## Read statistics

[Read statistics](https://docs.cloud.google.com/spanner/docs/introspection/read-statistics) can be used to investigate the most common and most resource-consuming reads on your database using the Spanner [Reads API](https://docs.cloud.google.com/spanner/docs/reads). These statistics are collected and stored in 3 different time intervals - minute, 10 minutes and an hour. For each time interval, Spanner tracks the reads that are using the most resources.

Use read statistics to find out the combined resource usage by all reads, find the most CPU consuming reads, and find out how a specific read's frequency changes over time.

## Split statistics

You can [debug hotspots in your database](https://docs.cloud.google.com/spanner/docs/introspection/hot-split-statistics) to find splits in the database that are _warm_ or _hot_ , meaning that a high percentage of the load on a split is constrained by the available resources. You can view statistics for splits that had the highest split CPU usage scores over the last 6 hours, by 1-minute intervals.

## Table operations statistics

You can use [Table operations statistics](https://docs.cloud.google.com/spanner/docs/introspection/table-operations-statistics) to do the following:

  * Monitor the usages of your tables and indexes in your database.
  * Find trends in the usage of your tables and indexes.
  * Identify changes in traffic.



Also, you can correlate the changes in your table storage with the changes in your write traffic.

## Table sizes statistics

You can use [Table sizes statistics](https://docs.cloud.google.com/spanner/docs/introspection/table-sizes-statistics) to monitor the historical sizes of the tables and indexes in your database.

Use table sizes statistics to find trends in the sizes of your tables, indexes, and change stream tables. You can also keep a track of your biggest tables and indexes.

Please note that this feature provides a historical perspective only. It is not for real-time monitoring.

## Transaction statistics

You can use [Transaction statistics](https://docs.cloud.google.com/spanner/docs/introspection/transaction-statistics) to investigate transaction-related issues. For example, you can check for slow-running transactions that might be causing contention or identify changes in transaction shapes that are leading to performance regressions. Each row contains statistics of all transactions executed over the database during 1, 10, and 60 minute intervals.

You can visualize these metrics on a time series by using the [Transaction insights](https://docs.cloud.google.com/spanner/docs/use-lock-and-transaction-insights#txn-insights) dashboard. The pre-built dashboard helps you view the latencies in transactions and identify problematic transactions.

## Vector index statistics

You can use [vector index statistics](https://docs.cloud.google.com/spanner/docs/introspection/vector-index-statistics) to review the performance of your vector index, identify areas for improvement, and tune your index based on the metrics provided.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
