---
url: https://docs.cloud.google.com/tpu/docs/performance-guide/
title: Cloud TPU performance guide \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:19.719900+00:00
---

# Cloud TPU performance guide  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/performance-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud TPU performance guide

Your first step when troubleshooting TPU performance is to profile your model. For more information on capturing a performance profile, see [Profile your model](https://docs.cloud.google.com/tpu/docs/profile-tpu-vm).

## TPU model performance

This section describes general issues that can reduce model performance and how you can address them.

### Input-bound models

TPUs perform calculations very fast. To ensure the TPU is not idle, it is important to make sure there is a steady stream of data being loaded onto the TPU. How this is done depends on how you load and preprocess your dataset. For example, you can read datafiles in parallel using [tf.data.TFRecordset()](https://www.tensorflow.org/api_docs/python/tf/data/TFRecordDataset) and the `num_parallel_reads` parameter.

### Small batch size due to sharding

The TPU runtime splits a batch across all 8 cores of a TPU device (for example v2-8 or v3-8). If you specify a global batch size of 128, each core receives a batch size of 16 (128 / 8).

For optimum memory usage, use the largest batch size that fits into TPU memory. Each TPU core uses two-dimensional 8 X 128 vector registers for processing matrix multiplications. In general, your batch size should be evenly divisible by 8 or 128.

### Memory management tuning

You can use memory-related environment variables to fine-tune low-level runtime behaviors.

#### `TPU_PREMAPPED_BUFFER_SIZE`

`TPU_PREMAPPED_BUFFER_SIZE` sets the size of the host memory buffer (in bytes) that is pre-mapped and pinned for use by the TPU runtime for data transfers (for example, DMA). The default value is 4294967296 bytes. The value must be a multiple of 2^12 (4KB = 4 * 1024 Bytes = 4096 = 2^12).

The following examples are valid `TPU_PRE_MAPPED_BUFFER_SIZE` values.
    
    
    17179869184 = 2^34 = 2^22 * 2^12 (2^22 4KB pages will be premapped).
    40000000000 = 5^10 * 2^12 = (5^10 4KB pages will be premapped).
    

Increasing this size can potentially improve data transfer performance between the host and TPU device, especially for workloads with large tensors or frequent host-device communication. However, it also increases the amount of pinned host memory, reducing memory available for other processes.

#### Troubleshoot memory issues

If the pre-mapped buffer region isn't large enough to allocate memory during program runtime, the workload will fail and return a `RESOURCE_EXHAUSTED` error similar to:

"Allocating buffer from premmaped region failed with: `RESOURCE_EXHAUSTED`: Attempting to allocate `allocation_size`. That was not possible. There are `available_size` free."

If the buffer is excessively large, TPU initialization can take much longer (potentially more than 15 seconds), making it seem as if the TPU is stuck.

To diagnose this, inspect the TPU runtime logs. These logs detail the operations being performed, including the pre-mapping of buffers. You can find the logs at /tmp/tpu_logs/tpu_driver.INFO or print them directly to the console by setting the environment variable TPU_STDERR_LOG_LEVEL=0. This setting will generate output similar to:
    
    
    I0604 12:45:24.926233   62136 tpu_hal.cc:214] Starting premapped memory manager initialization...
    I0604 12:45:29.411218   62136 system.cc:1059] tpu::System initialized, current host id: 0, logical device ids: 0
    I0604 12:45:29.411244   61600 tfrt_tpu_system_state.cc:216] CreateTpuSystemState: TPU initialization is successful and it took 5.583190661s
    I0604 12:45:29.411267   61600 tfrt_tpu_system_state.cc:220] CreateTpuSystemState: using TPU host premapped buffer of size: 4294967296
    

This output will tell you how long it took to initialize the TPU and the size of the premapped buffer.

#### Set buffer size

If the premapped buffer is too small or too large, you can manually set the buffer size using the following environment variables.

  * `TPU_PREMAPPED_BUFFER_SIZE`: Sets the total size (in bytes) of the pre-mapped buffer region.

  * `TPU_PREMAPPED_BUFFER_TRANSFER_THRESHOLD_BYTES`: Sets the maximum size of a single buffer that can be allocated from the pre-mapped region.




For example, you can:
    
    
    export TPU_PREMAPPED_BUFFER_SIZE=4294967296
    

to set the buffer size and:
    
    
    export TPU_PREMAPPED_BUFFER_TRANSFER_THRESHOLD_BYTES
    

to enable it.

This export sets the size to the default.

Adjust the value of `TPU_PREMAPPED_BUFFER_SIZE` if you suspect host-device data transfer is a bottleneck. Monitor host memory usage and model performance to find an optimal balance. The default value is typically sufficient for most use cases.

#### Host memory spaces: `pinned_host` versus `unpinned_host`

In JAX on Cloud TPU, `memory_kind="unpinned_host"` and `memory_kind="pinned_host"` use different host memory allocation and transfer paths:

  * `unpinned_host` (and standard device-to-host transfers such as `copy_to_host_async()` or `np.asarray()`): stages DMA transfers through the pre-mapped buffer pool configured by `TPU_PREMAPPED_BUFFER_SIZE` when the transfer size is smaller than `TPU_PREMAPPED_BUFFER_TRANSFER_THRESHOLD_BYTES`. After the DMA transfer into the pre-mapped staging buffer completes, the runtime converts the tensor from the tiled TPU device layout into the untiled CPU layout in regular host memory and immediately returns the staging buffer to the pre-mapped pool. This path avoids per-transfer DMA mapping system calls.
  * `pinned_host`: allocates and pins dedicated DMA pages separate from the `TPU_PREMAPPED_BUFFER_SIZE` pool. The runtime maps these pages for DMA when the buffer is created and unmaps them when the buffer is freed. Tensors in `pinned_host` retain their tiled TPU device layout in host memory, so transfers between TPU high-bandwidth memory (HBM) and `pinned_host` perform direct DMA without CPU layout conversion.



Choose the memory kind that matches your workload's transfer pattern:

  * **Use`unpinned_host` (or `copy_to_host_async()`)** when transferring data to the host for CPU consumption—such as logging, metrics, NumPy conversion, or checkpoint serialization—or when allocating new host buffers on every step. Because these transfers reuse the pre-mapped buffer pool and produce untiled CPU arrays, they avoid repeated DMA mapping and unmapping overhead.
  * **Use`pinned_host`** when offloading tensors from TPU HBM to host memory to copy back to TPU HBM later (such as activation offloading with `jax.remat`, parameter or optimizer state offloading, and KV cache offloading), or when passing host-resident arrays directly as inputs or outputs of a `jax.jit` compiled function. When using `pinned_host` across multiple steps, reuse or donate the buffers instead of allocating and freeing them on every step to avoid repeated DMA mapping system calls.



### tcmalloc configuration

The `tcmalloc` library is used by default on Cloud TPU VMs to improve performance for models with sizable, frequent memory allocations. This is configured through the `LD_PRELOAD` environment variable.

However, for some workloads (for example, DLRM with very large embedding table allocations), `tcmalloc` can cause a slowdown. In such cases, you can revert to the standard `malloc` function by unsetting the `LD_PRELOAD` variable in your shell session before running your training script:
    
    
    unset LD_PRELOAD
    

## Network performance optimizations

The following sections describe how to optimize your network performance by configuring the maximum transmission unit (MTU) and using multi-NIC for Multislice environments.

### Configure MTU

For the best network performance, use a network with 8,896 MTU (maximum transmission unit).

By default, a Virtual Private Cloud (VPC) only provides an MTU of 1,460 bytes, which provides suboptimal network performance. You can set a VPC network's MTU to any value between 1,300 bytes and 8,896 bytes (inclusive). Common custom MTU sizes are 1,500 bytes (standard Ethernet) or 8,896 bytes (the maximum possible). For more information, see [Valid VPC network MTU sizes](https://docs.cloud.google.com/vpc/docs/mtu#valid_mtus).

For more information about changing the MTU setting for an existing or default network, see [Change the MTU setting of a VPC network](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network).

### Use the multi-NIC option for Multislice

When training large models in Multislice environments consisting of thousands of TPU chips, inter-slice communication over the data center network (DCN) can be a bottleneck. To improve network bandwidth for network-bound workloads, you can use multi-NIC to increase the number of network interfaces on your TPU VMs. When you use multi-NIC, each TPU VM is allocated additional network interfaces, each connected to a unique VPC network, increasing overall network throughput. The additional NICs must be in mutually-exclusive IP ranges.

For more information about enabling multi-networking when using Google Kubernetes Engine (GKE), see [Improve network performance without hostNetwork on TPU Trillium or Ironwood (TPU7x)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpu-multislice#enable_multi-nic).

## XLA compiler optimizations

[XLA](https://www.tensorflow.org/performance/xla/) is a compiler for machine learning that can produce binaries for TPUs, CPUs, GPUs, and other platforms. Models written in [PyTorch](https://pytorch.org/), [JAX](https://docs.jax.dev/en/latest/index.html), or [TensorFlow](https://www.tensorflow.org/) generate an XLA high-level operation (HLO) graph, which XLA compiles to a TPU executable. For more information about XLA, see [XLA: Optimizing Compiler for Machine Learning](https://www.tensorflow.org/xla).

### Padding

To use TPU memory efficiently, structure your data so that it can be tiled into 128 x 8 chunks. When the data for a matrix computation does not fill an entire 128 x 8 chunk, the XLA compiler pads tensors. There are two drawbacks to padding:

  1. Padded tensors under-utilize the TPU core.
  2. Padding increases the amount of on-chip memory storage required for a tensor and can lead to an out-of-memory error.



While padding is automatically performed by the XLA compiler when necessary, you can determine the amount of padding performed using the memory viewer tool. You can avoid padding by picking tensor dimensions that are well suited for TPU.

### Tensor dimensions

To achieve peak FLOPs, dimensions of matrix multiplication should be larger than the MXU size for the TPU version you are using. MXU size is 256 x 256 for v6e and TPU7x (Ironwood), and 128 x 128 for versions prior to v6e. For more information, see [Cloud TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture).

### Batch size

The XLA compiler rounds up the sizes of tensors stored in TPU HBM memory to perform computations more efficiently. This padding happens transparently at the hardware level and does not affect results. However, in certain cases the padding can result in significantly increased memory use and execution time.

The TPU runtime lays out tensors in memory to maximize computational efficiency and minimize padding. To minimize memory overhead and maximize computational efficiency, _one_ of the following must be true:

  1. The total batch size should be a multiple of 64 (8 per TPU core), and feature dimension sizes should be a multiple of 128.

  2. The total batch size should be a multiple of 1024 (128 per TPU core), and feature dimension sizes should be a multiple of 8.




Using a batch size of 1024 and feature dimensions that are a multiple of 128 results in the best efficiency, although this may not be possible for all models.

**Note:** _Feature dimension_ refers to the hidden size of a fully-connected layer or the number of output channels in a convolution. Not all layers can conform to this rule, especially the first and last layers of the network. This is fine, most models require some amount of padding.

### Fusion

_Fusion_ is a general technique the XLA compiler uses to optimize programs. A fused operation is the combination of multiple constituent operations that are to be executed in combination.

For example, consider the following series of operations:
    
    
        tmp = tf.add(x, y)
        result = tf.multiply(tmp, z)
    

This code is roughly equivalent to the following pseudo code:
    
    
        for (i = 0; i < element_count; i++) {
          tmp[i] = x[i] + y[i];
        }
    
        for (i = 0; i < element_count; i++) {
          result[i] = tmp[i] * z[i];
        }
    

With fusion, the array accesses happen at the same time:
    
    
        for (i = 0; i < element_count; i++) {
          result[i] = (x[i] + y[i]) * z[i];
        }
    

In this example, the number of memory round trips is reduced and XLA does not need to allocate any space for 'tmp'.

Fusion is a critical optimization and benefits the Cloud TPU in several ways:

  * It reduces memory transfers by removing the need to store intermediate results in main memory, which is slow.
  * It allows greater utilization of hardware units which would otherwise be unutilized.
  * It can reduce the memory utilization of a model as fewer buffers need to be live at the same time.



### Broadcasting

Broadcasting implicitly occurs when two tensors with different, but compatible, shapes are combined.

For example, `tf.add(vector, matrix)` requires the vector to be broadcasted to the shape of the matrix. The result of the operation has the same shape as the matrix. For more details, see the guide to [broadcasting arrays](https://docs.scipy.org/doc/numpy/user/basics.broadcasting.html).

While broadcasts can often be fused with their consumers, forcing a broadcast may result in poor performance and increased memory usage.

In the following example, the broadcast implicit in the addition of a vector and matrix cannot be fused with the argmax resulting in a materialized broadcast:

`tf.argmax(tf.add(vector, zero_matrix), axis=0)`

## Performance recommendations for the Ironwood dual-chiplet architecture

The [Ironwood](https://docs.cloud.google.com/tpu/docs/tpu7x) programming model lets you access two TPU devices instead of the single logical core (also known as [MegaCore](https://docs.jax.dev/en/latest/pallas/tpu/pipelining.html#tpus-in-megacore-configuration)) architecture used in previous generations (TPU v4 and v5p). This change improves the cost-effectiveness and efficiency of manufacturing the chip. While this represents an architectural shift, the new design ensures that you can reuse existing software models with minimal changes.

To achieve the best performance with the dual-chiplet architecture, we recommend the following approaches:

  * **Use tensor parallelism across chiplets:** The high bandwidth D2D interface is designed for efficient tensor parallelism. We recommend splitting tensors across the two on-chip devices.

  * **Utilize hierarchical collectives:** To maximize communication efficiency, take advantage of the two-level network hierarchy: the ultra-fast D2D link between on-chip chiplets and the fast ICI links within a slice. When using automatic parallelism with SPMD (single program, multiple data), the XLA compiler handles this for you by automatically generating hierarchical collective operations. When manually partitioning your model, you should also design your communication patterns around this hierarchy. Prioritize communication between the two devices on the same chip before communicating with devices on other chips.

  * **Overlap communication with computation:** To maximize hardware utilization, offload collective communication operations, such as all-reduce, to the SparseCores. These operations, which aren't bound to the matrix-multiply unit (MXU), can execute on the SparseCores concurrently while the TensorCores continue their computation. This technique can recover some of the performance benefits that were inherent to the fused operations in the previous MegaCore architecture.

  * **Offload to SparseCore for embeddings:** In the dual-chiplet design, embedding tables could be partitioned across the HBM of both chiplets. To avoid performance degradation from this lack of sharing memory, offload embedding gather operations to the SparseCore. This strategy utilizes the high-speed D2D interconnect to efficiently transfer embedding vectors between the chiplets. For more information about SparseCore and embedding models, see [A deep dive into SparseCore for Large Embedding Models (LEM)](https://openxla.org/xla/sparsecore).




For a comprehensive guide on optimizing performance on TPU7x, see [TPU7x (Ironwood) performance optimizations](https://docs.cloud.google.com/tpu/docs/ironwood-performance).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
