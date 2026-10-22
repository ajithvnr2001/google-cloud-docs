---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpu-ironwood/
title: About Ironwood (TPU7x) in GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:38.678234+00:00
---

# About Ironwood (TPU7x) in GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpu-ironwood/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  About Ironwood (TPU7x) in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document provides an overview of Ironwood (TPU7x) in Google Kubernetes Engine (GKE). Ironwood (TPU7x) is Google's seventh-generation [Tensor Processing Unit (TPU)](https://docs.cloud.google.com/tpu), custom-designed for large-scale AI workloads. It offers a significant performance improvement over previous TPU generations, which lets you train and serve larger and more complex models.

## Characteristics of Ironwood (TPU7x)

Ironwood (TPU7x) introduces unique features that differentiate it from other TPU versions. These features impact availability, node pool configuration, and workload performance.

For information about the underlying hardware, see [Ironwood (TPU7x) architecture](https://docs.cloud.google.com/tpu/docs/tpu7x).

### Availability

Ironwood (TPU7x) is available in GKE Standard clusters that run version 1.34.0-gke.2201000 and later, and in Autopilot clusters that run version 1.34.1-gke.3084001 and later.

### Workload policy for multi-host node pools

Ironwood (TPU7x) uses a [workload policy](https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy) to configure the physical placement of the underlying infrastructure when you create multi-host TPU slice node pools. You create a workload policy and then apply it by using the `--placement-policy` flag. This policy replaces the `--tpu-topology` flag used by other TPU versions.

A workload policy is a type of resource policy that lets you configure the physical placement of infrastructure. Ironwood (TPU7x) supports the _High throughput_ workload policy. This policy colocates the TPU VMs to reduce network latency and lets you define the maintenance strategy to minimize workload disruptions.

### NUMA binding

The Ironwood (TPU7x) architecture includes the following elements:

  * Each Ironwood (TPU7x) virtual machine (VM) contains four chips and two NICs.
  * Each VM contains two [Non-Uniform Memory Access (NUMA)](https://en.wikipedia.org/wiki/Non-uniform_memory_access) nodes.
  * The CPU, memory, and NICs resources are equally split between the two NUMA nodes.



Accessing resources across different NUMA nodes (cross-NUMA access) can introduce performance bottlenecks in your workloads. Therefore, to optimize your workload performance, GKE lets you deploy your workloads in a [_multi-container_ setup](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#deploy-multi-container). This binds each container to the CPU, memory, and TPU resources within a given NUMA node.

## Reference implementations of LLMs

To learn how to deploy large language models (LLMs) on Ironwood (TPU7x), see the following reference implementations. You can use one of the following options for cluster creation:

  * **GKE XPK** : use Accelerated Processing Kit (XPK) to quickly create GKE clusters and run workloads for proofs-of-concept and testing. For more information, see the [XPK documentation](https://github.com/AI-Hypercomputer/xpk/blob/main/README.md).
  * **GKE on Google Cloud CLI:** use the Google Cloud CLI to create your GKE cluster instance manually for precise customization or expansion of existing production GKE environments.

LLM | GKE XPK | GKE on Google Cloud CLI  
---|---|---  
Llama 70b with BF16 and a `4x4x4` topology | [Pretrain llama3.1-70b workload on Ironwood GKE clusters with XPK](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/training/ironwood/llama3.1-70b/8k-bf16-tpu7x-4x4x4/xpk) | [Pretrain llama3.1-70b workload on Ironwood GKE clusters with Kubernetes JobSet](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/training/ironwood/llama3.1-70b/8k-bf16-tpu7x-4x4x4/k8s)  
DeepSeek with BF16 and a `4x4x8` topology | [Pretrain deepseek3-671b workload on Ironwood GKE clusters with XPK](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/training/ironwood/deepseek3-671b/4k-bf16-tpu7x-4x4x8/xpk) | [Pretrain deepseek3-671b workload on Ironwood GKE clusters with Kubernetes JobSet](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/training/ironwood/deepseek3-671b/4k-bf16-tpu7x-4x4x8/k8s)  
GPT-oss-120b with BF16 and a `4x4x4` topology | [Pretrain gpt-oss-120b workload on Ironwood GKE clusters with XPK](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/training/ironwood/gpt-oss-120b/8k-bf16-tpu7x-4x4x4/xpk) | [Pretrain gpt-oss-120b workload on Ironwood GKE clusters with Kubernetes JobSet](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/training/ironwood/gpt-oss-120b/8k-bf16-tpu7x-4x4x4/k8s)  
Qwen3-235b-a22b with BF16 and a `4x8x8` topology | [Pretrain qwen3-235b-a22b workload on Ironwood GKE clusters with XPK](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/training/ironwood/qwen3-235b-a22b/4k-bf16-tpu7x-4x8x8) | Not available  
  
## What's next

  * Learn how to [plan TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/plan-tpus).
  * Learn how to [deploy TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus).
  * Try the end-to-end tutorials for Ironwood (TPU7x): 
    * [Run training workload with Ironwood (TPU7x) and reservations using Cloud Storage](https://github.com/AI-Hypercomputer/xpk/blob/main/docs/usage/tpu7x/recipes/reservation_gcs_bucket_recipe.md)
    * [Run training workload with Ironwood (TPU7x) with flex-start using Filestore storage](https://github.com/AI-Hypercomputer/xpk/blob/main/docs/usage/tpu7x/recipes/flex_filestore_recipe.md)
    * [Run training workload with Ironwood (TPU7x) and flex-start using Lustre storage](https://github.com/AI-Hypercomputer/xpk/blob/main/docs/usage/tpu7x/recipes/flex_lustre_recipe.md)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
