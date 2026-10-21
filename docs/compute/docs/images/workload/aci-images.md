---
url: https://docs.cloud.google.com/compute/docs/images/workload/aci-images/
title: Overview of Advanced Compute Images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:44.630394+00:00
---

# Overview of Advanced Compute Images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/workload/aci-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Overview of Advanced Compute Images Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Artificial intelligence (AI), machine learning (ML), and high performance computing (HPC) workloads often require you to create a custom image that includes additional software packages and is tuned for optimal performance. You can now use _Advanced Compute Images_ to set up an optimized environment for your AI/ML or HPC workloads.

Advanced Compute Images provide a standardized image stack for AI/ML and HPC infrastructure. These images can eliminate the need to manually build your own custom images for AI/ML and HPC workloads.

## Benefits

Advanced Compute Images provide the following benefits:

  * **Compute instances ready for AI/ML or HPC workloads by default**. There is no need to manually tune performance, manage instance reboots, install Slurm agents, or stay up to date with the latest Google Cloud updates for tightly coupled AI/ML or HPC workloads.
  * **Consistent, reproducible performance**. Image standardization gives you consistent, reproducible application-level performance.



## Features of Advanced Compute Images

Advanced Compute Images contain multiple layers of configurations to support running AI/ML and HPC workloads.

  * **Operating system configurations** : Includes disabling automatic updates, setting HPC-optimized ulimits, tuning kernel sysctl parameters, and configuring security settings like [SELinux](https://wikipedia.org/wiki/SELinux).
  * **Network tuning** : Contains the necessary scripts for network tuning, such as enabling multi-queue service.
  * **Google Cloud integration** : Installs and configures Google Cloud CLI and the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent).
  * **Container tools** : Installs and configures all container-related software, including: 
    * [Docker](https://github.com/Docker)
    * [NVIDIA Container Toolkit](https://github.com/NVIDIA/nvidia-container-toolkit) (version 1.19.0-1)
    * [NVIDIA Enroot](https://github.com/NVIDIA/enroot)
    * [NVIDIA Pyxis](https://github.com/NVIDIA/pyxis/)
  * **NVIDIA** : Installs the following tools: 
    * [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda/toolkit) version 13.0,
    * [NVIDIA Data Center GPU Manager (DCGM)](https://developer.nvidia.com/dcgm) version 4
    * [NVIDIA Fabric Manager](https://docs.nvidia.com/datacenter/tesla/fabric-manager-user-guide/index.html)
    * [NCCL/gIB plugin](https://docs.cloud.google.com/ai-hypercomputer/docs/nccl/overview)
  * **MPI** : Installs the Message Passing Interface (MPI) libraries. Installs Open MPI on both Ubuntu-based and Rocky Linux-based images. For Rocky Linux-based images, you can also install and configure the Intel MPI library using a pre-installed script:
        
        sudo google_install_intelmpi --impi_2021 --install_dir=PATH_INSTALL_MPI
        

  * **Slurm** : Installs the core components required to create a [Slurm](https://slurm.schedmd.com/overview.html) cluster node, including:

    * Slurm binaries (version 25.11)
    * [Munge](https://github.com/dun/munge/wiki) for authentication
    * [PMIx](https://github.com/openpmix/openpmix) for process management
    * [JSON Web Token (JWT)](https://wikipedia.org/wiki/JSON_Web_Token) library (`libjwt`)
  * **Filesystem clients** : Installs client-side tools for accessing various filesystems, such as Cloud Storage FUSE, NFS utilities (`nfs-utils`), and the Lustre client.

  * **Developer tools** : Installs common development and debugging tool chains and utilities, such as:

    * `gcc-toolset-12` or `gcc-toolset-11`
    * [htop](https://en.wikipedia.org/wiki/Htop)
    * `ltrace`
    * `strace`
    * [perf](https://wikipedia.org/wiki/Perf_\(Linux\))
    * [Valgrind](https://valgrind.org/docs/manual/quick-start.html)
  * **Environment management** : Installs and configures environment management tools, primarily [Lmod](https://lmod.readthedocs.io/en/latest/), and sets up the necessary profile scripts to make the module command available to users.

  * **RDMA** : Installs Remote Direct Memory Access (RDMA) drivers and packages on CPU (Rocky Linux-based) images, including:

    * `rdma-core` and development libraries
    * `libfabric`
    * `perftest`
    * `kmod-idpf-irdma` \- Intel Ethernet RDMA driver for supported compute-optimized machine types
    * `infiniband-diags`, `libibverbs`, and `librdmacm` utilities



## Supported hardware and image families

ACI supports two primary hardware platforms:

  * **CPU (HPC)** : support CPU workloads and have the following characteristics:

    * Are optimized for compute-intensive workloads
    * Support Rocky Linux 9
    * Come with RDMA drivers and utilities to support Cloud RDMA
    * Come with pre-integrated MPI libraries, including Open MPI and configurable Intel MPI
  * **GPU (AI/ML/HPC)** : support GPU workloads and have the following characteristics:

    * Are optimized for NVIDIA accelerators
    * Support Ubuntu LTS 22.04 and Ubuntu LTS 24.04
    * Come with pre-integrated CUDA and NVIDIA drivers
    * Include RDMA drivers and utilities to support MRDMA for GPU-to-GPU communication
    * Are suitable for AI, ML, or HPC workloads
    * Are the default images installed when you deploy Slurm cluster blueprints for A4X, A4, and A3 Ultra machine types in Cluster Toolkit

Hardware | OS | Orchestrator | Features | Architecture | Supported machine series | Image family  
---|---|---|---|---|---|---  
CPU | Rocky Linux 9 | none | 

  * RDMA
  * OpenMPI,IntelMPI

| AMD x86_64 | C2D, H3, H4D | `aci-cpu-rocky-linux-9-amd64`  
CPU | Rocky Linux 8 | none | 

  * RDMA
  * OpenMPI,IntelMPI

| AMD x86_64 | C2D, H3, H4D | `aci-cpu-rocky-linux-8-amd64`  
CPU | Rocky Linux 9 | Slurm 25.11 | 

  * RDMA
  * MPI

| AMD x86_64 | C2D, H3, H4D | `aci-cpu-rocky-linux-9-slurm-2511-amd64`  
GPU | Ubuntu LTS 24.04 | Slurm 25.11 | 

  * CUDA 13.0
  * NVIDIA 580

| AMD x86_64 | A3 Ultra, A4 | `aci-gpu-u2404-slurm-2511-cuda-130-nvidia-580-amd64`  
GPU | Ubuntu LTS 24.04 | Slurm 25.11 | 

  * CUDA 13.0
  * NVIDIA 580

| Arm64 | A4X | `aci-gpu-u2404-slurm-2511-cuda-130-nvidia-580-arm64`  
GPU | Ubuntu LTS 24.04 | Slurm 26.05 | 

  * CUDA 13.2
  * NVIDIA 595

| AMD x86_64 | A3 Ultra, A4 | `aci-gpu-u2404-slurm-2605-cuda-132-nvidia-595-amd64`  
GPU | Ubuntu LTS 24.04 | Slurm 26.05 | 

  * CUDA 13.2
  * NVIDIA 595

| Arm64 | A4X | `aci-gpu-u2404-slurm-2605-cuda-132-nvidia-595-arm64`  
GPU | Ubuntu LTS 24.04 | none | 

  * CUDA 13.0
  * NVIDIA 580

| AMD x86_64 | A3 Ultra, A4 | `aci-gpu-u2404-cuda-130-nvidia-580-amd64`  
GPU | Ubuntu LTS 22.04 | Slurm 25.11 | 

  * CUDA 13.0
  * NVIDIA 580

| AMD x86_64 | A3 Ultra, A4 | `aci-gpu-u2204-slurm-2511-cuda-130-nvidia-580-amd64`  
GPU | Ubuntu LTS 22.04 | none | 

  * CUDA 13.0
  * NVIDIA 580

| AMD x86_64 | A3 Ultra, A4 | `aci-gpu-u2204-cuda-130-nvidia-580-amd64`  
  
### Pre-installed packages (or RPMs)

Advanced Compute Images come with a variety of tools, libraries, drivers, and packages pre-installed. To see a list of what is installed for any image, refer to the manifest file for that image.

You can find the manifest file at `/usr/share/google/manifest.txt`.

## Image family lifecycle phases and support

All families of Advanced Compute Images follow a standardized lifecycle to ensure security, stability, and a predictable maintenance schedules. During each phase of the lifecycle, an image family has one of the following support statuses:

  * **Supported** : 
    * Receives critical security updates and bug fixes
    * Supported through Cloud Customer Care.
    * Can be used to create compute instances.
  * **Unsupported** : 
    * No longer receives critical security updates or bug fixes.
    * No new features.
    * Not supported through Cloud Customer Care.
    * Can't be used to create compute instances.



The lifecycle of an Advanced Compute Images family consists of four phases:

Lifecycle phase | Support status | Description and impact  
---|---|---  
**Active** | Supported | Recommended for new deployments. For 12 months after the release date, the image family is fully supported. Receives critical security updates and bug fixes.  
**Deprecated (EOS date)** | Unsupported | We recommend that you migrate to a supported image family. For approximately six months after the Active phase ends, the image family is deprecated. No new features or patches are released. Google Cloud console and Google Cloud CLI warnings appear when you create instances that use this image family.   
**Obsolete** | Unsupported | After the deprecated phase ends, the image family becomes obsolete. You can no longer create compute instances by using this image family. Existing compute instances continue to run, but risk incompatibility with the Slurm controller.   
**Deletion** | Unsupported | Three months after an image family becomes obsolete, the underlying Advanced Compute Images image resource is permanently deleted. Existing compute instances continue to run, but risk incompatibility with the Slurm controller and vulnerabilities.  
  
For information about the exact end of support dates for an image family, see Supported hardware and image families.

## Pricing

Advanced Compute Images are available at no additional cost. Because Advanced Compute Images run on Compute Engine, you might incur charges for Compute Engine resources such as vCPUs, GPUs, TPUs, disks, and memory. To learn more, see [Compute Engine pricing](https://docs.cloud.google.com/compute/vm-instance-pricing).

## What's next

  * [Create an instance with Advanced Compute Images](https://docs.cloud.google.com/compute/docs/instances/use-aci-images)
  * Learn how to deploy turnkey Slurm cluster blueprints with Advanced Compute Images:

    * [Create an A4X Slurm cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a4x-cluster)
    * [Create an A4 Slurm cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a4-cluster)
    * [Create an A3 Ultra Slurm cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/create-a3-ultra-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
