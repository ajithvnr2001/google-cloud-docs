---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vm-boot-disks/create-customized-boot-disk/
title: Create a customized boot disk \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:27.545059+00:00
---

# Create a customized boot disk  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vm-boot-disks/create-customized-boot-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create a customized boot disk Stay organized with collections  Save and categorize content based on your preferences. 

When you create a virtual machine (VM) instance, you must also create a boot disk for that VM. You can use either a public image or a custom image. GDC automatically creates a boot persistent disk when you [create a VM instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start). If you require additional data storage disks for your instances, [add a persistent disk to your VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-storage/add-a-vm-disk).

Use the procedures described on this page to create boot disks that you can use later to create VMs.

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview). All commands for GDC air-gapped appliance use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. Locate the Management API server name, or ask your Platform Administrator (PA) what the server name is.

  2. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  3. Use the path to replace `MANAGEMENT_API_SERVER{"</var>"}}` in these instructions.




## Request permissions and access

To perform the tasks listed in this page, you must have access to VM disks. Follow the steps to either [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation) or have your Project IAM Admin [assign](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#grant-user-access-vm-resources) you the Project VirtualMachine Admin (`project-vm-admin`) role in the namespace of the project where the VM resides.

For VM operations using the GDC console or the gdcloud CLI, request your Project IAM Admin to assign you both the Project VirtualMachine Admin role and the Project Viewer (`project-viewer`) role.

## Create a boot disk from an image

You can create a standalone, boot, persistent disk outside of instance creation and attach it to an instance afterwards. This section shows how to create a boot disk from either a [GDC-provided OS image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start#create-vm-from-provided-image) or a [custom OS image](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start#create-vm-from-custom).

### Create a boot disk from a GDC-provided image

Before you create a boot disk by using a GDC-provided image, review the list of available images. Then create a boot disk with the provided image.

###  gdcloud 

  1. List all available images and their minimum disk size:
         
         gdcloud compute images list
         

This command includes both GDC air-gapped appliance-provided and custom images. Choose either one in the `vm-system` namespace.

  2. Select a GDC air-gapped appliance-provided image to create the VM disk:
         
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
             get virtualmachineimages.virtualmachine.gdc.goog --namespace vm-system
         

  2. Get the `minimumDiskSize` of a specific GDC-provided image. The size of the created customized boot disk must be at least the `minimumDiskSize`:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           get virtualmachineimages.virtualmachine.gdc.goog --namespace vm-system \
           IMAGE_NAME -ojsonpath='{.spec.minimumDiskSize}'
         

  3. Create a `VirtualMachineDisk` object:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER apply -n PROJECT -f - <<EOF
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
         

Replace the variables using the following definitions:

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` file.  
---|---  
`IMAGE_NAME` | The name of the image.  
`PROJECT` | The GDC project in which to create the boot disk.  
`BOOT_DISK_NAME` | The name of the boot disk.  
`DISK_SIZE` | The size of the boot disk, needs to be at least the `minimumDiskSize` of the image.  



### Create a boot disk from a custom image

A custom image belongs exclusively to your project. To create a VM with a custom boot disk image, if the image doesn't already exist in your project then you must [create one](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-custom-images/create-custom-images).

Set up the necessary [IAM roles](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation) to access custom images in your project if you haven't done so yet. Then proceed with these instructions.

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



###  kubectl 

  1. List all custom images:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             get virtualmachineimages.virtualmachine.gdc.goog --namespace PROJECT
         

  2. Get the `minimumDiskSize` of a specific customized image. The size of the created customized boot disk must be at least the `minimumDiskSize`:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           get virtualmachineimages.virtualmachine.gdc.goog --namespace vm-system \
           IMAGE_NAME -ojsonpath='{.spec.minimumDiskSize}'
         

  3. Create a `VirtualMachineDisk` object:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             apply --namespace PROJECT -f - <<EOF
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

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server `kubeconfig` file.  
---|---  
`IMAGE_NAME` | The name of the image chosen from the list all custom images command.  
`PROJECT` | The GDC project in which to create the boot disk.  
`BOOT_DISK_NAME` | The name of the boot disk.  
`DISK_SIZE` | The size of the boot disk, needs to be at least the `minimumDiskSize` of the image.  



To replace a boot disk, see the [Replace a boot disk](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/manage-vm-boot-disks/replace-a-boot-disk) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
