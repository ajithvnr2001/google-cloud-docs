---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/choose-infrastructure/
title: Choose your accelerator infrastructure \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:13.657247+00:00
---

# Choose your accelerator infrastructure  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/choose-infrastructure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Choose your accelerator infrastructure Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

Use this document to identify the optimal accelerator infrastructure for your artificial intelligence (AI) and machine learning (ML) workloads based on your lifecycle stage, such as small-scale prototyping, real-time inference, and massive distributed training. AI Hypercomputer organizes accelerator offerings into two categories: [general GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) and [clustered GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus).

## GPU infrastructure

AI Hypercomputer offers two distinct categories of GPUs. Each category has a distinct management model that determines how the system handles lifecycle events, manages maintenance, and optimizes networking for your workload:

### General GPU management model

The general GPU management model is designed for workloads that prioritize resource independence and high availability. This model uses the standard Google Cloud management plane, providing a familiar experience for teams already using Compute Engine or GKE.

  * **Maintenance:** asynchronous. Individual instances are updated independently. In a multinode serving fleet, a maintenance event on one node doesn't impact the availability of others, allowing traffic to be redirected to healthy nodes without stalling the entire job.

  * **Primary use cases:** recommended for mainstream tasks like real-time inference, model serving, small-scale prototyping, and development environments where supercomputing scale is not required.




#### General GPU machine series

The following machine series are general GPUs:

  * A3 High with 1, 2, or 4 GPUs
  * A3 Edge
  * A2
  * G4
  * G2
  * N1+T4
  * N1+V100



For technical information about each of the general GPU machines, see [GPU machine types](https://docs.cloud.google.com/ai-hypercomputer/docs/gpu).

### Clustered GPU management model

The clustered GPU management model is a supercomputing-class environment engineered for large-scale distributed training. Resources are managed as a single, tightly coupled system by using a clustered GPU stack.

  * **Maintenance:** coordinated. This model coordinates maintenance events to support tightly coupled workloads. For distributed training, you can use synchronized maintenance, where updates are applied across all nodes simultaneously. This approach prevents node restarts from stalling jobs and maximizes _goodput_. This model also offers 90-day maintenance notifications.

  * **Primary use cases:** designed for training exascale foundation models with trillions of parameters or running complex high performance computing (HPC) simulations, such as drug discovery and protein folding.




#### Clustered GPU machine series

The following machine series are clustered GPUs:

  * A4X Max
  * A4X
  * A4
  * A3 Ultra
  * A3 Mega
  * A3 High with 8 GPUs



For technical information about each of the clustered GPU machines, see [GPU machine types](https://docs.cloud.google.com/ai-hypercomputer/docs/gpu).

### Capability matrix

Compare the technical and operational characteristics of the general GPU and clustered GPU management models:

Characteristic | General GPU management model | Clustered GPU management model  
---|---|---  
Primary use cases | Inference, model serving, prototyping, and development | Large-scale distributed training and HPC  
Maintenance | **Asynchronous:** Independent node updates allow traffic to be redirected without stalling jobs | **Coordinated:** Supports cluster-wide coordinated (synchronized) updates to keep nodes in sync and maximize goodput  
Target hardware | [A3 High (1, 2, or 4 GPUs)](https://docs.cloud.google.com/compute/docs/gpus#a3-vms), [A3 Edge](https://docs.cloud.google.com/compute/docs/gpus#a3-vms), [G4](https://docs.cloud.google.com/compute/docs/gpus#g4-vms), [G2](https://docs.cloud.google.com/compute/docs/gpus#g2-vms), [A2](https://docs.cloud.google.com/compute/docs/gpus#a2-vms), [N1+T4](https://docs.cloud.google.com/compute/docs/gpus#n1-vms), and [N1+V100](https://docs.cloud.google.com/compute/docs/gpus#n1-vms) | [A4X](https://docs.cloud.google.com/compute/docs/gpus#a4-vms), [A4](https://docs.cloud.google.com/compute/docs/gpus#a4-vms), [A3 Ultra](https://docs.cloud.google.com/compute/docs/gpus#a3-vms), [A3 Mega](https://docs.cloud.google.com/compute/docs/gpus#a3-vms), and [A3 High (8 GPUs)](https://docs.cloud.google.com/compute/docs/gpus#a3-vms)  
Networking | Standard VPC networking over gVNIC interfaces (with the exception of A3 Edge, which uses GPUDirect-TCPX over multiple VPCs) | Specialized low-latency fabrics (RDMA, RoCE, TCPX, or NVIDIA NVLink)  
Management stack | Standard Google Cloud plane (Compute Engine or GKE) | Specialized management stack (for example, Cluster Director)  
Reliability | Standard node auto-repair and pod-level uptime | Specialized Resource and Recovery suite  
  
## Decision matrix

Use this matrix to identify which hardware families align with your specific workload intent:

If your workload involves... | Recommended GPU infrastructure | Recommended machine series  
---|---|---  
Prototyping and development | General GPUs | [A3 High (1, 2, or 4 GPUs)](https://docs.cloud.google.com/compute/docs/gpus#a3-vms), [A3 Edge](https://docs.cloud.google.com/compute/docs/gpus#a3-vms),, [A2](https://docs.cloud.google.com/compute/docs/gpus#a2-vms), [G4](https://docs.cloud.google.com/compute/docs/gpus#g4-vms), [G2](https://docs.cloud.google.com/compute/docs/gpus#g2-vms), [N1+T4](https://docs.cloud.google.com/compute/docs/gpus#n1-vms), [N1+V100](https://docs.cloud.google.com/compute/docs/gpus#n1-vms)  
Real-time inference (< 100B parameters) | General GPUs | [A3 High (1, 2, or 4 GPUs)](https://docs.cloud.google.com/compute/docs/gpus#a3-vms), [A3 Edge](https://docs.cloud.google.com/compute/docs/gpus#a3-vms),, [A2](https://docs.cloud.google.com/compute/docs/gpus#a2-vms), [G4](https://docs.cloud.google.com/compute/docs/gpus#g4-vms), [G2](https://docs.cloud.google.com/compute/docs/gpus#g2-vms), [N1+T4](https://docs.cloud.google.com/compute/docs/gpus#n1-vms), [N1+V100](https://docs.cloud.google.com/compute/docs/gpus#n1-vms)  
Inference across multiple GPUs | Clustered GPUs | [A4](https://docs.cloud.google.com/compute/docs/gpus#a4-vms), [A3 Ultra](https://docs.cloud.google.com/compute/docs/gpus#a3-vms), [A3 Mega](https://docs.cloud.google.com/compute/docs/gpus#a3-vms), [A3 High (8 GPUs)](https://docs.cloud.google.com/compute/docs/gpus#a3-vms)  
Large-scale training and inference | Clustered GPUs | [A4](https://docs.cloud.google.com/compute/docs/gpus#a4-vms), [A3 Ultra](https://docs.cloud.google.com/compute/docs/gpus#a3-vms), [A3 Mega](https://docs.cloud.google.com/compute/docs/gpus#a3-vms), [A3 High (8 GPUs)](https://docs.cloud.google.com/compute/docs/gpus#a3-vms)  
Massive-scale training (> 500B parameters) and disaggregated inference | Clustered GPUs | [A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/gpu#a4x-max-machine), [A4X](https://docs.cloud.google.com/compute/docs/gpus#a4-vms), [A4](https://docs.cloud.google.com/compute/docs/gpus#a4-vms)  
  
For a detailed decision tree mapping model architectures directly to hardware, see [Choose an accelerator](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy).

After establishing these primary criteria, choose an orchestration platform. This choice depends on your team's preference for automated management or granular control over the operating system and drivers.

## What's next

  * To select an orchestrator and deployment option, see [Choose an orchestrator and deployment option](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-platform).
  * To deploy inference workloads or run large-scale training, see [AI Hypercomputer tutorials](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials).
  * To optimize your system efficiency, see [Goodput optimization recipes](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/goodput-recipes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
