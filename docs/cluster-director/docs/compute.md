---
url: https://docs.cloud.google.com/cluster-director/docs/compute/
title: Supported machine series for Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:11.094970+00:00
---

# Supported machine series for Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Supported machine series for Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the CPU-based machines and GPU-accelerated machines that are available in Cluster Director. You use these machines to deploy and manage the underlying infrastructure to run high performance computing (HPC), artificial intelligence (AI), or machine learning (ML) workloads.

## CPU-based machines

Cluster Director supports general-purpose machine series, which are primarily CPU-based and suitable for HPC workloads and cluster management roles, such as [_login nodes_](https://docs.cloud.google.com/cluster-director/docs/orchestration#architecture).

### C4A machine series

**Note:** You can use the C4A machine series for login nodes only.

Cluster Director supports the [C4A machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#c4a_series). This machine series runs on Arm-based Google Axion processors and delivers consistent performance for Arm-based workloads. You must pair login nodes that use the C4A machine series with compute nodes that use the A4X Max or A4X machine series.

The machine types in the C4A series differ by the amount of DDR5 memory per vCPU. These memory configurations are as follows:

  * **`standard`** : 4 GB of memory per vCPU

  * **`highmem`** : 8 GB of memory per vCPU

  * **`highcpu`** : 2 GB of memory per vCPU




Each family offers a range of machine sizes, from 1 to 72 vCPUs. You can't use machine types that have Local SSD disks attached (`-lssd`) or run on bare metal (`-metal`) for login nodes. The following table summarizes the C4A machine types that are available in Cluster Director:

### C4A standard

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`c4a-standard-1` | 1 | 4 | Up to 10 | N/A  
`c4a-standard-2` | 2 | 8 | Up to 10 | N/A  
`c4a-standard-4` | 4 | 16 | Up to 23 | N/A  
`c4a-standard-8` | 8 | 32 | Up to 23 | N/A  
`c4a-standard-16` | 16 | 64 | Up to 23 | N/A  
`c4a-standard-32` | 32 | 128 | Up to 23 | Up to 50  
`c4a-standard-48` | 48 | 192 | Up to 34 | Up to 50  
`c4a-standard-64` | 64 | 256 | Up to 45 | Up to 75  
`c4a-standard-72` | 72 | 288 | Up to 50 | Up to 100  
  
* A vCPU represents an entire physical core because simultaneous multithreading (SMT) isn't supported. For more information, see [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. 

### C4A high-mem

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`c4a-highmem-1` | 1 | 8 | Up to 10 | N/A  
`c4a-highmem-2` | 2 | 16 | Up to 10 | N/A  
`c4a-highmem-4` | 4 | 32 | Up to 23 | N/A  
`c4a-highmem-8` | 8 | 64 | Up to 23 | N/A  
`c4a-highmem-16` | 16 | 128 | Up to 23 | N/A  
`c4a-highmem-32` | 32 | 256 | Up to 23 | Up to 50  
`c4a-highmem-48` | 48 | 384 | Up to 34 | Up to 50  
`c4a-highmem-64` | 64 | 512 | Up to 45 | Up to 75  
`c4a-highmem-72` | 72 | 576 | Up to 50 | Up to 100  
  
* A vCPU represents an entire physical core because simultaneous multithreading (SMT) isn't supported. For more information, see [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. 

### C4A high-cpu

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`c4a-highcpu-1` | 1 | 2 | Up to 10 | N/A  
`c4a-highcpu-2` | 2 | 4 | Up to 10 | N/A  
`c4a-highcpu-4` | 4 | 8 | Up to 23 | N/A  
`c4a-highcpu-8` | 8 | 16 | Up to 23 | N/A  
`c4a-highcpu-16` | 16 | 32 | Up to 23 | N/A  
`c4a-highcpu-32` | 32 | 64 | Up to 23 | Up to 50  
`c4a-highcpu-48` | 48 | 96 | Up to 34 | Up to 50  
`c4a-highcpu-64` | 64 | 128 | Up to 45 | Up to 75  
`c4a-highcpu-72` | 72 | 144 | Up to 50 | Up to 100  
  
* A vCPU represents an entire physical core because simultaneous multithreading (SMT) isn't supported. For more information, see [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. 

### N2 machine series

Cluster Director supports the [N2 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2_series). This series offers a balance of price and performance suitable for a variety of workloads, such as CPU-bound computational tasks or general-purpose HPC workloads.

The machine types in the N2 series differ by the amount of memory per vCPU. These memory configurations are as follows:

  * **`standard`** : 4 GB of memory per vCPU

  * **`highmem`** : 8 GB of memory per vCPU

  * **`highcpu`** : 1 GB of memory per vCPU




Each family offers a range of machine sizes, from 2 to 128 vCPUs. The following table summarizes the N2 machine types that are available in Cluster Director:

### N2 standard

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`n2-standard-2` | 2 | 8 | Up to 10 | N/A  
`n2-standard-4` | 4 | 16 | Up to 10 | N/A  
`n2-standard-8` | 8 | 32 | Up to 16 | N/A  
`n2-standard-16` | 16 | 64 | Up to 32 | N/A  
`n2-standard-32` | 32 | 128 | Up to 32 | Up to 50  
`n2-standard-48` | 48 | 192 | Up to 32 | Up to 50  
`n2-standard-64` | 64 | 256 | Up to 32 | Up to 75  
`n2-standard-80` | 80 | 320 | Up to 32 | Up to 100  
`n2-standard-96` | 96 | 384 | Up to 32 | Up to 100  
`n2-standard-128` | 128 | 512 | Up to 32 | Up to 100  
  
* A vCPU is implemented as a single hardware thread, or logical core, on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

### N2 high-mem

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`n2-highmem-2` | 2 | 16 | Up to 10 | N/A  
`n2-highmem-4` | 4 | 32 | Up to 10 | N/A  
`n2-highmem-8` | 8 | 64 | Up to 16 | N/A  
`n2-highmem-16` | 16 | 128 | Up to 32 | N/A  
`n2-highmem-32` | 32 | 256 | Up to 32 | Up to 50  
`n2-highmem-48` | 48 | 384 | Up to 32 | Up to 50  
`n2-highmem-64` | 64 | 512 | Up to 32 | Up to 75  
`n2-highmem-80` | 80 | 640 | Up to 32 | Up to 100  
`n2-highmem-96` | 96 | 768 | Up to 32 | Up to 100  
`n2-highmem-128` | 128 | 864 | Up to 32 | Up to 100  
  
* A vCPU is implemented as a single hardware thread, or logical core, on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

### N2 high-cpu

Machine types | vCPUs* | Memory (GB) | Default egress bandwidth (Gbps)‡ | Tier_1 egress bandwidth (Gbps)#  
---|---|---|---|---  
`n2-highcpu-2` | 2 | 2 | Up to 10 | N/A  
`n2-highcpu-4` | 4 | 4 | Up to 10 | N/A  
`n2-highcpu-8` | 8 | 8 | Up to 16 | N/A  
`n2-highcpu-16` | 16 | 16 | Up to 32 | N/A  
`n2-highcpu-32` | 32 | 32 | Up to 32 | Up to 50  
`n2-highcpu-48` | 48 | 48 | Up to 32 | Up to 50  
`n2-highcpu-64` | 64 | 64 | Up to 32 | Up to 75  
`n2-highcpu-80` | 80 | 80 | Up to 32 | Up to 100  
`n2-highcpu-96` | 96 | 96 | Up to 32 | Up to 100  
  
* A vCPU is implemented as a single hardware thread, or logical core, on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
‡ Maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
# Supports [ high-bandwidth networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for larger machine types. For Windows OS images, the maximum network bandwidth is limited to 50 Gbps. 

## GPU-accelerated machines

Cluster Director supports a specific set of accelerator-optimized machine series designed for large-scale AI, ML, and HPC workloads.

GPU machine types are available only in specific regions and zones. To review availability, see [GPU locations](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones).

### A4X Max and A4X machine series

The [A4X Max and A4X machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) runs on an exascale platform based on [NVIDIA's rack-scale architecture](https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/) and is optimized for compute and memory-intensive, network-bound ML training and HPC workloads. A4X Max and A4X differ primarily in their GPU and networking components. A4X Max is available only as bare metal instances, which provide direct access to the host server's CPU and memory, without the Compute Engine hypervisor layer.

#### A4X Max machine types (bare metal)

[A4X Max accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) machine types use NVIDIA GB300 Grace Blackwell Ultra Superchips (`nvidia-gb300`) and are ideal for foundation model training and serving. A4X Max machine types are available as [bare metal instances](https://docs.cloud.google.com/compute/docs/instances/bare-metal-instances). 

A4X Max is an exascale platform based on [NVIDIA GB300 NVL72](https://www.nvidia.com/en-us/data-center/gb300-nvl72/). Each machine has two sockets with NVIDIA Grace CPUs with Arm Neoverse V2 cores. These CPUs are connected to four NVIDIA B300 Blackwell GPUs with fast chip-to-chip ([NVLink-C2C](https://www.nvidia.com/en-us/data-center/nvlink-c2c/)) communication. For information about machine type limitations, see [A4X Max and A4X limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-limitations). 

**Note:** When provisioning A4X Max instances, you must [reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity) to create instances and clusters. You can then create instances that use the features and services available from AI Hypercomputer. For more information, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview) in the AI Hypercomputer documentation. Machine type | vCPU count | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | NVIDIA GB300 GPU count | GPU memory (GB HBM3e)  
---|---|---|---|---|---|---|---  
`a4x-maxgpu-4g-metal` | 144 | 960 | 12,000 | 6 | 3,600 | 4 | 1,116  
  
The following notes apply to the preceding table:

  * **vCPU count** : a vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * **Maximum network bandwidth** : maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).
  * **GPU memory** : GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads.



#### A4X machine types

[A4X accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) machine types use NVIDIA GB200 Grace Blackwell Superchips (`nvidia-gb200`) and are ideal for foundation model training and serving. 

A4X is an exascale platform based on [NVIDIA GB200 NVL72](https://www.nvidia.com/en-us/data-center/gb200-nvl72/). Each machine has two sockets with NVIDIA Grace CPUs with Arm Neoverse V2 cores. These CPUs are connected to four NVIDIA B200 Blackwell GPUs with fast chip-to-chip ([NVLink-C2C](https://www.nvidia.com/en-us/data-center/nvlink-c2c/)) communication. For information about machine type limitations, see [A4X Max and A4X limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-limitations). 

**Note:** To use A4X machine types in your cluster, you must reserve capacity through your account team and use the reserved capacity to create VMs. For more information about the ways you can create A4X VMs in a cluster, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option). Machine type | vCPU count | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | NVIDIA GB200 GPU count | GPU memory (GB HBM3e)  
---|---|---|---|---|---|---|---  
`a4x-highgpu-4g` | 140 | 884 | 12,000 | 6 | 2,000 | 4 | 744  
  
The following notes apply to the preceding table:

  * **vCPU count** : a vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * **Maximum network bandwidth** : maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).
  * **GPU memory** : GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads.



### A4 machine series

[A4 accelerator-optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) machine types have [NVIDIA B200 Blackwell GPUs](https://www.nvidia.com/en-us/data-center/b200/) (`nvidia-b200`) attached and are ideal for foundation model training and serving. For information about machine type limitations, see [A4 limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-limitations). 

**Note:** To use A4 machine types in your cluster, you must reserve capacity to create VMs, create Spot VMs, or create Flex-start VMs. For more information about the ways you can create A4 VMs in a cluster, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option). Machine type | vCPU count | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | NVIDIA B200 Blackwell GPU count | GPU memory (GB HBM3e)  
---|---|---|---|---|---|---|---  
`a4-highgpu-8g` | 224 | 3,968 | 12,000 | 10 | 3,600 | 8 | 1,440  
  
The following notes apply to the preceding table:

  * **vCPU count** : a vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * **Maximum network bandwidth** : maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).
  * **GPU memory** : GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads.



### A3 machine series

The A3 machine series is powered by NVIDIA H100 or H200 SXM GPUs and is suitable for a wide range of large model training and inference workloads.

Cluster Director supports the A3 machine types that are described in the following sections.

#### A3 Ultra machine type

[A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) machine types have [NVIDIA H200 SXM GPUs](https://www.nvidia.com/en-us/data-center/h200/) (`nvidia-h200-141gb`) attached and provide the highest network performance in the A3 series. A3 Ultra machine types are ideal for foundation model training and serving. For information about machine type limitations, see [A3 Ultra limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-limitations). 

**Note:** To use A3 Ultra machine types in your cluster, you must reserve capacity to create VMs, create Spot VMs, or create Flex-start VMs. For more information about the ways to create A3 Ultra VMs in a cluster, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option). Machine type | vCPU count | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | NVIDIA H200 GPU count | GPU memory (GB HBM3e)  
---|---|---|---|---|---|---|---  
`a3-ultragpu-8g` | 224 | 2,952 | 12,000 | 10 | 3,600 | 8 | 1128  
  
The following notes apply to the preceding table:

  * **vCPU count** : a vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * **Maximum network bandwidth** : maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).
  * **GPU memory** : GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads.



#### A3 Mega machine type

[A3 Mega](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms) machine types have [NVIDIA H100 SXM GPUs](https://www.nvidia.com/en-us/data-center/h100/) and are ideal for large model training and multi-host inference. For information about machine type limitations, see [A3 Mega limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-limitations). **Note:** To use A3 Mega machine types in your cluster, you must reserve capacity to create VMs, create Spot VMs, or create Flex-start VMs. For more information about the ways to create A3 Mega VMs in a cluster, see [Choose a consumption option](https://docs.cloud.google.com/cluster-director/docs/choose-consumption-option). Machine type | vCPU count | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | NVIDIA H100 GPU count | GPU memory (GB HBM3)  
---|---|---|---|---|---|---|---  
`a3-megagpu-8g` | 208 | 1,872 | 6,000 | 9 | 1,800 | 8 | 640  
  
The following notes apply to the preceding table:

  * **vCPU count** : a vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * **Maximum network bandwidth** : maximum egress bandwidth can't exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).
  * **GPU memory** : GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads.



## What's next

  * [Supported OS images in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/os-images)

  * [Try out Cluster Director](https://docs.cloud.google.com/cluster-director/docs/create/quickstart)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
