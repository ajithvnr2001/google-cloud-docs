---
url: https://docs.cloud.google.com/docs/compute-area/gpus/
title: Understand GPUs \u00a0|\u00a0 Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:40.213449+00:00
---

# Understand GPUs  |  Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/compute-area/gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Guides ](https://docs.cloud.google.com/docs/compute-area/overview)



Send feedback 

#  Understand GPUs Stay organized with collections  Save and categorize content based on your preferences. 

Graphics processing units (GPUs) are specialized hardware accelerators that are designed to process massively parallel workloads simultaneously. On Google Cloud, you can attach NVIDIA GPUs to Compute Engine instances and bare metal instances to accelerate demanding workloads, such as artificial intelligence (AI) and machine learning (ML) training, high performance computing (HPC), graphics rendering, and video transcoding.

This document provides an overview of GPUs in Google Cloud, including available GPU models, machine series mappings, performance characteristics, ideal use cases, and pricing considerations.

## What is a GPU?

A GPU is a massively parallel processor that was originally designed for computer graphics and has evolved into an essential computing engine for AI, ML, and scientific computing. Unlike central processing units (CPUs), which contain a few powerful cores optimized for sequential, single-threaded processing, GPUs consist of thousands of smaller, highly efficient cores designed to perform mathematical calculations concurrently across large datasets.

The key architectural components of a GPU system are as follows:

  * **CUDA cores** : general-purpose vector processing units that execute instructions across multiple parallel threads simultaneously by using a single instruction, multiple threads (SIMT) architecture. CUDA cores handle standard vector and floating-point computations (such as FP32 and FP64), as well as general graphics rendering and physical simulations.

  * **Tensor Cores** : specialized matrix multiply-accumulate (MMA) processing units that are designed to accelerate neural network calculations. Tensor Cores deliver exponential speedups for AI training and inference across specialized numeric precision formats, including FP4, FP8, INT8, TF32, and FP16/BF16.

  * **High-bandwidth memory** : dedicated on-device memory that delivers up to several terabytes per second (TBps) of bandwidth, such as High Bandwidth Memory (HBM) or Graphics Double Data Rate (GDDR). This high throughput keeps thousands of GPU cores supplied with data during intensive matrix operations.

  * **High-speed interconnects (NVLink and NVSwitch)** : high-bandwidth, low-latency interconnect technologies that connect multiple GPUs on the same server or across nodes. NVLink provides direct GPU-to-GPU communication that bypasses the slower PCIe bus, allowing clusters of GPUs to function as a single, coherent accelerator memory pool.

  * **Virtual workstation software (NVIDIA RTX vWS)** : enterprise software that provides virtualized graphics acceleration for remote visual workstations, computer-aided design (CAD), digital content creation, and 3D modeling.




## GPU models and machine series

Google Cloud offers NVIDIA GPUs across multiple generations to meet different workload and budget needs. On Compute Engine, GPUs are available either as pre-configured accelerator-optimized machine series (A and G series) or as attachable accelerators on general-purpose N1 machine series.

The following table summarizes the hardware specifications, machine series mappings, networking bandwidth, and storage capabilities of GPU models available on Compute Engine:

GPU model | Machine series | Architecture | GPU memory and bandwidth | GPUs per compute instance | Max network bandwidth | Local SSD | Interconnect | NVIDIA RTX Virtual Workstation (vWS) support  
---|---|---|---|---|---|---|---|---  
NVIDIA GB300 | [A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) | Blackwell Ultra | 279 GB HBM3e (8 TBps) | 4 (NVL72) | 3,600 Gbps | 12,000 GiB | NVLink Full Mesh (1,800 GBps) | No  
NVIDIA GB200 | [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) | Blackwell | 186 GB HBM3e (8 TBps) | 4 (NVL72) | 2,000 Gbps | 12,000 GiB | NVLink Full Mesh (1,800 GBps) | No  
NVIDIA B200 | [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) | Blackwell | 180 GB HBM3e (8 TBps) | 8 | 3,600 Gbps | 12,000 GiB | NVLink Full Mesh (1,800 GBps) | No  
NVIDIA H200 | [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) | Hopper | 141 GB HBM3e (4.8 TBps) | 8 | 3,600 Gbps | 12,000 GiB | NVLink Full Mesh (900 GBps) | No  
NVIDIA H100 | [A3 Mega, High, Edge](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) | Hopper | 80 GB HBM3 (3.35 TBps) | 1, 2, 4, 8 | Up to 1,000 Gbps | Up to 6,000 GiB | NVLink Full Mesh (900 GBps) | No  
NVIDIA A100 (80GB) | [A2 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms) | Ampere | 80 GB HBM2e (1.9 TBps) | 1, 2, 4, 8 | 100 Gbps | Up to 3,000 GiB | NVLink Full Mesh (600 GBps) | No  
NVIDIA A100 (40GB) | [A2 Standard](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms) | Ampere | 40 GB HBM2 (1.6 TBps) | 1, 2, 4, 8, 16 | 100 Gbps | Up to 3,000 GiB | NVLink Full Mesh (600 GBps) | No  
NVIDIA RTX PRO 6000 | [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) | Blackwell | 96 GB GDDR7 (1.597 TBps) | 1/8, 1/4, 1/2, 1, 2, 4, 8 | 200 Gbps | Up to 3,000 GiB | PCIe Gen 5 | Yes  
NVIDIA L4 | [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) | Ada Lovelace | 24 GB GDDR6 (300 GBps) | 1, 2, 4, 8 | 100 Gbps | Up to 3,000 GiB | PCIe Gen 4 | Yes  
NVIDIA V100 | [N1+V100](https://docs.cloud.google.com/compute/docs/gpus#v100-gpus) | Volta | 16 GB HBM2 (900 GBps) | 1, 2, 4, 8 | 100 Gbps | Supported | NVLink Ring (300 GBps) | No  
NVIDIA T4 (approaching [end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos)) | [N1+T4](https://docs.cloud.google.com/compute/docs/gpus#t4-gpus) | Turing | 16 GB GDDR6 (320 GBps) | 1, 2, 4 | 100 Gbps | Supported | PCIe Gen 3 | Yes  
NVIDIA P4 (approaching [end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos)) | [N1+P4](https://docs.cloud.google.com/compute/docs/gpus#p4-gpus) | Pascal | 8 GB GDDR5 (192 GBps) | 1, 2, 4 | 100 Gbps | Supported | PCIe Gen 3 | Yes  
  
## GPU performance characteristics

Choosing the right GPU model depends on the computational characteristics, memory requirements, precision formats, and scalability needs of your workload.

### Ideal use cases and workload requirements

GPUs accelerate diverse computational workloads across AI, visual computing, and scientific modeling. To understand the architectural requirements for each workload category, select one of the following tabs:

### AI/ML training

  * **Frontier foundation models and mixture-of-experts (MoE)** : pre-training large transformer models, multimodal architectures, and [mixture-of-experts (MoE)](https://en.wikipedia.org/wiki/Mixture_of_experts) networks requires high [Tensor Core](https://www.nvidia.com/en-us/data-center/tensor-cores/) throughput, large [High Bandwidth Memory (HBM)](https://en.wikipedia.org/wiki/High_Bandwidth_Memory) capacities (up to 279 GB per GPU), and ultra-high-speed [NVLink](https://www.nvidia.com/en-us/data-center/nvlink/) interconnect bandwidth (up to 1,800 GBps) to minimize multi-node synchronization latency. Recommended machine series:

    * [A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) (NVIDIA GB300)
    * [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) (NVIDIA GB200)
    * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) (NVIDIA B200)
    * [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) (NVIDIA H200)
    * [A3 Mega](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) (NVIDIA H100)

For more information, see [Recommendations for pre-training models](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy#pre-train) in the AI Hypercomputer documentation.

  * **Fine-tuning and moderate model training** : adapting existing foundation models by using techniques like [parameter-efficient fine-tuning (PEFT)](https://en.wikipedia.org/wiki/Fine-tuning_\(deep_learning\)) and [Low-Rank Adaptation (LoRA)](https://en.wikipedia.org/wiki/LoRA_\(machine_learning\)) requires sufficient GPU memory to hold model weights and gradients without requiring exascale multi-node clustering. Recommended machine series:

    * [A3 High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) (NVIDIA H100)
    * [A2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms) (NVIDIA A100)
    * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) (NVIDIA RTX PRO 6000)

For more information, see [Recommendations for fine-tuning models](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy#fine-tuning) in the AI Hypercomputer documentation.




### AI/ML inference

  * **Large model inference (more than 70 billion parameters)** : serving [large language models (LLMs)](https://en.wikipedia.org/wiki/Large_language_model) benefits from high [High Bandwidth Memory (HBM3e)](https://en.wikipedia.org/wiki/High_Bandwidth_Memory) capacity (141–186 GB per GPU) to fit model weights across fewer GPUs, reducing inter-chip communication overhead. Recommended machine series:

    * [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) (NVIDIA GB200)
    * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) (NVIDIA B200)
    * [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) (NVIDIA H200)
  * **High-throughput and real-time serving** : low-latency interactive queries, streaming responses, and image generation use hardware-accelerated quantized numeric formats, such as 8-bit floating-point (FP8), 8-bit integer (INT8), and 4-bit integer (INT4), to maximize request throughput per dollar. Recommended machine series:

    * [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) (NVIDIA L4)
    * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) (NVIDIA RTX PRO 6000)
    * [A3 Edge and High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) (NVIDIA H100)

For more information, see [Recommendations for serving inference](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy#inference) in the AI Hypercomputer documentation.




### Graphics and visual

  * **3D CAD, digital twins, and virtual workstations** : interactive 3D modeling, [computer-aided design (CAD)](https://en.wikipedia.org/wiki/Computer-aided_design), architectural rendering, and [digital twins](https://en.wikipedia.org/wiki/Digital_twin) (such as [NVIDIA Omniverse](https://www.nvidia.com/en-us/omniverse/)) use dedicated [ray tracing (RT) cores](https://en.wikipedia.org/wiki/Ray_tracing_\(graphics\)) and [NVIDIA RTX Virtual Workstations (vWS)](https://www.nvidia.com/en-us/design-visualization/virtual-workstation/) for remote visual workstations and fractional virtual GPUs (vGPUs). Recommended machine series:

    * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) (NVIDIA RTX PRO 6000)
    * [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) (NVIDIA L4)
  * **Video processing and transcoding** : live streaming pipelines, video transcoding, and media processing use dedicated hardware [NVIDIA Encoder (NVENC)](https://en.wikipedia.org/wiki/Nvidia_NVENC) and [NVIDIA Decoder (NVDEC)](https://en.wikipedia.org/wiki/Nvidia_NVDEC) video engines supporting [AV1](https://en.wikipedia.org/wiki/AV1), [High Efficiency Video Coding (HEVC)](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding), and [H.264](https://en.wikipedia.org/wiki/Advanced_Video_Coding) codecs. Recommended machine series:

    * [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) (NVIDIA L4)
    * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) (NVIDIA RTX PRO 6000)



### HPC and simulation

  * **Scientific simulation and modeling** : applications in [molecular dynamics](https://en.wikipedia.org/wiki/Molecular_dynamics) (such as [GROMACS](https://www.gromacs.org/) and [AMBER](https://ambermd.org/)), [computational fluid dynamics (CFD)](https://en.wikipedia.org/wiki/Computational_fluid_dynamics), quantum chemistry, astrophysics, and weather forecasting require high 64-bit double-precision (FP64) floating-point performance and high memory bandwidth. Recommended machine series:

    * [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) (NVIDIA GB200)
    * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) (NVIDIA B200)
    * [A3](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) (NVIDIA H100)
    * [A2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms) (NVIDIA A100)

For more information, see [Recommendations for HPC](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy#recommendations_for_hpc) in the AI Hypercomputer documentation.




### Workload considerations

GPUs aren't usually suitable for the following workloads:

  * **Sequential and single-threaded logic** : tasks dominated by sequential decision branches or serial execution pipelines perform better on CPUs with high single-core clock frequencies.
  * **Standard web applications and microservices** : general-purpose web servers, relational database management systems (RDBMS), and standard API backends without AI or graphics processing requirements don't benefit from GPU acceleration. These workloads are more cost-effectively hosted on general-purpose or compute-optimized CPU instances.
  * **Workloads optimized for XLA and graph-compiled frameworks** : if your deep learning models are built by using frameworks like JAX, PyTorch/XLA, or TensorFlow, then they can take advantage of compiler-driven graph optimizations (XLA). If your models also benefit from custom matrix systolic arrays and optical circuit switching, then consider evaluating alternative accelerator architectures designed for those specific execution paradigms.



## Pricing considerations

The following factors determine GPU pricing on Google Cloud:

  * The specific GPU model.

  * The number of attached GPUs.

  * Provisioned resources, such as vCPUs, system memory, and storage.

  * The consumption model that you select.




The following sections outline the available consumption models and discount options for GPUs in Google Cloud.

### Consumption and purchasing models

You can provision GPU instances by using several consumption options depending on your availability requirements and cost tolerance:

  * **On-demand** : standard pay-as-you-go (PAYG) pricing billed per second with no long-term commitment. On-demand instances offer complete lifecycle flexibility for development, testing, and variable production workloads.

  * **[Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)** : highly discounted compute instances (up to 60–91% off on-demand rates) that draw from surplus Google Cloud capacity. Because Google Cloud can stop or delete Spot VMs to reclaim capacity with a 30-second notice, these compute instances are ideal for fault-tolerant batch ML training, checkpointed batch jobs, and distributed data processing.

  * **[Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms)** : dynamic scheduling option powered by Dynamic Workload Scheduler (DWS) that provisions GPU resources within a specified period for fixed-duration workloads (up to 7 days) at discounted rates.

  * **Reservations** :

    * **[Reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview)** : you can reserve capacity for standard GPUs and immediately use the reserved capacity.
    * **[Future reservations](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview)** ([calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview) and [AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity)): you can request to reserve clustered GPU capacity for a future date and time. If Google Cloud approves your request, then you can start using the capacity at your specified time and retain exclusive access until the reservation ends.



### Discount options

  * **[Committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview)** : provide substantial discounts (up to 55% for 3-year commitments or 37% for 1-year commitments) in exchange for a commitment to maintain a continuous level of resource usage in a specific region. For accelerator-optimized machine types and attached GPUs, CUDs require purchasing [resource-based commitments attached to reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments).

  * **[Sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts)** : automatic discounts applied to N1 compute instances and attached GPUs when they run for more than 25% of a billing month. Accelerator-optimized machine series (A and G series) don't receive SUDs.




For detailed hourly and monthly pricing across all regions, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing) and the [VM instance pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#accelerator-optimized).

For a detailed feature matrix of consumption option availability across all accelerator machine types, see [Consumption option availability by machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#consumption_option_availability_by_machine_type).

## What's next

  * Explore [GPU machines in the accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines).
  * Learn how to [Create a VM with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).
  * Discover Google Cloud's supercomputing AI architecture in the [ AI Hypercomputer overview](https://docs.cloud.google.com/ai-hypercomputer/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
