---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/terminology/
title: Terminology \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:47.575346+00:00
---

# Terminology  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/terminology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Terminology Stay organized with collections  Save and categorize content based on your preferences. 

The following terms apply to AI Hypercomputer. 

Acceleratorlink
    A specialized hardware device, such as a GPU or TPU, designed to perform specific tasks, such as machine learning workloads, more efficiently than a general-purpose processor.

Blocklink
    A collection of sub-blocks interconnected by a non-blocking, high-speed network that provides high bandwidth for all host machines in the block.

Clusterlink
    A collection of blocks interconnected by a high-speed network fabric. Each cluster is globally unique. For A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) machines, a cluster provides a common, non-blocking network fabric for your blocks of accelerator capacity. Within a cluster, inter-node communication ([east-west traffic](https://en.wikipedia.org/wiki/East%E2%80%93west_traffic)) is non-blocking for the entire collection of blocks.

Clustered GPUlink
    A category of machine families for GPUs, including A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs). Clustered GPUs let teams deploy and scale thousands of interconnected accelerators as a single, tightly coupled system by using specialized networking fabrics and synchronized maintenance. They are ideal for workloads that require extreme compute, memory, and high-speed networking synchronization. Common use cases include pre-training foundation models with trillions of parameters, frontier model serving, and simulations for drug discovery.

Emergent maintenancelink
    Sometimes referred to as _emergency maintenance_. An unplanned maintenance event caused by a critical hardware, software, or security issue. For supported accelerator machine types, emergent maintenance provides an advance notification instead of an immediate disruption. This notification gives you time to gracefully drain your workloads and optionally trigger the repair before the system terminates the VMs.

General GPUlink
    A category of GPU machine families, including G2, G4, A2, N1+T4, and A3 Edge. General GPUs let teams deploy and scale NVIDIA accelerators with complete operational autonomy, bypassing the architectural complexity of coordinated supercomputing clusters. They are ideal for workloads that prioritize high availability, self-service provisioning, and independent scaling. Common use cases include real-time inference, RAG, prototyping, and small-to-medium model training.

Network fabriclink
    High-speed network infrastructure that provides high bandwidth and low latency across all blocks and Google Cloud services in a cluster. The fabric uses the architecture of the [Jupiter](https://cloud.google.com/blog/topics/systems/the-evolution-of-googles-jupiter-data-center-network) network. To optimize performance, the fabric uses software-defined network and optical switches. 

Node or hostlink
    A single physical server machine in the data center. Each host has associated compute resources, such as accelerators. The number and configuration of these compute resources depend on the machine family. Compute Engine instances are provisioned on top of a physical host.

NVLink domainlink
    An NVLink domain, also referred to as a sub-block, is the core unit of capacity for A4X Max and A4X machines. An NVLink domain consists of 18 A4X Max or A4X instances (72 GPUs) that are connected by a multi-node NVLink system.

Sub-blocklink
    A group of hosts and associated connectivity hardware that are on a single physical block. In the context of A4X Max and A4X machines, a sub-block is also referred to as an NVLink domain.

Superblocklink
    A physical grouping of interconnected machines within data centers. By placing machines inside a superblock, you achieve the extreme network throughput and sub-millisecond latency required to execute tightly coupled training workloads.

## More information

The following documents provide further explanations of the terminologies that are relevant to the corresponding topics:

  * [GPU network architecture](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-overview#rail-aligned-network-architecture)
  * [A4X fundamentals of topology](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a4x#a4x_fundamentals)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
