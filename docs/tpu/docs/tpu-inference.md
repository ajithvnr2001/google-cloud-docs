---
url: https://docs.cloud.google.com/tpu/docs/tpu-inference/
title: Run inference on Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:14.312138+00:00
---

# Run inference on Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/tpu-inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run inference on Cloud TPU

**Note:** If you're new to Cloud TPU, see [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).

Serving is the process of deploying a trained machine learning model to a production environment to run inference. TPU v5e and later versions support inference. Meeting latency service level objectives (SLOs) is a priority for serving workloads.

This document discusses serving a model on a _single-host_ TPU. TPU slices with eight or fewer chips have one TPU VM or host and are called _single-host_ TPUs. For information about multi-host inference with PyTorch, see [vLLM-TorchTPU](https://github.com/vllm-project/vllm-torchtpu) and [SGLang-TorchTPU](https://github.com/sgl-project/sglang-torchtpu). For information about multi-host inference with JAX, see [Perform multi-host inference using Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference).

## Set up your TPU

Whichever stack you choose, you need a Google Cloud project with a single-host TPU before you can serve a model. The following steps apply to every combination of library and framework:

  1. **Create a project.** You need a Google Cloud account and project to use Cloud TPU. For more information, see [Set up a Google Cloud project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute).
  2. **Check your quota.** Ensure that you have sufficient quota for the number of TPU cores that you plan to use for inference. TPU v5e uses separate quotas for training and serving. In the Cloud TPU API, the serving-specific quotas for TPU v5e are as follows:

     * **On-demand v5e resources** : `TPU v5 lite pod cores for serving per project per zone`
     * **Preemptible v5e resources** : `Preemptible TPU v5 lite pod cores for serving per project per zone`

For other TPU versions, training and serving workloads use the same quota. For more information, see [Cloud TPU quotas](https://docs.cloud.google.com/tpu/docs/quota).

  3. **Create a TPU VM.** Choose a TPU version and zone that has serving capacity, and then create a single-host TPU VM. For more information, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones) and [Manage TPU resources](https://docs.cloud.google.com/tpu/docs/managing-tpus-compute).




After the TPU VM is running, follow the setup guide for your library and framework in Choose an inference stack.

## Choose an inference stack

Cloud TPU supports large language model (LLM) inference through two open-source serving libraries: [vLLM](https://docs.vllm.ai/en/latest/) and [SGLang](https://docs.sglang.io/). Both libraries run on Cloud TPU with either a JAX or a PyTorch backend, so you can choose the library that best fits your workload regardless of the framework that your model is written in.

Choose the library first, and then select the backend that matches your model's framework, as shown in the following table:

Serving library | JAX backend | PyTorch backend  
---|---|---  
vLLM |  [`vllm-jax`](https://github.com/vllm-project/vllm-jax) |  [`vllm-torchtpu`](https://github.com/vllm-project/vllm-torchtpu)  
SGLang |  [`sglang-jax`](https://docs.sglang.io/docs/hardware-platforms/tpu) |  [`sglang-torchtpu`](https://github.com/sgl-project/sglang-torchtpu)  
  
## Inference with vLLM

[vLLM](https://docs.vllm.ai/en/latest/) is an open-source library for fast inference and serving of LLMs, built around continuous batching and [PagedAttention](https://vllm.ai/blog/2023-06-20-vllm). Cloud TPU works with vLLM through the [`vllm-jax`](https://github.com/vllm-project/vllm-jax) plugin for JAX models and the [`vllm-torchtpu`](https://github.com/vllm-project/vllm-torchtpu) plugin for PyTorch models.

For additional examples of using vLLM to serve a model on TPUs, see the following resources:

  * [Get started with vLLM TPU](https://github.com/vllm-project/vllm-jax/tree/main/docs/getting_started/quickstart.md)
  * [Serve an LLM using TPU Trillium on Google Kubernetes Engine with vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu)
  * [Recipes for serving vLLM on Trillium TPUs (v6e)](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/inference/trillium/vLLM)



### vLLM with JAX

The vLLM TPU documentation covers installation, a quickstart, supported models, and tuning options. For more information, see [Serve JAX models with vLLM on TPU](https://docs.vllm.ai/projects/tpu).

### vLLM with PyTorch

The `vllm-torchtpu` plugin adds TorchTPU kernel and runtime support to vLLM. For more information, see [Serve PyTorch models with vLLM on TPU](https://github.com/vllm-project/vllm-torchtpu).

## Inference with SGLang

[SGLang](https://docs.sglang.io/) is an open-source serving framework for large language and multimodal models that pairs a high-performance runtime with a structured generation frontend. On Cloud TPU, SGLang runs through the SGLang-JAX backend (`sglang-jax`) for JAX models and the SGLang-TorchTPU backend (`sglang-torchtpu`) for PyTorch models.

### SGLang with PyTorch

For information about installation, server launch, and supported configurations, see [Serve PyTorch models with the SGLang-TorchTPU runtime on TPU](https://github.com/sgl-project/sglang-torchtpu).

### SGLang with JAX

For information about installation, server launch, and supported configurations, see [Serve JAX models with the SGLang-JAX runtime on TPU](https://docs.sglang.io/docs/hardware-platforms/tpu).

## Profile inference performance

After setting up inference, you can use profilers to analyze performance and TPU utilization. For more information about profiling, see the following resources:

  * [Profiling on Cloud TPU](https://docs.cloud.google.com/tpu/docs/profile-tpu-vm)
  * [PyTorch profiling](https://torchtpu.readthedocs.io/en/latest/performance_profiling_with_xprof/)
  * [JAX profiling](https://jax.readthedocs.io/en/latest/profiling.html#profiling-jax-programs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
