---
url: https://docs.cloud.google.com/compute/docs/tpus/tpu-machines/
title: TPU machines in accelerator-optimized machine family \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:45:42.321686+00:00
---

# TPU machines in accelerator-optimized machine family  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/tpus/tpu-machines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  TPU machines in accelerator-optimized machine family Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the Compute Engine instances in the accelerator-optimized machine family that have Tensor Processing Units (TPUs). TPUs are Google's custom-developed, application-specific integrated circuits (ASICs) that are optimized specifically for artificial intelligence (AI) and machine learning (ML) workloads.

Compute Engine supports the following TPU versions:

  * TPU7x
  * TPU v6e
  * TPU v5p



Each machine type within a version has a specific topology and a number of TPU chips attached.

## Fundamentals of TPU architecture

Understanding the fundamentals of TPU architecture helps you to choose the TPU version and machine type for your workload.

  * **TPU chip** : A TPU chip is a specialized accelerator designed by Google for machine learning. Each TPU chip contains one or more TensorCores to handle massive matrix operations. Each TensorCore consists of one or more matrix-multiply units (MXUs), which use a systolic array architecture to perform thousands of multiply-accumulate operations per cycle without constant memory access. While primarily used for high-speed matrix processing, the TPU chip also includes vector and scalar units for general computation and control flow operations.

  * **TPU Pod** : A TPU Pod is a contiguous set of TPUs grouped together over a specialized network. The number of TPU chips in a TPU Pod is dependent on the TPU version.

  * **TPU instance** : a Linux compute instance that runs on a TPU host and has direct access to the underlying TPU hardware, offering access to high-performance libraries, SSH connectivity, and runtime debug logs.

  * **TPU slice** : A logical group of interconnected TPU chips, accessed through one or more TPU instances. Slices have one of the following scopes:

    * **Single-host slice** : A slice consisting of one host machine. In general, this maps to one TPU instance.
    * **Multi-host slice** : A slice consisting of multiple TPU instances interconnected using a high-speed inter-chip interconnect (ICI).
  * **TPU cube** : A 4x4x4 topology of interconnected TPU chips. This is only applicable to 3D topologies.

  * **SparseCore** : SparseCores are dataflow processors that accelerate models using sparse operations. A primary use case is accelerating recommendation models, which rely heavily on embeddings.

  * **TPU versions** : The exact architecture of a TPU chip depends on the TPU version that you use. Each TPU version also supports different slice sizes and configurations.




For information about how TPUs work, see [TPU architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm) document in the Cloud TPU documentation.

## Recommended TPU versions by workload types

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




## Consumption options

To optimize resource utilization and cost while balancing workload performance, Compute Engine supports the following TPU consumption options:

  * **On-demand** : to consume TPUs without arranging capacity in advance. Before requesting resources, you must have enough [on-demand quota](https://docs.cloud.google.com/compute/resource-usage#tpu_quota) for the specific type and quantity of TPU instances. On-demand is the most flexible consumption option; however, there is no guarantee that enough on-demand resources will be available to fulfill your request.

  * **Spot** : to provision Spot VMs, you can get significant discounts, but Spot VMs can be preempted at any time, with a 30-second warning. For more information, see [About Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).

  * **Flex-start** : to provision {flex_start_vms_name} for up to seven days, with Compute Engine automatically allocating the hardware on a best-effort basis based on availability. For more information, see [About {flex_start_vms_name}](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms).

  * **Future reservation for capacity blocks** : to request a future reservation for one year or longer. For more information, see [Request a future reservation for one year or longer](https://docs.cloud.google.com/tpu/docs/long-term-reservation) in the Cloud TPU documentation.

  * **Future reservation in calendar mode** : to provision TPU resources for up to 90 days, for a specified time period. For more information, see [About future reservation requests in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).




On-demand is the default consumption model for TPUs if you don't specify another option.

For information about the underlying provisioning model that enables the consumption option, see [About VM provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

### Consumption option availability by TPU versions

The following table summarizes the availability of each consumption option by TPU versions.

TPU version | On-demand | [Spot](https://docs.cloud.google.com/compute/docs/instances/spot) | [Flex-start](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms) | [On-demand reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) | [Future reservations](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview) | [Future reservations in calendar mode1](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview) | [Future reservations for capacity blocks](https://docs.cloud.google.com/tpu/docs/long-term-reservation)  
---|---|---|---|---|---|---|---  
**TPU7x** |  | 2 | 2 |  |  | 2 | 2  
**TPU v6e** |  |  |  |  |  |  |   
**TPU v5p** |  |  |  |  |  |  |   
  
1 You can't create future reservation requests in calendar mode when using the All Capacity mode.

2 Spot, Flex-start, future reservations in calendar mode, and future reservations for capacity blocks for TPU7x are restricted by an allowlist. To request access, contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact).

### All Capacity mode

By default, TPU reservations include automatic failure recovery. Google Cloud manages this process by automatically replacing faulty TPU machines with healthy ones from the reserved capacity to ensure resources are available to restart your TPU slices.

Alternatively, for TPU v6e and TPU7x, you can request TPU capacity in _All Capacity mode_. This mode grants access to your full reserved capacity and full topology visibility. In this mode, you can also target specific blocks or sub-blocks for precise, topology-aware workload placement. However, you are responsible for managing hardware failures and maintenance.

For more information about these modes, see [TPU capacity modes](https://docs.cloud.google.com/tpu/docs/capacity-modes) in the Cloud TPU documentation.

## TPU versions comparison

Compare the characteristics of different TPU versions. You can select specific properties in the **Choose properties to compare** field to compare those properties across all TPU versions in the following table.

Workload typeInstance typeCPU typeArchitecturevCPUsvCPU definitionMemoryShared memory architectureCustom machine typesExtended memorySole tenancyNested virtualizationConfidential ComputingDisk interface typeHyperdisk BalancedHyperdisk Balanced HAHyperdisk ExtremeHyperdisk MLHyperdisk ThroughputLocal SSDStandard PDBalanced PDSSD PDExtreme PDNetwork interfacesMaximum network bandwidthMax TPUs per VMSustained use discountsResource-based committed use discounts (CUDs)Compute flexible CUDsSpot VM discounts

Clear all

| TPU7x| v6e| v5p  
---|---|---|---  
**Workload type** |  Accelerator optimized |  Accelerator optimized |  Accelerator optimized  
**Instance type** |  VM |  VM |  VM  
**CPU type** |  Intel Emerald Rapids |  AMD EPYC Genoa |  Intel Sapphire Rapids  
**Architecture** |  x86 |  x86 |  x86  
**vCPUs** |  224 |  44 to 180 |  208  
**vCPU definition** |  Thread |  Thread |  Thread  
**Memory** |  960 GB |  176 to 1440 GB |  448 GB  
**Shared memory architecture** |  NUMA |  NUMA |  NUMA  
**Custom machine types** | **—** | **—** | **—**  
**Extended memory** | **—** | **—** | **—**  
**Sole tenancy** | **—** | **—** | **—**  
**Nested virtualization** | **—** | **—** | **—**  
**Confidential Computing** | **—** |  | **—**  
**Disk interface type** |  NVMe |  NVMe |  NVMe  
**Hyperdisk Balanced** |  |  | **—**  
**Hyperdisk Balanced HA** | **—** | **—** | **—**  
**Hyperdisk Extreme** | **—** | **—** | **—**  
**Hyperdisk ML** |  |  |   
**Hyperdisk Throughput** | **—** | **—** | **—**  
**Local SSD** | **—** | **—** | **—**  
**Standard PD** | **—** | **—** | **—**  
**Balanced PD** | **—** | **—** |   
**SSD PD** | **—** | **—** | **—**  
**Extreme PD** | **—** | **—** | **—**  
**Network interfaces** |  gVNIC |  gVNIC |  gVNIC  
**Maximum network bandwidth** |  400 Gbps |  50 to 400 Gbps |  200 Gbps  
**Max TPUs per VM** |  4 |  8 |  4  
**Sustained use discounts** | **—** | **—** | **—**  
**Resource-based committed use discounts (CUDs)** |  discounts |  discounts |  discounts  
**Compute flexible CUDs** | **—** discounts| **—** discounts| **—** discounts  
**Spot VM discounts** |  |  |   
  
### TPU architecture specifications

The following table lists the key specifications for each TPU version.

Specification | TPU7x | TPU v6e | TPU v5p  
---|---|---|---  
Number of chips per pod | 9216 | 256 | 8960  
Peak compute per chip (BF16) (TFLOPs) | 2307 | 918 | 459  
Peak compute per chip (FP8) (TFLOPs) | 4614 | 918 | 459  
HBM capacity per chip (GiB) | 192 | 32 | 95  
HBM bandwidth per chip (GBps) | 7380 | 1638 | 2765  
Number of vCPUs (4-chip VM) | 224 | 180 | 208  
RAM (GiB) (4-chip VM) | 960 | 720 | 448  
Number of TensorCores per chip | 2 | 1 | 2  
Number of SparseCores per chip | 4 | 2 | 4  
Bidirectional inter-chip interconnect (ICI) bandwidth per chip (GBps) | 1200 | 800 | 1200  
Data center network (DCN) bandwidth per chip (Gbps) | 100 | 100 | 50  
  
## TPU machine types

The following sections describe the machine types available for each TPU version.

### TPU7x (Ironwood)

Each TPU7x virtual machine (VM) contains 4 TPU chips. All TPU7x slices use full-host, 4-chip VMs.

Each TPU7x chip contains two TensorCores and four SparseCores.

The Ironwood programming model lets you access two TPU devices instead of a single logical core architecture used in previous generations. For more information, see [Dual-chiplet architecture](https://docs.cloud.google.com/tpu/docs/tpu7x#dual-chiplet_architecture) in the Cloud TPU documentation.

Machine type | Number of vCPUs | Instance memory (GiB) | Physical NIC count | Maximum network bandwidth (Gbps) | Number of TPU chips per VM | Number of NUMA nodes | Total TPU memory (GiB HBM)  
---|---|---|---|---|---|---|---  
`tpu7x-standard-4t` | 224 | 960 | 2 | 400 | 4 | 2 | 768  
  
For more information about the TPU7x architecture, see [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x) in the Cloud TPU documentation.

### TPU v6e (Trillium)

Each TPU v6e VM can contain 1, 4, or 8 TPU chips. 4-chip and smaller slices have the same non-uniform memory access (NUMA) node.

v6e slices are created using half-host VMs, each with 4 TPU chips, except for the following:

  * `ct6e-standard-1t` with only a single TPU chip is primarily intended for testing.
  * `ct6e-standard-8t` is a full-host VM that has been optimized for an inference use case, allowing all 8 TPU chips that are attached to a single VM to be used in a single serving workload.

Machine type | Number of vCPUs | Instance memory (GB) | Physical NIC count | Maximum network bandwidth (Gbps) | Number of TPU chips per VM | Number of NUMA nodes | Total TPU memory (GiB HBM)  
---|---|---|---|---|---|---|---  
`ct6e-standard-1t` | 44 | 176 | 1/4 | 50 | 1 | 1 | 32  
`ct6e-standard-4t` | 180 | 720 | 2 | 400 | 4 | 1 | 128  
`ct6e-standard-8t` | 360 | 1440 | 1 | 200 | 8 | 2 | 256  
  
For more information about the TPU v6e architecture, see [TPU v6e](https://docs.cloud.google.com/tpu/docs/v6e) in the Cloud TPU documentation.

### TPU v5p

A TPU v5p Pod is composed of 8960 TPU chips interconnected with reconfigurable high-speed links. TPU v5p's flexible networking lets you connect the TPU chips in a same-sized slice in multiple ways. Single slice training is supported for up to 6144 TPU chips.

Machine type | Number of vCPUs | Instance memory (GB) | Physical NIC count | Maximum network bandwidth (Gbps) | Number of TPU chips per VM | Number of NUMA nodes | Total TPU memory (GiB HBM)  
---|---|---|---|---|---|---|---  
`ct5p-hightpu-4t` | 208 | 448 | 1 | 200 | 4 | 2 | 380  
  
For more information about the TPU v5p architecture, see [TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p) in the Cloud TPU documentation.

## TPU topology

The topology defines the physical arrangement of TPUs within a TPU slice. Depending on the TPU version, the topology is two- or three-dimensional. You can identify the number of TPU chips in a slice by calculating the product of each size in the topology. For example:

  * The `tpu7x-standard-4t` machine type with a `2x2x2` topology is an 8-chip multi-host TPU7x slice.



The following table lists the topologies available for each TPU version.

TPU7x (Ironwood)TPU v6e (Trillium)TPU v5pSingle-hostMulti-hostClear all

TPU version | Machine type | Scope | Technical specifications  
---|---|---|---  
TPU7x (Ironwood) | `tpu7x-standard-4t` | Single-host | 

  * Topology: 2x2x1
  * Number of TPU chips for the topology: 4
  * Number of hosts: 1
  * Number of VMs: 1
  * Cubes count: 1/16

  
TPU7x (Ironwood) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 2x2x2
  * Number of TPU chips for the topology: 8
  * Number of hosts: 2
  * Number of VMs: 2
  * Cubes count: 1/8

  
TPU7x (Ironwood) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 2x2x4
  * Number of TPU chips for the topology: 16
  * Number of hosts: 4
  * Number of VMs: 4
  * Cubes count: 1/4

  
TPU7x (Ironwood) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 2x4x4
  * Number of TPU chips for the topology: 32
  * Number of hosts: 8
  * Number of VMs: 8
  * Cubes count: 1/2

  
TPU7x (Ironwood) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 4x4x4
  * Number of TPU chips for the topology: 64
  * Number of hosts: 16
  * Number of VMs: 16
  * Cubes count: 1

  
TPU7x (Ironwood) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 4x4x8
  * Number of TPU chips for the topology: 128
  * Number of hosts: 32
  * Number of VMs: 32
  * Cubes count: 2

  
TPU7x (Ironwood) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 4x8x8
  * Number of TPU chips for the topology: 256
  * Number of hosts: 64
  * Number of VMs: 64
  * Cubes count: 4

  
TPU7x (Ironwood) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 8x8x8
  * Number of TPU chips for the topology: 512
  * Number of hosts: 128
  * Number of VMs: 128
  * Cubes count: 8

  
TPU7x (Ironwood) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: 8x8x16
  * Number of TPU chips for the topology: 1024
  * Number of hosts: 256
  * Number of VMs: 256
  * Cubes count: 16

  
TPU7x (Ironwood) | `tpu7x-standard-4t` | Multi-host | 

  * Topology: {A}x{B}x{C} (where A, B, and C are multiples of two)
  * Number of TPU chips for the topology: A*B*C
  * Number of hosts: (A*B*C)/4
  * Number of VMs: (A*B*C/4)
  * Cubes count: (A*B*C/64)

  
TPU v6e (Trillium) | `ct6e-standard-1t` | Single-host | 

  * Topology: 1x1
  * Number of TPU chips for the topology: 1
  * Number of VMs: 1

  
TPU v6e (Trillium) | `ct6e-standard-8t` | Single-host | 

  * Topology: 2x4
  * Number of TPU chips for the topology: 8
  * Number of VMs: 1

  
TPU v6e (Trillium) | `ct6e-standard-4t` | Single-host | 

  * Topology: 2x2
  * Number of TPU chips for the topology: 4
  * Number of VMs: 1

  
TPU v6e (Trillium) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 2x4
  * Number of TPU chips for the topology: 8
  * Number of VMs: 2

  
TPU v6e (Trillium) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 4x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 4

  
TPU v6e (Trillium) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 4x8
  * Number of TPU chips for the topology: 32
  * Number of VMs: 8

  
TPU v6e (Trillium) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 8x8
  * Number of TPU chips for the topology: 64
  * Number of VMs: 16

  
TPU v6e (Trillium) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 8x16
  * Number of TPU chips for the topology: 128
  * Number of VMs: 32

  
TPU v6e (Trillium) | `ct6e-standard-4t` | Multi-host | 

  * Topology: 16x16
  * Number of TPU chips for the topology: 256
  * Number of VMs: 64

  
TPU v5p | `ct5p-hightpu-4t` | Single-host | 

  * Topology: 2x2x1
  * Number of TPU chips for the topology: 4
  * Number of VMs: 1

  
TPU v5p | `ct5p-hightpu-4t` | Multi-host | 

  * Topology: 2x2x2
  * Number of TPU chips for the topology: 8
  * Number of VMs: 2

  
TPU v5p | `ct5p-hightpu-4t` | Multi-host | 

  * Topology: 2x2x4
  * Number of TPU chips for the topology: 16
  * Number of VMs: 4

  
TPU v5p | `ct5p-hightpu-4t` | Multi-host | 

  * Topology: 2x4x4
  * Number of TPU chips for the topology: 32
  * Number of VMs: 8

  
TPU v5p | `ct5p-hightpu-4t` | Multi-host | 

  * Topology: {A}x{B}x{C} (where A, B, and C are multiples of two)
  * Number of TPU chips for the topology: A*B*C
  * Number of VMs: (A*B*C/4)1

  
  
  1. Calculated by the topology product divided by four. ↩




## What's next

  * Learn about [TPU resources in Compute Engine](https://docs.cloud.google.com/compute/docs/tpus/tpu-resources-in-compute-engine)
  * Try the quickstart: [Create a single TPU VM](https://docs.cloud.google.com/compute/docs/tpus/quickstart-create-tpu-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
