---
url: https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views/
title: Continuous materialized views \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:10.476381+00:00
---

# Continuous materialized views  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/continuous-materialized-views/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Continuous materialized views

This document provides an overview of continuous materialized views and common use cases for them. Before you read this page, you should be familiar with the [Bigtable overview](https://docs.cloud.google.com/bigtable/docs/overview).

In Bigtable, a _continuous materialized view_ is the result of a continuous, fully-managed background process. This process uses a SQL query that you provide to create and maintain a precomputed table that Bigtable updates incrementally as the source data changes. The SQL query can include aggregations and transformations on the underlying Bigtable table.

Data in a continuous materialized view includes the following:

  * Aggregated or transformed values that are derived from data in the source table
  * Unaggregated values that define the grouping key



Continuous materialized views let you pre-aggregate your data as you ingest it. Additionally, a continuous materialized view has a different schema than its source table, presenting the source-table data in a structure that is optimized for queries with different lookup patterns than queries used on the source table.

The following are key characteristics of continuous materialized views in Bigtable:

  * **Zero maintenance** : A continuous materialized view is precomputed in the background. Data changes to the source table, including updates and deletes, are automatically propagated in the background to the continuous materialized view, with no user action required.
  * **SQL development patterns** : Continuous materialized views are based on GoogleSQL for Bigtable queries, including SQL functions, filters, and aggregations. While the functions are deterministic by default, for limited use cases, you can opt in to use a curated set of non-deterministic functions.
  * **Synchronization with garbage collection** : A continuous materialized view stays in sync with the garbage collection policies of its source table, automatically updating as table data expires or is deleted.
  * **Read and write latency are unaffected** : A continuous materialized view has minimal impact on performance on the source table when the instance's clusters are adequately provisioned or use autoscaling.
  * **Eventually consistent** : Continuous materialized views are computed in the background. Updates to a continuous materialized view might be delayed, but the continuous materialized results are always consistent over time.



The row key, column qualifier, and column values that you use to define a continuous materialized view are treated as service data. For this reason, don't create a continuous materialized view using row key, column qualifier, or column values that contain [sensitive information](https://docs.cloud.google.com/bigtable/docs/schema-design#privacy). For information about how service data is handled, see the [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice).

You can create a continuous materialized view using the Google Cloud CLI, the Bigtable Studio query editor in the Google Cloud console, or the Bigtable client libraries for Java and Go.

You can read from a continuous materialized view by using the following:

  * Bigtable Studio query editor
  * The Bigtable [client libraries that support SQL queries](https://docs.cloud.google.com/bigtable/docs/googlesql-overview#client-libraries)
  * `ReadRows` API call using the Bigtable client libraries for Java and Go



For more information, see [Reading from a continuous materialized view](https://docs.cloud.google.com/bigtable/docs/reads#reads-continuous-materialized-views).

## When to use continuous materialized views

Continuous materialized views let you define a new representation of your Bigtable data using SQL. After it's been created, a continuous materialized view continually and automatically restructures data from the source table into the format defined by the SQL query. Then, instead of querying your table and transforming or aggregating the data after you read it, you can query the continuous materialized view.

Continuous materialized views can improve query performance for the following use cases:

  * **Data pre-aggregation** : You can use a continuous materialized view to aggregate incoming data across rows. This lets you retrieve summarized and aggregated data, such as metrics for dashboards, quickly.
  * **Automation of lambda and kappa architectures** : If your application requires a mix of real-time streaming pipeline data and batch pipeline data that contains historical data, then use continuous materialized views. These views provide a view of all data sources that is updated over time to reflect changes in the underlying data, without the need for additional stream processing tools or custom ETL jobs.
  * **Secondary access patterns** : Continuous materialized views create an alternative representation of your data. This representation can be optimized for queries with different lookup patterns than those that you use in queries against the source table. This makes continuous materialized views a powerful tool for creating what's effectively an asynchronous secondary index on your data. For more information about these patterns, see [Create an asynchronous secondary index](https://docs.cloud.google.com/bigtable/docs/asynchronous-secondary-index).



To compare continuous materialized views with other types of Bigtable views, see [Tables and views](https://docs.cloud.google.com/bigtable/docs/tables-and-views).

### When to use counters

Another way to pre-aggregate your data is by creating _distributed counters_ using [aggregate cells](https://docs.cloud.google.com/bigtable/docs/reference/data/rpc/google.bigtable.v2#aggregate).

Writes to aggregate cells are immediately readable from the cluster it is written to. Continuous materialized views are processed after data is written and eventually become consistent with the source table.

Use counters instead of continuous materialized views for the following:

  * Aggregations that don't require filters and don't need to be across rows.
  * If you need to immediately read your writes from the cluster they are written to.



Use continuous materialized views when you want to do the following:

  * Generate a different key for queries against your aggregations.
  * See changes to the base table reflected in your aggregations.
  * Automatically combine data across multiple rows.



Use a combination of counters and continuous materialized views for use cases like when you want to do the following:

  * Capture fresh metrics in an aggregate cell but keep historical rollups of those metrics.
  * Combine metrics in a continuous materialized view.



## Resource provisioning and performance

Ongoing processing for continuous materialized views occurs as a low-priority background job. As a result, it has a minimal impact on application performance and read and write latency on the source table, provided your clusters are adequately sized.

As a best practice to make sure the data in the continuous materialized view remains fresh, enable [autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling) for the clusters in the instance that contains your continuous materialized view. Autoscaling automatically adds enough nodes to handle the processing overhead and then removes them when they're no longer needed. This helps to ensure that enough compute capacity is available during the execution of the continuously running SQL query. Autoscaling can also ensure that you have enough nodes to handle your continuous materialized views' storage needs.

Continuous materialized views count toward the [1,000 tables-per-instance limit](https://docs.cloud.google.com/bigtable/quotas#limits-tables-per-instance).

### Creating continuous materialized views on existing tables

When you create a continuous materialized view for an existing table, Bigtable starts a one-time process that populates the view with existing table data. This process is known as _initial population_. The time required for the initial population depends on the size of the table and the complexity of the query. By default, you can't query the view during the initial population. However, if your use case can tolerate incomplete data, such as during application development, then you can use the `allow_incomplete_view` query hint to query the view before the population finishes. During this time, if the view performs aggregation, then the aggregates returned might reflect only some of the data. For more information, see [Read data during initial population](https://docs.cloud.google.com/bigtable/docs/reads#read-during-initial-population).

This initial population runs as a low-priority background job to minimize the effect on your cluster's performance. For large tables, you can temporarily add more nodes to your cluster to accelerate view creation.

The following diagram shows the process of creating continuous materialized views:

![The process of creating continuous materialized
    views in Bigtable.](https://docs.cloud.google.com/static/bigtable/img/cmv-arch-text-as-paths.svg) **Figure 1.** The process of creating continuous materialized views in Bigtable (click to enlarge).![](https://docs.cloud.google.com/static/bigtable/img/cmv-arch-text-as-paths.svg)

For example, assume that your source table contains rows with keys that follow the pattern `advertiser_id#region#ad_id` and one column family, `data`, that includes a `spend_usd` column qualifier with numeric data representing ad spend:

Row key | `data:spend_usd`  
---|---  
`adv1#us-east#ad1` | 100  
`adv1#us-west#ad2` | 150  
`adv2#us-east#ad3` | 200  
  
If you use the following query to define a continuous materialized view of this table, the initial population of 1 TB of data completes in approximately three hours on a 175-node cluster.
    
    
    SELECT
              SPLIT(_key, "#")[SAFE_OFFSET(0)] AS advertiser_id,
              count(*) AS count,
              sum(cast(cast(data['spend_usd'] as string) as int64)) as sum_spend
            FROM `$0`
            GROUP BY advertiser_id
    

Since Bigtable scales linearly, a 175-node cluster processes 2 TB of data in approximately six hours and 10 TB in approximately 30 hours, assuming that the data has a similar shape. To reduce the time required for the initial population, you can temporarily [add more nodes to your cluster](https://docs.cloud.google.com/bigtable/docs/modifying-instance#nodes) or, if you are using autoscaling, temporarily [increase the maximum node count](https://docs.cloud.google.com/bigtable/docs/modifying-instance#change-autoscaling).

### Non-deterministic SQL functions

By default, continuous materialized views only support deterministic functions to ensure consistent results across all clusters in an instance. However, you can opt in to use non-deterministic functions, such as `CLUSTER_ATTRIBUTE()`, to filter data by the cluster that processes it. For more information, see [Non-deterministic queries](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-view-queries#non-deterministic-queries).

To use these functions, when you create the continuous materialized view, you must acknowledge potential semantic differences. For more information, see [Create a continuous materialized view](https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views#create).

## Storage

For each continuous materialized view, Bigtable stores the following:

  * The data in the continuous materialized view
  * Intermediate storage



Like any Bigtable table, a continuous materialized view exists on all clusters in the instance that contains it. The clusters in your instance must have enough nodes to store the source table and any continuous materialized views based on the table. Autoscaling lets your clusters scale up or down in size as storage requirements change.

A continuous materialized view must be created in the same instance as the source table even though storage for the continuous materialized view is distinct from the source table.

### Continuous materialized view storage

A continuous materialized view contains data resulting from the SQL query the continuous materialized view is based on. This means that it contains aggregated values defined by aggregation clauses in the SQL query and unaggregated values that define the grouping key.

### Intermediate storage

To support the synchronization of a continuous materialized view with its source table, Bigtable uses _intermediate storage_ to store copies of the data that it needs to incrementally update the continuous materialized view.

The amount of data in intermediate storage is roughly equivalent to the amount of data that is scanned in the source table to generate the result of the SQL query that defines the continuous materialized view. For example, if your query aggregates data across the entire table, Bigtable holds the equivalent of the entire table in intermediate storage. A continuous materialized view based on a query of specific row key ranges or columns keeps only those rows or columns in intermediate storage.

Intermediate storage persists for the life of the continuous materialized view to efficiently support incremental updates to the view and propagate deletes from the source table to the continuous materialized view. You can't read the data in intermediate storage. For insights into your intermediate storage usage, see Continuous materialized view metrics.

## Replication

In instances that use replication, continuous materialized views aren't replicated in the same way that tables are. Instead, each cluster in an instance processes the continuous materialized view independently, using its own copy of the source table. This means, for example, that data that is written to a source table on cluster A is replicated to the table on cluster B and then to the continuous materialized view on cluster B.

## Costs

There is no per-resource cost for using continuous materialized views. However, the creation and syncing of continuous materialized views require processing and storage, and you are charged at the standard rates. You can expect to see increases in the following when you create a continuous materialized view:

  * **Storage** \- You are charged to store the data in the continuous materialized view and for intermediate storage. For more information, see Storage.
  * **Compute** \- The ongoing syncing of the source table and the continuous materialized view requires CPU processing, and your clusters might need more nodes to handle the additional background work.



At the same time, you might see some processing on the source table decrease, such as when you are no longer conducting range scans of the data to perform repeated computations and other less efficient queries. You also might eliminate the need to run pipeline jobs, such as Dataflow or Spark, to aggregate source data and write it back to Bigtable.

For more information about pricing, see [Bigtable pricing](https://cloud.google.com/bigtable/pricing). For metrics that can help you monitor your continuous materialized view usage, see Metrics.

## Metrics

A continuous materialized view reports several key metrics to Cloud Logging that you can use to monitor your continuous materialized views.

**Metric** | **Description**  
---|---  
`materialized_view/max_delay` | Upper bound of processing delay for the continuous materialized view  
`materialized_view/storage` | Amount of data used for the continuous materialized view storage in bytes  
`materialized_view/intermediate_storage` | Amount of data used by intermediate processing for the continuous materialized view in bytes  
`table/materialized_view_intermediate_storage` | Amount of data used by intermediate processing for continuous materialized views defined on this table  
`materialized_view/user_errors` | Number of errors from user data for the continuous materialized view. User errors prevent data from propagating to the view.  
`materialized_view/system_errors` | Number of errors from system for the continuous materialized view  
  
You can also use many Bigtable table metrics to monitor a continuous materialized view, using the continuous materialized view ID in place of the table ID. In particular, continuous materialized views are included in the breakdown for [CPU metrics](https://docs.cloud.google.com/bigtable/docs/monitoring-instance#cpu), which can help you understand their impact. Bigtable metrics for requests per second, latency, and throughput are generated when you read a continuous materialized view using the Data API's `ReadRows` method. For more information, see [Metrics](https://docs.cloud.google.com/bigtable/docs/metrics).

To get started with Cloud Logging, see [Query and view logs overview](https://docs.cloud.google.com/logging/docs/log-analytics).

## Limitations

  * You can create up to 50 continuous materialized views per instance.
  * You can create up to 5 continuous materialized views per table. If necessary, you can request an increase to this limit by contacting [Cloud Customer Care](https://docs.cloud.google.com/bigtable/docs/support/getting-support).
  * When you create a view without a specified `_key`, selected columns in the source table must not be `NULL`. For more information, see [Row keys defined by `GROUP BY` or `ORDER BY` clause](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-view-queries#group-by-order-by-as-row-key).
  * You can't modify the SQL query that defines a continuous materialized view. You must delete the continuous materialized view and create a new one with your changes.
  * You can't create a continuous materialized view of another continuous materialized view or of a logical view.
  * The query that defines a continuous materialized view can't use `SELECT *`.
  * You can't configure garbage collection policies for a continuous materialized view. All data retention is governed by the garbage collection policies for the source table and garbage collection of the source is automatically reflected in the continuous materialized view.



## What's next

  * [Continuous materialized view query](https://docs.cloud.google.com/bigtable/docs/continuous-materialized-view-queries)
  * [Create and manage continuous materialized views](https://docs.cloud.google.com/bigtable/docs/manage-continuous-materialized-views)
  * [Create an asynchronous secondary index](https://docs.cloud.google.com/bigtable/docs/asynchronous-secondary-index)
  * [Schema design best practices](https://docs.cloud.google.com/bigtable/docs/schema-design)
  * [Distributed counting in Bigtable](https://cloud.google.com/blog/products/databases/distributed-counting-with-bigtable)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
