---
url: https://docs.cloud.google.com/dataflow/docs/gpu/use-l4-gpus/
title: Use the NVIDIA\u00ae L4 GPU type \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:02:45.446273+00:00
---

# Use the NVIDIA® L4 GPU type  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/gpu/use-l4-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use the NVIDIA® L4 GPU type Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to run your Dataflow pipeline with the NVIDIA® L4 GPU type. The L4 GPU type is useful for running machine learning inference pipelines.

## Requirements

  * Use the Apache Beam SDK version 2.46 or later. Apache Beam 2.50 or later is recommended.
  * You need L4 GPU quota (`NVIDIA_L4_GPUS`) in the region that your job runs in. For more information, see [GPU quotas](https://docs.cloud.google.com/compute/resource-usage#gpu_quota).
  * The L4 GPU type is available only with the G2 accelerator-optimized machine type. For more information, see [The G2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms). Pipelines that use the L4 GPU type are subject to the [G2 standard limitations](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2_limitations).
  * The NVIDIA L4 GPU type uses the NVIDIA driver version 525.0 or later and the [CUDA toolkit](https://developer.nvidia.com/cuda-toolkit) version 12.0 or later. Any code that you use in your pipeline must be compatible with the NVIDIA driver version and CUDA toolkit version. For example, if you use PyTorch, you need to use PyTorch version 23.01 or later.



## Run pipelines with the NVIDIA® L4 GPU type

To use the NVIDIA L4 GPU type, you need to include the following [pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options) and [service options](https://docs.cloud.google.com/dataflow/docs/reference/service-options) in your pipeline code.

###  Java 
    
    
    --workerMachineType=G2_MACHINE_TYPE
    --dataflowServiceOptions="worker_accelerator=type:nvidia-l4;count:GPU_COUNT;install-nvidia-driver"
    

###  Python 
    
    
    --machine_type=G2_MACHINE_TYPE
    --dataflow_service_options="worker_accelerator=type:nvidia-l4;count:GPU_COUNT;install-nvidia-driver"
    

###  Go 
    
    
    --worker_machine_type=G2_MACHINE_TYPE
    --dataflow_service_options="worker_accelerator=type:nvidia-l4;count:GPU_COUNT;install-nvidia-driver"
    

Replace the following values:

  * G2_MACHINE_TYPE: the [G2 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-standard-vms) to use
  * GPU_COUNT: The number of GPUs to use. Each G2 machine type has a fixed number of NVIDIA L4 GPUs. To find the correct number of GPUs for your machine type, see the **GPU count** column in the [G2 standard machine types](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-standard-vms) table.



For more information about running pipelines with GPUs, see [Run a pipeline with GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus).

## Manage dependencies

To manage dependencies, use a custom container. For more information, see [Use custom containers in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers).

The following Dockerfile example contains compatible dependencies for a pipeline that uses the NVIDIA L4 GPU type.
    
    
    RUN apt-get -y update
    RUN apt-get install [system packages]
    
    # Install the SDK.
    RUN pip install --no-cache-dir apache-beam[gcp]==2.51.0
    # Install the machine learning dependencies.
    RUN pip install --no-cache-dir tensorflow[and-cuda]
    RUN pip install xgboost
    RUN pip install transformers accelerate
    (etc…..)
    # Verify that the image doesn't have conflicting dependencies.
    RUN pip check
    
    # Copy files from official SDK image, including the script and dependencies.
    COPY --from=apache/beam_python3.10_sdk:2.51.0 /opt/apache/beam /opt/apache/beam
    
    # Set the entrypoint to Apache Beam SDK launcher.
    ENTRYPOINT ["/opt/apache/beam/boot"]
    

## What's next

  * Read about [best practices for working with Dataflow GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/develop-with-gpus).
  * [Run a pipeline with GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus).
  * Learn more about [Dataflow ML](https://docs.cloud.google.com/dataflow/docs/machine-learning). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
