---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/components/hbase/
title: Managed Service for Apache Spark optional HBase component \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:38.959473+00:00
---

# Managed Service for Apache Spark optional HBase component  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/components/hbase/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark optional HBase component Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** Starting with Managed Service for Apache Spark [version 2.1](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.1), you can no longer use the optional HBase component. Managed Service for Apache Spark [version 1.5](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.5) and Managed Service for Apache Spark [version 2.0](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.0) offer a Beta version of HBase with no support. However, due to the ephemeral nature of Managed Service for Apache Spark clusters, using HBase is not recommended.

Installation of the optional HBase component is limited to Managed Service for Apache Spark clusters created with image version [1.5](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-1.5) or [2.0](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-release-2.0).

While Google Cloud provides many services that let you deploy self-managed Apache HBase, [Bigtable](https://docs.cloud.google.com/bigtable/docs/overview) is often the best option as it provides an open API with HBase and workload portability. HBase database tables can be migrated to Bigtable for management of the underlying data, while applications that previously interoperated with HBase, such as Spark, may remain on Managed Service for Apache Spark and securely connect with Bigtable. In this guide, we provide the high-level steps for getting started with Bigtable and provide references for migrating data to Bigtable from Managed Service for Apache Spark HBase deployments.

## Get started with Bigtable

Cloud Bigtable is a highly scalable and performant NoSQL platform that provides [Apache HBase API client compatibility](https://cloud.google.com/bigtable/docs/hbase-bigtable) and portability for HBase workloads. The client is compatible with HBase API versions 1.x and 2.x and may be included with the existing application to read and write to Bigtable. Existing HBase applications may add the Bigtable HBase client library to read and write data stored in Bigtable.

See [Bigtable and the HBase API](https://cloud.google.com/bigtable/docs/hbase-bigtable) for more information on configuring your HBase application with Bigtable.

## Create a Bigtable cluster

You can get started using Bigtable by creating a cluster and tables for storing data that was previously stored in HBase. Follow the steps in the Bigtable documentation for [creating an instance](https://docs.cloud.google.com/bigtable/docs/creating-instance#creating-instance), a cluster, and [tables](https://docs.cloud.google.com/bigtable/docs/managing-tables) with the same schema as the HBase tables. For automated creation of tables from HBase table DDLs, refer to the [schema translator tool](https://docs.cloud.google.com/bigtable/docs/migrate-hbase-on-google-cloud-to-bigtable#create-destination-table).

Open the Bigtable instance in Google Cloud console to view the table and server-side monitoring charts, including rows per second, latency, and throughput, to manage the newly provisioned table. For additional information, see [Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).

![](https://docs.cloud.google.com/static/managed-spark/images/bigtable-ui.png)

## Migrate data from Managed Service for Apache Spark to Bigtable

After you create the tables in Bigtable, you can import and validate your data by following the guidance at [Migrate data from HBase to Bigtable offline](https://docs.cloud.google.com/bigtable/docs/migrate-hbase-data-to-bigtable). After you migrate the data, you can update applications to send reads and writes to Bigtable.

## What's next

  * See [Wordcount Spark examples](https://github.com/GoogleCloudPlatform/java-docs-samples/tree/main/bigtable/spark) for running Spark with the Bigtable.
  * Review online migration options with [live replication from HBase to Bigtable](https://docs.cloud.google.com/bigtable/docs/hbase-replication).
  * Watch [How Box modernized their NoSQL databases](https://www.youtube.com/watch?v=DteQ09WFhaU) to understand other benefits.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
