---
url: https://docs.cloud.google.com/compute/docs/gpus/overview/
title: About GPUs on Google Cloud \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:17.576327+00:00
---

# About GPUs on Google Cloud  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About GPUs on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud is focused on delivering world-class artificial intelligence (AI) infrastructure to power your most demanding GPU-accelerated workloads across a wide range of segments. You can use GPUs on Google Cloud to run AI, machine learning (ML), scientific, analytics, engineering, consumer, and enterprise applications.

Through our partnership with NVIDIA, Google Cloud delivers the latest GPUs while optimizing the software stack with a wide array of storage and networking options. For a full list of GPUs available, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

The following sections outline the benefits of GPUs on Google Cloud.

## GPU-accelerated VMs

On Google Cloud, you can access and provision GPUs in the way that best suits your needs. A specialized [accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) is available, with pre-attached GPUs and networking capabilities that are ideal for maximizing performance. These are available in the A4X Max, A4X, A4, A3, A2, G4, and G2 machine series.

## Multiple provisioning options

You can provision clusters by using the accelerator-optimized machine family with any of the following open-source or Google Cloud products.

### Vertex AI

Vertex AI is a fully-managed machine learning (ML) platform that you can use to train and deploy ML models and AI applications. In Vertex AI applications, you can use GPU-accelerated VMs to improve performance in the following ways:

  * [Use GPU-enabled VMs](https://docs.cloud.google.com/vertex-ai/docs/training/configure-compute) in custom training GKE worker pools.
  * Use [open source LLM models from the Vertex AI Model Garden](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/open-models/use-open-models).
  * Reduce [prediction](https://docs.cloud.google.com/vertex-ai/docs/predictions/configure-compute#gpus) latency.
  * Improve performance of [Vertex AI Workbench](https://docs.cloud.google.com/vertex-ai/docs/workbench/instances/change-machine-type) notebook code.
  * Improve performance of a [Colab Enterprise runtime](https://docs.cloud.google.com/colab/docs/create-runtime-template).



### AI Hypercomputer

AI Hypercomputer is a supercomputing system that is optimized to support your artificial intelligence (AI) and machine learning (ML) workloads. It's an integrated system of performance-optimized hardware, open software, ML frameworks, and flexible consumption models. AI Hypercomputer features and services that are designed to let you deploy and manage large numbers, up to tens of thousands, of accelerator and networking resources that function as a single homogeneous unit. This option is ideal for creating a densely allocated, performance-optimized infrastructure that has integrations for Google Kubernetes Engine (GKE) and Slurm schedulers. For more information, see the [AI Hypercomputer overview](https://docs.cloud.google.com/ai-hypercomputer/docs/overview).

To get started with Cluster Director, see [Choose a deployment strategy](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy).

### Compute Engine

You can also create and manage individual VMs or small clusters of VMs with attached GPUs on Compute Engine. This method is mostly used for running graphics-intensive workloads, simulation workloads, or small-scale ML model training.

The following table shows the methods that you can use to create VMs that have GPUs attached:

**Deployment option** | **Deployment guides**  
---|---  
Create a VM for serving and single node workloads | [Create an A3 Edge or A3 High VM](https://docs.cloud.google.com/compute/docs/gpus/gpudirect)  
Create managed instance groups (MIGs)  
  
This option uses the [ Dynamic Workload Scheduler (DWS)](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler). | [Create a MIG with GPU VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms)  
Create VMs in bulk | [Create a group of GPU VMs in bulk](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-bulk)  
Create a single VM | [Create a single GPU VM](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus)  
Create virtual workstations | [Create a virtual GPU-accelerated workstation](https://docs.cloud.google.com/compute/docs/virtual-workstation#choose_a_virtual_workstation)  
  
### Cloud Run

You can configure GPUs for your Cloud Run instances. GPUs are ideal for running AI inference workloads using large language models on Cloud Run.

On Cloud Run, consult these resources for running AI workloads on GPUs:

  * [Configure GPUs for a Cloud Run service](https://docs.cloud.google.com/run/docs/configuring/services/gpu)
  * [Load large ML models on Cloud Run with GPUs](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices#model-loading-recommendations)
  * [Tutorial: Run LLM inference on Cloud Run GPUs with Ollama](https://docs.cloud.google.com/run/docs/tutorials/gpu-gemma2-with-ollama)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
