---
url: https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering/
title: Partition and cluster BigQuery tables \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:30.332386+00:00
---

# Partition and cluster BigQuery tables  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/partitioning-and-clustering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Partition and cluster BigQuery tables Stay organized with collections  Save and categorize content based on your preferences. 

By configuring partitioning and clustering for your BigQuery destination, you can optimize query performance and control costs. Partitioning and clustering lets you reduce the amount of data that BigQuery needs to scan during query execution.

## Table partitioning

Table partitioning divides your table into segments called partitions, which make it easier to manage and query your data. You partition tables by specifying a partition column, which is used to segment the table.

Datastream supports three types of partitioning for BigQuery tables:

  * **Partitioning by ingestion time** : you can partition a table based on the time that Datastream ingests the data into BigQuery. You can select hourly, daily, monthly, or yearly granularity for ingestion time partitioning. Daily is the default granularity.

  * **Partitioning by time-unit** : you can partition a table based on a source column of a data type that Datastream maps to one of the following BigQuery data types: `DATE`, `DATETIME`, or `TIMESTAMP`. For information about how Datastream maps source data types to BigQuery data types, see [Data type mappings in BigQuery](https://docs.cloud.google.com/datastream/docs/bq-map-data-types#map-data-types).

**Note:** When you configure partitioning in Google Cloud, the column selection drop-down shows only the source columns or fields that are eligible for partitioning. If you use the Datastream API, Google Cloud CLI, or Terraform, the request fails with an error if you try to use a source type that doesn't map to an eligible BigQuery data type.

Depending on the BigQuery data type to which the source column maps, you can select one of the following granularity types:

    * `DAY`, `MONTH`, `YEAR`: for the `DATE` data type.
    * `HOUR`, `DAY`, `MONTH`, `YEAR`: for the `DATETIME` and `TIMESTAMP` data types.

**Note:** `DAY` is the default granularity type for all eligible data types.
  * **Partitioning by integer range** : you can partition a table by a source column of a data type that Datastream then maps to the BigQuery `INTEGER` data type. You need to provide the following information:

    * **Start** : the start value of the first partition range (inclusive).
    * **End** : The end value of the last partition range (exclusive).
    * **Interval** : The width of each partition range.

For more information, see [Integer range partitioning](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#integer_range).




For information about how to configure partitioning for your stream, see [Configure information about the source database for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#sourceconnectionprofileinfo).

## Table clustering

Clustering sorts the data in a table based on the values in the clustering columns and colocates data with similar values. Queries that filter by the clustered columns only scan the relevant data blocks instead of the entire table or table partition. This can improve query performance and reduce query costs.

You can cluster your BigQuery tables by up to four columns. The order in which you specify the columns determines the sort order of the data.

**Note:** If you don't specify clustering settings for a table, Datastream defaults to using up to four primary keys from the source table as the clustering keys in BigQuery.

You can cluster a table based on a source column of a data type that Datastream maps to one of the following BigQuery data types:

  * `BIGNUMERIC`
  * `BOOLEAN`
  * `DATE`
  * `DATETIME`
  * `GEOGRAPHY`
  * `INT64`
  * `NUMERIC`
  * `RANGE`
  * `STRING`
  * `TIMESTAMP`



For information about how Datastream maps source data types to BigQuery data types, see [Data type mappings in BigQuery](https://docs.cloud.google.com/datastream/docs/bq-map-data-types#map-data-types).

For information about how to configure clustering for your stream, see [Configure information about the source database for the stream](https://docs.cloud.google.com/datastream/docs/create-a-stream#sourceconnectionprofileinfo).

## Limitations

  * For partitioning limitations in BigQuery, see [Introduction to partitioned tables](https://docs.cloud.google.com/bigquery/docs/partitioned-tables#limitations).

  * For clustering limitations in BigQuery, see [Introduction to clustered tables](https://docs.cloud.google.com/bigquery/docs/clustered-tables#limitations).

  * For quota limits that apply to BigQuery partitioned tables, see [Quotas and limits](https://docs.cloud.google.com/bigquery/quotas#partitioned_tables).

  * Additionally, the following limitations apply when using Datastream:

    * Partitioning and clustering is only applied when Datastream creates a new BigQuery table. If you want to configure or modify partitioning and clustering settings for a table that already exists, first delete it from BigQuery, and then configure or modify its settings in Datastream.
    * For MongoDB sources, you can partition your tables only by ingestion time.
    * Clustering isn't supported for MongoDB databases.



## What's next

  * To learn more about partitioning in BigQuery, see [Introduction to partitioned tables](https://docs.cloud.google.com/bigquery/docs/partitioned-tables) and [Managing partitioned tables](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables).
  * For more information about clustering in BigQuery, see [Introduction to clustered tables](https://docs.cloud.google.com/bigquery/docs/clustered-tables) and [Manage clustered tables](https://docs.cloud.google.com/bigquery/docs/manage-clustered-tables).
  * To learn more about streams, see [Stream lifecycle](https://docs.cloud.google.com/datastream/docs/stream-states-and-actions).
  * To learn how to create a stream, see [Create a stream](https://docs.cloud.google.com/datastream/docs/create-a-stream).
  * To learn more about BigQuery, see [BigQuery destination](https://docs.cloud.google.com/datastream/docs/destination-bigquery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
