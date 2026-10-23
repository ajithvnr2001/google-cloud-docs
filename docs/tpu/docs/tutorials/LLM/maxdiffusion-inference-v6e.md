---
url: https://docs.cloud.google.com/tpu/docs/tutorials/LLM/maxdiffusion-inference-v6e/
title: MaxDiffusion inference on v6e TPUs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:12.057729+00:00
---

# MaxDiffusion inference on v6e TPUs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/tutorials/LLM/maxdiffusion-inference-v6e/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MaxDiffusion inference on v6e TPUs

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This tutorial shows how to serve MaxDiffusion models on TPU v6e. In this tutorial, you generate images using the Stable Diffusion XL model.

**Note:** After you complete the inference benchmark, be sure to clean up the TPU resources.

## Before you begin

Prepare to provision a TPU v6e with 4 chips:

  1. Follow [Set up the Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account) guide to set up a Google Cloud project, configure the Google Cloud CLI, enable the Cloud TPU API, and ensure you have access to use Cloud TPUs.

  2. Authenticate with Google Cloud and configure the default project and zone for Google Cloud CLI.
         
         gcloud auth login
         gcloud config set project PROJECT_ID
         gcloud config set compute/zone ZONE




### Secure capacity

When you are ready to secure TPU capacity, see [Cloud TPU Quotas](https://docs.cloud.google.com/tpu/docs/quota) for more information about the Cloud TPU quotas. If you have additional questions about securing capacity, contact your Cloud TPU sales or account team.

### Provision the Cloud TPU environment

You can provision TPU VMs with [GKE](https://docs.cloud.google.com/tpu/docs/tpus-in-gke), with GKE and [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview), or as [queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources).

**Note:** This document describes how to provision TPUs using queued resources. If you are provisioning your TPUs using [Cluster Toolkit](https://docs.cloud.google.com/cluster-toolkit/docs/overview), see [Cluster Toolkit environment setup](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).

### Prerequisites

**Note:** This tutorial has been tested with Python 3.10 or later.

  * Verify that your project has enough `TPUS_PER_TPU_FAMILY` quota, which specifies the maximum number of chips you can access within your Google Cloud project.
  * Verify that your project has enough TPU quota for: 
    * TPU VM quota
    * IP address quota
    * Hyperdisk Balanced quota
  * User project permissions 
    * If you are using GKE with Cluster Toolkit, see [Cluster Toolkit prerequisites](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-environment).



## Provision a TPU v6e
    
    
       gcloud alpha compute tpus queued-resources create QUEUED_RESOURCE_ID \
            --node-id TPU_NAME \
            --project PROJECT_ID \
            --zone ZONE \
            --accelerator-type v6e-4 \
            --runtime-version v2-alpha-tpuv6e \
            --service-account SERVICE_ACCOUNT

Use the `list` or `describe` commands to query the status of your queued resource.
    
    
       gcloud alpha compute tpus queued-resources describe QUEUED_RESOURCE_ID  \
          --project=PROJECT_ID --zone=ZONE

For a complete list of queued resource request statuses, see the [Queued Resources](https://docs.cloud.google.com/tpu/docs/queued-resources) documentation.

## Connect to the TPU using SSH
    
    
       gcloud compute tpus tpu-vm ssh TPU_NAME

## Create a Conda environment

  1. Create a directory for Miniconda:
         
         mkdir -p ~/miniconda3

  2. Download the Miniconda installer script:
         
         wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh

  3. Install Miniconda:
         
         bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

  4. Remove the Miniconda installer script:
         
         rm -rf ~/miniconda3/miniconda.sh

  5. Add Miniconda to your `PATH` variable:
         
         export PATH="$HOME/miniconda3/bin:$PATH"

  6. Reload `~/.bashrc` to apply the changes to the `PATH` variable:
         
         source ~/.bashrc

  7. Create a new Conda environment:
         
         conda create -n tpu python=3.10

  8. Activate the Conda environment:
         
         source activate tpu




## Set up MaxDiffusion

  1. Clone the MaxDiffusion GitHub repository and navigate to the MaxDiffusion directory:
         
         git clone https://github.com/google/maxdiffusion.git && cd maxdiffusion

  2. Switch to the `mlperf-4.1` branch:
         
         git checkout mlperf4.1

  3. Install MaxDiffusion:
         
         pip install -e .

  4. Install dependencies:
         
         pip install -r requirements.txt

  5. Install JAX:
         
         pip install jax[tpu]==0.4.34 jaxlib==0.4.34 ml-dtypes==0.2.0 -i https://us-python.pkg.dev/ml-oss-artifacts-published/jax/simple/ -f https://storage.googleapis.com/jax-releases/libtpu_releases.html

  6. Install additional dependencies:
         
         pip install huggingface_hub==0.25 absl-py flax tensorboardX google-cloud-storage torch tensorflow transformers 




## Generate images

  1. Set environment variables to configure the TPU runtime:
         
         LIBTPU_INIT_ARGS="--xla_tpu_rwb_fusion=false --xla_tpu_dot_dot_fusion_duplicated=true --xla_tpu_scoped_vmem_limit_kib=65536"

  2. Generate images using the prompt and configurations defined in [`src/maxdiffusion/configs/base_xl.yml`](https://github.com/AI-Hypercomputer/maxdiffusion/blob/main/src/maxdiffusion/configs/base_xl.yml):
         
         python -m src.maxdiffusion.generate_sdxl src/maxdiffusion/configs/base_xl.yml run_name="my_run"

When the images have been generated, be sure to clean up the TPU resources.




## Clean up

Delete the TPU:
    
    
    gcloud compute tpus queued-resources delete QUEUED_RESOURCE_ID \
        --project PROJECT_ID \
        --zone ZONE \
        --force \
        --async

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
