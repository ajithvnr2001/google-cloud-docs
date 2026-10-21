---
url: https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-g-series/
title: Create a G2 or G4 instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:55.852630+00:00
---

# Create a G2 or G4 instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-g-series/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a G2 or G4 instance Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document explains how to create a virtual machine (VM) instance that uses a machine type from the G2 or G4 machine series. These G series [accelerator-optimized machine types](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines) are a good fit for running graphics-intensive applications and cost-effective machine learning (ML) inference.

You can create these VMs as on-demand VMs. To lower your costs, you can also create G2 and G4 Spot VMs, or you can create G2 Flex-start VMs. To learn more about creating VMs with attached GPUs, see [Overview of creating an instance with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).

For workloads that don't require the resources of a full GPU, to optimize costs, you can create VMs that have fractional GPUs (vGPUs) attached to let multiple workloads access a single physical GPU.

To create multiple G2 or G4 VMs, you can use one of the following:

  * **Managed instance groups (MIGs)** : for workloads that require high availability, scalability, and automated repairs, you can [create a MIG that uses a GPU instance template](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms).
  * **Bulk instance creation** : to create a large number of independent instances, you can [create G2 and G4 VMs in bulk](https://docs.cloud.google.com/compute/docs/gpus/create-gpu-vm-bulk).



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

## Create an instance that has attached GPUs

You can create a G2 or G4 accelerator-optimized instance by using the Google Cloud console, Google Cloud CLI, or REST.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Name** field, enter a unique name for your instance. See [Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format).

  3. Select a region and zone where these GPU machine types are available. See [GPU regions and zones](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).

  4. In the machine types section, select **GPUs**.

     1. In the **GPU type** list, select the GPU type.

        * For G2 instances, select `NVIDIA L4`
        * For G4 instances, select `NVIDIA RTX PRO 6000`
     2. In the **Number of GPUs** list, select the number of GPUs.

        * For G4 instances, the console automatically selects the corresponding machine type based on the number of GPUs selected.
        * For G2 instances, review the following:

          * If you select one GPU, you can then choose from a set of machine type with preset amounts of vCPUs and memory that suit your workloads.
          * If you select two or more GPUs, the console automatically selects the corresponding machine type based on the number of GPUs selected.

For G2 instances, you can also specify custom machine types. To specify the number of vCPUs and the amount of memory for the instance, drag the sliders or enter the values in the text boxes. The console displays an estimated cost for the instance as you change the number of vCPUs and memory.

     3. _Optional_ : The G2 and G4 machine series support [NVIDIA RTX Virtual Workstations (vWS) for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations). If you plan on running graphics-intensive workloads on your instance, select **Enable Virtual Workstation (NVIDIA GRID)**.

  5. Configure the boot disk as follows:

     1. In the **OS and storage** section, click **Change**. This opens the **Boot disk configuration** page.
     2. On the **Boot disk configuration** page, do the following:

        1. On the **Public images** tab, choose a [supported Compute Engine image](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support) or [Deep Learning VM Images](https://docs.cloud.google.com/ai-platform/deep-learning-vm/docs/images).
        2. Specify a boot disk size of at least 40 GiB.
        3. To confirm your boot disk options, click **Select**.
  6. _Optional_ : Add Local SSDs. Local SSDs can be used for fast scratch disks or for feeding data into the GPUs while preventing I/O bottlenecks. To add Local SSDs to your instance, complete the following:

     1. In the **OS and storage** section, click **Add local SSD**.
     2. For the **Interface** , select **NVMe**.
     3. In **Disk capacity** , select the number of Local SSDs you want to attach. For the maximum number of Local SSD disks per instance, see the [machine series limits for Local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd#limits).
  7. _Optional_ : To achieve higher network bandwidth for your `g4-standard-384` instances, configure multiple network interfaces. You can configure up to two network interfaces. This configuration creates a `g4-standard-384` instance with dual network interfaces (2x 200 Gbps). In the **Networking** section, complete the following steps:

     1. Expand the default network interface.
     2. Specify the **Network** and **Subnetwork** for your first interface.
     3. For **Network interface card** , select **gVNIC**.
     4. Click **Add network interface** to add the second interface. Configure the second network interface as follows:

        1. Select a different VPC **Network** and **Subnetwork**. Each network interface must be in a unique VPC network.
        2. For **Network interface card** , select **gVNIC**.
  8. _Optional_ : Configure a different provisioning model to lower your costs. In the **Advanced options** section, under **VM provisioning model** , select one of the following:

     * **(G2 only) Flex-start** : for short-duration workloads that can tolerate a flexible start time. For more information, see [About Flex-start VMs](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms).

     * **Spot** : for fault-tolerant workloads that can be preempted. For more information, see [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot).

  9. _Optional_ : In the **On VM termination** list, select what happens when Compute Engine preempts the Spot VMs or the Flex-start VMs reaches the end of its run duration:

     * To stop the VM during preemption, select **Stop** (default).
     * To delete the VM during preemption, select **Delete**.
  10. To create and start the VM, click **Create**.




###  gcloud 

To create and start an instance, use the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). The following command includes the required flags.

**Note:** For a list of optional flags that you can include, see Optional flags. Depending on your workload requirement, you might need to include one or more of these optional flags. 
    
    
      gcloud compute instances create VM_NAME \
          --machine-type=MACHINE_TYPE \
          --zone=ZONE \
          --boot-disk-size=DISK_SIZE \
          --image=IMAGE \
          --image-project=IMAGE_PROJECT \
          --maintenance-policy=TERMINATE \
          --restart-on-failure
    

Replace the following:

  * `VM_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance.
  * `MACHINE_TYPE` : the machine type that you selected. Choose from one of the following:

    * A [G4 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-machine-types).
    * A [G2 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-standard-vms). G2 machine types also support custom memory. Memory must be a multiple of 1024 MB and within the supported memory range. For example, to create an instance with 4 vCPUs and 19 GB of memory, specify `--machine-type=g2-custom-4-19456`.
  * `ZONE`: the zone for the instance. The zone must support [your selected GPU model](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  * `DISK_SIZE`: the size of your boot disk in GiB. Specify a boot disk size of at least 40 GiB.
  * `IMAGE`: an operating system image [ that supports GPUs](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support). To use the latest image in an [image family](https://docs.cloud.google.com/compute/docs/images#image_families), replace the `--image` flag with the `--image-family` flag and set its value to an image family that supports GPUs. For example: `--image-family=rocky-linux-8-optimized-gcp`.  
You can also specify a custom image or [ Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images).
  * `IMAGE_PROJECT`: the Compute Engine [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that the OS image belongs to. If using a custom image or Deep Learning VM Images, specify the project that those images belong to.



### Optional flags

To further configure your instance to meet your workload or operating system needs, include one or more of the following flags when you run the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

Feature | Description  
---|---  
Provisioning model | Sets the provisioning model for the instance. You can specify `STANDARD`, `SPOT`, or `FLEX_START`. If you specify `FLEX_START`, then you must specify [additional flags](https://docs.cloud.google.com/compute/docs/instances/create-flex-start-vm#gcloud_1) in the command to create the instance. If you don't specify a provisioning model, then Compute Engine sets the value to `STANDARD`. For more information, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models). 
    
    
    --provisioning-model=PROVISIONING_MODEL  
  
Virtual workstation | Specifies [NVIDIA RTX Virtual Workstations (vWs) for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations). 
    
    
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

Send a POST request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert). Because instances with GPUs can't live migrate, set the `onHostMaintenance` field to `TERMINATE`. The following method includes the required fields for the request body.

**Note:** For a list of optional flags that you can include, see the Optional flags section. Depending on your workload requirement, you might need to include one or more of these optional flags. 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
       "machineType":"projects/PROJECT_ID/zones/ZONE/machineTypes/MACHINE_TYPE",
       "disks":[
          {
             "type":"projects/PROJECT_ID/zones/ZONE/diskTypes/hyperdisk-balanced",
             "initializeParams":{
                "diskSizeGb":"DISK_SIZE",
                "sourceImage":"SOURCE_IMAGE_URI"
             },
             "boot":true
          }
       ],
       "name":"VM_NAME",
       "networkInterfaces":[
          {
             "network":"projects/PROJECT_ID/global/networks/default"
          }
       ],
       "scheduling":{
          "onHostMaintenance": "TERMINATE",
          "automaticRestart": true
       }
    }
    

Replace the following:

  * `VM_NAME`: the [name](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the new instance.
  * `PROJECT_ID`: the ID of your project.
  * `ZONE`: the zone for the instance. This zone must support [your selected GPU model](https://docs.cloud.google.com/compute/docs/gpus/gpu-regions-zones).
  * `MACHINE_TYPE` : the machine type that you selected. Choose from one of the following: 
    * A [G4 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g4-machine-types).
    * A [G2 machine type](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#g2-standard-vms). G2 machine types also support custom memory. Memory must be a multiple of 1024 MB and within the supported memory range. For example, the machine type name for an instance with 4 vCPUs and 19 GB of memory would be `g2-custom-4-19456`.
  * `SOURCE_IMAGE_URI`: the URI for the specific [image or image family](https://docs.cloud.google.com/compute/docs/images/os-details#gpu-support) that you want to use. For example: 
    * Specific image: `"sourceImage": "projects/rocky-linux-cloud/global/images/rocky-linux-8-optimized-gcp-v20220719"`
    * Image family: `"sourceImage": "projects/rocky-linux-cloud/global/images/family/rocky-linux-8-optimized-gcp"`
When you specify an image family, Compute Engine creates a instance from the most recent, non-deprecated OS image in that family. For more information about when to use image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).
  * `DISK_SIZE`: the size of your boot disk in GiB. Specify a boot disk size of at least 40 GiB.



### Optional fields

To further configure your instance to meet your workload or operating system needs, include one or more of the following flags when you run the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

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
  * `FLEX_START`: A Flex-start VM. Flex-start VMs run for up to seven days and can help you acquire high-demand resources like GPUs at a discounted price. If you create a Flex-start VM, then you must specify additional fields in your request. For more information, see [Create a Flex-start VM](https://docs.cloud.google.com/compute/docs/instances/create-flex-start-vm#rest_1).

  
Virtual workstation | Specifies [NVIDIA RTX Virtual Workstations (vWS) for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations). 
    
    
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

  
  
## Install drivers

After you create your instance, you must install a driver for the instance to be able to use the GPU. The driver that you need to install depends on whether you enabled an [NVIDIA RTX Virtual Workstation (vWS) for graphics workloads](https://docs.cloud.google.com/compute/docs/gpus#gpu-virtual-workstations) when you created the instance.

  * If you didn't enable a virtual workstation, [install the GPU driver on your VM](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu).
  * If you enabled a virtual workstation, [install a driver for the virtual workstation](https://docs.cloud.google.com/compute/docs/gpus/install-grid-drivers).



### Install vGPU drivers for fractional GPUs

For G4 instances that have less than one GPU attached, after you create your instance, you must install a specific vGPU driver on it, which connects to the physical machine's host driver. For instructions, see [install vGPU drivers (fractional VMs)](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#fractional-vms).

## (Optional) Multi-Instance GPU mode (G4 only)

Multi-Instance GPU (MIG) mode is a feature that you can enable on a supported [NVIDIA GPU](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#supported-mig-profiles).

After you create a G4 instance, you can enable Multi-Instance GPU (MIG) mode on a single NVIDIA RTX PRO 6000 GPU that is attached to your machine. With MIG mode enabled, the single GPU is partitioned into as many as seven independent GPU instances. Each instance runs simultaneously, each with its own memory, cache, and streaming multiprocessors. You can then run different workloads on these GPU instances in parallel. This is distinct from using G4 machine types that have fractional GPUs attached, where multiple workloads share access to a single physical GPU through fractional (vGPUs) partitioning.

For more information about using Multi-Instance GPUs, see [Getting Started with MIG](https://docs.nvidia.com/datacenter/tesla/mig-user-guide/index.html#getting-started-with-mig) in the NVIDIA documentation.

## What's next?

  * Learn more about [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus).
  * To handle GPU host maintenance, see [Handling GPU host maintenance events](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
