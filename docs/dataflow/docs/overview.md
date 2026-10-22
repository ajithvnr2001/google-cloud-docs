---
url: https://docs.cloud.google.com/dataflow/docs/overview/
title: Dataflow overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:17.735491+00:00
---

# Dataflow overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow overview Stay organized with collections  Save and categorize content based on your preferences. 

Dataflow is a Google Cloud service that provides unified stream and batch data processing at scale. Use Dataflow to create data pipelines that read from one or more sources, transform the data, and write the data to a destination.

Typical use cases for Dataflow include the following:

  * Data movement: Data ingestion or replication across subsystems.
  * [ETL](https://cloud.google.com/learn/what-is-etl) (extract-transform-load) workflows that ingest data into a data warehouse such as BigQuery.
  * Backend support for business intelligence (BI) dashboards.
  * Real-time machine learning (ML) analysis of streaming data.
  * Sensor data processing or log data processing at scale.



Dataflow uses the same programming model for both batch and stream analytics. Streaming pipelines can achieve low latency. You can ingest, process, and analyze fluctuating volumes of real-time data. By default, Dataflow provides [exactly-once processing](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once) of every record. For streaming pipelines that can tolerate duplicates, you can reduce cost and improve latency by enabling [at-least-once mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes).

## Advantages for data processing with Dataflow

This section describes some of the advantages of using Dataflow.

### Managed data processing

Dataflow is a fully managed service. That means Google manages all of the resources needed to run Dataflow. When you run a Dataflow job, the Dataflow service allocates a pool of worker VMs to execute the pipeline. You don't need to provision or manage these VMs. When the job completes or is cancelled, Dataflow automatically deletes the VMs. You're billed for the compute resources that your job uses. For more information about costs, see [Dataflow pricing](https://cloud.google.com/dataflow/pricing).

### Scalable data pipelines

Dataflow is designed to support batch and streaming pipelines at large scale. Data is processed in parallel, so the work is distributed across multiple VMs.

Dataflow can autoscale by provisioning extra worker VMs, or by shutting down some worker VMs if fewer are needed. It also optimizes the work, based on the characteristics of the pipeline. For example, Dataflow can [dynamically rebalance work](https://docs.cloud.google.com/dataflow/docs/dynamic-work-rebalancing) among the VMs, so that parallel work completes more efficiently.

### Portable with Apache Beam

Dataflow is built on the open source [Apache Beam](https://beam.apache.org/) project. Apache Beam lets you write pipelines using a language-specific SDK. Apache Beam supports Java, Python, and Go SDKs, as well as [multi-language pipelines](https://beam.apache.org/documentation/programming-guide/#multi-language-pipelines).

Dataflow executes Apache Beam pipelines. If you decide later to run your pipeline on a different platform, such as Apache Flink or Apache Spark, you can do so without rewriting the pipeline code.

### Flexible data pipeline development

You can use Dataflow for pipelines with straightforward use cases, such as just moving data. However, Dataflow is also suitable for more advanced applications, such as real-time streaming analytics. A solution built on Dataflow can grow with your needs as you move from batch to streaming or encounter more advanced use cases.

Dataflow supports several different ways to create and execute pipelines, depending on your needs:

  * Write code using the Apache Beam SDKs.

  * Deploy a [Dataflow template](https://docs.cloud.google.com/dataflow/docs/concepts/dataflow-templates). Templates let you run predefined pipelines. For example, a developer can create a template, and then a data scientist can deploy it on demand.

Google also provides a [library of templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) for common scenarios. You can deploy these templates without knowing any Apache Beam programming concepts.

  * Use [JupyterLab notebooks](https://docs.cloud.google.com/dataflow/docs/guides/interactive-pipeline-development) to develop and run pipelines iteratively.




### Observable data pipeline jobs

You can monitor the status of your Dataflow jobs through the [Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview) in the Google Cloud console. The monitoring interface includes a graphical representation of your pipeline, showing the progress and [execution details](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details) of each pipeline stage. The monitoring interface makes it easier to spot problems such as bottlenecks or high latency. You can also [profile your Dataflow jobs](https://docs.cloud.google.com/dataflow/docs/guides/profiling-a-pipeline) to monitor CPU usage and memory allocation.

## How data pipelines work for stream and batch processing

Dataflow uses a data pipeline model, where data moves through a series of stages. Stages can include reading data from a source, transforming and aggregating the data, and writing the results to a destination.

Pipelines can range from very basic to more complex processing. For example, a pipeline might do the following:

  * Move data as-is to a destination.
  * Transform data to be more usable by the target system.
  * Aggregate, process, and enrich data for analysis.
  * Join data with other data.



A pipeline that is defined in Apache Beam does not specify _how_ the pipeline is executed. Running the pipeline is the job of a [_runner_](https://beam.apache.org/documentation/basics/#runner). The purpose of a runner is to run an Apache Beam pipeline on a specific platform. Apache Beam supports multiple runners, including a [Dataflow runner](https://beam.apache.org/documentation/runners/dataflow/).

To use Dataflow with your Apache Beam pipelines, specify the Dataflow runner. The runner uploads your executable code and dependencies to a Cloud Storage bucket and creates a Dataflow _job_. Dataflow then allocates a pool of VMs to execute the pipeline.

The following diagram shows a typical ETL and BI solution using Dataflow and other Google Cloud services:

![Diagram of an ETL and BI solution that uses Dataflow.](https://docs.cloud.google.com/static/dataflow/images/dataflow-pipeline-example.png)

This diagram shows the following stages:

  1. Pub/Sub ingests data from an external system.
  2. Dataflow reads the data from Pub/Sub and writes it to BigQuery. During this stage, Dataflow might transform or aggregate the data.
  3. BigQuery acts as a data warehouse, allowing data analysts to run ad hoc queries on the data.
  4. Looker provides real-time BI insights from the data stored in BigQuery.



For basic data movement scenarios, you might run a Google-provided template. Some templates support user-defined functions (UDFs) written in JavaScript. UDFs let you add custom processing logic to a template. For more complex pipelines, start with the Apache Beam SDK.

## What's next

  * For more information about Apache Beam, see [Programming model for Apache Beam](https://docs.cloud.google.com/dataflow/docs/concepts/beam-programming-model).
  * Create your first pipeline by following the [Job builder quickstart](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-job-builder) or [Dataflow template quickstart](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-streaming-pipeline-template).
  * Learn how to [use Apache Beam to build pipelines](https://docs.cloud.google.com/dataflow/docs/guides/use-beam).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
