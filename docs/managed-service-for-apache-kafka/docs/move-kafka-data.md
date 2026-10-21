---
url: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/move-kafka-data/
title: Integrate Managed Service for Apache Kafka with other Google Cloud services \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:09.642212+00:00
---

# Integrate Managed Service for Apache Kafka with other Google Cloud services  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/move-kafka-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Kafka ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/overview)



Send feedback 

#  Integrate Managed Service for Apache Kafka with other Google Cloud services Stay organized with collections  Save and categorize content based on your preferences. 

This document advises developers, architects, and decision-makers on options for integrating Managed Service for Apache Kafka with other Google Cloud services.

The following table lists some factors to consider when choosing an integration solution for your Kafka data in Google Cloud.

Solution| Use cases  
---|---  
Kafka Connect |  Common data integration tasks Replicating Kafka data between clusters High availability/disaster recovery  
Dataflow |  High-volume data pipelines Complex data transformations or data aggregation Advanced windowing  
Managed Service for Apache Spark |  Integrate with existing Apache Spark workloads Migrate Apache Spark workloads to Google Cloud  
  
### Use Kafka Connect

[Kafka Connect](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview) provides a framework for streaming data between Kafka and other systems. Managed Service for Apache Kafka lets you provision clusters that run Kafka Connect.

Kafka Connect is recommended for most common data integration tasks for which there is a [supported connector](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview). Kafka Connect with [MirrorMaker 2.0](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/create-mirrormaker-connector) is recommended for replicating data between Kafka clusters, for example in high availability and disaster recovery (HA/DR) architectures.

Advantages of using Kafka Connect include:

  * Built-in connectors for sources and sinks such as BigQuery, Cloud SQL, and Cloud Storage.

  * Fully integrated into Managed Service for Apache Kafka, which simplifies management, operations, and monitoring.

  * Support for [filtering and per-message transformations](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/connect-cluster/connectors-overview#transformations-and-predicates).




### Use Dataflow

[Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) is a managed streaming platform built on the open source Apache Beam project. You can run Dataflow pipelines to write Kafka data to sinks such as BigQuery and Cloud Storage.

Consider using Dataflow for the following scenarios:

  * High-volume data pipelines. Dataflow jobs can scale up to thousands of workers. Dataflow also supports horizontal autoscaling, adding or removing workers as needed.

  * Data pipelines that require complex transformations, such as data cleaning, enrichment, or aggregation.

  * Integrating AI and ML into your data pipeline.

  * Joining multiple data streams with fine-grained control over windowing and handling of late-arriving data.




To deploy a Dataflow pipeline, you can run a prebuilt template or create an Apache Beam pipeline. For common data integration scenarios, consider running a template. For maximum flexibility and control, or if your pipeline requires custom logic, create an Apache Beam pipeline.

### Use Managed Service for Apache Spark

[Managed Service for Apache Spark](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts) lets you run Apache Spark workloads using a serverless model or a cluster-based model.

Consider using Managed Service for Apache Spark with your Kafka data if you have existing Spark pipelines. For example, if you have a Spark application that processes streaming data from Kafka, and you want to migrate this application to Google Cloud, Managed Service for Apache Spark is a suitable choice.

## What's next

  * Learn about [Kafka Connect in Managed Service for Apache Kafka](https://docs.cloud.google.com/managed-service-for-apache-kafka/docs/kafka-connect-overview).

  * Use a Dataflow template:

    * [Replicate Kafka data to Managed Service for Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/use-kafka-to-kafka-template)
    * [Write Managed Service for Apache Kafka data to BigQuery](https://docs.cloud.google.com/dataflow/docs/guides/use-kafka-to-bq-template)
    * [Write Managed Service for Apache Kafka data to Cloud Storage](https://docs.cloud.google.com/dataflow/docs/guides/use-kafka-to-cloud-storage-template)
  * Create an Apache Beam pipeline:

    * [Dataflow managed I/O for Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/managed-io-kafka)
    * [Read from Apache Kafka to Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/read-from-kafka)
    * [Write Dataflow to Apache Kafka](https://docs.cloud.google.com/dataflow/docs/guides/write-to-kafka)
  * For Spark Streaming and Kafka, Apache Spark provides an [integration guide](https://spark.apache.org/docs/latest/streaming-kafka-integration.html).




_Apache Kafka® is a registered trademark of The Apache Software Foundation or its affiliates in the United States and/or other countries._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
