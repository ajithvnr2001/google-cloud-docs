---
url: https://docs.cloud.google.com/dataflow/docs/concepts/parallelism/
title: Understand parallelism in Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:54.879692+00:00
---

# Understand parallelism in Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/concepts/parallelism/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Understand parallelism in Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Dataflow is designed to execute large data processing pipelines by distributing work across a managed pool of compute instances. Understanding how Dataflow parallelizes processing helps you design efficient pipelines, avoid performance bottlenecks, and optimize resource costs.

This page explains how Dataflow parallelizes data processing, how it manages and scales execution, the common factors that constrain parallelism, and techniques you can use to optimize pipeline throughput.

## Parallelism models: Horizontal versus vertical

Dataflow achieves parallelism using two complementary strategies:

  * **Horizontal parallelism:** Pipeline data is partitioned and processed across multiple worker instances (virtual machines) concurrently. Dataflow can automatically adjust the worker pool size based on workload demand through [Horizontal Autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling). By default, Dataflow sets a resource limit of 4,000 workers per job, which can be adjusted using [quota requests](https://docs.cloud.google.com/dataflow/docs/request-quotas).

  * **Vertical parallelism:** Multiple CPU cores and threads within a single worker instance process pipeline data concurrently. Each worker VM runs worker processes and harness threads to use available compute resources. With [dynamic thread scaling](https://docs.cloud.google.com/dataflow/docs/guides/thread-scaling), Dataflow can adjust the number of active threads per worker in batch pipelines based on CPU utilization and memory headroom. In [Dataflow Prime](https://docs.cloud.google.com/dataflow/docs/guides/enable-dataflow-prime), [Vertical Autoscaling](https://docs.cloud.google.com/dataflow/docs/vertical-autoscaling) dynamically scales memory and compute allocated to workers.




## Work units and execution hierarchy

To distribute processing across workers and threads, Dataflow breaks Apache Beam pipelines into discrete units of work:

  * **PCollections and partitions:** A `PCollection` represents a distributed dataset. For bounded data (batch pipelines), Dataflow divides the dataset into splits or shards. For unbounded data (streaming pipelines), data arrives continuously and is ingested as messages or stream partitions.
  * **Bundles:** Dataflow groups elements into arbitrary bundles for processing by a `DoFn`. A bundle is the unit of failure and retry: if processing an element raises an unhandled exception, the entire bundle is retried. Operations with high memory consumption can increase worker memory pressure and lead to out-of-memory errors.
  * **Stages and step fusion:** During graph optimization, Dataflow combines adjacent transforms into fused execution stages to eliminate the overhead of intermediate data materialization. Within a fused stage, elements are processed in a tight execution loop on a single thread before being passed to the next stage or shuffle boundary.



For more details on pipeline translation and graph generation, see [Pipeline lifecycle](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle).

## Managed parallelism and autoscaling

By default, Dataflow manages pipeline parallelism automatically without requiring manual partition tuning in the following ways:

  * **Horizontal Autoscaling:**
    * **Batch pipelines:** Evaluates the total estimated remaining work, source backlog, and CPU usage to scale the worker pool up or down to complete the job quickly and cost-effectively.
    * **Streaming pipelines:** Analyzes system latency, backlog size, and CPU utilization to scale workers up during throughput spikes and scale down during low-traffic periods. For details, see [Tune Streaming Horizontal Autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling).
  * **Dynamic Work Rebalancing (DWR):** In batch pipelines, Dataflow monitors the progress of individual worker tasks. If a worker finishes early or another worker lags behind due to data skew (stragglers), Dataflow dynamically splits the residual unprocessed work from the slow worker and reassigns it to an idle worker. For more information, see [Dynamic work rebalancing](https://docs.cloud.google.com/dataflow/docs/dynamic-work-rebalancing).
  * **Dynamic thread scaling:** In batch pipelines that use the Portable Runner, automatically adjusts the number of concurrent processing threads per worker based on CPU utilization and memory headroom. For more information, see [Dynamic thread scaling](https://docs.cloud.google.com/dataflow/docs/guides/thread-scaling).
  * **Vertical Autoscaling:** In Dataflow Prime, Dataflow dynamically scales worker memory and compute resources to prevent out-of-memory errors and optimize resource utilization. For more information, see [Vertical Autoscaling](https://docs.cloud.google.com/dataflow/docs/vertical-autoscaling).



## Factors that constrain parallelism

A pipeline might not achieve expected parallelism due to the following data characteristics or pipeline graph design:

### Unsplittable input sources

If an input source can't be split into independent ranges, Dataflow is forced to read the source sequentially with a single worker thread:

  * **Non-splittable file compression:** Formats like `.gz` (gzip) or `.bzip2` (without indexing) can't be read in parallel from arbitrary byte offsets. Reading a single large compressed file restricts the ingestion stage to a single thread until the data is decompressed and redistributed.
  * **Resolution:** Store data in splittable file formats (such as Parquet, Avro, or Snappy-compressed formats) or split input data into multiple smaller files in Cloud Storage.



### Step fusion and high fan-out

Step fusion improves performance by reducing serialization overhead, but it can inadvertently limit parallelism and increase memory pressure when a step with low parallelism produces a large number of output elements (a "high fan-out" operation):

  * **Example:** A source reads five files and is fused with a `FlatMap` transform that produces 1,000,000 output elements. If the `FlatMap` transform is fused with downstream transforms, all 1,000,000 elements continue to execute on at most five worker threads, severely limiting downstream throughput. Furthermore, if intermediate transforms expand significantly in memory before committing, large bundles can exhaust available worker memory.
  * **Resolution:** Insert a `Redistribute` (or classic `Reshuffle`) transform between the high fan-out step and downstream transforms to break fusion and redistribute work across the worker pool. For debugging related memory issues, see [Troubleshoot out of memory errors](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-oom).



### Key skew and hot keys

Aggregation operations (`GroupByKey`, `CoGroupByKey`, `Combine.PerKey`) group elements by their associated key.

  * **Hot key bottleneck:** Dataflow routes all elements with the same key to a single worker thread for aggregation. If a single key contains a large percentage of the total dataset, that worker becomes a straggler, and upstream workers might experience backpressure. For example, a default `null` key or an extremely popular category key.
  * **Resolution:**
    1. Use [Combiners](https://beam.apache.org/documentation/programming-guide/#transforms-combine) (`CombineFn` or `Combine.PerKey`) instead of `GroupByKey` where possible, allowing Dataflow to perform partial local combinations before shuffle.
    2. Add a random integer prefix or suffix to hot keys (_key salting_) to distribute the key space across workers, followed by a second-stage aggregation to merge the salted results.



### Downstream sink throttling

When writing pipeline output to external services such as databases or third-party APIs, high parallelism can saturate the destination system:

  * **Throttling:** Hundreds of worker threads issuing concurrent write calls can lead to rate-limit errors, connection timeouts, or database degradation.
  * **Resolution:**
    * Limit write parallelism by grouping elements with `GroupByKey` or using batching sinks with controlled parallelism.
    * Implement client-side exponential backoff and retry logic in sink `DoFn` implementations.



## Optimization strategies

To optimize parallelism in your Dataflow jobs, consider the following approaches:

  * **Prevent undesirable fusion with`Redistribute`:**
    * `Redistribute.arbitrarily()`: Breaks step fusion and redistributes elements evenly across all available workers.
    * `Redistribute.byKey()`: Rebalances key-value pairs across worker threads while preserving key locality.
    * For implementation examples, see [Prevent fusion](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#prevent_fusion).
  * **Monitor stragglers and bottlenecks:** Use the Google Cloud console execution details to identify stages with high straggler counts or stalled progress: 
    * [Troubleshoot stragglers in batch jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-batch-stragglers)
    * [Troubleshoot stragglers in streaming jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-streaming-stragglers)
    * [Detect and resolve bottlenecks](https://docs.cloud.google.com/dataflow/docs/guides/detect-resolve-bottlenecks)



## What's next

  * Learn about the [Pipeline lifecycle](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle).
  * Explore [Horizontal Autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling).
  * Understand [Dynamic work rebalancing](https://docs.cloud.google.com/dataflow/docs/dynamic-work-rebalancing).
  * Review [Dataflow pipeline best practices](https://docs.cloud.google.com/dataflow/docs/guides/pipeline-best-practices).
  * Learn how to [Troubleshoot out of memory errors](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-oom).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
