---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview/
title: Deployment options overview \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:26.023643+00:00
---

# Deployment options overview  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Deployment options overview Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

To run artificial intelligence (AI), machine learning (ML), or high performance computing (HPC) workloads, you can deploy AI-optimized Compute Engine instances and clusters that use A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) machines. For more information about the features of these machines that enable you to run large-scale AI and ML clusters, see [Cluster management overview](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities).

**Note:** The Cluster Director and Cluster Toolkit guides only apply to the A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) machine types. We recommend that you consult the relevant documentation for your choice of machine type. To identify the compute instance and cluster creation guide for other machine types, see [Choose a deployment strategy](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy).

You can create A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) instances directly from Compute Engine, through managed services like Google Kubernetes Engine (GKE), or by using deployment tools like Cluster Toolkit.

For the most appropriate option to create your compute instances or clusters for your use case, choose one of the following:

**Option** | **Use case**  
---|---  
Cluster Director | You want a fully managed service that automates the setup and configuration of your Slurm clusters. Cluster Director helps you configure compute, networking, and storage resources for your clusters to maximize performance and minimize downtimes. To learn more, see [ Create a fully managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster).  
Cluster Toolkit | You want to use open-source software that simplifies the process for you to deploy both Slurm and GKE clusters. Cluster Toolkit is designed to be highly customizable and extensible. You can use blueprints to provision networking and storage resources. To learn more, see the following:

  * [Create a self-managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster)
  * [Create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)

  
GKE | You want maximum flexibility in configuring your GKE cluster based on the needs of your workload. To learn more, see the following:

  * [Create an AI-optimized GKE cluster that uses A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a4-a3-ultra)
  * [Create an AI-optimized GKE cluster that uses A3 Edge](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a3-edge)
  * [Create an AI-optimized GKE cluster that uses A2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-a2)
  * [Create an AI-optimized GKE cluster that uses G2 or G4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-g2-g4)
  * [Create an AI-optimized GKE cluster that uses N1](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-create-n1)

  
Use Compute Engine | You want full control of the infrastructure layer so that you can set up your own orchestrator. To learn more, see the following:

  * Create an AI-optimized instance 
    * [Create A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-instance)
    * [Create A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a4x)
    * [Create A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm)
    * [Create A3 Mega or A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a3-high-mega)
    * [Create A3 Edge](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a3-edge)
    * [Create A2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a2)
    * [Create G4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-g4)
    * [Create G2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-g2)
    * [Create N1](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-n1)
  * Create AI-optimized instances in bulk 
    * [Create A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-instances-in-bulk)
    * [Create A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-a4x)
    * [Create A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk)
    * [Create A3 Mega or A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-a3-high-mega)
    * [Create A3 Edge](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-a3-edge)
    * [Create A2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-a2)
    * [Create G4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-g4)
    * [Create G2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-g2)
    * [Create N1](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vms-in-bulk-n1)
  * Create an AI-optimized managed instance group (MIG) 
    * [Create A4X Max](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-a4xmax-mig)
    * [Create A4X](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4x)
    * [Create A4 or A3 Ultra](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a4-or-a3ultra)
    * [Create A3 Mega or A3 High](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a3-high-mega)
    * [Create A3 Edge](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a3-edge)
    * [Create A2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-a2)
    * [Create G4](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-g4)
    * [Create G2](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-g2)
    * [Create N1](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-mig-with-n1)

  
  
## What's next

  * Learn about the performance-optimized infrastructure of AI Hypercomputer: 
    * [About GPU accelerators](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus)
    * [Networking services](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-overview)
    * [Storage services](https://docs.cloud.google.com/ai-hypercomputer/docs/storage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
