---
url: https://docs.cloud.google.com/deep-learning-vm/docs/cli/
title: Create a Deep Learning VM instance from the command line \u00a0|\u00a0 Deep Learning VM Images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:27.918663+00:00
---

# Create a Deep Learning VM instance from the command line  |  Deep Learning VM Images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-vm/docs/cli/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Deep Learning VM Images ](https://docs.cloud.google.com/deep-learning-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/deep-learning-vm/docs/introduction)



Send feedback 

#  Create a Deep Learning VM instance from the command line Stay organized with collections  Save and categorize content based on your preferences. 

This document contains instructions for creating a new Deep Learning VM Images instance from the command line. You can use the `gcloud` command-line tool with your preferred SSH application or in Cloud Shell.

## Before you begin

To use the Google Cloud CLI to create a new Deep Learning VM instance, you must first install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs):

  1. Download and install the Google Cloud CLI using the instructions given on [Installing Google Cloud CLI](https://docs.cloud.google.com/sdk/downloads).
  2. Initialize the SDK using the instructions given in [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize).



To use `gcloud` in Cloud Shell, first activate Cloud Shell using the instructions given on [Starting Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell).

Next, choose the specific Deep Learning VM image to use. Your choice depends on your preferred framework and processor type. For more information about the available images, see [Choosing an Image](https://docs.cloud.google.com/deep-learning-vm/docs/images).

**Note:** If you are using GPUs with your Deep Learning VM, check the quotas page to ensure that you have enough GPUs available in your project: [Quotas](https://console.cloud.google.com/quotas). If GPUs are not listed on the quotas page or you require additional GPU quota, you can request a quota increase. See "[Requesting additional quota](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota)" on the Compute Engine [Resource Quotas](https://docs.cloud.google.com/compute/quotas) page.

## Creating an instance without GPUs

To provision a Deep Learning VM instance with a CPU but no GPU:
    
    
    export IMAGE_FAMILY="tf-ent-latest-cpu"
    export ZONE="us-west1-b"
    export INSTANCE_NAME="my-instance"
    
    gcloud compute instances create $INSTANCE_NAME \
      --zone=$ZONE \
      --image-family=$IMAGE_FAMILY \
      --image-project=deeplearning-platform-release
    

Options:

  * `--image-family` must be one of the CPU-specific image types. For more information, see [Choosing an Image](https://docs.cloud.google.com/deep-learning-vm/docs/images).

  * `--image-project` must be `deeplearning-platform-release`.




## Creating an instance with one or more GPUs

Compute Engine offers the option of adding GPUs to your virtual machine instances. GPUs offer faster processing for many complex data and machine learning tasks. To learn more about GPUs, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

To provision a Deep Learning VM instance with one or more GPUs:
    
    
    export IMAGE_FAMILY="tf-ent-latest-gpu"
    export ZONE="us-west1-b"
    export INSTANCE_NAME="my-instance"
    
    gcloud compute instances create $INSTANCE_NAME \
      --zone=$ZONE \
      --image-family=$IMAGE_FAMILY \
      --image-project=deeplearning-platform-release \
      --maintenance-policy=TERMINATE \
      --accelerator="type=nvidia-tesla-v100,count=1" \
      --metadata="install-nvidia-driver=True"
    

Options:

  * `--image-family` must be one of the GPU-specific image types. For more information, see [Choosing an Image](https://docs.cloud.google.com/deep-learning-vm/docs/images).

  * `--image-project` must be `deeplearning-platform-release`.

  * `--maintenance-policy` must be `TERMINATE`. See [GPU Restrictions](https://docs.cloud.google.com/compute/docs/gpus#restrictions) to learn more.

  * `--accelerator` specifies the GPU type to use. Must be specified in the format `--accelerator="type=TYPE,count=COUNT"`. Supported values of `TYPE` are:

    * `nvidia-tesla-v100` (`count=1` or `8`)
    * `nvidia-tesla-p100` (`count=1`, `2`, or `4`)
    * `nvidia-tesla-p4` (`count=1`, `2`, or `4`)
**Caution:** NVIDIA P100 GPUs reach end of support on September 15, 2026. For more information, see [NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos). 

Not all GPU types are supported in all regions. For details, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

  * `--metadata` is used to specify that the NVIDIA driver should be installed on your behalf. The value is `install-nvidia-driver=True`. If specified, Compute Engine loads the latest stable driver on the first boot and performs the necessary steps (including a final reboot to activate the driver).




If you've elected to install NVIDIA drivers, allow 3-5 minutes for installation to complete.

It may take up to 5 minutes before your VM is fully provisioned. In this time, you will be unable to connect to your instance using SSH. When the installation is complete, to ensure that the driver installation was successful, you can connect to your instance using SSH and run `nvidia-smi`.

When you've configured your image, you can save a snapshot of your image so that you can start derivative instances without having to wait for the driver installation.

## Creating a preemptible instance

You can create a preemptible Deep Learning VM instance. A preemptible instance is an instance you can create and run at a much lower price than normal instances. However, Compute Engine might stop (preempt) these instances if it requires access to those resources for other tasks. Preemptible instances always stop after 24 hours. To learn more about preemptible instances, see [Preemptible VM Instances](https://docs.cloud.google.com/compute/docs/instances/preemptible).

To create a preemptible Deep Learning VM instance:

  * Follow the instructions in the _Creating an instance without GPUs_ section to create a new instance. To the `gcloud compute instances create` command, append the following:
        
        --preemptible




## What's next

For instructions on connecting to your new Deep Learning VM instance through the Google Cloud console or command line, see [Connecting to Instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance). Your instance name is the **Deployment name** you specified with `-vm` appended.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
