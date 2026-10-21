---
url: https://docs.cloud.google.com/compute/docs/gpus/about-gpus/
title: About GPU instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:31.918996+00:00
---

# About GPU instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/about-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About GPU instances Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features and limitations of Compute Engine instances that have attached GPUs.

To accelerate specific workloads on Compute Engine, you can either deploy an accelerator-optimized instance that has attached GPUs, or attach GPUs to an N1 general-purpose instance. For most workloads, Compute Engine provides GPUs for your instances in [pass-through mode](https://docs.nvidia.com/vgpu/5.0/grid-vgpu-user-guide/index.html#pass-through-gpu-use-introduction), which provides your instances with direct control over GPUs and their memory. However, for workloads that are more graphics-intensive and run on G4, G2, or N1 GPUs, you can use NVIDIA RTX Virtual Workstations (vWS). On G4 instances, NVIDIA RTX vWS enables the use of fractional GPU machine types. With these machine types, a single physical GPU can be shared by multiple virtual workstations by assigning a virtual GPU (vGPU) to each instance. G2 and N1 instances support vWS but don't support fractional vGPU machine types.

You can also use some GPU machine types on [AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/overview). AI Hypercomputer is a supercomputing system that is optimized to support your artificial intelligence (AI) and machine learning (ML) workloads. This option is recommended for creating a densely allocated, performance-optimized infrastructure that has integrations for Google Kubernetes Engine (GKE) and Slurm schedulers.

## Supported machine types

Compute Engine offers different machine types to support your various workloads.

Some machine types support [NVIDIA RTX Virtual Workstations (vWS)](https://www.nvidia.com/en-us/design-visualization/virtual-workstation/). When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).

**GPU machine types**  
---  
AI and ML workloads | Graphics and visualization | Other GPU workloads  
**Accelerator-optimized A series machine types** are designed for high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads. The later generation A series are ideal for pre-training and fine-tuning foundation models that involves large clusters of accelerators, while the A2 series can be used for training smaller models and single host inference. For these machine types, the GPU model is automatically attached to the instance. |  **Accelerator-optimized G series machine types** are designed for workloads such as NVIDIA Omniverse simulation workloads, graphics-intensive applications, video transcoding, and virtual desktops. These machine types support [NVIDIA RTX Virtual Workstations (vWS)](https://www.nvidia.com/en-us/design-visualization/virtual-workstation/). The G series can also be used for training smaller models and for single-host inference. For these machine types, the GPU model is automatically attached to the instance. |  For N1 general-purpose machine types, except for the N1 shared-core (`f1-micro` and `g1-small`), you can attach a select set of GPU models. Some of these GPU models also support NVIDIA RTX Virtual Workstations (vWS).  
  
  * [A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) (NVIDIA GB300 Ultra Superchips)   
(`nvidia-gb300`)
  * [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) (NVIDIA GB200 Superchips)   
(`nvidia-gb200`)
  * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) (NVIDIA B200)   
(`nvidia-b200`)
  * [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) (NVIDIA H200)   
(`nvidia-h200-141gb`)
  * [A3 Mega](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms) (NVIDIA H100)   
(`nvidia-h100-mega-80gb`)
  * [A3 High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms) (NVIDIA H100)   
(`nvidia-h100-80gb`)
  * [A3 Edge](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms) (NVIDIA H100)   
(`nvidia-h100-80gb`)
  * [A2 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms) (NVIDIA A100 80GB)   
(`nvidia-a100-80gb`)
  * [A2 Standard](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-standard-vms) (NVIDIA A100 4OGB)   
(`nvidia-tesla-a100`)

| 

  * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) (NVIDIA RTX PRO 6000)   
(`nvidia-rtx-pro-6000`)   
(`nvidia-rtx-pro-6000-vws`)
  * [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) (NVIDIA L4)   
(`nvidia-l4`)   
(`nvidia-l4-vws`)

| The following GPU models can be attached to N1 general-purpose machine types: 

  * NVIDIA T4   
(`nvidia-tesla-t4`)   
(`nvidia-tesla-t4-vws`). NVIDIA T4 is approaching end of support, see [NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos).
  * NVIDIA P4   
(`nvidia-tesla-p4`)   
(`nvidia-tesla-p4-vws`). NVIDIA P4 is approaching end of support, see [NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos).
  * NVIDIA V100   
(`nvidia-tesla-v100`)

  
  
## GPUs on Spot VMs

You can add GPUs to your Spot VMs at lower [spot prices](https://cloud.google.com/compute/gpus-pricing) for the GPUs. GPUs attached to Spot VMs work like normal GPUs but persist only for the life of the VM. Spot VMs with GPUs follow the same [preemption process](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-process) as all Spot VMs.

Consider requesting dedicated `Preemptible GPU` quota to use for GPUs on Spot VMs. For more information, see [Quotas for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot#quotas). 

During maintenance events, Spot VMs with GPUs are preempted by default and cannot be automatically restarted. If you want to recreate your VMs after they have been preempted, use a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/manager). Managed instance groups recreate your VM instances if the vCPU, memory, and GPU resources are available.

If you want a warning before your VMs are preempted, or want to configure your VMs to automatically restart after a maintenance event, use standard VMs with a GPU. For standard VMs with GPUs, Compute Engine provides [one hour advance notice](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance) before preemption.

Compute Engine does not charge you for GPUs if their VMs are preempted in the first minute after they start running.

To learn how to create Spot VMs with GPUs attached, read [Create a VM with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus) and [Creating Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-manage-spot#create). For example, see [Create an A3 Ultra or A4 instance using Spot VMs](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-a3u-a4#create-spot-overview).

## GPUs on instances with predefined run times

Instances that use the [standard provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models) typically can't use _preemptible allocation quotas_. Preemptible quotas are for temporary workloads and are usually more available. If your project doesn't have preemptible quota, and you have never requested it, then all instances in your project consume standard allocation quotas.

If you request preemptible allocation quota, then instances that use the standard provisioning model must meet all of the following criteria to consume preemptible allocation quota:

  * The instances have GPUs attached.
  * The instances are configured to be automatically deleted after a predefined run time through the `maxRunDuration` or `terminationTime` field. For more information, see the following: 
    * [Limit the run time of an instance](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime)
    * [Limit the run time of instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/limit-vm-runtime-in-migs)
  * The instance isn't allowed to consume reservations. For more information, see [Prevent compute instances from consuming reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-prevent-consumption).



When you consume preemptible allocation for time-bound GPU workloads, you can benefit from both uninterrupted run time and the high obtainability of preemptible allocation quota. For more information, see [Preemptible quotas](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas).

## GPUs and Confidential VM

You can use a GPU with a Confidential VM instance that uses Intel TDX on the A3 High machine type and AMD SEV on the G4 machine type. For more information, see [Confidential VM supported configurations](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations). To learn how to create a Confidential VM instance with GPUs, see [Create a Confidential VM instance with GPU](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance-with-gpu).

## GPUs and block storage

When you create an instance by using a GPU machine type, you can add persistent or temporary block storage to the instance. To store non-transient data, use persistent block storage like [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) or [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) because these disks are independent of the instance's lifecycle. Data on persistent storage can be retained even after you delete the instance.

For temporary scratch storage or caches, use temporary block storage by adding [Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd) when you create the instance.

### Persistent block storage with Persistent Disk and Hyperdisk volumes

You can attach Persistent Disk and select [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) volumes to GPU-enabled instances.

For machine learning (ML) and serving workloads, use Hyperdisk ML volumes, which offer high throughput and shorter data load times. Hyperdisk ML is a more cost-effective option for ML workloads because it offers lower GPU idle times.

Hyperdisk ML volumes provide read-only multi-attach support, so you can attach the same disk to multiple instances, giving each instance access to the same data.

For more information about the supported disk types for machine series that support GPUs, see the [N1](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) and [accelerator optimized](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) machine series pages.

### Local SSD disks

[Local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd) provide fast, temporary storage for caching, data processing, or other transient data. Local SSD disks provide fast storage because they are physically attached to the server that hosts your instance. Local SSD disks provide temporary storage because the instance loses data if it restarts.

Avoid storing data with strong persistency requirements on Local SSD disks. To store non-transient data, use persistent storage instead.

**Warning:** For instances with GPUs, Compute Engine cannot recover data on any Local SSD disks attached to the instance if Compute Engine restarts the instance for [host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).

If you manually stop an instance with a GPU, you can preserve the Local SSD data, with certain restrictions. See the [Local SSD documentation](https://docs.cloud.google.com/compute/docs/disks/local-ssd#stop_instance) for more details.

For regional support for Local SSD with GPU types, see [Local SSD availability](https://docs.cloud.google.com/compute/docs/regions-zones/accelerator-zones#local-ssd-gpu).

## GPUs and host maintenance

Compute Engine always stops instances with attached GPUs when it performs maintenance events on the host server. If the instance has attached Local SSD disks, the instance loses the Local SSD data after it stops.

For information on handling maintenance events, see [Handling GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).

## Reserve GPU capacity

Reservations provide high assurance of capacity for zone-specific resources, including GPUs. You can use reservations to ensure that you have GPUs available when you need to use them for performance-intensive applications. For the different methods to reserve zone-specific resources in Compute Engine, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).

Reservations are also required when you want to receive resource-based committed use discounts (CUDs) for your GPUs.

## GPU pricing

If you request Compute Engine to provision GPUs using the [spot, flex-start, or reservation-bound provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models), then you get the GPUs at discounted prices, depending on the GPU type. You can also receive committed use discounts or sustained use discounts (only with N1 VMs) for your GPU usage.

For hourly and monthly pricing for GPUs, see [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).

### Committed use discounts for GPUs

You can receive committed use discounts for GPUs by purchasing resource-based commitments or compute flexible commitments:

  * **Resource-based commitments** provide deep discounts for Compute Engine resources in return for committing to using the resources in a specific region for at least one year. You typically purchase commitments for resources such as vCPUs, memory, GPUs, and Local SSD disks for use with a specific machine series. When you use your resources, you receive qualifying resource usage at discounted prices. To learn more about these discounts, see [Resource-based committed use discounts](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts). To purchase a commitment with GPUs, you must also reserve the GPUs and attach the reservations to your commitment. For more information, see [Attach reservations to resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/reservations-with-commitments#attach-reservations-to-resource-cuds).

  * **Compute flexible commitments** cover your eligible G2 and G4 GPU spend without requiring attached reservations. You can't attach reservations to a compute flexible commitment. Because compute flexible commitments don't reserve capacity, capacity isn't assured for G2 or G4 GPUs. If GPUs aren't available, then you can use the flexible commitment to cover other eligible resource types or services. If you want capacity assurance, then make sure to reserve the GPUs separately by creating reservations. For more information, see [Compute flexible CUDs](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based).




### Sustained use discounts for GPUs

Instances that use N1 machine types with attached GPUs receive [sustained use discounts (SUDs)](https://docs.cloud.google.com/compute/docs/sustained-use-discounts), similar to vCPUs. When you select a GPU for a virtual workstation, Compute Engine automatically adds an NVIDIA RTX Virtual Workstation license to your instance.

## GPU restrictions and limitations

For instances with attached GPUs, the following restrictions and limitations apply:

  * Only accelerator-optimized (A4X Max, A4X, A4, A3, A2, G4, and G2) and general-purpose N1 machine types support GPUs.

  * To protect Compute Engine systems and users, new projects have a global GPU quota that limits the total number of GPUs you can create in any supported zone. When you request a GPU quota, you must request a quota for the GPU models that you want to create in each region, and an additional global quota for the total number of GPUs of all types in all zones.

  * Instances with one or more GPUs have a maximum number of vCPUs for each GPU that you add to the instance. To see the available vCPU and memory ranges for different GPU configurations, see the [GPUs list](https://docs.cloud.google.com/compute/docs/gpus#gpus_for_compute_workloads).

  * GPUs require device drivers to function properly. NVIDIA GPUs that run on Compute Engine must use a minimum driver version. For more information about driver versions, see [Required NVIDIA driver versions](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#minimum-driver).

  * The [Compute Engine SLA](https://cloud.google.com/compute/sla) covers instances with an attached GPU model only if that attached GPU model is generally available.

For regions that have multiple zones, the Compute Engine SLA covers the instance only if the GPU model is available in more than one zone within that region. For GPU models by region, see [GPU locations](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones).

  * Compute Engine supports one concurrent user per GPU or vGPU.

  * Also see the [limitations for each machine type with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#limitations).




## What's next?

  * Learn how to [create instances with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).
  * Learn how to [add or remove GPUs](https://docs.cloud.google.com/compute/docs/gpus/add-remove-gpus).
  * Learn how to [create a Confidential VM instance with an attached GPU](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance-with-gpu).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
