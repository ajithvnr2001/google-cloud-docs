---
url: https://docs.cloud.google.com/dataflow/docs/gpu/use-nvidia-mps/
title: Improve performance on a shared GPU by using NVIDIA MPS \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:22.026759+00:00
---

# Improve performance on a shared GPU by using NVIDIA MPS  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/gpu/use-nvidia-mps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Improve performance on a shared GPU by using NVIDIA MPS Stay organized with collections  Save and categorize content based on your preferences. 

If you run multiple SDK processes on a shared Dataflow GPU, you can improve GPU efficiency and utilization by enabling the NVIDIA Multi-Process Service (MPS). MPS supports concurrent processing on a GPU by enabling processes to share CUDA contexts and scheduling resources. MPS can reduce context-switching costs, increase parallelism, and reduce storage requirements.

Target workflows are Python pipelines that run on workers with more than one vCPU.

MPS is an NVIDIA technology that implements the CUDA API, an NVIDIA platform that supports general-purpose GPU computing. For more information, see the [NVIDIA Multi-Process Service user guide](https://docs.nvidia.com/deploy/mps/index.html).

## Benefits

  * Improves parallel processing and overall throughput for GPU pipelines, especially for workloads with low GPU resource usage.
  * Improves GPU utilization, which might reduce your costs.



## Support and limitations

  * MPS is supported only on Dataflow workers that use a single GPU.
  * The pipeline can't use pipeline options that restrict parallelism.
  * Don't use the pipeline option `--experiments=no_use_multiple_sdk_containers` when using NVIDIA MPS. This option restricts Dataflow to a single Python process per VM. This prevents MPS from effectively dividing GPU resources across processes. It also severely limits parallelism due to Python's Global Interpreter Lock (GIL) and makes many other tuning parameters ineffective.
  * Avoid exceeding the available GPU memory, especially for use cases that involve loading large machine learning models. Balance the number of vCPUs and SDK processes with the available GPU memory that these processes need.
  * MPS doesn't affect the concurrency of non-GPU operations.
  * Dataflow Prime doesn't support MPS.



## Enable MPS

We recommend enabling MPS any time you are loading more than one copy of your model onto a single GPU (for example, by using `model_copies > 1` in the `RunInference` transform). This allows multiple processes to access the GPU simultaneously, improving efficiency and utilization.

When you [run a pipeline with GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus), enable MPS by doing the following:

  * In the pipeline option `--dataflow_service_options`, append `use_nvidia_mps` to the `worker_accelerator` parameter.
  * Set the `count` to 1.
  * Don't use the pipeline option `--experiments=no_use_multiple_sdk_containers`.



The pipeline option `--dataflow_service_options` looks like the following:
    
    
    --dataflow_service_options="worker_accelerator=type:GPU_TYPE;count:1;install-nvidia-driver;use_nvidia_mps"
    

If you use TensorFlow and enable MPS, do the following:

  1. [Enable dynamic memory allocation](https://www.tensorflow.org/guide/gpu#limiting_gpu_memory_growth) on the GPU. Use either of the following TensorFlow options: 
     * Turn on memory growth by calling `tf.config.experimental.set_memory_growth(gpu, True)`.
     * Set the environment variable `TF_FORCE_GPU_ALLOW_GROWTH` to true.
  2. Use logical devices with appropriate memory limits.
  3. For optimal performance, enforce the use of the GPU when possible by using [soft device placement](https://www.tensorflow.org/api_docs/python/tf/config/set_soft_device_placement) or [manual placement](https://www.tensorflow.org/guide/gpu#manual_device_placement).



## What's next

  * To review more best practices, see [GPUs and worker parallelism](https://docs.cloud.google.com/dataflow/docs/gpu/develop-with-gpus#parallelism).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
