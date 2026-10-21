---
url: https://docs.cloud.google.com/compute/docs/images/workload/hpc-vm-images/
title: Overview of HPC-ready VM images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:46.647737+00:00
---

# Overview of HPC-ready VM images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/workload/hpc-vm-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Overview of HPC-ready VM images Stay organized with collections  Save and categorize content based on your preferences. 

Tightly coupled high performance computing (HPC) workloads often use the Message Passing Interface (MPI) to communicate between processes and Compute Engine instances. However, the process of building your own OS image that is tuned for optimal MPI performance requires systems expertise, Google Cloud knowledge, and extra time for maintenance. To quickly set up an optimized environment for your HPC workloads, use an _HPC VM image_.

An HPC VM image is based on Rocky Linux 8 or Rocky Linux 9, and is optimized for tightly-coupled HPC workloads. The image includes pre-configured kernel and network tuning parameters required to create compute instances that achieve optimal MPI performance on Google Cloud.

For best results, deploy the HPC VM image on a machine type from the [compute-optimized machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines). These machine types are designed for tightly-coupled HPC applications. To use Cloud RDMA with H4D, you must use version 20250917 or later of the HPC VM Rocky 8 image.

You can create an HPC VM instance by using any of the methods available to create a compute instance. You can also use [SchedMD's Slurm workload manager](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/slurm-cluster), to deploy an HPC cluster. Slurm support isn't yet available for HPC VM images based on Rocky Linux 9.

## Benefits

The HPC VM image provides the following benefits:

  1. **Compute instances pre-configured for HPC workloads**. There is no need to manually tune performance, manage compute instance reboots, or stay up to date with the latest Google Cloud updates for tightly-coupled HPC workloads.
  2. **Networking optimizations for tightly-coupled workloads**. Optimizations that reduce latency for small messages are included. These optimizations benefit applications that are heavily dependent on point-to-point and collective communications. If using the H4D machine series, the HPC VM Rocky 8 image contains the necessary Cloud RDMA drivers.
  3. **Compute optimizations for HPC workloads**. Optimizations that reduce system jitter are included, which makes single-node high performance more predictable.
  4. **Consistent, reproducible performance**. OS image standardization gives you consistent, reproducible application-level performance.
  5. **Improved application compatibility**. Alignment with the node-level requirements of the [Intel HPC platform specification](https://www.intel.com/content/www/us/en/high-performance-computing/hpc-platform-specification.html) enables a high degree of interoperability between systems.



## HPC VM image features

The HPC VM image offers several features that are designed to optimize performance for high performance computing (HPC) workloads:

  * Automatic updates disabled
  * MPI collective tunings
  * Pre-installed RPMs



### Automatic updates disabled

Automatic updates can have a negative impact on the performance of HPC workloads. Disable automatic updates for HPC VM images by setting the `google_disable_automatic_updates` metadata entry to `TRUE` during instance creation. How you set this metadata entry during instance creation depends on the tool that you use to create the instance.

For example, when you use the [`gcloud compute instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) command to create a compute instance, provide the [`--metadata`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--metadata) argument. For more information, see [About VM metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).

The `google_disable_automatic_updates` metadata entry is available as follows:

  * **HPC VM Rocky 9 images** : all versions.
  * **HPC VM Rocky 8 images** : only in images built on or after July 12, 2024. The build date (formatted as `YYYYMMDD`) is used as the version number at the end of image names. For example, an HPC VM Rocky 8 image built on the 21st of July, 2025 has the name `hpc-rocky-linux-8-v20250721`.

**Important:** If you disable automatic updates, then VM Manager can cause performance of HPC workloads to degrade. VM Manager consumes CPU and network resources at regular intervals when it checks for updates. A workaround is to [disable the OS Config agent](https://docs.cloud.google.com/compute/vm-manager/docs/setup#disable-agent).

If you disable automatic updates on your H4D instances, then you should regularly run the `dnf update` command on the instance to keep the Cloud RDMA driver up to date.

### Intel MPI library

Google recommends that you use the `google_install_intelmpi` script to install the message passing interface (MPI) library before running MPI jobs on Google Cloud. For more information, see [Use Intel MPI 2021](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm#use-mpi-2021).

### Pre-installed RPMs

The HPC VM image comes with the following RPM packages pre-installed:

  * `gcc-gfortran`
  * `gcc-toolset-12`
  * `Lmod`
  * `dkms`
  * `htop`
  * `hwloc`
  * `hwloc-devel`
  * `infiniband-diags`
  * `kernel-devel`
  * `kmod-idpf-irdma`
  * `libfabric`
  * `librdmacm-utils`
  * `libibverbs-utils`
  * `libXt`
  * `ltrace`
  * `nfs-utils`
  * `numactl`
  * `numactl-devel`
  * `papi`
  * `pciutils`
  * `pdsh`
  * `perf`
  * `perftest`
  * `rdma-core`
  * `redhat-lsb-core` (HPC VM Rocky 8 only)
  * `redhat-lsb-cxx` (HPC VM Rocky 8 only)
  * `rsh`
  * `screen`
  * `strace`
  * `wget`
  * `zsh`
  * "Development Tools" package group



## Pricing

The HPC VM image is available at no additional cost. Because the HPC VM image runs on Compute Engine, you might incur charges for Compute Engine resources such as vCPUs, disks, and memory. To learn more, see [Compute Engine pricing](https://cloud.google.com/compute/vm-instance-pricing).

## What's next

  * Learn how to [Create an HPC-ready instance](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm).
  * Learn about [Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images) for HPC workloads.
  * Review the [best practices for running HPC workloads](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/best-practices).
  * Learn how to [set up and scale MPI applications on H4D VMs with Cloud RDMA](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application) on Google Cloud.
  * Learn how to [create H4D HPC clusters with enhanced cluster management capabilities](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters).
  * If you have feedback or require support, then send an email at [hpc-image-feedback@google.com](mailto:hpc-image-feedback@google.com).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
