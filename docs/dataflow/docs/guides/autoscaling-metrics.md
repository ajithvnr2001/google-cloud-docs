---
url: https://docs.cloud.google.com/dataflow/docs/guides/autoscaling-metrics/
title: Monitor Dataflow autoscaling \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:48.623898+00:00
---

# Monitor Dataflow autoscaling  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/autoscaling-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Monitor Dataflow autoscaling Stay organized with collections  Save and categorize content based on your preferences. 

You can view autoscaling monitoring charts for streaming jobs within the Dataflow monitoring interface. These charts display metrics over the duration of a pipeline job and include the following information:

  * The number of worker instances used by your job at any point in time
  * The autoscaling log files
  * The estimated backlog over time
  * The average CPU utilization over time



The charts are aligned vertically so that you can correlate the backlog and CPU utilization metrics with worker scaling events.

For more information about how Dataflow makes autoscaling decisions, see the [Autotuning features](https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline#autotuning-features) documentation. For more information about Dataflow monitoring and metrics, see [Use the Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/docs/guides/monitoring-overview).

## Access autoscaling monitoring charts

You can access the Dataflow monitoring interface by using the [Google Cloud console](https://console.cloud.google.com/). To access the **Autoscaling** metrics tab, follow these steps:

  1. [Sign in](https://console.cloud.google.com/) to the Google Cloud console.
  2. Select your Google Cloud project.
  3. Open the navigation menu.
  4. In **Analytics** , click **Dataflow**. A list of Dataflow jobs appears along with their status.
  5. Click the job that you want to monitor, and then click the **Autoscaling** tab.



## Monitor autoscaling metrics

The Dataflow service automatically chooses the number of worker instances required to run your autoscaling job. The number of worker instances can change over time according to the job requirements.

You can view autoscaling metrics in the **Autoscaling** tab of the Dataflow interface. Each metric is organized into the following charts:

  * Autoscaling
  * Backlog (Streaming Engine only)
  * CPU utilization



The autoscaling action bar displays the current autoscaling status and workers count.

### Autoscaling

The **Autoscaling** chart shows a time-series graph of the current number of workers, the target number of workers, and the [minimum and maximum number of workers](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling#set-range).

![A data visualization showing the number of workers in a pipeline.](https://docs.cloud.google.com/static/dataflow/images/autoscaling-chart2.png)

To see the autoscaling logs, click **Show autoscaling logs**.

To see the history of autoscaling changes, click **More history**. A table with information about the worker history of your pipeline is shown. The history includes autoscaling events, including whether the number of workers reached the minimum or maximum worker count.

![Table showing the worker history of a pipeline.](https://docs.cloud.google.com/static/dataflow/images/autoscaling-table.png)

### Autoscaling rationale (Streaming Engine only)

The **Autoscaling rationale** chart shows why the autoscaler scaled up, scaled down, or took no actions during a given time period.

![A data visualization showing the autoscaling rationale.](https://docs.cloud.google.com/static/dataflow/images/autoscaling-rationale.png)

To see a description of the rationale at a specific point, hold the pointer over the chart.

![A data visualization showing a descriptions of the autoscaling rationale.](https://docs.cloud.google.com/static/dataflow/images/autoscaling-rationale-hover.png)

The following table lists scaling actions and possible scaling rationales.

Scaling action | Rationale | Description  
---|---|---  
No change in scaling | Gathering more data for decision | The autoscaler does not have enough signals to scale up or down. For example, the worker pool status changed recently; or backlog or utilization metrics are fluctuating.  
No change in scaling, stable signals | Hit non-resource related limit | Scaling is constrained by a limit such as key parallelism or the configured minimum and maximum workers.  
Low backlog and high worker utilization | The pipeline's autoscaling has converged to a stable value given the current traffic and configuration. No scaling change is needed.  
Scale up | High backlog | Scaling up to reduce backlog.  
High worker utilization | Scaling up to achieve target CPU utilization.  
Hit a non-resource-related limit | The minimum number of workers was updated, and the current number of workers is below the configured minimum.  
Scale down | Low worker utilization | Scaling down to achieve target CPU utilization.  
Hit a non-resource-related limit | The maximum number of workers was updated, and the current number of workers is above the configured maximum.  
  
### Worker CPU utilization

CPU utilization is the amount of CPU used divided by the amount of CPU available for processing. The **Mean CPU utilization** chart shows the average CPU utilization for all workers over time, the [worker utilization hint](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling#utilization-hint), and whether Dataflow actively used the hint as a target.

![A data visualization showing the average CPU utilization for all Dataflow
workers.](https://docs.cloud.google.com/static/dataflow/images/mean-cpu.png)

### Backlog (Streaming Engine only)

The **Maximum backlog** chart provides information about elements waiting to be processed. The chart shows an estimate of the amount of time in seconds needed to consume the current backlog if no new data arrives and throughput doesn't change. The estimated backlog time is calculated from both the throughput and the backlog bytes from the input source that still need to be processed. This metric is used by the [streaming autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling#streaming_autoscaling) feature to determine when to scale up or down.

Data for this chart is only available for jobs that use Streaming Engine. If your streaming job doesn't use Streaming Engine, the chart is empty.

![A data visualization showing the maximum backlog chart in a
streaming pipeline.](https://docs.cloud.google.com/static/dataflow/images/max-backlog.png)

## Recommendations

Here are some behaviors that you might observe in your pipeline, and recommendations on how to [tune autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling):

  * **Excessive downscaling**. If the target CPU utilization is set too high, you might see a pattern where Dataflow scales down, the backlog starts to grow, and Dataflow scales up again to compensate, instead of converging on a stable number of workers. To mitigate this issue, try setting a lower worker utilization hint. Observe the CPU utilization at the point where the backlog starts to grow, and set the utilization hint to that value.

  * **Too slow upscaling**. If upscaling is too slow, it might lag behind spikes in traffic, resulting in periods of increased latency. Try reducing the worker utilization hint, so that Dataflow scales up more quickly. Observe the CPU utilization at the point where the backlog starts to grow, and set the utilization hint to that value. Monitor both latency and cost, because a lower hint value can increase the total cost for the pipeline, if more workers are provisioned.

  * **Excessive upscaling**. If you observe excessive upscaling, resulting in increased cost, consider increasing the worker utilization hint. Monitor latency to make sure it stays within acceptable bounds for your scenario.




For more information, see [Set the worker utilization hint](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling#utilization-hint). When you experiment with a new worker utilization hint value, wait a few minutes for the pipeline to stabilize after each adjustment.

## What's next

  * [Tune Horizontal Autoscaling for streaming pipelines](https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling)
  * [Troubleshoot Dataflow autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-autoscaling)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
