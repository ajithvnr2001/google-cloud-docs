---
url: https://docs.cloud.google.com/cluster-director/docs/os-images/
title: Supported OS images for Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:09.722609+00:00
---

# Supported OS images for Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/os-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Supported OS images for Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the pre-configured, bootable operating system (OS) images that Cluster Director uses to deploy Compute Engine instances in your clusters.

The OS images that you can use in Cluster Director come with pre-configured machine learning (ML) frameworks and libraries. These frameworks and libraries remove the need for manual installation, as well as simplify model creation and training for large-scale workloads. By understanding the available OS images in Cluster Director and their lifecycle, you can choose the right OS image for your workload, keep your clusters secure, and prevent workload disruptions caused by obsolete software.

## Slurm OS images for Cluster Director

When you deploy a Slurm cluster, Cluster Director provides OS images with pre-configured ML frameworks and libraries for the nodes in your cluster. These OS images offer the following benefits:

  * The OS images provision every node in your cluster with a consistent software stack, which includes the required NVIDIA drivers and CUDA versions.

  * The OS images are extensions of the [Ubuntu LTS OS images](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_lts), and they include all necessary system software for cluster and workload management.




### Included software

The custom OS images for Cluster Director include the following software components by default:

  * **OS images:** the following table lists the supported image families and image versions for each machine series. If you don't specify the OS image when you create a nodeset, then Cluster Director uses the default image for that machine series.

Supported machine series | Operating system | NVIDIA driver and CUDA Toolkit | Slurm version | Image version  
---|---|---|---|---  
A4X or C4A | Ubuntu 24.04 LTS | Driver 595, CUDA 13 | 26.05 |  `projects/clusterdirector-public-images/global/images/family/a4x-ubuntu-2404-arm64-nvidia-595-slurm-2605-v20260903`  
A4X or C4A | Ubuntu 24.04 LTS | Driver 580, CUDA 13 | 25.05 |  `projects/clusterdirector-public-images/global/images/family/a4x-ubuntu-2404-arm64-nvidia-580-slurm-2505-v20251118`   
(default)   
A4 or A3 Ultra | Ubuntu 24.04 LTS | Driver 595, CUDA 13 | 26.05 |  `projects/clusterdirector-public-images/global/images/family/common-ubuntu-2404-amd64-nvidia-595-slurm-2605-v20260903`  
A4, A3 Ultra, or N2 | Ubuntu 22.04 LTS | Driver 580, CUDA 13 | 25.05 |  `projects/clusterdirector-public-images/global/images/family/common-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20251113`   
(default)   
A4, A3 Ultra, or N2 | Ubuntu 22.04 LTS | Driver 570, CUDA 12 | 25.05 |  `projects/clusterdirector-public-images/global/images/family/common-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20250918`  
A3 Mega | Ubuntu 24.04 LTS | Driver 595, CUDA 13 | 26.05 |  `projects/clusterdirector-public-images/global/images/family/a3-h100-ubuntu-2404-amd64-nvidia-595-slurm-2605-v20260903`  
A3 Mega | Ubuntu 22.04 LTS | Driver 580, CUDA 13 | 25.05 |  `projects/clusterdirector-public-images/global/images/family/a3-h100-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20260805`   
(default)   
A3 Mega | Ubuntu 22.04 LTS | Driver 580, CUDA 13 | 25.05 |  `projects/clusterdirector-public-images/global/images/family/a3m-ubuntu-2204-amd64-nvidia-580-slurm-2505-v20260714`  
A3 Mega | Ubuntu 22.04 LTS | Driver 570, CUDA 12 | 25.05 |  `projects/clusterdirector-public-images/global/images/family/a3m-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20251114`  
A3 Mega | Ubuntu 22.04 LTS | Driver 570, CUDA 12 | 25.05 |  `projects/clusterdirector-public-images/global/images/family/a3m-ubuntu-2204-amd64-nvidia-570-slurm-2505-v20250918`  
  * **Orchestration:** Slurm version 25.05 or 26.05, and their dependencies, such as [MariaDB](https://mariadb.org). For more information about version compatibility between compute nodes and the controller node in a cluster, see [Slurm controller versions in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/slurm-controller-versions).

  * **Containerization tools:** the NVIDIA enroot container runtime and NVIDIA pyxis, used for running containerized workloads on Slurm clusters.

  * **Drivers:** NVIDIA driver version 595 or 580 with CUDA Toolkit 13, or version 570 with CUDA Toolkit 12.

  * **Libraries:** libraries for GPUDirect RDMA, including `ibverbs-utils` and `rdma-core`.

  * **Parallel computing libraries:** [Open MPI](https://www.open-mpi.org/) and [PMIx](https://pmix.org/) for managing parallel processing tasks across the cluster.

  * **Google Cloud integrations:** the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent) for monitoring and logging, and Cloud Storage FUSE for accessing Cloud Storage buckets from the cluster nodes.




### Image family lifecycle

To help ensure that your clusters remain secure and compatible with the latest Google Cloud features, Cluster Director releases new image families approximately every six months. Each image family that Cluster Director supports goes through the following lifecycle:

  * **Supported** : for 12 months after the release date, the image family is fully supported. It receives critical security and bug fixes. We recommend that you use supported image families for all new deployments.

  * **Deprecated** : for approximately six months after the active phase ends, the image family is deprecated. You can still use the image family to create nodes in your cluster, but we don't recommend it as the image family no longer receives security patches.

  * **Obsolete** : after the deprecated phase ends, the image family becomes obsolete. You can no longer create nodes in your cluster by using this image family. Existing nodes continue to run, but they risk being incompatible with the cluster controller.

  * **Deleted** : three months after an image family becomes obsolete, the underlying Compute Engine image resource is permanently deleted. Running nodes that use that image family are unaffected.




For information about the exact end of support dates for an image family, see [Image family release notes](https://docs.cloud.google.com/cluster-director/docs/image-family-release-notes).

## What's next

  * [Supported networking services in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/networking)

  * [Try out Cluster Director](https://docs.cloud.google.com/cluster-director/docs/create/quickstart)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
