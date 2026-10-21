---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/
title: AI workloads tutorials overview \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:35:01.274181+00:00
---

# AI workloads tutorials overview  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  AI workloads tutorials overview Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

To help you run proof-of-concept (POC) AI/ML workloads, this page provides an overview of AI Hypercomputer tutorials that describe the complete process of deploying common AI models on Google Cloud products.

These tutorials are designed for machine learning (ML) engineers, researchers, platform administrators and operators, and data and AI specialists. To use these tutorials effectively, you should have a foundational understanding of machine learning concepts and proficiency with Google Cloud services. Experience with deploying and managing AI models also helps you understand this content.

## Tutorial categories

The AI workload tutorials are organized into the following categories:

  * Run inference with vLLM on GKE
  * Run fine-tuning
  * Run training



### Run inference with vLLM on GKE

These tutorials describe how to deploy and serve large language models (LLMs) for inference using the vLLM serving framework on Google Kubernetes Engine (GKE). You learn to use GKE's container orchestration capabilities for efficient inference workloads. These tutorials cover accessing models using Hugging Face, setting up GKE clusters (for example, in Autopilot mode), handling credentials, and deploying vLLM containers for interaction with LLMs such as Gemma 3, Llama 4, and Qwen3.

### Run fine-tuning

These tutorials describe how to fine-tune LLMs for specific tasks across various Google Cloud cluster types, including GKE and Slurm. For example, you can fine-tune Gemma 3 on multi-node and multi-GPU GKE clusters (for example, using A4 VM instances with NVIDIA B200 GPUs) and Slurm clusters. You will create custom VM images, configure RDMA networks, and execute distributed fine-tuning jobs with libraries like Hugging Face Accelerate and FSDP. Some tutorials also cover using frameworks like Ray for vision-related tasks.

### Run training

These tutorials describe how to train or pre-train LLMs on high-performance clusters. For example, you learn to pre-train models like Qwen2 on multi-node and multi-GPU Slurm clusters with A4 virtual machines. You deploy Slurm clusters using the Google Cloud Cluster Toolkit, create custom VM images, configure shared Filestore instances, configure high-speed RDMA networking, and run distributed pre-training jobs with Hugging Face Accelerate.

## What's next

Explore the AI Hypercomputer tutorials:

  * [Use vLLM on GKE to serve Gemma 3 27B inference](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma-3-vllm-inference)
  * [Fine-tune Gemma 4 on an A4 GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma4-finetune-a4-gke-cluster)
  * [Fine-tune Gemma 4 on a multi-host A4 GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma4-finetune-a4-gke-multi-host-cluster)
  * [Train Qwen2 on an A4 Slurm cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/train-qwen2-a4-slurm-cluster)
  * [Serve Qwen2-72B with vLLM on TPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen2-7b-instruct)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
