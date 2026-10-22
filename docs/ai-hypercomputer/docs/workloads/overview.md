---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/overview/
title: Benchmarking recipes \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:13.559998+00:00
---

# Benchmarking recipes  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Benchmarking recipes Stay organized with collections  Save and categorize content based on your preferences. 

To support you with running your workloads, we have curated a set of reproducible benchmark recipes that use some of the most common machine learning (ML) frameworks and models. These are stored in GitHub repositories. To access these repositories, see [AI Hypercomputer GitHub organization](https://github.com/orgs/AI-Hypercomputer/repositories). These benchmark recipes were tested on clusters created using Cluster Toolkit.

**Important:** Benchmark recipes are only supported for VMs that use [future reservations](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models#future-reservations).

## Overview

Before you get started with these recipes, ensure that you have completed the following steps:

  1. Choose an accelerator that best suits your workload. See [Choose a deployment strategy](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy).
  2. Select a consumption method based on your accelerator of choice, see [Consumption options](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models).
  3. Create your cluster based on the type of accelerator selected. See [Cluster deployment guides](https://docs.cloud.google.com/ai-hypercomputer/docs/choose-strategy#accelerators-pre-train).



## Recipes

The following reproducible benchmark recipes are available for pre-training and inference on GKE clusters.

To search the catalog, you can filter by a combination of your framework, model, and accelerator.

NeMoMaxTextSGLangTensorRT-LLMvLLMDeepSeek R1 671BGPT3-175BLlama3 70BLlama3.1 70BLlama-3.1-405BMixtral-8-7BA3 UltraA3 MegaInferencePre-training

Clear all

**Recipe name** | **Accelerator** | **Model** | **Framework** | **Workload type**  
---|---|---|---|---  
[Llama3.1 70B - A3 Ultra](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/training/a3ultra/llama3-1-70b/maxtext-pretraining-gke/README.md) | A3 Ultra | Llama3.1 70B | MaxText | Pre-training on GKE  
[Llama3.1 70B - A3 Ultra](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/training/a3ultra/llama3-1-70b/nemo-pretraining-gke/README.md) | A3 Ultra | Llama3.1 70B | NeMo | Pre-training on GKE  
[Mixtral-8-7B - A3 Ultra](https://github.com/AI-Hypercomputer/gpu-recipes/tree/main/training/a3ultra/mixtral-8x7b/nemo-pretraining-gke/README.md) | A3 Ultra | Mixtral-8-7B | NeMo | Pre-training on GKE  
[GPT3-175B \- A3 Mega](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/training/a3mega/gpt3-175b/nemo-pretraining-gke/README.md) | A3 Mega | GPT3-175B | NeMo | Pre-training on GKE  
[Mixtral 8x7B - A3 Mega](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/training/a3mega/mixtral-8x7b/nemo-pretraining-gke/README.md) | A3 Mega | Mixtral 8x7B | NeMo | Pre-training on GKE  
[Llama3 70B - A3 Mega](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/training/a3mega/llama3-70b/nemo-pretraining-gke/README.md) | A3 Mega | Llama3 70B | NeMo | Pre-training on GKE  
[Llama3.1 70B A3 Mega](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/training/a3mega/llama3-1-70b/nemo-pretraining-gke/README.md) | A3 Mega | Llama3.1 70B | NeMo | Pre-training on GKE  
[DeepSeek R1 671B](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/inference/a3mega/deepseek-r1-671b/sglang-serving-gke/README.md) | A3 Mega | DeepSeek R1 671B | SGLang | Inference on GKE  
[DeepSeek R1 671B](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/inference/a3mega/deepseek-r1-671b/vllm-serving-gke/README.md) | A3 Mega | DeepSeek R1 671B | vLLM | Inference on GKE  
[Llama-3.1-405B - A3 Ultra](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/training/a3ultra/llama3-1-405b/maxtext-pretraining-gke/README.md) | A3 Ultra | Llama-3.1-405B | MaxText | Pre-training on GKE  
[Llama-3.1-405B - A3 Ultra (Resiliency)](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/training/a3ultra/llama3-1-405b/nemo-pretraining-gke-resiliency/README.md) | A3 Ultra | Llama-3.1-405B | NeMo | Pre-training on GKE  
[Llama-3.1-405B - A3 Ultra](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/training/a3ultra/llama3-1-405b/nemo-pretraining-gke/README.md) | A3 Ultra | Llama-3.1-405B | NeMo | Pre-training on GKE  
[DeepSeek R1 671B](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/inference/a3ultra/deepseek-r1-671b/sglang-serving-gke/README.md) | A3 Ultra | DeepSeek R1 671B | SGLang | Inference on GKE  
[DeepSeek R1 671B](https://github.com/AI-Hypercomputer/gpu-recipes/blob/main/inference/a3ultra/deepseek-r1-671b/vllm-serving-gke/README.md) | A3 Ultra | DeepSeek R1 671B | vLLM | Inference on GKE  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
