---
url: https://docs.cloud.google.com/bigquery/docs/load-data-partitioned-tables/
title: Load data into partitioned tables \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:18.916277+00:00
---

# Load data into partitioned tables  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/load-data-partitioned-tables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Load data into partitioned tables

This document describes how to load data into partitioned tables.

## Write data to a specific partition

You can load data to a specific partition by using the [`bq load`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_load) command with a partition decorator. The following example appends data into the `20160501` (May 1, 2016) partition of an existing table, assuming the table is already partitioned by date:
    
    
    bq load --source_format=CSV 'my_dataset.my_table$20160501' data.csv

You can also write the results of a query to a specific partition:
    
    
    bq query \
      --use_legacy_sql=false  \
      --destination_table='my_table$20160501' \
      --append_table=true \
      'SELECT * FROM my_dataset.another_table'

With ingestion-time partitioning, you can use this technique to load older data into the partition that corresponds to the time when the data was originally created.

You can also use this technique to adjust for time zones. By default, ingestion- time partitions are based on UTC time. If you want the partition time to match a particular time zone, you can use partition decorators to offset the UTC ingestion time. For example, if you are on Pacific Standard Time (PST), you can load data that was generated on May 1, 2016 23:30 PST into the partition for that date by using the corresponding explicit partition decorator, `$2016050123`. If you didn't use this explicit decorator, it would instead load into `$2016050207` (May 2nd 07:00 UTC).

For time-unit column and integer-range partitioned tables, the partition ID specified in the decorator must match the data being written. For example, if the table is partitioned on a `DATE` column, the decorator must match the value in that column. Otherwise, an error occurs. However, if you know beforehand that your data is in a single partition, specifying the partition decorator can improve write performance.

The preceding example appends data to a partition. To overwrite data in a partition instead, you must include different flags for each command, namely `bq load --replace=true ...` and `bq query --append_table=false ...`. For more information about the flags in these commands, see [`bq load`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_load) and [`bq query`](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_query).

For more information on loading data, see [Introduction to loading data into BigQuery](https://docs.cloud.google.com/bigquery/docs/loading-data).

## Stream data into partitioned tables

For information about streaming data into a partitioned table with the BigQuery Storage Write API (gRPC), see [Stream into partitioned tables](https://docs.cloud.google.com/bigquery/docs/write-api#stream_into_partitioned_tables).

## What's next

To learn more about working with partitioned tables, see:

  * [Create partitioned tables](https://docs.cloud.google.com/bigquery/docs/creating-partitioned-tables)
  * [Manage partitioned tables](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables)
  * [Querying partitioned tables](https://docs.cloud.google.com/bigquery/docs/querying-partitioned-tables)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
