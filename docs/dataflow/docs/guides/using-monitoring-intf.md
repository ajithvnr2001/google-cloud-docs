---
url: https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf/
title: Dataflow job metrics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:48.427051+00:00
---

# Dataflow job metrics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow job metrics Stay organized with collections  Save and categorize content based on your preferences. 

Dataflow collects metrics for your jobs, which can help you to debug errors, troubleshoot performance issues, or optimize your pipeline. The Dataflow monitoring interface displays visualizations for these metrics. You can also use Cloud Monitoring to create alerts or build Metrics Explorer queries.

## Access job metrics

To view the job metrics for a job, perform the following steps:

  1. In the Google Cloud console, go to the **Dataflow** > **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Select a job.

  3. Click the **Job metrics** tab.

  4. Select a metric to view.

  5. To access additional information in the job metrics charts, click query_stats **Explore data**.




Each metric is organized into the following dashboards:

  * Autoscaling metrics
  * Overview metrics
  * Streaming metrics
  * Resource metrics
  * Input/output metrics



For a complete list of Dataflow metrics, see [Google Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-dataflow).

## Support and limitations

When using the Dataflow metrics, be aware of the following details.

  * Sometimes job data is intermittently unavailable. When data is missing, gaps appear in the job monitoring charts.

  * Some of these charts are specific to streaming pipelines.

  * To write metrics data, a [user-managed service account](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#user-managed) must have the IAM API permission `monitoring.timeSeries.create`. This permission is included with the [Dataflow worker role](https://docs.cloud.google.com/dataflow/access-control#roles).

  * The Dataflow service reports the reserved CPU time after jobs complete. For unbounded (streaming) jobs, reserved CPU time is only reported after jobs are cancelled or fail. Therefore, the job metrics don't include reserved CPU time for streaming jobs.




## Autoscaling metrics

[Horizontal Autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling) enables Dataflow to choose the appropriate number of worker instances for your job, adding or removing workers as needed.

The **Autoscaling** section of the **Job metrics** tab shows the number of workers and the target number of workers over time. If your job uses Streaming Engine, it also shows the minimum and maximum number of workers.

![A data visualization showing number of workers in a pipeline.](https://docs.cloud.google.com/static/dataflow/images/autoscaling-chart.png)

To see the history of autoscaling changes, click **More history**. A table with information about the worker history of your job displays.

![Table showing history of the worker history of a pipeline.](https://docs.cloud.google.com/static/dataflow/images/autoscaling-table.png)

To see additional autoscaling information for streaming jobs, click the **Autoscaling** tab. For more information, see [Monitor Dataflow autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/autoscaling-metrics).

## Overview metrics

The following metrics appear under **Overview metrics**.

### Data freshness

_This metric applies only to streaming jobs._

Data freshness is the difference between the time when a data element is processed (processing time) and the data element's timestamp (event time). Higher values mean there was a longer delay between the event time and the processing time.

The data freshness chart shows the maximum data freshness value at any point in time. Dataflow processes multiple elements in parallel, so the graph reflects the element with the largest delay relative to its event time.

If some input data has not yet been processed, the output watermark might be delayed, which affects data freshness. A significant difference between the watermark time and the event time might indicate a [slow or stuck operation](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#processing-stuck). For more information, see [Watermarks and late data](https://beam.apache.org/documentation/programming-guide/#watermarks-and-late-data) in the Apache Beam documentation.

The dashboard includes the following two charts:

  * Data freshness by stages
  * Data freshness



In the following image, the highlighted area shows a large difference between the event time and the output watermark time, indicating a slow operation.

![A data visualization showing data freshness in a streaming pipeline.](https://docs.cloud.google.com/static/dataflow/images/data-freshness.png)

The following issues might cause high values for this metric:

  * **Performance bottlenecks** : If your pipeline has stages with high system latency or [logs indicating stuck transforms](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#processing-stuck), the pipeline might have performance issues that could raise data freshness. To investigate further, see [Troubleshoot slow or stuck streaming-jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-streaming-jobs).
  * **Data source bottlenecks** : If your data sources have growing backlogs, the event timestamps of your elements might diverge from the watermark as they wait to be processed. Large backlogs are often caused either by performance bottlenecks, or data source issues which are best detected by monitoring the sources used by your pipeline. 
    * Unordered sources such as Pub/Sub can produce stuck watermarks even while outputting at a high rate. This situation occurs because elements are not output in timestamp order, and the watermark is based on the minimum unprocessed timestamp.
  * **Frequent retries** : If you see any errors indicating elements failing to process and getting retried, that older timestamps from retried elements might be raising data freshness. The [list of common Dataflow errors](https://docs.cloud.google.com/dataflow/docs/guides/common-errors) can help you troubleshoot.



For recently updated streaming jobs, information about the job state and the watermark might be unavailable. The update operation makes several changes that take a few minutes to propagate to the Dataflow monitoring interface. Try refreshing the monitoring interface five minutes after updating your job.

### System latency

_This metric applies only to streaming jobs._

System latency is the current maximum number of seconds that an item of data has been processing or awaiting processing. The metric include how long elements wait inside a source. For example, if an output destination stops accepting write requests for a period of time, data might accumulate at the source, causing system latency to go up. If the write operations resume and the pipeline is able to catch up, system latency returns to its baseline level.

The following cases are additional considerations:

  * For multiple sources and sinks, system latency is the maximum amount of time that an element waits inside a source before it's written to all sinks.
  * Sometimes, a source does not provide a value for the time period for which an element waits inside the source. In addition, the element might not have metadata to define its event time. In this scenario, system latency is calculated from the time the pipeline first receives the element.



The dashboard includes the following two charts:

  * System latency by stages
  * System latency



![A data visualization showing system latency in a
streaming pipeline.](https://docs.cloud.google.com/static/dataflow/images/system-latency.png)

### Throughput

Throughput is the volume of data that is processed at any point in time. The dashboard includes the following charts:

  * Throughput per step in elements per second
  * Throughput per step in bytes per second



![A data visualization showing throughput of four steps in a
pipeline.](https://docs.cloud.google.com/static/dataflow/images/per-step-throughput-2.png)

### Worker error log count

The **Worker error log count** shows you the rate of errors observed across all workers at any point in time.

![A summary of each logged error and the number of times it occurred.](https://docs.cloud.google.com/static/dataflow/images/worker-error-log-count.png)

## Streaming metrics

The following metrics appear under **Streaming metrics**.

### Backlog

_This metric applies only to streaming jobs._

The **Backlog** dashboard provides information about elements waiting to be processed. The dashboard includes the following two charts:

  * Backlog seconds (Streaming Engine only)
  * Backlog bytes (with and without Streaming Engine)



The **Backlog seconds** chart shows an estimate of the amount of time in seconds needed to consume the current backlog if no new data arrives and throughput doesn't change. The estimated backlog time is calculated from both the throughput and the backlog bytes from the input source that still need to be processed. This metric is used by the [streaming autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling#streaming) feature to determine when to scale up or down.

![A data visualization showing the backlog seconds chart in a
streaming pipeline.](https://docs.cloud.google.com/static/dataflow/images/backlog-seconds.png)

The **Backlog bytes** chart shows the amount of known unprocessed input for a stage in bytes. This metric compares the remaining bytes to be consumed by each stage against upstream stages. For this metric to report accurately, each source ingested by the pipeline must be configured correctly. Built-in sources such as Pub/Sub and BigQuery are already supported out of the box, however, custom sources require some extra implementation. For more details, see [autoscaling for custom unbounded sources](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling#streaming).

![A data visualization showing the backlog bytes chart in a
streaming pipeline.](https://docs.cloud.google.com/static/dataflow/images/backlog-bytes.png)

### Processing

_This metric applies only to streaming jobs._

When you run an Apache Beam pipeline on the Dataflow service, pipeline tasks run on worker VMs. The **Processing** dashboard provides information about the amount of time tasks have been processing on the worker VMs. The dashboard includes the following two charts:

  * User processing latencies heatmap
  * User processing latencies by stage



The **User processing latencies heatmap** shows the maximum operation latencies over the 50th, 95th, and 99th percentile distributions. Use the heatmap to see whether any long-tail operations are causing high overall system latency or are negatively affecting overall data freshness.

To fix an upstream issue before it becomes a problem downstream, set an alerting policy for high latencies in the 50th percentile.

![A data visualization showing the user processing latencies heatmap chart for a
streaming pipeline.](https://docs.cloud.google.com/static/dataflow/images/user-processing.png)

The **User processing latencies by stage** chart shows the 99th percentile for all tasks that workers are processing broken down by stage. If user code is causing a bottleneck, this chart shows which stage contains the bottleneck. You can use the following steps to debug the pipeline:

  1. Use the chart to find a stage with an unusually high latency.

  2. On the job details page, in the **Execution details** tab, for **Graph view** , select **Stage workflow**. In the **Stage workflow** graph, find the stage that has unusually high latency.

  3. To find the associated user operations, in the graph, click the node for that stage.

  4. To find additional details, navigate to [Cloud Profiler](https://docs.cloud.google.com/dataflow/docs/guides/profiling-a-pipeline), and use Cloud Profiler to debug the stack trace at the correct time range. Look for the user operations that you identified in the previous step.




![A data visualization showing the user processing latencies by stage chart for a
streaming pipeline.](https://docs.cloud.google.com/static/dataflow/images/user-processing-stage.png)

### Time per active work item state

_This metric applies only to streaming jobs._

The **Time per active work item state** metric (`worker/time_per_active_work_item_state`) provides latency information about the key phases of a work item lifecycle. Unlike high-level aggregated metrics, this assessment lets you precisely attribute latency by breaking down stage-level latencies into distinct phases. For example, you can examine latency based on phases such as data retrieval (`READ`), user-code execution (`ACTIVE`), and state persistence (`COMMIT`).

#### Runner version support

While the metric is fully supported on the Streaming Java Runner, it's partially supported on the Portable Runner.

This table summarizes the latency states and their support by runner.

Latency state | Streaming Java Runner support | Portable Runner support  
---|---|---  
`GET_WORK` | Supported | Not supported  
`QUEUED` | Supported | Supported  
`ACTIVE` | Supported | Supported  
`READ` | Supported | Supported  
`COMMIT` | Supported | Supported  
  
#### Latency state definitions and troubleshooting

The following sections define each latency state and include troubleshooting information.

`GET_WORK`

  * This is the time a user worker takes to request work items, and for the Dataflow backend to assign and deliver them.
  * For typical ETL stages, a stable 0-1s time indicates a healthy connection. Actual values vary, depending on your workload complexity and data volume.



`QUEUED`

  * This is the time a work item spends in the worker's local buffer before a thread is available for processing.
  * If `QUEUED` latencies exceed 1s, work is arriving faster than threads can process it. For typical ETL stages, latencies under 1s are considered healthy. Actual values vary, depending on your workload complexity and data volume.



`ACTIVE`

  * This is the time spent executing `DoFn` code.
  * The `ACTIVE` latency refers to the time spent processing a bundle of elements, not a single element.
  * Sudden increases in this latency value might indicate throttling by external RPC calls or computationally expensive edge cases. Use [`DoFn` metrics](https://docs.cloud.google.com/dataflow/docs/guides/using-monitoring-intf#dofn-metrics) to identify the specific `DoFns` causing the delay.



`READ`

  * This is the time spent fetching data, including explicit state reads and implicit reads during a `GroupByKey` operation.
  * High `READ` time is often caused by large reads on a single key. Investigate state access patterns or use [state and timers](https://beam.apache.org/documentation/programming-guide/#state-and-timers) to avoid blocking threads.



`COMMIT`

  * This is the time taken to send results (state updates and output elements) to the Dataflow backend and receive an acknowledgement.
  * High `COMMIT` time is often caused by writing large payloads or updating large state objects. [Check for hot keys](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-streaming-jobs#hot-keys) using the bottleneck status.



### Parallelism

_This metric applies only to Streaming Engine jobs._

The **Parallel processing** chart shows the approximate number of keys in use for data processing for each stage. Dataflow scales based on the parallelism of a pipeline.

When Dataflow runs a pipeline, the processing is distributed across multiple Compute Engine virtual machines (VMs), also known as workers. The Dataflow service automatically parallelizes and distributes the processing logic in your pipeline to the workers. Processing for any given key is serialized, so the total number of keys for a stage represents the maximum available parallelism at that stage.

Parallelism metrics can be useful for finding hot keys or bottlenecks for slow or stuck pipelines.

![A data visualization showing the parallel processing chart in a
streaming pipeline.](https://docs.cloud.google.com/static/dataflow/images/parallel-processing.png)

### Persistence

_This metric applies only to streaming jobs._

The **Persistence** dashboard provides information about the rate at which persistent storage is written and read by a particular pipeline stage in bytes per second. Bytes read and written include user state operations and state for persistent shuffles, duplicate removal, side-inputs, and watermark tracking. Pipeline coders and caching affect bytes read and written. Storage bytes might differ from processed bytes due to internal storage usage and caching.

The dashboard includes the following two charts:

  * Storage write
  * Storage read



![A data visualization showing the storage write chart for a
streaming pipeline.](https://docs.cloud.google.com/static/dataflow/images/storage-write.png)

### Duplicates

_This metric applies only to streaming jobs._

The **Duplicates** chart shows the number of messages being processed by a particular stage that have been filtered out as duplicates. Dataflow supports many sources and sinks which guarantee `at least once` delivery. The downside of `at least once` delivery is that it can result in duplicates. Dataflow uses `exactly once` delivery, which means that duplicates are automatically filtered out. Downstream stages are saved from reprocessing the same elements, which ensures that state and outputs are not affected. The pipeline can be optimized for resources and performance by reducing the number of duplicates produced in each stage.

![A data visualization showing the duplicates chart in a
streaming pipeline.](https://docs.cloud.google.com/static/dataflow/images/duplicates.png)

### Timers

_This metric applies only to streaming jobs._

The **Timers** dashboard provides information about the number of timers pending and the number of timers already processed in a particular pipeline stage. Because windows rely on timers, this metric lets you track the progress of windows.

The dashboard includes the following two charts:

  * Timers pending by stage
  * Timers processing by stage



These charts show the rate at which windows are pending or processing at a specific point in time. The **Timers pending by stage** chart indicates how many windows are delayed due to bottlenecks. The **Timers processing by stage** chart indicates how many windows are collecting elements.

These charts display all job timers, so if timers are used elsewhere in your code, those timers also appear in these charts.

![A data visualization showing the number of timers pending in a particular stage.](https://docs.cloud.google.com/static/dataflow/images/timers-pending.png)

![A data visualization showing the number of timers already processed in a particular stage.](https://docs.cloud.google.com/static/dataflow/images/timers-processed.png)

## Resource metrics

The following metrics appear under **Resource metrics**.

### CPU utilization

CPU utilization is the amount of CPU used divided by the amount of CPU available for processing. This per-worker metric is displayed as a percentage. The dashboard includes the following four charts:

  * CPU utilization (All workers)
  * CPU utilization (Stats)
  * CPU utilization (Top 4)
  * CPU utilization (Bottom 4)



![An animated data visualization showing CPU utilization for one Dataflow
worker.](https://docs.cloud.google.com/static/dataflow/images/cpu-utilization.gif)

### Memory utilization

Memory utilization is the estimated amount of memory used by the workers in bytes per second. The dashboard includes the following two charts:

  * Max worker memory utilization (estimated bytes per second)
  * Memory utilization (estimated bytes per second)



The **Max worker memory utilization** chart provides information about the workers that use the most memory in the Dataflow job at each point in time. If, at different points during a job, the worker using the maximum amount of memory changes, the same line in the chart displays data for multiple workers. Each data point in the line displays data for the worker using the maximum amount of memory at that time. The chart compares the estimated memory used by the worker to the memory limit in bytes.

You can use this chart to troubleshoot out-of-memory (OOM) issues. Worker out-of-memory crashes are not shown on this chart.

The **Memory utilization** chart shows an estimate of the memory used by all workers in the Dataflow job compared to the memory limit in bytes.

## Input and output metrics

If your streaming Dataflow job reads or writes records using Pub/Sub, the **Job metrics** tab shows metrics for Pub/Sub reads or writes.

All input metrics of the same type are combined, and all output metrics are also combined. For example, all Pub/Sub metrics are grouped in one section. Each metric type is organized into a separate section. To change which metrics are displayed, select the section on the left which best represents the metrics you're looking for. The following images show all the available sections.

![An example image which shows the separate input and output sections for a Dataflow job.](https://docs.cloud.google.com/static/dataflow/images/job-metrics-io-section.png)

The following two charts are displayed in both the **Input Metrics** and **Output Metrics** sections.

![A series of charts showing input and output metrics for a Dataflow job.](https://docs.cloud.google.com/static/dataflow/images/job-metrics-io-expanded.png)

### Requests per second

Requests per sec is the rate of API requests to read or write data by the source or sink over time. If this rate drops to zero, or decreases significantly for an extended time period relative to expected behavior, then the pipeline might be blocked from performing certain operations. Also, there might be no data to read. In such a case, review the job steps that have a high system watermark. Also, examine the worker logs for errors or indications about slow processing.

![A chart showing the number of API requests to read or write data by the source or sink over time.](https://docs.cloud.google.com/static/dataflow/images/job-metrics-io-requests-per-second.png)

### Response errors per second by error type

Response errors per sec by error type is the rate of failed API requests to read or write data by the source or sink over time. If such errors occur frequently, these API requests might slow down processing. Such failed API requests must be investigated. To help troubleshoot these issues, review the general [Input and output error codes](https://docs.cloud.google.com/dataflow/docs/guides/input-and-output-error-codes). Also review any specific error code documentation used by the source or sink, such as the [Pub/Sub error codes](https://docs.cloud.google.com/pubsub/docs/reference/error-codes).

![A chart showing the rate of failed API requests to read or write data by the source or sink over time.](https://docs.cloud.google.com/static/dataflow/images/job-metrics-io-response-errors-per-sec-by-type.png)

**Note:** The chart is empty until the first error occurs.

For more information about scenarios where you can use these metrics for debugging, see [Tools for debugging](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-streaming-jobs#debug-tools) in "Troubleshoot slow or stuck jobs."

## Use Cloud Monitoring

Dataflow is fully integrated with Cloud Monitoring. Use Cloud Monitoring for the following tasks:

  * Create alerts when your job exceeds a user-defined threshold.
  * Use Metrics Explorer to build queries and adjust the timespan of the metrics.
  * View metrics that don't appear in the Dataflow monitoring interface.



For instructions about creating alerts and using Metrics Explorer, see [Use Cloud Monitoring for Dataflow pipelines](https://docs.cloud.google.com/dataflow/docs/guides/using-cloud-monitoring).

For the complete list of Dataflow metrics, see the [Google Cloud metrics documentation](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-dataflow).

### Create Cloud Monitoring alerts

Cloud Monitoring lets you create alerts when your Dataflow job exceeds a user-defined threshold. To create a Cloud Monitoring alert from a metric chart, click **Create alerting policy**.

If you're unable to see the monitoring graphs or create alerts, you might need additional [Monitoring permissions](https://docs.cloud.google.com/monitoring/access-control).

### View in Metrics Explorer

You can view the Dataflow metrics charts in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), where you can build queries and adjust the timespan of the metrics.

To view the Dataflow charts in Metrics Explorer, in the **Job metrics** view, open more_vert**More chart options** and click **View in Metrics Explorer**.

When you adjust the timespan of the metrics, you can select a predefined duration or select a custom time interval to analyze your job.

By default, for streaming jobs and in-flight batch jobs, the display shows the previous six hours of metrics for that job. For stopped or completed streaming jobs, the default display shows the entire runtime of the job duration.

### Dataflow I/O metrics

You can view the following Dataflow I/O metrics in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer):

  * [`job/pubsub/write_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/pubsub/write_count): Pub/Sub publish requests from [PubsubIO.Write](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/pubsub/PubsubIO.Write.html) in Dataflow jobs.
  * [`job/pubsub/read_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/pubsub/read_count): Pub/Sub pull requests from [PubsubIO.Read](https://beam.apache.org/releases/javadoc/current/org/apache/beam/sdk/io/gcp/pubsub/PubsubIO.Read.html) in Dataflow jobs.
  * [`job/bigquery/write_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/bigquery/write_count): BigQuery publish requests from [BigQueryIO.Write](https://beam.apache.org/releases/javadoc/2.27.0/org/apache/beam/sdk/io/gcp/bigquery/BigQueryIO.Write.html) in Dataflow jobs. `job/bigquery/write_count` metrics are available in Python pipelines using the [WriteToBigQuery transform](https://github.com/apache/beam/blob/master/sdks/python/apache_beam/io/gcp/bigquery.py) with `method='STREAMING_INSERTS'` enabled on Apache Beam v2.28.0 or later. This metric is available for both batch and streaming pipelines.
  * If your pipeline uses a BigQuery source or sink, to troubleshoot quota issues, use the [BigQuery Storage API metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-bigquerystorage).



### DoFn metrics

For streaming jobs that use [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine) and don't use the [Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner), you can view the following metrics for individual user-defined `DoFns`:

  * [`job/dofn_latency_average`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/dofn_latency_average): The average message processing time for a single `DoFn` over the past 3-minute window, in milliseconds.
  * [`job/dofn_latency_max`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/dofn_latency_max): The maximum message processing time for a single `DoFn` over the past 3-minute window, in milliseconds.
  * [`job/dofn_latency_min`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/dofn_latency_min): The minimum message processing time for a single `DoFn` over the past 3-minute window, in milliseconds.
  * [`job/dofn_latency_num_messages`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/dofn_latency_num_messages): The number of messages processed by a single `DoFn` over the past 3-minute.
  * [`job/dofn_latency_total`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/dofn_latency_total): The total message processing time for all messages in a single `DoFn` over the past 3-minute window, in milliseconds.
  * [`job/oldest_active_message_age`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#dataflow/job/oldest_active_message_age): How long the oldest active message has been processing within a `DoFn`, in milliseconds.



These metrics require Apache Beam SDK version 2.53.0 or later. To view these metrics, use [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).

You can use these metrics to find which `DoFns` contribute the most to processing latency in your jobs. For example, if a job is stuck, use the `job/oldest_active_message_age` metric to find the `DoFn` with the oldest active message. The following image shows a `DoFn` with a large spike in this metric:

![A chart showing a DoFn with an outlier for the oldest active message.](https://docs.cloud.google.com/static/dataflow/images/oldest-active-message-age.png)

To view the name of the `DoFn`, hold the pointer over the graph line.

## What's next

  * [Troubleshoot slow or stuck streaming jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-streaming-jobs).
  * [Troubleshoot slow or stuck batch jobs](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-slow-batch-jobs).
  * [Tune Horizontal Autoscaling for streaming pipelines](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling)
  * [Optimize costs](https://docs.cloud.google.com/dataflow/docs/optimize-costs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
