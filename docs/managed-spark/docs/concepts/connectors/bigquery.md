---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/bigquery/
title: BigQuery connector \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:10.760570+00:00
---

# BigQuery connector  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/bigquery/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  BigQuery connector Stay organized with collections  Save and categorize content based on your preferences. 

You can use a BigQuery connector to enable programmatic read and write access to [BigQuery](https://docs.cloud.google.com/bigquery). This is an ideal way to process data that is stored in BigQuery. Command-line access is not exposed. The BigQuery connector is a library that enables Spark and Hadoop applications to process data from BigQuery and write data to BigQuery using its native terminology.

The [GoogleCloudDataproc/spark-bigquery-connector](https://github.com/GoogleCloudDataproc/spark-bigquery-connector) is also available for reading data from BigQuery. It takes advantage of the [BigQueryStorage API](https://docs.cloud.google.com/bigquery/docs/reference/storage). 

## Pricing

When using the connector, charges include [BigQuery usage fees](https://cloud.google.com/bigquery/pricing). The following service-specific charges may also apply:

  * [Cloud Storage](https://docs.cloud.google.com/storage) \- the connector downloads data into a Cloud Storage bucket before or during job execution. After the job successfully completes, the data is deleted from Cloud Storage. You are charged for this storage according to [Cloud Storage pricing](https://cloud.google.com/storage/pricing). To avoid excess charges, check your Cloud Storage account and remove unneeded temporary files.
  * [Storage Read API](https://docs.cloud.google.com/bigquery/docs/reference/storage) \- the connector reads data from tables using the Storage Read API to achieve high throughput. 
    * When requests originate from either the [Managed Service for Apache Spark serverless](https://docs.cloud.google.com/managed-spark/docs/serverless-overview) or [BigQuery stored procedures for Apache Spark](https://docs.cloud.google.com/bigquery/docs/spark-procedures) Storage Read API streaming read costs are delegated to the connector at no additional charge. Standard network egress charges still apply if data is read across regions.
    * When requests originate from cluster-based Apache Spark workloads (such as the [Managed Service for Apache Spark on clusters](https://docs.cloud.google.com/managed-spark/docs/concepts/clusters-overview) or Apache Spark running on Google Kubernetes Engine (GKE)), standard [Storage Read API pricing](https://docs.cloud.google.com/bigquery/docs/reference/storage#pricing) applies.



## Available connectors

The following BigQuery connectors are available for use in the Hadoop ecosystem:

  1. The [Spark BigQuery Connector](https://github.com/GoogleCloudDataproc/spark-bigquery-connector) adds a Spark data source, which allows DataFrames to interact directly with BigQuery tables using Spark's `read` and `write` operations.
  2. The [Hive BigQuery Connector](https://github.com/GoogleCloudDataproc/hive-bigquery-connector) adds a Storage Handler, which allows Apache Hive to interact directly with BigQuery tables using HiveQL syntax.
  3. The [Hadoop BigQuery Connector](https://github.com/GoogleCloudDataproc/hadoop-connectors) allows Hadoop mappers and reducers to interact with BigQuery tables using abstracted versions of the [InputFormat](http://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapreduce/InputFormat.html) and [OutputFormat](http://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapreduce/OutputFormat.html) classes.

**Caution:** The Hadoop BigQuery connector for Hadoop MapReduce is not supported. Recommendation: Use the [Spark BigQuery Connector](https://github.com/GoogleCloudDataproc/spark-bigquery-connector) for improved performance. For more information, see [Use the BigQuery Connector with Spark](https://docs.cloud.google.com/managed-spark/docs/tutorials/bigquery-connector-spark-example).



## Use the connectors

For a quick start using the BigQuery connector, see the following examples:

  * [Spark example](https://docs.cloud.google.com/managed-spark/docs/tutorials/bigquery-connector-spark-example)
  * [Java MapReduce example](https://docs.cloud.google.com/managed-spark/docs/tutorials/bigquery-connector-mapreduce-example)
  * [Connect Managed Service for Apache Spark cluster to BigQuery](https://console.cloud.google.com/?walkthrough_id=dataproc--dataproc-bq-spark-connector)



## What's next

  * Learn more about [BigQuery](https://docs.cloud.google.com/bigquery).
  * Follow the [BigQuery example for Spark](https://docs.cloud.google.com/managed-spark/docs/tutorials/bigquery-connector-spark-example).
  * Learn more about the [Hive BigQuery Connector](https://docs.cloud.google.com/managed-spark/docs/concepts/connectors/hive-bigquery).
  * Follow the [BigQuery example for Java MapReduce](https://docs.cloud.google.com/managed-spark/docs/tutorials/bigquery-connector-mapreduce-example).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
