---
url: https://docs.cloud.google.com/run/docs/configuring/jobs/gpu-best-practices/
title: Best practices: Cloud Run jobs with GPUs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:43.265900+00:00
---

# Best practices: Cloud Run jobs with GPUs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/jobs/gpu-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Best practices: Cloud Run jobs with GPUs Stay organized with collections  Save and categorize content based on your preferences. 

This page provides best practices for optimizing performance when using a Cloud Run job with GPU for AI workloads such as, training large language models (LLMs) using your preferred frameworks, fine-tuning, and performing batch or offline inference on LLMs. To create a Cloud Run job that can perform compute intensive tasks or batch processing in real time, you should: 

  * Use models that load fast and require minimal transformation into GPU-ready structures, and optimize how they are loaded.
  * Use configurations that allow for maximum, efficient, concurrent execution to reduce the number of GPUs needed to serve a target request per second while keeping costs down.



## Recommended ways to load large ML models on Cloud Run

Google recommends downloading ML models from Cloud Storage and accessing them through the Google Cloud CLI. You might alternatively store models inside container images, but this method is best suited for smaller models less than 10 GB.

### Storing and loading ML models trade-offs

Here is a comparison of the options:

**Model location** | **Deploy time** | **Development experience** | **Container startup time** | **Storage cost**  
---|---|---|---|---  
Cloud Storage, downloaded concurrently using the Google Cloud CLI command [`gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) or the Cloud Storage API as shown in the [transfer manager concurrent download code sample](https://docs.cloud.google.com/storage/docs/samples/storage-transfer-manager-download-chunks-concurrently).  | Fastest. Model downloaded during container startup. Ensure the Cloud Run instance has sufficient RAM allocated to store the model files.  | Slightly more difficult to set up, because you'll need to either install the Google Cloud CLI on the image or update your code to use the Cloud Storage API. For more information on how to fetch credentials from the metadata server, see [Introduction to service identity](https://docs.cloud.google.com/run/docs/securing/service-identity#access-tokens).  | Fast when you use network optimizations. The Google Cloud CLI downloads the model file in parallel.  | One copy in Cloud Storage.   
Cloud Storage, loaded using Cloud Storage FUSE volume mount  | Faster. Model downloaded during container startup.  | Not difficult to set up, does not require changes to the docker image.  | Fast when you use network optimizations.  | One copy in Cloud Storage.   
Container image | Fast. An image containing a large model will take longer to import into Cloud Run.  | You'll need to build a new image every time you want to use a different model. Changes to the container image will require redeployment, which may be slow for large images.  | Depends on the size of the model. For very large models, use Cloud Storage for more predictable but slower performance.  | Potentially multiple copies in Artifact Registry.   
Internet | Slow. Model downloaded during container startup.  | Typically simpler (many frameworks download models from central repositories).  | Typically poor and unpredictable:

  * Frameworks may apply model transformations during initialization. (You should do this at build time).
  * Model host and libraries for downloading the model may not be efficient. 
  * There is reliability risk associated with downloading from the internet. Your job could fail to start if the download target is down, and the underlying model downloaded could change, which decreases quality. We recommend hosting in your own Cloud Storage bucket.

| Depends on the model hosting provider.   
  
### Store models in Cloud Storage

To optimize ML model loading when loading ML models from Cloud Storage, either using [Cloud Storage volume mounts](https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts) or directly using the Cloud Storage API or command line, you must use [Direct VPC](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) with the egress setting value set to `all-traffic`, along with [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

For an additional cost, using [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) can reduce model loading latency by efficiently caching data on SSDs for faster reads.

To reduce model read times, try the following mount options to enable Cloud Storage FUSE features:

  * `cache-dir`: Enable the [file caching feature](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/file-caching) with an [in-memory volume mount](https://docs.cloud.google.com/run/docs/configuring/services/in-memory-volume-mounts) to use as the underlying directory to persist files. Set the `cache-dir` mount option value to the in-memory volume name in the format, `cr-volume:{volume name}`. For example, if you have an in-memory volume named `in-memory-1` that you want to use as the cache directory, specify `cr-volume:in-memory-1`. When this value is set, you can also set other `file-cache` [flags available to configure for cache](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts#configure-cache).
  * `enable-buffered-read`: Set the [`enable-buffered-read`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#enable-buffered-read) field to `true` for asynchronous prefetching of parts of a Cloud Storage object into an in-memory buffer. This allows subsequent reads to be served from the buffer instead of requiring network calls. When you configure this field, you can also set the [`read-global-max-blocks`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#read-global-max-blocks) field to configure the maximum number of blocks available for buffered reads across all file handles.



When both `cache-dir` and `enable-buffered-read` are used, `cache-dir` will take precedence. Note that enabling any of these features will change the resource accounting of the Cloud Storage FUSE process to be counted under container memory limits. Consider raising the container memory limit by following [instructions on how to configure memory limits](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits#configure-services).

### Store models in container images

By storing the ML model in the container image, model loading will benefit from Cloud Run's optimized container streaming infrastructure. However, building container images that include ML models is a resource-intensive process, especially when working with large models. In particular, the build process can become bottlenecked on network throughput. When using Cloud Build, we recommend using a more powerful build machine with increased compute and networking performance. To do this, build an image using a [build config file](https://docs.cloud.google.com/build/docs/build-push-docker-image#build_an_image_using_a_build_config_file) that has the following steps:
    
    
    steps:
    - name: 'gcr.io/cloud-builders/docker'
      args: ['build', '-t', 'IMAGE', '.']
    - name: 'gcr.io/cloud-builders/docker'
      args: ['push', 'IMAGE']
    images:
    - IMAGE
    options:
     machineType: 'E2_HIGHCPU_32'
     diskSizeGb: '500'
     

You can create one model copy per image if the layer containing the model is distinct between images (different hash). There could be additional Artifact Registry cost because there could be one copy of the model per image if your model layer is unique across each image.

### Load models from the internet

To optimize ML model loading from the internet, [route all traffic through the vpc network](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) with the egress setting value set to `all-traffic` and set up [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to reach the public internet at high bandwidth.

## Build, deployment, runtime, and system design considerations

The following sections describe considerations for build, deploy, runtime and system design.

### At build time

The following list shows considerations you need to take into account when you are planning your build:

  * Choose a good base image. You should start with an image from the [Deep Learning Containers](https://docs.cloud.google.com/deep-learning-containers/docs/choosing-container) or the [NVIDIA container registry](https://catalog.ngc.nvidia.com/containers) for the ML framework you're using. These images have the latest performance-related packages installed. We don't recommend creating a custom image.
  * Choose 4-bit quantized models to maximize concurrency unless you can prove they affect result quality. Quantization produces smaller and faster models, reducing the amount of GPU memory needed to serve the model, and can increase parallelism at run time. Ideally, the models should be trained at the target bit depth rather than quantized down to it.
  * Pick a model format with fast load times to minimize container startup time, such as GGUF. These formats more accurately reflect the target quantization type and require less transformations when loaded onto the GPU. For security reasons, don't use pickle-format checkpoints.
  * Create and warm LLM caches at build time. Start the LLM on the build machine while building the docker image. Enable prompt caching and feed common or example prompts to help warm the cache for real-world use. Save the outputs it generates to be loaded at runtime.
  * Save your own inference model that you generate during build time. This saves significant time compared to loading less efficiently stored models and applying transforms like quantization at container startup.



### At deployment

The following list shows considerations you need to take into account when you are planning your deployment:

  * Set a [task timeout of one hour or lesser](https://docs.cloud.google.com/run/docs/configuring/task-timeout) for job executions.
  * If you are running parallel tasks in a job execution, determine and set [parallelism](https://docs.cloud.google.com/run/docs/configuring/parallelism) to less than the [GPU quota without zonal redundancy](https://console.cloud.google.com/projectselector2/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fnvidia_l4_gpu_allocation_no_zonal_redundancy_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22\)\)) allocated for your project. To request for a quota increase, see [How to increase quota](https://docs.cloud.google.com/run/quotas#increase). GPU tasks start as quickly as possible, and go up to a maximum that varies depending on how much GPU quota you allocated for the project and the region selected. Deployments fail if you set parallelism to more than the GPU quota limit.



### At run time

  * Actively manage your supported context length. The smaller the context window you support, the more queries you can support running in parallel. The details of how to do this depend on the framework.
  * Use the LLM caches you generated at build time. Supply the same flags you used during build time when you generated the prompt and prefix cache.
  * Load from the saved model you just wrote. See Storing and loading models trade-offs for a comparison on how to load the model.
  * Consider using a quantized key-value cache if your framework supports it. This can reduce per-query memory requirements and allows for configuration of more parallelism. However, it can also impact quality.
  * Tune the amount of GPU memory to reserve for model weights, activations and key-value caches. Set it as high as you can without getting an out-of-memory error.
  * Check to see whether your framework has any options for improving container startup performance (for example, using model loading parallelization). 



### At the system design level

  * Add semantic caches where appropriate. In some cases, caching whole queries and responses can be a great way of limiting the cost of common queries.
  * Control variance in your preambles. Prompt caches are only useful when they contain the prompts in sequence. Caches are effectively prefix-cached. Insertions or edits in the sequence mean that they're either not cached or only partially present.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
