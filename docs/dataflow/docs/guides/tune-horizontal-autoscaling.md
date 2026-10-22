---
url: https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling/
title: Tune Horizontal Autoscaling for streaming pipelines \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:23:15.802489+00:00
---

# Tune Horizontal Autoscaling for streaming pipelines  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/tune-horizontal-autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Tune Horizontal Autoscaling for streaming pipelines Stay organized with collections  Save and categorize content based on your preferences. 

In streaming pipelines with a high volume of input data, there is generally a tradeoff between cost and latency. To maintain low latency, Dataflow must add workers as the volume of traffic increases. Another factor is how quickly the pipeline should scale up or down in response to changes in the input data rate.

The Dataflow autoscaler has default settings that are suitable for many workloads. However, you might want to tune this behavior for your particular scenario. For example, a higher average latency might be acceptable in order to reduce costs, or you might want Dataflow to scale up more quickly in response to spikes in traffic.

To optimize Horizontal Autoscaling, you can adjust the following parameters:

  * Autoscaling range: The minimum and maximum number of workers to allocate.
  * Worker utilization hint: The target CPU utilization for workers.
  * Worker parallelism hint: The target number of parallelism for workers.
  * Latency tier: The backlog threshold tier to configure the autoscaler's sensitivity to backlog duration.



## Set the autoscaling range

When you create a new streaming job, you can set the initial number of workers and the maximum number of workers. To do so, specify the following [pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options):

### Java

  * `--numWorkers`: the initial number of workers available when the pipeline starts running
  * `--maxNumWorkers`: the maximum number of workers available to your pipeline



### Python

  * `--num_workers`: the initial number of workers available when the pipeline starts running
  * `--max_num_workers`: the maximum number of workers available to your pipeline



### Go

  * `--num_workers`: the initial number of workers available when the pipeline starts running
  * `--max_num_workers`: the maximum number of workers available to your pipeline



For streaming jobs that use Streaming Engine, the `--maxNumWorkers` flag is optional. The default is `100`. For streaming jobs not using Streaming Engine, `--maxNumWorkers` is required when Horizontal Autoscaling is enabled.

The starting value of `--maxNumWorkers` also determines how many [Persistent Disks](https://docs.cloud.google.com/compute/docs/disks#pdspecs) are allocated for the job. Pipelines are deployed with a fixed pool of Persistent Disks, equal in number to `--maxNumWorkers`. During streaming, Persistent Disks are redistributed such that each worker gets an equal number of attached disks.

If you set `--maxNumWorkers`, ensure the value provides enough disks for your pipeline. Consider future growth when setting the initial value. For information about Persistent Disk performance, see [Configure your Persistent Disk and VMs](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance). Dataflow [bills for Persistent Disk usage](https://cloud.google.com/dataflow/pricing) and has [Compute Engine quotas](https://docs.cloud.google.com/dataflow/quotas), including Persistent Disk quotas.

By default, the minimum number of workers is 1 for streaming jobs that use Streaming Engine, and (`maxNumWorkers`/15), rounded up, for jobs that don't use Streaming Engine.

### Update the autoscaling range

For jobs that use Streaming Engine, you can adjust the minimum and maximum number workers, without stopping or replacing the job. To adjust these values, use an [in-flight job update](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline#in-flight-updates). Update the following job options:

  * `--min-num-workers`: the minimum number of workers.
  * `--max-num-workers`: the maximum number of workers.




###  gcloud 

Use the `gcloud dataflow jobs update-options` command:
    
    
    gcloud dataflow jobs update-options \
      --region=REGION \
      --min-num-workers=MINIMUM_WORKERS \
      --max-num-workers=MAXIMUM_WORKERS \
      JOB_ID

Replace the following:

  * REGION: the region ID of the job's regional endpoint
  * MINIMUM_WORKERS: the minimum number of Compute Engine instances
  * MAXIMUM_WORKERS: the maximum number of Compute Engine instances
  * JOB_ID: the ID of the job to update



You can also update `--min-num-workers` and `--max-num-workers` individually.

###  REST 

Use the [`projects.locations.jobs.update`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.jobs/update) method:
    
    
    PUT https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/REGION/jobs/JOB_ID?updateMask=runtime_updatable_params.max_num_workers,runtime_updatable_params.min_num_workers
    {
      "runtime_updatable_params": {
        "min_num_workers": MINIMUM_WORKERS,
        "max_num_workers": MAXIMUM_WORKERS
      }
    }

Replace the following:

  * PROJECT_ID: the Google Cloud project ID of the Dataflow job
  * REGION: the region ID of the job's regional endpoint
  * JOB_ID: the ID of the job to update
  * MINIMUM_WORKERS: the minimum number of Compute Engine instances
  * MAXIMUM_WORKERS: the maximum number of Compute Engine instances



You can also update `min_num_workers` and `max_num_workers` individually. Specify which parameters to update in the `updateMask` query parameter, and include the updated values in the `runtimeUpdatableParams` field of the request body. The following example updates `min_num_workers`:
    
    
    PUT https://dataflow.googleapis.com/v1b3/projects/my_project/locations/us-central1/jobs/job1?updateMask=runtime_updatable_params.min_num_workers
    {
      "runtime_updatable_params": {
        "min_num_workers": 5
      }
    }

For jobs that don't use Streaming Engine, you can [replace the existing job](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline#Launching) with an updated value of `maxNumWorkers`.

If you update a streaming job that is not using Streaming Engine, the updated job has Horizontal Autoscaling disabled by default. To keep autoscaling enabled, specify `--autoscalingAlgorithm` and `--maxNumWorkers` for the updated job.

## Set the worker utilization hint

Dataflow uses the average CPU utilization as a signal for when to apply Horizontal Autoscaling. By default, Dataflow sets a target CPU utilization of 0.8. When utilization falls outside of this range, Dataflow might add or remove workers.

For more control over the autoscaling behavior, you can set the target CPU utilization to a value in the range [0.1, 0.9].

  * Set a lower CPU utilization value if you want to achieve lower peak latencies. A lower value allows Dataflow to scale out more aggressively in response to growing worker utilization, and to downscale more conservatively to improve stability. A lower value also provides more headroom when the pipeline is running at a steady state, generally resulting in a lower tail latency. (Tail latency measures the longest wait times before a new record is processed.) 

  * Set a higher value if you want to save resources and keep costs lower when traffic spikes. A higher value prevents excessive upscaling, at the expense of higher latency.




To configure the utilization hint when you run a non-template job, set the `worker_utilization_hint` [service option](https://docs.cloud.google.com/dataflow/docs/reference/service-options). For a template job, update the utilization hint instead, as service options are not supported.

The following example shows how to use `worker_utilization_hint`:

### Java
    
    
    --dataflowServiceOptions=worker_utilization_hint=TARGET_UTILIZATION
    

Replace TARGET_UTILIZATION with a value in the range [0.1, 0.9].

### Python
    
    
    --dataflow_service_options=worker_utilization_hint=TARGET_UTILIZATION
    

Replace TARGET_UTILIZATION with a value in the range [0.1, 0.9].

### Go
    
    
    --dataflow_service_options=worker_utilization_hint=TARGET_UTILIZATION
    

Replace TARGET_UTILIZATION with a value in the range [0.1, 0.9].

For new pipelines, we recommend that you test under realistic loads using the default setting. Then evaluate the autoscaling behavior as it applies to your pipeline and make adjustments as needed.

The utilization hint is just one factor that Dataflow uses when deciding whether to scale workers. Other factors such as backlog and available keys can override the hint value. Also, the hint is not a strict target. The autoscaler tries to keep CPU utilization within the range of the hint value, but the aggregated utilization metric might be higher or lower. For more information, see Streaming autoscaling heuristics.

### Update the utilization hint

To update the utilization hint while a job is running, perform an [in-flight update](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline#perform_an_in-flight_update) as follows:

###  gcloud 

Use the [`gcloud dataflow jobs update-options`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options) command:
    
    
    gcloud dataflow jobs update-options \
      --region=REGION \
      --worker-utilization-hint=TARGET_UTILIZATION \
      JOB_ID

Replace the following:

  * REGION: the region ID of the job's regional endpoint
  * JOB_ID: the ID of the job to update
  * TARGET_UTILIZATION: a value in the range [0.1, 0.9]



To reset the utilization hint to the default value, use the following gcloud command:
    
    
    gcloud dataflow jobs update-options \
      --unset-worker-utilization-hint \
      --region=REGION \
      --project=PROJECT_ID \
      JOB_ID

###  REST 

Use the [`projects.locations.jobs.update`](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.jobs/update) method:
    
    
    PUT https://dataflow.googleapis.com/v1b3/projects/PROJECT_ID/locations/REGION/jobs/JOB_ID?updateMask=runtime_updatable_params.worker_utilization_hint
    {
      "runtime_updatable_params": {
        "worker_utilization_hint": TARGET_UTILIZATION
      }
    }

Replace the following:

  * PROJECT_ID: the Google Cloud project ID of the Dataflow job.
  * REGION: the region ID of the job's regional endpoint.
  * JOB_ID: the ID of the job to update.
  * TARGET_UTILIZATION: a value in the range [0.1, 0.9]



## Set worker parallelism hint

To handle autoscaling with long operations that are less reliant on CPUs, such as ML-intensive workloads, you can set the worker parallelism hint by using Apache Beam resource hints. These hints switch autoscaling to a different mode that's optimized for GPU-intensive workloads or transforms with long processing time.

The following example shows how to attach parallelism hint to a transform:

### Java
    
    
    pcoll.apply(MyCompositeTransform.of(...)
      .setResourceHints(
          ResourceHints.create()
              .withMaxActiveBundlesPerWorker(TARGET_PARALLELISM_PER_WORKER)))
    

Replace TARGET_PARALLELISM_PER_WORKER with a value appropriate for your use case. For general guidance see how to choose a good starting value.

### Python
    
    
    pcoll | MyPTransform().with_resource_hints(
      max_active_bundles_per_worker="TARGET_PARALLELISM_PER_WORKER")
    

Replace TARGET_PARALLELISM_PER_WORKER with a value appropriate for your use case. For general guidance see how to choose a good starting value.

### Choose the worker parallelism hint value

For ML use cases, a good starting value is equalivent to the number of models running in parallel within each worker. This value is bounded by the capacity of the accelerators on the worker and the size of the model.

For other use cases, the pipeline is either memory-bound or CPU-bound. For memory-bound pipelines, use the memory limit to calculate the maximum parallel processing. For CPU-bound pipelines, it's recommended to keep the default autoscaling policy, instead of providing a parallelism hint.

It's possible to fine-tune the value to accommodate processing needs of other stages, such as writing to a sink. Increasing the value by 1 or 2 when your model parallelism is 2 helps recognizing the faster processing time of writing to sink by giving it more slack to account for the processing done in other stages. If your pipeline does not involve in shuffle and transforms are fused together into a single stage, there's no need to adjust the value for other transforms.

This value can also be adjusted to simulate the effects of acceptable backlog delays. For example, if you are comfortable with maximum of 10min of delay and average processing time of your model is 1min, you can choose to increase the value by 1 assuming your max num of workers is set to 10.

### GPU-intensive autoscaling heuristics

In the GPU-intensive setting indicated through setting parallelism hint, Dataflow takes several factors into account when autoscaling. These factors include:

  * **Available keys**. Keys are the fundamental unit of parallelism in Dataflow.
  * **Max active bundles per worker**. This suggests the max ideal number of processing parallelism within the worker.



The general idea behind scaling decisions is calculate the workers needed to handle current load as signaled by _available keys_. For example, if there's 100 keys available to be processed and max parallelism per worker is 10, you should aim to have 10 workers in total.

If your pipeline is complex and has both heavy GPU-intensive workload and numerous CPU-intensive transforms, we recommend you enable [right-fitting](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting). This lets the service make a good distinction between CPU-intensive and GPU-intensive work, and then scale each worker pool accordingly.

## Set the latency tier

Dataflow Horizontal Autoscaling uses backlog duration to determine when to scale workers. By default, Dataflow aims for a backlog of less than 15 seconds, which is suitable for real-time workloads but can result in higher resource costs.

For streaming jobs that use Streaming Engine, you can configure the backlog threshold by choosing a latency tier. A latency tier maps to a target backlog duration, allowing you to configure the autoscaler's sensitivity to backlog duration. An autoscaling decision is only triggered when the backlog duration exceeds your selected tier for several minutes.

The following table describes the available latency tiers:

Latency tier | Allowed estimated backlog time | Intended use case  
---|---|---  
`low_latency` | Less than 15 seconds | Prioritizes rapid scale-up to keep backlog minimal. Default value selected if no tier is specified  
`medium_latency` | Less than 2 minutes | Balanced middle ground between latency and resource costs.  
`high_latency` | Less than 10 minutes | Prioritizes cost savings by allowing backlog to accumulate. Designed for lag-tolerant workloads.  
  
To configure the latency tier when you run a job, set the `enable_latency_tier_lightweight_update` experiment flag:
    
    
    --experiments=enable_latency_tier_lightweight_update=TIER
    

Replace TIER with one of the available latency tiers (for example, `medium_latency`).

### Update the latency tier

To update the latency tier while a job is running, perform an [in-flight update](https://docs.cloud.google.com/dataflow/docs/guides/updating-a-pipeline#perform_an_in-flight_update) by using the [`gcloud dataflow jobs update-options`](https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options) command:
    
    
    gcloud dataflow jobs update-options \
      --region=REGION \
      --latency-tier=TIER \
      JOB_ID

Replace the following:

  * REGION: the region ID of the job's regional endpoint
  * JOB_ID: the ID of the job to update
  * TIER: the target latency tier. One of the following: `low_latency`, `medium_latency`, or `high_latency`



To reset the latency tier and revert to the default low-latency behavior, use the following command:
    
    
    gcloud dataflow jobs update-options \
      --unset-latency-tier \
      --region=REGION \
      JOB_ID

## Streaming autoscaling heuristics

For streaming pipelines, the objective of Horizontal Autoscaling is to minimize backlog while maximizing worker utilization and throughput and to react quickly to spikes in load.

Dataflow takes several factors into account when autoscaling, including:

  * **Backlog**. The estimated backlog time is calculated from the throughput and the backlog bytes still to be processed from the input source. A pipeline is considered backlogged when the estimated backlog time stays above the configured threshold. By default, this threshold is 15 seconds. For more information, see Set the latency tier.

  * **Target CPU utilization**. The default target for average CPU utilization is 0.8. You can override this value.

  * **Available keys**. Keys are the fundamental unit of parallelism in Dataflow.




In some cases, Dataflow uses the following factors in autoscaling decisions. If these factors are used for your job, you can see that information in the [**Autoscaling**](https://docs.cloud.google.com/dataflow/docs/guides/autoscaling-metrics) metrics tab.

  * _Key-based throttling_ uses the number of processing keys received by the job to calculate the cap for user workers, because each key can only be processed by one worker at a time.

  * _Downscale dampening_. If Dataflow detects that unstable autoscaling decisions have occurred, it slows the rate of downscaling in order to improve stability.

  * _CPU-based upscale_ uses high CPU utilization as an upscaling criteria.

  * For streaming jobs that don't use [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine), scaling might be constrained by the number of Persistent Disks. For more information, see Set the autoscaling range.

  * _GPU-intensive autoscaling_ , if enabled by setting worker parallelism hint. For more information, see GPU intensive autoscaling heuristics




**Upscaling**. If a streaming pipeline remains backlogged with sufficient parallelism on the workers for several minutes, Dataflow scales up. Dataflow attempts to clear the backlog within approximately 150 seconds of scaling up, given the current throughput per worker. If there is backlog but the worker doesn't have enough parallelism for additional workers, the pipeline does not scale up. (Scaling the number of workers beyond the number of keys available for parallel processing doesn't help process the backlog faster.)

**Downscaling** When the autoscaler makes a downscaling decision, backlog is the highest priority factor. The autoscaler aims for a backlog based on the latency tier. If the backlog drops sufficiently below the target for several minutes, and average worker utilization is below the CPU utilization target, then Dataflow scales down. As long as the backlog is acceptable, the autoscaler tries to maintain CPU utilization close to the target CPU utilization. If utilization is already sufficiently close to the target, however, the autoscaler might keep the number of workers unchanged, because each downscaling step has a cost.

Streaming Engine also uses a predictive autoscaling technique based on timer backlog. Unbounded data in a streaming pipeline is divided into [windows](https://docs.cloud.google.com/dataflow/docs/concepts/streaming-pipelines#windows) grouped by timestamps. At the end of a window, timers fire for each key being processed in that window. The firing of a timer indicates that the window is expired for a given key. Streaming Engine can measure the timer backlog and predict how many timers will fire at the end of a window. By using the timer backlog as a signal, Dataflow can estimate the amount of processing that must happen when future timers fire. Based on the estimated future load, Dataflow autoscales in advance to meet expected demand.

## Metrics

To find the current autoscale limits for a job, query the following metrics:

  * `job/max_worker_instances_limit`: Maximum number of workers.
  * `job/min_worker_instances_limit`: Minimum number of workers.



To get information about worker utilization, query the following metrics:

  * `job/aggregated_worker_utilization`: The aggregated worker utilization.
  * `job/worker_utilization_hint`: The current worker utilization hint.



To get insights into the behavior of the autoscaler, query the following metric:

  * `job.worker_utilization_hint_is_actively_used`: Indicates whether the autoscaler is actively using the worker utilization hint. If other factors override the hint when this metric is sampled, the value is `false`.
  * `job/horizontal_worker_scaling`: Describes the decisions taken by the autoscaler. This metric contains the following labels: 
    * `direction`: Specifies whether the autoscaler scaled up, scaled down, or took no action.
    * `rationale`: Specifies the rationale for the autoscaler's decision.



For more information, see [Cloud Monitoring metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_d_h#gcp-dataflow). These metrics are also displayed in the [autoscaling monitoring charts](https://docs.cloud.google.com/dataflow/docs/guides/autoscaling-metrics).

## What's next

  * [Monitor Dataflow autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/autoscaling-metrics)
  * [Troubleshoot Dataflow autoscaling](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-autoscaling)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
