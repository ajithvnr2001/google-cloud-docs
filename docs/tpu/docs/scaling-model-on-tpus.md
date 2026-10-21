---
url: https://docs.cloud.google.com/tpu/docs/scaling-model-on-tpus/
title: Scale a model on TPUs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:09.172218+00:00
---

# Scale a model on TPUs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/scaling-model-on-tpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Scale a model on TPUs

This document provides an overview of how to scale language models: how TPUs work and how they communicate with each other, how LLMs run on real hardware, and how to parallelize your models during training and inference so they run efficiently at massive scale. We provide information that helps you assess how expensive it will be to train an LLM, how much memory you need to serve the model, and how to effectively shard models across multiple TPUs.

While a lot of deep learning is complex, optimizing the performance of your models doesn't have to be, even at scale. Fundamental principles apply everywhere — from dealing with a single accelerator to tens of thousands — and understanding them lets you do many useful things:

  * Estimate how close parts of your model are to their theoretical optimum.
  * Make informed choices about different parallelism schemes at different scales (how you split the computation across multiple devices).
  * Estimate the cost and time required to train and run large Transformer models.
  * Design algorithms that take advantage of TPU architecture.
  * Design model architectures driven by an explicit understanding of what limits algorithm performance.



## Prerequisites

You should have a basic understanding of LLMs and the Transformer architecture but not necessarily how they operate at scale. You should understand the basics of LLM training and ideally have some basic familiarity with JAX. Useful background reading for Transformer architecture includes:

  * The [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/): blog post on the Transformer architecture
  * [Attention is all you need](https://arxiv.org/abs/1706.03762): the original Transformer paper



After becoming familiar with these prerequisites, you should feel comfortable estimating the best parallelism scheme for a Transformer model on a given TPU platform. You will also be able to estimate how long training and inference should take.

## Importance of model scaling

LLMs and most small models today run so close to hardware limits that developing models requires you to think about efficiency at scale. A 20% win on benchmarks is irrelevant if it comes at a 20% cost to roofline efficiency. Promising model architectures routinely fail either because they can't run efficiently at scale or because of a lack of optimization effort to make them do so.

The goal of model scaling is to be able to increase the number of chips used for training or inference while achieving a proportional, linear increase in throughput. This is known as strong scaling. Although adding additional chips (parallelism) usually decreases the computation time, it also comes at the cost of added communication between chips. When communication takes longer than computation, the model becomes communication bound and cannot scale well. Understanding hardware well enough to anticipate where these bottlenecks will arise lets you design or reconfigure your models to avoid these bottlenecks.

The following sections provide an overview of how to scale TPU hardware and how Transformer architecture has evolved. This information is useful for both researchers designing new architectures and engineers working to make the current generation of LLMs run fast.

### Part 1: Concepts

This part explains roofline analysis and the factors that limit the ability of a model to scale (communication, computation, and memory). Next, we describe how TPUs work, both as individual chips and — of critical importance — as an interconnected system with inter-chip links of limited bandwidth and latency.

  * [Introduction to roofline analysis](https://jax-ml.github.io/scaling-book/roofline): This section describes how to approximate how fast your algorithm will run based on compute, communication, and memory bounds.
  * [Operations on TPU architecture](https://jax-ml.github.io/scaling-book/tpus): This section describes the architecture of TPUs, how different hardware modules in TPU work, and how they affect model training and serving.
  * [Model sharding for multi-TPU parallelism](https://jax-ml.github.io/scaling-book/sharding/): This section delves into model sharding and multi-TPU parallelism by explaining sharded matrix multiplications.



### Part 2: Scaling Transformers

It's important to understand every piece of the Transformer architecture: the exact sizes of every matrix, where normalization occurs, and how many parameters and FLOPs are in each part. This part goes through this Transformer math carefully, showing how to count the parameters and FLOPs for both training and inference. This tells you how much memory your model will use, how much time you'll spend on compute or communications, and when attention will become important relative to the feed-forward blocks.

Finally, this part helps you get an answer to the fundamental question: given a model of a specific size and provided with some number of chips, how to parallelize the model to stay in the strong scaling condition. To answer this question, this part discusses the four primary parallelism techniques used to split models over multiple chips: data, tensor, pipeline, and expert. It also describes other techniques to reduce the memory requirements such as rematerialization, ZeRO-powered model sharding, host offload, and gradient accumulation.

  * [Introduction to Transformer math operations](https://jax-ml.github.io/scaling-book/transformers): This section works through the math to answer questions about the number of FLOPs used by a Transformer during forward and backward passes, calculations to compute the number of parameters, and size of KV caches.
  * [Transformer parallelization for training](https://jax-ml.github.io/scaling-book/training): This section details the process to maximize training efficiency by coordinating FSDP, Megatron sharding, and pipeline parallelism. It describes how to determine the optimal distribution for a specific model size and batch size across a fixed number of chips to achieve peak throughput. 
    * [Training Llama 3 on TPUs](https://jax-ml.github.io/scaling-book/applied-training): This sub-section describes how to train Llama 3 on TPUs, how long it might take, and how much it might cost.
  * [Transformer scaling for inference](https://jax-ml.github.io/scaling-book/inference): After a model is trained, it needs to be served. Inference adds a new consideration, latency, and changes the memory landscape. This section describes how disaggregated serving works and how to think about KV caches. 
    * [Serving Llama 3 on TPUs](https://jax-ml.github.io/scaling-book/applied-inference): This sub-section describes how to serve Llama 3 on TPUs, how much it might cost, and the latency and throughput tradeoffs.



### Part 3: Practical implementation

This part describes how to implement the scaling concepts using JAX, and how to profile and debug your code when things go wrong.

  * [Profiling TPU programs](https://jax-ml.github.io/scaling-book/profiling): Real LLMs are complex and are difficult to develop, optimize, and debug. This section explains the JAX + XLA stack and how to use the JAX/TensorBoard profiler to debug and fix real issues.
  * [Programming TPUs in JAX](https://jax-ml.github.io/scaling-book/jax-stuff): This section describes how to use the JAX APIs to parallelize computation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
