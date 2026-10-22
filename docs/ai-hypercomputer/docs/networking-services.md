---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/networking-services/
title: Network services for deployments \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:35.105046+00:00
---

# Network services for deployments  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/networking-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Network services for deployments Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

The network services you configure depend on your chosen deployment option (VMs or clusters) and infrastructure.

This document is intended for architects, network engineers, and developers who want to understand the network services for their AI Hypercomputer deployments. This document assumes you have basic familiarity with cloud networking and distributed computing concepts. For more information about deployment options, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).

For detailed information about network architecture, protocols, and hardware topologies, see the [GPU networking overview](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-overview).

## Networking for AI-optimized GKE deployments with Cluster Toolkit

When you create an AI-optimized GKE cluster with Cluster Toolkit, the blueprint configures the network as follows:

  * The blueprint uses the default VPC network for the main GKE cluster.
  * It creates two additional VPCs: one for a second host Network Interface Card (NIC) and another for GPU-to-GPU remote direct memory access (RDMA) traffic.
  * The blueprint applies a pre-configured, Google-managed network profile to the VPC used for GPU traffic. This profile automatically configures the network for high-speed, low-latency RDMA performance.
  * The blueprint automatically creates eight dedicated subnets within the RDMA VPC, one for each RDMA NIC on an accelerator VM.
  * It configures firewall rules that allow all TCP, UDP, and ICMP traffic between nodes within the cluster.



## Networking for GKE deployments

The network configuration for GKE setups depends on your workload type and infrastructure:

  * For General GPUs or non-distributed workloads, create a GKE cluster without GPUDirect RDMA. This configuration uses a single VPC network for all communication.
  * For Clustered GPUs or distributed workloads, create a GKE cluster with GPUDirect RDMA enabled. This configuration uses a multi-VPC environment that separates general-purpose traffic from high-bandwidth GPU-to-GPU communication.



## Networking for Slurm cluster deployments

Use the Cluster Toolkit to deploy AI and ML workloads through customizable blueprints, such as for the A4 or A3 Ultra series.

The network components configured by the blueprint for Clustered GPU Slurm deployments are as follows:

  * The blueprint creates three distinct VPCs: a primary VPC for the Slurm control plane, a secondary VPC for general host-level traffic, and a dedicated high-performance VPC for GPU-to-GPU communication.
  * For the GPU data plane, the blueprint applies a pre-configured, Google-managed network profile optimized for RoCE.
  * The blueprint sets a dedicated IP address range required by the Filestore service, which provides the shared `/home` directory for the cluster.
  * It creates a temporary, isolated image-build VPC used only during the process of building the custom VM image for the cluster nodes.



## Networking for Compute Engine instances

You can use Compute Engine to create standalone VMs, bulk compute instances, and managed instance groups (MIGs). The specific network requirements depend on the infrastructure model of the machine type:

  * **Clustered GPUs** : these machine series (A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High with 8 GPUs) require a multi-VPC network configuration to separate general host-to-host traffic from high-bandwidth GPU-to-GPU communication.
  * **General GPUs** : these machine series (G2, G4, A2, and N1 with T4 or V100) use a single-VPC architecture over gVNIC interfaces for all communication. A3 Edge is an exception that requires four data VPCs and GPUDirect-TCPX.



For detailed information about the NICs and network configuration for your machine type, see [Networking and GPU machines](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth).

## What's next

  * To learn about the best practices for creating a secure and resilient networking environment, see [Networking best practices](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-best-practices).
  * To learn about the storage options in AI Hypercomputer, see [About storage services for AI and ML workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/storage).
  * To onboard to cluster deployment, see [Plan and create your AI infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/process-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
