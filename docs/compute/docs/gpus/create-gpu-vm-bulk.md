---
url: https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-bulk/
title: Create GPU VMs in bulk \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:21.466223+00:00
---

# Create GPU VMs in bulk  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-bulk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create GPU VMs in bulk Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

You can create a group of virtual machines (VMs) that [have attached graphical processing units (GPUs)](https://docs.cloud.google.com/compute/docs/gpus/about-gpus) by using the bulk creation process. With the bulk creation process, you get upfront validation where the request fails fast if it is not feasible. Also, if you use the region flag, the bulk creation API automatically chooses the zone that has the capacity to fulfill the request. 

To learn more about bulk creation, see [About bulk creation of VMs](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation). To learn more about creating VMs with attached GPUs, see [Overview of creating an instance with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).

## Before you begin

  * To review limitations and additional prerequisite steps for creating instances with attached GPUs, such as selecting an OS image and checking GPU quota, see [Overview of creating an instance with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus). 
  * To review limitations for bulk creation, see [About bulk creation of VMs](https://docs.cloud.google.com/compute/docs/instances/multiple/about-bulk-creation#limitations). 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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

When creating VMs with attached GPUs using the bulk creation method, you can choose to create VMs in a region (such as `us-central1`) or in a specific zone such as (`us-central1-a`).

If you choose to specify a region, Compute Engine places the VMs in any zone within the region that supports GPUs.

## Machine types

You can create GPU VMs in bulk by using either accelerator-optimized or N1 general-purpose machine types.

Compute Engine offers different machine types to support your various workloads.

Some machine types support [NVIDIA RTX Virtual Workstations (vWS)](https://www.nvidia.com/en-us/design-visualization/virtual-workstation/). When you create an instance that uses NVIDIA RTX Virtual Workstation, Compute Engine automatically adds a vWS license. For information about pricing for virtual workstations, see the [GPU pricing page](https://cloud.google.com/compute/gpus-pricing).

**GPU machine types**  
---  
AI and ML workloads | Graphics and visualization | Other GPU workloads  
**Accelerator-optimized A series machine types** are designed for high performance computing (HPC), artificial intelligence (AI), and machine learning (ML) workloads. The later generation A series are ideal for pre-training and fine-tuning foundation models that involves large clusters of accelerators, while the A2 series can be used for training smaller models and single host inference. For these machine types, the GPU model is automatically attached to the instance. |  **Accelerator-optimized G series machine types** are designed for workloads such as NVIDIA Omniverse simulation workloads, graphics-intensive applications, video transcoding, and virtual desktops. These machine types support [NVIDIA RTX Virtual Workstations (vWS)](https://www.nvidia.com/en-us/design-visualization/virtual-workstation/). The G series can also be used for training smaller models and for single-host inference. For these machine types, the GPU model is automatically attached to the instance. |  For N1 general-purpose machine types, except for the N1 shared-core (`f1-micro` and `g1-small`), you can attach a select set of GPU models. Some of these GPU models also support NVIDIA RTX Virtual Workstations (vWS).  
  
  * [A4X Max](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) (NVIDIA GB300 Ultra Superchips)   
(`nvidia-gb300`)
  * [A4X](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms) (NVIDIA GB200 Superchips)   
(`nvidia-gb200`)
  * [A4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4-vms) (NVIDIA B200)   
(`nvidia-b200`)
  * [A3 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-ultra-vms) (NVIDIA H200)   
(`nvidia-h200-141gb`)
  * [A3 Mega](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms) (NVIDIA H100)   
(`nvidia-h100-mega-80gb`)
  * [A3 High](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms) (NVIDIA H100)   
(`nvidia-h100-80gb`)
  * [A3 Edge](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms) (NVIDIA H100)   
(`nvidia-h100-80gb`)
  * [A2 Ultra](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms) (NVIDIA A100 80GB)   
(`nvidia-a100-80gb`)
  * [A2 Standard](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-standard-vms) (NVIDIA A100 4OGB)   
(`nvidia-tesla-a100`)

| 

  * [G4](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-series) (NVIDIA RTX PRO 6000)   
(`nvidia-rtx-pro-6000`)   
(`nvidia-rtx-pro-6000-vws`)
  * [G2](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-vms) (NVIDIA L4)   
(`nvidia-l4`)   
(`nvidia-l4-vws`)

| The following GPU models can be attached to N1 general-purpose machine types: 

  * NVIDIA T4   
(`nvidia-tesla-t4`)   
(`nvidia-tesla-t4-vws`). NVIDIA T4 is approaching end of support, see [NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos).
  * NVIDIA P4   
(`nvidia-tesla-p4`)   
(`nvidia-tesla-p4-vws`). NVIDIA P4 is approaching end of support, see [NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos).
  * NVIDIA V100   
(`nvidia-tesla-v100`)

  
  
## Create groups of A4X, A4, and A3 Ultra

To create instances in bulk for the A4X, A4, and A3 Ultra machine series, see the [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview) in the AI Hypercomputer documentation.

## Create groups of A3, A2, G4, and G2 VMs

This section explains you can create instances in bulk for the A3 High, A3 Mega, A3 Edge, A2 Standard, A2 Ultra, G4, and G2 machine series by using [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1).

###  gcloud 

To create a group of VMs, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create). For more information about the parameters and how to use this command, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

**Note:** The following example outlines the required flags. For a list of optional flags that you can include, see the optional flags section. Depending on your workload requirement or if you need to use a Windows operating system, you might need to include one or more of these optional flags. 

**Example**

This example creates two VMs that have attached GPUs by using the following specifications:

  * VM names: `my-test-vm-1`, `my-test-vm-2`
  * Each VM has two GPUs attached, specified by using the appropriate [accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines)


    
    
    gcloud compute instances bulk create \
        --name-pattern="my-test-vm-#" \
        --region=REGION \
        --count=2 \
        --machine-type=MACHINE_TYPE \
        --boot-disk-size=200 \
        --image=IMAGE \
        --image-project=IMAGE_PROJECT \
        --on-host-maintenance=TERMINATE
    

Replace the following:

  * `REGION`: the region for the VMs. This region must support [your selected accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  * `MACHINE_TYPE`: the machine type that you selected. Choose from one of the following:

    * An [A3 High machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms)
    * An [A3 Mega machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms)
    * An [A3 Edge machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms)
    * An [A2 Standard machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms)
    * An [A2 Ultra machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms)
    * A [G4 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-machine-types)
    * A [G2 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-standard-vms) G2 machine types also support custom memory. Memory must be a multiple of 1024 MB and within the supported memory range. For example, to create a VM with 4 vCPUs and 19 GB of memory specify `--machine-type=g2-custom-4-19456`.
  * `IMAGE`: an operating system image [that supports GPUs](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support).

If you want to use the latest image in an [image family](https://docs.cloud.google.com/compute/docs/images#image_families), replace the `--image` flag with the `--image-family` flag and set its value to an image family that supports GPUs. For example: `--image-family=rocky-linux-8-optimized-gcp`.

You can also specify a custom image or [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images).

  * `IMAGE_PROJECT`: the Compute Engine [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that the OS image belongs to. If using a custom image or Deep Learning VM Images, specify the project that those images belong to.

  * `VWS_ACCELERATOR_COUNT`: the number of virtual GPUs that you need.




If successful, the output is similar to the following:
    
    
    NAME          ZONE
    my-test-vm-1  us-central1-b
    my-test-vm-2  us-central1-b
    Bulk create request finished with status message: [VM instances created: 2, failed: 0.]
    

### Optional flags

To further configure your instance to meet your workload or operating system needs, include one or more of the following flags when you run the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create). 

Feature | Description  
---|---  
Provisioning model | Sets the provisioning model for the instance. You can specify either `STANDARD` or `SPOT`. If you don't specify a provisioning model, then Compute Engine sets the value to `STANDARD`. For more information, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models). 
    
    
    --provisioning-model=PROVISIONING_MODEL  
  
Virtual workstation | Specifies [NVIDIA RTX Virtual Workstations (vWs) for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations). This feature is supported only for G4 and G2 instances. 
    
    
    --accelerator=type=VWS_ACCELERATOR_TYPE,count=VWS_ACCELERATOR_COUNT

Replace the following:

  * For `VWS_ACCELERATOR_TYPE`, choose from one of the following:
    * For G4 instances, specify `nvidia-rtx-pro-6000-vws`
    * For G2 instances, specify `nvidia-l4-vws`
  * For `VWS_ACCELERATOR_COUNT`, specify the number of virtual GPUs that you need.

  
Local SSD | Attaches one or more Local SSDs to your instance. Local SSDs can be used for fast scratch disks or for feeding data into the GPUs while preventing I/O bottlenecks. 
    
    
        --local-ssd=interface=nvme \
        --local-ssd=interface=nvme \
        --local-ssd=interface=nvme ...

For the maximum number of Local SSD disks that you can attach per VM instance, see [Local SSD limits](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options).   
Network interface | Attaches multiple network interfaces to your instance. For `g4-standard-384` instances, you can attach up to two network interfaces. You can use this flag to create an instance with dual network interfaces (2x 200 Gbps). Each network interface must be in a unique VPC network. 
    
    
       --network-interface=network=VPC_NAME_1,subnet=SUBNET_NAME_1,nic-type=GVNIC \
       --network-interface=network=VPC_NAME_2,subnet=SUBNET_NAME_2,nic-type=GVNIC
       

Dual network interfaces are only supported on `g4-standard-384` machine types. Replace the following:

  * `VPC_NAME`: the name of your [VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).
  * `SUBNET_NAME`: the name of the subnet that is part of the specified VPC network.

  
Placement policy | Controls the placement of your instance within a zone. You can specify a [compact policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) to minimize network latency across your G2 instances, or a [spread policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-spread-policies) to improve your G4 or G2 instances' resilience against zone-specific disruptions. 
    
    
       --resource-policies=POLICY_NAME
       

Replace `POLICY_NAME` with the name of your placement policy. You can only create the instance in the same region as the policy.  
  
###  REST 

Use the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert) with the required parameters to create multiple VMs in a zone. For more information about the parameters and how to use this command, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

**Note:** The following example outlines the required flags. For a list of optional flags that you can include, see the optional flags section. Depending on your workload requirement or if you need to use a Windows operating system, you might need to include one or more of these optional flags. 

**Example**

This example creates two VMs that have attached GPUs by using the following specifications:

  * VM names: `my-test-vm-1`, `my-test-vm-2`
  * Each VM has two GPUs attached, specified by using the appropriate [accelerator-optimized machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines)
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instances/bulkInsert
        {
        "namePattern":"my-test-vm-#",
        "count":"2",
        "instanceProperties": {
          "machineType":MACHINE_TYPE,
          "disks":[
            {
              "type":"PERSISTENT",
              "initializeParams":{
                "diskSizeGb":"200",
                "sourceImage":SOURCE_IMAGE_URI
              },
              "boot":true
            }
          ],
          "name": "default",
          "networkInterfaces":
          [
            {
              "network": "projects/PROJECT_ID/global/networks/default"
            }
          ],
          "scheduling":{
            "onHostMaintenance":"TERMINATE",
            ["automaticRestart":true]
          }
        }
        }
        




Replace the following:

  * `PROJECT_ID`: your project ID
  * `REGION`: the region for the VMs. This region must support [your selected GPU model](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  * `MACHINE_TYPE`: the machine type that you selected. Choose from one of the following:

    * An [A3 High machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-high-vms)
    * An [A3 Mega machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-mega-vms)
    * An [A3 Edge machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-edge-vms)
    * An [A2 Standard machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms)
    * An [A2 Ultra machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms)
    * A [G4 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-machine-types)
    * A [G2 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-standard-vms). G2 machine types also support custom memory. Memory must be a multiple of 1024 MB and within the supported memory range. For example, the machine type name for an instance with 4 vCPUs and 19 GB of memory would be `g2-custom-4-19456`.
  * `SOURCE_IMAGE_URI`: the URI for the specific [image or image family](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support) that you want to use.

For example:

    * Specific image: `"sourceImage": "projects/rocky-linux-cloud/global/images/rocky-linux-8-optimized-gcp-v20220719"`
    * Image family: `"sourceImage": "projects/rocky-linux-cloud/global/images/family/rocky-linux-8-optimized-gcp"`.

When you specify an image family, Compute Engine creates a VM from the most recent, non-deprecated OS image in that family. For more information about when to use image families, see [Image family best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




### Optional fields

To further configure your instance to meet your workload or operating system needs, include one or more of the following flags when you run the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert). 

Feature | Description  
---|---  
Provisioning model |  To lower your costs, you can specify a different provisioning model by adding the `"provisioningModel": "PROVISIONING_MODEL"` field to the `scheduling` object in your request. For more information, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models). 
    
    
        "scheduling":
         {
           "onHostMaintenance": "TERMINATE",
           "provisioningModel": "PROVISIONING_MODEL"
         }
      

Replace `PROVISIONING_MODEL` with one of the following:

  * `STANDARD`: A standard instance. This is the default value.
  * `SPOT`: A Spot VM. If you create a Spot VM, then the `onHostMaintenance` and `automaticRestart` fields are overridden. Spot VMs are deeply discounted, but Compute Engine can preempt them at any time to reclaim capacity.

  
Virtual workstation | Specifies [NVIDIA RTX Virtual Workstations (vWS) for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations). This feature is supported only for G4 and G2 instances. 
    
    
       "guestAccelerators":
         [
           {
             "acceleratorCount": VWS_ACCELERATOR_COUNT,
             "acceleratorType": "projects/PROJECT_ID/zones/ZONE/acceleratorTypes/VWS_ACCELERATOR_TYPE"
           }
         ]
        

Replace the following:

  * For `VWS_ACCELERATOR_TYPE`, choose from one of the following:
    * For G4 instances, specify `nvidia-rtx-pro-6000-vws`
    * For G2 instances, specify `nvidia-l4-vws`
  * For `VWS_ACCELERATOR_COUNT`, specify the number of virtual GPUs that you need.

  
Local SSD | Attaches one or more Local SSDs to your instance. Local SSDs can be used for fast scratch disks or for feeding data into the GPUs while preventing I/O bottlenecks. 
    
    
       {
         "type": "SCRATCH",
         "autoDelete": true,
         "initializeParams": {
           "diskType": "projects/PROJECT_ID/zones/ZONE/diskTypes/local-nvme-ssd"
         }
       }
      

For the maximum number of Local SSD disks that you can attach per VM instance, see [Local SSD limits](https://docs.cloud.google.com/compute/docs/disks/local-ssd#lssd_disk_options).   
Network interface | Attaches multiple network interfaces to your instance. For `g4-standard-384` instances, you can attach up to two network interfaces. This creates an instance with dual network interfaces (2x 200 Gbps). Each network interface must be in a unique VPC network. 
    
    
       "networkInterfaces":
       [
         {
           "network": "projects/PROJECT_ID/global/networks/VPC_NAME_1",
           "subnetwork": "projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME_1",
           "nicType": "GVNIC"
         },
         {
           "network": "projects/PROJECT_ID/global/networks/VPC_NAME_2",
           "subnetwork": "projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME_2",
           "nicType": "GVNIC"
         }
       ]
      

Dual network interfaces are only supported on `g4-standard-384` machine types. Replace the following:

  * `VPC_NAME_1` and `VPC_NAME_2`: the name of your [VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).
  * `SUBNET_NAME`: the name of the subnet that is part of the specified VPC networks.

  
Placement policy | Controls the placement of your instance within a zone. You can specify a [compact policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) to minimize network latency across your G2 instances, or a [spread policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-spread-policies) to improve your G4 or G2 instances' resilience against zone-specific disruptions. 
    
    
       "resourcePolicies": [
         "projects/PROJECT_ID/regions/REGION/resourcePolicies/POLICY_NAME"
       ]
       

Replace the following:

  * `REGION`: the region where your placement policy exists. You can only create the instance in the same region as the policy.
  * `POLICY_NAME`: the name of your placement policy.

  
  
## Create groups of N1-general purpose VMs

You create a group of VMs with attached GPUs by using either the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1).

This section describes how to create multiple VMs using the following GPU types:

**Caution:** NVIDIA T4 and P4 GPUs reach end of support on August 1, 2027. For more information, see [NVIDIA T4 end of support](https://docs.cloud.google.com/compute/docs/eol/t4-eos) and [NVIDIA P4 end of support](https://docs.cloud.google.com/compute/docs/eol/p4-eos).  NVIDIA GPUs: 

  * NVIDIA T4: `nvidia-tesla-t4`
  * NVIDIA P4: `nvidia-tesla-p4`
  * NVIDIA V100: `nvidia-tesla-v100`



NVIDIA RTX Virtual Workstation (vWS) (formerly known as NVIDIA GRID):

  * NVIDIA T4 Virtual Workstation: `nvidia-tesla-t4-vws`
  * NVIDIA P4 Virtual Workstation: `nvidia-tesla-p4-vws`

For these virtual workstations, an NVIDIA RTX Virtual Workstation (vWS) license is automatically added to your instance.




###  gcloud 

To create a group of VMs, use the [`gcloud compute instances bulk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/bulk/create). For more information about the parameters and how to use this command, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

**Example**

The following example creates two VMs with attached GPUs using the following specifications:

  * VM names: `my-test-vm-1`, `my-test-vm-2`
  * VMs created in any zone in `us-central1` that supports GPUs
  * Each VM has two T4 GPUs attached, specified by using the accelerator type and accelerator count flags
  * Each VM has GPU drivers installed
  * Each VM uses the Deep Learning VM image `pytorch-latest-gpu-v20211028-debian-10`


    
    
    gcloud compute instances bulk create \
        --name-pattern="my-test-vm-#" \
        --count=2 \
        --region=us-central1 \
        --machine-type=n1-standard-2 \
        --accelerator type=nvidia-tesla-t4,count=2 \
        --boot-disk-size=200 \
        --metadata="install-nvidia-driver=True" \
        --scopes="https://www.googleapis.com/auth/cloud-platform" \
        --image=pytorch-latest-gpu-v20211028-debian-10 \
        --image-project=deeplearning-platform-release \
        --on-host-maintenance=TERMINATE --restart-on-failure
    

If successful, the output is similar to the following:
    
    
    NAME          ZONE
    my-test-vm-1  us-central1-b
    my-test-vm-2  us-central1-b
    Bulk create request finished with status message: [VM instances created: 2, failed: 0.]
    

###  REST 

Use the [`instances.bulkInsert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/bulkInsert) with the required parameters to create multiple VMs in a zone. For more information about the parameters and how to use this command, see [Create VMs in bulk](https://docs.cloud.google.com/compute/docs/instances/multiple/create-in-bulk).

**Example**

The following example creates two VMs with attached GPUs using the following specifications:

  * VM names: `my-test-vm-1`, `my-test-vm-2`
  * VMs created in any zone in `us-central1` that supports GPUs
  * Each VM has two T4 GPUs attached, specified by using the accelerator type and accelerator count flags
  * Each VM has GPU drivers installed
  * Each VM uses the Deep Learning VM image `pytorch-latest-gpu-v20211028-debian-10`



Replace `PROJECT_ID` with your project ID.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-central1/instances/bulkInsert
    
    {
        "namePattern":"my-test-vm-#",
        "count":"2",
        "instanceProperties": {
          "machineType":"n1-standard-2",
          "disks":[
            {
              "type":"PERSISTENT",
              "initializeParams":{
                "diskSizeGb":"200",
                "sourceImage":"projects/deeplearning-platform-release/global/images/pytorch-latest-gpu-v20211028-debian-10"
              },
              "boot":true
            }
          ],
          "name": "default",
          "networkInterfaces":
          [
            {
              "network": "projects/PROJECT_ID/global/networks/default"
            }
          ],
          "guestAccelerators":
          [
            {
              "acceleratorCount": 2,
              "acceleratorType": "nvidia-tesla-t4"
            }
          ],
          "scheduling":{
            "onHostMaintenance":"TERMINATE",
            "automaticRestart":true
          },
          "metadata":{
            "items":[
              {
                "key":"install-nvidia-driver",
                "value":"True"
              }
            ]
          }
      }
     }
    

## What's next?

  * Learn how to [monitor GPU performance](https://docs.cloud.google.com/compute/docs/gpus/monitor-gpus).

  * Learn how to [use higher network bandwidth](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus).

  * Learn how to [handle GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).



  * Learn how to [view the actual and forecasted usage of your VMs and GPUs](https://docs.cloud.google.com/capacity-planner/docs/view-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
