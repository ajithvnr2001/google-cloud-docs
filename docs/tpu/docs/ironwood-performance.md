---
url: https://docs.cloud.google.com/tpu/docs/ironwood-performance/
title: TPU7x (Ironwood) performance optimizations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:18.872327+00:00
---

# TPU7x (Ironwood) performance optimizations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/ironwood-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TPU7x (Ironwood) performance optimizations

This guide describes several methods to optimize performance with TPU7x (Ironwood) by efficiently managing data movement between its multi-tiered memory system. This includes techniques like low-precision training, sharding, communication optimization, activation rematerialization, scoped virtual memory tuning, and custom accelerator kernels.

To optimize performance with TPU7x, you must first be familiar with the Ironwood architecture, specifically the memory hierarchy and interconnect topology. For more information, see [TPU7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x).

## Low-precision training with FP8

FP8 (8-bit floating point) is an efficient numerical data format used primarily to accelerate model training and inference. By representing numbers using 8 bits – rather than the standard 16-bit formats (FP16 or BF16) and 32-bit (FP32) – TPUs can process data significantly faster and use less memory.

TPU7x supports built-in hardware acceleration for FP8 data types, offering a peak theoretical performance of 4614 TFLOPS per chip. This capability can lead to significantly faster end-to-end training times. For compatible operations, particularly dense matrix multiplications that are common for AI workloads, using FP8 can yield performance improvements of 1.3x over standard BF16 training. Compared to BF16, FP8 doubles peak FLOPs and halves memory footprint for weights and activations. FP8 should be a primary tuning lever for both compute-bound workloads and scenarios that are constrained by memory capacity or bandwidth.

Using FP8 offers the following performance benefits:

  * **Reduced high-bandwidth memory (HBM) pressure** : A smaller memory footprint allows larger models, or models with larger KV caches during inference, to fit entirely within the 192 GB of HBM. This avoids costly offloading to slower host memory.
  * **Increased effective batch size** : By reducing the memory required for activations, FP8 enables the use of larger batch sizes. This improves data parallelism and can lead to higher throughput and better utilization of the compute units.
  * **Lower memory bandwidth requirements** : Moving half the amount of data for each operation reduces the demand on the HBM-to-MXU data path. On systems where data movement is a common bottleneck, this helps keep the MXUs saturated with work.



Using FP8 with zero or limited degradation in performance requires the careful selection of quantization techniques. Here are some best practices to consider for FP8 training:

  * **Scaling granularity** : Start with per-tensor scaling as the baseline. If there are quality or performance issues, switch to per-axis scaling. Subchannel scaling may be unnecessary.
  * **Scaling mode** : Dynamic scaling, which computes scaling factors at runtime, is a good default for maintaining quality. While static scaling can offer a significant performance boost by eliminating computations, it requires careful profiling to determine the correct scaling factors and may not be suitable for all use cases, especially when model configurations change. Conversely, some robust models and configurations can fix the scale to the FP8 limit for weights or activations, allowing you to reduce quantization overhead while maintaining accuracy and improving performance.
  * **FP8 formats (E4M3 and E5M2)** : A common and effective approach is to use a mix of FP8 formats. For example, use E4M3 for weights and activations in the forward pass to take advantage of the higher precision of E4M3, and use E5M2 for gradients in the backward pass to accommodate for the wider dynamic range of the gradients.
  * **Rounding** : Using "round to nearest even" (RNE) instead of stochastic rounding for gradients can maintain quality while offering better performance and reproducibility.
  * **Enabling FP8 in MaxText** : [MaxText](https://maxtext.readthedocs.io/en/latest/) supports FP8 training through the QWIX quantization library. To activate quantization, set the following flag in your configuration: `use_qwix_quantization=true`.



## Sharding and parallelism

Sharding is the process of slicing a large model or its training data into smaller pieces and distributing them across multiple TPU chips or cores. Choosing the right sharding strategy is important for achieving high performance on TPU7x.

A naive approach that purely maximizes the degree of parallelism will often result in poor performance by becoming communication-bound. The best approach is often to select the simplest sharding strategy that meets memory constraints, as this minimizes communication overhead and allows the compute units to be efficiently utilized.

Before selecting a sharding strategy, the first step in any performance tuning effort should be an arithmetic intensity analysis. This analysis determines whether a given computation is limited by compute, memory bandwidth, or interconnect bandwidth. It is calculated as the ratio of floating-point operations to the bytes of data that must be moved.

A high arithmetic intensity indicates a compute-bound workload. A low arithmetic intensity suggests a memory- or communication-bound workload, where performance is limited by the speed at which data can be moved from HBM or across the ICI network. This analysis informs the ideal batch size and sharding strategy. For example, a communication-bound workload won't benefit from a sharding strategy that introduces even more communication, such as high-degree tensor parallelism.

### Sharding strategy decision framework

MaxText offers a variety of sharding strategies. The optimal choice depends on the model architecture, sequence length, and the need to balance computational load against communication overhead.

  * **Fully Sharded Data Parallelism (FSDP)** : This is the preferred default strategy for data parallelism. FSDP shards the model weights, gradients, and optimizer states across the data-parallel devices. During computation, each device performs an All-Gather operation to retrieve the necessary full weights for its local microbatch. FSDP is highly effective as long as the per-device batch size is large enough to hide the latency of this All-Gather communication. For Mixture-of-Experts (MoE) models, the arithmetic intensity calculation must account for sparsity.
  * **Tensor Parallelism (TP)** : TP shards individual tensors across devices. Typically, the tensors are weight matrices in multilayer perceptron (MLP) and attention blocks. The hardware's high arithmetic intensity (11.5k) imposes a very high requirement on the model's dimensions to make TP viable over ICI, and attempting to use TP can result in the system being communication-bound.
  * **Expert Parallelism (EP)** : This is the standard and necessary strategy for training MoE models. EP shards the "expert" layers across a set of devices, and an All-to-All communication collective is used to route tokens to their designated expert device. EP can be efficient if the model's MLP dimension is large enough to approach the roofline.
  * **Context Parallelism (CP)** : CP is a specialized strategy that is essential for training models with very long sequence lengths. Its primary function is to manage the memory consumption of activations, which grows quadratically with sequence length and can exceed HBM capacity. CP shards the sequence dimension of the activation tensors, which allows for the use of a fractional per-device batch size. Because CP introduces more communication than FSDP, the general rule is to use the minimum degree of CP necessary to satisfy memory constraints and ensure the batch axis shard remains an integer.



The following table maps common workload types to the optimal sharding strategy:

Workload type | Recommended primary sharding | Secondary sharding | Key bottlenecks | Rationale  
---|---|---|---|---  
Dense model - short sequence | FSDP | N/A | Rematerialization, FF Matmuls | FSDP provides the best balance. With short sequences, activation memory may not be a major concern. The key is a large enough global batch to hide FSDP's weight All-Gather. As the batch size increases, activation size increases, and a suitable rematerialization policy is required to ensure this configuration does not run out of memory.  
Dense model - long sequence | FSDP | CP | Flash attention, activation memory | Activation memory becomes the primary constraint. CP is required to enable fractional per-device batch sizes and avoid out-of-memory (OOMs) issues. Flash attention is the dominant source of compute and wasted time.  
MoE model - short sequence | FSDP + EP | N/A | All-to-All (Expert routing), rematerialization | MoE models require EP to shard the experts. The All-to-All communication for token routing is a major bottleneck that must be overlapped. Rematerialization is also a significant source of waste.  
MoE model - very large scale | FSDP + EP + PP | Model parallelism (MP) | All previously mentioned bottlenecks, plus pipeline bubbles | For models that exceed the memory of a single pod, PP is needed to shard layers across pods. This introduces DCN communication and pipeline bubble overheads. This is a highly complex configuration requiring careful tuning.  
  
## Communication optimization

The primary mechanism for overlapping communication and computation on TPU7x is called _SparseCore Collective Offloading_. The Ironwood architecture includes dedicated SparseCore units, which act as independent threads of control capable of managing data movement over the ICI fabric. This allows collective communication operations (like All-Gather or Reduce-Scatter) to execute in parallel with the main computations happening on the TensorCores. This is the recommended method for asynchronous collectives on TPU7x. Use the [recommended flags](https://github.com/AI-Hypercomputer/maxtext/blob/c0abc4c0c0a98e02413d7b6c669927d013467045/benchmarks/xla_flags_library.py#L70-L116) to enable offloading for the most common collectives.

## Activation rematerialization

Activation rematerialization, also known as gradient checkpointing, is a fundamental technique for reducing the HBM footprint of a model. Instead of storing all intermediate activations from the forward pass in HBM to be used during the backward pass, it saves only a few key activations (checkpoints) and recomputes the others on-demand during the backward pass. This saves a significant amount of memory at the cost of increased computation (approximately 25-30% additional FLOPs for a standard transformer block).

The decision of how aggressively to apply rematerialization is a critical tuning parameter that depends entirely on the primary bottleneck, which often varies with sequence length.

**For long-sequence workloads** (such as 128k): In these cases, the size of the activation tensors is the dominant consumer of HBM. The workload is typically memory-bound. Therefore, applying an aggressive rematerialization policy is highly beneficial. The memory savings enable training to proceed without out-of-memory errors and also allow for larger batch sizes, and the computational overhead of recomputing is a worthwhile trade-off.

**For short-sequence workloads** (such as 8k): In these cases, activation memory is much less of a concern, and the workload is more likely to be compute-bound. The computational overhead of rematerialization can be the single largest source of inefficiency.

### Tuning rematerialization policies in MaxText

MaxText provides granular control over rematerialization through a set of preset and custom policies, configured using the `remat_policy` flag.

#### Preset policies

MaxText offers the following built-in policies:

  * **`full`** : The most aggressive policy, rematerializing almost everything. This minimizes HBM usage but maximizes recomputation overhead. Ideal for extremely memory-constrained, long-sequence scenarios.
  * **`minimal`** : The least aggressive policy, storing most activations. This maximizes HBM usage but minimizes recomputation. Best for short-sequence, compute-bound workloads where memory is not a concern.
  * **Intermediate policies** : Options like `save_dot_with_context_except_mlp`, `save_qkv_proj`, and `save_out_proj` provide various trade-offs by selectively checkpointing the outputs of expensive dot-product operations while rematerializing cheaper element-wise operations.



#### Custom policies

For a greater level of control, you can set `remat_policy` to `custom`. This lets you specify the behavior for individual layers within the model's decode module. Each layer can be assigned one of three behaviors:

  * **`device`** : The activation is stored in HBM on the TPU device.
  * **`remat`** : The activation is discarded and will be rematerialized during the backward pass.
  * **`offload`** : The activation is moved from HBM to the CPU host's memory, freeing up HBM at the cost of PCIe transfer latency.



## Scoped VMEM tuning

Kernel performance, like flash attention, depends on the selected tile sizes in the kernel, whose size is limited by the available vector memory (VMEM). Each of the two TensorCores in a TPU7x chip has 64 MiB of vector memory (VMEM). This VMEM capacity can be split between current scope (scoped VMEM) and future weight prefetch. Increasing scoped VMEM allows increasing the tile sizes in the kernel, potentially reducing memory stalls and increasing kernels' performance. You can alter the scoped VMEM size by setting `xla_tpu_scoped_vmem_limit_kib` (in `LIBTPU_INIT_ARGS`), which can be used to explore the kernel performance as well as end-to-end performance limits. Optimizing scoped VMEM size can indirectly affect custom Pallas kernel performance since increasing scoped VMEM unlocks a larger hyperparameter search space for in-kernel tile sizes.

## Tokamax kernels

[Tokamax](https://github.com/openxla/tokamax/tree/main), a high-performance JAX kernels library with many highly optimized TPU kernels, addresses several common hardware-specific bottlenecks:

  * **Splash attention** : Splash attention is used as the primary attention implementation to eliminate the HBM bottleneck of standard attention and uses the most efficient attention implementation on TPUs.
  * **Megablox Grouped Matrix Multiplication (GMM)** : For MoE workloads, Megablox efficiently handles grouped matrix multiplications by computing over the ragged activations representation. It efficiently maps over the ragged dimension, computing matrix multiplications between ragged groups of rows in LHS, and the corresponding expert matrix, avoiding the need to pad batches to a fixed size.
  * **Empirical tuning with`tune-jax`**: The `tune-jax` library has utilities to perform empirical searches for optimal block sizes. Default kernel sizes are often suboptimal; tuning allows choosing hardware-friendly VMEM tile sizes to maximize hardware utilization.
  * **Max logits estimate** : The Tokamax Splash attention kernel can further be optimized by setting a value for `max_logit_const`. If set, it replaces the reduction calculation of the max logit during the softmax operation of attention (softmax(Q * KT)), reducing some computational and synchronization overhead. In MaxText, it is implemented by the config `use_max_logits_estimate`, which can be set to `None` (disabled) or a floating point value. Verify that the logit range of your specific model remains compatible with the estimate to prevent numerical overflow. Convergence testing is recommended if this value is set.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
