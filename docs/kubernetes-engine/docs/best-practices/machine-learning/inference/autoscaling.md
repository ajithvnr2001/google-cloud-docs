---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling/
title: Best practices for autoscaling large language model (LLM) inference workloads with GPUs on Google Kubernetes Engine (GKE) \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:45.478767+00:00
---

# Best practices for autoscaling large language model (LLM) inference workloads with GPUs on Google Kubernetes Engine (GKE)  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Best practices for autoscaling large language model (LLM) inference workloads with GPUs on Google Kubernetes Engine (GKE) Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This best practices guide shows you the available metrics and how to select suitable metrics to set up your [Horizontal Pod Autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler) (HPA) for your inference workloads on GKE. HPA is an efficient way to ensure that your model servers scale appropriately with load. Fine-tuning the HPA settings is the primary way to align your provisioned hardware cost with traffic demands to achieve your inference server performance goals.

For examples of how to implement these best practices, see [Configure autoscaling for LLM workloads on GPUs with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling).

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

### Objectives

This guide is intended for generative AI customers, new or existing GKE users, ML Engineers, and LLMOps (DevOps) engineers who are interested in optimizing their LLM workloads using GPUs with Kubernetes.

After you read this guide, you should be able to:

  * Understand autoscaling metrics for LLM inference.
  * Understand the high-level tradeoffs when considering which metrics to autoscale on.



## Overview of autoscaling metrics for LLM inferencing

The following metrics are available on GKE:

  * Server metrics
  * GPU metrics
  * CPU metrics



### Server metrics

Popular LLM inference servers like TGI, vLLM, and NVIDIA Triton emit workload-specific performance metrics. GKE simplifies scraping and autoscaling of workloads based on these server-level metrics. You can use these metrics to gain visibility into performance indicators like batch size, queue size, and decode latencies.

Based on these metrics, you can direct autoscaling on the most relevant performance indicators. Key server-level metrics for autoscaling include:

  * **Queue Size:** The number of requests awaiting processing in the server queue. Use queue size to maximize throughput and minimize cost within a certain target latency threshold. To learn more, see the related [best practice](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling#queue-size) section.
  * **Batch Size:** The number of requests undergoing inference. Use batch size to reach lower target latency thresholds than queue size. To learn more, see the related [best practice](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling#batch-size) section.



These metrics are often resilient to performance and traffic fluctuations, making them a reliable starting point for autoscaling across diverse GPU hardware setups.

### GPU metrics

GPUs emit various usage and performance metrics, offering workload-agnostic autoscaling for any GPU-based task, including inferencing workloads that lack custom metrics. To learn how to set up DCGM collection, see [Configure DCGM collection](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics#configure-dcgm-collection).

Common GPU metrics for GKE include:

GPU metric | Usage | Limitations  
---|---|---  
GPU Utilization (`DCGM_FI_DEV_GPU_UTIL`) | Measures the duty cycle, which is the amount of time that the GPU is active.  | Does not measure how much work is being done while the GPU is active. This makes it difficult to map inference based performance metrics, such as latency and throughput, to a GPU Utilization threshold.  
GPU Memory Usage (`DCGM_FI_DEV_FB_USED`) | Measures how much GPU memory is being used at a given point in time. This is useful for workloads that implement dynamic allocation of GPU memory. |  For workloads that preallocate GPU memory or never deallocate memory (such as workloads running on TGI and vLLM), this metric only works for scaling up, and won't scale down when traffic decreases.  
  
### CPU metrics

In GKE, HPA works out of the box with CPU and memory-based autoscaling. For workloads that run on CPUs, CPU and memory utilization metrics are typically the primary autoscaling metric.

For inference workloads running on GPUs, we don't recommend CPU and memory utilization as the only indicators of the amount of resources a job consumes because inferencing workloads primarily rely on GPU resources. Therefore, using CPU metrics alone for autoscaling can lead to suboptimal performance and costs.

## Considerations for choosing your autoscaling metrics

Use the following considerations and best practices to select the best metric for autoscaling on GKE to meet your inference workload performance goals.

### Best practice: Use queue size to maximize throughput and minimize cost within a certain target latency threshold

We recommend queue size autoscaling when optimizing throughput and cost, and when your latency targets are achievable with the maximum throughput of your model server's max batch size.

Queue size directly correlates to request latency. Incoming requests queue up in the model server before they are processed, and this queue time adds to overall latency. Queue size is a sensitive indicator of load spikes, as increased load quickly fills the queue.

Autoscaling based on queue size minimizes queue time by scaling up under load, and scaling down when the queue is empty. This approach is relatively easy to implement and largely workload-agnostic, because queue size is independent of request size, model, or hardware.

Consider focusing on queue size if you want to maximize throughput while respecting your model server's configuration. Queue size tracks pending, not processing, requests. vLLM and TGI use continuous batching, which maximizes concurrent requests and keeps the queue low when batch space is available. The queue grows noticeably when batch space is limited, so use the growth point as a signal to initiate scale-up. By combining queue size autoscaling with optimized batch throughput, you can maximize request throughput.

#### Determine the optimal queue size threshold value for HPA

Be mindful of the [HPA tolerance](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details), which defaults to a 0.1 no-action range around the target value to dampen oscillation.

To choose the correct queue size threshold, start with a value between 3-5 and gradually increase it until requests reach the preferred latency. Use the [`locust-load-inference`](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/benchmarks/benchmark/tools/locust-load-inference) tool for testing. For thresholds under 10, fine-tune HPA scale-up settings to handle traffic spikes.

You can also create a [Cloud Monitoring custom dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards) to visualize the metric behavior.

#### Limitations

Queue size doesn't directly control concurrent requests, so its threshold can't guarantee lower latency than the max batch size allows. As a workaround, you can manually reduce the max batch size or autoscale on batch size.

### Best practice: Use batch size to reach lower target latency thresholds than queue size

We recommend choosing batch size-based autoscaling if you have latency-sensitive workloads where queue-based scaling isn't fast enough to meet your requirements.

Batch size directly correlates to the throughput and latency of an incoming request. Batch size is a good indicator for spikes in load, as an increase in load causes more requests to be added to the existing batch, causing a larger batch size. In general, the larger the batch size, the higher the latency. Autoscaling on batch size ensures that your workload scales up to maximize the number of requests being processed in parallel at once, and scale down when there are less requests being processed in parallel.

If queue size already meets your latency targets, prioritize it for autoscaling. This maximizes both throughput and cost efficiency. However, batch size is valuable for latency-sensitive workloads. Larger batch sizes increase throughput but also raise latency due to the prefill phase of some requests interrupting the decode phase of others in continuous batching model servers. You can monitor batch size patterns and use autoscaling to minimize concurrent requests during load spikes.

If your model server allows, we recommend customizing the max batch size as an additional tuning mechanism. You can also pair this with queue-based autoscaling.

#### Determine the optimal batch size threshold value for HPA

Be mindful of the [HPA tolerance](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/#algorithm-details), which is a default 0.1 no-action range around the target value to dampen oscillation.

To choose the right batch size threshold, experimentally increase the load on your server and observe where the batch size peaks. We also recommend using the [`locust-load-inference`](https://github.com/GoogleCloudPlatform/ai-on-gke/tree/main/benchmarks/benchmark/tools/locust-load-inference) tool for testing. Once you've identified the max batch size, set the initial target value slightly beneath this maximum and decrease it until the preferred latency is achieved.

You can also create a [Cloud Monitoring custom dashboard](https://docs.cloud.google.com/monitoring/charts/dashboards) to visualize the metric behavior.

#### Limitations

Autoscaling on batch size, while helpful for latency control, has limitations. Varying request sizes and hardware constraints make finding the right batch size threshold challenging.

### Best practice: Optimize your HPA configuration

We recommend setting these HPA configuration options:

  * **Stabilization window** : Use this HPA configuration option to prevent rapid replica count changes due to fluctuating metrics. Defaults are 5 minutes for scale-down (avoiding premature downscaling) and 0 for scale-up (ensuring responsiveness). Adjust the value based on your workload's volatility and your preferred responsiveness.
  * **Scaling policies** : Use this HPA configuration option to fine-tune the scale-up and scale-down behavior. You can set the "Pods" policy limit to specify the absolute number of replicas changed per time unit, and the "Percent" policy limit to specify by the percentage change.



To learn more about these options, see [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale) in the open source Kubernetes documentation.

## What's next

  * Learn how to [Configure autoscaling for LLM workloads on GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
