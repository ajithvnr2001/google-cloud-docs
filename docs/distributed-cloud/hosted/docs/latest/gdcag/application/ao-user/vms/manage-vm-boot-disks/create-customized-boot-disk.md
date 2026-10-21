---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vm-boot-disks/create-customized-boot-disk/
title: Create a customized boot disk \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:46:20.954382+00:00
---

# Create a customized boot disk  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vm-boot-disks/create-customized-boot-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create a customized boot disk Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the steps to create custom boot disks for virtual machines (VMs) in Google Distributed Cloud (GDC) air-gapped. 

When you [create a VM instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start), Distributed Cloud automatically creates a boot-persistent disk with default configurations. You must also create a boot disk for the VM. You can use either a public image or a custom image.

If you require additional data storage disks for your instances, [add a persistent disk to your VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-storage/add-a-vm-disk).

This document is for developers in platform administrator or application operator groups that create customized boot disks for VMs. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

Contact your Project IAM Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete standard and high-performance VMs in the project namespace.

  * **Project Viewer**(`project-viewer`): view all resources within the project namespace.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Create a boot disk

Use the procedures described on this page to create boot disks that you can use later to create VMs.

## Create a boot disk from an image

You can create a standalone boot persistent disk outside of instance creation and attach it to an instance afterwards. This section shows how to create a boot disk from either a [GDC-provided OS image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start#create-vm-from-provided-image) or a [custom OS image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start#create-vm-from-custom).

### Create a boot disk from a GDC-provided image

Before you create a boot disk by using a GDC-provided image, review the list of available images. Then create a boot disk with the provided image.

###  gdcloud 

  1. List all available images and their minimum disk size:
         
         gdcloud compute images list
         

This command includes both Distributed Cloud-provided and custom images. Choose either one in the `vm-system` namespace.

  2. Select a Distributed Cloud-provided image to create the VM disk:
         
         gdcloud compute disks create BOOT_DISK_NAME \
           --project=PROJECT \
           --size=DISK_SIZE \
           --image=IMAGE_NAME \
           --image-project=vm-system
         

Replace the variables using the following definitions:

Variable| Definition | `BOOT_DISK_NAME` | The name of the boot disk.  
---|---  
`PROJECT` | The GDC project in which to create the boot disk.  
`DISK_SIZE` | The size of the boot disk, needs to be at least the `minimumDiskSize` of the image.  
`IMAGE_NAME` | The name of the image.  



###  kubectl 

  1. List all available GDC-provided images:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n vm-system \
           get virtualmachineimages.virtualmachine.gdc.goog
         

  2. Get the `minimumDiskSize` of a specific GDC-provided image. The size of the created customized boot disk must be at least the `minimumDiskSize`:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n vm-system \
           get virtualmachineimages.virtualmachine.gdc.goog IMAGE_NAME \
           -ojsonpath='{.spec.minimumDiskSize}'
         

  3. Create a `VirtualMachineDisk` object:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           apply -f - <<EOF
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineDisk
         metadata:
           name: BOOT_DISK_NAME
         spec:
           source:
             image:
               name: IMAGE_NAME
               namespace: vm-system
           size: DISK_SIZE
         EOF
         

Replace the variables using the following definitions,

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server kubeconfig file.  
---|---  
`IMAGE_NAME` | The name of the image.  
`PROJECT` | The GDC project in which to create the boot disk.  
`BOOT_DISK_NAME` | The name of the boot disk.  
`DISK_SIZE` | The size of the boot disk, needs to be at least the `minimumDiskSize` of the image.  



### Create a boot disk from a custom image

A custom image belongs exclusively to your project. To create a VM with a custom image, you must first [create a custom image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/create-custom-images) in the same project if you don't already have one.

Set up the necessary [IAM roles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation) to access custom images in your project if you haven't done so yet. Then proceed with these instructions.

###  gdcloud 

  1. List all custom images and their minimum disk size:
         
         gdcloud compute images list \
           --project=PROJECT \
         

  2. Select a custom image to create the VM disk:
         
         gdcloud compute disks create BOOT_DISK_NAME \
           --project=PROJECT \
           --size=DISK_SIZE \
           --image=IMAGE_NAME \
           --image-project=PROJECT
         

Replace the variables using the following definitions:

Variable| Definition | `BOOT_DISK_NAME` | The name of the boot disk.  
---|---  
`PROJECT` | The GDC project in which to create the boot disk.  
`DISK_SIZE` | The size of the boot disk, needs to be at least the `minimumDiskSize` of the image.  
`IMAGE_NAME` | The name of the image.  



###  API 

  1. List all custom images:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachineimages.virtualmachine.gdc.goog
         

  2. Get the `minimumDiskSize` of a specific customized image. The size of the created customized boot disk must be at least the `minimumDiskSize`:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n vm-system \
           get virtualmachineimages.virtualmachine.gdc.goog IMAGE_NAME \
           -ojsonpath='{.spec.minimumDiskSize}'
         

  3. Create a `VirtualMachineDisk` object:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           apply -f - <<EOF
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineDisk
         metadata:
           name: BOOT_DISK_NAME
         spec:
           source:
             image:
               name: IMAGE_NAME
               namespace: PROJECT
           size: DISK_SIZE
         EOF
         

Replace the variables, using the following definitions:

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server kubeconfig file.  
---|---  
`IMAGE_NAME` | The name of the image chosen from the list all custom images command.  
`PROJECT` | The GDC project in which to create the boot disk.  
`BOOT_DISK_NAME` | The name of the boot disk.  
`DISK_SIZE` | The size of the boot disk, needs to be at least the `minimumDiskSize` of the image.  



## What's next?

  * [Replace a boot disk](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vm-boot-disks/replace-a-boot-disk)
  * [Connect to a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/connect-to-a-vm)
  * [Transfer files to VMs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/connect-to-vm/transfer-files)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
