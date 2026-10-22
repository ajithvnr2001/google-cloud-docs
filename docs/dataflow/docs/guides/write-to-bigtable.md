---
url: https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigtable/
title: Write from Dataflow to Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:32.421128+00:00
---

# Write from Dataflow to Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/write-to-bigtable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Write from Dataflow to Bigtable Stay organized with collections  Save and categorize content based on your preferences. 

To write data from Dataflow to Bigtable, use the Apache Beam [Bigtable I/O connector](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigtable/package-summary.html).

**Note:** Depending on your scenario, consider using one of the [Google-provided Dataflow templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates). Several of these write to Bigtable.

## Parallelism

Parallelism is controlled by the number of [nodes](https://docs.cloud.google.com/bigtable/docs/instances-clusters-nodes#nodes) in the Bigtable cluster. Each node manages one or more key ranges, although key ranges can move between nodes as part of [load balancing](https://docs.cloud.google.com/bigtable/docs/overview#load-balancing). For more information, see [Understand performance](https://docs.cloud.google.com/bigtable/docs/performance) in the Bigtable documentation.

You are charged for the number of nodes in your instance's clusters. See [Bigtable pricing](https://cloud.google.com/bigtable/pricing).

## Performance

The following table shows performance metrics for Bigtable I/O write operations. The workloads were run on one `e2-standard2` worker, using the Apache Beam SDK 2.48.0 for Java. They did not use the Portable Runner.

100M record | 1kB | 1 column | Throughput (bytes) | Throughput (elements)  
---|---|---  
[Write](https://github.com/apache/beam/blob/master/it/google-cloud-platform/src/test/java/org/apache/beam/it/gcp/bigtable/BigTableIOLT.java#L117) | 65 MBps | 60,000 elements per second  
  
These metrics are based on simple batch pipelines. They are intended to compare performance between I/O connectors, and are not necessarily representative of real-world pipelines. Dataflow pipeline performance is complex, and is a function of VM type, the data being processed, the performance of external sources and sinks, and user code. Metrics are based on running the Java SDK, and aren't representative of the performance characteristics of other language SDKs. For more information, see [Beam IO Performance](https://beam.apache.org/performance/).

## Best practices

  * In general, avoid using transactions. Transactions aren't guaranteed to be idempotent, and Dataflow might invoke them multiple times due to retries, causing unexpected values.

  * A single Dataflow worker might process data for many key ranges, leading to inefficient writes to Bigtable. Using `GroupByKey` to group data by Bigtable key can significantly improve write performance.

  * If you write large datasets to Bigtable, consider calling [`withFlowControl`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigtable/BigtableIO.Write.html#withFlowControl-boolean-). This setting automatically rate-limits traffic to Bigtable, to ensure the Bigtable servers have enough resources available to serve data.




## What's next

  * Read the [Bigtable I/O connector](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/bigtable/package-summary.html) documentation.
  * See the list of [Google-provided templates](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided-templates).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
