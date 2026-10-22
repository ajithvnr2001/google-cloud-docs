---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview/
title: Optimize cluster networking by using NCCL/gIB \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:00.852707+00:00
---

# Optimize cluster networking by using NCCL/gIB  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Optimize cluster networking by using NCCL/gIB Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

Modern machine learning frameworks often use the [NVIDIA Collective Communications Library (NCCL)](https://developer.nvidia.com/nccl) for GPU-to-GPU communication primitives.

Google's enhanced version of NCCL is called NCCL/gIB and is available on Google Cloud's A3 Ultra, A4, and A4X VMs. NCCL/gIB is often more performant than upstream NCCL on Google infrastructure. Because NCCL performance can impact overall workload performance, we recommend that you use NCCL/gIB.

NCCL/gIB contains Google-specific features and optimizations such as the following:

  * The **gIB network plugin** offers improved load balancing on Google's networks, leading to high throughput and low latency more consistently during collective operations.
  * A **custom tuner plugin** , which selects the best tuning options on Google Cloud VMs.
  * The [**CoMMA profiler plugin**](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma) provides detailed performance metrics and diagnostic data for your workload.
  * The **env plugin** provides platform-specific variable configurations across Google Cloud VMs.



## NCCL/gIB architecture

NCCL/gIB interacts with your machine learning framework and the NVIDIA GPUs on your clusters to optimize performance and gather telemetry, as shown in this diagram:

![The ML workload is managed by a ML framework that connects to both the NVIDIA GPUs and NCCL, while NCCL connects to various Google tools and plugins.](https://docs.cloud.google.com/static/ai-hypercomputer/images/nccl-gib-architecture-v2.png)

## Benefits of using NCCL/gIB

Although it's possible to use the upstream NVIDIA Collective Communications Library on Google Cloud VMs without stability problems, NCCL/gIB is better optimized for Google Cloud and the performance disparity can be very significant for certain communication patterns, even with the same NCCL parameters.

For example, the following graph shows a comparison of NCCL/gIB with upstream NCCL on AllReduce performance. NCCL/gIB outperforms upstream NCCL by as much as 12x on certain message sizes.

![A graph showing NCCL/gIB outperforms upstream NCCL at AllReduce tasks.](https://docs.cloud.google.com/static/ai-hypercomputer/images/nccl-gib-all-reduce.png)

32-node NCCL AllReduce performance using A3 Ultra (H200) with no background traffic.

Similarly in a comparison of NCCL/gIB with upstream NCCL on AllGather performance with background traffic, NCCL/gIB outperforms upstream NCCL by approximately 50% on larger message sizes, as shown in this graph.

![A graph showing NCCL/gIB outperforms upstream NCCL at AllGather tasks.](https://docs.cloud.google.com/static/ai-hypercomputer/images/nccl-gib-all-gather.png)

32-node NCCL AllGather performance using A3 Ultra (H200) on a shared fabric with a noisy background.

In addition, the [**CoMMA profiler plugin**](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/comma) provides Google with improved custom telemetry, enabling us to better assist you should a workload-level issue arise.

## Install NCCL/gIB

Before you run NCCL tests, you must [install NCCL/gIB](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/install-nccl) in your runtime environment.

## Use NCCL/gIB

To run NCCL/gIB tests on your cluster, choose the page from the following list that best meets your requirements:

  * [Use gIB NCCL plugins in NVIDIA NGC containers](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/ngc-containers)
  * [Run NCCL tests on Compute Engine VMs](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-vms)
  * [Run NCCL on GKE clusters that use Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke)
  * [Run NCCL on GKE clusters that use A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom-a4x)
  * [Run NCCL on GKE clusters that use A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-gke-custom)
  * [Run NCCL tests on Slurm clusters](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/test-slurm)
  * [Run NCCL tests in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/monitor/cluster-health#verify-health)



To learn how to address any issues with your cluster after you have run your tests, see [Collect and understand NCCL/gIB logs for troubleshooting](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/collect-and-understand).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
