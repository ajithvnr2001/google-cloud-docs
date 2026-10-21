---
url: https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-about/
title: About Dataflow HPC highly parallel workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:56.525844+00:00
---

# About Dataflow HPC highly parallel workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-about/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  About Dataflow HPC highly parallel workloads Stay organized with collections  Save and categorize content based on your preferences. 

Highly parallel workloads, also known as [embarrassingly parallel](https://wikipedia.org/wiki/Embarrassingly_parallel) workloads, are common in finance, media, and life-sciences enterprises. For parallel workloads like these, enterprises typically deploy a cluster of compute nodes. Each node can carry out independent processing tasks, in a configuration referred to as [grid computing](https://wikipedia.org/wiki/Grid_computing). To process data for parallel workloads, you can use [Apache Beam](https://beam.apache.org/get-started/beam-overview/) with Dataflow. For more information about Apache Beam, see the [Apache Beam programming guide](https://beam.apache.org/documentation/programming-guide/).

Using Dataflow for highly parallel workloads provides many benefits.

  * Create a fully-managed workflow, with data processing and orchestration in the same pipeline. 
    * The Dataflow user interface and API include [observability features](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview).
    * Dataflow has [centralized logging](https://docs.cloud.google.com/dataflow/docs/guides/logging) for all pipeline stages.
    * Dataflow offers [autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling) to maximize performance and optimize resource usage.
    * Dataflow is [fault tolerant](https://docs.cloud.google.com/dataflow/docs/guides/pipeline-workflows#geographic-redundancy) and provides dynamic load balancing.
    * Dataflow offers [straggler detection and correction](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-batch-stragglers).
  * Use a single system for all aspects of the pipeline, for both pre- and post-processing and for task processing. You can even use your existing C++ code in the pipeline.
  * Use the built-in [exactly once processing](https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once) that Dataflow provides.



In addition, Dataflow includes various security features:

  * Use [customer-managed encryption key (CMEK)](https://docs.cloud.google.com/dataflow/docs/guides/customer-managed-encryption-keys) with your pipeline.
  * Define [firewall rules](https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall) for the network associated with your Dataflow job.
  * Use a [VPC network](https://docs.cloud.google.com/dataflow/docs/guides/specifying-networks).



These workloads require distribution of data to functions that run across many cores. This distribution often requires very high concurrency reads followed by a large fan-out of data, absorbed by downstream systems. The core competencies of Dataflow are the distribution of batch and stream workloads across resources and managing autoscaling and dynamic work rebalancing across these resources. Therefore, when you use Dataflow for your highly parallel workloads, performance, scalability, availability, and security needs are handled automatically.

## Incorporate external code into your pipeline

Apache Beam has built-in SDKs for Java, Python, and Go. However, many highly parallel workloads use code written in C++. You can use Dataflow and other Google Cloud services to run C++ binaries (libraries) as external code using Apache Beam. Including C++ binaries lets you unlock these types of workloads using fully managed services. It also gives you the ability to build complete pipelines using a sophisticated [directed acyclic graph](https://wikipedia.org/wiki/Directed_acyclic_graph#Data_processing_networks) (DAG).

The same approach for running C++ binaries is also relevant for code written in other languages where you can compile a standalone binary.

## End-to-end highly parallel pipelines

With Dataflow, you can do the I/O read and write processing, analysis, and task output all in the same pipeline. This lets you run complete highly parallel pipelines.

For example, an HPC highly parallel workload might incorporate the following steps:

  1. Ingest raw data, both from internal and external sources. Data might come from unbounded or bounded sources. Unbounded sources are mostly converted to bounded sources to accommodate the technologies used for task farming.

  2. Pre-process the raw data into a data shape and encoding that the task farming component can use.

  3. Use a system to distribute the calculations to hosts and to retrieve data from a source, and then materialize the results for post-analysis.

  4. Conduct post-analysis to convert the results into output.




You can use Dataflow to manage all of these steps in a single pipeline while taking advantage of Dataflow features:

  * Because a single system is responsible for all stages, you don't need an external orchestration system to coordinate the running of multiple pipelines.

  * With data locality, you don't need to explicitly materialize and dematerialize between the stage boundaries, increasing efficiency.

  * With better in-system telemetry, information about the total bytes in stage is available, which helps with designing later stages.

  * With autoscaling, when the data is in the system, the resources scale based on the data volumes as the data moves through the pipeline stages.




The core Dataflow HPC highly parallel pipeline uses modern DAG execution engines. All the typical pipeline processes can be completed in a single DAG and, therefore, a single Dataflow pipeline. You can use a DAG generated by Apache Beam to define the shape of the pipeline.

If you're migrating from a task farm system to a highly parallel workflow, you need to shift from tasks to data. A `PTransform` contains a [`DoFn`](https://beam.apache.org/documentation/programming-guide/#creating-a-dofn), which has a process function that takes in a data element. The data point can be any object with one or more properties.

By using a DAG and a single pipeline, you can load all the data within the system during the entire workflow. You don't need to output data to databases or storage.

## Google Cloud components used with highly parallel workflows

Grid computing applications require data to be distributed to functions running on many cores. This pattern often requires high-concurrency reads and is often followed by a large fan-out of data absorbed by downstream systems.

Dataflow is integrated with other Google Cloud managed services that can absorb massive-scale parallelized data I/O:

  * Pub/Sub: global event stream ingestion service
  * Bigtable: wide-column store for caching and serving
  * Cloud Storage: unified object store
  * BigQuery: petabyte-scale data warehouse service



Used together, these services provide a compelling solution for highly parallel workloads.

Common architecture for highly parallel workloads running on Google Cloud includes the following:

  * The [Dataflow Runner for Apache Beam](https://beam.apache.org/documentation/runners/dataflow/). This runner distributes work to the grid nodes with a processing flow derived from a DAG. A single Apache Beam DAG lets you define complex multi-stage pipelines in which parallel pipelined stages can be brought back together using [side-inputs](https://beam.apache.org/documentation/programming-guide/#side-inputs) or [joins](https://beam.apache.org/documentation/programming-guide/#cogroupbykey).

  * [Cloud Storage](https://docs.cloud.google.com/storage/docs). This service provides a location to stage the C++ binaries. When large files need to be stored, as in many media use cases, those files also reside in Cloud Storage.

  * [Bigtable](https://docs.cloud.google.com/bigtable/docs), [BigQuery](https://docs.cloud.google.com/bigquery/docs), and [Pub/Sub](https://docs.cloud.google.com/pubsub/docs). These services are used as both sources and sinks.




The following diagram outlines high-level architecture for an example workflow.

![Architecture of a grid computing solution](https://docs.cloud.google.com/static/dataflow/images/running-external-binaries-beam-grid-computing-architecture.svg)

You can also use other storage systems. For details, see the list of storage systems and streaming sources in the [pipeline I/O page](https://beam.apache.org/documentation/io/built-in) in the Apache Beam documentation.

### The Dataflow runner for Apache Beam

Use Dataflow to transform and enrich your data in both streaming and batch modes. Dataflow is based on [Apache Beam](https://beam.apache.org/).

### Cloud Storage

[Cloud Storage](https://docs.cloud.google.com/storage/docs) is a unified object storage that encompasses live data serving, data analytics, machine learning (ML), and data archiving. For highly parallel workloads with Dataflow, Cloud Storage provides access to C++ binaries. In some use cases, Cloud Storage also provides the location for data needed by the processing phase.

For the high-burst loads required by grid computing, you need to understand Cloud Storage performance characteristics. For more information about Cloud Storage data-serving performance, see [Request Rate and Access Distribution Guidelines](https://docs.cloud.google.com/storage/docs/request-rate) in the Cloud Storage documentation.

### Bigtable

[Bigtable](https://docs.cloud.google.com/bigtable/docs) is a high-performance NoSQL database service optimized for large analytical and operational workloads. Bigtable is complementary to Dataflow. The primary characteristics of Bigtable, low latency reads and writes (6 ms on the 90th percentile), allow it to handle many thousands of concurrent clients and heavy-burst workloads. These features make Bigtable ideal as a sink and as a data source within the `DoFn` function in the processing phase of Dataflow.

### BigQuery

[BigQuery](https://docs.cloud.google.com/bigquery/docs) is a fast, economical, and fully managed enterprise data warehouse for large-scale data analytics. Grid results are often used for analysis, and enable you to run large-scale aggregations against the data output of the grid.

### Pub/Sub

[Pub/Sub](https://docs.cloud.google.com/pubsub/docs) is an asynchronous and scalable messaging service that decouples services producing messages from services processing those messages. You can use Pub/Sub for streaming analytics and data integration pipelines to ingest and distribute data. It's equally effective as a messaging-oriented middleware for service integration or as a queue to parallelize tasks.

### The Dataflow DAG

You can use the Apache Beam SDK to build expressive DAGs, which in turn lets you create stream or batch multi-stage pipelines. Data movement is handled by the runner, with data expressed as [`PCollection`](https://beam.apache.org/documentation/programming-guide/#pcollections) objects, which are immutable parallel element collections.

The following diagram illustrates this flow.

![Flow using
DAG](https://docs.cloud.google.com/static/dataflow/images/running-external-binaries-beam-grid-computing-flow-using-dag.svg)

The Apache Beam SDK lets you define a DAG. In the DAG, you can include user-defined code as functions. Normally, the same programming language (Java, Python, or Go) is used for both the declaration of the DAG and for the user-defined code. You can also use code that isn't built-in, such as C++, for the user-defined code.

## What's next

  * Learn about [best practices](https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-best-practices) for working with Dataflow HPC highly parallel pipelines.
  * Follow the [tutorial](https://docs.cloud.google.com/dataflow/docs/hpc-ep/hpc-tutorial) to create a pipeline that uses custom containers with C++ libraries.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
