---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-custom-images/import-virtual-disk/
title: Import virtual disks \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:34.729928+00:00
---

# Import virtual disks  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-custom-images/import-virtual-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Import virtual disks Stay organized with collections  Save and categorize content based on your preferences. 

If you have virtual disks in your on-premises environment with software and configurations that you need, occasionally referred to as _golden disks_ or _golden images_ , you can save time by importing those virtual disks into GDC air-gapped appliance and using the resulting image to create virtual machines. The import tool supports RAW and QCOW image formats.

## Before you begin

Before continuing, ensure that you have the following:

  * The [gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-overview) downloaded, installed, and configured. All CLI commands for GDC use the `gdcloud` or `kubectl` CLI, and require an operating system (OS) environment.


  * Access to the Management API server. Follow the CLI steps in [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/iam/sign-in#cli) to sign in to the Management API server.

**Note:** Record the path to the generated file, such as `/tmp/org-1-admin-kubeconfig.yaml`. Use the path to replace MANAGEMENT_API_SERVER_KUBECONFIG in these instructions.



### Request IAM roles

Contact your Project IAM Admin to request the following roles on your project:

  * **Virtual Machine Project Admin** (`project-vm-admin`): create, modify, list, and delete VMs in the project namespace.

  * **Project Viewer**(`project-viewer`): view all resources within the project namespace.

  * **Virtual Machine Image Project Admin** (`project-vm-image-admin`): create, list, and delete VM images in the project namespace.




All VM roles must bind to the namespace of the project where the VM resides. Follow the steps to [verify](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/preparation#verify-user-access) your access.

## Import virtual disks

You can import VM image disk files directly from your workstation. The import tool automatically uploads the file to an object storage bucket in your project.

To import your virtual disks, use either the gdcloud CLI or the [Virtual Machine Manager API](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/apis/service/virtualmachine/vmm-api-overview).

###  gdcloud 

The `import` command checks that the GDC-provided image has the required packages to configure credentials for connecting to the instance using secure shell (SSH) and Remote Desktop Protocol (RDP). This includes packages for the guest environment.

The command also installs packages for network time protocol (NTP) and `cloud-init` for the instance to run properly in GDC.

To create a bootable image, use the `gdcloud compute images import` command:
    
    
    gdcloud compute images import IMAGE_NAME \
      --source-file=SOURCE_FILE \
      --os=IMAGE_OS \
      --timeout=TIMEOUT
    

Replace the following variables:

  * IMAGE_NAME: the name of your destination image. The name must be no longer than 35 characters.
  * SOURCE_FILE: your virtual disk file. This file is a local file on your workstation. You can provide an absolute or relative path. 
  * IMAGE_OS: the OS on the disk to import. 
  * TIMEOUT: the time an import can last before it fails with "TIMEOUT". For example, if you specify `2h`, the process fails after 2 hours. The default timeout is `1h`.



The upload operation can take an extended period of time depending on the size of your virtual disk and the speed of your network connection. The import operation can take tens of minutes to run depending on the size of the disk.

###  API 

To import a virtual disk through the API, do the following:

  1. Create a `VirtualMachineImageImport` object in the Management API server to start the image import process:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT_ID \
           apply -f - <<EOF
         apiVersion: virtualmachine.gdc.goog/v1
         kind: VirtualMachineImageImport
         metadata:
           name: IMAGE_NAME
           namespace: PROJECT_ID
         spec:
           source:
             objectStorage:
               bucketRef:
                 name: vm-images-bucket
               objectName: SOURCE_FILE
           imageMetadata:
             name: IMAGE_NAME
             operatingSystem: IMAGE_OS
             minimumDiskSize: DISK_SIZE
         EOF
         

Replace the following variables:

     * IMAGE_NAME: The name of the image to import. The name must be no longer than 35 characters.
     * PROJECT_ID: The project ID for the project where you want to import the image.
     * SOURCE_FILE: The name of the source file that contains the upload of the virtual disk to object storage. This value is the section of the object storage path after `vm-images-bucket/`. 
     * IMAGE_OS: The OS on the disk to import. 
     * DISK_SIZE: The minimum size a disk must have to be created with this image. Use at least a 20% buffer on top of the file system size of the original image. For example, use at least `12G` for a virtual disk with an original file system size of 10G.
  2. Monitor the progress of the import by querying the status of the `VirtualMachineImageImport` object:
         
         kubectl --kubeconfig MANAGEMENT_API_SERVER \
           -n PROJECT_ID \
           get virtualmachineimageimport.virtualmachine.gdc.goog IMAGE_NAME \
           -o jsonpath='{.status}'
         




### Clean up resources

The import process involves uploading your virtual disk file to object storage. If you use the gdcloud CLI, the object is cleaned up when the command finishes, whether or not it was successful. If the command is interrupted, or the image import is done with the API, the virtual disk file might remain in the object storage bucket named `vm-images-bucket` until you manually delete the file.

## What's next

Create a new VM instance that uses your image in the page, [Create and start a VM](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/create-a-vm/create-and-start).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
