---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus/
title: About GPU accelerators \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:47.431030+00:00
---

# About GPU accelerators  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  About GPU accelerators Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

AI Hypercomputer provides vertically integrated infrastructure optimized for demanding artificial intelligence (AI) and machine learning (ML) workloads. High-performance NVIDIA GPUs are categorized by how the system handles their lifecycle events and maintenance: _General GPUs_ and Clustered GPUs.

To identify the optimal infrastructure category for your workload, see [Choose your accelerator infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-infrastructure).

## General GPUs

General GPUs are managed as independent compute units, by using standard Compute Engine and Google Kubernetes Engine (GKE) APIs to integrate directly with Google Cloud's control plane.

General GPUs include the following machine series:

  * **[A3 High with 1, 2, or 4 (NVIDIA H100) GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#a3-high)** : optimized for standard training and inference workloads that don't require an 8-GPU synchronized cluster.
  * **[A3 Edge (NVIDIA H100)](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#a3-edge)** : optimized for inference that is distributed across multiple hosts with high throughput using standard VPC networking.
  * **[A2 (NVIDIA A100)](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#a2)** : optimized for high-performance single-node serving and small-scale fine-tuning.
  * **[G4 (NVIDIA RTX PRO 6000)](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#g4)** : optimized for cost-effective entry-level inference and graphics workloads.
  * **[G2 (NVIDIA L4)](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#g2)** : optimized for mainstream inference and RAG.
  * **[N1 (NVIDIA T4 or V100)](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus#n1)** : optimized for entry-level inference and research tasks that prioritize cost over high-performance interconnects.



## Clustered GPUs

Clustered GPUs are managed as a single, tightly coupled system of thousands of interconnected accelerators using Cluster Director.

Clustered GPUs include the following machine series:

  * **[A4X Max (NVIDIA GB300)](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4x-max-machine)** : designed for bare-metal exascale training and high performance computing, featuring NVIDIA GB300 Grace Blackwell Ultra Superchips.
  * **[A4X (NVIDIA GB200)](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4x-machine) and [A4 (NVIDIA B200)](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a4)**: designed for foundation model training and exascale foundation model training.
  * **[A3 Ultra (NVIDIA H200), A3 Mega (NVIDIA H100), and A3 High with 8 (NVIDIA H100) GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus#a3)** : optimized for large-scale distributed training and multi-host inference involving massive data tables.



## GPU performance considerations

To evaluate and optimize your workload's performance, you can track hardware-level metrics such as CUDA core and Tensor Core utilization. To monitor your resources and evaluate performance across both General and Clustered environments, see the following:

  * [Monitoring dashboards](https://docs.cloud.google.com/ai-hypercomputer/docs/monitor): track real-time GPU utilization and memory usage for individual standalone instances or orchestrated cluster fleets.
  * [Goodput metrics recipes](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/goodput-recipes): measure the percentage of time your accelerators perform useful computation versus system overhead, which is highly recommended for large-scale distributed training on clustered hardware.



## What's next

  * To evaluate your infrastructure requirements, see [Choose your accelerator infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-infrastructure).
  * To review the process and choices to make when you start a cluster, see [Plan and create your AI infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/process-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
