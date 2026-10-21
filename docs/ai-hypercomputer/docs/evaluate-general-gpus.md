---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus/
title: General GPUs overview \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:51.879267+00:00
---

# General GPUs overview  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  General GPUs overview Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus)

General GPUs are optimized for artificial intelligence (AI) and machine learning (ML) workloads that prioritize operational flexibility, resource independence, and cost-effectiveness.

General GPUs let teams deploy and scale NVIDIA accelerators with complete operational autonomy, bypassing the architectural complexity of coordinated supercomputing clusters. They are ideal for workloads that prioritize high availability, self-service provisioning, and independent scaling. Common use cases include real-time inference, RAG, prototyping, and small-to-medium model training.

## Key characteristics of General GPUs

  * **Operational flexibility** : you can manage resources by using standard GKE (Autopilot and Standard) and Compute Engine interfaces to simplify deployment and scaling.
  * **High availability** : Google Cloud updates individual instances independently to help ensure updates on one node don't impact the availability of others, allowing your load balancer to redirect traffic without stalling serving fleets.
  * **Networking simplicity** : your workloads use standard Virtual Private Cloud (VPC) services and standard TCP/IP over Google Virtual NIC (gVNIC) interfaces to eliminate complex hardware-level fabrics.
  * **Cost optimization** : you can use Spot VMs for fault-tolerant research to achieve cost savings of up to 90% compared to standard on-demand rates.
  * **Self-service acquisition** : you can obtain capacity directly through standard reservations and on-demand requests without requiring account-team-managed workflows.



## General GPU families and technical specifications

Review the workloads and hardware specifications for the General GPU machine series. For high-throughput serving, use the A3 Edge series.

### A3 series (High with 1, 2, or 4 GPUs and Edge)

#### A3 High (1, 2, or 4 GPUs)

If you are running inference or standard training workloads that require high performance but don't need a full 8-GPU synchronized cluster, use the A3 High machine series with 1, 2, or 4 GPUs attached.

[A3 High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms) machine types have [NVIDIA H100 SXM GPUs](https://www.nvidia.com/en-us/data-center/h100/) and are well-suited for both large model inference and model fine tuning. **Note:** When provisioning `a3-highgpu-1g`, `a3-highgpu-2g`, or `a3-highgpu-4g` machine types, you must create instances by using Spot VMs or Flex-start VMs. For detailed instructions on these options, review the following: 

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

#### A3 Edge

If you are running high-throughput distributed inference workloads across multiple hosts without a coordinated cluster fabric, use the A3 Edge series to simplify deployment over standard virtual private networks.

[A3 Edge](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms) machine types have [NVIDIA H100 SXM GPUs](https://www.nvidia.com/en-us/data-center/h100/) and are designed specifically for serving and are available in a [limited set of regions](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table). **Note:** To get started with A3 Edge instances, see [Create an A3 VM with GPUDirect-TCPX enabled](https://docs.cloud.google.com/compute/docs/gpus/gpudirect). 

| Attached NVIDIA H100 GPUs  
---|---  
Machine type | vCPU count1 | Instance memory (GB) | Attached Local SSD (GiB) | Physical NIC count | Maximum network bandwidth (Gbps)2 | GPU count | GPU memory3  
(GB HBM3)  
`a3-edgegpu-8g` | 208 | 1,872 | 6,000 | 5 | 

  * 600: _for asia-south1 and northamerica-northeast2_
  * 400: _for all other[A3 Edge regions](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones#view-using-table)_

| 8 | 640  
  
### A2 series (Standard and Ultra)

If you need to perform high-performance single-node model serving or small-scale model fine-tuning, use the A2 machine series to access dedicated NVIDIA A100 GPU resources.

#### A2 Ultra

| Attached NVIDIA A100 80GB GPUs  
---|---  
Machine type | vCPU count1 | Instance memory (GB) | Attached Local SSD (GiB) | Maximum network bandwidth (Gbps)2 | GPU count | GPU memory3  
(GB HBM2e)  
`a2-ultragpu-1g` | 12 | 170 | 375 | 24 | 1 | 80  
`a2-ultragpu-2g` | 24 | 340 | 750 | 32 | 2 | 160  
`a2-ultragpu-4g` | 48 | 680 | 1,500 | 50 | 4 | 320  
`a2-ultragpu-8g` | 96 | 1,360 | 3,000 | 100 | 8 | 640  
  
1A vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads. 

#### A2 Standard

| Attached NVIDIA A100 40GB GPUs  
---|---  
Machine type | vCPU count1 | Instance memory (GB) | Local SSD supported | Maximum network bandwidth (Gbps)2 | GPU count | GPU memory3  
(GB HBM2)  
`a2-highgpu-1g` | 12 | 85 | Yes | 24 | 1 | 40  
`a2-highgpu-2g` | 24 | 170 | Yes | 32 | 2 | 80  
`a2-highgpu-4g` | 48 | 340 | Yes | 50 | 4 | 160  
`a2-highgpu-8g` | 96 | 680 | Yes | 100 | 8 | 320  
`a2-megagpu-16g` | 96 | 1,360 | Yes | 100 | 16 | 640  
  
1A vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads. 

### G4 series

If your team requires cost-effective entry-level inference or standard graphics rendering workloads, use the G4 machine series featuring NVIDIA RTX PRO 6000 GPUs.

G4 machine types use [ NVIDIA RTX PRO 6000 Blackwell Server Edition GPUs](https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/) (`nvidia-rtx-pro-6000`) and are suitable for NVIDIA Omniverse simulation workloads, graphics-intensive applications, video transcoding, and virtual desktops. G4 machine types also provide a low-cost solution for performing single host inference and model tuning compared with A series machine types. 

**Note:** To get started with G4 instances, see [Create a G4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-g-series).  | Attached NVIDIA RTX PRO 6000 GPUs  
---|---  
Machine type | vCPU count1 | Instance memory (GB) | Maximum Titanium SSD supported (GiB)2 | Physical NIC count | Maximum network bandwidth (Gbps)3 | GPU count | GPU memory4  
(GB GDDR7)  
`g4-standard-6` | 6 | 22 | 0 | 1 | 20 | 1/8 | 12  
`g4-standard-12` | 12 | 45 | 375 | 1 | 20 | 1/4 | 24  
`g4-standard-24` | 24 | 90 | 750 | 1 | 20 | 1/2 | 48  
`g4-standard-48` | 48 | 180 | 1,500 | 1 | 50 | 1 | 96  
`g4-standard-96` | 96 | 360 | 3,000 | 1 | 100 | 2 | 192  
`g4-standard-192` | 192 | 720 | 6,000 | 1 | 200 | 4 | 384  
`g4-standard-384` | 384 | 1,440 | 12,000 | 2 | 400 | 8 | 768  
  
*GPU memory is the memory available on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your accelerated workloads such as machine learning and graphics-intensive workloads. 

### G2 series

If you are deploying mainstream real-time inference applications or Retrieval-Augmented Generation (RAG) pipelines, use the G2 machine series to balance performance and cost efficiency with NVIDIA L4 GPUs.

| Attached NVIDIA L4 GPUs  
---|---  
Machine type | vCPU count1 | Default instance memory (GB) | Custom instance memory range (GB) | Max Local SSD supported (GiB) | Maximum network bandwidth (Gbps)2 | GPU count | GPU memory3 (GB GDDR6)  
`g2-standard-4` | 4 | 16 | 16 to 32 | 375 | 10 | 1 | 24  
`g2-standard-8` | 8 | 32 | 32 to 54 | 375 | 16 | 1 | 24  
`g2-standard-12` | 12 | 48 | 48 to 54 | 375 | 16 | 1 | 24  
`g2-standard-16` | 16 | 64 | 54 to 64 | 375 | 32 | 1 | 24  
`g2-standard-24` | 24 | 96 | 96 to 108 | 750 | 32 | 2 | 48  
`g2-standard-32` | 32 | 128 | 96 to 128 | 375 | 32 | 1 | 24  
`g2-standard-48` | 48 | 192 | 192 to 216 | 1,500 | 50 | 4 | 96  
`g2-standard-96` | 96 | 384 | 384 to 432 | 3,000 | 100 | 8 | 192  
  
1A vCPU is implemented as a single hardware hyper-thread on one of the available [CPU platforms](https://docs.cloud.google.com/compute/docs/cpu-platforms).  
2Maximum egress bandwidth cannot exceed the number given. Actual egress bandwidth depends on the destination IP address and other factors. For more information about network bandwidth, see [Network bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth).  
3GPU memory is the memory on a GPU device that can be used for temporary storage of data. It is separate from the instance's memory and is specifically designed to handle the higher bandwidth demands of your graphics-intensive workloads. 

### N1 series (NVIDIA T4 or V100)

If your priority is cost-sensitive experimentation or running low-concurrency, entry-level inference, use the N1 machine series to attach NVIDIA T4 or V100 GPUs.

#### NVIDIA T4

**Caution:** NVIDIA T4 GPUs reach end of support on August 1, 2027. For more information, see [NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos). Accelerator type | GPU count | GPU memory1 (GB GDDR6) | vCPU count | Instance memory (GB) | Local SSD supported  
---|---|---|---|---|---  
`nvidia-tesla-t4` or   
`nvidia-tesla-t4-vws` | 1 | 16 | 1 to 48 | 1 to 312 | Yes  
2 | 32 | 1 to 48 | 1 to 312 | Yes  
4 | 64 | 1 to 96 | 1 to 624 | Yes  
  
#### NVIDIA V100

Accelerator type | GPU count | GPU memory1 (GB HBM2) | vCPU count | Instance memory (GB) | Local SSD supported2  
---|---|---|---|---|---  
`nvidia-tesla-v100` | 1 | 16 | 1 to 12 | 1 to 78 | Yes  
2 | 32 | 1 to 24 | 1 to 156 | Yes  
4 | 64 | 1 to 48 | 1 to 312 | Yes  
8 | 128 | 1 to 96 | 1 to 624 | Yes  
  
## Capacity acquisition

General GPU accelerators use standard, self-service provisioning. You can obtain capacity through standard reservations, on-demand requests, or Spot VMs. Because on-demand capacity can experience stockouts, use Spot VMs or Flex-start where possible.

## What's next

  * To learn how to acquire capacity, see [Consumption options](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  * To evaluate your infrastructure requirements, see [Choose an infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-infrastructure).
  * To review the network services for GPUs, see [GPU networking overview](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-overview).
  * To review the process and choices to make when you start a cluster, see [Plan and create your AI infrastructure](https://docs.cloud.google.com/ai-hypercomputer/docs/process-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
