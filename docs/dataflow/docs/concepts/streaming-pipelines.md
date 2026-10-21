---
url: https://docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines/
title: Streaming pipelines \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:54.802875+00:00
---

# Streaming pipelines  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Streaming pipelines Stay organized with collections  Save and categorize content based on your preferences. 

Unbounded [PCollections](https://docs.cloud.google.com/dataflow/docs/concepts/beam-programming-model#basic-concepts), or unbounded _collections_ , represent data in streaming pipelines. An unbounded collection contains data from a continuously updating data source such as [Pub/Sub](https://docs.cloud.google.com/pubsub/docs).

You cannot use only a key to group elements in an unbounded collection. There might be infinitely many elements for a given key in streaming data because the data source constantly adds new elements. You can use windows, watermarks, and triggers to aggregate elements in unbounded collections.

The concept of windows also applies to bounded PCollections that represent data in batch pipelines. For information on windowing in batch pipelines, see the Apache Beam documentation for [Windowing with bounded PCollections](https://beam.apache.org/documentation/programming-guide/#windowing-bounded-collections).

If a Dataflow pipeline has a bounded data source, that is, a source that does not contain continuously updating data, and the pipeline is switched to streaming mode using the `--streaming` flag, when the bounded source is fully consumed, the pipeline stops running.

## Use streaming mode

To run a pipeline in streaming mode, set the `--streaming` flag in the [command line](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#set_pipeline_options_on_the_command_line) when you run your pipeline. You can also set the streaming mode [programmatically](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options#set_pipeline_options_programmatically) when you construct your pipeline.

Batch sources are not supported in streaming mode.

When you update your pipeline with a larger pool of workers, your streaming job might not upscale as expected. For streaming jobs that don't use [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine), you cannot scale beyond the original number of workers and Persistent Disk resources allocated at the start of your original job. When you [update](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline) a Dataflow job and specify a larger number of workers in the new job, you can only specify a number of workers equal to the maximum number of workers that you specified for your original job.

Specify the maximum number of workers by using the following flags:

### Java

`--maxNumWorkers`

### Python

`--max_num_workers`

### Go

`--max_num_workers`

## Windows and windowing functions

_Windowing functions_ divide unbounded collections into logical components, or _windows_. Windowing functions group unbounded collections by the timestamps of the individual elements. Each window contains a finite number of elements.

You set the following windows with the [Apache Beam SDK](https://beam.apache.org/documentation/programming-guide/#windowing):

  * Tumbling windows (called [fixed windows](https://beam.apache.org/documentation/programming-guide/#fixed-time-windows) in Apache Beam)
  * Hopping windows (called [sliding windows](https://beam.apache.org/documentation/programming-guide/#sliding-time-windows) in Apache Beam)
  * Session windows



### Tumbling windows

A tumbling window represents a consistent, disjoint time interval in the data stream.

For example, if you set a thirty-second tumbling window, the elements with timestamp values [0:00:00-0:00:30) are in the first window. Elements with timestamp values [0:00:30-0:01:00) are in the second window.

The following image illustrates how elements are divided into thirty-second tumbling windows.

![An image that shows tumbling windows, 30 seconds in duration](https://docs.cloud.google.com/static/dataflow/images/fixed-time-windows.png)

### Hopping windows

A hopping window represents a consistent time interval in the data stream. Hopping windows can overlap, whereas tumbling windows are disjoint.

For example, a hopping window can start every thirty seconds and capture one minute of data. The frequency with which hopping windows begin is called the _period_. This example has a one-minute window and thirty-second period.

The following image illustrates how elements are divided into one-minute hopping windows with a thirty-second period.

![An image that shows hopping windows with 1 minute window duration and 30 second window period](https://docs.cloud.google.com/static/dataflow/images/sliding-time-windows.png)

To take running averages of data, use hopping windows. You can use one-minute hopping windows with a thirty-second period to compute a one-minute running average every thirty seconds.

### Session windows

A session window contains elements within a _gap duration_ of another element. The gap duration is an interval between new data in a data stream. If data arrives after the gap duration, the data is assigned to a new window.

For example, session windows can divide a data stream representing user mouse activity. This data stream might have long periods of idle time interspersed with many clicks. A session window can contain the data generated by the clicks.

Session windowing assigns different windows to each data key. Tumbling and hopping windows contain all elements in the specified time interval, regardless of data keys.

The following image visualizes how elements are divided into session windows.

![An image that shows session windows with a minimum gap duration](https://docs.cloud.google.com/static/dataflow/images/session-windows.png)

## Watermarks

A _watermark_ is a threshold that indicates when Dataflow expects all of the data in a window to have arrived. If the watermark has progressed past the end of the window and new data arrives with a timestamp within the window, the data is considered _late data_. For more information, see [Watermarks and late data](https://beam.apache.org/documentation/programming-guide/#watermarks-and-late-data) in the Apache Beam documentation.

Dataflow tracks watermarks for the following reasons:

  * Data is not guaranteed to arrive in time order or at predictable intervals.
  * Data events are not guaranteed to appear in pipelines in the same order that they were generated.



The data source determines the watermark. You can [allow late data](https://beam.apache.org/documentation/programming-guide/#managing-late-data) with the Apache Beam SDK.

## Triggers

_Triggers_ determine when to emit aggregated results as data arrives. By default, results are emitted when the watermark passes the end of the window.

You can use the Apache Beam SDK to create or modify triggers for each collection in a streaming pipeline.

The Apache Beam SDK can [set triggers](https://beam.apache.org/documentation/programming-guide/#triggers) that operate on any combination of the following conditions:

  * Event time, as indicated by the timestamp on each data element.
  * Processing time, which is the time that the data element is processed at any given stage in the pipeline.
  * The number of data elements in a collection.



## What's next

  * [Streaming 101: The world beyond batch](https://www.oreilly.com/ideas/the-world-beyond-batch-streaming-101) (blog)
  * [Streaming 102: The world beyond batch](https://www.oreilly.com/ideas/the-world-beyond-batch-streaming-102) (blog)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
