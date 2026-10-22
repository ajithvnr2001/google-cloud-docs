---
url: https://docs.cloud.google.com/dataflow/docs/gpu/develop-with-gpus/
title: Best practices for working with Dataflow GPUs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:22.526549+00:00
---

# Best practices for working with Dataflow GPUs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/gpu/develop-with-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Best practices for working with Dataflow GPUs Stay organized with collections  Save and categorize content based on your preferences. 

Using GPUs with Dataflow lets you accelerate compute-intensive workloads such as machine learning inference and large-scale image processing. Using the recommended pipeline design and resource tuning practices helps you maximize throughput while managing hardware costs.

For instructions and examples on configuring GPUs in your Dataflow jobs, see [Run a pipeline with GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus) and [Processing Landsat satellite images with GPUs](https://docs.cloud.google.com/dataflow/docs/tutorials/satellite-images-gpus).

## Prerequisites for using GPUs in Dataflow

  * To use GPUs with your Dataflow job, you must use the Portable Runner (previously called Runner v2).
  * Dataflow runs user code in worker VMs inside a Docker container. These worker VMs run [Container-Optimized OS](https://docs.cloud.google.com/container-optimized-os/docs). For Dataflow jobs to use GPUs, you need the following prerequisites: 
    * GPU drivers are installed on worker VMs and accessible to the Docker container. For more information, see [Install GPU drivers](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus#drivers).
    * GPU libraries required by your pipeline, such as [NVIDIA CUDA-X libraries](https://developer.nvidia.com/gpu-accelerated-libraries) or the [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-toolkit), are installed in the custom container image. For more information, see [Configure your container image](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus#container-image).
  * Because GPU containers are typically large, to avoid [running out of disk space](https://docs.cloud.google.com/dataflow/docs/guides/common-errors#no-space-left), increase the default [boot disk size](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options#worker-level_options) to 50 gigabytes or more.



## Considerations

When designing both your test and production environments, consider the following factors.

### Local development

Using Apache Beam with NVIDIA GPUs lets you create large-scale data processing pipelines that handle preprocessing and inference. When you're using GPUs for local development, consider the following information:

  * Often, data processing workflows use additional libraries that you need to install in the launch environment and in the execution environment on Dataflow workers. This configuration adds steps to the development workflow for [configuring pipeline requirements](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/) or for [using custom containers in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers). It's beneficial to have a local development environment that mimics the production environment as closely as possible.

  * If your workflow meets both of the following criteria, you don't need to build custom containers or change your development workflow to configure pipeline requirements:

    * You're using a library that implicitly uses NVIDIA GPUs.
    * Your code doesn't require any changes to support GPU.
  * Some libraries don't switch transparently between the CPU and GPU usage, and hence require specific builds and different code paths. To replicate the code-run-code development lifecycle for this scenario, additional steps are required.

  * When running local experiments, replicate the environment of the Dataflow worker as closely as possible. Depending on the library, you might need a machine with a GPU and the required GPU libraries installed. This type of machine might not be available in your local environment. You can emulate the Dataflow runner environment using a container running on a GPU-equipped Google Cloud virtual machine.




### Machine type specifications

For details about machine type support for each GPU model, see [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus). GPUs that are supported with N1 machine types also support the [custom N1 machine types](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type#n1_custom_machine_types).

The type and number of GPUs define the upper bound restrictions on the available amounts of vCPU and memory that workers can have. To find the corresponding restrictions, see [Availability](https://docs.cloud.google.com/dataflow/docs/gpu/gpu-support#availability).

Specifying a higher number of CPUs or memory might require that you specify a higher number of GPUs.

For more details, read [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus/about-gpus#restrictions).

### Optimize resource usage

Most pipelines are not composed entirely of transformations that require a GPU. A typical pipeline has an ingestion stage that uses one of the many sources provided by Apache Beam. That stage is followed by data manipulation or shaping transforms, which then feed into a GPU transform.

Right fitting uses [Apache Beam resource hints](https://beam.apache.org/documentation/runtime/resource-hints/) to customize worker resources for your batch pipelines. When right fitting is enabled, Dataflow only uses GPUs for the stages of the pipeline that need them. Consequently, this feature improves pipeline flexibility and capability while potentially reducing costs.

For more information, see [Right fitting](https://docs.cloud.google.com/dataflow/docs/guides/right-fitting).

### GPUs and worker parallelism

For Python pipelines that use the [Dataflow Portable Runner](https://docs.cloud.google.com/dataflow/docs/portable-runner) architecture, Dataflow launches one Apache Beam SDK process per VM core. Each SDK process runs in its own Docker container and in turn spawns many threads, each of which processes incoming data.

GPUs use multiple process architecture, and GPUs in Dataflow workers are visible to all processes and threads.

If you're running multiple SDK processes on a shared GPU, you can improve GPU efficiency and utilization by enabling the NVIDIA Multi-Process Service (MPS). MPS improves worker parallelism and overall throughput for GPU pipelines, especially for workloads with low GPU resource usage. For more information, see [Improve performance on a shared GPU by using NVIDIA MPS](https://docs.cloud.google.com/dataflow/docs/gpu/use-nvidia-mps).

To avoid GPU memory oversubscription, you might need to manage GPU access. If you're using TensorFlow, either of the following suggestions can help you avoid GPU memory oversubscription:

  * Configure the Dataflow workers to start only one containerized Python process, regardless of the worker vCPU count. To make this configuration, when launching your job, use the following [pipeline options](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options):

    * `--experiments=no_use_multiple_sdk_containers`
    * `--number_of_worker_harness_threads`

For more information about how many threads to use, see [Reduce the number of threads](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-oom#reduce-threads).

  * [Enable MPS](https://docs.cloud.google.com/dataflow/docs/gpu/use-nvidia-mps#enable).




### Inference workloads

When you're using machine learning (ML) models to do local and remote inference, use the built-in Apache Beam [`RunInference` transform](https://beam.apache.org/documentation/ml/inference-overview/). The `RunInference` API is a `PTransform` optimized for machine learning inferences. Using the `RunInference` transform can improve efficiency when you use ML models in your pipelines.

## Workflow

The following two-stage workflow shows how to build a pipeline using GPUs. This flow takes care of GPU and non-GPU related issues separately and shortens the feedback loop.

  1. Create a pipeline

Create a pipeline that can run on Dataflow. Replace the transforms that require GPUs with the transforms that don't use GPUs, but are functionally the same:

     1. Create all transformations that surround the GPU usage, such as data ingestion and manipulation.

     2. Create a stub for the GPU transform with a pass-through or schema change.

  2. Test locally

Test the GPU portion of the pipeline code in the environment that mimics the Dataflow worker execution environment. The following steps describe one of the methods to run this test:

     1. Create a [Docker](https://www.docker.com/) image with all necessary libraries.

     2. Start development of the GPU code.

     3. Begin the code-run-code cycle using a Google Cloud virtual machine with the Docker image. To rule out library incompatibilities, run the GPU code in a local Python process separately from an Apache Beam pipeline. Then, run the entire pipeline on the direct runner, or launch the pipeline on Dataflow.




## Use a VM running container-optimized operating system

For a minimum environment, use a container-optimized virtual machine (VM). For more information, see [Create a VM with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).

The general flow is:

  1. Create a VM.

  2. Connect to the VM and run the following commands:
         
         sudo cos-extensions install gpu -- -version latest
         sudo mount --bind /var/lib/nvidia /var/lib/nvidia
         sudo mount -o remount,exec /var/lib/nvidia
         

  3. Confirm that GPUs are available:
         
         ./nvidia-smi
         

  4. Start a Docker container with GPU drivers from the VM mounted as volumes. For example:
         
         sudo docker run --rm -it --entrypoint /bin/bash
         --volume /var/lib/nvidia/lib64:/usr/local/nvidia/lib64
         --volume /var/lib/nvidia/bin:/usr/local/nvidia/bin
         --privileged gcr.io/bigdatapivot/image_process_example:latest
         




For a sample Dockerfile, see [Build a custom container image](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus#custom-container). Add all the dependencies that you need for your pipeline to the Dockerfile.

For more information about using a Docker image that is pre-configured for GPU usage, see [Use an existing image configured for GPU usage](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus#existing-image).

### Tools for working with container-optimized systems

  * To configure Docker CLI to use `docker-credential-gcr` as a credential helper for the default set of Google Container Registries (GCR), use:
        
        sudo docker-credential-gcr configure-docker
        

For more information about setting up Docker credentials, see [docker-credential-gcr](https://github.com/GoogleCloudPlatform/docker-credential-gcr).

  * To copy files, such as pipeline code, to or from a VM, use `toolbox`. This technique is useful when using a Custom-Optimized image. For example:
        
        toolbox /google-cloud-sdk/bin/gsutil cp gs://bucket/gpu/image_process/* /media/root/home/<userid>/opencv/
        

For more information, see [Debugging node issues using toolbox](https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox).




## What's next

  * Learn more about [Dataflow support for GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/gpu-support).
  * Learn more about how to [run a pipeline by using GPUs](https://docs.cloud.google.com/dataflow/docs/gpu/use-gpus).
  * Work through [Processing Landsat satellite images with GPUs](https://docs.cloud.google.com/dataflow/docs/tutorials/satellite-images-gpus).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
