---
url: https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/
title: Optimize resources and isolate read queries with transparent query forwarding \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:42.372451+00:00
---

# Optimize resources and isolate read queries with transparent query forwarding  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/transparent-query-forwarding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Optimize resources and isolate read queries with transparent query forwarding Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Transparent query forwarding**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to enable, configure, and monitor transparent query forwarding in your AlloyDB for PostgreSQL instances. Transparent query forwarding is an intelligent resource optimization feature that allows the primary node to intercept read-only queries and selectively forward them to underutilized [read pool instances](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create) while maintaining read-your-writes consistency. Queries forwarded to the read pool yield results consistent with primary node execution.

![transparent query forwarding](https://docs.cloud.google.com/alloydb/images/tqf-diag.png)

**Note:** Queries are forwarded to in-region read pool instances. Queries are not forwarded to secondary clusters.

Transparent query forwarding is best-suited for the following scenarios:

  * Hybrid workloads (HTAP): you run reporting or analytical queries, with read-your-writes consistency, on the same database that handles transactions, and you want to prevent expensive reads from impacting write latency.
  * Monolithic applications: You want to use read pool capacity without refactoring your application to use separate reader and writer endpoints, while still requiring strict read-your-writes consistency.
  * Dynamic load management: You experience unpredictable spikes in read traffic and you want the database to automatically offload work to read pool nodes when the primary node is under heavy load with read-your-writes consistency.



## Before you begin

  * Make sure your AlloyDB cluster is compatible with PostgreSQL 17 or 18.

  * You must have at least one active read pool instance configured in your AlloyDB cluster. For information about creating or verifying read pool instances, see [Create a read pool instance in a cluster](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create) and [View instance details](https://docs.cloud.google.com/alloydb/docs/instance-view).

**Note:** If your cluster only has a primary or high availability (HA) setup without read pools, transparent query forwarding has no destination nodes available to receive forwarded queries.



### Required roles

  * Make sure that you connect using a [built-in database user](https://docs.cloud.google.com/alloydb/docs/database-users/built-in-authentication), such as `postgres`. [IAM-based authentication](https://docs.cloud.google.com/alloydb/docs/database-users/iam-authentication) isn't supported.



## Enable transparent query forwarding

Transparent query forwarding is disabled by default. You can enable it dynamically at the session level or the database level without restarting the database.

### Enable at the session level

To enable transparent query forwarding for your current session, run the following SQL command:
    
    
    SET alloydb.enable_query_forwarding = TRUE;
    

### Enable at the database level

To enable transparent query forwarding for a specific database, run the following SQL command:
    
    
    ALTER DATABASE DATABASE_NAME SET alloydb.enable_query_forwarding = ON;
    

Replace `DATABASE_NAME` with the name of your database.

**Note:** After you run the `ALTER DATABASE` command, transparent query forwarding is enabled for new connections to the database.

## Query eligibility conditions

  * Transparent query forwarding applies only to read-only `SELECT` statements.
  * The query must not take any row-level locks, such as those used in `SELECT ... FOR UPDATE`.
  * Transparent query forwarding has limited support for `SELECT` statements within multi-statement transactions.
  * Queries cannot reference temporary, unlogged, or catalog tables.
  * The query must adhere to the following function constraints: 
    * The query must not contain volatile functions or any user-defined functions (UDFs).
    * The query must not contain SQL value functions such as `CURRENT_DATE`, `LOCALTIME`, `USER`, or `CURRENT_SCHEMA`.
    * The query must not contain `NEXTVAL()` expressions.
    * The query cannot contain any SQL procedures or SQL functions.
  * All result columns must use data types that implement binary send and receive functions.
  * A query is only eligible for forwarding if its overhead cost is minimal compared to the query's total cost. This means queries using index scans are typically excluded, as their overhead usually exceeds the cost of the query itself.
  * Forwarding to a AlloyDB hot standby node is not supported. A AlloyDB hot standby node is a dedicated secondary node for high availability (HA) primary instances.
  * The query must use the [simple query protocol](https://www.postgresql.org/docs/17/protocol-flow.html#PROTOCOL-FLOW-SIMPLE-QUERY). Extended query protocol is not supported.



## Verify query eligibility with EXPLAIN

In the following example, `large_table` is a table in a database with many rows. To check whether a specific query is eligible for forwarding under your current configuration, run the `EXPLAIN` command:
    
    
    EXPLAIN SELECT count(*) FROM large_table t1, large_table t2;
    

If the query is eligible, the output includes a query forwarding status statement after the standard Postgres execution plan. If this statement is missing, then the query is not eligible for query forwarding and executes locally on the primary.
    
    
    Aggregate  (cost=25000.00..25000.01 rows=1 width=8)
      ->  Nested Loop  (cost=0.00..20000.00 rows=1000000 width=0)
            ... [Standard Postgres Plan Steps] ...
    Query Forwarding: Eligible. (overhead=1250.02)
    

In the output response, `Eligible` indicates that the query meets standard read-only SQL criteria and the cost-benefit analysis favors routing it to a read pool instance. The `overhead` parameter indicates the calculated planner cost of forwarding the query to a read pool instance, including the overhead of establishing the connection and restoring snapshots on the replica.

## Monitor query forwarding metrics

To verify that transparent query forwarding is working across your workload, you can track the following metric in Cloud Monitoring:

Metric | Description | Details  
---|---|---  
`alloydb.googleapis.com/internal/database/postgresql/workload/distributed/tqf_query_count` | The cumulative count of queries handled by transparent query forwarding. | **Display Name:** TQF query count  
**Metric Kind:** CUMULATIVE  
**Value Type:** INT64  
**Labels:**  
`status`: Query handling if transparent query forwarding is enabled. This label records one of the following values: 

  * `completed`: executed on a read pool instance.
  * `fallback`: executed on the primary.
  * `disqualified`: couldn't be forwarded.

  
  
## What's next

  * [Create a read pool instance in a cluster](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create)
  * [Monitor instances](https://docs.cloud.google.com/alloydb/docs/monitor-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
