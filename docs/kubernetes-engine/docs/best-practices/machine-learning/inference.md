---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/
title: Overview of inference best practices on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:26:10.499954+00:00
---

# Overview of inference best practices on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Overview of inference best practices on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document provides a high-level overview of best practices for running inference workloads on GKE.

This document is for Data administrators, Operators, and Developers who want to adopt best practices for their inference workloads using accelerators, such as GPUs and TPUs, with Kubernetes and GKE. To learn more about common roles, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

## Prepare for inference serving on GKE

This section describes foundational best practices you should follow when you're preparing to deploy an inference workload. These practices include analyzing your use case, choosing models, and selecting accelerators.

### Analyze the characteristics of your inference use case

Before you deploy an inference workload, analyze its specific requirements. This analysis helps you make architectural decisions that balance performance, cost, and reliability. Understanding your use case helps you select the appropriate models, accelerators, and configurations to meet your service-level objectives (SLOs).

To guide your analysis, evaluate the following key dimensions of your workload:

  * **Define performance and latency requirements** : determine your application's SLOs for latency and throughput. Key metrics to define include requests per second (RPS), response latency, input and output token length, and prefix cache hit rate. For more information, see [Inference performance metrics](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning/inference#performance).
  * **Evaluate model requirements and scale** : the characteristics of your chosen model directly influence your infrastructure needs. Consider the maximum context length the model supports and compare it to what your workload requires. If your use case doesn't require maximum context, lowering the maximum context length can free accelerator memory for a larger [KV cache](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization#kv-cache-quantization), potentially increasing throughput.
  * **Establish cost and business constraints** : your budget and business objectives are key factors in designing a sustainable and cost-effective inference service. Define your target cost-per-million-tokens for input and output and your total monthly budget for this workload. Identify your optimization goal, such as price-performance, lowest latency, or highest throughput, and whether or not your app can tolerate variable latency.



### Choose the right models for your inference use cases

Selecting the right model directly impacts the performance, cost, and feasibility of your inference application. To select the optimal model, evaluate candidates based on the following criteria:

  * **Task and modality alignment** : evaluate models based on their designated tasks and supported modalities. A model optimized for a specific task almost always outperforms a more general-purpose model.
  * **Technical characteristics** : a model's architecture and data type precision—such as FP16, FP8, and FP4—are key factors in determining its resource requirements and performance. This assessment helps you determine if you need to apply quantization techniques. Check the supported precision for model weights, ensure framework support, and verify the model's maximum supported context length.
  * **Performance and cost-effectiveness** : to make a data-driven decision, compare your shortlisted models using publicly available benchmarks and your own internal tests. Use leaderboards like the [Chatbot Arena](https://lmsys.org/blog/2023-05-03-arena/) to compare models, and evaluate the cost-per-million-tokens for each model on your target hardware.



### Apply quantization to the model

Quantization is a technique for optimizing your inference workloads by reducing the memory footprint of your model. It converts the model's weights, activations, and key-value (KV) cache from high-precision floating-point formats (such as FP16, FP32, and FP64) to lower-precision formats (such as FP8 and FP4). This reduction in memory can lead to significant improvements in both performance and cost-effectiveness.

Quantization reduces the model's memory footprint, which in turn reduces data transfer overhead and frees up memory for a larger KV cache.

To effectively apply quantization to your models, follow these recommendations:

  * **Evaluate the accuracy trade-off** : quantization can sometimes result in a loss of model accuracy. When you evaluate the accuracy trade-off of quantization, consider that 8-bit quantization can often result in minimal loss of accuracy. In contrast, 4-bit quantization can provide up to a four-fold reduction in accelerator memory requirements, but it might also cause a greater loss of accuracy compared to 8-bit quantization. Evaluate the quantized model's performance on your specific use case to ensure that the accuracy is still within an acceptable range. To evaluate the loss of accuracy, you can use tools like [OpenCompass](https://github.com/open-compass/opencompass) and [Language Model Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness).
  * **Evaluate hardware acceleration support** : to get the most out of quantization, use accelerators that provide hardware acceleration for the data formats that the quantized model uses. For example: 
    * NVIDIA H100 GPUs provide hardware acceleration for FP8 and FP16 operations.
    * NVIDIA B200 GPUs provide hardware acceleration for FP4, FP8, and FP16 operations.
    * Cloud TPU v5p provides hardware acceleration for FP8 operations.
  * **Check for pre-quantized models** : before quantizing a model yourself, check public model repositories like [Hugging Face](https://huggingface.co/). Ideally, find a model that was natively trained at a lower precision, as this can provide performance benefits without the potential loss of accuracy from post-training quantization.
  * **Use a quantization library** : if a pre-quantized model isn't available, use a library to perform the quantization yourself. Inference servers like [vLLM](https://docs.vllm.ai/en/latest/features/quantization/index.html) support running models that have been quantized with a variety of techniques. You can use tools like [llm-compressor](https://github.com/vllm-project/llm-compressor) to apply quantization techniques to a non-quantized model.
  * **Consider KV cache quantization** : in addition to quantizing the model's weights, you can also quantize the KV cache. This technique further reduces the memory required for the KV cache at runtime, which can lead to improved performance.



For more information, see [Optimize LLM inference workloads on GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization#quantization).

### Choose the right accelerators

Selecting the right accelerator directly impacts the performance, cost, and user experience of your inference service. The optimal choice depends on an analysis of your model's memory requirements, your performance goals, and your budget.

**Tip:** For a detailed analysis of model serving performance and costs, we recommend using the GKE Inference Quickstart tool. To learn more, see the [GKE Inference Quickstart guide](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart) and the accompanying [Colab notebook](https://github.com/GoogleCloudPlatform/kubernetes-engine-samples/blob/main/ai-ml/notebooks/giq_visualizations.ipynb).

To choose the right accelerator for your specific use case, follow these steps:

  1. **Calculate your memory requirements** : first, calculate the minimum accelerator memory required to load and run your model. The total memory is the sum of the memory required for the model weights, the inference engine overhead, intermediate activations, and the KV cache.

To estimate the required memory, use the following equation:

\\[ \begin{aligned} \text{Required accelerator memory} = {} & (\text{Model weights} + \text{Overhead} + \text{Activations}) \\\ & \+ (\text{KV cache per batch} \times \text{Batch size}) \end{aligned} \\]

The terms in the equation are as follows:

     * **Model weights** : the size of the model's parameters.
     * **Overhead** : a buffer for the inference server and other system overhead, typically 1-2 GB.
     * **Activation** : the memory required for intermediate activations during the execution of a model.
     * **KV cache per batch** : the memory required for the KV cache for a single sequence, which scales with the context length and model configuration.
     * **Batch size** : the number of sequences (`max_num_sequences`) that will be processed concurrently by the inference engine.

#### Example: Calculate accelerator memory requirements for Gemma 3

To compute the required accelerator memory to deploy a Gemma 3 27-billion parameter model with a precision of BF16 for a text-generation use case, you can use the following values.

For an interactive walkthrough of this calculation, see the [How Much VRAM Does My Model Need?](https://colab.research.google.com/github/ericehanley/rightsize-vllm/blob/main/HBM_Calculator.ipynb) Colab notebook.

     * **Inputs** : 
       * Model weights: 54 GB
       * Batch size (`max_num_sequences`): 1
       * Average input length: 1,500 tokens
       * Average output length: 200 tokens
       * Inference engine overhead: 1 GB (estimated)
       * KV cache data type size: 2 (for BF16)
       * KV vectors: 2 (one for Key, one for Value)
     * [**Model configuration**](https://huggingface.co/google/gemma-3-27b-it/blob/main/config.json) for a Gemma 3 27B instruction-tuned model: 
       * `hidden_size`: 5376
       * `intermediate_size`: 21504
       * `num_attention_heads`: 32
       * `num_hidden_layers`: 62
       * `num_key_value_heads`: 16
     * **Memory Calculation** : 
       * `sequence_length` = `avg_input_length` \+ `avg_output_length` = 1500 + 200 = 1700 tokens
       * `pytorch_activation_peak_memory` = (`max_num_sequences` * `sequence_length` * (18 * `hidden_size` \+ 4 * `intermediate_size`)) / (1000^3) = ~0.31 GB (estimated).
       * `head_dims` = `hidden_size` / `num_attention_heads` = 5376 / 32 = 168
       * `kv_cache_memory_per_batch` = (`kv_vectors` * `max_num_sequences` * `sequence_length` * `num_key_value_heads` * `head_dims` * `num_hidden_layers` * `kv_data_type_size`) / (1000^3) = (2 * 1 * 1700 * 16 * 168 * 62 * 2) / (1000^3) = ~1.13 GB
       * **Required accelerator memory** = `Model weights` \+ `Overhead` \+ `Activations` \+ `KV cache per batch` = 54 + 1 + 0.31 + 1.13 = **~56.44 GB**

The total estimated accelerator memory you require to deploy the model is approximately **57 GB**.

  2. **Evaluate accelerator options** : once you estimate your memory requirements, evaluate the available [GPU](https://docs.cloud.google.com/compute/docs/gpus) and [TPU](https://docs.cloud.google.com/tpu/docs/regions-zones) options on GKE.

In addition to the amount of accelerator memory, consider the following model requirements for your evaluation:

     * For models that require more than one accelerator, check for support for high-speed connectivity, such as NVLINK and GPUDirect, to reduce communication latency.
     * For quantized models, use accelerators with native hardware acceleration for lower-precision data types, such as FP8 and FP4, to get the most performance benefits.

Your choice involves a trade-off between these features, performance, cost, and availability.

#### Recommended accelerators by use case

**Tip** : For the latest accelerator recommendations based on serving performance benchmarks and cost analysis, you can also use the GKE Inference Quickstart tool. For more details, see the [GKE Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart) documentation.

To help you choose the right accelerators for your workload, the following table summarizes the most suitable options for common inference use cases. These use cases are defined as follows:

     * **Small model inference** : for models with a few billion parameters, where the computational load is confined to a single host.
     * **Single-host large model inference** : for models with tens to hundreds of billions of parameters, where the computational load is shared across multiple accelerators on a single host machine.
     * **Multi-host large model inference** : for models with hundreds of billions to trillions of parameters, where the computational load is shared across multiple accelerators on multiple host machines.
Use Case | Recommended Accelerators | Machine Series | Key Characteristics  
---|---|---|---  
Small model inference | NVIDIA L4 | G2 | Cost-effective option for small models (24 GB memory per GPU).  
NVIDIA RTX Pro 6000 | G4 | Cost-effective for models under 30B parameters and image generation (96 GB memory per GPU). Supports direct GPU peer-to-peer communication, making it suitable for single-host, multi-GPU inference.   
TPU v5e | - | Optimized for cost-efficiency.  
TPU v6e | - | Offers the highest value for transformer and text-to-image models.  
Single-host large model inference | NVIDIA A100 | A2 | Suitable for most models that fit on a single node (up to 640 GB total memory).  
NVIDIA H100 | A3 | Ideal for inference workloads that fit on a single node (up to 640 GB total memory).  
NVIDIA B200 | A4 | Future-proof option for demanding models that fit on a single node (up to 1,440 GB total memory).  
TPU v4 | - | Offers a good balance between cost and performance.  
TPU v5p | - | A high-performance option for demanding workloads.  
Multi-host large model inference | NVIDIA H200 | A3 Ultra | Suitable for large, memory-intensive models (up to 1,128 GB total memory).  
NVIDIA B200 / GB200 | A4 / A4X | For the most demanding, compute-intensive, and network-bound workloads. A4X machines use Arm-based CPUs, which may require workload refactoring (code changes beyond a simple container rebuild) if your workload uses x86-specific features or optimizations.  
TPU v5e | - | Optimized for cost-efficiency and performance for medium-to-large LLM serving.  
TPU v5p | - | A high-performance option for multi-host inference that requires large-scale parallelization.  
TPU v6e | - | Optimized for transformer, text-to-image, and CNN serving.  
  
#### Example: Choose an accelerator for a 260 GB model

Imagine you need to deploy a model that requires 260 GB of total accelerator memory (200 GB for the model, 50 GB for the KV cache, and 10 GB for overhead).

Based on memory requirements alone, you can exclude NVIDIA L4 GPUs, as the largest G2 machine offers a maximum of 192 GB of accelerator memory. Additionally, because L4 GPUs don't support high-speed, low-latency connectivity between accelerators, distributing the workload across multiple nodes is not a viable option for achieving the desired performance.

If you want to avoid refactoring your x86-64 workloads (that is, having to modify your code so that it can run on a different type of processor), you would also exclude NVIDIA GB200 and GB300 accelerators, which use Arm-based CPUs.

This leaves you with the following options:

     * NVIDIA A100
     * NVIDIA RTX Pro 6000
     * NVIDIA H100
     * NVIDIA H200
     * NVIDIA B200

All of these accelerators have enough memory. Your next step is to evaluate their availability in your target regions. Let's say you find that only NVIDIA A100 and NVIDIA H100 GPUs are available in a particular region. After comparing the price-performance ratio of these two options, you might choose the NVIDIA H100 for your workload.

#### Multi-instance GPUs

To increase GPU utilization and optimize GPU costs, you can use multi-instance GPU configurations. With this configuration, you partition a [supported GPU](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi#supported_gpus) to share a single GPU across multiple containers on GKE. When you provision a multi-instance GPU, you attach whole GPUs only to your GKE nodes, and you are subject to the corresponding GPU pricing. We recommend that you use multi-instance GPUs with trusted workloads only.

For example, you can attach an NVIDIA RTX PRO 6000 and do the following:

     * Partition it to four instances (each instance provides 24 GB of accelerator memory), and run diffusion models or small model inference workloads, such as models that have approximately 8 billion parameters and use FP16 data format precision for model weights. This partition might have a better price to performance ratio compared an NVIDIA L4.
     * Partition it to two instances (each instance provides 48 GB of accelerator memory), and run small model inference workloads, such as models that have approximately 15 billion parameters and use FP16 data format precision for model weights. This partition might be an alternative to running inference workloads on an NVIDIA A100 40 GB GPU.

For more information, see [Running multi-instance GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus-multi).

For more information, see [GPU machine types](https://docs.cloud.google.com/compute/docs/gpus) and [Accelerator-optimized machine family](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) in the Compute Engine documentation.

  3. **Select an inference distribution strategy** : if your model is too large for a single accelerator, select a distribution strategy based on your workload's requirements.

First, choose a distribution strategy based on the topology of your hardware:

     * **Single accelerator** : if your model fits on a single accelerator, this is the simplest and recommended approach.
     * **Single-node, multi-accelerator** : if your model fits on a single node with multiple accelerators, you can use tensor parallelism to distribute the model across the accelerators on that node.
     * **Multi-node, multi-accelerator** : if your model is too large for a single node, you can use a combination of tensor and pipeline parallelism to distribute it across multiple nodes.

To implement these strategies, you can use the following parallelism techniques:

     * **Tensor parallelism** : this technique shards a model's layers across multiple accelerators. It is highly effective within a single node with high-speed interconnects like NVLINK or or direct peer-to-peer PCIe, but it requires significant communication between accelerators.

#### Example: Tensor parallelism

For example, consider that you need to deploy a model with 109 billion parameters. At its default BF16 (16-bit) precision, loading the model's weights into accelerator memory requires approximately 113 GB. A single NVIDIA H100 GPU provides 80 GB of memory. Therefore, even without accounting for other memory requirements such as the KV cache, you need at least two NVIDIA H100 GPUs to load the model, using a tensor parallelism size of two.

     * **Pipeline parallelism** : This technique partitions a model's layers sequentially across multiple nodes. It is well-suited for distributing a model across multiple nodes in a multi-host deployment and requires less communication between model ranks than tensor parallelism. 

#### Example: Hybrid parallelism (tensor and pipeline)

For a very large model with over 600 billion parameters, the memory requirement can exceed 1.1 TB. In a scenario with two `a3-megagpu-8g` nodes (each with eight NVIDIA H100 GPUs), the total cluster has 1.28 TB of accelerator memory. To run the model, you would implement a hybrid strategy: 8-way tensor parallelism within each node, and 2-way pipeline parallelism across the two nodes. The model would be split into two stages, with the first half of the layers on the first node and the second half on the second node. When a request arrives, the first node processes it and sends the intermediate data over the network to the second node, which completes the computation.

For more guidelines about choosing a distributed inference strategy for a single-model replica, see [Parallelism and Scaling](https://docs.vllm.ai/en/stable/serving/parallelism_scaling.html) in the vLLM documentation.

  4. **Select an accelerator-optimized machine type** : based on your choice of accelerator and the number you require, select a machine type that provides those resources. Each machine type offers a specific combination of vCPUs, system memory, and network bandwidth, which can also impact the performance of your workload. For example, if you need 16 NVIDIA H100 GPUs, you would select the `a3-megagpu-16g` machine type.

  5. **Run your own benchmarks** : the performance of your inference workload is highly dependent on your specific use case. Run your own benchmarks to validate your choices and fine-tune your configuration.




### Optimize the configuration of your inference server

To achieve optimal performance when you deploy your inference workload, we recommend a cycle of benchmarking and tuning:

  1. Start with the [GKE Inference Quickstart](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/inference-quickstart) to get an optimized baseline Kubernetes configuration for your use case.
  2. Run benchmarks to capture baseline throughput and latency metrics.
  3. Tune the configuration of your inference server.
  4. Run benchmarks again and compare the results to validate your changes.



The following recommendations are based on the [`vLLM`](https://docs.vllm.ai/en/latest/index.html) inference server, but the principles apply to other servers as well. For detailed guidance on all available settings, see the [vLLM Optimization and Tuning](https://docs.vllm.ai/en/latest/configuration/optimization/) documentation:

  * **Configure parallelism** : 
    * **Tensor Parallelism (`tensor_parallel_size`)**: set this to the number of accelerators on a single node to shard the workload. For example, setting `tensor_parallel_size=4` will distribute the workload across four accelerators. Be aware that increasing this value can lead to excessive synchronization overhead.
    * **Pipeline Parallelism (`pipeline_parallel_size`)**: set this to the number of nodes you are distributing your model across. For example, if you are deploying across two nodes with eight accelerators each, you would set `tensor_parallel_size=8` and `pipeline_parallel_size=2`. Increasing this value can introduce latency penalties.
  * **Tune the KV cache (`gpu_memory_utilization`)**: this parameter controls the percentage of GPU memory reserved for the model weights, activations, and the KV cache. A higher value increases the KV cache size and can improve throughput. We recommend setting this to a value between `0.9` and `0.95`. If you encounter out-of-memory (OOM) errors, lower this value.
  * **Configure maximum context length (`max_model_len`)**: to reduce KV cache size and memory requirements, you can set a lower maximum context length than the model's default. This can enable you to use smaller, more cost-effective GPUs. For example, if your use case only requires a context of 40,000 tokens, but your model's default is 256,000, setting `max_model_len` to 40,000 will free up memory for a larger KV cache, potentially leading to higher throughput.
  * **Configure the number of concurrent requests (`max_num_batched_tokens`, `max_num_seqs`)**: tune the maximum number of requests that vLLM processes concurrently to avoid preemption when the KV cache is low on space. Lower values for `max_num_batched_tokens` and `max_num_seqs` reduce memory requirements, while higher values can improve throughput at the risk of OOM errors. To find the optimal values, we recommend running performance experiments and observing the number of preemption requests in the Prometheus metrics that vLLM exports.



For more information, see the following resources:

  * For a deep dive on how to tune these parameters, see [vLLM Performance Tuning: The Ultimate Guide to xPU Inference Configuration](https://cloud.google.com/blog/topics/developers-practitioners/vllm-performance-tuning-the-ultimate-guide-to-xpu-inference-configuration).
  * For more guidance on model memory optimization, see [Best practices for optimizing large language model inference with GPUs on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/llm-optimization).
  * For a complete, deployable example, see the [GKE Inference reference implementation](https://github.com/GoogleCloudPlatform/accelerated-platforms/blob/main/platforms/gke/base/use-cases/inference-ref-arch/terraform/README.md).



## Optimize for latency and availability

To ensure your inference service is both responsive and reliable, you must optimize for low startup latency and high resource availability.

### Optimize inference workload cold start latency

Minimizing the time it takes for your inference workloads to start is critical for both cost-efficiency and user experience. A low cold-start latency lets your cluster scale up quickly to meet demand, ensuring a responsive service while minimizing the need for costly over-provisioning.

#### Optimize Pod startup time

The time it takes for a Pod to become ready is largely determined by the time it takes to pull the container image and download the model weights. To optimize both, consider the following strategies:

  * **Accelerate model loading with an optimized data loader** : the method you use to store and load your model weights has a significant impact on startup time. For vLLM versions 0.10.2 and later, the recommended approach is to use the [Run:ai Model Streamer](https://docs.vllm.ai/en/stable/models/extensions/runai_model_streamer.html) to load models by streaming them directly from a Cloud Storage bucket.

If the streamer isn't available for your use case, you can [mount a Cloud Storage bucket using Cloud Storage FUSE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-ephemeral) and tune its performance by enabling [hierarchical namespaces](https://docs.cloud.google.com/storage/docs/hns-overview) and using techniques like parallel downloads and pre-fetching. To learn more about these techniques, see [Optimize Cloud Storage FUSE CSI driver for GKE performance](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cloud-storage-fuse-csi-driver-perf). In either case, we recommend using [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) to create high-performance zonal read caches for your buckets, and enabling [Uniform bucket-level access](https://docs.cloud.google.com/storage/docs/uniform-bucket-level-access) to uniformly control access to your buckets.

If you are already using [Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/overview) for high-performance file storage for your training workloads, you can also use it to load model weights for inference. This approach offers low-latency access when data locality and POSIX compatibility are critical.

  * **Enable Image Streaming** : to reduce the time it takes to pull your container images, enable [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) on your GKE cluster. Image streaming allows your containers to start before the entire image has been downloaded, which can dramatically reduce Pod startup time.




#### Enable fast-starting nodes

For workloads that require rapid scaling, you can take advantage of [fast-starting nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/fast-starting-nodes) in GKE. Fast-starting nodes are pre-initialized hardware resources that have a significantly shorter startup time than standard nodes. If your cluster meets the [requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/fast-starting-nodes#requirements), GKE automatically enables fast-starting nodes.

### Plan flexibility, efficiency, and availability of accelerator capacity

High-demand accelerators like GPUs and TPUs can have limited availability, so a proactive capacity planning strategy is essential.

#### Plan and reserve capacity

High-demand accelerators can have limited availability, so a proactive capacity planning strategy is essential. To guarantee access to the resources you need, follow these recommendations:

  * **Determine capacity baseline and peak handling** : plan the baseline accelerator capacity you need to reserve. The amount to reserve depends on your use case. For example, you might reserve 100% of the required capacity for critical workloads with no tolerance for delays, or you might reserve a certain percentile (like the 90th or 95th) and acquire the rest on-demand to handle peaks.

  * **Reserve baseline capacity** : to get resources with a high level of assurance, create [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview). You can choose a reservation type based on your needs. For example, to reserve high-demand resources like accelerators for a specific future timeframe, you can create [future reservations in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

  * **Orchestrate capacity for peaks** : for demand that exceeds your baseline reservations, you can implement a fall-back strategy using other capacity types like on-demand, [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms), or the [Dynamic Workload Scheduler (DWS)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws). You can automate this fallback strategy by using custom ComputeClasses to define a priority order for provisioning different capacity types.

  * **Get access to discounted prices** : for your baseline capacity, purchase [committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts) to get deeply discounted prices in exchange for a one- or three-year commitment.




#### Use Dynamic Workload Scheduler with flex-start provisioning mode if your workloads tolerate delays in acquiring capacity

For workloads that can tolerate some delay in acquiring capacity, the [Dynamic Workload Scheduler (DWS) with flex-start provisioning mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws) is an option for obtaining accelerators at a discounted price. DWS lets you queue requests for capacity for up to seven days.

When using DWS with flex-start provisioning mode, we recommend the following:

  * **Incorporate it into a ComputeClass** : use a ComputeClass to define DWS as part of a prioritized fallback strategy for acquiring capacity.
  * **Set a maximum runtime duration** : the `maxRunDurationSeconds` parameter sets the maximum runtime for nodes requested through DWS. Setting this to a value lower than the default of seven days can increase your chances of getting the requested nodes.
  * **Enable node recycling** : to prevent downtime for your workloads, enable [node recycling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dws#node-recycling). This feature begins provisioning a new node before the old one expires, ensuring a smoother transition.
  * **Minimize disruptions** : to minimize disruptions from node eviction and upgrades, configure [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), [disable node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#disable), and take advantage of the short-lived upgrades strategy.



#### Use ComputeClasses

[ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) are a GKE feature that lets you define a prioritized list of infrastructure configurations for your workloads. ComputeClasses provide key capabilities designed to improve the flexibility, efficiency, and availability of accelerator capacity:

  * **Fallback compute priorities** : you can define a prioritized list of configurations. If your preferred option is unavailable during a scale-up event, the autoscaler automatically falls back to the next one on the list, significantly increasing the likelihood of successfully acquiring capacity.
  * **Active migration to higher-priority nodes** : when you configure this feature, GKE automatically replaces nodes running on lower-priority configurations with nodes from higher-priority configurations as they become available. This helps ensure that your Pods eventually run on your most preferred (and often most cost-effective) nodes.



With ComputeClasses, you can create a fallback strategy for acquiring nodes. This strategy uses a prioritized list of different capacity types, such as on-demand VMs, Spot VMs, or reservations. Each of these capacity types has a different level of availability:

  * **Reservations** : provide the highest level of assurance for obtaining capacity. When consuming reservations with ComputeClasses, consider their restrictions. For example, some reservation types limit the machine types you can reserve or the maximum number of machines you can request.
  * **On-demand** : the standard provisioning model, which offers flexibility but might be subject to regional capacity constraints for high-demand resources.
  * **Spot VMs** : use spare capacity at a lower price but can be preempted. When a preemption event happens, GKE provides a graceful termination period of up to 30 seconds to affected Pods on a best-effort basis. To take advantage of this, make your workloads tolerant to preemption events by implementing checkpoints and retry mechanisms.
  * **Dynamic Workload Scheduler (DWS)** : lets you queue requests for scarce resources at discounted prices. This feature is ideal for workloads that can tolerate delays in acquiring capacity.



The order of your priority list should change depending on whether your primary goal is minimizing latency or optimizing for cost. For example, you can configure the following priority lists for different workload requirements:

Priority | Low-Latency Workloads | Cost-Optimized (Latency-Tolerant) Workloads  
---|---|---  
1 | Reservations (Specific, then any) | Reservations (Specific, then any)  
2 | On-demand | Spot VMs  
3 | Spot VMs | Dynamic Workload Scheduler  
4 | Dynamic Workload Scheduler | On-demand  
  
For low-latency use cases, on-demand capacity is prioritized after reservations because it reports capacity shortages quickly, allowing the ComputeClass to rapidly fall back to the next option.

For cost-optimized use cases, Spot VMs and DWS with flex-start are prioritized after reservations to take advantage of lower costs. On-demand capacity is used as the final fallback.

#### Configure the location policy of your GKE clusters and node pools

The Cluster Autoscaler's [location policy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler#balancing_across_zones) controls how GKE distributes nodes across zones during a scale-up event. This setting is particularly important when using ComputeClasses because it determines which zones the Cluster Autoscaler will consider before applying the ComputeClass's priority list.

To improve your chances of obtaining accelerators, configure the location policy based on your workload's requirements:

  * **`location-policy=ANY`** : prioritizes obtaining capacity over balancing nodes evenly across zones. This setting is particularly relevant when your ComputeClass includes Spot VMs or machine types with variable availability, as `ANY` allows the Cluster Autoscaler to pick the zone with the best chance of fulfilling the ComputeClass's prioritized node types. Use this setting also to prioritize the use of unused reservations. When using this policy, we recommend that you start with `num-nodes=0` to give the Cluster Autoscaler maximum flexibility in finding capacity.

  * **`location-policy=BALANCED`** : attempts to distribute nodes evenly across all available zones. Use this policy when your workloads use easily obtainable resources and you want to maintain zonal redundancy for high availability.




You can configure this setting when you create or update a [node pool](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--location-policy).

## Optimize for efficiency and cost

By carefully monitoring your accelerators and intelligently scaling your workloads, you can significantly reduce waste and lower your operational costs.

### Observe your accelerators and inference servers

A comprehensive observability strategy is essential for understanding the performance and utilization of your inference workloads. GKE provides a suite of tools to help you monitor your accelerators and inference servers:

  * **Monitor DCGM metrics for NVIDIA GPUs** : to monitor the health and performance of your NVIDIA GPUs, configure GKE to send [NVIDIA Data Center GPU Manager (DCGM)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dcgm-metrics) metrics to Cloud Monitoring.
  * **Enable automatic application monitoring** : to simplify the process of monitoring your inference servers, enable [automatic application monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-automatic-application-monitoring) in GKE.
  * **Instrument your workloads with OpenTelemetry** : for workloads that aren't supported by automatic application monitoring, use [OpenTelemetry](https://docs.cloud.google.com/stackdriver/docs/instrumentation/ai-agent-langgraph) to collect custom metrics and traces.



### Automatically scale your Pods

To ensure that your inference workloads can dynamically adapt to changes in demand, use a [Horizontal Pod Autoscaler (HPA)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling) to automatically scale the number of Pods. For inference workloads, it's essential to base your scaling decisions on metrics that directly reflect the load on the inference server, rather than on standard CPU or memory metrics.

To configure autoscaling for your inference workloads, we recommend the following:

  * **Configure HPA based on inference-aware metrics** : for optimal performance, configure the HPA to scale based on metrics from your inference server. The best metric depends on whether you are optimizing for low latency or high throughput.

    * **For latency-sensitive workloads** , you have two primary options:

      * **KV cache utilization** (for example, `vllm:gpu_cache_usage_perc`): this metric is often the best indicator of impending latency spikes. High utilization of the KV cache indicates that the inference engine is nearing capacity. The HPA can use this signal to preemptively add replicas and maintain a stable user experience.
      * **Number of running requests (batch size)** (for example,`vllm:num_requests_running`): this metric directly relates to latency, as smaller batch sizes typically result in lower latency. However, using it to autoscale can be challenging because maximizing throughput depends on the size of incoming requests. You might need to choose a value lower than the maximum possible batch size to ensure that the HPA scales up appropriately.
    * **For throughput-sensitive workloads** , scale based on the **queue size** (for example, `vllm:num_requests_waiting`). This metric directly measures the work backlog and is a straightforward way to match processing capacity to incoming demand. Because this metric only considers requests that are waiting and not those currently being processed, it might not achieve the lowest possible latency compared to scaling on batch size.

  * **Set a minimum number of replicas** : to ensure consistent availability and a baseline user experience, always set a minimum number of replicas for your inference deployment.

  * **Enable the Performance HPA profile** : on GKE versions 1.33 or later, the Performance HPA profile is enabled by default on qualifying clusters to improve the HPA's reaction time.




For more information, see [Configure HPA for LLM workloads on GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/machine-learning/inference/autoscaling) and [Autoscale LLM inference workloads on TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/machine-learning/inference/autoscaling-tpu).

### Move data closer to your workloads

The time it takes for your workloads to load data, such as model weights, can be a significant source of latency. By moving your data closer to your compute resources, you can reduce data transfer times and improve overall performance.

  * **Create zonal read caches with Rapid Cache** : if you use Cloud Storage to store data for your AI/ML workloads, enable [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache). Rapid Cache creates high-performance zonal read caches for your Cloud Storage buckets.
  * **Cache frequently accessed data on Local SSDs** : for workloads that require extremely low-latency access to temporary data, use [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/local-ssd) as a high-performance cache. Using Local SSDs as a low-latency, temporary storage to hold frequently used data helps you reduce the idle time of expensive resources, such as accelerators, by drastically reducing the time accelerators wait for I/O operations to complete. Note that not all machine series support Local SSDs, which can impact your choice of accelerators.
  * **Manage caches with GKE Data Cache** : for workloads that frequently read data from Persistent Disks, enable [GKE Data Cache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/data-cache). GKE Data Cache uses Local SSDs to create a managed, high-performance cache for your Persistent Disks. For most production workloads, we recommend using the `Writethrough` mode to prevent data loss by writing data synchronously to both the cache and the underlying persistent disk.



## Optimize for advanced scaling architectures

To meet the demands of large-scale or globally distributed applications, you can adopt advanced scaling architectures to enhance performance, reliability, and traffic management.

### Load balance traffic with GKE Inference Gateway

For inference workloads in a single cluster, we recommend using [GKE Inference Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-gke-inference-gateway). The Inference Gateway is an AI-aware load balancer that monitors inference metrics to route requests to the most optimal endpoint. This feature improves performance and accelerator utilization.

When using GKE Inference Gateway, we recommend that you follow these best practices:

  * **Group serving Pods into an`InferencePool`**: define an `InferencePool` for each group of Pods serving your inference workloads. For more information, see [Customize GKE Inference Gateway configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/customize-gke-inference-gateway-configurations).
  * **Multiplex latency-critical workloads** : define `InferenceObjectives` to specify your model's serving properties, such as its name and priority. GKE Inference Gateway gives preference to workloads with a higher priority, letting you multiplex latency-critical and latency-tolerant workloads and implement load-shedding policies during heavy traffic.
  * **Use model-aware routing** : to route requests based on the model name in the request body, use [body-based routing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-body-based-routing). When you use body-based routing, ensure that your backends are highly available. The gateway will return an error if the extension is unavailable, preventing requests from being routed incorrectly.
  * **Allow the gateway to automatically distribute traffic** : GKE Inference Gateway intelligently routes traffic by monitoring key metrics from the inference servers in the `InferencePool`, such as KV cache utilization, queue length, and prefix cache indexes. This real-time load balancing optimizes accelerator utilization, reduces tail latency, and increases overall throughput compared to traditional methods.
  * **Integrate with Apigee and Model Armor** : for enhanced security and management, integrate with Apigee for API management and with [Model Armor](https://docs.cloud.google.com/security-command-center/docs/model-armor-overview) for safety checks.



### Deploy inference workloads on multiple nodes

For very large models that can't fit on a single node, you need to distribute your inference workload across multiple nodes. This requires an architecture that minimizes inter-node communication latency and ensures that all components of the distributed workload are managed as a single unit.

Consider these best practices:

  * **Maximize accelerator network bandwidth and throughput** : when a workload is distributed across multiple nodes, the network becomes a critical performance factor. To minimize inter-node communication latency, use high-performance networking technologies like [NVIDIA GPUDirect](https://developer.nvidia.com/gpudirect). Depending on the scale of your cluster and the intensity of communication your workload requires, you can choose from these options:

    * **GPUDirect-TCPX** : effective for a range of multi-node inference workloads running on A3 High.
    * **GPUDirect-TCPXO** : offers enhanced performance with greater offload and higher bandwidth, which is beneficial for larger clusters compared to standard TCPX, and runs on A3 Mega machines.
    * **GPUDirect RDMA** : provides the highest inter-node bandwidth and lowest latency by allowing direct memory access between GPUs across different nodes, bypassing the CPU, and is best suited for the most demanding, large-scale inference scenarios on A3 Ultra and A4 machines.

For more information, see:

    * [Maximize GPU network bandwidth in Standard mode clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx).
    * [Maximize GPU network bandwidth in Autopilot mode clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpu-bandwidth-gpudirect-tcpx-autopilot).

To validate that your multi-node network configuration is performing as expected, we recommend that you run tests with tools like the [NVIDIA Collective Communications Library (NCCL)](https://developer.nvidia.com/nccl).

  * **Use LeaderWorkerSet to manage distributed workloads** : when you deploy a stateful distributed workload, such as a multi-node inference service, it's essential to manage all of its components as a single unit. To do this, use [LeaderWorkerSet](https://lws.sigs.k8s.io/docs/overview/), a Kubernetes-native API that lets you manage a group of related Pods as a single entity. A LeaderWorkerSet ensures that all Pods in the set are created and deleted together, which is critical for maintaining the integrity of a distributed workload.

  * **Place nodes in physical proximity using compact placement** : the physical distance between the nodes in your distributed workload can have a significant impact on inter-node network latency. To minimize this latency, use a [compact placement policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/compact-placement) for your GKE node pools. A compact placement policy instructs GKE to place the nodes in a node pool as physically close to each other as possible within a zone.




### Deploy inference workloads across multiple regions

For globally distributed applications that require high availability and low latency, deploying your inference workloads across multiple regions is a critical best practice. A multi-region architecture can help you increase reliability, improve the flexibility, efficiency, and availability of accelerator capacity, reduce user-perceived latency, and meet location-specific regulatory requirements.

To effectively deploy and manage a multi-region inference service, follow these recommendations:

  * Provision GKE clusters in multiple regions where you have reserved capacity or anticipate needing capacity to handle peak loads.
  * Choose the right storage strategy for your model weights. To optimize for operational efficiency, create a multi-region Cloud Storage bucket. To optimize for cost, create a regional bucket in each region and replicate your model weights.
  * Use [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) to create zonal read caches for your Cloud Storage buckets to reduce both network latency and data egress costs.



## Summary of best practices

The following table summarizes the best practices recommended in this document:

Topic | Task  
---|---  
Deployment and configuration | 

  * Analyze the characteristics of your inference use case
  * Choose the right models for your inference use cases
  * Apply quantization to the model
  * Choose the right accelerators
  * Choose your inference distribution strategy
  * Optimize the configuration of your inference server

  
Cold start latency | 

  * Optimize Pod startup time
  * Enable fast-starting nodes

  
Capacity planning, flexibility, efficiency, and availability | 

  * Plan and reserve capacity
  * Use Dynamic Workload Scheduler
  * Use ComputeClasses
  * Configure the location policy of your GKE clusters and node pools

  
Resource and accelerator efficiency | 

  * Observe your accelerators and inference servers
  * Automatically scale your Pods
  * Move data closer to your workloads

  
Load balancing | 

  * Use GKE Inference Gateway for single-cluster deployments

  
Multi-node deployments | 

  * Maximize accelerator network bandwidth and throughput
  * Use LeaderWorkerSet to group Pods
  * Place nodes in physical proximity using compact placement

  
Multi-region deployments | 

  * Provision GKE clusters in multiple regions
  * Load balance traffic across regions
  * Store model weights in Cloud Storage buckets
  * Cache data with Rapid Cache

  
  
## What's next

  * See the [GKE Inference reference architecture](https://github.com/GoogleCloudPlatform/accelerated-platforms/tree/main/docs/platforms/gke/base/use-cases/inference-ref-arch).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
