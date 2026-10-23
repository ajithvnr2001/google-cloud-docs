---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/
title: AI workloads tutorials overview \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:54:10.658003+00:00
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

These tutorials are designed for machine learning (ML) engineers, researchers, platform administrators and operators, and data and AI specialists. These tutorials assume that you have a foundational understanding of ML concepts and proficiency with Google Cloud services, container orchestration, and cluster management.

## Tutorial categories

The AI workload tutorials are organized into the following categories:

  * Run inference with vLLM and SGLang on GKE: deploy and serve large language models (LLMs) for inference using the vLLM and SGLang serving frameworks on Google Kubernetes Engine (GKE).
  * Run LLM fine-tuning on GKE and Slurm: fine-tune LLMs for specific tasks on GKE and Slurm clusters using distributed frameworks such as Hugging Face Accelerate, PyTorch Fully Sharded Data Parallel (FSDP), and Ray.
  * Run LLM training on Slurm clusters: train and pre-train LLMs on multi-node Slurm clusters using Cluster Toolkit and Hugging Face Accelerate.



### Run inference with vLLM and SGLang on GKE

These tutorials describe how to deploy and serve LLMs for inference using the vLLM and SGLang serving frameworks on GKE. You learn to use GKE's container orchestration capabilities for efficient inference workloads. These tutorials cover accessing models using Hugging Face, setting up GKE clusters (for example, in Autopilot mode), handling credentials, and deploying vLLM or SGLang containers for interaction with LLMs such as Gemma 4, Gemma 3, Llama 4, and Qwen3.

### Run LLM fine-tuning on GKE and Slurm

These tutorials describe how to fine-tune LLMs for specific tasks across various Google Cloud cluster types, including GKE and Slurm. For example, you can fine-tune Gemma 3 on multi-node and multi-GPU GKE clusters (for example, using A4 VM instances with NVIDIA B200 GPUs) and Slurm clusters. You create custom VM images, configure RDMA networks, and run distributed fine-tuning jobs using Hugging Face Accelerate and FSDP for text tasks, or the Ray framework for multimodal vision tasks.

### Run LLM training on Slurm clusters

These tutorials describe how to train or pre-train LLMs on high-performance clusters. For example, you learn to pre-train models like Qwen2 on multi-node and multi-GPU Slurm clusters with A4 virtual machines. You deploy Slurm clusters using the Google Cloud Cluster Toolkit, create custom VM images, configure shared Filestore instances, configure high-speed RDMA networking, and run distributed pre-training jobs with Hugging Face Accelerate.

## What's next

Explore the AI Hypercomputer tutorials:

  * [Serve Qwen3-Coder-480B with multi-host SGLang TorchTPU on TPU7x](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-coder-gke-ironwood-multi-host-torchtpu)
  * [Serve Qwen3.5-397B with multi-host vLLM TorchTPU on TPU7x](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-5-397b-ironwood-multi-host-vllm-torchtpu)
  * [Serve Gemma 4 26B with multi-host vLLM TorchTPU on Trillium TPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-gemma4-26b-gke-trillium-vllm)
  * [Serve Qwen3.5-397B with vLLM TorchTPU on TPU7x](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen3-5-397b-ironwood-vllm-torchtpu)
  * [Fine-tune Gemma 4 on a multi-host A4 GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma4-finetune-a4-gke-multi-host-cluster)
  * [Fine-tune Gemma 4 on an A4 GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma4-finetune-a4-gke-cluster)
  * [Run multi-host RL training for Gemma 4 26B on TPU v6e](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-26b-rl-maxtext)
  * [Run SFT for Gemma 4 31B on multi-host TPU v6e](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-gemma4-31b-sft-maxtext)
  * [Run multi-host RL training for Qwen3-30B-A3B on TPU v6e](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-qwen3-30b-a3b-rl-maxtext)
  * [Fine-tune Gemma 3 on a multi-host A4 GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/gpu/gemma3-finetune-a4-gke-multi-host-cluster)
  * [Run RL training on a v6e-8 TPU VM](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-rl-v6e-8-tpu-vm)
  * [Run supervised fine-tuning on a TPU VM with MaxText](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/run-sft-v6e-8-tpu-vm-maxtext)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
