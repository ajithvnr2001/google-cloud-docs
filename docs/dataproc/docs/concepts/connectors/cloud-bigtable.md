---
url: https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-bigtable/
title: Bigtable with Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:39:11.267226+00:00
---

# Bigtable with Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc/docs/concepts/connectors/cloud-bigtable/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Bigtable with Managed Service for Apache Spark Stay organized with collections  Save and categorize content based on your preferences. 

[Bigtable](https://docs.cloud.google.com/bigtable) is Google's NoSQL Big Data database service. It's the same database that powers many core Google services, including Search, Analytics, Maps, and Gmail. Bigtable is designed to handle massive workloads at consistent low latency and high throughput, so it's a great choice for both operational and analytical applications, including IoT, user analytics, and financial data analysis.

Bigtable is an excellent option for any Apache Spark or Hadoop uses that require [Apache HBase](https://hbase.apache.org/). Bigtable supports the [Apache HBase](https://hbase.apache.org/) 1.0+ and 2.0+ APIs, and offers a [Bigtable HBase client in Maven](https://docs.cloud.google.com/bigtable/docs/using-maven) to use Bigtable with Managed Service for Apache Spark.

## Use the Bigtable Spark connector

The Bigtable Spark connector lets you read and write data from and to Bigtable. You can read data from within your Spark application using Spark SQL and DataFrames. For read-only jobs, you can use [Data Boost serverless compute](https://docs.cloud.google.com/bigtable/docs/data-boost-overview), Data Boost is designed for the performance requirements of high-throughput jobs and queries, and it lets you avoid impacting your application-serving cluster traffic when those jobs and queries are run.

For more information, see [Use the Bigtable Spark connector](https://docs.cloud.google.com/bigtable/docs/use-bigtable-spark-connector).

## What's next

  * For more information about using Bigtable, see the [Bigtable](https://docs.cloud.google.com/bigtable/docs/overview) documentation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
