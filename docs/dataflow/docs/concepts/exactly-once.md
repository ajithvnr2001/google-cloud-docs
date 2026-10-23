---
url: https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once/
title: Exactly-once in Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:25.912720+00:00
---

# Exactly-once in Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/concepts/exactly-once/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Exactly-once in Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

Dataflow supports exactly-once processing of records. This page explains how Dataflow implements exactly-once processing while also ensuring low latency.

## Overview

Batch pipelines always use exactly-once processing. Streaming pipelines use exactly-once processing by default, but can also use [at-least-once processing](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes).

Exactly-once processing provides assurances about record processing results, including the results from each pipeline stage. Specifically, for each record that arrives to the pipeline from a source, or arrives at a stage from a previous stage, Dataflow ensures the following:

  * The record is processed and not lost.
  * Any results of processing that stay within the pipeline are reflected at most once.



In other words, records are processed at least once, and the results are committed exactly once.

Exactly-once processing ensures that results are accurate, with no duplicate records in the output. Dataflow is optimized to minimize latency while maintaining exactly-once semantics. However, exactly-once processing still incurs cost to perform deduplication. For use cases that can tolerate duplicate records, you can often reduce cost and improve latency by enabling at-least-once mode. For more information about choosing between exactly-once and at-least-once streaming, see [Set the pipeline streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes).

### Late data

Exactly-once processing ensures the _accuracy_ of the pipeline: If the pipeline processes a record, then Dataflow ensures that the record is reflected in the output, and that the record is not duplicated.

In a streaming pipeline, however, exactly-once processing cannot guarantee that results are _complete_ , because records might arrive late. For example, suppose your pipeline performs an aggregation over a time window, such as `Count`. With exactly-once processing, the result is accurate for the records that arrive within the window in a timely fashion, but late records might be dropped.

Generally, there is no way to guarantee completeness in a streaming pipeline, because in theory records can arrive arbitrarily late. In the limiting case you would need to wait forever to produce a result. More practically, Apache Beam lets you configure the threshold for dropping late data and when to emit aggregated results. For more information, see [Watermarks and late data](https://beam.apache.org/documentation/programming-guide/#watermarks-and-late-data) in the Apache Beam documentation.

### Side effects

Side effects are not guaranteed to have exactly-once semantics. Importantly, this includes writing output to an external store, unless the sink also implements exactly-once semantics.

Specifically, Dataflow does not guarantee that each record goes through each transform exactly one time. Due to retries or worker failures, Dataflow might send a record through a transform multiple times, or even simultaneously on multiple workers.

As part of exactly-once processing, Dataflow deduplicates the outputs. However, if the code in a transform has side effects, those effects might occur multiple times. For example, if a transform makes a remote service call, that call might be made multiple times for the same record. Side effects can even lead to data loss in some situations. For example, suppose that a transform reads a file to produce output, and then immediately deletes the file without waiting for the output to be committed. If an error occurs when committing the result, Dataflow retries the transform, but now the transform can't read the deleted file.

### Logging

Log output from processing indicates that the processing occurred but does not indicate whether the data was committed. Therefore, log files might indicate that data was processed multiple times even though the results of the processed data are committed to persistent storage only once. In addition, logs don't always reflect processed and committed data. Logs might be dropped due to throttling or lost due to other logging service issues.

## Exactly-once streaming

This section explains how Dataflow implements exactly-once processing for streaming jobs, including how Dataflow manages complexities like non-deterministic processing, late data, and custom code.

### Dataflow streaming shuffle

Streaming Dataflow jobs run on many different workers in parallel by assigning work ranges to each worker. Though assignments might change over time in response to worker failures, autoscaling, or other events, after each [`GroupByKey` transform](https://beam.apache.org/documentation/programming-guide/#groupbykey) , all records with the same key are processed on the same worker. The `GroupByKey` transform is often used by composite transformations, such as `Count` or `FileIO`. To ensure that records for a given key end up on the same worker, Dataflow workers shuffle data between themselves by using remote procedure calls (RPCs).

To help make sure that records aren't lost during shuffle, Dataflow uses upstream backup. With upstream backup, the worker that sends the records retries RPCs until it receives positive acknowledgment that the record has been received. The side-effects of processing the record are committed to persistent storage downstream. If the worker that sends the records becomes unavailable, Dataflow continues to retry RPCs, which ensures that every record is delivered at least once.

Because these retries might create duplicates, every message is tagged with a unique ID. Each receiver stores a catalog of all IDs that have already been seen and processed. When a record is received, Dataflow looks up its ID in the catalog. If the ID is found, the record has already been received and committed, and it's dropped as a duplicate. To ensure that the record IDs are stable, every output from step to step is checkpointed to storage. As a result, if the same message is sent multiple times due to repeated RPC calls, the message is only committed to storage once.

### Ensuring low latency

For exactly-once processing to be viable, I/O has to be reduced, in particular by preventing I/O on every record. To accomplish this goal, Dataflow uses Bloom filters and garbage collection.

#### Bloom filters

[Bloom filters](https://en.wikipedia.org/wiki/Bloom_filter) are compact data structures that allow for quick set-membership checks. In Dataflow, each worker keeps a Bloom filter of every ID it sees. When a new record ID arrives, the worker looks up the ID in the filter. If the filter returns false, then this record is not a duplicate, and the worker does not look up the ID in stable storage.

Dataflow keeps a set of rolling Bloom filters bucketed by time. When a record arrives, Dataflow picks the appropriate filter to check based on the system timestamp. This step prevents the Bloom filters from saturating as filters get garbage-collected, and also bounds the amount of data that needs to be scanned at startup.

#### Garbage collection

To avoid filling storage with record IDs, Dataflow uses garbage collection to remove old records. Dataflow uses the system timestamp to calculate a garbage-collection watermark.

This watermark is based on the amount of physical time spent waiting in a given stage. Therefore, it also provides information about what parts of the pipeline are slow. This metadata is the basis for the system lag metric shown in the [Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview).

If a record arrives with a timestamp older than the watermark, and if IDs for this time have already been garbage collected, the record is ignored. Because the low watermark that triggers garbage collection doesn't advance until record deliveries are acknowledged, these late arriving records are duplicates.

## Non-deterministic sources

Dataflow uses the Apache Beam SDK to read data into pipelines. If processing fails, Dataflow might retry reads from a source. In that situation, Dataflow needs to ensure that every unique record produced by a source is recorded exactly once. For deterministic sources, such as Pub/Sub Lite or Kafka, records are read based on a recorded offset, mitigating the need for this step.

Because Dataflow can't automatically assign record IDs, non-deterministic sources must tell Dataflow what the record IDs are in order to avoid duplication. When a source provides unique IDs for each record, the connector uses a shuffle in the pipeline to remove duplicates. Records with the same ID are filtered out. For an example of how Dataflow implements exactly-once processing when using Pub/Sub as a source, see the [Exactly-once processing](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub#exactly-once-processing) section in the Streaming with Pub/Sub page.

When you execute custom `DoFn`s as part of your pipeline, Dataflow does not guarantee that this code is run only once per record. To help guarantee at-least-once processing in case of worker failures, Dataflow might run a given record through a transform multiple times, or it might run the same record simultaneously on multiple workers. If you include code in your pipeline that does things like contact an outside service, the actions might be run more than once for a given record.

To make non-deterministic processing effectively deterministic, use [checkpointing](https://beam.apache.org/documentation/programming-guide/#user-initiated-checkpoint). When you use checkpointing, each output from a transform is checkpointed to stable storage with its unique ID before it's delivered to the next stage. Retries in the shuffle delivery of Dataflow relay the output that has been checkpointed. Though your code might run multiple times, Dataflow ensures that output from only one of those runs is stored. Dataflow uses a consistent store that prevents duplicates from being written to stable storage.

## Exactly-once output delivery

The Apache Beam SDK includes [built-in sinks](https://beam.apache.org/documentation/io/connectors/) that are designed to ensure that they don't produce duplicates. Whenever possible, use one of these built-in sinks.

If you need to [write your own sink](https://beam.apache.org/documentation/io/developing-io-overview/#sinks), the best approach is to make your function object [idempotent](https://beam.apache.org/documentation/programming-guide/#user-code-idempotence) so that it can be retried as often as necessary without causing unintended side effects. Nevertheless, often some component of the transform that implements the functionality of the sink is non-deterministic and might change if it's retried.

For example, in a windowed aggregation, the set of records in the window might be non-deterministic. Specifically, the window might attempt to fire with element e0, e1, e2. The worker might crash before committing the window processing but not before those elements are sent as a side effect. When the worker restarts, the window fires again, and a late element e3 arrives. Because this element arrives before the window is committed, it's not counted as late data, so the `DoFn` is called again with elements e0, e1, e2, e3. These elements are then sent to the side-effect operation. Idempotency does not help in this scenario, because different logical record sets are sent each time.

To address non-determinacy in Dataflow, use the built-in `Reshuffle` transform. When Dataflow shuffles data, Dataflow writes the data durably so that any non-deterministically generated elements are stable if operations are retried after the shuffle occurs. Using the `Reshuffle` transform helps guarantee that only one version of a `DoFn`'s output can make it past a shuffle boundary. The following pattern ensures that the side-effect operation always receives a deterministic record to output:
    
    
    c.apply(Window.<..>into(FixedWindows.of(Duration.standardMinutes(1))))
     .apply(GroupByKey.<..>.create())
     .apply(new PrepareOutputData())
     .apply(Reshuffle.<..>of())
     .apply(WriteToSideEffect());
    

To ensure that the Dataflow runner knows that elements must be stable before executing a `DoFn`, add the [`RequiresStableInput`](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/transforms/DoFn.RequiresStableInput.html) annotation to the `DoFn`.

## Learn more

  * [Set the pipeline streaming mode](https://docs.cloud.google.com/dataflow/docs/guides/streaming-modes)
  * [Read from Pub/Sub to Dataflow](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-with-cloud-pubsub)
  * [Streaming Engine: Execution Model for Highly Scalable, Low-Latency Data Processing](https://medium.com/google-cloud/streaming-engine-execution-model-1eb2eef69a8e)
  * Learn more about the [Apache Beam execution model](https://beam.apache.org/documentation/runtime/model/)
  * [After Lambda: Exactly-once processing in Dataflow, Part 1](https://cloud.google.com/blog/products/data-analytics/after-lambda-exactly-once-processing-in-google-cloud-dataflow-part-1)
  * [After Lambda: Exactly-once processing in Dataflow, Part 2 (Ensuring low latency)](https://cloud.google.com/blog/products/gcp/after-lambda-exactly-once-processing-in-cloud-dataflow-part-2-ensuring-low-latency)
  * [After Lambda: Exactly-once processing in Dataflow, Part 3 (sources and sinks)](https://cloud.google.com/blog/products/gcp/after-lambda-exactly-once-processing-in-cloud-dataflow-part-3-sources-and-sinks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
