---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma/
title: Overview \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:35:07.257289+00:00
---

# Overview  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Overview Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document describes the Collective Communication Analyzer (CoMMA), a library for collecting NCCL telemetry for Google Cloud services. _NCCL telemetry_ collects performance metrics and operational events that NCCL generates during its execution. The [NVIDIA Collective Communication Library (NCCL)](https://developer.nvidia.com/nccl) accelerates high-performance communication between GPUs running in parallel and distributed computing systems. This high-performance communication is especially useful for deep learning and high performance computing (HPC).

For NCCL versions 2.23 and later, NVIDIA introduced the [NCCL profiler plugin API](https://developer.nvidia.com/blog/new-scaling-algorithm-and-initialization-with-nvidia-collective-communications-library-2-23/#new_profiler_plugin_api%C2%A0), which lets developers register function callbacks to collect telemetry during NCCL collective operations. Google provides the [Collective Communication Analyzer (CoMMA)](https://github.com/google/CoMMA), which is a library that uses NVIDIA's NCCL profiler plugin API to collect NCCL telemetry for Google Cloud services. CoMMA automatically installs and enables for some images, but you can also disable, re-enable, or manually install and enable CoMMA to control data collection.

## Images that have CoMMA enabled

For A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) machine types, CoMMA is installed and automatically enabled when you use any images that packages the gIB NCCL plugin. The following images contain the gIB NCCL plugin:

  * [Container-Optimized OS with containerd (cos_containerd)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos-variants) node images: Google Kubernetes Engine (GKE) uses these images for creating GKE Autopilot clusters. The CoMMA binaries are available in the `/home/kubernetes/bin/gib` directory.
  * [Deep learning Software Layer container images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#dlsl-container-images): you use these images to deploy and configure AI and ML frameworks and libraries on GKE clusters.



If you use any of these images and want to disable CoMMA from collecting NCCL telemetry, then see [Disable CoMMA](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/configure-comma#disable-plugin). However, CoMMA must be enabled for features such as [straggler detection](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor#straggler-detection) or [unresponsive workload detection](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor#unresponsive-workload-detection) to function. If you don't use these images and want to enable CoMMA to collect NCCL telemetry, then see [Install CoMMA](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/configure-comma#install-plugin).

## Benefits

The NCCL telemetry that CoMMA collects helps identify performance bottlenecks, specifically stragglers, in GPU communication. CoMMA collects fine-grained data, such as latency histograms for collective communication operations. A diagnostic service can then process and use this data to pinpoint stragglers.

Using CoMMA to collect telemetry offers the following benefits:

  * **Required for straggler detection and unresponsive workload detection** : CoMMA collects the fine-grained NCCL telemetry to identify performance bottlenecks or stragglers in GPU-to-GPU communication. CoMMA provides detailed NCCL telemetry that helps identify and resolve issues in large-scale AI and ML training workloads.

For example, CoMMA captures the algorithm used in NCCL operations. This information is valuable for performance analysis and tuning because different algorithms can have significantly varying performance characteristics based on workload and system configuration.

CoMMA also helps with the troubleshooting of suboptimal performance and errors. It traces errors originating in lower-level transport layers, such as TCP, RDMA, or switch fabrics, back to specific NCCL collectives and initiating nodes. It can recognize when a heartbeat telemetry signal stops responding and trace potential causes for unresponsive workloads.

  * **Low-overhead tracing** : CoMMA uses minimal computational resources during active NCCL telemetry collection, making it ideal for performance-sensitive and long-running machine learning workloads like large language model (LLM) training.

  * **Broaden NCCL telemetry scope** : CoMMA uses the NCCL profiler plugin API. This API collects a broader scope of NCCL telemetry in comparison to transport-based plugins. Transport-based plugins primarily collect telemetry about the underlying network transport, including data transfers over network hardware and network protocols. The profiler plugin collects telemetry for NCCL's communication operations, including the timing of collective communications, proxy operations, and data transfers.




## Understand how CoMMA works

During application runtime, NCCL automatically loads the CoMMA libraries that are installed in the location specified by the `LD_LIBRARY_PATH` environment variable. CoMMA then collects NCCL telemetry, which other Google services can then use. You can also optionally export this data to your local file system.

## What's next

  * Learn how to [enable, disable, and configure CoMMA](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/configure-comma).
  * Learn how to [troubleshoot issues with CoMMA](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-comma).
  * Learn how to [detect and resolve stragglers](https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-slow-performance).
  * Learn how to [detect unresponsive workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor#unresponsive-workload-detection).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
