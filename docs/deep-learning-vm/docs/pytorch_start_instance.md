---
url: https://docs.cloud.google.com/deep-learning-vm/docs/pytorch_start_instance/
title: Create a PyTorch Deep Learning VM instance \u00a0|\u00a0 Deep Learning VM Images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:02.271207+00:00
---

# Create a PyTorch Deep Learning VM instance  |  Deep Learning VM Images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-vm/docs/pytorch_start_instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Deep Learning VM Images ](https://docs.cloud.google.com/deep-learning-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/deep-learning-vm/docs/introduction)



Send feedback 

#  Create a PyTorch Deep Learning VM instance Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to create a PyTorch Deep Learning VM Images instance with PyTorch and other tools pre-installed. You can create a PyTorch instance from Cloud Marketplace within the Google Cloud console or using the command line.

## Before you begin

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

  6. If you are using GPUs with your Deep Learning VM, check the [quotas page](https://console.cloud.google.com/quotas) to ensure that you have enough GPUs available in your project. If GPUs are not listed on the quotas page or you require additional GPU quota, [request a quota increase](https://docs.cloud.google.com/compute/quotas#requesting_additional_quota). 



## Creating a PyTorch Deep Learning VM instance from the Cloud Marketplace

To create a PyTorch Deep Learning VM instance from the Cloud Marketplace, complete the following steps:

  1. Go to the Deep Learning VM Cloud Marketplace page in the Google Cloud console.

[ Go to the Deep Learning VM Cloud Marketplace page](https://console.cloud.google.com/marketplace/details/click-to-deploy-images/deeplearning)

  2. Click **Get started**.

  3. Enter a **Deployment name** , which will be the root of your VM name. Compute Engine appends `-vm` to this name when naming your instance.

  4. Select a **Zone**.

  5. Under **Machine type** , select the specifications that you want for your VM. [Learn more about machine types.](https://docs.cloud.google.com/compute/docs/machine-types)

  6. Under **GPUs** , select the **GPU type** and **Number of GPUs**. If you don't want to use GPUs, click the **Delete GPU** button and skip to step 7. [Learn more about GPUs.](https://docs.cloud.google.com/gpu)

     1. Select a **GPU type**. Not all GPU types are available in all zones. [Find a combination that is supported.](https://docs.cloud.google.com/compute/docs/gpus)
     2. Select the **Number of GPUs**. Each GPU supports different numbers of GPUs. [Find a combination that is supported.](https://docs.cloud.google.com/compute/docs/gpus)
  7. Under **Framework** , select **PyTorch 1.8 + fast.ai 2.1 (CUDA 11.0)**.

  8. If you're using GPUs, an NVIDIA driver is required. You can install the driver yourself, or select **Install NVIDIA GPU driver automatically on first startup**.

  9. You have the option to select **Enable access to JupyterLab via URL instead of SSH (Beta)**. Enabling this Beta feature lets you access your JupyterLab instance using a URL. Anyone who is in the Editor or Owner role in your Google Cloud project can access this URL. Currently, this feature only works in the United States, the European Union, and Asia.

  10. Select a boot disk type and boot disk size.

  11. Select the networking settings that you want.

  12. Click **Deploy**.




If you choose to install NVIDIA drivers, allow 3-5 minutes for installation to complete.

After the VM is deployed, the page updates with instructions for accessing the instance.

## Creating a PyTorch Deep Learning VM instance from the command line

To use the Google Cloud CLI to create a new a Deep Learning VM instance, you must first install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs):

  1. Download and install the Google Cloud CLI using the instructions given on [Installing Google Cloud CLI](https://docs.cloud.google.com/sdk/downloads).
  2. Initialize the SDK using the instructions given in [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize).



To use `gcloud` in Cloud Shell, first activate Cloud Shell using the instructions given on [Starting Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell).

### Without GPUs

To create a Deep Learning VM instance with the latest PyTorch image family and a CPU, enter the following at the command line:
    
    
    export IMAGE_FAMILY="pytorch-latest-cpu"
    export ZONE="us-west1-b"
    export INSTANCE_NAME="my-instance"
    
    gcloud compute instances create $INSTANCE_NAME \
      --zone=$ZONE \
      --image-family=$IMAGE_FAMILY \
      --image-project=deeplearning-platform-release
    

Options:

  * `--image-family` must be either `pytorch-latest-cpu` or `pytorch-VERSION-cpu` (for example, `pytorch-1-13-cpu`).

  * `--image-project` must be `deeplearning-platform-release`.




### With one or more GPUs

Compute Engine offers the option of adding one or more GPUs to your virtual machine instances. GPUs offer faster processing for many complex data and machine learning tasks. To learn more about GPUs, see [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus).

To create a Deep Learning VM instance with the latest PyTorch image family and one or more attached GPUs, enter the following at the command line:
    
    
    export IMAGE_FAMILY="pytorch-latest-gpu"
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

  * `--image-family` must be either `pytorch-latest-gpu` or `pytorch-VERSION-CUDA-VERSION` (for example, `pytorch-1-10-cu110`).

  * `--image-project` must be `deeplearning-platform-release`.

  * `--maintenance-policy` must be `TERMINATE`. To learn more, see [GPU Restrictions](https://docs.cloud.google.com/compute/docs/gpus#restrictions).

  * `--accelerator` specifies the GPU type to use. Must be specified in the format `--accelerator="type=TYPE,count=COUNT"`. For example, `--accelerator="type=nvidia-tesla-v100,count=2"`. See the [GPU models table](https://docs.cloud.google.com/compute/docs/gpus#other_available_nvidia_gpu_models) for a list of available GPU types and counts.

Not all GPU types are supported in all regions. For details, see [GPU regions and zones availability](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

  * `--metadata` is used to specify that the NVIDIA driver should be installed on your behalf. The value is `install-nvidia-driver=True`. If specified, Compute Engine loads the latest stable driver on the first boot and performs the necessary steps (including a final reboot to activate the driver).




If you've elected to install NVIDIA drivers, allow 3-5 minutes for installation to complete.

It may take up to 5 minutes before your VM is fully provisioned. In this time, you will be unable to SSH into your machine. When the installation is complete, to guarantee that the driver installation was successful, you can SSH in and run `nvidia-smi`.

When you've configured your image, you can save a snapshot of your image so that you can start derivitave instances without having to wait for the driver installation.

## Creating a preemptible instance

You can create a preemptible Deep Learning VM instance. A preemptible instance is an instance you can create and run at a much lower price than normal instances. However, Compute Engine might stop (preempt) these instances if it requires access to those resources for other tasks. Preemptible instances always stop after 24 hours. To learn more about preemptible instances, see [Preemptible VM Instances](https://docs.cloud.google.com/compute/docs/instances/preemptible).

To create a preemptible Deep Learning VM instance:

  * Follow the instructions located above to create a new instance using the command line. To the `gcloud compute instances create` command, append the following:
        
        --preemptible




## What's next

For instructions on connecting to your new Deep Learning VM instance through the Google Cloud console or command line, see [Connecting to Instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance). Your instance name is the **Deployment name** you specified with `-vm` appended.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
