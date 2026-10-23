---
url: https://docs.cloud.google.com/tpu/docs/pytorch-pods/
title: Run PyTorch code on TPU slices \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:17.688865+00:00
---

# Run PyTorch code on TPU slices  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/pytorch-pods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run PyTorch code on TPU slices

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. **Deprecated:** This page applies to PyTorch/XLA, which is deprecated and replaced by [TorchTPU](https://docs.cloud.google.com/tpu/docs/pytorch-on-tpu). The PyTorch/XLA repo will be archived on November 15, 2026. Start new PyTorch workloads with TorchTPU and migrate existing PyTorch/XLA workloads to TorchTPU. 

Before running the commands in this document, follow the instructions in [Set up an account and Cloud TPU project](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

After you have your PyTorch code running on a single TPU VM, you can scale up your code by running it on a [TPU slice](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#slices). TPU slices are multiple TPU boards connected to each other over dedicated high-speed network connections. This document is an introduction to running PyTorch code on TPU slices.

## Required roles

To get the permissions that you need to create a TPU and connect to it using SSH, ask your administrator to grant you the following IAM roles on your project: 

  * [TPU Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin) (`roles/tpu.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Cloud TPU slice

  1. Define environment variables for Google Cloud CLI command parameters.
         
         export PROJECT_ID=your-project-id
         export TPU_NAME=your-tpu-name
         export ZONE=us-central1-b
         export ACCELERATOR_TYPE=v6e-8
         export RUNTIME_VERSION=v2-alpha-tpuv6e

#### Environment variable descriptions

     * `PROJECT_ID`: Your Google Cloud project ID. Use an existing project or [create a new one.](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#set-up-project)
     * `TPU_NAME`: The name of the TPU.
     * `ZONE`: The zone in which to create the TPU VM. For more information about supported zones, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones). 
     * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions). 
     * `RUNTIME_VERSION`: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).
  2. Create your TPU VM by running the following command:
         
         gcloud compute tpus tpu-vm create $TPU_NAME \
              --zone=$ZONE \
              --project=$PROJECT_ID \
              --accelerator-type=$ACCELERATOR_TYPE \
              --version=$RUNTIME_VERSION
         




## Install PyTorch/XLA on your slice

After creating the TPU slice, you must install PyTorch on all hosts in the TPU slice. You can do this using the `gcloud compute tpus tpu-vm ssh` command using the `--worker=all` and `--command` parameters.

  1. Create a file named `requirements.txt` with the following content:
         
         --find-links https://storage.googleapis.com/libtpu-releases/index.html
         --find-links https://storage.googleapis.com/libtpu-wheels/index.html
         torch~=2.6.0
         torch_xla[tpu]~=2.6.0
         torchvision
         ray[default]==2.40.0
         

  2. Copy `requirements.txt` to each VM in your slice:
         
         gcloud compute tpus tpu-vm tpu-vm scp ./requirements.txt \
              $TPU_NAME:~/ \
              --zone=$ZONE \
              --project=$PROJECT_ID \
              --worker=all
         

  3. Install the dependencies on each VM in your slice:
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME \
              --zone=$ZONE \
              --project=$PROJECT_ID \
              --worker=all \
              --command="pip3 install -r requirements.txt"
         

  4. Clone XLA on all TPU VM workers:
         
         gcloud compute tpus tpu-vm ssh $TPU_NAME \
              --zone=$ZONE \
              --project=$PROJECT_ID \
              --worker=all \
              --command="git clone https://github.com/pytorch/xla.git"
         




## Run a training script on your TPU slice

Run the training script on all workers. The training script uses a Single Program Multiple Data (SPMD) sharding strategy. For more information on SPMD, see [PyTorch/XLA SPMD User Guide](https://pytorch.org/xla/release/r2.4/spmd.html).
    
    
    gcloud compute tpus tpu-vm ssh $TPU_NAME \
       --zone=$ZONE \
       --project=$PROJECT_ID \
       --worker=all \
       --command="PJRT_DEVICE=TPU python3 ~/xla/test/spmd/test_train_spmd_imagenet.py  \
       --fake_data \
       --model=resnet50  \
       --num_epochs=1 2>&1 | tee ~/logs.txt"
    

The training takes about 15 minutes. When it completes, you should see a message similar to the following:
    
    
       Epoch 1 test end 23:49:15, Accuracy=100.00
       10.164.0.11 [0] Max Accuracy: 100.00%
    

## Clean up

When you are done with your TPU VM, follow these steps to clean up your resources.

  1. Disconnect from the Cloud TPU instance, if you have not already done so:
         
         exit
         

Your prompt should now be `username@projectname`, showing you are in the Cloud Shell.

  2. Delete your Cloud TPU resources.
         
         gcloud compute tpus tpu-vm delete $TPU_NAME --zone=$ZONE
         

  3. Verify the resources have been deleted by running `gcloud compute tpus tpu-vm list`. The deletion might take several minutes. The output from the following command shouldn't include any of the resources created in this tutorial:
         
         gcloud compute tpus tpu-vm list --zone=$ZONE
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
