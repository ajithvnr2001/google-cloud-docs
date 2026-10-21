---
url: https://docs.cloud.google.com/tpu/docs/v5e-inference/
title: Run inference on Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:13:08.819585+00:00
---

# Run inference on Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/v5e-inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run inference on Cloud TPU

**Note:** If you are new to Cloud TPUs, see [Introduction to Cloud TPU](https://docs.cloud.google.com/tpu/docs/intro-to-tpu).

Serving refers to the process of deploying a trained machine learning model to a production environment, where it can be used for inference. Inference is supported on TPU v5e and newer versions. Latency SLOs are a priority for serving.

This document discusses serving a model on a _single-host_ TPU. TPU slices with 8 or less chips have one TPU VM or host and are called _single-host_ TPUs. For information about multi-host inference, see [Perform multihost inference using Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference).

## Get started

You need a Google Cloud account and project to use Cloud TPU. For more information, see [Set up a Google Cloud project for TPUs](https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute).

Ensure that you have sufficient quota for the number of TPU cores that you plan to use for inference. TPU v5e uses separate quotas for training and serving. In the Cloud TPU API, the serving-specific quotas for TPU v5e are as follows:

  * **On-demand v5e resources** : `TPUv5 lite pod cores for serving per project per zone`
  * **Preemptible v5e resources** : `Preemptible TPU v5 lite pod cores for serving per project per zone`



For other TPU versions, training and serving workloads use the same quota. For more information, see [Cloud TPU quotas](https://docs.cloud.google.com/tpu/docs/quota).

## Serve LLMs with vLLM

[vLLM](https://docs.vllm.ai/en/latest/) is an open-source library designed for fast inference and serving of large language models (LLMs). Cloud TPU integrates with vLLM using the `tpu-inference` plugin, which supports JAX and PyTorch models. For more information, see the [`tpu-inference` GitHub repository](https://github.com/vllm-project/tpu-inference).

For examples of using vLLM to serve a model on TPUs, see the following:

  * [Get started with vLLM TPU](https://github.com/vllm-project/tpu-inference/tree/main/docs/getting_started/quickstart.md)
  * [Serve an LLM using TPU Trillium on GKE with vLLM](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/serve-vllm-tpu).
  * [Recipes for serving vLLM on Trillium TPUs (v6e)](https://github.com/AI-Hypercomputer/tpu-recipes/tree/main/inference/trillium/vLLM)



## Profiling

After setting up inference, you can use profilers to analyze the performance and TPU utilization. For more information about profiling, see:

  * [Profiling on Cloud TPU](https://docs.cloud.google.com/tpu/docs/profile-tpu-vm)
  * [TensorFlow profiling](https://www.tensorflow.org/guide/profiler)
  * [PyTorch profiling](https://docs.cloud.google.com/tpu/docs/pytorch-xla-performance-profiling-tpu-vm)
  * [JAX profiling](https://jax.readthedocs.io/en/latest/profiling.html#profiling-jax-programs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
