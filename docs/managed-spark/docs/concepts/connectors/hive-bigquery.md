---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/hive-bigquery/
title: Hive-BigQuery connector \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:01.573892+00:00
---

# Hive-BigQuery connector  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/hive-bigquery/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Hive-BigQuery connector Stay organized with collections  Save and categorize content based on your preferences. 

The open source [Hive-BigQuery connector](https://github.com/GoogleCloudDataproc/hive-bigquery-connector) lets your [Apache Hive](https://hive.apache.org/) workloads read and write data from and to [BigQuery](https://docs.cloud.google.com/bigquery) and [BigLake](https://docs.cloud.google.com/lakehouse/docs) tables. You can store data in BigQuery storage or in open source data formats on Cloud Storage.

Use the connector to work with Hive and BigQuery together or to migrate your data warehouse from Hive to BigQuery.

The Hive-BigQuery connector implements the [Hive Storage Handler API](https://cwiki.apache.org/confluence/display/Hive/StorageHandlers) to allow Hive workloads to integrate with BigQuery and BigLake tables. The Hive execution engine handles compute operations, such as aggregates and joins, and the connector manages interactions with data stored in BigQuery or in BigLake-connected Cloud Storage buckets.

The following diagram illustrates how Hive-BigQuery connector fits between the compute and data layers.

![Hive-BigQuery connector architecture](https://docs.cloud.google.com/static/managed-spark/images/hive-bigquery-connector-overview.png)

## Use cases

Here are some of the ways the Hive-BigQuery connector can help you in common data-driven scenarios:

  * Data migration. You plan to move your Hive data warehouse to BigQuery, then incrementally translate your Hive queries into BigQuery SQL dialect. You expect the migration to take a significant amount of time due to the size of your data warehouse and the large number of connected applications, and you need to ensure continuity during the migration operations. Here's the workflow:

    1. You move your data to BigQuery
    2. Using the connector, you access and run your original Hive queries while you gradually translate the Hive queries to BigQuery ANSI-compliant SQL dialect.
    3. After completing the migration and translation, you retire Hive.
  * Hive and BigQuery workflows. You plan to use Hive for some tasks, and BigQuery for workloads that benefit from its features, such as [BigQuery BI Engine](https://docs.cloud.google.com/bigquery/docs/bi-engine-intro) or [BigQuery ML](https://docs.cloud.google.com/bigquery/docs/bqml-introduction). You use the connector to join Hive tables to your BigQuery tables.

  * Reliance on an open source software (OSS) stack. To avoid vendor lock-in, you use a full OSS stack for your data warehouse. Here's your data plan:

    1. You migrate your data in its original OSS format, such as Avro, Parquet, or ORC, to Cloud Storage buckets using a BigLake connection.

    2. You continue to use Hive to execute and process your Hive SQL dialect queries.

    3. You use the connector as needed to connect to BigQuery to benefit from the following features:

       * [Metadata caching](https://docs.cloud.google.com/bigquery/docs/biglake-intro#metadata_caching_for_performance) for query performance
       * [Data loss prevention](https://docs.cloud.google.com/bigquery/docs/scan-with-dlp)
       * [Column-level access control](https://docs.cloud.google.com/bigquery/docs/column-level-security-intro)
       * [Dynamic data masking](https://docs.cloud.google.com/bigquery/docs/column-data-masking-intro) for security and governance at scale.



## Features

You can use the Hive-BigQuery connector to work with your BigQuery data and accomplish the following tasks:

  * Run queries with MapReduce and Tez execution engines.
  * Create and delete BigQuery tables from Hive.
  * Join BigQuery and BigLake tables with Hive tables.
  * Perform fast reads from BigQuery tables using the [Storage Read API](https://docs.cloud.google.com/bigquery/docs/reference/storage) streams and the [Apache Arrow](https://arrow.apache.org/) format
  * Write data to BigQuery using the following methods: 
    * Direct writes using the BigQuery [Storage Write API in pending mode](https://docs.cloud.google.com/bigquery/docs/write-api-batch). Use this method for workloads that require low write latency, such as near-real-time dashboards with short refresh time windows.
    * Indirect writes by staging temporary Avro files to Cloud Storage, and then loading the files into a destination table using the [Load Job API](https://docs.cloud.google.com/bigquery/docs/batch-loading-data). This method is less expensive than the direct method, since BigQuery load jobs don't accrue charges. Since this method is slower, and finds its best use in workloads that aren't time critical
  * Access BigQuery [time-partitioned](https://docs.cloud.google.com/bigquery/docs/partitioned-tables) and [clustered](https://docs.cloud.google.com/bigquery/docs/clustered-tables) tables. The following example defines the relation between a Hive table and a table that is partitioned and clustered in BigQuery.
        
        CREATE TABLE my_hive_table (int_val BIGINT, text STRING, ts TIMESTAMP)
        STORED BY 'com.google.cloud.hive.bigquery.connector.BigQueryStorageHandler'
        TBLPROPERTIES (
        'bq.table'='myproject.mydataset.mytable',
        'bq.time.partition.field'='ts',
        'bq.time.partition.type'='MONTH',
        'bq.clustered.fields'='int_val,text'
        );

  * Prune columns to avoid retrieving unnecessary columns from the data layer.

  * Use predicate pushdowns to pre-filter data rows at the BigQuery storage layer. This technique can significantly improve overall query performance by reducing the amount of data traversing the network.

  * Automatically convert Hive data types to BigQuery data types.

  * Read BigQuery [views](https://docs.cloud.google.com/bigquery/docs/views-intro) and [table snapshots](https://docs.cloud.google.com/bigquery/docs/table-snapshots-intro).

  * Integrate with Spark SQL.

  * Integrate with Apache Pig and HCatalog.




## Get started

See the instructions to [install and configure the Hive-BigQuery connector on a Hive cluster](https://github.com/GoogleCloudDataproc/hive-bigquery-connector/blob/main/README.md).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
