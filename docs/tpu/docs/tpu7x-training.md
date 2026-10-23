---
url: https://docs.cloud.google.com/tpu/docs/tpu7x-training/
title: Train a model using TPU7x (Ironwood) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:13.921854+00:00
---

# Train a model using TPU7x (Ironwood)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/tpu7x-training/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Train a model using TPU7x (Ironwood)

This document describes how to provision TPU7x resources with [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview) and deploy a training workload using either [MaxText](https://github.com/AI-Hypercomputer/maxtext) (JAX) or [TorchTitan on TPU](https://github.com/google-pytorch/torchtitan) (PyTorch).

TPU7x is the first release within the Ironwood family, Google Cloud's seventh generation TPU. The Ironwood generation is designed for large-scale AI training and inference. For more information, see [TPU7x](https://docs.cloud.google.com/tpu/docs/tpu7x).

For more examples optimized for TPU7x, see the following repositories on GitHub:

  * [Training recipes for Ironwood TPU](https://github.com/AI-Hypercomputer/tpu-recipes/blob/main/training/ironwood/README.md)
  * [TorchTitan Ironwood recipes](https://github.com/google-pytorch/torchtitan/tree/main/torchtitan/experiments/tpu/recipes/ironwood)



## Before you begin

Before you start, make sure you meet the following requirements:

  * You have a Google Cloud project with billing enabled.
  * You have [installed and initialized the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  * You have [installed Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).



Then complete the following setup steps:

  1. Set the environment variables for your project and cluster:
         
         export PROJECT_ID=YOUR_PROJECT_ID
         export ZONE=YOUR_ZONE
         export CLUSTER_NAME=YOUR_CLUSTER_NAME
         export BASE_OUTPUT_DIR="gs://YOUR_BUCKET_NAME"

Replace the following:

     * YOUR_PROJECT_ID: Your Google Cloud project ID.
     * YOUR_ZONE: The zone in which to create the cluster.
     * YOUR_CLUSTER_NAME: The name of the new cluster.
     * YOUR_BUCKET_NAME: The name of your Cloud Storage bucket for training output.
  2. If you don't have an existing Cloud Storage bucket, create one:
         
         gcloud storage buckets create ${BASE_OUTPUT_DIR} \
             --project=${PROJECT_ID} \
             --location=US \
             --default-storage-class=STANDARD \
             --uniform-bucket-level-access
         




## Deploy the TPU7x (Ironwood) cluster

Deploy a Google Kubernetes Engine (GKE) TPU7x cluster by following the instructions in [Deploy a GKE TPU 7x cluster](https://docs.cloud.google.com/cluster-toolkit/docs/deploy/gke/gke-tpu-7x). Ensure that your cluster node pool topology matches your training workload requirements, such as `4x4x8` for the MaxText example or `2x2x4` for the TorchTitan example.

## Deploy a training workload with MaxText

The following sections show how to build a container image and submit a [MaxText](https://github.com/AI-Hypercomputer/maxtext) training job with Cluster Toolkit.

### Build and upload the MaxText Docker image

**Note:** MaxText supports **Python 3.12 only**. Build your virtual environment with Python 3.12 to install the required dependencies.

Build and push the MaxText Docker image:
    
    
    # Clone MaxText
    git clone https://github.com/AI-Hypercomputer/maxtext.git
    cd maxtext
    git checkout maxtext-tutorial-v1.0.0
    
    # Build the Docker image
    bash docker_build_dependency_image.sh MODE=stable JAX_VERSION=0.8.2
    
    export CLOUD_IMAGE_NAME="${USER}-maxtext-runner"
    bash docker_upload_runner.sh CLOUD_IMAGE_NAME=${CLOUD_IMAGE_NAME}
    

### Define the MaxText training command

Prepare the command to run your training script inside the Docker container.

The MaxText 1B model configuration trains a language model with approximately 1 billion parameters. Use this model to test small chip scales. Performance is not optimized.
    
    
    export MAXTEXT_COMMAND="JAX_PLATFORMS=tpu,cpu \
        ENABLE_PJRT_COMPATIBILITY=true \
        python3 src/MaxText/train.py src/MaxText/configs/base.yml \
            base_output_directory=${BASE_OUTPUT_DIR} \
            dataset_type=synthetic \
            per_device_batch_size=2 \
            enable_checkpointing=false \
            gcs_metrics=true \
            run_name=maxtext_training \
            steps=30"
    

### Submit the MaxText training job

Submit your training job using `gcluster job submit`. For details on job submission options, see the [Cluster Toolkit Job Guide](https://github.com/GoogleCloudPlatform/cluster-toolkit/blob/main/docs/gcluster_job_guide.md):
    
    
    gcluster job submit \
        --name="maxtext-1b-$(date +%H%M)" \
        --cluster=${CLUSTER_NAME} \
        --project=${PROJECT_ID} \
        --location=${ZONE} \
        --compute-type=tpu7x-standard-4t \
        --topology=4x4x8 \
        --image="gcr.io/${PROJECT_ID}/${CLOUD_IMAGE_NAME}" \
        --command="${MAXTEXT_COMMAND}"
    

Workload names must be unique within the cluster. This example appends `$(date +%H%M)` to the workload name.

## Deploy a training workload with TorchTitan

TorchTitan uses [TorchTPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu) to run distributed PyTorch training on Cloud TPU. For more information, see the [TorchTitan on TPU README](https://github.com/google-pytorch/torchtitan/blob/main/torchtitan/experiments/tpu/README.md).

## What's next

  * [Learn about PyTorch on Cloud TPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu)
  * [Use the Google Cloud ML Diagnostics platform to optimize and diagnose your workloads](https://github.com/AI-Hypercomputer/google-cloud-mldiagnostics)
  * [Run a training workload using a recipe optimized for TPU7x](https://github.com/AI-Hypercomputer/tpu-recipes/blob/main/training/ironwood/README.md)
  * [Explore TorchTitan Ironwood recipes](https://github.com/google-pytorch/torchtitan/tree/main/torchtitan/experiments/tpu/recipes/ironwood)
  * [Run a TPU7x microbenchmark](https://github.com/AI-Hypercomputer/accelerator-microbenchmarks/blob/main/Ironwood/Ironwood_Microbenchmarks_readme.md)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
