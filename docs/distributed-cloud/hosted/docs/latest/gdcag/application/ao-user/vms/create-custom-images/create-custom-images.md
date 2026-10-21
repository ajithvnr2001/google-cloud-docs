---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/create-custom-images/
title: Create custom images \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:00:16.463151+00:00
---

# Create custom images  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/create-custom-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create custom images Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a custom image for use with Google Distributed Cloud (GDC) air-gapped virtual machine (VM) instances.

You can create custom images from existing source disks and use them to [create and start](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-and-start) virtual machines (VMs). Custom images are ideal for when you create and modify a persistent boot disk to a certain state and need to save that state for creating VMs. Creating and saving a custom image to use as a new VM image in future VM creation prevents duplicating your setup steps later.

This document is for developers in platform administrator or application operator groups that create VMs and manage VM images in a Google Distributed Cloud (GDC) air-gapped environment. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

To use `gdcloud` command-line interface (CLI) commands, ensure that you have downloaded, installed, and configured the [`gdcloud` CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-overview). All commands for Distributed Cloud use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.

### Get the kubeconfig file path

To run commands against the Management API server, ensure you have the following resources:

  1. [Sign in and generate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/iam/sign-in#cli) the kubeconfig file for the Management API server if you don't have one.

  2. Use the path to the kubeconfig file of the Management API server to replace `MANAGEMENT_API_SERVER` in these instructions.




### Request IAM roles

Contact your Project IAM Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Project Viewer**(`project-viewer`): view all resources within the project namespaces.

  * **Virtual Machine Image Project Admin** (`project-vm-image-admin`): create, list, and delete custom VM images in the project namespace.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/preparation#verify-user-access) your access.

## Create a custom image

This section describes how to create a custom image on a VM.

### Prepare your VM for an image

You can create an image from a disk while it is attached to a running VM. However, your image is more reliable if you put the VM into a state for the image to capture.

### Stop writing data to the persistent disk

[Stop the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#stop-a-vm) so that it can shut down and stop writing any data to the persistent disk.

**Important:** If you don't stop the VM, the image import process won't run successfully.

## Create the image

Follow these steps to create disk images from a persistent disk, even while that disk is attached to a VM:

###  Console 

  1. Select a project.

  2. In the navigation menu, click **Virtual Machines > Images**.

  3. Click **Create Image**.

  4. Enter a unique name for the image. The name must be no longer than 35 characters.

  5. Enter a version to add to the image name.

  6. In the **Source Disk** field, select a disk.

  7. In the **Minimum Disk Size field** , enter a disk size.

  8. Enter a description of the image.

  9. Click **Create**.




The image appears in the list of images.

###  API 

  1. List all `VirtualMachineDisk` objects:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachinedisks.virtualmachine.gdc.goog
         

  2. Select a `VirtualMachineDisk` object to use as source disk for the new image.

**Important:** Ensure that the selected `VirtualMachineDisk` is not attached to a running VM. If the image is created while attached to the VM, the new image can be corrupt.
  3. Check whether the VM disk is attached to a VM:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             -n PROJECT \
             get virtualmachinedisks.virtualmachine.gdc.goog DISK_NAME \
             -o jsonpath='{.status.virtualMachineAttachments}'
         

The following example output shows a disk attached to a VM:
         
         [{"autoDelete":true,"nameRef":{"name":"vm1"},"uid":"...."}]
         

     * If the output returns a value for `"name"`, the disk is attached to a VM signified by the `name` field. In this example, the `name` value is `vm1`. Proceed to check the VM's running status.
     * If the output is empty, proceed to get the `size` of the `VirtualMachineDisk`.
  4. [Check](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/vm-instance-lifecycle#vm-status) the VM's running status. If the status is not `Stopped`, [Stop the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#stop-a-vm) and proceed with creating the `VirtualMachineImage`.

  5. Get the `size` of `VirtualMachineDisk` to create the image:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachinedisks.virtualmachine.gdc.goog DISK_NAME \
           -o jsonpath='{.spec.size}'
         

  6. Create a `VirtualMachineImageImport` object and deploy it to the Management API server:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           apply -f - <<EOF
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineImageImport
         metadata:
           name: VM_IMAGE_IMPORT_NAME
         spec:
           source:
             diskRef:
               name: DISK_NAME
           imageMetadata:
             name: IMAGE_NAME
             operatingSystem: OS_NAME
             minimumDiskSize: MINIMUM_DISK_SIZE
         EOF
         

  7. Verify that the image import has finished and the status is `Ready`:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachineimageimports.virtualmachine.gdc.goog VM_IMAGE_IMPORT_NAME \
           -o jsonpath='{.status}'
         

When the import is complete, the status output looks similar to the following:
         
         {
           "conditions": [
             {
               "lastTransitionTime": "",
               "message": "",
               "observedGeneration": 1,
               "reason": "ImportJobComplete",
               "status": "True",
               "type": "Ready"
             }
           ],
           "imageName": IMAGE_NAME
         }
         

  8. Verify the image has been created:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachineimages.virtualmachine.gdc.goog  \
           CREATED_IMAGE_NAME
         

Replace the variables using the following definitions.

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server kubeconfig file.  
---|---  
`PROJECT` | The GDC project in which to create the image.  
`DISK_NAME` | The name of the source disk, such as `vm1-boot-disk`.  
`VM_IMAGE_IMPORT_NAME` | The name of the VM image import. The name must be no longer than 35 characters.  
`IMAGE_NAME` | The name of the created image, such as `custom-image`.  
`OS_NAME` | The name of the Linux image OS. Specify one of the following:  
`ubuntu-2004`, `ubuntu-2204`, `ubuntu-2404`, or `rhel-8`.  
`MINIMUM_DISK_SIZE` | The minimum disk size in the VM image import, such as `20G`:  
_`minimumDiskSize` must always be greater than or equal to the source boot disk size._  
`CREATED_IMAGE_NAME` | The name of the created image. The created image name must be unique; you cannot use an image name that already exists in the project.  



###  Terraform 

  1. List all `VirtualMachineDisk` objects:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachinedisks.virtualmachine.gdc.goog
         

  2. Select a `VirtualMachineDisk` object to use as source disk for the new image.

**Important:** Ensure that the selected `VirtualMachineDisk` is not attached to a running VM. If the image is created while attached to the VM, the new image can be corrupt.
  3. Check whether the VM disk is attached to a VM:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
             -n PROJECT \
             get virtualmachinedisks.virtualmachine.gdc.goog DISK_NAME \
             -o jsonpath='{.status.virtualMachineAttachments}'
         

Example output showing a disk is attached to a VM:
         
         [{"autoDelete":true,"nameRef":{"name":"vm1"},"uid":"...."}]
         

     * If the output returns a value for `"name"`, the disk is attached to a VM signified by the `name` field. In this example output, the `name` value is `vm1`. Proceed to check the VM's running status.
     * If the output is empty, proceed to get the `size` of the `VirtualMachineDisk`.
  4. [Check](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/vm-instance-lifecycle#vm-status) the VM's running status. If the status is not `Stopped`, [Stop the VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/manage-vms/operations-and-lifecycle/start-and-stop-vm#stop-a-vm) and proceed with creating the `VirtualMachineImage`.

  5. Get the `size` of `VirtualMachineDisk` to create the image:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachinedisks.virtualmachine.gdc.goog DISK_NAME \
           -o jsonpath='{.spec.size}'
         

  6. Create a file named `main.tf` with the following content:
         
         provider "kubernetes" {
           config_path = "MANAGEMENT_API_SERVER"
         }
         
         resource "kubernetes_manifest" "image_import" {
           manifest = {
             "apiVersion" = "virtualmachine.gdc.goog/v1"
             "kind" = "VirtualMachineImageImport"
             "metadata" = {
               "name" = "VM_IMAGE_IMPORT_NAME"
               "namespace" = "PROJECT"
             }
             "spec" = {
               "source" = {
                 "diskRef" = {
                   "name" = "DISK_NAME"
                 }
               }
               "imageMetadata" = {
                 "name" = "IMAGE_NAME"
                 "operatingSystem" = "OS_NAME"
                 "minimumDiskSize" = "MINIMUM_DISK_SIZE"
               }
             }
           }
         }
         

  7. Apply the `VirtualMachineImageImport` object using Terraform:
         
         terraform apply
         

  8. Verify that the image import has finished and the status is `Ready`:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachineimageimports.virtualmachine.gdc.goog VM_IMAGE_IMPORT_NAME \
           -o jsonpath='{.status}'
         

The status should look like this when the import is complete:
         
         {
           "conditions": [
             {
               "lastTransitionTime": "",
               "message": "",
               "observedGeneration": 1,
               "reason": "ImportJobComplete",
               "status": "True",
               "type": "Ready"
             }
           ],
           "imageName": IMAGE_NAME
         }
         

  9. Verify the image has been created:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT \
           get virtualmachineimages.virtualmachine.gdc.goog  \
           CREATED_IMAGE_NAME
         

Replace the variables, using the following definitions.

Variable| Definition | `MANAGEMENT_API_SERVER` | The Management API server kubeconfig file.  
---|---  
`PROJECT` | The GDC project in which to create the image.  
`DISK_NAME` | The name of the source disk, such as `vm1-boot-disk`.  
`VM_IMAGE_IMPORT_NAME` | The name of the VM image import. The name must be no longer than 35 characters.  
`IMAGE_NAME` | The name of the created image, such as `custom-image`.  
`OS_NAME` | The name of the Linux image OS. Specify one of the following:  
`ubuntu-2004`, `ubuntu-2204`, `ubuntu-2404`, or `rhel-8`.  
`MINIMUM_DISK_SIZE` | The minimum disk size in the VM image import, such as `20G`:  
_`minimumDiskSize` must always be greater than or equal to the source boot disk size._  
`CREATED_IMAGE_NAME` | The name of the created image. The created image name must be unique; you cannot use an image name that already exists in the project.  



## What's next

  * [Supported VM images](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/supported-vm-images)
  * [Import virtual disks](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-custom-images/import-virtual-disk)
  * [Create a VM with GPUs](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vms/create-a-vm/create-vm-gpu)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
