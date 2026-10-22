---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy/
title: Choose between general GPUs and clustered GPUs \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:49.428411+00:00
---

# Choose between general GPUs and clustered GPUs  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Choose between general GPUs and clustered GPUs Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document provides recommendations for the accelerators, consumption options, and deployment tools that are best suited for different artificial intelligence (AI), machine learning (ML), and high performance computing (HPC) workloads. Use this document to help you identify the best deployment for your workload.

For information and recommendations about infrastructure pillars for AI, ML, and HPC workloads, see the following documents:

  * [About GPU accelerators](https://docs.cloud.google.com/ai-hypercomputer/docs/understand-gpus)
  * [GPU networking overview](https://docs.cloud.google.com/ai-hypercomputer/docs/networking-overview)
  * [Storage services overview](https://docs.cloud.google.com/ai-hypercomputer/docs/storage)



## Workloads overview

AI Hypercomputer architecture supports the following use cases:

Workload | Description | Recommendation  
---|---|---  
**Pre-training foundation models** | This involves building a language model using a large dataset. The result of pre-training foundation models is a new model that is good at performing general tasks.  
Models are categorized based on their size as follows:  


  * **_Frontier model_** : ML models that span hundreds of billions to trillions of parameters or higher. These include large language models (LLMs) such as Gemini.
  * **_Large model_ :** ML models that span tens to hundreds of billions of parameters or higher.

| See [ recommendations for pre-training models](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy#pre-train)  
**Fine-tuning** | This involves taking a trained model and adapting it to perform specific tasks by using specialized data sets or other techniques. Fine-tuning is generally performed on large models. | See [ recommendations for fine-tuning models](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy#fine-tuning)  
**Inference or serving** | This involves taking a trained or fine-tuned model and making it available for consumption by users or applications.  
Inference workloads are categorized based on the size of the models as follows:  


  * **_Inference for foundation models across multiple hosts_** : performing inference with trained ML models that span hundreds of billions to trillions of parameters or higher. For these inference workloads the computational load is shared across multiple host machines.
  * **_Single-host foundation model inference_** : performing inference with trained ML models that span tens to hundreds of billions of parameters. For these inference workloads the computational load is confined to a single host machine.
  * **_Large model inference_ :** performing inference with trained or fine-tuned ML models that span tens to hundreds of billions of parameters.

| See [ recommendations for inference](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy#inference)  
**ML for small or medium-sized models** | This involves training and serving ML models that are smaller in size and complexity, typically for more specialized tasks. | See [ recommendations for ML for small or medium-sized models](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy#small-medium-ml)  
**HPC** | This is the practice of aggregating computing resources to gain performance greater than that of a single workstation, server, or computer. HPC is used to solve problems in academic research, science, design, simulation, and business intelligence. | See [ recommendations for HPC](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy#hpc)  
  
## Recommendations for pre-training models

To pre-train foundation models, large clusters of accelerators continuously read large volumes of data. These accelerators adjust weights through forward and backward passes to learn from the data. These training jobs run for weeks or even months at a time.

The following sections outline the accelerators and consumption options that we recommend you use to pre-train foundation models.

### Recommended accelerators

To pre-train foundation models on Google Cloud, we recommend that you use **A4X Max** (NVIDIA GB300), **A4X** (NVIDIA GB200), **A4** (NVIDIA B200), **A3 Ultra** (NVIDIA H200 141GB), **A3 Mega** (NVIDIA H100 80GB), or **A3 High** (NVIDIA H100 80GB) accelerator-optimized machine types, and use an orchestrator to deploy the cluster.

To deploy these clusters of accelerators, we also recommend that you use [Cluster Director](https://docs.cloud.google.com/cluster-director/docs/overview) or [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview). For more information, see the respective cluster deployment guide for your machine type of choice in the following table.

Workloads | Recommendations | Cluster deployment guide  
---|---|---  
| Machine type | Orchestrator |   
Pre-training foundation models | 

  * **A4X Max** (NVIDIA GB300)
  * **A4X** (NVIDIA GB200)
  * **A4** (NVIDIA B200)

| GKE | [Create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)  
Slurm | 

  * [Create a fully managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster)
  * [Create a self-managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster)

  
Large model training | **A3 Ultra** (NVIDIA H200 141GB) | GKE | [Create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)  
Slurm | 

  * [Create a fully managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster)
  * [Create a self-managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster)

  
Large model training | 

  * **A3 Mega** (NVIDIA H100 80GB)
  * **A3 High** (NVIDIA H100 80GB)

| GKE | [Maximize GPU network bandwidth in Standard mode clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx)  
Slurm | 

  * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)
  * [Deploy an A3 Mega Slurm cluster for ML training](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/deploy-a3-mega-cluster)
  * [Deploy an A3 High Slurm cluster](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a3-highgpu-8g)

  
  
### Recommended consumption option

For a high level of assurance in obtaining large clusters of accelerators, we recommend using a reservation. Specifically, to minimize the costs of reserved resources, we recommend that you request a reservation duration that's long enough to receive committed use discounts. For more information about consumption options, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

## Recommendations for fine-tuning models

To fine-tune large foundation models, smaller clusters of accelerators read moderate volumes of data. These accelerators adjust the model to perform specific tasks. These fine-tuning jobs run for days or even weeks.

The following sections outline the recommended accelerators and consumption option to use when fine-tuning models.

### Recommended accelerators

To fine-tune models on Google Cloud, we recommend that you use **A3 Ultra** (NVIDIA H200 141GB), **A3 Mega** (NVIDIA H100 80GB), or **A3 High** (NVIDIA H100 80GB) accelerator-optimized machine types, and use an orchestrator to deploy the cluster.

To deploy these clusters of accelerators, we also recommend that you use [Cluster Director](https://docs.cloud.google.com/cluster-director/docs/overview) or [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview). For more information, see the respective cluster deployment guide for your machine type of choice in the following table.

Workloads | Recommendations | Cluster deployment guide  
---|---|---  
| Machine type | Orchestrator |   
Fine-tuning large models | **A3 Ultra** (NVIDIA H200 141GB) | GKE | [Create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)  
Slurm | 

  * [Create a fully managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster)
  * [Create a self-managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster)

  
Fine-tuning large models | 

  * **A3 Mega** (NVIDIA H100 80GB)
  * **A3 High** (NVIDIA H100 80GB)

| GKE | [Maximize GPU network bandwidth in Standard mode clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx)  
Slurm | 

  * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)
  * [Deploy an A3 Mega Slurm cluster for ML training](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/deploy-a3-mega-cluster)
  * [Deploy an A3 High Slurm cluster](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a3-highgpu-8g)

  
  
### Recommended consumption option

For fine-tuning workloads, use a future reservation in calendar mode to provision resources. For more information about consumption options, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

## Recommendations for inference

The following sections outline the recommended accelerators and consumption options to use when performing inference.

### Recommended accelerators

The recommended accelerators for inference depend on whether you're performing multi-host frontier or large model inference, or single-host frontier inference.

#### Recommended accelerators (multi-host)

To perform multi-host frontier or large model inference on Google Cloud, use an **A4X Max** (NVIDIA GB300), **A4X** (NVIDIA GB200), **A4** (NVIDIA B200), **A3 Ultra** (NVIDIA H200 141GB), **A3 Mega** (NVIDIA H100 80GB), or **A3 High** (NVIDIA H100 80GB) accelerator-optimized machine types, and deploy the machine by using an orchestrator. To deploy these clusters of accelerators, we also recommend that you use [Cluster Director](https://docs.cloud.google.com/cluster-director/docs/overview) or [ Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview). The table provides links to cluster deployment guides for each recommended machine type.

Workloads | Recommendations | Cluster deployment guide  
---|---|---  
| Machine type | Orchestrator |   
Multi-host frontier inference | 

  * **A4X Max** (NVIDIA GB300)
  * **A4X** (NVIDIA GB200)
  * **A4** (NVIDIA B200)

| GKE | [Create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)  
Slurm | 

  * [Create a fully managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster)
  * [Create a self-managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster)

  
Large model inference | **A3 Ultra** (NVIDIA H200 141GB) | GKE | [Create an AI-optimized GKE cluster with Cluster Toolkit](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute)  
Slurm | 

  * [Create a fully managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster)
  * [Create a self-managed Slurm cluster for AI workloads](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-self-managed-slurm-cluster)

  
Large model inference | 

  * **A3 Mega** (NVIDIA H100 80GB)
  * **A3 High** (NVIDIA H100 80GB)

| GKE | [Maximize GPU network bandwidth in Standard mode clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx)  
Slurm | 

  * [Create an AI-optimized cluster based on a template](https://docs.cloud.google.com/cluster-director/docs/create/cluster-from-template)
  * [Deploy an A3 Mega Slurm cluster for ML training](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/slurm/deploy-a3-mega-cluster)
  * [Deploy an A3 High Slurm cluster](https://github.com/GoogleCloudPlatform/cluster-toolkit/tree/main/examples/machine-learning/a3-highgpu-8g)

  
  
#### Recommended accelerators (single host)

The table outlines the accelerators that we recommend you use to perform single-host frontier inference. The table provides links to VM deployment guides for each recommended machine type.

Workloads | Recommendations | VM deployment guide  
---|---|---  
| Machine type | Orchestrator |   
Single-host frontier and mainstream inference | 

  * **A4** (NVIDIA B200)
  * **A3 Ultra** (NVIDIA H200 141GB)

| N/A | [Create an A4 or A3 Ultra instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm)  
  
  * **A3 High** (NVIDIA H100 80GB)
  * **A3 Edge** (NVIDIA H100 80GB)

| [Create an A3 High or A3 Edge instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a3-high-mega)  
**A2** (NVIDIA A100) | [Create an A2 instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a2)  
**G4** (NVIDIA RTX PRO 6000) | [Create a G4 instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-g4)  
**G2** (NVIDIA L4) | [Create a G2 instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-g2)  
**N1** (NVIDIA T4 or V100) | [Create an N1 instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-n1)  
  
### Recommended consumption option

For inference, use either a long-running reservation or a future reservation in calendar mode. For more information about consumption options, see [Choose a consumption option](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).

## Recommendations for small or medium-sized models

For ML workloads that involve small to medium-sized models, achieving an optimal balance between price and performance is a primary consideration.

### Recommended accelerators

The following table outlines the recommended accelerators to use for small to medium-sized model ML workloads.

Workloads | Recommendations | VM deployment guide  
---|---|---  
| Machine type | Orchestrator |   
ML for small or medium-sized models | **A3 Edge** (NVIDIA H100 80GB) | N/A | [Create an A3 Edge instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a3-high-mega)  
**A2** (NVIDIA A100) | [Create an A2 instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-a2)  
**G4** (NVIDIA RTX PRO 6000) | [Create a G4 instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-g4)  
**G2** (NVIDIA L4) | [Create a G2 instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-g2)  
**N1** (NVIDIA T4 or V100) | [Create an N1 instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm-n1)  
  
## Recommendations for HPC

For HPC workloads, any [accelerator-optimized machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) or [compute-optimized machine series](https://docs.cloud.google.com/compute/docs/compute-optimized-machines) works well. If using an accelerator-optimized machine series, the best fit depends on the amount of computation that must be offloaded to the GPU. For a detailed list of recommendations for HPC workloads, see [Best practices for running HPC workloads](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/best-practices).

## Summary of recommendations

The following table summarizes the recommended accelerators and consumption options for each workload.

Resource | Recommendation  
---|---  
Model pre-training  
Machine family | Use one of the following accelerator-optimized machine types: **A4X Max** (NVIDIA GB300), **A4X** (NVIDIA GB200), **A4** (NVIDIA B200), **A3 Ultra** (NVIDIA H200 141GB), **A3 Mega** (NVIDIA H100 80GB), or **A3 High** (NVIDIA H100 80GB)  
Consumption option | 'Use standard future reservations  
Model fine-tuning  
Machine family | Use **A3 Ultra** (NVIDIA H200 141GB), **A3 Mega** (NVIDIA H100 80GB), or **A3 High** (NVIDIA H100 80GB) accelerator-optimized machine types  
Consumption option | 'Use standard future reservations  
Inference  
Machine family | Use one of the following machine types: **A4X Max** (NVIDIA GB300), **A4X** (NVIDIA GB200), **A4** (NVIDIA B200), **A3 Ultra** (NVIDIA H200 141GB), **A3 Mega** (NVIDIA H100 80GB), **A3 High** (NVIDIA H100 80GB), **A3 Edge** (NVIDIA H100 80GB), **A2** (NVIDIA A100), **G4** (NVIDIA RTX PRO 6000), **G2** (NVIDIA L4), or **N1** (NVIDIA T4 or V100)  
Consumption option | Use reservations, on-demand, or Spot  
ML for small or medium-sized models  
Machine family | Use one of the following machine types: **A3 Edge** (NVIDIA H100 80GB), **A2** (NVIDIA A100), **G4** (NVIDIA RTX PRO 6000), **G2** (NVIDIA L4), or **N1** (NVIDIA T4 or V100)  
Consumption option | Use on-demand, Spot, or standard reservations  
Storage | Use Cloud Storage FUSE  
HPC  
See [the summary section](https://docs.cloud.google.com/cluster-toolkit/docs/tutorials/best-practices#summary) of the best practices for running HPC workloads  
  
## What's next

  * Learn how to [Create an AI-optimized GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/gke-ai-hypercompute).
  * Learn how to [Create a fully managed Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-fully-managed-slurm-cluster).
  * Learn how to [Create an AI-optimized instance](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
