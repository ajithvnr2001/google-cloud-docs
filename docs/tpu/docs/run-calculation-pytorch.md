---
url: https://docs.cloud.google.com/tpu/docs/run-calculation-pytorch/
title: Run a calculation on a Cloud TPU VM using PyTorch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:54.480143+00:00
---

# Run a calculation on a Cloud TPU VM using PyTorch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/run-calculation-pytorch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run a calculation on a Cloud TPU VM using PyTorch

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. **Deprecated:** This page applies to PyTorch/XLA, which is deprecated and replaced by [TorchTPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu). The PyTorch/XLA repo will be archived on November 15, 2026. Start new PyTorch workloads with TorchTPU and migrate existing PyTorch/XLA workloads to TorchTPU. 

This document provides a brief introduction to working with PyTorch and Cloud TPU.

**Note:** This example shows how to run code on a v5litepod-8 (v5e) TPU, which is a single-host TPU. Single-host TPUs have only one TPU VM. To run code on TPUs with more than one TPU VM (for example, v5litepod-32 or larger), see [Run PyTorch code on Cloud TPU slices](https://docs.cloud.google.com/tpu/docs/pytorch-pods).

## Before you begin

Before running the commands in this document, you must create a Google Cloud account, install the Google Cloud CLI, and configure the `gcloud` command. For more information, see [Set up the Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

### Required roles

To get the permissions that you need to create a TPU and connect to it using SSH, ask your administrator to grant you the following IAM roles on your project: 

  * [TPU Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin) (`roles/tpu.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Cloud TPU using `gcloud`

  1. Define some environment variables to make the commands easier to use.
         
         export PROJECT_ID=your-project-id
         export TPU_NAME=your-tpu-name
         export ZONE=us-east5-a
         export ACCELERATOR_TYPE=v5litepod-8
         export RUNTIME_VERSION=v2-alpha-tpuv5-lite

#### Environment variable descriptions

     * `PROJECT_ID`: Your Google Cloud project ID. Use an existing project or [create a new one.](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#set-up-project)
     * `TPU_NAME`: The name of the TPU.
     * `ZONE`: The zone in which to create the TPU VM. For more information about supported zones, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones). 
     * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions). 
     * `RUNTIME_VERSION`: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).
  2. Create your TPU VM by running the following command:
         
         gcloud compute tpus tpu-vm create $TPU_NAME \
              --project=$PROJECT_ID \
              --zone=$ZONE \
              --accelerator-type=$ACCELERATOR_TYPE \
              --version=$RUNTIME_VERSION
         




## Connect to your Cloud TPU VM

Connect to your TPU VM over SSH using the following command:
    
    
    gcloud compute tpus tpu-vm ssh $TPU_NAME \
        --project=$PROJECT_ID \
        --zone=$ZONE
    

If you cannot connect to a TPU VM using SSH, it might be because the TPU VM does not have an external IP address. To access a TPU VM without an external IP address, follow the instructions in [Connect to a TPU VM without a public IP address](https://docs.cloud.google.com/tpu/docs/tpu-iap).

## Install PyTorch/XLA on your TPU VM

  1. Save the following to a file named `requirements.txt`:
         
         --find-links https://storage.googleapis.com/libtpu-releases/index.html
         --find-links https://storage.googleapis.com/libtpu-wheels/index.html
         torch~=2.6.0
         torch_xla[tpu]~=2.6.0
         ray[default]==2.40.0
         

  2. Install the dependencies:
         
         pip install -r requirements.txt
         




## Verify PyTorch can access TPUs

Use the following command to verify PyTorch can access your TPUs:
    
    
    PJRT_DEVICE=TPU python3 -c "import torch_xla.core.xla_model as xm; print(xm.get_xla_supported_devices(\"TPU\"))"
    

The output from the command should look like the following:
    
    
    ['xla:0', 'xla:1', 'xla:2', 'xla:3', 'xla:4', 'xla:5', 'xla:6', 'xla:7']
    

## Perform a basic calculation

  1. Create a file named `tpu-test.py` in the current directory and add the following script to it:
         
         import torch
         import torch_xla.core.xla_model as xm
         
         dev = xm.xla_device()
         t1 = torch.randn(3,3,device=dev)
         t2 = torch.randn(3,3,device=dev)
         print(t1 + t2)
         

  2. Run the script:
         
         PJRT_DEVICE=TPU python3 tpu-test.py
         

The output from the script shows the result of the computation:
         
         tensor([[-0.2121,  1.5589, -0.6951],
                  [-0.7886, -0.2022,  0.9242],
                  [ 0.8555, -1.8698,  1.4333]], device='xla:1')
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

  1. Disconnect from the Cloud TPU instance, if you have not already done so:
         
         exit
         

Your prompt should now be `username@projectname`, showing that you are in the Cloud Shell.

  2. Delete your Cloud TPU.
         
         gcloud compute tpus tpu-vm delete $TPU_NAME \
              --project=$PROJECT_ID \
              --zone=$ZONE
         

  3. Verify that the resources have been deleted by running the following command. Make sure your TPU is no longer listed. The deletion might take several minutes.
         
         gcloud compute tpus tpu-vm list \
              --zone=$ZONE
         




## What's next

Read more about Cloud TPU VMs:

  * [Run PyTorch code on TPU slices](https://docs.cloud.google.com/tpu/docs/pytorch-pods)
  * [Manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm)
  * [Cloud TPU system architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm)
  * [PyTorch/XLA documentation](https://pytorch.org/xla/release/1.7/index.html)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
