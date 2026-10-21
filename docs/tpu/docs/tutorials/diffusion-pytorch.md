---
url: https://docs.cloud.google.com/tpu/docs/tutorials/diffusion-pytorch/
title: Training ResNet-50 on Cloud TPU with PyTorch \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:45:39.639496+00:00
---

# Training ResNet-50 on Cloud TPU with PyTorch  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/tutorials/diffusion-pytorch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback 

#  Training ResNet-50 on Cloud TPU with PyTorch Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This tutorial shows you how to train the ResNet-50 model on a Cloud TPU device with PyTorch. You can apply the same pattern to other TPU-optimized image classification models that use PyTorch and the ImageNet dataset.

The model in this tutorial is based on [Deep Residual Learning for Image Recognition](https://arxiv.org/pdf/1512.03385.pdf), which first introduces the residual network (ResNet) architecture. The tutorial uses the 50-layer variant, ResNet-50, and demonstrates training the model using [PyTorch/XLA](https://github.com/pytorch/xla).

**Warning:** This tutorial uses a third-party dataset. Google provides no representation, warranty, or other assurances about the validity, or any other aspects of this dataset.

## Objectives

  * Prepare the dataset.
  * Run the training job.
  * Verify the output results.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * Compute Engine
  * Cloud TPU



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

## Before you begin

Before starting this tutorial, check that your Google Cloud project is correctly set up.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

This walkthrough uses billable components of Google Cloud. Check the [Cloud TPU pricing page](https://docs.cloud.google.com/tpu/docs/pricing) to estimate your costs. Be sure to clean up resources you created when you've finished with them to avoid unnecessary charges.




## Create a TPU VM

  1. Open a Cloud Shell or a terminal window.

[Open Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. Define environment variables for Google Cloud CLI command parameters:
         
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
  3. Create a TPU VM
         
         gcloud compute tpus tpu-vm create $TPU_NAME \
          --accelerator-type=$ACCELERATOR_TYPE \
          --version=$RUNTIME_VERSION \
          --zone=$ZONE \
          --project=$PROJECT_ID
         

**Note:** The first time you run a command in a new Cloud Shell VM, an `Authorize Cloud Shell` page is displayed. Click `Authorize` at the bottom of the page to allow `gcloud` to make Google Cloud API calls with your credentials.
  4. Connect to your TPU VM using SSH:
         
         gcloud compute tpus tpu-vm ssh  $TPU_NAME --zone=$ZONE
         




## Install PyTorch/XLA on your TPU VM

  1. Create a file named `requirements.txt` and add the following content:
         
         --find-links https://storage.googleapis.com/libtpu-releases/index.html
         --find-links https://storage.googleapis.com/libtpu-wheels/index.html
         torch~=2.6.0
         torch_xla[tpu]~=2.6.0
         torchvision
         ray[default]==2.40.0
         

  2. Install the dependencies:
         
         pip install -r requirements.txt
         

  3. Clone the [PyTorch/XLA GitHub repository](https://github.com/pytorch/xla)
         
         git clone --depth=1 https://github.com/pytorch/xla.git
         

  4. Run the training script with fake data
         
         PJRT_DEVICE=TPU python3 xla/test/test_train_mp_imagenet.py \
         --fake_data \
         --batch_size=256 \
         --num_epochs=1
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

  1. Disconnect from the TPU VM:
         
         exit
         

  2. Delete your TPU VM.
         
         gcloud compute tpus tpu-vm delete $TPU_NAME \
             --zone=$ZONE
         




## What's next

  * [Training diffusion models with PyTorch](https://docs.cloud.google.com/tpu/docs/tutorials/diffusion-pytorch)
  * [Troubleshooting PyTorch on TPUs](https://docs.cloud.google.com/tpu/docs/troubleshooting/trouble-pytorch)
  * [PyTorch/XLA documentation](https://pytorch.org/xla/)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
