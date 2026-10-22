---
url: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance-with-gpu/
title: Create a Confidential VM instance with GPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:02.755370+00:00
---

# Create a Confidential VM instance with GPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/create-a-confidential-vm-instance-with-gpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Confidential VM ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs)
  * [ Guides ](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview)



Send feedback 

#  Create a Confidential VM instance with GPU Stay organized with collections  Save and categorize content based on your preferences. 

To use [GPUs](https://docs.cloud.google.com/compute/docs/gpus/about-gpus) with Confidential VM instances, you must create a VM instance using a supported machine type and instance [provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models). After you create the VM instance, you then enable confidential computing mode on the attached GPU.

Confidential VM instances with NVIDIA GPUs are available on the following machine types:

  * **A3 High machine type** : NVIDIA H100 GPUs with Intel TDX. Supports spot and flex-start provisioning models.

  * **G4 machine type** : NVIDIA RTX PRO 6000 with AMD SEV. Supports standard (on-demand), spot, and flex-start provisioning models, and [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

Using NVIDIA RTX Pro 6000 GPUs with Confidential G4 VM instances automatically incurs a license fee for NVIDIA Confidential Computing software and services. For more details, see [Confidential Computing with GPUs pricing](https://docs.cloud.google.com/confidential-computing/confidential-vm/pricing?e=13802955#confidential-computing-with-gpus-pricing).




Before you create a Confidential VM instance with GPU, make sure you have enough GPU quota. For more information, see [Quotas](https://docs.cloud.google.com/confidential-computing/confidential-vm/quotas#gpu-quotas).

## Create a Confidential VM instance with GPU

To create a Confidential VM instance with an attached GPU, use one of the following provisioning models:

  * **Standard (on-demand)** : Create a standard (on-demand) accelerator-optimized VM instance. This model is available for the G4 machine type only. For detailed steps, see Standard (on-demand) or Spot model.

  * **Spot** : Create an accelerator-optimized [Spot VM instance](https://docs.cloud.google.com/compute/docs/instances/spot) for either A3 High or G4 machine types. For detailed steps, see Standard (on-demand) or Spot model.

  * **Flex-start** : Create a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) for either A3 High or G4 machine types. For detailed steps, see Flex-start model.


**Caution:** Don't flash the GPU firmware of the Confidential VM instances. This can cause instability and potential system crashes.

### Standard (on-demand) or spot model

### gcloud

To create an accelerator-optimized standard (on-demand) or Spot VM instance with the gcloud CLI, use the [`instances create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) sub-command with the `--provisioning-model` flag.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --provisioning-model=PROVISIONING_MODEL \
        --confidential-compute-type=CONFIDENTIAL_COMPUTING_TECHNOLOGY \
        --machine-type=MACHINE_TYPE_NAME \
        --maintenance-policy=TERMINATE \
        --zone=ZONE_NAME \
        --image-project=IMAGE_PROJECT \
        --image-family=IMAGE_FAMILY_NAME \
        --boot-disk-size=30G
    

To enable [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot), you can use the `--shielded-secure-boot` flag for VM instance boots.

Provide the following values:

  * `INSTANCE_NAME`: The name of the new VM instance.

  * `PROVISIONING_MODEL`: The provisioning model supported by the machine type. Choose one of the following:

    * **A3 High machine type** : `SPOT` for Spot VM instances.

    * **G4 machine type** : `STANDARD` for standard (on-demand) VM instances or `SPOT` for Spot VM instances. If not specified, this value defaults to `STANDARD`.

  * `CONFIDENTIAL_COMPUTING_TECHNOLOGY`: The type of [Confidential Computing technology](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#technologies) to use. Choose one of the following:

    * **A3 High machine type** (`a3-highgpu-1g`): `TDX`

    * **G4 machine type** (`g4-standard-48`): `SEV`

  * `MACHINE_TYPE_NAME`: The VM machine type. Choose one of the following:

    * `a3-highgpu-1g`

    * `g4-standard-48`

  * `ZONE_NAME`: The [supported zone](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones) to create the VM in.

  * `IMAGE_PROJECT`: The project that contains the [Confidential VM-supported operating system image for GPU](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-images-gpu).

  * `IMAGE_FAMILY_NAME`: The family for the [Confidential VM-supported operating system image for GPU](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-images-gpu).




### REST

To create a standard (on-demand) or a Spot VM instance, send the following POST request with the appropriate body content.

Use the following HTTP method and URL:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    

Use the following request JSON body:
    
    
    {
      "name": "INSTANCE_NAME",
      "machineType": "zones/ZONE/machineTypes/MACHINE_TYPE_NAME",
      "confidentialInstanceConfig": {
        "confidentialInstanceType": "CONFIDENTIAL_COMPUTING_TECHNOLOGY"
      },
      "scheduling": {
        "onHostMaintenance": "TERMINATE",
        "automaticRestart": true,
        "provisioningModel": "PROVISIONING_MODEL"
      },
      "disks": [
        {
          "boot": true,
          "autoDelete": true,
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY",
            "diskSizeGb": "30"
          }
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/default"
        }
      ]
    }
    

Provide the following values:

  * `PROJECT_ID`: Optional. The ID of the project to create the VM in.

  * `ZONE`: The [supported zone](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones) to create the VM in.

  * `INSTANCE_NAME`: The name of the new VM instance.

  * `MACHINE_TYPE_NAME`: The VM machine type. Choose one of the following:

    * `a3-highgpu-1g`

    * `g4-standard-48`

  * `CONFIDENTIAL_COMPUTING_TECHNOLOGY`: The type of [Confidential Computing technology](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#technologies) to use. Choose one of the following:

    * **A3 High machine type** (`a3-highgpu-1g`): `TDX`

    * **G4 machine type** (`g4-standard-48`): `SEV`

  * `PROVISIONING_MODEL`: The provisioning model supported by the machine series. Choose one of the following:

    * **A3 High machine type** : `SPOT` for Spot VM instances.

    * **G4 machine type** : `STANDARD` for standard (on-demand) VM instances or `SPOT` for Spot VM instances. If not specified, this value defaults to `STANDARD`.

  * `IMAGE_PROJECT`: The project that contains the [Confidential VM-supported operating system image for GPU](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-images-gpu).

  * `IMAGE_FAMILY`: The family for the [Confidential VM-supported operating system image for GPU](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-images-gpu).




## Flex-start model

To use the [flex-start model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models), first create an instance template, and then use that template to create a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups). You can then add GPU VM instances to the MIG using [resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

Using a MIG resize request with the flex-start provisioning model improves the obtainability of GPU VM instances. For more information, see [About resize requests in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

### Before you begin

  * For creating a MIG, see the [MIG prerequisites](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms#byb).
  * For creating a resize request in a MIG, see the [resize request limitations](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig#limitations).



### Create a MIG with GPU VM instances

To create an instance template, and then to use the template to create a MIG, complete the following steps.

  1. Create an instance template.

### gcloud
         
         gcloud beta compute instance-templates create INSTANCE_TEMPLATE_NAME \
             --provisioning-model=FLEX_START \
             --confidential-compute-type=CONFIDENTIAL_COMPUTING_TECHNOLOGY \
             --machine-type=MACHINE_TYPE_NAME \
             --maintenance-policy=TERMINATE \
             --image-project=IMAGE_PROJECT \
             --image-family=IMAGE_FAMILY_NAME \
             --boot-disk-size=30G \
             --instance-termination-action=DELETE \
             --max-run-duration=RUN_DURATION \
             --project=PROJECT_ID
         

Provide the following values:

     * `INSTANCE_TEMPLATE_NAME`: The name of the new VM instance template.

     * `CONFIDENTIAL_COMPUTING_TECHNOLOGY`: The type of [Confidential Computing technology](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#technologies) to use. Choose one of the following:

       * **A3 High machine type** (`a3-highgpu-1g`): `TDX`

       * **G4 machine type** (`g4-standard-48`): `SEV`

     * `MACHINE_TYPE_NAME`: The VM machine type. Choose one of the following:

       * `a3-highgpu-1g`

       * `g4-standard-48`

     * `IMAGE_PROJECT`: The project that contains the [Confidential VM-supported operating system image for GPU](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-images-gpu).

     * `IMAGE_FAMILY_NAME`: The family for the [Confidential VM-supported operating system image for GPU](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-images-gpu) to use.

     * `RUN_DURATION`: The duration you want the requested VM instances to run. You must format the value as the number of days, hours, minutes, or seconds followed by `d`, `h`, `m`, and `s`, respectively. For example: `6d8h44m`.

     * `PROJECT_ID`: The ID of the project to create the VM in.

### REST

To create a Confidential VM instance template, send the following POST request with the appropriate body content.

Use the following HTTP method and URL:
    
    POST https://compute.googleapis.com/compute/beta/projects/PROJECT_ID/regions/REGION/instanceTemplates
    

Use the following request JSON body:
    
    {
      "name": "INSTANCE_TEMPLATE_NAME",
      "properties": {
        "confidentialInstanceConfig": {
          "confidentialInstanceType": "CONFIDENTIAL_COMPUTING_TECHNOLOGY"
        },
        "machineType": "MACHINE_TYPE_NAME",
        "scheduling": {
          "instanceTerminationAction": "DELETE",
          "maxRunDuration": {
            "seconds": "RUN_DURATION_IN_SECONDS"
          },
          "automaticRestart": true,
          "onHostMaintenance": "TERMINATE",
          "provisioningModel": "FLEX_START",
          "preemptible": false
        },
        "disks": [
          {
            "autoDelete": true,
            "index": 0,
            "boot": true,
            "kind": "compute#attachedDisk",
            "mode": "READ_WRITE",
            "initializeParams": {
              "sourceImage": "projects/IMAGE_PROJECT/global/images/family/IMAGE_FAMILY_NAME",
              "diskSizeGb": "30"
            },
            "type": "PERSISTENT"
          }
        ],
        "networkInterfaces": [
          {
            "accessConfigs": [
              {
                "kind": "compute#accessConfig",
                "name": "external-nat",
                "networkTier": "PREMIUM",
                "type": "ONE_TO_ONE_NAT"
              }
            ],
            "kind": "compute#networkInterface",
            "name": "nic0",
            "network": "projects/PROJECT_ID/global/networks/default"
          }
        ],
        "canIpForward": false
      }
    }
    

To enable Secure Boot, you can include the following object for VM instance boots.
    
    "shieldedInstanceConfig": {
      "enableIntegrityMonitoring": true,
      "enableSecureBoot": true,
      "enableVtpm": true
    }
    

Provide the following values:

     * `PROJECT_ID`: The ID of the project to create the template in.

     * `REGION`: The region to create the template in.

     * `INSTANCE_TEMPLATE_NAME`: The name of the new VM instance template.

     * `CONFIDENTIAL_COMPUTING_TECHNOLOGY`: The type of [Confidential Computing technology](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview#technologies) to use. Choose one of the following:

       * **A3 High machine type** (`a3-highgpu-1g`): `TDX`

       * **G4 machine type** (`g4-standard-48`): `SEV`

     * `MACHINE_TYPE_NAME`: The VM machine type. Choose one of the following:

       * `a3-highgpu-1g`

       * `g4-standard-48`

     * `RUN_DURATION_IN_SECONDS`: The duration, in seconds, that you want the requested VM instances to run. The value must be between `600` and `604800` seconds.

     * `IMAGE_PROJECT`: The project that contains the [Confidential VM-supported operating system image for GPU](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-images-gpu).

     * `IMAGE_FAMILY_NAME`: The family for the [Confidential VM-supported operating system image for GPU](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-images-gpu) to use.

  2. [Create a MIG and a resize request](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-gpu-vms#create-mig-and-add-gpu-vms-all-at-once) to add GPU VM instances all at once.

  3. List the instances present in the MIG.

### gcloud
         
         gcloud compute instance-groups managed list-instances INSTANCE_GROUP_NAME \
             --zone=ZONE_NAME \
             --project=PROJECT_ID
         

Provide the following values:

     * `INSTANCE_GROUP_NAME`: The name of the MIG.

     * `ZONE_NAME`: The [supported zone](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones) to get a list of VM instances from.

     * `PROJECT_ID`: Optional. The ID of the project to get a list of VM instances from.

### REST

To list all templates, send the following GET request.

Use the following HTTP method and URL:
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/instanceTemplates
    

To narrow the list of instances to a specific zone, send the following GET request.

Use the following HTTP method and URL:
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/ZONE_NAME/instanceTemplates
    

Provide the following values:

     * `ZONE_NAME`: The [supported zone](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones) to get a list of VM instances from.

     * `PROJECT_ID`: The ID of the project to get a list of VM instances from.




## Use reservations with Confidential VM instances

You can use [reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview) to make sure you have capacity for your Confidential VM instances only with the G4 machine type.

To use a reservation for your Confidential VM instance:

  1. [Create a standard reservation in the supported zone](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project). You can control how instances consume this reservation using the `--require-specific-reservation` flag during reservation creation.

  2. Create a Confidential VM instance to use the reservation. When you create the VM instance, include the `--confidential-compute-type=SEV` flag to make it a Confidential VM instance. How this instance consumes the reservation depends on the reservation's affinity settings.




The following examples show how to use reservations with Confidential VM instances. The method for consuming the reservation depends on how the reservation was created:

  * **Automatic consumption** : If a reservation is created without the `--require-specific-reservation` flag, you can create a G4 Confidential VM instance with matching properties (such as machine type or zone) to automatically use the reservation.

  * **Specific consumption** : If a reservation is created with the `--require-specific-reservation` flag, you must target the reservation using the `--reservation-affinity=specific` and `--reservation=RESERVATION_NAME` flags when creating the instance:
        
        gcloud compute instances create INSTANCE_NAME \
            --project=PROJECT_ID \
            --zone=ZONE_NAME \
            --machine-type=g4-standard-48 \
            --confidential-compute-type=SEV \
            --image-project=ubuntu-os-cloud \
            --image-family=ubuntu-2404-lts-amd64 \
            --reservation-affinity=specific \
            --reservation=RESERVATION_NAME
        

Provide the following values:

    * `INSTANCE_NAME`: The name of the new VM instance.

    * `PROJECT_ID`: Optional. The ID of the project to create the VM in.

    * `ZONE_NAME`: The [supported zone](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones) to create the VM in.

    * `RESERVATION_NAME`: The name of the reservation.




To learn how VM instances consume reservations and how affinity works, see [Consume reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume).

## Enable confidential computing mode on the GPU

  1. Connect to a VM instance in the MIG using the [gcloud compute ssh command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh).
         
         gcloud compute ssh
         

  2. Update the package list and install the necessary tools and libraries.
         
         sudo apt-get update --yes
         sudo apt-get install linux-headers-$(uname -r)
         sudo apt install -y build-essential libxml2 libncurses5-dev pkg-config libvulkan1 gcc-12
         

  3. [Install the appropriate GPU drivers on the VM instance](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu). For Secure Boot enabled VM instances, see [Install GPU drivers (Secure Boot VMs)](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#secure-boot). We recommend using version 580 or later of the NVIDIA open kernel module drivers.

  4. To configure secure communication between the GPU and the GPU driver, enable the Linux Kernel Crypto API (LKCA).
         
         echo "install nvidia /sbin/modprobe ecdsa_generic; /sbin/modprobe ecdh; /sbin/modprobe --ignore-install nvidia" | sudo tee /etc/modprobe.d/nvidia-lkca.conf
         sudo update-initramfs -u
         

  5. Enable persistence mode to establish a secure Security Protocol and Data Model (SPDM) connection between the GPU and the GPU driver.
         
         sudo test -f /usr/lib/systemd/system/nvidia-persistenced.service && sudo sed -i "s/no-persistence-mode/uvm-persistence-mode/g" /usr/lib/systemd/system/nvidia-persistenced.service
         sudo systemctl daemon-reload
         

  6. Reboot the VM instance to apply LKCA and persistence mode configurations.
         
         sudo reboot
         

  7. Connect to a VM instance in the MIG using the [gcloud compute ssh command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh).
         
         gcloud compute ssh
         

  8. (Optional) [Install the CUDA samples](https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu#no-secure-boot) that support the driver version that you need.
         
         wget -O cuda-samples.tar.gz https://github.com/NVIDIA/cuda-samples/archive/refs/tags/v12.9.tar.gz
         tar xzvf cuda-samples.tar.gz
         




## What's next

  * Learn how to [verify confidential mode is enabled on GPUs](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/verify-confidential-computing-mode-on-gpu).

  * Learn more about [GPU quota](https://docs.cloud.google.com/confidential-computing/confidential-vm/quotas#gpu-quotas).

  * To understand quota consumption, see [GPU VMs and preemptible allocation quotas](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#preemptible-quotas).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
