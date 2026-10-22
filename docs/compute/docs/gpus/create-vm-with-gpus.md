---
url: https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus/
title: Overview of creating an instance with attached GPUs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:36.672882+00:00
---

# Overview of creating an instance with attached GPUs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Overview of creating an instance with attached GPUs Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document provides an overview of the steps required to create a Compute Engine instance with attached graphics processing units (GPUs). You can use GPUs to accelerate specific workloads, such as machine learning and data processing.

You can also use some GPU machine types on [AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/overview). AI Hypercomputer is a supercomputing system that is optimized to support your artificial intelligence (AI) and machine learning (ML) workloads. This option is recommended for creating a densely allocated, performance-optimized infrastructure that has integrations for Google Kubernetes Engine (GKE) and Slurm schedulers.

For more information about GPUs on Compute Engine, see [About GPUs](https://docs.cloud.google.com/compute/docs/gpus/about-gpus).

## Select the GPU model

For a list of GPU models that are available, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus). Also make a note of the machine type that is supported for the selected GPU model.

For each model, it might also be helpful to review the following:

  * [Supported regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  * [GPU pricing](https://docs.cloud.google.com/compute/gpus-pricing#gpus) to understand the cost to use each GPU model on your instances. For instances that use accelerator-optimized machines, also review [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing).



### Limitations

In addition to the [restrictions for all instances with GPUs](https://docs.cloud.google.com/compute/docs/gpus/about-gpus#restrictions), each machine series with attached GPUs has the following limitations:

###  A4X Max instances 

**Caution:** The [ Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to the A4X Max machine series.

  * You can only request capacity that uses the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning).
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) or [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use this machine type.
  * You can only create instances in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * This machine type is only available on the [NVIDIA Grace platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#arm_processors).
  * Machine type changes aren't supported for A4X Max. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on this machine type. For a list of supported Linux operating systems, review the [supported operating systems for GPU instances](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support).
  * A4X Max instances don't support the following: 
    * [Sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms)
  * You can't attach Hyperdisk ML disks created before February 4, 2026 to A4X Max machine types.



###  A4X instances 

**Caution:** The [ Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to the A4X machine series.

  * You can only request capacity that uses the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning).
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) or [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use this machine type.
  * You can only create instances in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * This machine type is only available on the [NVIDIA Grace platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#arm_processors).
  * Machine type changes aren't supported for A4X. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on this machine type. For a list of supported Linux operating systems, review the [supported operating systems for GPU instances](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support).
  * For A4X instances, when you use `ethtool -S` to monitor GPU networking, the physical port counters that end in `_phy` don't update. This is expected behavior for instances that use the MRDMA Virtual Function (VF) architecture. For more information, see [MRDMA functions and network monitoring tools](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mrdma-monitoring).
  * A4X instances don't support the following: 
    * [Sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
    * [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)
    * [Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms)
  * You can't attach Hyperdisk ML disks created before February 4, 2026 to A4X machine types.



###  A4 instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for an A4 machine type.
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A4 machine type.
  * You can only use an A4 machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * The A4 machine type is only available on the [Emerald Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * You can't change the machine type of an instance to or from A4 machine type. You must create a new instance with this machine type.
  * A4 machine types don't support [sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).
  * You can't run Windows operating systems on an A4 machine type.
  * For A4 instances, when you use `ethtool -S` to monitor GPU networking, physical port counters that end in `_phy` don't update. This is expected behavior for instances that use the MRDMA Virtual Function (VF) architecture. For more information, see [MRDMA functions and network monitoring tools](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mrdma-monitoring).
  * You can't attach Hyperdisk ML disks that were created before February 4, 2026 to A4 machine types.



###  A3 Ultra instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for an A3 Ultra machine type.
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 Ultra machine type.
  * You can only use an A3 Ultra machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use Persistent Disk (regional or zonal). You can only use [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * The A3 Ultra machine type is only available on the [Emerald Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 Ultra machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 Ultra machine type.
  * A3 Ultra machine types don't support [sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).
  * For A3 Ultra instances, when you use `ethtool -S` to monitor GPU networking, physical port counters that end in `_phy` don't update. This is expected behavior for instances that use the MRDMA Virtual Function (VF) architecture. For more information, see [MRDMA functions and network monitoring tools](https://docs.cloud.google.com/compute/docs/gpus/gpu-network-bandwidth#mrdma-monitoring).



###  A3 Mega instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for an A3 Mega machine type.
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 Mega machine type.
  * You can only use an A3 Mega machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) on an instance that uses an A3 Mega machine type.
  * The A3 Mega machine type is only available on the [Sapphire Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 Mega machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 Mega machine type.



###  A3 High instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for an A3 High machine type.
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 High machine type.
  * You can only use an A3 High machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) on an instance that uses an A3 High machine type.
  * The A3 High machine type is only available on the [Sapphire Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 High machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 High machine type.
  * For `a3-highgpu-1g`, `a3-highgpu-2g`, and`a3-highgpu-4g` machine types, you must create instances by using Spot VMs or Flex-start VMs. For detailed instructions on these options, review the following: 
    * To create Spot VMs, set the provisioning model to `SPOT` when you [create an accelerator-optimized VM](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized).
    * To create Flex-start VMs, you can use one of the following methods: 
      * Create a standalone VM and set the provisioning model to `FLEX_START` when you [create an accelerator-optimized VM](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized).
      * Create a resize request in a managed instance group (MIG). For instructions, see [Create a MIG with GPU VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms).
  * You can only use a [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with an `a3-highgpu-1g` machine type in limited [regions and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing_1), and all the [limitations for Confidential VM running on the A3 High machine type](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing) apply.



###  A3 Edge instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for an A3 Edge machine type.
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A3 Edge machine type.
  * You can only use an A3 Edge machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) on an instance that uses an A3 Edge machine type.
  * The A3 Edge machine type is only available on the [Sapphire Rapids CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Machine type changes aren't supported for A3 Edge machine type. To switch to or from this machine type, you must create a new instance.
  * You can't run Windows operating systems on an A3 Edge machine type.
  * A3 Edge machine types don't support [sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes).



###  A2 Standard instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for an A2 Standard machine type.
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A2 Standard machine type.
  * You can only use an A2 Standard machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * The A2 Standard machine type is only available on the [Cascade Lake platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * If your instance uses an A2 Standard machine type, you can only switch from one A2 Standard machine type type to another A2 Standard machine type. You can't change to any other machine type. For more information, see [Modify accelerator-optimized instances](https://docs.cloud.google.com/compute/docs/gpus/add-remove-gpus#accelerator-optimized_vms).
  * You can't use the Windows operating system with the `a2-megagpu-16g` machine type. When using a Windows operating system, choose a different A2 Standard machine type.
  * You can't do a quick format of the attached Local SSDs on Windows instances that use A2 Standard machine types. To format these Local SSDs, you must do a full format by using the [diskpart utility](https://docs.microsoft.com/windows-server/administration/windows-commands/diskpart) and specifying `format fs=ntfs label=tmpfs`.



###  A2 Ultra instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for an A2 Ultra machine type.
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use an A2 Ultra machine type.
  * You can only use an A2 Ultra machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * The A2 Ultra machine type is only available on the [Cascade Lake platform](https://docs.cloud.google.com/compute/docs/cpu-platforms).
  * If your instance uses an A2 Ultra machine type, you can't change the machine type. If you need to use a different A2 Ultra machine type, or any other machine type, you must create a new instance.
  * You can't change any other machine type to an A2 Ultra machine type. If you need a instance that uses an A2 Ultra machine type, you must create a new instance.
  * You can't do a quick format of the attached Local SSDs on Windows instances that use A2 Ultra machine types. To format these Local SSDs, you must do a full format by using the [diskpart utility](https://docs.microsoft.com/windows-server/administration/windows-commands/diskpart) and specifying `format fs=ntfs label=tmpfs`.



###  G4 instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for a G4 machine type.
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use a G4 machine type.
  * You can only use a G4 machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * You can't use [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) (regional or zonal) on an instance that uses a G4 machine type.
  * The G4 machine type is only available on the [AMD EPYC Turin 5th Generation platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#amd_processors).
  * You can only use a [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview) with the `g4-standard-48` machine type in limited [regions and zones](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing_1). All the [limitations for Confidential VM running on the G4 machine type](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#nvidia-confidential-computing) apply.
  * You can't use Windows operating systems on `g4-standard-384` instances.
  * You can't attach Hyperdisk ML disks that were created before February 4, 2026 to G4 machine types.
  * When creating G4 instances that have less than one GPU attached (fractional GPUs), don't use the `--no-service-account` or `--no-scopes` flags. To authenticate NVIDIA vGPU drivers, Compute Engine must [verify the VM's identity](https://docs.cloud.google.com/compute/docs/instances/verifying-instance-identity). This process requires that service accounts are enabled.



###  G2 instances 

  * You can only request capacity by using the [supported consumption options](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#pricing-and-provisioning) for a G2 machine type.
  * You don't receive [sustained use discounts](https://docs.cloud.google.com/compute/docs/sustained-use-discounts) and [flexible committed use](https://docs.cloud.google.com/compute/docs/instances/committed-use-discounts-overview#spend_based) discounts for instances that use a G2 machine type.
  * You can only use a G2 machine type in certain [regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones#view-using-table).
  * The G2 machine type is only available on the [Cascade Lake platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#intel_processors).
  * Standard Persistent Disk (`pd-standard`) isn't supported on instances that use the G2 machine type. For supported disk types, see [Supported disk types for G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-disks).
  * You can't create [Multi-Instance GPUs](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) on an instance that uses a G2 machine type.
  * If you need to change the machine type of a G2 instance, review [Modify accelerator-optmized instances](https://docs.cloud.google.com/compute/docs/gpus/add-remove-gpus#accelerator-optimized_vms).
  * You can't use [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images) as boot disks for instances that use the G2 machine type.
  * The current default driver for Container-Optimized OS doesn't support L4 GPUs running on G2 machine types. Also, Container-Optimized OS only supports a select set of drivers. If you want to use Container-Optimized OS on G2 machine types, review the following notes: 
    * Use a Container-Optimized OS version that supports the minimum recommended NVIDIA driver version `525.60.13` or later. For more information, review the [Container-Optimized OS release notes](https://docs.cloud.google.com/container-optimized-os/docs/release-notes). 
    * When you [install the driver](https://docs.cloud.google.com/container-optimized-os/docs/how-to/run-gpus#install-driver), specify the latest available version that works for the L4 GPUs. For example, `sudo cos-extensions install gpu -- -version=525.60.13`. 
  * You must use the Google Cloud CLI or REST to [create G2 instances](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized#create-vm) for the following scenarios: 
    * You want to specify custom memory values.
    * You want to customize the number of visible CPU cores.



###  N1+GPU instances 

To learn about the limitations for N1 instances with GPUs, see [features for the N1 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) and [GPUs for the N1 machine series](https://docs.cloud.google.com/compute/docs/gpus#n1-gpus).

## Choose an operating system

If you are using GPUs for machine learning, use one of the following operating systems:

  * _Images optimized for AI workloads._ You can use Ubuntu and Rocky images, which are available in accelerator-optimized versions with NVIDIA drivers and CUDA Toolkit pre-installed. See [OS images](https://docs.cloud.google.com/ai-hypercomputer/docs/images#os-image) in the AI Hypercomputer documentation.

  * _Deep Learning VM Images._ Each Deep Learning VM has a GPU driver installation tool and includes packages such as TensorFlow and PyTorch. You can also use a Deep Learning VM for general GPU workloads. To learn more about available images and packages installed on these images, see [Choosing an image](https://docs.cloud.google.com/deep-learning-vm/docs/images) in the Deep Learning VM documentation.

**Caution:** You can't use [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images) on boot disks for your VMs that use G2 machine types. G2 machine types are accelerator-optimized machine series that have NVIDIA L4 GPUs attached. 



Alternatively, you can use a public or custom image. For most [public images](https://docs.cloud.google.com/compute/docs/images/os-details) or [custom images](https://docs.cloud.google.com/compute/docs/images#custom_images), you need to install NVIDIA drivers and CUDA Toolkit. To help identify which drivers are appropriate for your GPU model, see [installing GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu).

## Check GPU quota

To protect Compute Engine systems and users, new projects have a global GPU quota, which limits the total number of GPUs you can create in any supported zone. To review GPU quota, see [GPU quota](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).

**Note:** Some regions might display quotas even though GPUs are not currently available in that region. Ensure that the region that you are requesting quotas for support GPUs. For a list of regions with GPUs, see [GPUs regions and zone availability](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

If you need additional GPU quota, [request a quota increase](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota). When you request GPU quota, you must request quota for the GPU types that you want to create in each region and an additional global quota for the total number of GPUs of all types in all zones.

If your project has an established billing history, it will receive quota automatically after you submit the request.

### GPU instances and preemptible allocation quotas

Instances that use the [standard provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models) typically can't use _preemptible allocation quotas_. Preemptible quotas are for temporary workloads and are usually more available. If your project doesn't have preemptible quota, and you have never requested it, then all instances in your project consume standard allocation quotas.

If you request preemptible allocation quota, then instances that use the standard provisioning model must meet all of the following criteria to consume preemptible allocation quota:

  * The instances have GPUs attached.
  * The instances are configured to be automatically deleted after a predefined run time through the `maxRunDuration` or `terminationTime` field. For more information, see the following: 
    * [Limit the run time of an instance](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime)
    * [Limit the run time of instances in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/limit-vm-runtime-in-migs)
  * The instance isn't allowed to consume reservations. For more information, see [Prevent compute instances from consuming reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-prevent-consumption).



When you consume preemptible allocation for time-bound GPU workloads, you can benefit from both uninterrupted run time and the high obtainability of preemptible allocation quota. For more information, see [Preemptible quotas](https://docs.cloud.google.com/compute/resource-usage#preemptible-quotas).

## Create an instance that has attached GPUs

To create an instance that has attached GPUs, complete the following steps:

  1. Create the instance. The method used to create an instance depends on the workload that you want to run.

**GPU machine types**  
---  
AI and ML workloads | Graphics and visualization | Other GPU workloads  
**Accelerator-optimized A series machine types** are designed for high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads. For these machine types, the GPU model is automatically attached to the instance. |  **Accelerator-optimized G series machine types** are designed for workloads such as NVIDIA Omniverse simulation workloads, graphics-intensive applications, video transcoding, and virtual desktops. These machine types support [NVIDIA RTX Virtual Workstations (vWS)](https://www.nvidia.com/en-us/design-visualization/virtual-workstation/). The G series can also be used for training smaller models and for single-host inference. For these machine types, the GPU model is automatically attached to the instance. To optimize costs for workloads that don't require a full GPU, G4 machine types are available that have less than one GPU attached. These machine types come with 1/2, 1/4, or 1/8 of a standard GPU. |  For N1 general-purpose machine types, except for the N1 shared-core (`f1-micro` and `g1-small`), you can attach a select set of GPU models. Some of these GPU models also support NVIDIA RTX Virtual Workstations (vWS).  
For AI, ML, and HPC workloads, choose one of the following options:
     * To create A4X Max (GB300), A4X (GB200), A4 (B200) or A3 Ultra (H200) instances, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview) in the AI Hypercomputer documentation.
     * To create A3 (H100) instances that have 8 GPUs attached, see [Create an A3 Mega, A3 High, or A3 Edge instance with GPUDirect enabled](https://docs.cloud.google.com/compute/docs/gpus/gpudirect).
     * To create an A3 (less than 8 GPUs attached) or A2 (A100) instances, see [Create an A3 High or A2 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized).
| To create a G2 (L4) or G4 (RTX PRO 6000) instance, see [Create a G2 or G4 instance](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-g-series). | To create an N1 instance that has attached NVIDIA T4, P4, or V100 GPUs, see [Create an N1 instance that has attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-general-purpose).  
  2. For the instance to use the GPU, you need to [install the GPU driver on your instance](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu). If you enabled an NVIDIA RTX virtual workstation (formerly known as NVIDIA GRID), [install a driver for virtual workstation](https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers).




## What's next?

  * Learn more about [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

  * Learn more about the [features and limitations of using GPUs](https://docs.cloud.google.com/compute/docs/gpus/about-gpus).



  * Learn how to [view the actual and forecasted usage of your GPUs](https://docs.cloud.google.com/capacity-planner/docs/view-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
