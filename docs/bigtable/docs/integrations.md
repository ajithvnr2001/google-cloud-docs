---
url: https://docs.cloud.google.com/bigtable/docs/integrations/
title: Integrations with Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:35:37.347994+00:00
---

# Integrations with Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/integrations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Resources ](https://docs.cloud.google.com/bigtable/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrations with Bigtable

Connecting Bigtable with other Google Cloud services and open-source tools lets you process, analyze, and synchronize data across your applications. These integrations help you build scalable data pipelines, run analytics, and manage database infrastructure.

## Google Cloud services

This section describes the Google Cloud services that Bigtable integrates with.

### BigQuery

[BigQuery](https://docs.cloud.google.com/bigquery) is Google's fully managed, petabyte-scale, low-cost analytics data warehouse. You can use BigQuery with Bigtable for the following purposes:

  * You can create a BigQuery external table and then use it to query your Bigtable table and join the data to other BigQuery tables. For more information, see [Query Bigtable data](https://docs.cloud.google.com/bigquery/external-data-bigtable).

  * You can export your BigQuery data to a Bigtable table by using reverse ETL (RETL) from BigQuery to Bigtable. For more information, see [Export data to Bigtable](https://docs.cloud.google.com/bigquery/docs/export-to-bigtable).




### Cloud Asset Inventory

Cloud Asset Inventory, which provides inventory services based on a time series database, supports and returns Bigtable resources types. For a complete list, see [Supported resource types](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types#supported_resource_types).

### Knowledge Catalog

Knowledge Catalog automatically catalogs metadata about Bigtable resources. Cataloged information about your data can help facilitate analysis, data reuse, application development, and data management. For more information, see [Manage data assets using Knowledge Catalog](https://docs.cloud.google.com/bigtable/docs/manage-data-assets-using-data-catalog).

### Dataflow

[Dataflow](https://docs.cloud.google.com/dataflow) is a cloud service and programming model for big data processing. Dataflow supports both batch and streaming processing. You can use Dataflow to process data that is stored in Bigtable or to store the output of your Dataflow pipeline. You can also use Dataflow templates to [export](https://docs.cloud.google.com/dataflow/docs/templates/provided-templates#cloudbigtabletosequencefile) and [import](https://docs.cloud.google.com/dataflow/docs/templates/provided-templates#sequencefiletocloudbigtable) your data as Avro, Parquet, or SequenceFiles.

**Note:** The Python client library for Bigtable supports Dataflow writes but not reads.

To get started, see [Bigtable Beam connector](https://docs.cloud.google.com/bigtable/docs/beam-connector).

You can also use Bigtable as a key-value lookup to enrich the data in a pipeline. For an overview, see [Enrich streaming data](https://docs.cloud.google.com/dataflow/docs/guides/enrichment). For a tutorial, see [Use Apache Beam and Bigtable to enrich data](https://docs.cloud.google.com/dataflow/docs/notebooks/bigtable_enrichment_transform).

### Managed Service for Apache Spark

[Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc) provides Apache Hadoop and related products as a managed service in the cloud. With Managed Service for Apache Spark, you can run Hadoop jobs that read from and write to Bigtable.

For an example of a Hadoop MapReduce job that uses Bigtable, see the `/java/dataproc-wordcount` directory in the GitHub repository [GoogleCloudPlatform/cloud-bigtable-examples](https://github.com/GoogleCloudPlatform/cloud-bigtable-examples/tree/master/java/dataproc-wordcount).

### Pub/Sub

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Bigtable supports ingestion from Pub/Sub subscriptions. You can configure a Pub/Sub subscription to send messages to a Bigtable table. Pub/Sub writes these messages to Bigtable as new rows. For more information, see [Bigtable subscriptions](https://docs.cloud.google.com/pubsub/docs/bigtable-subscriptions).

### Agent Platform Vector Search

[Gemini Enterprise Agent Platform Vector Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search/overview) is a technology that can search from billions of semantically similar or semantically related items. It's useful for implementing recommendation engines, chatbots, and text classification.

You can use Bigtable to store vector embeddings, export them into a Vector Search index, and then query the index for similar items. For a sample workflow, see the [Bigtable to Vector Search export tutorial](https://github.com/GoogleCloudPlatform/workflows-demos/tree/master/bigtable-ai/vertex-vector-search/workflows#readme) in the `workflows-demos` GitHub repository.

You can also push streaming updates to keep the Vector Search index in sync with Bigtable in real time. For more information, see the [Bigtable change streams to Vector Search template](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/bigtable-change-streams-to-vector-search).

## Big Data

This section describes Big Data products that Bigtable integrates with.

### Apache Beam

Apache Beam is a unified model for defining batch and streaming data-parallel processing pipelines. The [Bigtable Beam connector](https://docs.cloud.google.com/bigtable/docs/\(/bigtable/docs/beam-connector\)) (`BigtableIO`) helps you perform batch and streaming operations on Bigtable data in a pipeline.

For a tutorial showing how to use the Bigtable Beam connector to deploy a data pipeline to Dataflow, see [Process a Bigtable change stream](https://docs.cloud.google.com/bigtable/docs/change-streams-tutorial).

### Apache Hadoop

[Apache Hadoop](https://hadoop.apache.org/) is a framework that enables distributed processing of large data sets across clusters of computers. You can use [Managed Service for Apache Spark](https://docs.cloud.google.com/dataproc) to create a Hadoop cluster, then run MapReduce jobs that read from and write to Bigtable.

For an example of a Hadoop MapReduce job that uses Bigtable, see the `/java/dataproc-wordcount` directory in the GitHub repository [GoogleCloudPlatform/cloud-bigtable-examples](https://github.com/GoogleCloudPlatform/cloud-bigtable-examples/tree/master/java/dataproc-wordcount).

### StreamSets Data Collector

StreamSets Data Collector is a data-streaming application that you can [configure to write data to Bigtable](https://streamsets.com/documentation/datacollector/latest/help/datacollector/UserGuide/Destinations/Bigtable.html). StreamSets provides a Bigtable library in its GitHub repository at [streamsets/datacollector](https://github.com/streamsets/datacollector).

## Graph databases

This section describes graph databases that Bigtable integrates with.

### HGraphDB

[HGraphDB](https://github.com/rayokota/hgraphdb) is a client layer for using Apache HBase or Bigtable as a graph database. It implements the [Apache TinkerPop 3](https://tinkerpop.apache.org/) interfaces.

For more information about running HGraphDB with Bigtable support, see the [HGraphDB documentation](https://github.com/rayokota/hgraphdb#support-for-google-cloud-bigtable).

**Note:** This integration was developed independently by a third party. Google is not affiliated with, and does not endorse, this integration.

### JanusGraph

[JanusGraph](https://janusgraph.org/) is a scalable graph database. It is optimized for storing and querying graphs containing hundreds of billions of vertices and edges.

For more information about running JanusGraph with Bigtable support, see [Running JanusGraph with Bigtable](https://docs.cloud.google.com/solutions/running-janusgraph-with-bigtable) or the [JanusGraph documentation](https://docs.janusgraph.org/storage-backend/bigtable/).

## Infrastructure management

This section describes infrastructure management tools that Bigtable integrates with.

### Pivotal Cloud Foundry

Pivotal Cloud Foundry is an application development and deployment platform that offers the ability to [bind an application to Bigtable](https://docs.pivotal.io/partners/gcp-sb/using.html).

### Terraform

Terraform is an open source tool that codifies APIs into declarative configuration files. These files can be shared among team members, treated as code, edited, reviewed, and versioned.

For more information about using Bigtable with Terraform, see [Bigtable Instance](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_instance) and [Bigtable Table](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_table) in the Terraform documentation.

## Time-series databases and monitoring

This section describes time-series databases and monitoring tools that Bigtable integrates with.

### OpenTSDB

[OpenTSDB](http://opentsdb.net/) is a time-series database that can use Bigtable for storage. The [OpenTSDB documentation](http://opentsdb.net/docs/build/html/user_guide/backends/bigtable.html) provides information to help you get started.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
