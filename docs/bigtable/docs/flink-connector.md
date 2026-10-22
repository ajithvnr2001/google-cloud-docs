---
url: https://docs.cloud.google.com/bigtable/docs/flink-connector/
title: Flink Bigtable connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:40.088207+00:00
---

# Flink Bigtable connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/flink-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Flink Bigtable connector

Apache Flink is a stream-processing framework that lets you manipulate data in real time. If you have a Bigtable table, you can use a _Flink Bigtable connector_ to stream, serialize, and write data from your specified data source to Bigtable. The connector lets you do the following, using either the Apache Flink Table API or the Datastream API:

  1. Create a pipeline
  2. Serialize the values from your data source into Bigtable mutation entries
  3. Write those entries to your Bigtable table



This document describes the Flink Bigtable connector and what you need to know before you use it. Before you read this document, you should be familiar with [Apache Flink](https://nightlies.apache.org/flink/flink-docs-master/), the [Bigtable storage model](https://docs.cloud.google.com/bigtable/docs/overview#storage-model), and [Bigtable writes](https://docs.cloud.google.com/bigtable/docs/writes).

To use the connector, you must have a pre-existing Bigtable table to serve as your data sink. You must create the table's column families before you start the pipeline; column families can't be created on write. For more information, see [Create and manage tables](https://docs.cloud.google.com/bigtable/docs/managing-tables).

The connector is compatible with Apache Flink version 2.1.0 and available on GitHub. For information about installing the connector, see the [Flink Bigtable Connector](https://github.com/google/flink-connector-gcp/blob/main/connectors/bigtable/README.md) repository. For code samples that demonstrate how to use the connector, see the [flink-examples-gcp-bigtable](https://github.com/google/flink-connector-gcp/tree/main/connectors/bigtable/flink-examples-gcp-bigtable) directory.

## Serializers

The Flink connector has three built-in serializers that you can use to convert data into Bigtable mutation entries:

  * `GenericRecordToRowMutationSerializer`: For AVRO `GenericRecord` objects
  * `RowDataToRowMutationSerializer`: For Flink `RowData` objects
  * `FunctionRowMutationSerializer`: For custom serialization logic using a provided function



You can also choose to create your own custom serializer inheriting from `BaseRowMutationSerializer`.

## Serialization modes

When you use the Flink connector, you choose one of two serialization modes. The mode specifies how your source data is serialized into mutation entries that are written to column families in your Bigtable table. You must use either one mode or the other.

### Column family mode

In column family mode, all data is written to a single specified column family. Nested fields are not supported.

### Nested-rows mode

In nested-rows mode, each top-level field represents a column family. The value of the top-level field (RowKeyField) is another field. The value of that field has a row object for each column in the Bigtable column family. In nested rows mode, all fields other than the top-level field must be row objects. Double-nested rows are not supported.

## Configuration options

To configure the connector's performance and behavior, you can use several options. For more information about these options, see the [connector documentation on GitHub](https://github.com/google/flink-connector-gcp/blob/main/connectors/bigtable/README.md#connector-options).

## Exactly-once processing

In Apache Flink, _exactly once_ means that each data record in a stream is processed exactly one time, preventing any duplicate processing or data loss, even in the event of system failures.

A Bigtable `mutateRow` mutation is idempotent by default, so a write request that has the same row key, column family, column, timestamp, and value doesn't create a new cell, even if it's retried. When you use Bigtable as the data sink for an Apache Flink framework, you get exactly-once behavior automatically, as long as the following conditions are met:

  * You don't set the timestamp to use the server-side timestamp (`-1`) in retries.
  * The rest of your pipeline satisfies exactly-once requirements.



For more information on exactly-once semantics, see [An overview of end-to-end exactly-once processing in Apache Flink](https://flink.apache.org/2018/02/28/an-overview-of-end-to-end-exactly-once-processing-in-apache-flink-with-apache-kafka-too/).

## What's next

  * [Bigtable Beam connector](https://docs.cloud.google.com/bigtable/docs/beam-connector)
  * [Bigtable Kafka Connect sink connector](https://docs.cloud.google.com/bigtable/docs/kafka-sink-connector)
  * [Integrations with Bigtable](https://docs.cloud.google.com/bigtable/docs/integrations)
  * [Datastream API reference](https://docs.cloud.google.com/datastream/docs/use-the-datastream-api)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
