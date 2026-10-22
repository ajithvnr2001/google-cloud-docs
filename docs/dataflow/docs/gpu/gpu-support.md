---
url: https://docs.cloud.google.com/dataflow/docs/gpu/gpu-support/
title: Dataflow support for GPUs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:22.352575+00:00
---

# Dataflow support for GPUs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/gpu/gpu-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Dataflow support for GPUs Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** NVIDIA T4 and P4 GPUs are deprecated on Dataflow and will reach End of Life on August 1, 2027. To avoid pipeline failures, migrate your workloads to the G2 (NVIDIA L4) VM family. For more information, see [Use the NVIDIA® L4 GPU type](https://docs.cloud.google.com/dataflow/docs/gpu/use-l4-gpus) and [Compute Engine feature deprecations](https://docs.cloud.google.com/compute/docs/deprecations).

This page provides background information on how GPUs work with Dataflow, including information about prerequisites and supported GPU types.

Using GPUs in Dataflow jobs lets you accelerate some data processing tasks. GPUs can perform certain computations faster than CPUs. These computations are usually numeric or linear algebra, often used in image processing and machine learning use cases. The extent of performance improvement varies by the use case, type of computation, and amount of data processed.

## Prerequisites for using GPUs in Dataflow

  * To use GPUs with your Dataflow job, you must use the Portable Runner (previously called Runner v2).
  * Dataflow runs user code in worker VMs inside a Docker container. These worker VMs run [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs). For Dataflow jobs to use GPUs, you need the following prerequisites: 
    * GPU drivers are installed on worker VMs and accessible to the Docker container. For more information, see [Install GPU drivers](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus#drivers).
    * GPU libraries required by your pipeline, such as [NVIDIA CUDA-X libraries](https://developer.nvidia.com/gpu-accelerated-libraries) or the [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit), are installed in the custom container image. For more information, see [Configure your container image](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus#container-image).
  * Because GPU containers are typically large, to avoid [running out of disk space](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#no-space-left), increase the default [boot disk size](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#worker-level_options) to 50 gigabytes or more.



## Pricing

Jobs using GPUs incur charges as specified in the Dataflow [pricing page](https://cloud.google.com/dataflow/pricing).

## Availability

**Note:** TPUs are also supported with Dataflow. For more information, see [Dataflow support for TPUs](https://docs.cloud.google.com/dataflow/docs/tpu/tpu-support).

The following GPU types are supported with Dataflow:

GPU type | `worker_accelerator` string  
---|---  
NVIDIA® L4 | `nvidia-l4`  
NVIDIA® A100 40 GB | `nvidia-tesla-a100`  
NVIDIA® A100 80 GB | `nvidia-a100-80gb`  
NVIDIA® Tesla® T4 (deprecated) | `nvidia-tesla-t4`  
NVIDIA® Tesla® P4 (deprecated) | `nvidia-tesla-p4`  
NVIDIA® Tesla® V100 | `nvidia-tesla-v100`  
NVIDIA® H100 | `nvidia-h100-80gb`  
NVIDIA® H100 Mega | `nvidia-h100-mega-80gb`  
NVIDIA® RTX Pro 6000 | `nvidia-rtx-pro-6000`  
  
For more information about each GPU type, including performance data, see [Compute Engine GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).

For information about available regions and zones for GPUs, see [GPU regions and zones availability](https://docs.cloud.google.com/compute/docs/regions-zones/gpu-regions-zones) in the Compute Engine documentation.

### Recommended workloads

The following table provides recommendations for which type of GPU to use for different workloads. The examples in the table are suggestions only, and you need to test in your own environment to determine the appropriate GPU type for your workload.

For more detailed information about GPU memory size, feature availability, and ideal workload types for different GPU models, see the [General comparison chart](https://docs.cloud.google.com/compute/docs/gpus#general_comparison_chart) on the GPU platforms page.

Workload | A100, H100 | RTX Pro 6000 | L4 | T4 (deprecated)  
---|---|---|---|---  
Model fine-tuning | Recommended |  |  |   
Large model inference | Recommended | Recommended | Recommended |   
Medium model inference |  | Recommended | Recommended | Recommended  
Small model inference |  | Recommended | Recommended | Recommended  
  
## What's next

  * See an example of a [developer workflow for building pipelines that use GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/develop-with-gpus).
  * Learn how to [run an Apache Beam pipeline on Dataflow with GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus).
  * Work through [Processing Landsat satellite images with GPUs](https://docs.cloud.google.com/dataflow/docs/tutorials/satellite-images-gpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
