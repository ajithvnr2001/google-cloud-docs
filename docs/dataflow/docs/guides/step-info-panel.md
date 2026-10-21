---
url: https://docs.cloud.google.com/dataflow/docs/guides/step-info-panel/
title: Dataflow job step information \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:48.324478+00:00
---

# Dataflow job step information  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/step-info-panel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow job step information Stay organized with collections  Save and categorize content based on your preferences. 

In the Dataflow monitoring interface, the **Step info** panel shows information about individual steps in a job. A _step_ represents a single transform in your pipeline. [Composite transforms](https://beam.apache.org/documentation/programming-guide/#composite-transforms) contain sub-steps.

The **Step info** panel displays the following information:

  * Metrics for the step.
  * Information about the step's input and output collections.
  * Which stages correspond to this step.
  * Side input metrics



Use the **Step info** panel to understand how your job performs at each step, and to find steps that can potentially be optimized.

## View step information

To view step information, perform the following steps:

  1. In the Google Cloud console, go to the **Dataflow** > **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Select a job.

  3. Click the **Job graph** tab to view the [job graph](https://docs.cloud.google.com/dataflow/docs/guides/job-graph). The job graph represents each step in the pipeline as a box.

  4. Click a step. Information about the step appears in the **Step info** panel.

  5. To view substeps for a composite transform, click the expand_more **Expand node** arrow.




## Step metrics

The **Step info** panel shows the following metrics for the step.

### System watermark and lag

The system watermark is the latest timestamp for which all event times have been fully processed. The system watermark lag is the maximum time that an item of data has been awaiting processing.

### Data watermark and lag

The data watermark is the timestamp that marks the estimated completion time of data input for this step. The data watermark lag is the difference between the latest input event time and the data watermark.

### Wall time

Wall time is the total approximate time spent across all threads in all workers on the following actions:

  * Initializing the step
  * Processing data
  * Shuffling data
  * Ending the step



For composite steps, wall time equals the sum of time spent in the component steps.

Wall time can help you identify slow steps and diagnose which part of your pipeline is taking more time than required.

### Bottleneck status

If Dataflow detects a bottleneck, an alert is shown, along with the cause, if known. For more information, see [Troubleshoot bottlenecks](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-bottlenecks).

### Maximum operation latency

Maximum operation latency is the maximum time being spent in this step to process incoming messages or window expirations. This metric is measured in aggregate across steps fused into a single stage, so the value represents the entire stage.

### Key parallelism

Key parallelism is the approximate number of keys in use for data processing at this step.

### Windowing information

For aggregation steps in streaming pipelines, the **Step info** panel displays windowing information derived from the windowing strategy of the pipeline's `ParDo` transform. For example:

  * **Windowing Function:** `org.apache.beam.sdk.transforms.windowing.SlidingWindows`
  * **Window Period:** `30 sec`
  * **Window Size:** `5 min`
  * **Window Start Offset:** `0 ms`
  * **Windowing Accumulation Mode:** `DISCARDING`
  * **Windowing Write Amplification Factor:** `10`



The following windowing fields provide important context for streaming performance and data volume:

  * **Windowing Accumulation Mode:** Indicates whether window state is retained across trigger firings. For more information, see [Window accumulation modes](https://beam.apache.org/documentation/programming-guide/#window-accumulation-modes) in the Apache Beam documentation.
  * **Windowing Write Amplification Factor:** The average number of windows to which each incoming element is assigned, calculated as `Window Size / Window Period`. For example, a window size of 5 minutes (`300 sec`) with a slide period of 30 seconds (`30 sec`) assigns each element to 10 overlapping windows (`300 / 30 = 10`), resulting in a write amplification factor of `10`. An amplification factor greater than `1` multiplies downstream element volume, shuffle traffic, and state storage.



## Input/output collections

The **Step info** panel shows the following information about each of the input and output collections in the step:

  * Throughput chart. This chart shows the throughput for the collection. You can view the chart as elements per second, or as bytes per second. For more information about this metric, see [Throughput](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf#throughput).

  * Count of elements added to the collection.

  * Estimated size of the collection, in bytes.




## Optimized stages

A _stage_ represents a single unit of work that is performed by Dataflow. When you select a step in the job graph, the **Step info** panel shows the names of the stages that perform this step, along with the current status, such as running, stopped, or succeeded.

To view more information about the stages in your job, use the [**Execution details** tab](https://docs.cloud.google.com/dataflow/docs/concepts/execution-details).

## Side input metrics

A [side input](https://beam.apache.org/documentation/programming-guide/#side-inputs) is an additional input that a transform can access each time it processes an element. If a transform creates or consumes a side input, the **Side Info** panel shows metrics for the side input collection.

If a [composite transform](https://docs.cloud.google.com/dataflow/docs/guides/job-graph#composite-transforms) creates or consumes a side input, expand the composite transform until you see the specific subtransform that creates or consumes the side input. Select that subtransform to view the side input metrics.

### Transforms that create a side input

If a transform creates a side input collection, the **Side Input Metrics** section displays the name of the collection, along with the following metrics:

  * **Time spent writing:** The time spent writing the side input collection.
  * **Bytes written:** The total number of bytes written to the side input collection.
  * **Time & bytes read from side input:** A table that contains additional metrics for all transforms that consume the side input collection, called _side input consumers_.



The **Time & bytes read from side input** table contains the following information for each side input consumer:

  * **Side input consumer:** The transform name of the side input consumer.
  * **Time spent reading:** The time this consumer spent reading the side input collection.
  * **Bytes read:** The number of bytes this consumer read from the side input collection.



The following image shows side input metrics for a transform that creates a side input collection:

![Side input metrics shown in the Step info panel](https://docs.cloud.google.com/static/dataflow/images/monitoring-side-input-write.png)

The job graph has an expanded composite transform (`MakeMapView`). The subtransform that creates the side input (`CreateDataflowView`) is selected, and the side input metrics are visible in the **Step info** panel.

### Transforms that consume side inputs

If a transform consumes one or more side inputs, the **Side Input Metrics** section displays the **Time & bytes read from side input** table. This table contains the following information for each side input collection:

  * **Side input collection:** The name of the side input collection.
  * **Time spent reading:** The time the transform spent reading this side input collection.
  * **Bytes read:** The number of bytes the transform read from this side input collection.



The following image shows side input metrics for a transform that reads from a side input collection.

![Side input metrics shown in the Step info panel](https://docs.cloud.google.com/static/dataflow/images/monitoring-side-input-read.png)

The `JoinBothCollections` transform reads from a side input collection. `JoinBothCollections` is selected in the job graph, and the side input metrics are visible in the **Step info** panel.

### Identify side input performance issues

Side inputs can affect your pipeline's performance. When your pipeline uses a side input, Dataflow writes the collection to a persistent layer, such as a disk, and your transforms read from this persistent collection. These reads and writes affect your job's run time.

_Reiteration_ is a common side input performance issue. If your side input `PCollection` is too large, workers can't cache the entire collection in memory. As a result, the workers must repeatedly read from the persistent side input collection.

In the following image, the side input metrics show that the total bytes read from the side input collection are much larger than the collection's size, which is shown as total bytes written. The side input collection is 563 MB, and the sum of the bytes read by consuming transforms is almost 12 GB.

![An example of reiteration](https://docs.cloud.google.com/static/dataflow/images/monitoring-side-input-reiteration.png)

To improve the performance of this pipeline, redesign your algorithm to avoid iterating or refetching the side input data. In this example, the pipeline creates the Cartesian product of two collections. The algorithm iterates through the entire side input collection for each element of the main collection. You can improve the access pattern of the pipeline by batching multiple elements of the main collection together. This change reduces the number of times workers must re-read the side input collection.

Another common performance issue can occur if your pipeline performs a join by applying a `ParDo` with one or more large side inputs. In this case, workers spend a large percentage of the processing time for the join operation reading from the side input collections.

The following image shows side input metrics for this issue:

![An example of an expensive side-input join](https://docs.cloud.google.com/static/dataflow/images/monitoring-side-input-read.png)

The `JoinBothCollections` transform has a total processing time of more than 18 minutes. Workers spend the majority of the processing time (10 minutes) reading from the 10 GB side input collection. To improve the performance of this pipeline, use [`CoGroupByKey`](https://beam.apache.org/documentation/programming-guide/#cogroupbykey) instead of side inputs.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
