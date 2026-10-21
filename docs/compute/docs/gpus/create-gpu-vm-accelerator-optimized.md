---
url: https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized/
title: Create an A3 High or A2 instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:52.691667+00:00
---

# Create an A3 High or A2 instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-accelerator-optimized/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create an A3 High or A2 instance Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document explains how to create a virtual machine (VM) instance that uses a machine type from the [A2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms) or [A3 High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) accelerator-optimized machine series.

For A3 High machine types, this document only covers machine types that have fewer than 8 GPUs attached. These A3 High machine types with fewer than 8 GPUs can only be created as Spot VMs or Flex-start VMs. To create an A3 instance that has 8 GPUs attached, see [Create an A3 Mega, A3 High, or A3 Edge instance with GPUDirect enabled](https://docs.cloud.google.com/compute/docs/gpus/gpudirect).

To create multiple A3 or A2 VMs, you can also use one of the following options:

  * **Managed instance groups (MIGs)** : for workloads that require high availability, scalability, and automated repairs, you can [create a MIG that uses a GPU instance template](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms).
  * **Bulk instance creation** : to create a large number of independent instances, you can [create A3 or A2 VMs in bulk](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-bulk).



## Before you begin

  * To review limitations and additional prerequisite steps for creating instances with attached GPUs, such as selecting an OS image and checking GPU quota, see [Overview of creating an instance with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus). 
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

## Create a VM that has attached GPUs

To create a GPU VM that specifies a compact placement policy, use the gcloud CLI or REST API. Otherwise, select one of the following options:

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.   
  
[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)
  2. In the **Name** field, enter a unique name for your instance. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).
  3. Select a region and zone where these GPU machine types are available. See [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  4. In the machine types section, select **GPUs**. 
     1. In the **GPU type** list, select the GPU type. 
        * For A2 accelerator-optimized VMs, select either `NVIDIA A100 40GB` or `NVIDIA A100 80GB`
        * For A3 accelerator-optimized VMs, select `NVIDIA H100 80GB`
     2. In the **Number of GPUs** list, select the number of GPUs. **Note:** Each accelerator-optimized machine type has a fixed number of GPUs attached. If you change the number of GPUs, the machine type changes.
  5. Configure the boot disk as follows: 
     1. In the **OS and storage** section, click **Change**. This opens the **Boot disk configuration** page.
     2. On the **Boot disk configuration** page, do the following: 
        1. On the **Public images** tab, choose a [supported Compute Engine image](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support) or [Deep Learning VM Images](https://docs.cloud.google.com/ai-platform/deep-learning-vm/docs/images). 
        1. Specify a boot disk size of at least 40 GiB.
        2. To confirm your boot disk options, click **Select**.
  6. Configure the provisioning model. **Note:** A3 machine types with fewer than 8 GPUs can only be created as Spot VMs or Flex-start VMs. When creating these specific A3 machine types, you must select either **Spot** or **Flex-start**. For A2 machine types, you can select any of the provisioning models. In the **Advanced options** section, under **VM provisioning model** , select one of the following: 
     * **Standard** : for general-purpose workloads.
     * **Flex-start** : for short-duration workloads that can tolerate a flexible start time. For more information, see [About Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms).
     * **Spot** : for fault-tolerant workloads that can be preempted. For more information, see [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).
  7. Optional: In the **On VM termination** list, select what happens when Compute Engine preempts the Spot VMs or the Flex-start VMs reaches the end of its run duration: 
     * To stop the VM during preemption, select **Stop** (default).
     * To delete the VM during preemption, select **Delete**.
  8. To create and start the VM, click **Create**.



###  gcloud 

To create and start a VM, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the following flags. Because VMs with GPUs can't live migrate, set the `--maintenance-policy` flag to `TERMINATE`.

The sample command also shows the `--provisioning-model` flag. This flag sets the provisioning model for the VM. This flag is required when creating A3 machine types with fewer than 8 GPUs and must be set to either `SPOT` or `FLEX_START`. For A2 machine types, this flag is optional. If you don't specify a model, then\ Compute Engine uses the standard provisioning model. For more information, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).
    
    
      gcloud compute instances create VM_NAME \
          --machine-type=MACHINE_TYPE \
          --zone=ZONE \
          --boot-disk-size=DISK_SIZE \
          --image=IMAGE \
          --image-project=IMAGE_PROJECT \
          --maintenance-policy=TERMINATE \
          --provisioning-model=PROVISIONING_MODEL
      

Replace the following:

  * `VM_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new VM.
  * `MACHINE_TYPE`: an [A2 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms) or an [A3 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms) with 1, 2, or 4 GPUs. For A3 machine types, you must specify a provisioning model.
  * `ZONE`: the zone for the VM. This zone must support [your selected GPU model](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  * `DISK_SIZE`: the size of your boot disk in GiB. Specify a boot disk size of at least 40 GiB.
  * `IMAGE`: an operating system image [ that supports GPUs](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). To use the latest image in an [image family](https://docs.cloud.google.com/compute/docs/images#image_families), replace the `--image` flag with the `--image-family` flag and set its value to an image family that supports GPUs. For example: `--image-family=rocky-linux-8-optimized-gcp`.  
You can also specify a custom image or [ Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images).
  * `IMAGE_PROJECT`: the Compute Engine [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that the OS image belongs to. If using a custom image or Deep Learning VM Images, specify the project that those images belong to.
  * `PROVISIONING_MODEL`: the provisioning model to use to create the VM. You can specify either `SPOT` or `FLEX_START`. If you remove the `--provisioning-model` flag from the command, then Compute Engine uses the standard provisioning model. This flag is required when creating A3 VMs with fewer than 8 GPUs. For required flags for the spot or flex-start provisioning models, see [Create a Spot VM](https://docs.cloud.google.com/compute/docs/instances/create-use-spot) or [Create a Flex-start VM](https://docs.cloud.google.com/compute/docs/instances/create-flex-start-vm).



###  REST 

Send a POST request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). Because VMs with GPUs can't live migrate, set the `onHostMaintenance` field to `TERMINATE`.

The sample request includes the `provisioningModel` field in the request body. This field sets the provisioning model for the VM. This field is required when creating A3 machine types with fewer than 8 GPUs and must be set to either `SPOT` or `FLEX_START`. For A2 machine types, this field is optional. If you don't specify a provisioning model, then Compute Engine uses the standard provisioning model. For more information, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "machineType": "projects/PROJECT_ID/zones/ZONE/machineTypes/MACHINE_TYPE",
      "disks":
      [
        {
          "type": "PERSISTENT",
          "initializeParams": {
            "diskSizeGb": "DISK_SIZE",
            "sourceImage": "SOURCE_IMAGE_URI"
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
      "scheduling": {
        "automaticRestart": true,
        "onHostMaintenance": "TERMINATE",
        "provisioningModel": "PROVISIONING_MODEL"
      }
    }
    

Replace the following: 

  * `VM_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new VM.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: the zone for the VM. The zone must support [your selected GPU model](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  * `MACHINE_TYPE`: an [A2 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms) or an [A3 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms) with 1, 2, or 4 GPUs. For A3 machine types, you must specify a provisioning model.
  * `SOURCE_IMAGE_URI`: the URI for the specific [image or image family](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support) that you want to use. For example: 
    * Specific image: `"sourceImage": "projects/rocky-linux-cloud/global/images/rocky-linux-10-optimized-gcp-v20251017"`
    * Image family: `"sourceImage": "projects/rocky-linux-cloud/global/images/family/rocky-linux-10-optimized-gcp"`
When you specify an image family, Compute Engine creates a VM from the most recent, non-deprecated OS image in that family. For more information about when to use image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).
  * `DISK_SIZE`: the size of your boot disk in GB. Specify a boot disk size of at least 40 GB.
  * `NETWORK`: the VPC network that you want to use for the VM. You can specify `default` to use your default network.
  * `PROVISIONING_MODEL`: the provisioning model to use to create the VM. You can specify either `SPOT` or `FLEX_START`. If you remove the `provisioningModel` field from the request body, then Compute Engine uses the standard provisioning model. This field is required when creating A3 VMs with fewer than 8 GPUs. For required fields for the spot or flex-start provisioning model, see [Create a Spot VM](https://docs.cloud.google.com/compute/docs/instances/create-use-spot) or [Create a Flex-start VM](https://docs.cloud.google.com/compute/docs/instances/create-flex-start-vm).



## Install drivers

For the VM to use the GPU, you need to [Install the GPU driver on your VM](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu).

## Examples

In these examples, most of the VMs are created by using the Google Cloud CLI. However, you can also use either the [Google Cloud console](https://console.cloud.google.com/) or [REST](https://docs.cloud.google.com/compute/docs/reference/latest/instances) to create these VMs.

The following examples show how to create an A3 Spot VM by using a standard OS image, and an A2 VM by using a [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images) image.

### Create an A3 Spot VM by using the Debian 13 OS image family

This example creates an A3 (`a3-highgpu-1g`) Spot VM by using the Debian 13 OS image family.
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=a3-highgpu-1g \
        --provisioning-model=SPOT \
        --maintenance-policy=TERMINATE \
        --image-family=debian-13 \
        --image-project=debian-cloud \
        --boot-disk-size=200GB \
        --scopes=https://www.googleapis.com/auth/cloud-platform
    

Replace the following:

  * `VM_NAME`: the name of your VM instance
  * `PROJECT_ID` : your project ID
  * `ZONE`: the zone for the VM instance



### Create an A2 VM with a Vertex AI Workbench user-managed notebooks instance on the VM

This example creates an A2 Standard (`a2-highgpu-1g`) VM by using the `tf2-ent-2-3-cu110` [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images) image. In this example, optional flags such as boot disk size and scope are specified.

Using DLVM images is the easiest way to get started because these images already have the NVIDIA drivers and CUDA libraries pre-installed.

These images also provide performance optimizations.

The following DLVM images are supported for NVIDIA A100:

  * `common-cu110`: NVIDIA driver and CUDA pre-installed
  * `tf-ent-1-15-cu110`: NVIDIA driver, CUDA, TensorFlow Enterprise 1.15.3 pre-installed
  * `tf2-ent-2-1-cu110`: NVIDIA driver, CUDA, TensorFlow Enterprise 2.1.1 pre-installed
  * `tf2-ent-2-3-cu110`: NVIDIA driver, CUDA, TensorFlow Enterprise 2.3.1 pre-installed
  * `pytorch-1-6-cu110`: NVIDIA driver, CUDA, Pytorch 1.6



For more information about the DLVM images that are available, and the packages installed on the images, see the [Deep Learning VM documentation](https://docs.cloud.google.com/deep-learning-vm/docs/images).
    
    
    gcloud compute instances create VM_NAME \
        --project=PROJECT_ID \
        --zone=ZONE \
        --machine-type=a2-highgpu-1g \
        --maintenance-policy=TERMINATE \
        --image-family=tf2-ent-2-3-cu110 \
        --image-project=deeplearning-platform-release \
        --boot-disk-size=200GB \
        --metadata="install-nvidia-driver=True,proxy-mode=project_editors" \
        --scopes=https://www.googleapis.com/auth/cloud-platform
    

Replace the following:

  * `VM_NAME`: the name of your VM instance
  * `PROJECT_ID` : your project ID
  * `ZONE`: the zone for the VM instance



The preceding example command also generates a [Vertex AI Workbench user-managed notebooks instance](https://docs.cloud.google.com/vertex-ai/docs/workbench/user-managed/introduction) for the VM. To access the notebook, in the Google Cloud console, go to the **Vertex AI Workbench** > **User-managed notebooks** page.

[Go to the User-managed notebooks page](https://console.cloud.google.com/vertex-ai/workbench/list/instances)

## Multi-Instance GPU

A [Multi-Instance GPU](https://www.nvidia.com/en-us/technologies/multi-instance-gpu/) partitions a single NVIDIA A100 or NVIDIA H100 GPU within the same VM into as many as seven independent GPU instances. They run simultaneously, each with its own memory, cache and streaming multiprocessors. This setup enables the NVIDIA A100 and H100 GPU to deliver consistent quality-of-service (QoS) at up to 7x higher utilization compared to earlier GPU models.

You can create up to seven Multi-instance GPUs. For A100 40GB GPUs, each Multi-instance GPU is allocated 5 GB of memory. With the A100 80GB GPUs the allocated memory doubles to 10 GB each. With H100 80GB GPUs, each Multi-instance GPU is also allocated 10 GB of memory.

For more information about using Multi-Instance GPUs, see [NVIDIA Multi-Instance GPU User Guide](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/).

To create Multi-Instance GPUs, complete the following steps:

  1. Create an A2 (A100) or A3 (H100) accelerator-optimized VM instance.

  2. Connect to the VM instance. For more information, see [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) or [Connect to Windows VMs](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows).

  3. Enable [NVIDIA GPU drivers](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu).

**Note:** If you use a [Deep Learning VM Images image](https://docs.cloud.google.com/deep-learning-vm/docs/images), then you can skip this step. Drivers are pre-installed on the image.

  4. Enable Multi-Instance GPUs.
         
         sudo nvidia-smi -mig 1
         

  5. Review the Multi-Instance GPU shapes that are available.
         
         sudo nvidia-smi mig --list-gpu-instance-profiles
         

The output is similar to the following:
         
         +-----------------------------------------------------------------------------+
         | GPU instance profiles:                                                      |
         | GPU   Name             ID    Instances   Memory     P2P    SM    DEC   ENC  |
         |                              Free/Total   GiB              CE    JPEG  OFA  |
         |=============================================================================|
         |   0  MIG 1g.10gb       19     7/7        9.62       No     16     1     0   |
         |                                                             1     1     0   |
         +-----------------------------------------------------------------------------+
         |   0  MIG 1g.10gb+me    20     1/1        9.62       No     16     1     0   |
         |                                                             1     1     1   |
         +-----------------------------------------------------------------------------+
         |   0  MIG 1g.20gb       15     4/4        19.50      No     26     1     0   |
         |                                                             1     1     0   |
         +-----------------------------------------------------------------------------+
         |   0  MIG 2g.20gb       14     3/3        19.50      No     32     2     0   |
         |                                                             2     2     0   |
         +-----------------------------------------------------------------------------+
         |   0  MIG 3g.40gb        9     2/2        39.25      No     60     3     0   |
         |                                                             3     3     0   |
         +-----------------------------------------------------------------------------+
         .......
         

  6. Create the Multi-Instance GPU (GI) and associated compute instances (CI) that you want. You can create these instances by specifying either the full or shortened profile name, profile ID, or a combination of both. For more information, see [Creating GPU Instances](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#create-gi).

The following example creates two `MIG 3g.20gb` GPU instances by using the profile ID (`9`).

The `-C` flag is also specified which creates the associated compute instances for the required profile.
         
         sudo nvidia-smi mig -cgi 9,9 -C
         

  7. Check that the two Multi-Instance GPUs are created:
         
         sudo nvidia-smi mig -lgi
         

  8. Check that both the GIs and corresponding CIs are created.
         
         sudo nvidia-smi
         

The output is similar to the following:
         
         +-----------------------------------------------------------------------------+
         | NVIDIA-SMI 525.125.06   Driver Version: 525.125.06   CUDA Version: 12.0     |
         |-------------------------------+----------------------+----------------------+
         | GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
         | Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
         |                               |                      |               MIG M. |
         |===============================+======================+======================|
         |   0  NVIDIA H100 80G...  Off  | 00000000:04:00.0 Off |                   On |
         | N/A   33C    P0    70W / 700W |     39MiB / 81559MiB |     N/A      Default |
         |                               |                      |              Enabled |
         +-------------------------------+----------------------+----------------------+
         |   1  NVIDIA H100 80G...  Off  | 00000000:05:00.0 Off |                   On |
         | N/A   32C    P0    69W / 700W |     39MiB / 81559MiB |     N/A      Default |
         |                               |                      |              Enabled |
         +-------------------------------+----------------------+----------------------+
         ......
         
         +-----------------------------------------------------------------------------+
         | MIG devices:                                                                |
         +------------------+----------------------+-----------+-----------------------+
         | GPU  GI  CI  MIG |         Memory-Usage |        Vol|         Shared        |
         |      ID  ID  Dev |           BAR1-Usage | SM     Unc| CE  ENC  DEC  OFA  JPG|
         |                  |                      |        ECC|                       |
         |==================+======================+===========+=======================|
         |  0    1   0   0  |     19MiB / 40192MiB | 60      0 |  3   0    3    0    3 |
         |                  |      0MiB / 65535MiB |           |                       |
         +------------------+----------------------+-----------+-----------------------+
         |  0    2   0   1  |     19MiB / 40192MiB | 60      0 |  3   0    3    0    3 |
         |                  |      0MiB / 65535MiB |           |                       |
         +------------------+----------------------+-----------+-----------------------+
         ......
         
         +-----------------------------------------------------------------------------+
         | Processes:                                                                  |
         |  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
         |        ID   ID                                                   Usage      |
         |=============================================================================|
         |  No running processes found                                                 |
         +-----------------------------------------------------------------------------+
         




## What's next?

  * Learn more about [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).
  * For A2 VMs, [add a Local SSD to your VM](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd). Local SSD devices pair well with GPUs when your apps require high-performance storage. A3 VMs have Local SSD attached by default.
  * To handle GPU host maintenance, see [Handling GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
