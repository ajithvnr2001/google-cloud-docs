---
url: https://docs.cloud.google.com/bigquery/docs/best-practices-storage/
title: Optimize storage for query performance \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:24.014918+00:00
---

# Optimize storage for query performance  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/best-practices-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Optimize storage for query performance

This page provides best practices for optimizing BigQuery storage for query performance. You can also [optimize storage for cost](https://docs.cloud.google.com/bigquery/docs/best-practices-costs#control-storage-cost). While these best practices are primarily focused on tables using BigQuery storage, they can be applied to external tables as well.

BigQuery stores data in columnar format. Column-oriented databases are optimized for analytic workloads that aggregate data over a very large number of records. As columns have typically more redundancy than rows, this characteristic allows for greater data compression by using techniques such as run-length encoding. For more information about how BigQuery stores data, see [Overview of BigQuery storage](https://docs.cloud.google.com/bigquery/docs/storage_overview). Optimizing BigQuery storage improves [query performance](https://docs.cloud.google.com/bigquery/docs/best-practices-performance-compute) and [controls cost](https://docs.cloud.google.com/bigquery/docs/best-practices-costs).

BigQuery provides details about the storage consumption of your resources. To view the table storage metadata, query the following `INFORMATION_SCHEMA` views:

  * [`INFORMATION_SCHEMA.TABLE_STORAGE`](https://docs.cloud.google.com/bigquery/docs/information-schema-table-storage)
  * [`INFORMATION_SCHEMA.TABLE_STORAGE_BY_ORGANIZATION`](https://docs.cloud.google.com/bigquery/docs/information-schema-table-storage-by-organization)
  * [`INFORMATION_SCHEMA.TABLE_STORAGE_USAGE_TIMELINE`](https://docs.cloud.google.com/bigquery/docs/information-schema-table-storage-usage)
  * [`INFORMATION_SCHEMA.TABLE_STORAGE_USAGE_TIMELINE_BY_ORGANIZATION`](https://docs.cloud.google.com/bigquery/docs/information-schema-table-storage-usage-by-organization)



## Cluster table data

**Best practice:** Create clustered tables.

To optimize storage for queries, start by clustering table data. By clustering frequently used columns, you can reduce the total volume of data scanned by the query. For information about how to create clusters, see [Create and use clustered tables](https://docs.cloud.google.com/bigquery/docs/creating-clustered-tables).

## Partition table data

**Best practice:** Divide large tables with partitions.

With partitions, you can group and sort your data by a set of defined column characteristics, such as an integer column, a time-unit column, or the ingestion time. Partitioning improves the query performance and control costs by reducing the number of bytes read by a query.

For more information about partitions, see [Introduction to partitioned tables](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).

## Use the table and partition expiration settings

**Best practice:** To optimize storage, configure the default expiration settings for [datasets](https://docs.cloud.google.com/bigquery/docs/updating-datasets#table-expiration), [tables](https://docs.cloud.google.com/bigquery/docs/managing-tables#updating_a_tables_expiration_time), and [partitioned tables](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#partition-expiration).

You can control storage costs and optimize storage usage by setting the default table expiration for newly created tables in a dataset. When a table expires, it gets deleted along with all of the data that the table contains. If you set the property when the dataset is created, any table created in the dataset is deleted after the expiration period. If you set the property after the dataset is created, only new tables are deleted after the expiration period.

For example, if you set the default table expiration to seven days, older data is automatically deleted after one week.

This option is useful if you need access to only the most recent data. It is also useful if you are experimenting with data and don't need to preserve it.

If your tables are partitioned by date, the dataset's default table expiration applies to the individual partitions. You can also control partition expiration using the `time_partitioning_expiration` flag in the bq command-line tool or the `expirationMs` configuration setting in the API. When a partition expires, data in the partition is deleted but the partitioned table is not dropped even if the table is empty.

For example, the following command expires partitions after three days:
    
    
    bq mk \
    --time_partitioning_type=DAY \
    --time_partitioning_expiration=259200 \
    project_id:dataset.table

## Aggregate long-term data

**Best practice:** Identify if row-level data needs to be stored long term, and if not, only store aggregated data long term.

In many cases, details contained in transactional or row-level data are useful in the short term, but are referenced less over the long term. In these situations, you can build aggregation queries to compute and store the metrics associated with this data, and then use table or partition expiration to systematically remove the row-level data. This reduces storage charges while keeping metrics available for long-term consumption.

## What's next

  * Learn how to [optimize cost](https://docs.cloud.google.com/bigquery/docs/best-practices-costs).
  * Learn how to [optimize query](https://docs.cloud.google.com/bigquery/docs/best-practices-performance-compute).
  * Learn how to [optimize functions](https://docs.cloud.google.com/bigquery/docs/best-practices-performance-functions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
