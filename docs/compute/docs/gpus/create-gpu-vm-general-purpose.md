---
url: https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-general-purpose/
title: Create an N1 VM that has attached GPUs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:54.990062+00:00
---

# Create an N1 VM that has attached GPUs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-general-purpose/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an N1 VM that has attached GPUs Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

When you need a general-purpose VM with the option to add a GPU for moderate acceleration, you can create compute instances with attached GPUs on Google Cloud Compute Engine's [N1 general-purpose machines](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines). Attaching earlier-generation GPUs (such as T4, V100, and P4) to N1 VMs provides cost-effective flexibility for smaller-scale or less performance-critical AI tasks, remote virtual workstations, and video transcoding. Most N1 machine types support attached GPUs, with the exception of N1 shared-core machines.

If your primary workload is highly GPU-intensive and can benefit from the latest GPU architectures and platform optimizations, choose [accelerator-optimized A-series or G-series machines](https://docs.cloud.google.com/compute/docs/gpus#introduction).

## Before you begin

  * To review additional prerequisite steps such as selecting an OS image and checking GPU quota, review the [overview](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus) document. 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to create VMs, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create VMs. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create VMs:

  * `compute.instances.create` on the project
  * To use a custom image to create the VM: `compute.images.useReadOnly` on the image 
  * To use a snapshot to create the VM: `compute.snapshots.useReadOnly` on the snapshot 
  * To use an instance template to create the VM: `compute.instanceTemplates.useReadOnly` on the instance template 
  * To specify a subnet for your VM: `compute.subnetworks.use` on the project or on the chosen subnet 
  * To specify a static IP address for the VM: `compute.addresses.use` on the project 
  * To assign an external IP address to the VM when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet 
  * To assign a [legacy network](https://docs.cloud.google.com/vpc/docs/legacy) to the VM: `compute.networks.use` on the project 
  * To assign an external IP address to the VM when using a legacy network: `compute.networks.useExternalIp` on the project 
  * To set VM instance metadata for the VM: `compute.instances.setMetadata` on the project 
  * To set tags for the VM: `compute.instances.setTags` on the VM 
  * To set labels for the VM: `compute.instances.setLabels` on the VM 
  * To set a service account for the VM to use: `compute.instances.setServiceAccount` on the VM 
  * To create a new disk for the VM: `compute.disks.create` on the project 
  * To attach an existing disk in read-only or read-write mode: `compute.disks.use` on the disk 
  * To attach an existing disk in read-only mode: `compute.disks.useReadOnly` on the disk 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Overview

The following GPU models can be attached to VMs that use N1 machine families.

**Caution:** NVIDIA T4 and P4 GPUs reach end of support on August 1, 2027. For more information, see [NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos) and [NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos).  NVIDIA GPUs: 

  * NVIDIA T4: `nvidia-tesla-t4`
  * NVIDIA P4: `nvidia-tesla-p4`
  * NVIDIA V100: `nvidia-tesla-v100`



NVIDIA RTX Virtual Workstation (vWS) (formerly known as NVIDIA GRID):

  * NVIDIA T4 Virtual Workstation: `nvidia-tesla-t4-vws`
  * NVIDIA P4 Virtual Workstation: `nvidia-tesla-p4-vws`

For these virtual workstations, an NVIDIA RTX Virtual Workstation (vWS) license is automatically added to your instance.




## Create a VM that has attached GPUs

You can create an N1 VM that has attached GPUs by using either the Google Cloud console, Google Cloud CLI, or REST.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Specify a **Name** for your VM. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  3. Select a region and zone where GPUs are available. See the list of available [GPU zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

  4. In the **Machine configuration** section, select the **GPUs** machine family, and then do the following:

     1. In the **GPU type** list, select one of the GPU models supported on N1 machines.
     2. In the **Number of GPUs** list, select the number of GPUs.
     3. If your GPU model supports [NVIDIA RTX Virtual Workstations (vWS) for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations), and you plan on running graphics-intensive workloads on this VM, select **Enable Virtual Workstation (NVIDIA GRID)**.

     4. In the **Machine type** list, select one of the preset N1 machine types. Alternatively, you can also specify custom machine type settings.

  5. In the **Boot disk** section, click **Change**. This opens the **Boot disk configuration** page.

  6. On the **Boot disk configuration** page, do the following:

     1. On the **Public images** tab, choose a [supported Compute Engine image](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support) or [Deep Learning VM Images](https://docs.cloud.google.com/ai-platform/deep-learning-vm/docs/images).
     2. Specify a boot disk size of at least 40 GB.
     3. To confirm your boot disk options, click **Select**.
  7. Optional: In the **VM provisioning model** list, select a [provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

  8. To create and start the VM, click **Create**.




###  gcloud 

To create and start a VM use the [`gcloud compute instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) command with the following flags.

If your workload is fault-tolerant or can start at any time, then consider using a different provisioning model to reduce your costs. To change your provisioning model, include the `--provisioning-model=PROVISIONING_MODEL` flag in the command. For more information about the available models, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).
    
    
    gcloud compute instances create VM_NAME \
        --machine-type MACHINE_TYPE \
        --zone ZONE \
        --boot-disk-size DISK_SIZE \
        --accelerator type=ACCELERATOR_TYPE,count=ACCELERATOR_COUNT \
        [--image IMAGE | --image-family IMAGE_FAMILY] \
        --image-project IMAGE_PROJECT \
        --maintenance-policy TERMINATE \
        [--provisioning-model=PROVISIONING_MODEL]
    

Replace the following:

  * `VM_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new VM.
  * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-types#gpu-support) that you selected for your VM.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/zones) for the VM. This zone must support the [GPU type](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  * `DISK_SIZE`: the size of your boot disk in GB. Specify a boot disk size of at least 40 GB.
  * `IMAGE` or `IMAGE_FAMILY` that [supports GPUs](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). Specify one of the following:

    * `IMAGE`: the required version of a public image. For example, `--image debian-10-buster-v20200309`.
    * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info). This creates the VM from the most recent, non-deprecated OS image. For example, if you specify `--image-family debian-10`, Compute Engine creates a VM from the latest version of the OS image in the Debian 10 image family.

You can also specify a custom image or [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images).

  * `IMAGE_PROJECT`: the Compute Engine [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that the image family belongs to. If using a custom image or Deep Learning VM Images, specify the project that those images belong to.

  * `PROVISIONING_MODEL`: the provisioning model for the VM. Specify either `SPOT` or `FLEX_START`. If you don't specify a provisioning model, the standard model is used. This flag is optional.

  * `ACCELERATOR_COUNT`: the number of GPUs that you want to add to your VM. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a list of GPU limits based on the machine type of your VM.

  * `ACCELERATOR_TYPE`: the [GPU model](https://docs.cloud.google.com/compute/docs/gpus#introduction) that you want to use. If you plan on running graphics-intensive workloads on this VM, use one of the [virtual workstation models](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations).

Choose one of the following values:

    * NVIDIA GPUs:

      * NVIDIA T4: `nvidia-tesla-t4`
      * NVIDIA P4: `nvidia-tesla-p4`
      * NVIDIA V100: `nvidia-tesla-v100`
    * NVIDIA RTX Virtual Workstation (vWS) (formerly known as NVIDIA GRID):

      * NVIDIA T4 Virtual Workstation: `nvidia-tesla-t4-vws`
      * NVIDIA P4 Virtual Workstation: `nvidia-tesla-p4-vws`

For these virtual workstations, an NVIDIA RTX Virtual Workstation (vWS) license is automatically added to your instance.




**Example**

For example, you can use the following `gcloud` command to start an Ubuntu 22.04 VM with 1 NVIDIA T4 GPU and 2 vCPUs in the `us-east1-d` zone.
    
    
    gcloud compute instances create gpu-instance-1 \
        --machine-type n1-standard-2 \
        --zone us-east1-d \
        --boot-disk-size 40GB \
        --accelerator type=nvidia-tesla-t4,count=1 \
        --image-family ubuntu-2204-lts \
        --image-project ubuntu-os-cloud \
        --maintenance-policy TERMINATE
    

###  REST 

Identify the GPU type that you want to add to your VM. Submit a GET request to list the GPU types that are available to your project in a specific zone.

To create VMs at a discounted price, you can specify a different provisioning model by adding the `"provisioningModel": "PROVISIONING_MODEL"` field to the `scheduling` object in your request. For more information about the available models, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/acceleratorTypes
    

Replace the following:

  * `PROJECT_ID`: project ID.
  * `ZONE`: [zone](https://docs.cloud.google.com/compute/docs/zones) from which you want to list the available GPU types.



Send a POST request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). Include the `acceleratorType` parameter to specify which GPU type you want to use, and include the `acceleratorCount` parameter to specify how many GPUs you want to add. Also set the `onHostMaintenance` parameter to `TERMINATE`.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "machineType": "projects/PROJECT_ID/zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks":
      [
        {
          "type": "PERSISTENT",
          "initializeParams":
          {
            "diskSizeGb": "DISK_SIZE",
            "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY"
          },
          "boot": true
        }
      ],
      "name": "VM_NAME",
      "networkInterfaces":
      [
        {
          "network": "projects/PROJECT_ID/global/networks/NETWORK"
        }
      ],
      "guestAccelerators":
      [
        {
          "acceleratorCount": ACCELERATOR_COUNT,
          "acceleratorType": "projects/PROJECT_ID/zones/ZONE/acceleratorTypes/ACCELERATOR_TYPE"
        }
      ],
      "scheduling":
      {
        ["automaticRestart": true],
        "onHostMaintenance": "TERMINATE",
        "provisioningModel": "PROVISIONING_MODEL"
      },
    }
    
    

Replace the following:

  * `VM_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) of the VM.
  * `PROJECT_ID`: your project ID.
  * `ZONE`: the [zone](https://docs.cloud.google.com/compute/docs/zones) for the VM. This zone must support the [GPU type](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  * `MACHINE_TYPE`: the [machine type](https://docs.cloud.google.com/compute/docs/machine-types) that you selected for the VM. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) to see what machine types are available based on your chosen GPU count.
  * `IMAGE` or `IMAGE_FAMILY`: specify one of the following:

    * `IMAGE`: the required version of a public image. For example, `"sourceImage": "projects/debian-cloud/global/images/debian-10-buster-v20200309"`
    * `IMAGE_FAMILY`: an [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info). This creates the VM from the most recent, non-deprecated OS image. For example, if you specify `"sourceImage": "projects/debian-cloud/global/images/family/debian-10"`, Compute Engine creates a VM from the latest version of the OS image in the Debian 10 image family.

You can also specify a custom image or [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images).

  * `IMAGE_PROJECT`: the Compute Engine [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that the image family belongs to. If using a custom image or Deep Learning VM Images, specify the project that those images belong to.

  * `DISK_SIZE`: the size of your boot disk in GB. Specify a boot disk size of at least 40 GB.

  * `NETWORK`: the VPCnetwork that you want to use for the VM. You can specify `default` to use your default network.

  * `ACCELERATOR_COUNT`: the number of GPUs that you want to add to your VM. See [GPUs on Compute Engine](https://docs.cloud.google.com/compute/docs/gpus#introduction) for a list of GPU limits based on the machine type of your VM.

  * `ACCELERATOR_TYPE`: the [GPU model](https://docs.cloud.google.com/compute/docs/gpus#introduction) that you want to use. If you plan on running graphics-intensive workloads on this VM, use one of the [virtual workstation models](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations).

Choose one of the following values:

    * NVIDIA GPUs:

      * NVIDIA T4: `nvidia-tesla-t4`
      * NVIDIA P4: `nvidia-tesla-p4`
      * NVIDIA V100: `nvidia-tesla-v100`
    * NVIDIA RTX Virtual Workstation (vWS) (formerly known as NVIDIA GRID):

      * NVIDIA T4 Virtual Workstation: `nvidia-tesla-t4-vws`
      * NVIDIA P4 Virtual Workstation: `nvidia-tesla-p4-vws`

For these virtual workstations, an NVIDIA RTX Virtual Workstation (vWS) license is automatically added to your instance.

  * `PROVISIONING_MODEL`: the provisioning model for the VM. Specify either `SPOT` or `FLEX_START`. If you don't specify a provisioning model, the standard model is used. This property is optional. For more information on provisioning models, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).




## Install drivers

To install the drivers, choose one of the following options:

  * If you plan to run graphics-intensive workloads, such as those for gaming and visualization, [install drivers for the NVIDIA RTX Virtual Workstation](https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers).
  * For most workloads, [install the GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu).



## What's next?

  * Learn more about [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).
  * [Add Local SSDs to your instances](https://docs.cloud.google.com/compute/docs/disks/local-ssd). Local SSD devices pair well with GPUs when your apps require high-performance storage.
  * [Install the GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu). If you enabled an NVIDIA RTX Virtual Workstation, [install a driver for the virtual workstation](https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers).
  * To handle GPU host maintenance, see [Handling GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
