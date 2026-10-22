---
url: https://docs.cloud.google.com/batch/docs/vm-os-environment-overview/
title: Overview of the OS environment for a job's VMs \u00a0|\u00a0 Batch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:26.333112+00:00
---

# Overview of the OS environment for a job's VMs  |  Batch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/batch/docs/vm-os-environment-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Batch ](https://docs.cloud.google.com/batch/docs)
  * [ Guides ](https://docs.cloud.google.com/batch/docs/get-started)



Send feedback 

#  Overview of the OS environment for a job's VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains concepts for the operating system (OS) environment—the boot disks and OS image—for the Compute Engine virtual machine (VM) instances that run Batch jobs.

A job is executed by running the instructions on the boot disk of each of its VMs. Each boot disk contains a bootloader, file system, and OS. You can optionally configure the VM OS environment for a job by doing one of the following:

  * To configure only the software on the boot disks, specify the job's VM OS image.
  * To configure any properties of the boot disk—including the VM OS image, disk size, and/or disk type—customize the job's boot disks.



The following sections describe when to configure the OS environment, the default OS environment, VM OS image options, and boot disk options.

## When to configure the OS environment

Review this section to determine whether to configure the VM OS image and/or boot disks when you create a job or use the default configuration.

Configure the VM OS image for a job in the following cases:

  * If the trusted images (`compute.trustedImageProjects`) policy constraint prevents you from creating a job with the default VM OS image.

**Tip:** If you aren't sure which policy constraints have been enabled for your project, folder, or organization, [view your organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

For more information about the trusted images policy constraint, see [Control access to the VM OS images for Batch](https://docs.cloud.google.com/batch/docs/control-access-vm-os-images).

  * If you prefer not to or cannot use the default VM OS image for your job. For example, if the runnables that you've defined for a job require an application that is not supported by the default image, you might be able to specify a different public VM OS image. Alternatively, if you want to preinstall an application that is required for your job to help reduce runtime, you might want to create and specify a custom image.




Configure the boot disk for a job in the following cases:

  * If you prefer not to or cannot use the default boot disk for your job. For example, if the runnables or VM OS image that you've defined for a job require additional storage space on the boot disk, then you might need to customize the boot disk for a job to increase its size.



If you are still unsure if your job requires you to configure the VM OS image and/or boot disks, you can review the following section to understand the default configuration. Additionally, you might also just try to create and run the job with the default configuration. If the job fails with the default configuration, you can try to determine if the issue was caused by the VM OS image or boot disk by [troubleshooting](https://docs.cloud.google.com/batch/docs/troubleshooting).

Otherwise, if you don't need and don't want to configure the VM OS image and/or boot disk for a job, leave these properties undefined to use the default configuration.

## Default OS environment

Review this section to understand the default configuration for a job's VM OS image and boot disks. For example, you might use the default configuration as a reference when determining how you want to configure the OS environment for a job.

When you create a job and don't define the VM OS image, the job defaults to using one of the following VM OS images:

  * If the job only has container runnables, the job uses the latest version of the Batch Container-Optimized OS (COS) image.
  * Otherwise, the job uses the latest version of the Batch Debian image.



When you create a job and don't define the other properties of the boot disks, the job defaults to using the following options:

  * [Persistent Disk type](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types): the default Persistent Disk type for boot disks is `pd-balanced`.

  * size: the default size for each VM's boot disk is determined by the following formula for \\({defaultBootDiskSize}\\). Additionally, the default size is rounded to be at least 30 GB and at most 10,000 GB.

\\[{defaultBootDiskSize}={reservedSize}+({taskSize}*{parallelTasksPerVm})\\]

This formula has the following values:

    * \\({reservedSize}\\): the reserved size in GB for required software for the VM, such as the VM OS image. For the default boot disk size, Batch reserves 10 GB.

    * \\({taskSize}\\): the boot disk size for each task in GB, which is is determined by converting the units of the [boot disk size per task (`bootDiskMib`) field](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#ComputeResource).

    * \\({parallelTasksPerVM}\\): the maximum number of tasks that can run on a VM simultaneously. For more information, see the [formula for \\({parallelTasksPerVM}\\)](https://docs.cloud.google.com/batch/docs/create-run-job#parallel-tasks-per-vm).

  * [interface](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#choose_an_interface): the interface is automatically selected as either [NVMe](http://wikipedia.org/wiki/NVM_Express) or [SCSI](http://wikipedia.org/wiki/SCSI) depending on the [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) of your job's VMs. You can optionally specify a machine type when you [define the type of resources for a job to use](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#instancepolicyortemplate). For the default interface of each machine type, see [Storage interface types](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#choose_an_interface) in the Compute Engine documentation.

**Note:** Unlike the other properties in this list, you cannot directly choose the interface of a persistent disk. However, the interface determines the required drivers, which you might need to consider if you specify your VM OS image. For more information, see Restrictions for VM OS images in this document.



## VM OS image options

The following sections describe the VM OS image options for Batch, including all the types of VM OS images that Batch jobs can support and the restrictions for the supported VM OS images. When you [specify the VM OS image for a job](https://docs.cloud.google.com/batch/docs/specify-vm-os-image), you can specify an image name or image family for any of the supported VM OS images that are allowed by the restrictions.

### Supported VM OS images

Batch jobs can support the following types of VM OS images:

  * **Public images:** images that are provided and maintained by Google, open source communities, and third-party vendors. Specifically, Batch jobs can use public images from Batch or Compute Engine.

    * **Batch images:** images that are provided and maintained by Batch based on Compute Engine OSes, stored in the `batch-custom-image` image project, and are recommended for Batch jobs.

Batch images are available in the following OSes. When you view image families and image names from Batch, the OS is indicated by the corresponding prefix.

      * **Batch Debian (`batch-debian` prefix):** an OS based on [Debian images from Compute Engine](https://docs.cloud.google.com/compute/docs/images/os-details#debian) that is optimized for Batch jobs. This OS is the default for jobs with any script runnables.

      * **Batch Container-Optimized OS (`batch-cos` prefix):** an OS based on [Container-Optimized OS images from Compute Engine](https://docs.cloud.google.com/compute/docs/images/os-details#container-optimized_os_cos) that is optimized for Batch jobs with containers. This OS is the default for jobs with only container runnables.

      * **Batch High-Performance Computing (HPC) Rocky Linux (`batch-hpc-rocky` prefix):** an OS based on [HPC Rocky Linux images from Compute Engine](https://docs.cloud.google.com/compute/docs/images/workload/hpc-vm-images) that is optimized for Batch jobs with HPC workloads.

To see the specific image names and families from Batch that you can specify for a job, follow the steps to [view VM OS images from Batch](https://docs.cloud.google.com/batch/docs/view-os-images).

    * **Compute Engine images:** public images available on Compute Engine, which are described on the [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) page in the Compute Engine documentation.

Batch only supports [generally available (GA)](https://cloud.google.com/products#product-launch-stages) Compute Engine images from the following OSes:

      * [Debian](https://www.debian.org/)
      * [Rocky Linux](https://rockylinux.org/)
**Important:** Due to a known issue, some Compute Engine images are causing jobs to fail. You might resolve this issue by using a newer image version. For more information, see [Jobs might fail when specifying Compute Engine (or custom) VM OS images with outdated kernels](https://docs.cloud.google.com/batch/docs/known-issues#jobs-fail-specify-compute-images-outdated-kernels).
  * **Custom images:** images that you create, own, and control access to by using Compute Engine. Learn more about [custom images](https://docs.cloud.google.com/compute/docs/images/building-custom-os) in the Compute Engine documentation.

**Important** : Custom images can be used with Batch but might not be supported. If you want to use a custom image with Batch, building your custom image on top of a public image that Batch supports is recommended.

To learn how to build an image that is compatible with Batch for various OSes, see the [ `build-custom-image` samples on GitHub](https://github.com/GoogleCloudPlatform/batch-samples/tree/main/build-custom-image).




### Restrictions for VM OS images

The supported VM OS images that a job can specify are subject to the following restrictions:

  * Batch images that are marked as deprecated might not be supported. The minimum supported lifetime for Batch images is the earliest of the following dates:

    * **60 days after the image's starting date.** The starting date of a Batch image is indicated in the image name—for example, the `batch-cos-stable-official-20230719-00-p00` image is from July 19, 2023 (`20230719`).
    * **The date that the base Compute Engine OS version is deprecated.** The date that each Compute Engine OS version is deprecated is listed on the [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) page in the Compute Engine documentation.
  * Certain job configurations require external access for the image. Specifically, when a job [does not have external access](https://docs.cloud.google.com/batch/docs/job-without-external-access) and does not allow access through Cloud NAT or Private Google Access, only the following images are supported:

    * For jobs that use GPU(s) and only container runnable(s), only the default image (the latest Batch Container-Optimized OS image) is supported.
    * Otherwise, jobs only support Batch images.
  * If the trusted images policy constraint is enabled, you cannot use _any_ VM OS images that the trusted image policy does not allow.

An administrator for your project, folder, or organization can optionally configure the trusted images policy constraint to restrict the VM OS images that can be used to create boot disks. For example, the trusted images policy constraint can be used to require users to create VMs that contain approved software that meets your policy or security requirements. For more information, see [Control access to VM OS images for Batch](https://docs.cloud.google.com/batch/docs/control-access-vm-os-images).

  * The VM OS image for your job must have the drivers for the interface of its boot disks and any [persistent disk storage volumes](https://docs.cloud.google.com/batch/docs/create-run-job-storage#use-persistent-disk) installed. Most public images automatically install both NVMe and SCSI drivers, including all Batch images.

You cannot configure the interface of persistent disks, so the VM OS image requires the drivers for the default interface.

  * If a job specifies any VM OS image that is neither a Batch image nor a custom image based on a Batch image, Batch installs required packages on the job's VMs after they start. These required packages can vary for different job configurations and change over time, and they are required for Batch to run the job.




## Boot disk options

This section describes the options for the type and size of boot disks for Batch. When you [customize the boot disks for a job](https://docs.cloud.google.com/batch/docs/create-run-job-custom-boot-disks), you can specify the VM OS image, type, and/or size. For information about specifying the VM OS image, see VM OS image options in this document instead.

For boot disk type, Batch supports all the [Persistent Disk types](https://docs.cloud.google.com/compute/docs/disks/persistent-disks#disk-types) in the Compute Engine documentation.

For boot disk size, Batch supports all sizes and increments for persistent disks in the Compute Engine documentation that meet the following requirements:

  * For Batch jobs, the minimum boot disk size is 30 GB.

  * For a Batch job to run properly, the boot disk size must be big enough to allocate the job's VM OS image and the tasks that run on each VM. For example, see the formula for the default boot disk size in this document.




## What's next

  * Learn more about the OS environment for a job: 
    * [View VM OS images for Batch](https://docs.cloud.google.com/batch/docs/view-os-images)
    * [Control access to the VM OS images for Batch](https://docs.cloud.google.com/batch/docs/control-access-vm-os-images)
    * [Specify the VM OS image for a job](https://docs.cloud.google.com/batch/docs/specify-vm-os-image)
    * [Customize the boot disks for a job](https://docs.cloud.google.com/batch/docs/create-run-job-custom-boot-disks)
  * Alternatively, to create a job that uses default OS environment, see [Create and run a basic job](https://docs.cloud.google.com/batch/docs/create-run-basic-job).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
