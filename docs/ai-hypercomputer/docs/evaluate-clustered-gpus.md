---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus/
title: Clustered GPUs overview \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:51.942561+00:00
---

# Clustered GPUs overview  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Clustered GPUs overview Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

Clustered GPUs are optimized for artificial intelligence (AI) and machine learning (ML) workloads that prioritize massive-scale distributed training, multi-host inference, and complex high performance computing (HPC) tasks.

Clustered GPUs let teams deploy and scale thousands of interconnected accelerators as a single, tightly coupled system by using specialized networking fabrics and synchronized maintenance. They are ideal for workloads that require extreme compute, memory, and high-speed networking synchronization. Common use cases include pre-training foundation models with trillions of parameters, frontier model serving, and simulations for drug discovery.

## Key characteristics of Clustered GPUs

  * **Synchronized maintenance** : Google Cloud updates all nodes in the cluster simultaneously, preventing a single node restart from stalling a job.
  * **Automated health monitoring** : the system proactively identifies stragglers and monitors for hardware failures or silent data corruption.
  * **Proactive node replacement** : the system evicts and reschedules underperforming VMs on healthy machines from a spare pool.
  * **Rail-aligned topology** : a rail-aligned topology isolates GPU-to-GPU traffic from standard host communication to help ensure jitter-free performance for massive multi node coordination.
  * **Advanced protocols** : these machine series support high-bandwidth interconnects including GPUDirect RDMA (based on RoCE).



## Clustered GPU families and technical specifications

Review the workloads and hardware specifications for the premium Clustered GPU machine series in these tables. For exascale training, use the A4X or A3 Ultra series.

### A4X Max and A4X series

**Caution:** The [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to the A4X Max and A4X machine series.

If you are training massive exascale foundation models or running highly complex, bare-metal high performance computing (HPC) simulations, use the A4X Max or A4X machine series. These series feature NVIDIA GB300 Grace Blackwell Ultra Superchips to handle extreme computational and memory demands.

#### A4X Max (Bare metal)

A4X Max machine types use NVIDIA GB300 Grace Blackwell Ultra Superchips (`nvidia-gb300`) and are ideal for foundation model training and serving. A4X Max machine types are available as [bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances). 

A4X Max is an exascale platform based on [NVIDIA GB300 NVL72](https://www.nvidia.com/en-us/data-center/gb300-nvl72/). Each machine has two sockets with NVIDIA Grace CPUs with Arm Neoverse V2 cores. These CPUs are connected to four NVIDIA B300 Blackwell GPUs with fast chip-to-chip ([NVLink-C2C](https://www.nvidia.com/en-us/data-center/nvlink-c2c/)) communication. 

**Note:** When provisioning A4X Max instances, you must [reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) to create instances and clusters. You can then create instances that use the features and services available from AI Hypercomputer. For more information, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).  | Attached NVIDIA GB300 Grace Blackwell Ultra Superchips  
---|---  
Machine type | vCPU count1 | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps)2 | GPU count | GPU memory3  
(GB HBM3e)  
`a4x-maxgpu-4g-metal` | 144 | 960 | 12,000 | 6 | 3,600 | 4 | 1,116  
  
1A vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads. 

#### A4X

A4X machine types use NVIDIA GB200 Grace Blackwell Superchips (`nvidia-gb200`) and are ideal for foundation model training and serving. 

A4X is an exascale platform based on [NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/). Each machine has two sockets with NVIDIA Grace CPUs with Arm Neoverse V2 cores. These CPUs are connected to four NVIDIA B200 Blackwell GPUs with fast chip-to-chip ([NVLink-C2C](https://www.nvidia.com/en-us/data-center/nvlink-c2c/)) communication. 

**Note:** When provisioning A4X instances, you must [reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) to create instances and clusters. You can then create instances that use the features and services available from AI Hypercomputer. For more information, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).  | Attached NVIDIA GB200 Grace Blackwell Superchips  
---|---  
Machine type | vCPU count1 | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps)2 | GPU count | GPU memory3  
(GB HBM3e)  
`a4x-highgpu-4g` | 140 | 884 | 12,000 | 6 | 2,000 | 4 | 744  
  
1A vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads. 

### A4 series

If your goal is to train state-of-the-art foundation models requiring massive parallel processing scale, use the A4 machine series to optimize processing time and maximize hardware throughput.

A4 machine types have [NVIDIA B200 Blackwell GPUs](https://www.nvidia.com/en-us/data-center/b200/) (`nvidia-b200`) attached and are ideal for foundation model training and serving. 

**Note:** When provisioning A4 machine types, you must reserve capacity to create instances or clusters, use Spot VMs, use Flex-start VMs, or create a resize request in a MIG. For instructions on how to create A4 instances, see [Create VMs and clusters overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview). .  | Attached NVIDIA B200 Blackwell GPUs  
---|---  
Machine type | vCPU count1 | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps)2 | GPU count | GPU memory3  
(GB HBM3e)  
`a4-highgpu-8g` | 224 | 3,968 | 12,000 | 10 | 3,600 | 8 | 1,440  
  
1A vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads. 

### A3 series (Ultra, Mega, and High with 8 GPUs)

If you need to execute large-scale distributed training runs or serve frontier models across multiple hosts with large dataset tables, use the A3 machine series to minimize host-to-host network latency.

#### A3 Ultra

**Note:** When provisioning A3 Ultra machine types, you must reserve capacity to create instances or clusters, use Spot VMs, use Flex-start VMs, or create a resize request in a MIG. For more information about the parameters to set when creating an A3 Ultra instance, see [Create VMs and clusters overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).  | Attached NVIDIA H200 GPUs  
---|---  
Machine type | vCPU count1 | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps)2 | GPU count | GPU memory3  
(GB HBM3e)  
`a3-ultragpu-8g` | 224 | 2,952 | 12,000 | 10 | 3,600 | 8 | 1128  
  
#### A3 Mega

**Note:** When provisioning `a3-megagpu-8g` machine types, we recommend using a cluster of these instances and deploying with a scheduler such as Google Kubernetes Engine (GKE) or Slurm. For detailed instructions on either of these options, review the following: 

  * To create Google Kubernetes Engine cluster, see [Deploy an A3 Mega cluster with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx).
  * To create a Slurm cluster, see [Deploy an A3 Mega Slurm cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/deploy-a3-mega-cluster).

| Attached NVIDIA H100 GPUs  
---|---  
Machine type | vCPU count1 | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps)2 | GPU count | GPU memory3  
(GB HBM3)  
`a3-megagpu-8g` | 208 | 1,872 | 6,000 | 9 | 1,800 | 8 | 640  
  
#### A3 High

**Note:** When provisioning `a3-highgpu-1g`, `a3-highgpu-2g`, or `a3-highgpu-4g` machine types, you must create instances by using Spot VMs or Flex-start VMs. For detailed instructions on these options, review the following: 

  * To create Spot VMs, set the provisioning model to `SPOT` when you [create an accelerator-optimized VM](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized).
  * To create Flex-start VMs, you can use one of the following methods: 
    * Create a standalone VM and set the provisioning model to `FLEX_START` when you [create an accelerator-optimized VM](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized).
    * Create a resize request in a managed instance group (MIG). For instructions, see [Create a MIG with GPU VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms).

| Attached NVIDIA H100 GPUs  
---|---  
Machine type | vCPU count1 | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps)2 | GPU count | GPU memory3  
(GB HBM3)  
`a3-highgpu-1g` | 26 | 234 | 750 | 1 | 25 | 1 | 80  
`a3-highgpu-2g` | 52 | 468 | 1,500 | 1 | 50 | 2 | 160  
`a3-highgpu-4g` | 104 | 936 | 3,000 | 1 | 100 | 4 | 320  
`a3-highgpu-8g` | 208 | 1,872 | 6,000 | 5 | 1,000 | 8 | 640  
  
1A vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads. 

## Capacity acquisition

Acquiring compute capacity for Clustered GPUs requires coordination to manage the supply and demand of high-performance accelerators. Because these resources are physically located within specialized networking fabrics, you must request them through managed workflows.

You can reserve capacity through your account team or use future reservations and Dynamic Workload Scheduler.

## What's next

  * To learn how to acquire capacity, see [Consumption options](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  * To evaluate your infrastructure requirements, see [Choose an infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-infrastructure).
  * To plan your network topology, see [GPU networking requirements for clustered environments](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-overview).
  * To reserve compute resources, see [Reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
