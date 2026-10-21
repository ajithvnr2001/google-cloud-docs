---
url: https://docs.cloud.google.com/dataflow/docs/use-cases/
title: Use cases for Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:36.079697+00:00
---

# Use cases for Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

##  Dataflow use cases 

![](https://docs.cloud.google.com/static/dataflow/images/ml-landing01.png)

Dataflow is designed to support streaming and batch pipelines at large scale. Dataflow is built on the open-source Apache Beam framework.

This page links to tutorials and example use cases to help you get started.

[About Dataflow](https://docs.cloud.google.com/dataflow/docs/overview) [About Apache Beam](https://docs.cloud.google.com/dataflow/docs/concepts/beam-programming-model)

##  Data movement 

###  [ Ingest data from Apache Iceberg tables into borderless Lakehouse ](https://docs.cloud.google.com/dataflow/docs/guides/iceberg-df-lakehouse-integration)

Learn how to use the Dataflow job builder to ingest data from external Apache Iceberg REST catalogs into Lakehouse managed tables. 

###  [ Import Parquet files from storage into borderless Lakehouse ](https://docs.cloud.google.com/dataflow/docs/guides/parquet-df-lakehouse-integration)

Learn how to use the Dataflow job builder to add existing Apache Parquet files from cloud storage to an Apache Iceberg table in Lakehouse. 

###  [ Import Delta Lake tables into borderless Lakehouse ](https://docs.cloud.google.com/dataflow/docs/guides/delta-lake-df-lakehouse-integration)

Learn how to use the Dataflow job builder to import existing Delta Lake tables from Google Cloud Storage into Lakehouse. 

###  [ Process data from Kafka to BigQuery ](https://docs.cloud.google.com/dataflow/docs/kafka-dataflow)

This tutorial shows how to run a Dataflow template that reads from Managed Service for Apache Kafka and writes the records to a BigQuery table. 

###  [ Process data from Pub/Sub to BigQuery ](https://docs.cloud.google.com/dataflow/docs/tutorials/dataflow-stream-to-bigquery)

This tutorial shows how to run a Dataflow template that reads JSON-encoded messages from Pub/Sub and writes them to a BigQuery table. 

##  Dataflow ML 

###  [ Use RunInference and Embeddings ](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_huggingface)

This notebook shows how to use ML models in Apache Beam pipelines that use the RunInference transform. 

###  [ Use GPUs in your pipeline ](https://docs.cloud.google.com/dataflow/docs/notebooks/run_inference_vllm)

This notebook shows how to run machine learning inference by using vLLM and GPUs. vLLM is a library for LLM inference and serving. 

##  Other resources 

###  [ Reference patterns ](https://docs.cloud.google.com/dataflow/docs/tutorials/reference-patterns)

Links to sample code and technical reference guides for common Dataflow use cases. 

###  [ Ecommerce streaming pipeline ](https://docs.cloud.google.com/dataflow/docs/tutorials/ecommerce-retail-pipeline)

In this tutorial, you create a pipeline that transforms ecommerce data from Pub/Sub and outputs the data to BigQuery and Bigtable. 

###  [ HPC highly parallel workloads ](https://docs.cloud.google.com/dataflow/docs/hpc-ep)

With Dataflow, you can run highly parallel workloads in a single pipeline, improving efficiency and making your workflow easier to manage. 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-26 UTC."],[],[]] 
