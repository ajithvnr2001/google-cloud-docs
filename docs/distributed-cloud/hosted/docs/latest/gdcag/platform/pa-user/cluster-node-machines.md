---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines/
title: Cluster node machine types \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:43:58.951747+00:00
---

# Cluster node machine types  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-node-machines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Cluster node machine types Stay organized with collections  Save and categorize content based on your preferences. 

[ Shared ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#shared-cluster) [ Standard ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cluster-configs#standard-cluster)

When you create a Kubernetes cluster in Google Distributed Cloud (GDC) air-gapped, you create node pools that are responsible for running your container workloads in the cluster. You provision nodes based on your container workload requirements, and can update them as your requirements evolve.

GDC provides predefined machine types for your worker nodes that are selectable when you [add a node pool](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-node-pools#add-a-node-pool). There are also multiple ways to partition separate GPU instances using the Multi-Instance GPU (MIG) feature.

This document is for application developers within the application operator group and IT administrators within the platform administrator group who are responsible for managing Kubernetes clusters within their organization. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

Reference the following sections for available machine types and GPU support.

## Available machine types

GDC defines machine types with some parameters for a Kubernetes cluster node, which include CPU, memory, and GPU. GDC has various machine types for different purposes. For example, clusters use `n2-standard-4-gdc` for general purpose container workloads. If you plan to run artificial intelligence (AI) and machine learning (ML) notebooks, you must provision GPU machines, such as `a2-highgpu-1g-gdc`.

The following is a list of all GDC predefined machine types available for Kubernetes cluster worker nodes:

Name | vCPUs | Memory | GPU  
---|---|---|---  
n2-standard-4-gdc | 4 | 16G | N/A  
n2-standard-8-gdc | 8 | 32G | N/A  
n2-standard-16-gdc | 16 | 64G | N/A  
n2-standard-32-gdc | 32 | 128G | N/A  
n2-highmem-4-gdc | 4 | 32G | N/A  
n2-highmem-8-gdc | 8 | 64G | N/A  
n2-highmem-16-gdc | 16 | 128G | N/A  
n2-highmem-32-gdc | 32 | 256G | N/A  
n2-highcpu-8-gdc | 8 | 8G | N/A  
n3-standard-4-gdc | 4 | 16G | N/A  
n3-standard-8-gdc | 8 | 32G | N/A  
n3-standard-16-gdc | 16 | 64G | N/A  
n3-standard-32-gdc | 32 | 128G | N/A  
n3-standard-64-gdc | 64 | 256G | N/A  
n3-standard-80-gdc | 80 | 320G | N/A  
n4-highmem-4-gdc | 4 | 32G | N/A  
n4-highmem-8-gdc | 8 | 64G | N/A  
n4-highmem-16-gdc | 16 | 128G | N/A  
n4-highmem-32-gdc | 32 | 256G | N/A  
n4-highmem-48-gdc | 48 | 384G | N/A  
n4-highmem-64-gdc | 64 | 512G | N/A  
n4-highmem-80-gdc | 80 | 640G | N/A  
n4-megamem-64-gdc | 64 | 896G | N/A  
a2-highgpu-1g-gdc | 12 | 85G | 1x A100 40GB  
a2-ultragpu-1g-gdc | 12 | 170G | 1x A100 80GB  
a2-ultragpu-2g-gdc | 24 | 340G | 2x A100 80GB  
a3-highgpu-1g-gdc  | 28 | 240G | 1x H100 94GB  
a3-highgpu-2g-gdc  | 56 | 480G | 2x H100 94GB  
a3-highgpu-4g-gdc | 112 | 960G | 4x H100 94GB  
a3-ultragpu-8g-gdc | 224 | 1792G | 8x H200 141GB  
a4-ultragpu-8g-gdc | 224 | 3584G | 8x B300  
**Preview:** The following machine types are in Preview: 

  * a3-highgpu-1g-gdc
  * a3-highgpu-2g-gdc

For more information on Preview features, see [Feature stages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/feature-stages#preview). 

## Supported MIG profiles

This section defines the supported partitioning schemes of MIG profiles on supported GPUs. You can define a partitioning scheme for a node pool in your `Cluster` custom resource.

**Important:** A partitioning scheme gets applied to all GPUs in a node. For example, the `a3-highgpu-4g-gdc` machine can support four iterations of the `7x 1g.12gb` GPU slicing because there are four GPUs available to the machine type.

For more information on how to apply a GPU partitioning scheme, see [Add a node pool](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-node-pools#add-a-node-pool).

### A100 40GB GPU

The following table defines the MIG profiles supported on the A100 40GB NVIDIA GPU:

Partitioning Scheme | Available Partitions  
---|---  
1g.5gb  | 7x 1g.5gb   
2g.10gb  | 3x 2g.10gb   
3g.20gb  | 2x 3g.20gb   
7g.40gb  | 1x 7g.40gb   
mixed-1  | 1x 4g.20gb  
1x 2g.10gb  
1x 1g.5gb  
mixed-2  | 1x 4g.20gb  
3x 1g.5gb  
mixed-3  | 1x 3g.20gb  
2x 2g.10gb  
mixed-4  | 1x 3g.20gb  
1x 2g.10gb  
2x 1g.5gb  
mixed-5  | 1x 3g.20gb  
4x 1g.5gb  
mixed-6  | 3x 2g.10gb  
1x 1g.5gb  
mixed-7  | 2x 2g.10gb  
3x 1g.5gb  
mixed-8  | 1x 2g.10gb  
5x 1g.5gb  
  
### A100 80GB GPU

The following table defines the MIG profiles supported on the A100 80GB NVIDIA GPU:

Partitioning Scheme | Available Partitions  
---|---  
1g.10gb  | 7x 1g.10gb   
2g.20gb  | 3x 2g.20gb   
3g.40gb  | 2x 3g.40gb   
7g.80gb  | 1x 7g.80gb   
mixed-1  | 1x 4g.40gb  
1x 2g.20gb  
1x 1g.10gb  
mixed-2  | 1x 4g.40gb  
3x 1g.10gb  
mixed-3  | 1x 3g.40gb  
2x 2g.20gb  
mixed-4  | 1x 3g.40gb  
1x 2g.20gb  
2x 1g.10gb  
mixed-5  | 1x 3g.40gb  
4x 1g.10gb  
mixed-6  | 3x 2g.20gb  
1x 1g.10gb  
mixed-7  | 2x 2g.20gb  
3x 1g.10gb  
mixed-8  | 1x 2g.20gb  
5x 1g.10gb  
  
### H100 94GB GPU

The following table defines the MIG profiles supported on the H100 94GB NVIDIA GPU:

Partitioning Scheme | Available Partitions  
---|---  
1g.12gb  | 7x 1g.12gb   
1g.24gb  | 7x 1g.24gb   
2g.24gb  | 3x 2g.24gb   
3g.47gb  | 2x 3g.47gb   
4g.47gb  | 1x 4g.47gb   
7g.94gb  | 1x 7g.94gb   
mixed-1  | 1x 4g.47gb  
1x 3g.47gb  
mixed-2  | 1x 4g.47gb  
1x 2g.24gb  
1x 1g.12gb  
mixed-3  | 1x 4g.47gb  
3x 1g.12gb  
mixed-4  | 1x 3g.47gb  
2x 2g.24gb  
mixed-5  | 1x 3g.47gb  
1x 2g.24gb  
2x 1g.12gb  
mixed-6  | 1x 3g.47gb  
4x 1g.12gb  
mixed-7  | 3x 2g.24gb  
1x 1g.12gb  
mixed-8  | 2x 2g.24gb  
3x 1g.12gb  
mixed-9  | 1x 2g.24gb  
5x 1g.12gb  
  
### H200 141GB GPU

The following table defines the MIG profiles supported on the H200 141GB NVIDIA GPU:

Partitioning Scheme | Available Partitions  
---|---  
1g.18gb  | 7x 1g.18gb   
1g.35gb  | 4x 1g.35gb   
2g.35gb  | 3x 2g.35gb   
3g.71gb  | 2x 3g.71gb   
4g.71gb  | 1x 4g.71gb   
7g.141gb  | 1x 7g.141gb   
mixed-1  | 1x 4g.71gb  
1x 3g.71gb  
mixed-2  | 1x 4g.71gb  
1x 2g.35gb  
1x 1g.18gb  
mixed-3  | 1x 4g.71gb  
3x 1g.18gb  
mixed-4  | 1x 3g.71gb  
2x 2g.35gb  
mixed-5  | 1x 3g.71gb  
1x 2g.35gb  
2x 1g.18gb  
mixed-6  | 1x 3g.71gb  
4x 1g.18gb  
mixed-7  | 3x 2g.35gb  
1x 1g.18gb  
mixed-8  | 2x 2g.35gb  
3x 1g.18gb  
mixed-9  | 1x 2g.35gb  
5x 1g.18gb  
  
### B300 GPU

The following table defines the MIG profiles supported on the B300 NVIDIA GPU:

Partitioning Scheme | Available Partitions  
---|---  
1g.34gb  | 7x 1g.34gb   
1g.67gb  | 4x 1g.67gb   
2g.67gb  | 3x 2g.67gb   
3g.135gb  | 2x 3g.135gb   
4g.135gb  | 1x 4g.135gb   
7g.269gb  | 1x 7g.269gb   
mixed-1  | 1x 4g.135gb  
1x 3g.135gb  
mixed-2  | 1x 4g.135gb  
1x 2g.67gb  
1x 1g.34gb  
mixed-3  | 1x 4g.135gb  
3x 1g.34gb  
mixed-4  | 1x 3g.135gb  
2x 2g.67gb  
mixed-5  | 1x 3g.135gb  
1x 2g.67gb  
2x 1g.34gb  
mixed-6  | 1x 3g.135gb  
4x 1g.34gb  
mixed-7  | 3x 2g.67gb  
1x 1g.34gb  
mixed-8  | 2x 2g.67gb  
3x 1g.34gb  
mixed-9  | 1x 2g.67gb  
5x 1g.34gb  
  
## What's next

  * [Create a shared cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-user-cluster)
  * [Create a standard cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/create-standard-cluster)
  * [Maintain Kubernetes clusters](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster)
  * [Manage node pools](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/manage-node-pools)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
