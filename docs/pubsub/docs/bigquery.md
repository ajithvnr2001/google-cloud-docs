---
url: https://docs.cloud.google.com/pubsub/docs/bigquery/
title: BigQuery subscriptions \u00a0|\u00a0 Pub/Sub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:20:58.382514+00:00
---

# BigQuery subscriptions  |  Pub/Sub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/pubsub/docs/bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Pub/Sub ](https://docs.cloud.google.com/pubsub/docs)
  * [ Guides ](https://docs.cloud.google.com/pubsub/docs/overview)



Send feedback 

#  BigQuery subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of a BigQuery subscription, its workflow, and associated properties.

A BigQuery subscription is a type of export subscription that writes messages to an existing BigQuery table as they are received. You don't need to configure a separate subscriber client. Use the Google Cloud console, the Google Cloud CLI, the client libraries, or the Pub/Sub API to create, update, list, detach, or delete a BigQuery subscription.

**Key Point:** Understand the workflow for a BigQuery subscription and read about the permissions, properties, quotas, and pricing related to the subscription.

Without the BigQuery subscription type, you need a pull or push subscription and a subscriber (such as Dataflow) that reads messages and writes them to a BigQuery table. The overhead of running a Dataflow job is not necessary when messages don't require additional processing before storing them in a BigQuery table; you can use a BigQuery subscription instead.

For lightweight modifications on messages, you can attach a [Single Message Transform](https://docs.cloud.google.com/pubsub/docs/smts/smts-overview) to your BigQuery subscription. However, a Dataflow pipeline is recommended for Pub/Sub systems where more complex data transformation is required before the data is stored in a BigQuery table, especially if you want to window or aggregate across messages.

To learn how to stream data from Pub/Sub to BigQuery with transformation by using Dataflow, see Stream from [Pub/Sub to BigQuery](https://docs.cloud.google.com/dataflow/docs/tutorials/dataflow-stream-to-bigquery).

The [ Pub/Sub subscription to BigQuery template from Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/pubsub-subscription-to-bigquery) enforces exactly once delivery by default. This is typically achieved through deduplication mechanisms within the Dataflow pipeline. However, the BigQuery subscription only supports at least once delivery. If exact deduplication is critical for your use case, consider downstream processes in BigQuery to handle potential duplicates.

## Before you begin

Before reading this document, ensure that you're familiar with the following:

  * How [Pub/Sub works](https://docs.cloud.google.com/pubsub/docs/overview) and the different Pub/Sub terms.

  * The different [kinds of subscriptions](https://docs.cloud.google.com/pubsub/docs/subscription-overview) that Pub/Sub supports and why you might want to use a BigQuery subscription.

  * How [BigQuery](https://docs.cloud.google.com/bigquery/docs) works and how to configure and manage BigQuery tables.




## BigQuery subscription workflow

The following image shows the workflow between a BigQuery subscription and BigQuery.

![Flow of messages for a BigQuery subscription](https://docs.cloud.google.com/static/pubsub/images/subscriber_bigquery.png)**Figure 1.** Workflow for a BigQuery subscription

Here is a brief description of the workflow that references Figure 1:

  1. Pub/Sub uses the [BigQuery Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api) to send data to the BigQuery table.
  2. The messages are sent in batches to the BigQuery table.
  3. After a successful completion of a write operation, the API returns an OK response.
  4. If there are any failures in the write operation, the Pub/Sub message itself is negatively acknowledged. The message is then re-sent. If the message fails enough times and there's a dead letter topic configured on the subscription, then the message is moved to the dead letter topic.



## Properties of a BigQuery subscription

The properties that you configure for a BigQuery subscription determine the BigQuery table to which Pub/Sub writes messages and the type of schema of that table.

For more information, see [BigQuery properties](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription#subscription_properties).

## Schema compatibility

This section is only applicable if you select the option [**Use topic schema**](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription#use-topic-schema) when you create a BigQuery subscription.

Pub/Sub and BigQuery use different ways to define their schemas. Pub/Sub schemas are defined in [Apache Avro or Protocol Buffer](https://docs.cloud.google.com/pubsub/docs/schemas#schema_types) format while BigQuery schemas are defined using a [variety of formats](https://docs.cloud.google.com/bigquery/docs/schemas).

The following is a list of important information regarding the schema compatibility between a Pub/Sub topic and a BigQuery table.

  * Any message that contains an improperly formatted field is not written to BigQuery.

  * In the BigQuery schema, `INT`, `SMALLINT`, `INTEGER`, `BIGINT`, `TINYINT`, and `BYTEINT` are aliases for `INTEGER`; `DECIMAL` is an alias for `NUMERIC`; and `BIGDECIMAL` is an alias for `BIGNUMERIC`.

  * When the type in the topic schema is a `string` and the type in the BigQuery table is `JSON`, `TIMESTAMP`, `DATETIME`, `DATE`, `TIME`, `NUMERIC`, or `BIGNUMERIC`, then any value for this field in a Pub/Sub message must adhere to the format specified for the [BigQuery data type](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types).

  * Some Avro logical types are supported, as specified in the following table. Any logical types not listed only match the equivalent Avro type that they annotate, as detailed in the [Avro specification](https://avro.apache.org/docs/1.10.2/spec.html#Logical+Types).




The following is a collection of mapping of different schema formats to BigQuery data types.

### Avro types

**Avro Type** | **BigQuery Data Type**  
---|---  
`null` | `Any NULLABLE `  
`boolean` | `BOOLEAN`  
`int` | `INTEGER`, `NUMERIC`, or `BIGNUMERIC`  
`long` | `INTEGER`, `NUMERIC`, or `BIGNUMERIC`  
`float` | `FLOAT64`, `NUMERIC`, or `BIGNUMERIC`  
`double` | `FLOAT64`, `NUMERIC`, or `BIGNUMERIC`  
`bytes` | `BYTES`, `NUMERIC`, or `BIGNUMERIC`  
`string` | `STRING`, `JSON`, `TIMESTAMP`, `DATETIME`, `DATE`, `TIME`, `NUMERIC`, or `BIGNUMERIC`  
`record` | `RECORD/STRUCT`  
`array` of `Type` | `REPEATED Type`  
`map` with value type `ValueType` | `REPEATED STRUCT <key STRING, value ValueType>`  
`union` with two types, one that is `null` and the other `Type` | `NULLABLE Type`  
other `union`s  | Unmappable   
`fixed` | `BYTES`, `NUMERIC`, or `BIGNUMERIC`  
`enum` | `INTEGER`  
  
### Avro logical types

**Avro Logical Type** | **BigQuery Data Type**  
---|---  
`timestamp-micros` | `TIMESTAMP`  
`timestamp-millis` | `TIMESTAMP`  
`date` | `DATE`  
`time-micros` | `TIME`  
`time-millis` | `TIME`  
`duration` | `INTERVAL`  
`decimal` | `NUMERIC` or `BIGNUMERIC`  
  
### Protocol Buffer types

**Protocol Buffer Type** | **BigQuery Data Type**  
---|---  
`double` | `FLOAT64`, `NUMERIC`, or `BIGNUMERIC`  
`float` | `FLOAT64`, `NUMERIC`, or `BIGNUMERIC`  
`int32` | `INTEGER`, `NUMERIC`, `BIGNUMERIC`, or `DATE`  
`int64` | `INTEGER`, `NUMERIC`, `BIGNUMERIC`, `DATE`, `DATETIME`, or `TIMESTAMP`  
`uint32` | `INTEGER`, `NUMERIC`, `BIGNUMERIC`, or `DATE`  
`uint64` | `NUMERIC` or `BIGNUMERIC`  
`sint32` | `INTEGER`, `NUMERIC`, or `BIGNUMERIC`  
`sint64` | `INTEGER`, `NUMERIC`, `BIGNUMERIC`, `DATE`, `DATETIME`, or `TIMESTAMP`  
`fixed32` | `INTEGER`, `NUMERIC`, `BIGNUMERIC`, or `DATE`  
`fixed64` | `NUMERIC` or `BIGNUMERIC`  
`sfixed32` | `INTEGER`, `NUMERIC`, `BIGNUMERIC`, or `DATE`  
`sfixed64` | `INTEGER`, `NUMERIC`, `BIGNUMERIC`, `DATE`, `DATETIME`, or `TIMESTAMP`  
`bool` | `BOOLEAN`  
`string` | `STRING`, `JSON`, `TIMESTAMP`, `DATETIME`, `DATE`, `TIME`, `NUMERIC`, or `BIGNUMERIC`  
`bytes` | `BYTES`, `NUMERIC`, or `BIGNUMERIC`  
`enum` | `INTEGER`  
`message` | `RECORD/STRUCT`  
`oneof` | Unmappable   
`map<KeyType, ValueType>` | `REPEATED RECORD<key KeyType, value ValueType>`  
`enum` | `INTEGER`  
`repeated/array of Type` | `REPEATED Type`  
  
## Date and time integer representation

When mapping from an integer to one of the date or time types, the number must represent the correct value. The following is the mapping from BigQuery data types to the integer that represents them.

**BigQuery Data Type** | **Integer Representation**  
---|---  
`DATE` | The number of days since the Unix epoch, January 1, 1970  
`DATETIME` | The date and time in microseconds expressed as civil time using the [CivilTimeEncoder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CivilTimeEncoder)  
`TIME` | The time in microseconds expressed as civil time using the [CivilTimeEncoder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.CivilTimeEncoder)  
`TIMESTAMP` | The number of microseconds since the Unix epoch, January 1, 1970 00:00:00 UTC  
  
## BigQuery change data capture ingestion

BigQuery subscriptions support [change data capture (CDC) ingestion updates](https://docs.cloud.google.com/bigquery/docs/change-data-capture) when [`use_topic_schema`](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription#use-topic-schema) or [`use_table_schema`](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription#use-table-schema) is set to `true` in the subscription properties. To use the feature with `use_topic_schema`, set the [schema](https://docs.cloud.google.com/pubsub/docs/schemas) of the topic with the following fields:

  * `_CHANGE_TYPE` (required): A `string` field set to `UPSERT` or `DELETE`.

    * If a Pub/Sub message written to the BigQuery table has `_CHANGE_TYPE` set to `UPSERT`, then BigQuery updates the row with the same key if it exists or inserts a new row if it does not.

    * If a Pub/Sub message written to the BigQuery table has `_CHANGE_TYPE` set to `DELETE`, then BigQuery deletes the row in the table with the same key if it exists.

  * `_CHANGE_SEQUENCE_NUMBER` (optional): A `string` field set to ensure that updates and deletes made to the BigQuery table are processed in order. Messages for the same row key must contain a monotonically increasing value for `_CHANGE_SEQUENCE_NUMBER`. Messages with sequence numbers that are less than the highest sequence number processed for a row don't have any effect on the row in the BigQuery table. The sequence number must follow the [`_CHANGE_SEQUENCE_NUMBER` format](https://docs.cloud.google.com/bigquery/docs/change-data-capture#format).




To use the feature with `use_table_schema`, include the preceding fields in the JSON message.

**Note:** When using BigQuery CDC ingestion, the BigQuery table must have a primary key. For more information, see [BigQuery CDC ingestion prerequisites](https://docs.cloud.google.com/bigquery/docs/change-data-capture#prerequisites).

For information about pricing, see [BigQuery CDC ingestion pricing](https://docs.cloud.google.com/bigquery/docs/change-data-capture#estimate-costs).

## Apache Iceberg tables managed by BigQuery

BigQuery subscriptions can be used with Iceberg managed tables with no additional changes required.

Iceberg managed tables provide the foundation for building open-format lakehouses on Google Cloud. These tables offer the same fully managed experience as [standard (built-in) BigQuery tables](https://docs.cloud.google.com/bigquery/docs/tables), but store data in customer-owned storage buckets using Parquet to be interoperable with Iceberg open table formats.

For information on how to create an Iceberg managed table in BigQuery, see [Create Iceberg managed tables](https://docs.cloud.google.com/bigquery/docs/iceberg-tables#create-iceberg-tables).

## Handle message failures

When a Pub/Sub message cannot be written to BigQuery, the message cannot be acknowledged. To forward such undeliverable messages, configure a [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead-letter_topic) on the BigQuery subscription. The Pub/Sub message forwarded to the dead-letter topic contains an attribute `CloudPubSubDeadLetterSourceDeliveryErrorMessage` that has the reason that the Pub/Sub message couldn't be written to BigQuery.

If Pub/Sub cannot write messages to BigQuery, then Pub/Sub backs off delivery of messages in a way similar to [push backoff behavior](https://docs.cloud.google.com/pubsub/docs/push#push_backoff). However, if the subscription has a [dead-letter topic](https://docs.cloud.google.com/pubsub/docs/handling-failures#dead-letter_topic) attached to it, Pub/Sub does not back off delivery when message failures are due to schema compatibility errors.

## Quotas and limits

There are quota limitations on the BigQuery subscriber throughput per region. For more information, see [Pub/Sub quotas and limits](https://docs.cloud.google.com/pubsub/quotas).

BigQuery subscriptions write data by using the [BigQuery Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api). For information about the quotas and limits for the Storage Write API (gRPC), see [Storage Write API (gRPC) requests](https://docs.cloud.google.com/bigquery/quotas#write-api-limits). BigQuery subscriptions only consume the throughput quota for the Storage Write API (gRPC). You can ignore the other Storage Write API (gRPC) quota considerations in this instance.

## Pricing

For the pricing for BigQuery subscriptions, see the [ Pub/Sub pricing page](https://cloud.google.com/pubsub/pricing#pubsub).

## What's next

  * Create a subscription, such as a [BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/create-bigquery-subscription).

  * Troubleshoot a [BigQuery subscription](https://docs.cloud.google.com/pubsub/docs/bigquery-troubleshooting).

  * Read about [BigQuery](https://docs.cloud.google.com/bigquery/docs).

  * Review pricing for Pub/Sub, including [ BigQuery subscriptions](https://cloud.google.com/pubsub/pricing).

  * Create or modify a subscription with [`gcloud` CLI commands](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions).

  * Create or modify a subscription with [REST APIs](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
