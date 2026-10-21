---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling-tpu/
title: Best practices for autoscaling large language model (LLM) inference workloads with TPUs \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:11.053646+00:00
---

# Best practices for autoscaling large language model (LLM) inference workloads with TPUs  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling-tpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Best practices for autoscaling large language model (LLM) inference workloads with TPUs Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This best practices guide shows you the available metrics and how to select suitable metrics to set up your [Horizontal Pod Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler)(HPA) for your single-host [JetStream](https://github.com/google/JetStream) inference workloads with [TPUs](https://docs.cloud.google.com/tpu/docs/intro-to-tpu) on GKE. HPA is an efficient way to ensure that your model servers scale appropriately with load. Fine-tuning the HPA settings is the primary way to align your provisioned hardware cost with traffic demands to achieve your inference server performance goals.

For examples of how to implement these best practices, see [Configure autoscaling for LLM workloads on TPUs with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling-tpu).

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

### Objectives

This guide is intended for generative AI customers, new or existing GKE users, ML Engineers, and LLMOps (DevOps) engineers who are interested in optimizing their single-host JetStream workloads using TPUs with Kubernetes.

After you read this guide, you should be able to:

  * Understand key autoscaling metrics for single-host JetStream inference.
  * Understand the high-level tradeoffs when considering which metrics to autoscale on.



## Overview of autoscaling metrics for JetStream inferencing

We recommend using the following metrics:

  * Server metrics
  * TPU metrics



### Server metrics

JetStream, like many other LLM inference servers, provides performance metrics. GKE simplifies monitoring and autoscaling JetStream based on these server-level metrics. In order to configure any autoscaling, you must first understand how JetStreams request pipeline influences key performance indicators. All incoming requests move through a prefill queue, transfer queue, and generate queue, then becoming a decode request. JetStream accepts decode requests on a rolling basis and processes them concurrently using a fixed number of decode threads. The percentage of decode engines occupied with handling a decode request at a given point is measured as the `jetstream_slots_used_percentage` metric.

For scaling single host JetStream, this has two implications for latency and throughput:

  * Requests won't be backlogged in the queues if the rate of requests coming in is less than the rate at which the decode slots can process the requests. If JetStream has no backlog, then throughput will be proportional to the rate of incoming requests. Latency will remain mostly constant but increase slightly and proportionally to the number of concurrent decode requests since newly accepted decode requests will interrupt decode.
  * Requests will be backlogged in the queues once the rate of requests coming in exceeds the rate at which the decode slots can process the requests. If JetStream has a backlog, then request latency will increase more significantly and proportionally to the number of requests backlogged while throughput will remain constant.



The following server metrics will have the strongest correlation with these relevant performance indicators, we recommend using these for autoscaling:

  * **`jetstream_prefill_backlog_size`:** The number of requests awaiting processing in the server queue (backlog). This metric has a strong correlation with latency. To learn more, see the related [best practice](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling-tpu#queue-size) section.
  * **`jetstream_slots_used_percentage`:** The number of requests undergoing inference as a percentage of the total number of requests JetStream is capable of handling. This metric has a strong correlation with throughput. To learn more, see the related [best practice](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling-tpu#slots-used-percentage) section.



These metrics are often resilient to performance and traffic fluctuations, making them a reliable starting point for autoscaling across diverse TPU hardware setups.

**Note:** If serving single-host jetstream, don't use `jetstream_transfer_backlog_size` or `jetstream_generate_backlog_size` as targets since accumulated requests will land in the prefill queue. Instead, use `jetstream_prefill_backlog_size`.

### TPU metrics

Given LLM serving is bottlenecked by memory and not compute, we recommend that you scale JetStream with memory usage rather than with other TPU metrics since it best reflects the resource utilization of the hardware. To learn more, see the related [best practice](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling-tpu#tpu-hbm) section.

## Considerations for choosing your autoscaling metrics

Use the following considerations and best practices to select the best metric for autoscaling on GKE to meet your inference workload performance goals.

### Best practice: Use prefill backlog (queue) size to maximize throughput and minimize cost within a certain target latency threshold

We recommend prefill queue size autoscaling when optimizing throughput and cost, and when your latency targets are achievable with the maximum throughput of your model server's per device batch size.

Prefill queue size directly correlates to request latency. Incoming requests queue up in the model servers prefill queue before they are processed, and this queue time adds to overall latency. Queue size is a sensitive indicator of load spikes, as increased load quickly fills the queue.

Autoscaling based on prefill queue size minimizes queue time by scaling up under load, and scaling down when the queue is empty. This approach is relatively easy to implement because queue size is independent of request size, model, or hardware.

Consider focusing on prefill queue size if you want to maximize throughput of each model server replica. Prefill queue size tracks pending, not processing, requests. JetStream uses continuous batching, which maximizes concurrent requests and keeps the queue low when batch space is available. The queue grows noticeably when batch space is limited, so use the growth point as a signal to initiate scale-up. By combining queue size autoscaling with optimized batch throughput, you can maximize request throughput.

#### Determine the optimal queue size threshold value for HPA

To choose the correct queue size threshold, start with a value between 3-5 and gradually increase it until requests reach the preferred latency. Use the [`locust-load-inference`](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/benchmarks/benchmark/tools/locust-load-inference) tool for testing. For thresholds under 10, fine-tune HPA scale-up settings to handle traffic spikes.

You can also create a [Cloud Monitoring custom dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards) to visualize the metric behavior.

#### Limitations

Be mindful of the [HPA tolerance](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details), which defaults to a 0.1 no-action range around the target value to dampen oscillation.

Prefill queue size doesn't directly control concurrent requests, so its threshold can't guarantee lower latency than the per device batch size allows. As a workaround, you can manually reduce the per device batch size or autoscale on batch size.

### Best practice: Use slots_used percentage to reach lower target latency thresholds than queue size

We recommend choosing slots_used based autoscaling if you have latency-sensitive workloads where queue-based scaling isn't fast enough to meet your requirements.

Autoscaling on slots_used ensures that your workloads throughput scales up to maximize the number of requests being processed in parallel at once, and scales down when there are less requests being processed in parallel. This has two implications for latency. Firstly, since slots_used based autoscaling scales in order to assure a slot for each incoming request, how close the threshold is set to 1 will correspond to the likelihood of a request spending time enqueued and consequently having a higher latency. Secondly, larger batch sizes increase throughput but also increase latency due to the prefill phase of some requests interrupting the decode phase of others in continuous batching model servers. You can monitor batch size patterns and use autoscaling to minimize concurrent requests during load spikes.

If queue size already meets your latency targets, prioritize it for autoscaling. This maximizes both throughput and cost efficiency. However, slots_used is valuable for latency-sensitive workloads.

We also recommend tuning the per device batch size to an appropriate value prior to exploring slots_used based autoscaling. Optionally you can also pair this with queue-based autoscaling.

#### Determine the optimal slots_used percentage threshold value for HPA

To choose the right batch size threshold, experimentally increase the load on your server and observe where the batch size peaks. We also recommend using the [`locust-load-inference`](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/benchmarks/benchmark/tools/locust-load-inference) tool for testing. Once you've identified a optimal per device batch size where memory use is maximized you can then configure your slots_used percentage target. Set the initial target value slightly beneath 1 and decrease it until the preferred latency is achieved.

You can also create a [Cloud Monitoring custom dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards) to visualize the metric behavior.

#### Limitations

Be mindful of the [HPA tolerance](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details), which is a default 0.1 no-action range around the target value to dampen oscillation.

Autoscaling on slots_used percentage, while helpful for latency control, has limitations. Varying request sizes and hardware constraints make finding the right slots_used percentage threshold challenging. Having a scale rule attempting to keep the average slots_used percentage under 100% means that the scale rule is attempting to keep a non-zero number of available slots. These available slots correspond to available throughput not being used which is not ideal if you're looking to make the most of your available TPUs.

### Best practice: Use TPU high bandwidth memory (HBM) use to maximize hardware utilization

TPU high bandwidth memory (HBM) use has the most direct correspondence with hardware utilization, even in comparison to system metrics since they don't take into account request sizes. Although scaling with queue size better maximize hardware utilization, it will do so at the expense of latency. If you prefer to rely on system metrics rather than server metrics, we recommend HBM usage as the best alternative for autoscaling with slots_used since they both correspond with throughput. For more information about TPU memory, see [How a TPU works](https://docs.cloud.google.com/tpu/docs/intro-to-tpu#how_a_tpu_works).

Increasing batch size beyond the optimal point improves throughput, but also increases the risk of out of memory (OOM) errors. We highly recommend scaling based on the HBM metric to balance throughput and stability. We recommend not scaling with prefill queue size and HBM usage at the same time since as load increases, HBM usage will increase and trigger scaling first.

#### Determine the optimal TPU HBM usage threshold value for HPA

Prior to picking the memory use threshold, we recommend setting the per device batch size to a value that maximizes the memory used when operating under the maximum expected load. Note this value will need to be determined experimentally and will depend heavily on total HBM as well as expected prompt and response lengths. We recommend using the [`locust-load-inference`](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/benchmarks/benchmark/tools/locust-load-inference) tool for your experimentation and testing.

Similar to per-device batch size, set the threshold to maximize TPU memory utilization while minimizing the risk of OOM behavior.

You can also create a [Cloud Monitoring custom dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards) to visualize the metric behavior.

#### Limitations

There are two caveats that diminish the strength with which latency and throughput correspond with HBM use, namely the volatility of HBM use and the lower sampling rate of TPU metrics in general. Also, although there still is a correspondence between HBM use and latency, increases in HBM use impact latency far less than increases in the number of queued requests.

### Best practice: Optimize your HPA configuration

We recommend setting these HPA configuration options:

  * **Stabilization window** : Use this HPA configuration option to prevent rapid replica count changes due to fluctuating metrics. Defaults are 5 minutes for scale-down (avoiding premature downscaling) and 0 for scale-up (ensuring responsiveness). Adjust the value based on your workloads volatility and your preferred responsiveness.
  * **Scaling policies** : Use this HPA configuration option to fine-tune the scale-up and scale-down behavior. You can set the "Pods" policy limit to specify the absolute number of replicas changed per time unit, and the "Percent" policy limit to specify by the percentage change.



To learn more about these options, see [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale) in the open source Kubernetes documentation.

## What's next

  * Learn how to [Configure autoscaling for LLM workloads on TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling-tpu).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
