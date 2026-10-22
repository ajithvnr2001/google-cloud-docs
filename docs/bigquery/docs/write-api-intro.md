---
url: https://docs.cloud.google.com/bigquery/docs/write-api-intro/
title: Introduction to the Storage Write API \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:55.671417+00:00
---

# Introduction to the Storage Write API  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/write-api-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to the Storage Write API

The BigQuery Storage Write API is a unified data-ingestion API that you can use to stream records into BigQuery in real time. The Storage Write API is available through both gRPC and REST endpoints.

## Choose a streaming approach

You can use the Storage Write API in two ways, through [gRPC streaming](https://docs.cloud.google.com/bigquery/docs/write-api) or through the [REST endpoint](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery). gRPC streaming is ideal for long-lived connections and continuous streaming, while the REST endpoint is best for ephemeral, stateless, or constrained environments.

For new workloads, we recommend using gRPC streaming for the following reasons:

  * **Efficient protocol.** gRPC streaming is more efficient than REST over HTTP. It also supports the [protocol buffer](https://protobuf.dev/) binary format and the [Apache Arrow](https://arrow.apache.org/) columnar format, which are more efficient wire formats than JSON. Write requests are asynchronous with guaranteed ordering.
  * **Lower cost**. gRPC streaming has a significantly lower cost than REST. In addition, you can ingest up to 2 TiB per month for free.
  * **Exactly-once delivery semantics.** gRPC streaming supports exactly-once semantics through the use of stream offsets, and it never writes two messages that have the same offset within a stream, if the client provides stream offsets when appending records.
  * **Stream-level transactions.** With gRPC streaming, you can write data to a stream and commit the data as a single transaction. If the commit operation fails, you can safely retry the operation.
  * **Transactions across streams.** With gRPC streaming, multiple workers can create their own streams to process data independently. When all the workers finish, you can commit all of the streams as a transaction.
  * **Schema update detection.** With gRPC streaming, if the underlying table schema changes while the client is streaming, then the API notifies the client. The client can decide whether to reconnect using the updated schema, or continue to write to the existing connection.



The following diagram illustrates other technical details to be aware of when selecting a streaming approach:

![Diagram for choosing Storage Write API streaming approach.](https://docs.cloud.google.com/static/bigquery/images/storage-write-api-protocol-selection.svg)

## What's next

  * Learn more about the [BigQuery Storage Write API (gRPC)](https://docs.cloud.google.com/bigquery/docs/write-api).
  * Learn more about the [BigQuery Storage Write API (REST)](https://docs.cloud.google.com/bigquery/docs/streaming-data-into-bigquery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
