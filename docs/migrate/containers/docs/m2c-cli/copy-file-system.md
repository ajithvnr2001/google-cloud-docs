---
url: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/copy-file-system/
title: Copy the source machine's file system \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:09.077158+00:00
---

# Copy the source machine's file system  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/copy-file-system/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Copy the source machine's file system 

Modernization of an application component requires creating a copy of the source machine's file system.

This page describes the steps required to copy the source machine's file system along with some specifications for reducing the size of the copied file system.

## Create a local copy of the Linux source machine file system

The Migrate to Containers CLI supports access to source machines using either direct SSH connection or by using `gcloud`.

**Note:** The user that you use to access the source machine must be a sudoer to be able to access all files and directories relevant to modernization. If sudo is disabled for all users including root, use the root user and use the flag `--remote-sudo=false`.

###  Direct SSH 

To copy using direct SSH access, run the following command:
    
    
    ./m2c copy ssh [USERNAME@]HOSTNAME \
      -i PATH_TO_PRIVATE_KEY \
      -o OUTPUT_FILESYSTEM_DIR
    

Replace the following:

  * USERNAME: your username
  * HOSTNAME: the hostname
  * PATH_TO_PRIVATE_KEY: the path to private key
  * OUTPUT_FILESYSTEM_DIR: the path for the output directory on your local machine where you want to copy the source machine's file system



###  gcloud 

If the source machine has a public IP, run the following command:
    
    
    ./m2c copy gcloud \
      -p PROJECT_ID \
      -z ZONE \
      -n VM_NAME \
      -o OUTPUT_FILESYSTEM_DIR
    

Replace the following:

  * PROJECT_ID: the project ID
  * ZONE: the zone of your VM
  * VM_NAME: the name of the source VM
  * OUTPUT_FILESYSTEM_DIR: the path for the directory output on your local machine where you want to copy the source machine's file system



If the source machine doesn't have a public IP, you can do one of the following:

  * If you are running the Migrate to Containers CLI from a machine in the same internal network, Use the `--internal-ip` flag.
  * If you are running on a different network, use the `--tunnel-through-iap` flag.



For more information about these flags, see the [gcloud documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/ssh#:%7E:text=can%20be%20specified%3A-,%2D%2Dinternal%2Dip,-Connect%20to%20instances).

After the copy is complete, a copy of the source machine's file system is available in the specified output directory.

### Reduce the size of the copied file system

Depending on the source machine, the copied file system might be very large. The larger the copy, the longer it takes for each operation to complete and, if there's not enough space, the copy operation fails.

The Migrate to Containers CLI applies filters to reduce the size of the copy, but with the given knowledge of the application component, you can modify the filters to further reduce the size of the copy.

When you run the `copy` command again with the modified filters, the contents of the output directory are updated according to the changes you applied in the filter file.

To modify the default filters, follow these steps:

  1. Get a list of the default filters:
         
         ./m2c copy default-filters > filters.txt
         

  2. Edit the file `filters.txt` to remove irrelevant directories. The file uses the `rsync` filter rule format, as specified in the [`rsync` documentation page](https://linux.die.net/man/1/rsync#Filter%20Rules).

  3. Use the `--filters` flag to specify the filter file with the `copy` command.

###  Direct SSH 
         
         ./m2c copy ssh [USERNAME@]HOSTNAME \
           -i PATH_TO_PRIVATE_KEY \
           -o OUTPUT_FILESYSTEM_DIR \
           --filters filters.txt
         

###  gcloud 
         
         ./m2c copy gcloud \
           -p PROJECT_ID \
           -z ZONE \
           -n VM_NAME \
           -o OUTPUT_FILESYSTEM_DIR \
           --filters filters.txt
         




## Create a local copy of the Windows source machine file system

For Windows source machines, you need to copy the disk images in VHD or VHDX format for the migration process. However, Migrate to Containers CLI does not support exporting disk images from your source platform to your local machine.

  * To export a Compute Engine virtual machine (VM) instance disk, first [create an image from the disk](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image) and then export the image to the local machine.

  * To export an image from Compute Engine, perform the following steps:

    1. Export the image to Cloud Storage using the [`gcloud compute images export` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/export):
           
           gcloud compute images export \
             --export-format vhdx \
             --destination-uri DESTINATION_URI \
             --image IMAGE_NAME
           

Replace the following:

       * `DESTINATION_URI`: the Cloud Storage URI destination for the exported image file.
       * `IMAGE_NAME`: the name of the disk image to export.
    2. Download the image on your local machine:
           
           gcloud storage cp DESTINATION_URI LOCAL_PATH
           

Replace the following:

       * DESTINATION_URI: the Cloud Storage URI destination of the exported image file
       * LOCAL_PATH: the path to the local folder where you want to download the image

For more information, see [Export a custom image to Cloud Storage](https://docs.cloud.google.com/compute/docs/images/export-image).

  * For more information on exporting Amazon EC2 images, see [Exporting an instance as a VM using VM Import/Export](https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html).

**Note:** When you create the JSON file for exporting an image, omit the `ContainerFormat` field, and set `DiskImageFormat` to `"VHD"`.
  * For more information on exporting Azure Cloud Compute images, see [Download a Windows VHD from Azure](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/download-vhd?tabs=azure-portal).

  * To export VMware VM disk images, first complete the steps to [export an image to a VMDK file](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere-lifecycle-manager.doc/GUID-A3E9D4BA-CAAC-4F2C-B97F-C0904ECE5E14.html). Then, convert the VMDK file to a VHD file using third-party tools such as [qemu-img](https://cloudbase.it/qemu-img-windows/).




## What's next

  * Learn how to [create a migration plan](https://docs.cloud.google.com/migrate/containers/docs/m2c-cli/create-a-migration-plan).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
