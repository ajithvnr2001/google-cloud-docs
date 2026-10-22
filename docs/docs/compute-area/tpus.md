---
url: https://docs.cloud.google.com/docs/compute-area/tpus/
title: Understand TPUs \u00a0|\u00a0 Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:07.371152+00:00
---

# Understand TPUs  |  Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/compute-area/tpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Guides ](https://docs.cloud.google.com/docs/compute-area/overview)



Send feedback 

#  Understand TPUs Stay organized with collections  Save and categorize content based on your preferences. 

Tensor Processing Units (TPUs) are Google's custom-developed, application-specific integrated circuits (ASICs) designed to accelerate machine learning (ML) and artificial intelligence (AI) workloads. Whether you are training complex foundation models for weeks or running large-scale inference, TPUs offer scalable, specialized computing resources that are optimized for advanced AI frameworks.

This document describes the role of TPUs in Google Cloud, the technical specifications of each available TPU version, performance characteristics, pricing considerations, and how they map to Compute Engine machine series.

## What is a TPU?

A TPU is a custom-designed ASIC engineered to handle the demands of massive matrix operations central to ML algorithms.

The key architectural components of a TPU system include the following:

  * **TensorCore** : the processing unit of a TPU chip. Each TensorCore consists of one or more Matrix Multiply Units (MXUs) that use systolic array architecture to perform matrix multiplication with high efficiency, along with scalar and vector units for control flow and general computation.

  * **SparseCore** : specialized dataflow processors designed to accelerate sparse operations. SparseCores work alongside TensorCores to process large embedding tables efficiently, making them ideal for accelerating recommendation models and large-scale embeddings.

  * **High-bandwidth memory (HBM)** : large physical memory attached to the TPU chip that offers massive memory bandwidth. HBM enables the training and serving of larger models with larger batch sizes.

  * **TPU instance** : a Linux compute instance that runs on a TPU host and has direct access to the underlying TPU hardware, offering access to high-performance libraries, SSH connectivity, and runtime debug logs.

  * **TPU slices and Pods** : a TPU Pod is a large contiguous cluster of physically linked TPU chips. A TPU slice is a logical partition of a Pod (comprising one or more hosts connected using high-speed interconnects) allotted to run a single workload.

  * **XLA compiler** : the Accelerated Linear Algebra (XLA) compiler compiles machine learning graphs into optimized machine instructions that run on the TPU TensorCores.




## TPU versions and machine series

Compute Engine supports multiple generations and versions of TPUs. The following table provides key specifications for each supported TPU version:

TPU version | Machine series | Peak compute per chip (TFLOPs) | TPU memory and bandwidth | Cores per chip | Interconnect (ICI) bandwidth per chip | Network bandwidth (DCN) per chip | Chips per pod  
---|---|---|---|---|---|---|---  
TPU7x (Ironwood) | [tpu7x-standard](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu7x) |  BF16: 2,307 FP8: 4,614 | 192 GiB (7,380 GBps) |  2 TensorCores 4 SparseCores | 1,200 GBps | 100 Gbps | 9,216  
TPU v6e (Trillium) | [ct6e-standard](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v6e) |  BF16: 918 FP8: 918 | 32 GiB (1,638 GBps) |  1 TensorCore 2 SparseCores | 800 GBps | 100 Gbps | 256  
TPU v5p | [ct5p-hightpu](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v5p) |  BF16: 459 FP8: 459 | 95 GiB (2,765 GBps) |  2 TensorCores 4 SparseCores | 1,200 GBps | 50 Gbps | 8,960  
  
## TPU performance characteristics

TPUs are optimized to execute dense matrix-algebra operations with maximum efficiency. To choose when a TPU is best for your ML workloads, consider the following guidelines.

### Ideal use cases and workload requirements

Choosing the right TPU model depends on the computational characteristics, memory requirements, and scalability needs of your workload. Select one of the following tabs to view the recommendations.

### AI/ML training

  * **Pre-training large models** : training massive models from scratch. These workloads are compute and communication bound.

    * Required TPU capability: high peak FLOPS, low-precision support, and high interconnect bandwidth.
    * Recommended TPU versions: 
      * [TPU7x](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu7x). This version provides high FP8 performance.
      * [TPU v5p](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v5p). This version supports large-scale cluster configurations.
  * **Fine-tuning and distilling models** : adapting existing models using parameter-efficient methods or training smaller model variants.

    * Required TPU capability: moderate compute and sufficient memory capacity.
    * Recommended TPU versions: 
      * [TPU v6e](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v6e). This version is cost-efficient for standard training tasks.
      * [TPU7x](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu7x). This version offers high performance for large-scale fine-tuning.



### AI/ML inference

  * **Serving models online** : deploying models for real-time interaction where low latency is critical. These workloads are memory-bandwidth bound during the sequential generation of tokens.

    * Required TPU capability: high HBM bandwidth and large on-chip SRAM to minimize data retrieval latency.
    * Recommended TPU versions: 
      * [TPU v6e](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v6e). This version is optimized for cost-effective serving at scale.
      * [TPU7x](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu7x). This version provides high HBM bandwidth and large SRAM to accelerate token generation.
  * **Running batch inference** : processing large datasets offline where high throughput is the primary goal. These workloads are compute-bound during the prompt prefill phase.

    * Required TPU capability: high compute density to maximize throughput per dollar.
    * Recommended TPU versions: 
      * [TPU v6e](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v6e). This version is cost-efficient for high-throughput batch processing.
      * [TPU7x](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu7x). This version offers high compute density to process large batches quickly.



### Recommender systems

  * **Processing large embeddings** : training and serving recommendation models that use massive embedding tables. These workloads are capacity and communication bound. 
    * Required TPU capability: specialized SparseCore hardware to process sparse operations in parallel, large HBM capacity, and support for offloading to host memory.
    * Recommended TPU versions: 
      * [TPU7x](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu7x). This version includes four SparseCores per chip and offers the largest HBM capacity.
      * [TPU v6e](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v6e). This version includes two SparseCores per chip for cost-effective serving.
      * [TPU v5p](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v5p). This version includes four SparseCores per chip for large-scale training.



### Reinforcement learning

  * **Running reinforcement learning loops** : managing hybrid workloads that require tight loops of generating samples and updating policy weights.

    * Required TPU capability: low-latency ICI for fast weight and activation transfers between chips, and high-bandwidth host connections.
    * Recommended TPU versions:

      * [TPU7x](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu7x)
      * [TPU v5p](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#v5p)

These TPU versions use a high-speed 3D torus interconnect.




### Workload considerations

TPUs might not be the optimal choice for the following workloads:

  * Linear algebra programs that require frequent logical branching or contain many element-wise algebra operations.
  * Workloads that depend on custom operators in JAX or PyTorch that run on CPUs.
  * Scientific workloads requiring double-precision floating-point (FP64) arithmetic.



## Pricing considerations

The following factors determine TPU pricing on Google Cloud:

  * TPU version

  * Location

  * Consumption model




For complete pricing details, see the [TPU pricing](https://cloud.google.com/tpu/pricing) page.

### Consumption and purchasing models

You can provision TPU instances by using any of the following consumption options depending on your availability requirements and cost tolerance:

  * **On-demand** : Standard pay-as-you-go (PAYG) pricing for immediate execution. Offers maximum lifecycle flexibility, but availability is subject to physical resource constraints.
  * **[Spot](https://docs.cloud.google.com/compute/docs/instances/spot)** : Highly discounted (up to 70%) excess Google Cloud capacity. Because Google Cloud can stop or delete Spot VMs to reclaim capacity with a 30-second notice, these compute instances are ideal for fault-tolerant and checkpointed workloads.
  * **[Flex-start](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms)** : Enables requesting compute instances from a dedicated pool for up to seven days with higher availability.
  * **[Future reservations](https://docs.cloud.google.com/tpu/docs/about-tpu-reservations)** : Reservations that guarantee capacity and that offer a discounted price compared to on-demand pricing. Reserve TPU capacity for a specified future date and time, either for up to 90 days (calendar mode) or for 1 year or longer. If Google Cloud approves your request, then you can start using the capacity for the duration of the reservation.



### Committed use discounts (CUDs)

When you request a future reservation of 1 year or longer, you can obtain a CUD on your reserved TPU capacity. Applying a CUD to your compute instances gives you a significant price reduction compared to on-demand rates in exchange for a committed usage period.

For more information, see [CUDs for Compute Engine](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview).

## What's next

  * Review [TPU machines in accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines).
  * Learn how to [Create a TPU instance](https://docs.cloud.google.com/compute/docs/tpus/create-tpu-vm-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
