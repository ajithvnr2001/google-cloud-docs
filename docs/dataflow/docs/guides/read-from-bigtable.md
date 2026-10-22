---
url: https://docs.cloud.google.com/dataflow/docs/guides/read-from-bigtable/
title: Read from Bigtable to Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:12.896906+00:00
---

# Read from Bigtable to Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/read-from-bigtable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Read from Bigtable to Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Operational data stored in Bigtable often needs to be processed, aggregated, or exported for downstream analytics without degrading performance for live applications. Ingesting Bigtable data into Dataflow lets you use scalable, parallel pipelines to handle high-volume operational records for ETL workflows, analytical aggregations, and data lake exports.

To build custom data pipelines, you can use the Apache Beam [Bigtable I/O connector](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigtable/package-summary.html). For common tasks such as exporting tables to Cloud Storage, you can also use [Google-provided Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates) to deploy prebuilt pipelines without writing custom code.

## Parallelism

Parallelism is controlled by the number of [nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes) in the Bigtable cluster. Each node manages one or more key ranges, although key ranges can move between nodes as part of [load balancing](https://docs.cloud.google.com/bigtable/docs/overview#load-balancing). For more information, see [Reads and performance](https://docs.cloud.google.com/bigtable/docs/reads#performance) in the Bigtable documentation.

You are charged for the number of nodes in your instance's clusters. See [Bigtable pricing](https://cloud.google.com/bigtable/pricing).

## Performance

The following table shows performance metrics for Bigtable read operations. The workloads were run on one `e2-standard2` worker, using the Apache Beam SDK 2.48.0 for Java. They did not use the Portable Runner.

100 M records | 1 kB | 1 column | Throughput (bytes) | Throughput (elements)  
---|---|---  
[Read](https://github.com/apache/beam/blob/master/it/google-cloud-platform/src/test/java/org/apache/beam/it/gcp/bigtable/BigTableIOLT.java#L117) | 180 MBps | 170,000 elements per second  
  
These metrics are based on simple batch pipelines. They are intended to compare performance between I/O connectors, and are not necessarily representative of real-world pipelines. Dataflow pipeline performance is complex, and is a function of VM type, the data being processed, the performance of external sources and sinks, and user code. Metrics are based on running the Java SDK, and aren't representative of the performance characteristics of other language SDKs. For more information, see [Beam IO Performance](https://beam.apache.org/performance/).

## Best practices

  * For new pipelines, use the [`BigtableIO`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigtable/BigtableIO.html) connector, not `CloudBigtableIO`.

  * Create separate [app profiles](https://docs.cloud.google.com/bigtable/docs/app-profiles) for each type of pipeline. App profiles enable better metrics for differentiating traffic between pipelines, both for support and for tracking usage.

  * Monitor the Bigtable nodes. If you experience performance bottlenecks, check whether resources such as CPU utilization are constrained within Bigtable. For more information, see [Monitoring](https://docs.cloud.google.com/bigtable/docs/monitoring-instance).

  * In general, the default timeouts are well tuned for most pipelines. If a streaming pipeline appears to get stuck reading from Bigtable, try calling [`withAttemptTimeout`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigtable/BigtableIO.Read.html#withAttemptTimeout-org.joda.time.Duration-) to adjust the attempt timeout.

  * Consider enabling [Bigtable autoscaling](https://docs.cloud.google.com/bigtable/docs/autoscaling), or resize the Bigtable cluster to scale with the size of your Dataflow jobs.

  * Consider setting [`maxNumWorkers`](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#resource_utilization) on the Dataflow job to limit load on the Bigtable cluster.

  * If significant processing is done on a Bigtable element before a shuffle, calls to Bigtable might time out. In that case, you can call [`withMaxBufferElementCount`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigtable/BigtableIO.Read.html#withMaxBufferElementCount-java.lang.Integer-) to buffer elements. This method converts the read operation from streaming to paginated, which avoids the issue.

  * If you use a single Bigtable cluster for both streaming and batch pipelines, and the performance degrades on the Bigtable side, consider setting up replication on the cluster. Then separate the batch and streaming pipelines, so that they read from different replicas. For more information, see [Replication overview](https://docs.cloud.google.com/bigtable/docs/replication-overview).




## What's next

  * Read the [Bigtable I/O connector](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigtable/package-summary.html) documentation.
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
