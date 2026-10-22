---
url: https://docs.cloud.google.com/deep-learning-vm/docs/create-vm-instance-gcloud/
title: Quickstart: Create a Deep Learning VM instance by using the gcloud CLI \u00a0|\u00a0 Deep Learning VM Images \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:45.782355+00:00
---

# Quickstart: Create a Deep Learning VM instance by using the gcloud CLI  |  Deep Learning VM Images  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deep-learning-vm/docs/create-vm-instance-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Deep Learning VM Images ](https://docs.cloud.google.com/deep-learning-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/deep-learning-vm/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Deep Learning VM instance by using the gcloud CLI

This page shows you how to create a Deep Learning VM Images instance by using the Google Cloud CLI.

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




To use the Google Cloud CLI for this quickstart, you must first install and initialize the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs):

  1. Download and install the Google Cloud CLI using the instructions given on [Installing Google Cloud CLI](https://docs.cloud.google.com/sdk/downloads).
  2. Initialize the SDK using the instructions given in [Initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize).



To use `gcloud` in Cloud Shell for this quickstart, first activate Cloud Shell using the instructions given on [Starting Cloud Shell](https://docs.cloud.google.com/shell/docs/starting-cloud-shell).

## Create a new instance

These instructions create a Deep Learning VM instance with the following parameters:

  * Using a TensorFlow on CUDA 9.2 [image](https://docs.cloud.google.com/deep-learning-vm/docs/images): `tf-latest-cu92`.
  * In the US West1-B [zone](https://docs.cloud.google.com/compute/docs/gpus): `us-west1-b`.
  * Named `my-new-instance`.
  * Of the [instance type](https://docs.cloud.google.com/compute/docs/machine-types) `n1-standard-8`.
  * Using an NVIDIA Tesla V100 [GPU](https://docs.cloud.google.com/compute/docs/gpus): `type=nvidia-tesla-v100,count=8`.
  * With a boot disk of 120 GB.
  * With an NVIDIA GPU driver set to install on first run: `install-nvidia-driver=True`.

**Note:** For more information about additional VM options available to you, see [Choosing an Image](https://docs.cloud.google.com/deep-learning-vm/docs/images).

At the command line, enter the following:
    
    
    export IMAGE_FAMILY="tf-latest-cu92"
    export ZONE="us-west1-b"
    export INSTANCE_NAME="my-new-instance"
    export INSTANCE_TYPE="n1-standard-8"
    gcloud compute instances create $INSTANCE_NAME \
            --zone=$ZONE \
            --image-family=$IMAGE_FAMILY \
            --image-project=deeplearning-platform-release \
            --maintenance-policy=TERMINATE \
            --accelerator="type=nvidia-tesla-v100,count=8" \
            --machine-type=$INSTANCE_TYPE \
            --boot-disk-size=120GB \
            --metadata="install-nvidia-driver=True"
    

After some time, the VM instance is created and a summary of its configuration is shown.

You've just created your first Deep Learning VM instance. To verify the instance and see its status, use the `gcloud` [`list`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/list) command as shown here to list all instances:
    
    
    gcloud compute instances list
    

This displays all Compute Engine instances from all zones in the current project.

You can also view and maintain your Deep Learning VM instance on the Google Cloud console in [Compute Engine VM instances](https://console.cloud.google.com/compute/instances).

To view the status of just this instance:
    
    
    gcloud compute instances describe $INSTANCE_NAME
    

## Access your new instance

After you've created your Deep Learning VM instance, it starts automatically. You can access it using SSH using the following command:
    
    
    gcloud compute ssh $INSTANCE_NAME
    

Compute Engine will propagate your SSH keys and create your user. For more information, see [Connecting to Instances](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).

## Stop the instance

Run the following command from your local machine (not on the instance):
    
    
    gcloud compute instances stop $INSTANCE_NAME
    

The [`stop`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/stop) command performs a clean shutdown.

## Start the instance

After the instance is initially created, Compute Engine starts it. To start the instance manually when it's stopped, run the following command:
    
    
    gcloud compute instances start $INSTANCE_NAME
    

The [`start`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/start) command starts a stopped virtual machine instance.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

To delete the Deep Learning VM instance that you created, at the command line, enter the following command:
    
    
    gcloud compute instances delete $INSTANCE_NAME
    

The [`delete`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/delete) command deletes Compute Engine instances.

## What's next

  * Read a more in-depth description of this process in [Creating a Deep Learning VM instance From the CLI](https://docs.cloud.google.com/deep-learning-vm/docs/cli).
  * Learn more about [Images, image families, and instances](https://docs.cloud.google.com/deep-learning-vm/docs/concepts-images).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
