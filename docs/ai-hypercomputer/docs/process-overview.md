---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/process-overview/
title: Plan and create your AI infrastructure \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:08.037616+00:00
---

# Plan and create your AI infrastructure  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/process-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Plan and create your AI infrastructure Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document summarizes how you create a cluster for your AI workloads on AI Hypercomputer. Specifically, this document guides you through the process and choices to make when you start a cluster. As an alternative to manual evaluation, you can prompt Gemini in the Google Cloud console to compare consumption options for your workload and budget. For more information, see [Design AI infrastructure with Compute Advisor](https://docs.cloud.google.com/ai-hypercomputer/docs/design-with-gemini).

This document assumes that you are familiar with commonly used terminology for AI and ML workloads, such as model training and inference. It also assumes that you have identified the specific AI workload for which you need to determine the optimal machine type and capacity needs for your deployment—for example, foundation model pre-training, fine-tuning, or inference.

**Tip:** For a quick end-to-end tutorial that deploys an A4 machine type on Slurm, see instead [Create an AI-optimized Slurm cluster with an A4 machine type](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a-slurm-cluster-with-a4).

## Start a cluster

Starting a cluster involves the following steps:

  1. Determine your workload and choose a machine type
  2. Choose a consumption option and obtain capacity
  3. Choose a deployment option
  4. Choose an orchestrator
  5. Choose the operating system and cluster image
  6. Create your cluster
  7. Provision storage for your workload



### Determine your workload and choose a machine type

Select a machine type for your AI workload. AI Hypercomputer supports cluster creation for both [clustered GPUs and general GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-infrastructure).

To help you choose, determine your workload requirements and match them with the recommended machine type and GPU type:

  * Clustered GPUs: best for large-scale, high-performance workloads such as pre-training foundation models, fine-tuning large models, and inference across multiple hosts.
  * General GPUs: best for mainstream inference and serving, retrieval-augmented generation (RAG), and cost-effective small-to-medium model training and fine-tuning.



To match your workload to the recommended machine type, use this table:

GPU type | Workload or use case | Recommended machine types  
---|---|---  
**Clustered GPU** | Pre-training foundation models and inference across multiple hosts | **A4X Max** (NVIDIA GB300)*, **A4X** (NVIDIA GB200)*  
Large model training, fine-tuning, and inference | **A4** (NVIDIA B200), **A3 Ultra** (NVIDIA H200 141GB)  
Mainstream model inference and fine-tuning | **A3 Mega** (NVIDIA H100 80GB), **A3 High** (NVIDIA H100 80GB)  
**General GPU** | High-throughput edge serving and inference | **A3 Edge** (NVIDIA H100 80GB)  
High-performance single-node serving and small-scale fine-tuning | **A2** (NVIDIA A100)  
Cost-optimized entry-level inference | **G4** (NVIDIA RTX PRO 6000), **N1** (NVIDIA T4 or V100)  
Mainstream inference, RAG, and small-to-medium model training | **G2** (NVIDIA L4)  
**Caution:** *The [Compute Engine Service Level Agreement (SLA)](https://cloud.google.com/compute/sla) doesn't apply to the A4X Max and A4X machine series.

For detailed information about each machine series, see [About GPU accelerators](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus).

### Choose a consumption option and obtain capacity

Select a [consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models) for your GPU resources based on your chosen machine type and whether you use General GPUs or Clustered GPUs.

#### Consumption options for general GPUs

Consumption option | Available for | Best for | How to request  
---|---|---|---  
**On-demand** | All [general GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus). | Workloads that don't require assured capacity. | Create a compute instance or cluster and specify the standard provisioning model. For instructions, see [Create VM instances](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).  
  
**Tip:** To increase your chances of obtaining general GPU capacity, use Flex-start or Spot.  
**Standard reservations and standard future reservations** | All [general GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus). | Workloads that require assured capacity either immediately (standard reservations) or for a specific future date (standard future reservations). | Create an on-demand reservation or a future reservation request. For instructions, see [Reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).  
**Flex-start** | All [GPU machine types](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus) except for A4X Max and A4X. | Workloads that require short-lived, dense clusters that last up to seven days. Offers dense resource allocation and up to a 53% discount on supported machine types; otherwise, standard on-demand rates apply. | Create a request by using Compute Engine, Cluster Director, Cluster Toolkit, or GKE. Resources are provisioned as soon as they become available (start time isn't immediate). For instructions, see [Obtain capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity).  
**Spot** | All [GPU machine types](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus) except A4X Max and A4X. | Workloads that are fault-tolerant, batch, or short-lived. Offers the deepest discount (between 61% and 90%), but compute resources can be preempted at any time. | Create instances or node pools immediately by using the Spot provisioning model. For instructions, see [Obtain capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity).  
  
#### Consumption options for clustered GPUs

Consumption option | Available for | Best for | How to request  
---|---|---|---  
**Future reservations for capacity blocks** | All [clustered GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus) and A3 Edge machine types. | Workloads that require stability for an extended period of time, such as pre-training foundation models or foundation model inference across multiple hosts. This reservation method offers dense resource allocation and an optional Hyperdisk pool, as well as discounts for vCPUs, memory, GPUs, Local SSD disks, and Hyperdisk pools if you reserve resources for 365 days or more. | Request resources through your Google account team for a future date and time, and for a duration of 90 days or more.  
**Future reservations in calendar mode** | All [clustered GPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus) except for A4X Max and A4X. | Workloads that run for up to 90 days and require stability, such as pre-training or fine-tuning models. Offers dense resource allocation and up to a 53% discount. | Create a self-service reservation request for a future date and time; Google Cloud must approve the request. For instructions, see [Reserve capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/reserve-capacity).  
**Flex-start** | All [GPU machine types](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus) except for A4X Max and A4X. | Workloads that require short-lived, dense clusters that last up to seven days. Offers dense resource allocation and up to a 53% discount on supported machine types; otherwise, standard on-demand rates apply. | Create a request by using Compute Engine, Cluster Director, Cluster Toolkit, or GKE. Resources are provisioned as soon as they become available (start time isn't immediate). For instructions, see [Obtain capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity).  
**Spot** | All [GPU machine types](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus) except A4X Max and A4X. | Workloads that are fault-tolerant, batch, or short-lived. Offers the deepest discount (between 61% and 90%), but compute resources can be preempted at any time. | Create instances or node pools immediately by using the Spot provisioning model. For instructions, see [Obtain capacity](https://docs.cloud.google.com/ai-hypercomputer/docs/obtain-capacity).  
  
### Choose a deployment option

Depending on the level of control that you need over your cluster deployment, choose between the following options:

  * **Highly managed deployment:** managed services automate the setup, orchestration, and configuration of your compute, networking, and storage resources.
  * **Less managed, more control deployment:** you manually create and manage your VMs, custom environments, and orchestration layers.



#### Highly managed

Highly managed deployment options automate the setup and orchestration of your compute, networking, and storage resources, which reduces the operational overhead of cluster management. To deploy and configure your infrastructure, use Cluster Director, Cluster Toolkit, or GKE.

  * [**Cluster Director**](https://docs.cloud.google.com/cluster-director/docs/overview): a Google Cloud product that automates the complex setup and configuration of clusters, helping you configure compute, networking, and storage resources for your clusters to maximize performance and minimize downtimes. Cluster Director is designed for IT administrators and AI researchers who want to avoid the overhead of managing a cluster, and instead focus on running their workloads.

  * [**Cluster Toolkit**](https://docs.cloud.google.com/cluster-toolkit/docs/overview): an open source tool offered by Google that simplifies cluster configuration and deployment for GKE or Compute Engine. You use predefined blueprints to deploy common configurations, such as A4 machine types with Slurm. You can modify blueprints to customize deployments and your software stack.

  * [**GKE**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview): a managed Kubernetes service and open source container orchestration platform. GKE offers features like autoscaling and high availability. It's also able to orchestrate containerized applications, support specialized hardware, and is compatible with the Google Cloud ecosystem, making it well-suited for deploying and managing AI or ML workloads. You can deploy GKE clusters by using GKE directly or by using Cluster Toolkit.




#### Less managed, more control

For more granular control over your clusters and the software installed on them, create a Compute Engine cluster by using managed Compute Engine instance groups (MIGs) or by creating instances in bulk. Then, manually install any key software you need on the instances.

### Choose an orchestrator

An orchestrator automates the management of your clusters. With an orchestrator, you don't have to manage each compute instance in the cluster. An orchestrator, such as Slurm or GKE, handles tasks like job queuing, resource allocation, autoscaling (in the case of GKE), and other day-to-day cluster management tasks.

  * **Slurm** : Slurm is an open source orchestrator commonly used for HPC, AI, or ML workloads. For a managed Slurm experience, you can use Cluster Director. To use Slurm natively, you can use Cluster Toolkit (which offers cluster blueprints that automatically install Slurm on your clusters), or you can manually install Slurm on a Compute Engine cluster.

  * **GKE** : GKE is a managed service built on top of Kubernetes, an open-source container orchestration platform. GKE is ideal for deploying and managing AI or ML workloads, because of its ability to orchestrate containerized applications, its support of specialized hardware, and its place in the Google Cloud ecosystem. You can deploy GKE clusters by using GKE directly or by using Cluster Toolkit.

  * **Bring your own orchestrator** : to use other orchestrators, use Compute Engine clusters. Creating a Compute Engine cluster is the least managed option offered on Google Cloud. This choice means that you're responsible for setting up, maintaining, and updating your instances.




### Choose the operating system image

The image that you should use depends on which GPU infrastructure you're using (clustered GPUs or general GPUs) and how you plan to deploy your clusters (GKE, Slurm, or Compute Engine). For GKE clusters, use Container-Optimized OS. For Compute Engine and Slurm clusters, select an operating system image optimized for accelerators, such as GPUs. In addition, you can select a Deep Learning Software Layer (DLSL) container image for your workload.

For detailed information, review [AI Hypercomputer images](https://docs.cloud.google.com/ai-hypercomputer/docs/software-stack).

#### Images for GKE clusters

To create GKE clusters, use the default container OS images for both Standard and Autopilot modes. However, in Standard mode, you can also choose to use other available images, like Ubuntu.

If you use Cluster Toolkit to deploy your cluster, then you can only use container OS images, as these are the images built into the cluster blueprints. For more information about each node image, see [Node images](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images) in the GKE documentation.

GKE also offers Deep Learning Software Layer (DLSL) container images that install packages like NVIDIA CUDA, and NCCL, as well as ML frameworks like PyTorch, providing a ready-to-use environment for deep learning workloads. These prebuilt DLSL container images are tested and verified to work seamlessly on GKE clusters.

#### OS images for Compute Engine clusters

AI Hypercomputer offers images optimized for running AI and ML workloads by using Compute Engine. Choose the OS you are most familiar with:

  * Rocky Linux 9 accelerator
  * Rocky Linux 8 accelerator
  * Ubuntu 24.04 LTS accelerator
  * Ubuntu 22.04 LTS accelerator



If you use Cluster Toolkit, then these accelerator images are already bundled into Cluster Toolkit blueprints, because Cluster Toolkit creates custom images that extend the Ubuntu LTS Accelerator OS images.

For more information about each OS image, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) in the Compute Engine documentation.

### Create your cluster

After you review the cluster creation process and make preliminary decisions for your workload, create your cluster by using one of these options:

  * Create a GKE cluster: 
    * [Create a GKE cluster by using Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)
    * [Create a custom GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra)
  * Create a Slurm cluster: 
    * [Create a fully managed cluster by using Cluster Director](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster)
    * [Create a self-managed cluster by using Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster)
  * [Create VM instances (single, bulk, or MIGs)](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview)



### Provision storage for your workload

Choose a [storage service](https://docs.cloud.google.com/ai-hypercomputer/docs/storage) to provision, based on performance, cost, and storage architecture requirements.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
