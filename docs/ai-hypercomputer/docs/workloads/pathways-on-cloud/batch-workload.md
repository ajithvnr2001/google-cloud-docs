---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload/
title: Run a batch workload with Pathways \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:02.222760+00:00
---

# Run a batch workload with Pathways  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/batch-workload/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Run a batch workload with Pathways Stay organized with collections  Save and categorize content based on your preferences. 

For the purpose of this document, batch workloads are defined as JAX workloads that execute to completion and are deployed within the same GKE cluster as the Pathways cluster, specifically alongside the Pathways controller components (IFRT proxy server and Pathways resource manager). Completion of the JAX workload terminates the Pathways cluster components. This guide uses a JAX training workload to demonstrate this.

## Before you begin

Make sure you have:

  * [Created a GKE cluster](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster).
  * [Set up Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment)
  * [Installed Kubernetes tools](https://kubernetes.io/docs/tasks/tools/)
  * [Enabled the Google Kubernetes Engine API](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api)



## Build a training image using Maxtext

[MaxText](https://github.com/AI-Hypercomputer/maxtext) is an open-source, large language model (LLM) project developed by Google. It's written in JAX and designed to be highly performant and scalable, running efficiently on Google Cloud TPUs and GPUs.

To build a MaxText Docker image by using the latest version of stable JAX from the OSS GitHub repository, run the following command:
    
    
    git clone https://github.com/AI-Hypercomputer/maxtext
    cd maxtext/dependencies/scripts
    gcloud config set project PROJECT_ID
    bash ./docker_build_dependency_image.sh MODE=stable
    gcloud auth configure-docker
    bash ./docker_upload_runner.sh CLOUD_IMAGE_NAME=USER_runner # This script needs bash version >= 4.2 to execute.

This command pushes the MaxText Kubernetes image to `gcr.io/$PROJECT_ID/${USER}_runner`. You can use this Docker image to run training on TPUs by using the Pathways backend.

## Run a batch workload with Cluster Toolkit

Submit the prebuilt MaxText Docker image by using the `gcluster job submit` command:
    
    
    gcluster job submit \
        --pathways \
        --pathways-gcs-location="gs://BUCKET_NAME/pathways-artifacts" \
        --name=WORKLOAD \
        --cluster=CLUSTER \
        --project=PROJECT_ID \
        --location=ZONE \
        --num-slices=WORKLOAD_NODEPOOL_COUNT \
        --compute-type=COMPUTE_TYPE \
        --topology=TOPOLOGY \
        --image="gcr.io/PROJECT_ID/USER_runner" \
        --command="python3 -m MaxText.train /deps/src/MaxText/configs/base.yml base_output_directory=gs://BUCKET_NAME per_device_batch_size=1 enable_checkpointing=false remat_policy=full global_parameter_scale=1 steps=20 max_target_length=2048 use_iota_embed=true reuse_example_batch=1 dataset_type=synthetic attention=flash gcs_metrics=True enable_single_controller=True run_name=RUN_NAME-pathways-job"
    

For more information about job submission options, see the [Cluster Toolkit Job Submission Guide](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gcluster_job_guide.md).

Replace the following:

  * `WORKLOAD`: a unique name to identify your workload; because of DNS label limits, this must be 22 characters or fewer
  * `CLUSTER`: the name of your GKE cluster
  * `WORKLOAD_NODEPOOL_COUNT`: the number of TPU slice node pools
  * `COMPUTE_TYPE`: the TPU machine type (for example, `ct6e-standard-4t`). For more information about supported TPU types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `TOPOLOGY`: the TPU placement topology (for example, `2x4`)
  * `PROJECT_ID`: your Google Cloud project ID
  * `ZONE`: the zone where you plan to run your workload
  * `USER`: your Google Cloud user ID
  * `BUCKET_NAME`: the Cloud Storage bucket for outputs
  * `RUN_NAME`: a user-assigned name to identify the workflow run



Follow the progress of your workload by using the `gcluster job logs` command:
    
    
    gcluster job logs WORKLOAD \
        --cluster=CLUSTER \
        --project=PROJECT_ID \
        --location=ZONE \
        --main-only=false
    
    
    
    completed step: 1, seconds: 0.484, TFLOP/s/device: 87.349, Tokens/s/device: 2117.382, total_weights: 2945, loss: 10.888
    completed step: 2, seconds: 0.407, TFLOP/s/device: 103.699, Tokens/s/device: 2513.735, total_weights: 3253, loss: 9.697
    completed step: 3, seconds: 0.248, TFLOP/s/device: 170.300, Tokens/s/device: 4128.167, total_weights: 3154, loss: 9.641
    completed step: 4, seconds: 0.216, TFLOP/s/device: 195.122, Tokens/s/device: 4729.880, total_weights: 3119, loss: 9.547
    completed step: 5, seconds: 0.272, TFLOP/s/device: 155.298, Tokens/s/device: 3764.512, total_weights: 2837, loss: 10.179
    completed step: 6, seconds: 0.472, TFLOP/s/device: 89.489, Tokens/s/device: 2169.266, total_weights: 3069, loss: 9.776

To cancel the workload before it completes, use the `gcluster job cancel` command:
    
    
    gcluster job cancel WORKLOAD --cluster=CLUSTER --project=PROJECT_ID --location=ZONE
    

## What's next

  * [Create a GKE cluster with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/create-gke-cluster)
  * [Multihost inference with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/multihost-inference)
  * [Pathways interactive mode](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/pathways-interactive-mode)
  * [Porting JAX workloads to Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/porting-jax-workloads)
  * [Resilient training with Pathways](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/resilient-training)
  * [Troubleshoot Pathways on cloud](https://docs.cloud.google.com/ai-hypercomputer/docs/workloads/pathways-on-cloud/troubleshooting-pathways)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
