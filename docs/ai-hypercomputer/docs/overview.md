---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/overview/
title: AI Hypercomputer overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:47.832600+00:00
---

# AI Hypercomputer overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  AI Hypercomputer overview Stay organized with collections  Save and categorize content based on your preferences. 

AI Hypercomputer is an integrated supercomputing system that's optimized to support your artificial intelligence (AI) and machine learning (ML) workloads. It is the unified portfolio for Google Cloud's AI infrastructure, and provides a single entry point to explore, configure, and deploy performance-optimized hardware, open software, and flexible consumption models.

AI Hypercomputer incorporates systems-level design and best practices to boost efficiency across the entire AI development lifecycle—from prototyping and development to massive-scale training and real-time serving.

## System architecture

AI Hypercomputer vertically integrates these three components to maximize [goodput](https://cloud.google.com/blog/products/ai-machine-learning/goodput-metric-as-measure-of-ml-productivity)—the measure of actual machine learning productivity:

  * **Performance-optimized infrastructure** : provides accelerators (NVIDIA GPUs and Google Cloud TPUs), networking, and storage resources. 
    * **GPUs** : categorized by how the system handles their lifecycle events and maintenance: 
      * **General GPUs** : infrastructure managed as independent compute units with asynchronous maintenance.
      * **Clustered GPUs** : high-performance clusters managed as a single tightly coupled system with synchronized maintenance.
    * **TPUs** : use hardware designed for performing large matrix operations and have on-chip high-bandwidth memory (HBM) for larger models and batch sizes. TPUs can be connected in groups called _slices_ that scale up your workloads with little to no code changes. For information about TPU infrastructure, see the [Cloud TPUs documentation](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).
  * **Open software** : offers optimized versions of machine learning frameworks (PyTorch, JAX, and TensorFlow) and orchestration platforms. To deploy and manage your accelerators, you can choose from the following options: 
    * Google Kubernetes Engine for automated container-native scaling
    * Slurm through Cluster Director
    * Cluster Toolkit blueprints
  * **Consumption options** : offers flexible provisioning options based on your workload needs: 
    * **Flex-start VMs** , **Spot VMs** , and **Reservations** : provide flexible options for different workloads.
    * **[Dynamic Workload Scheduler](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler)** : provides atomic provisioning for entire blocks of interconnected nodes for large-scale training.



## Benefits

  * **High performance and goodput** : optimize the scheduling and runtime layers to maximize goodput, helping accelerators spend more time on productive computation and less time on system overhead.
  * **Integrated reliability** : gain access to specialized reliability features: 
    * **Clustered GPUs** : includes automated hardware health monitoring and proactive node replacement.
    * **General GPUs** : uses standard Google Cloud node auto-repair to maintain pod-level uptime for serving fleets.
  * **Optimized storage** : use high-throughput storage services, such as Google Cloud Managed Lustre and Cloud Storage Rapid, to eliminate I/O bottlenecks.



## Use cases

AI Hypercomputer meets the needs of these use cases:

Use case | Example workloads  
---|---  
Large-scale AI and ML workloads | 

  * Distributed training for generative AI
  * Inference for generative AI
  * Fraud detection
  * Recommendation models

  
Inference and model serving | 

  * Fraud detection in real time
  * Recommendation engines for results in real time

  
Prototyping and development | 

  * Small-scale experiments
  * Early-stage development

  
  
## What's next

  * Learn about the performance-optimized infrastructure of AI Hypercomputer: 
    * [About GPU accelerators](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus)
    * [Networking services](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-overview)
    * [Storage services](https://docs.cloud.google.com/ai-hypercomputer/docs/storage)
  * Review [consumption models](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  * Learn about [cluster management](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
