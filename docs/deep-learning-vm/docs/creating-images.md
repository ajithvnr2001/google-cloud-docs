---
url: https://docs.cloud.google.com/deep-learning-vm/docs/creating-images/
title: Create a new image from an existing Deep Learning VM instance \u00a0|\u00a0 Deep Learning VM Images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:50.989511+00:00
---

# Create a new image from an existing Deep Learning VM instance  |  Deep Learning VM Images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-vm/docs/creating-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Deep Learning VM Images ](https://docs.cloud.google.com/deep-learning-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/deep-learning-vm/docs/introduction)



Send feedback 

#  Create a new image from an existing Deep Learning VM instance Stay organized with collections  Save and categorize content based on your preferences. 

Installing NVIDIA drivers on a new VM instance can be time consuming, especially if you are creating numerous images. One way to prevent this is to create your own image that is based on one of the Deep Learning VM images, but that already has the NVIDIA drivers preinstalled.

This topic describes how to create a new image based on an existing Deep Learning VM image.

## Create a new instance

First, follow the instructions in one of the following topics to create a new instance. Be sure to include at least one GPU in your new instance.

  * [Creating a TensorFlow Deep Learning VM Instance](https://docs.cloud.google.com/deep-learning-vm/docs/tensorflow_start_instance)
  * [Creating a PyTorch Deep Learning VM Instance](https://docs.cloud.google.com/deep-learning-vm/docs/pytorch_start_instance)
  * [Creating a Deep Learning VM Instance from the Command Line](https://docs.cloud.google.com/deep-learning-vm/docs/cli)
  * [Creating a Deep Learning VM Instance from the Cloud Marketplace](https://docs.cloud.google.com/deep-learning-vm/docs/cloud-marketplace)



## Verify NVIDIA driver install

Once the instance has booted, verify that the NVIDIA driver has been installed:

  1. SSH to your image: 
         
         gcloud compute ssh "DEPLOYMENT_NAME"

  2. Run the following command: 
         
         nvidia-smi




If the drivers have been installed, you can continue.

## Stop the instance

Stop the instance by running the following command:
    
    
    gcloud compute instances stop "DEPLOYMENT_NAME"

## Create your own image

Now you create your own image based on the stopped instance. Run the following at the command line, giving the new image a name and a family name:
    
    
    gcloud compute images create "NEW_IMAGE_NAME" \
            --source-disk DEPLOYMENT_NAME \
            --source-disk-zone ZONE \
            --family NEW_FAMILY_NAME

Once the command is finished running, you have a new image with NVIDIA drivers preinstalled that you can use to create new Deep Learning VM instances.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
