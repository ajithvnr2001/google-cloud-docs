---
url: https://docs.cloud.google.com/compute/docs/import/import-existing-image/
title: Manually import boot disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:05.319939+00:00
---

# Manually import boot disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/import/import-existing-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manually import boot disks Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

The image import feature on Compute Engine is being moved to Migrate to Virtual Machines. We recommend that you use the new [image import feature on Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import) to import your virtual disks to Google Cloud. 

The recommended way to import boot disk images to Compute Engine from your physical datacenters, from virtual machines (VMs) on your local workstation, or from VMs that run on another cloud platform, is to use the [virtual disk import tool](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks), which automates all of the steps in this guide.

If you prefer not to use the automated tool, you can follow the manual, step-by-step instructions in this guide.

This image import process can import only one disk at a time, and this guide focuses on how to import boot disk images.

Import your existing boot disks only if you are unable to build or migrate your apps to run on top of [Compute Engine public images](https://docs.cloud.google.com/compute/docs/images). Public images are already configured to run in the Compute Engine environment, so you can run apps on those images without having to worry about bootloader and operating system configurations. However, you might need to import your own boot disk images in the following scenarios:

  * Your apps require an operating system that is not provided as a public image.
  * You already have a set of basic images that you use to create VMs in another cloud platform.
  * The work required to migrate app code to one of the public images is greater than the work required to complete the boot disk image import process.



Alternatively, you can get assistance with migration for your VMs using partner services. For more information, see [Migrating VMs to Compute Engine](https://docs.cloud.google.com/compute/docs/tutorials/migrating-vms-compute-engine).

## Overview

To import a boot disk image to Compute Engine, use the following process:

  1. Plan your import path. You must identify where you are going to prepare your boot disk image before you upload it, and how you are going to connect to that image after it boots in the Compute Engine environment.
  2. Prepare your boot disk so it can boot within the Compute Engine environment and so you can access it after it boots.
  3. Create and compress the boot disk image file.
  4. Upload the image file to [Cloud Storage](https://docs.cloud.google.com/storage) and import the image to Compute Engine as a new [custom image](https://docs.cloud.google.com/compute/docs/images#custom_images).
  5. Use the imported image to create a VM instance and make sure it boots properly.
  6. If the image does not successfully boot, you can troubleshoot the issue by attaching the boot disk image to another instance and reconfiguring it.
  7. [Optimize the image](https://docs.cloud.google.com/compute/docs/import/configuring-imported-images) and install the [guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment) so that your imported operating system image can communicate with the metadata server and use additional Compute Engine features.



## Requirements

### Requirements for the boot disk

To import boot disks to Compute Engine, the boot disks must meet the following requirements:

  * We recommend that you install all available updates in your source VM.
  * If you built a custom operating system kernel, it must meet the [hardware and kernel configuration requirements](https://docs.cloud.google.com/compute/docs/images/building-custom-os). Most stock Linux distributions already meet these requirements, so this requirement is only for advanced users who build their own custom operating systems to run on Compute Engine.
  * The boot disk must be no larger than 2048 GB (2 TB).
  * The boot disk that you import must have a functional [MBR partition table](https://wikipedia.org/wiki/Master_boot_record) or a hybrid configuration of a [GPT partition table](https://wikipedia.org/wiki/GUID_Partition_Table) with an MBR bootloader.
  * The primary partition on the boot disk can be in any format that you like as long as it boots properly from the MBR bootloader.
  * The bootloader on the boot disk must not have `quiet`, `rhgb`, or `splashimage=` kernel command-line arguments. Compute Engine does not support splash screens on startup. You can remove these values from the GRUB config during the bootloader configuration step.
  * The operating system on the boot disk must support [ACPI](https://wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface).



### Requirements for the image file

The image file that you import must meet the following requirements:

  * Perform a consistency check on the disk image by using the `qemu-img check` command on the disk.
  * To export the virtual disk, use the export function of your VM management software. Don't copy the VMDK file from your VM manager's file system.
  * The image file must be of a [supported image](https://docs.cloud.google.com/compute/docs/images/os-details#import).
  * The disk image filename must be `disk.raw`.
  * The RAW image file must have a size in an increment of 1 GB. For example, the file must be either 10 GB or 11 GB but not 10.5 GB.
  * The compressed file must be a `.tar.gz` file that uses [gzip compression](https://wikipedia.org/wiki/Gzip) and the `--format=oldgnu` option for the `tar` utility ([manual](https://www.gnu.org/software/tar/manual/tar.html)).



### Requirements for your project

When you create a VM instance from an imported image, the instance must be able to access the external package repository for the operating system that is configured on the boot disk.

This repository can be accessed directly from the operating system vendor or through a network connection to your on-premises infrastructure that hosts these repositories.

To set up access to the external repository, complete one of the following steps in your project:

  * [Configure a static external IP address](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address) for your VM to connect to your local on-premises network or other external networks.
  * Set up a [bastion host, VPN or IAP TCP forwarding](https://docs.cloud.google.com/compute/docs/connect/ssh-using-iap) that can be used to connect to your local on-premises network or other external networks.



## Limitations

To import disks using networks that don't allow external IP addresses you need to meet additional networking requirements. For more information, see [Importing disks using networks that don't allow external IP addresses](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks#no-external-ip).

## Image import costs

Before you begin, understand the costs for the import process. There is no cost for the [inbound network data transfer](https://cloud.google.com/storage/pricing#network-pricing) to upload your boot disk image file to Cloud Storage and there is no cost to import that image as a Compute Engine [custom image](https://docs.cloud.google.com/compute/docs/images#custom_images). However, there are costs for some specific steps in the import process:

  * The cost to temporarily store your compressed image files in a Cloud Storage [standard bucket](https://cloud.google.com/storage/pricing#storage-pricing). You must use a temporary Cloud Storage bucket to hold your files before you can import them as custom Compute Engine images. You can remove the bucket after you complete the import process.
  * The cost for [storing custom images](https://docs.cloud.google.com/compute/disks-image-pricing#imagestorage) after you finish importing them to Compute Engine.
  * The potential cost for outbound data transfers on your existing data center, network provider, or your current cloud service. Image files can be very large even after you compress them, so copying those files to Compute Engine could incur significant outbound data transfer charges on some platforms.
  * The cost for Compute Engine [persistent disks](https://docs.cloud.google.com/compute/disks-image-pricing#disk) and [VM instances](https://cloud.google.com/compute/vm-instance-pricing) where you can configure your image after you import it to Compute Engine.



## Plan and prepare your import path

Your method for importing your disk depends on the current configuration of the system that you want to move to Compute Engine. You need a system where you can create and compress the boot disk image file as well as a system where you can upload the image file to Cloud Storage. Consider the following items when you plan your import path:

  * The image import path requires you to configure your boot disk in a working operating system environment. This process can cause the boot disk to not boot anywhere outside of a Compute Engine environment. It is your responsibility to ensure that you do not lose data on your disks or disrupt your functional business apps while you import your system to Compute Engine.
  * Identify what your existing system access configuration is, and plan how you want to access the system after you import it to Compute Engine. 
    * If your system has existing user login or SSH configurations, you can configure only the bootloader and then later configure the image to run optimally on Compute Engine. You can access the instance through your existing SSH configuration or through a direct user login in the [interactive serial console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console).
    * If your system does not have existing user login or SSH configurations, you must configure the boot disk so that you are able to access it after it boots on Compute Engine.
  * The length of the import process can take several hours or days depending on the size of your boot disk and the speed of your network connection.
  * The system where you create and compress your boot disk image must have enough storage space to create the image files on a storage device other than the boot disk itself. Typically your image and `tar.gz` files use 2–3 times as much space as the boot disk itself.
  * Understand the file system structure for the existing system that you want to import. 
    * If your operating system and app files are spread across multiple disks, import each of those disks individually and use each image to create a unique persistent disk for your Compute Engine VM instance.
    * If your systems have boot volumes in a [RAID](https://wikipedia.org/wiki/RAID) configuration where multiple disks act as a single logical volume, create a single image from the entire array rather than creating one image for each disk in the array. Compute Engine persistent disks eliminate the need for RAID configurations.
  * If your system encrypts the contents of your boot disk with a [Trusted Platform Module](https://en.wikipedia.org/wiki/Trusted_Platform_Module) or with software-level encryption, decrypt your boot disk before you create the boot disk image file. Google cannot read your images if they are encrypted. We encrypt your images for you after you upload them, and let you provide your own encryption keys for your [persistent disks](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption) and [Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/encryption#customer-supplied).



After you identify or create a system where you can complete the import process, connect to that system and configure the bootloader.

## Prepare the boot disk image

On a running system, prepare the boot disk image so that it can function in a Compute Engine environment.

  * Configure the bootloader on the boot disk so that the image can boot on Compute Engine.
  * Configure SSH or user login access on the boot disk so that you can access it after you import it to Compute Engine and start it as a VM instance.



This process can make the system unbootable outside of Compute Engine, so the best practice is to complete this step on an isolated system using a copy of the boot disk that you want to import.

### Configure the bootloader

Configure the bootloader on the system so that it can boot on Compute Engine.

  1. Connect to the terminal on the system with the boot disk that you plan to import.

  2. Edit the GRUB config file. Usually this file is at `/etc/default/grub`, but on some earlier distributions, it might be located in a non-standard directory.

  3. Make the following changes to the GRUB config file:

     * Remove any line that has `splashimage=`. Compute Engine does not support splash screens on startup.
     * Remove the `rhgb` and `quiet` kernel command-line arguments.
     * Add `console=ttyS0,38400n8d` to the kernel command-line arguments, so that the instance can [interact with the Serial Console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console).
  4. Regenerate the `grub.cfg` file. Use one of the following commands, depending on your distribution.

     * Debian and Ubuntu: `sudo update-grub`
     * RHEL, CentOS, SUSE, openSUSE: `sudo grub2-mkconfig -o /boot/grub2/grub.cfg`
  5. Edit the `/etc/fstab` file and remove references to all disks and partitions other than the boot disk itself and partitions on that boot disk. Invalid entries in `/etc/fstab` can cause your system startup process to stop.




After you configure the bootloader, create and compress the disk image file.

### Configure SSH or user login access on the image

After your image is running in Compute Engine as a VM instance, you must have a way to access that instance. You can either connect to the instance using an existing SSH configuration or you can sign in using a username and password by connecting to the [Serial Console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console).

Complete the SSH or user login configuration before you create and compress the disk image file.

## Create and compress the disk image file

Create and compress the boot disk image file for the system that you want to import to Compute Engine. The process to create and compress the image file is different depending on the platform where your systems operate.

###  Generic 

On almost any system, you can use this process to create a RAW image file that you can import to Compute Engine. You can complete this process on the running system that you are importing, or you can attach your boot disk as a secondary disk on another system and create the boot disk image from the stopped disk. Ensure that you have enough available storage space to temporarily hold the disk image files. This example takes an image from a running system.

  1. Connect to the terminal on the system that has the boot disk that you plan to import.

  2. Use the `lsblk` command to identify the source boot disk from which you want to create an image and the location where you have sufficient space to write the image files. For this example, `/dev/sda` is the source boot disk and `/dev/sdb` is a large secondary disk mounted at the `/tmp` directory. Although /dev/sda is running, you can still create an image from it. It is best to do this on a quiet system that is not actively processing data or running apps.
         
         lsblk
         
         
         NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
         sda      8:0    0  100G  0 disk
         ├─sda1   8:1    0   96G  0 part /
         ├─sda2   8:2    0    1K  0 part
         └─sda3   8:5    0    4G  0 part [SWAP]
         sdb      8:16   0  500G  0 disk /tmp
         sr0     11:0    1 1024M  0 rom
         

  3. Create the image file from your boot disk.
         
         sudo dd if=/dev/sda of=/tmp/disk.raw bs=4M conv=sparse
         

  4. Change to the directory where you wrote the `disk.raw` file.
         
         cd /tmp
         

  5. Compress the raw disk into `tar.gz` format. This step compresses the image file so that you can more quickly upload it to Cloud Storage. On OSX, [install `gtar`](http://macappstore.org/gnu-tar/) and use it for this step instead of `tar`.
         
         tar --format=oldgnu -Sczf /tmp/compressed-image.tar.gz disk.raw
         




###  VirtualBox 

If you prepared your system in a VirtualBox environment, you can use the `VBoxManage` tool to convert a `.vdi` or `.qcow2` disk image to `disk.raw` format.

  1. Shut down the VirtualBox guest machine that you want to import, replacing GUEST_NAME with the name of your guest machine. You can shut down the guest machine with the VirtualBox interface or by using the [VBoxManage](https://www.virtualbox.org/manual/ch08.html) utility.
         
         VBoxManage controlvm GUEST_NAME acpipowerbutton

  2. Convert the guest image to RAW format by using the [VBoxManage](https://www.virtualbox.org/manual/ch08.html) utility, replacing GUEST_NAME with the path to your guest image. This guest image can be supplied as either a `vdi` or `qcow2` file:
         
         VBoxManage clonemedium GUEST_NAME ~/disk.raw --format RAW

  3. Compress the raw disk into `tar.gz` format. This step compresses the image file so that you can more quickly upload it to Cloud Storage. On OSX, [install `gtar`](http://macappstore.org/gnu-tar/), and use it for this step instead of `tar`.
         
         sudo tar --format=oldgnu -Sczf /tmp/compressed-image.tar.gz disk.raw
         




The image file is compressed and ready to upload to Cloud Storage.

## Import the image to your custom images list

Upload the file to Cloud Storage and import the image into your custom images list. Optionally, you can [encrypt the image](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#encrypt_an_imported_image) during the image import step.

Import the image with either the console or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) tools:

###  Console 

Copy the `compressed-image.tar.gz` file to your local workstation and use the Google Cloud console to [create a bucket and upload the file](https://docs.cloud.google.com/storage/docs/quickstart-console).

  1. In the Google Cloud console, go to the Cloud Storage browser page. 

[Go to Browser](https://console.cloud.google.com/storage/browser)

  2. At the top of the page, click **Create bucket**.
  3. Specify a unique bucket name, the **Standard** storage class, and a location where you want to store your image files.
  4. Click **Create** to create the bucket. The browser page navigates to the new bucket.
  5. At the top of the page, click **Upload files**.
  6. In the file dialog, select the `compressed-image.tar.gz` file that you downloaded from your system. The file uploads from your local workstation. This step can take several hours depending on the size of your compressed image file and the speed of your network connection.



After you upload the image to Cloud Storage, import the image file to your custom images list.

  1. In the Google Cloud console, go to the **Images** page. 

[Go to Images](https://console.cloud.google.com/compute/images)

  2. At the top of the page, click **Create image**.
  3. In the **Name** field, specify a unique name for the image.
  4. Optionally, specify an image family for your new image, or configure specific encryption settings for the image.
  5. Click the **Source** menu and select **Cloud Storage file**.
  6. Enter the path to the `compressed-image.tar.gz` file that you uploaded to Cloud Storage.
         
         BUCKET_NAME/compressed-image.tar.gz

  7. Click **Create** to import the image. The process can take several minutes depending on the size of the boot disk image.




The image is now included on the [**Images** page](https://console.cloud.google.com/compute/images). You can create a VM using this imported image. If there is a boot failure, verify and ensure that you have configured the bootloader correctly.

###  gcloud and gcloud storage 

Use the gcloud CLI to upload the compressed boot disk image file. You can complete this process on the system where you created the boot disk image, or you can copy that file to another system and complete the upload process there, instead.

  1. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs) on the system from which you plan to upload the `compressed-image.tar.gz`.

  2. Use the gcloud CLI to create a new Cloud Storage bucket.
         
         gcloud storage buckets create gs://BUCKET_NAME

  3. Upload the `compressed-image.tar.gz` file to the new bucket.
         
         gcloud storage cp compressed-image.tar.gz gs://BUCKET_NAME

  4. Import the image file as a new custom image.

**Note:** When you manually import an image, you must set the right license code for your operating system using the [`--licenses` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create#--licenses). For more information on license codes, in the [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details) page, see the **License** tab in the section applicable to your operating system.
         
         gcloud compute images create IMAGE_NAME --source-uri gs://BUCKET_NAME/compressed-image.tar.gz
         

Replace the following:

     * IMAGE_NAME: the name of the image that you imported.
     * BUCKET_NAME: the name of the bucket that the imported image is stored in.



The image is now included in the list of custom images. You can create a VM using this imported image. If there is a boot failure, verify and ensure that you have configured the bootloader correctly.
    
    
    gcloud compute images list --no-standard-images
    
    
    
    NAME                                            PROJECT                  FAMILY                    DEPRECATED  STATUS
    [IMAGE_NAME]                                    [PROJECT_ID]                                                   READY

## Test the imported image to ensure it works

Confirm that the imported image works as expected. Create a VM with a boot disk that uses the imported image.

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. In the **Boot disk** section, click **Change** , and then do the following:

     1. Select the **Custom images** tab.
     2. To select the image project, click **Select a project** , and then do the following: 
        1. Select the project that contains the image.
        2. Click **Open**.
     3. In the **Image** list, click the image that you imported.
     4. Select the type and size of your boot disk.
     5. To confirm your boot disk options, click **Select**.
  3. Click **Create**.




###  gcloud 
    
    
    gcloud compute instances create VM_NAME --zone ZONE --image IMAGE_NAME

Replace the following:

  * VM_NAME: a unique name for your VM.
  * ZONE: the zone where you created the standalone disk.
  * IMAGE_NAME: the name of the image that you imported.



After you create the VM, confirm that it booted properly. Check the serial port output:

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page. 

[Go to Instances](https://console.cloud.google.com/compute/instances)

  2. On the list of VMs, click the name of the VM that you created from the imported image. The VM details page opens.
  3. In the **Logs** section, click the appropriate serial port to expand and view the serial port output for this VM.



If the VM stopped at `Booting from Hard Disk 0...`, you must [troubleshoot](https://docs.cloud.google.com/compute/docs/troubleshooting/vm-startup#persistent_book_disks) the issues from within the Compute Engine environment, or you can reconfigure the boot disk on your original system and repeat the import process.

###  gcloud 
    
    
    gcloud compute instances get-serial-port-output VM_NAME

If the VM stopped at `Booting from Hard Disk 0...`, you must [troubleshoot](https://docs.cloud.google.com/compute/docs/troubleshooting/vm-startup#persistent_book_disks) the issues from within the Compute Engine environment or you can reconfigure the boot disk on your original system and repeat the import process.

You can also test the VM by connecting to it. Connect to the VM through one of the following options:

  * SSH: If the VM had a functional SSH configuration, you can connect to the VM using SSH and your private key. You can find the VM instance IP address on the [**VM instances** page](https://console.cloud.google.com/compute/instances).
  * Serial Console: If you need to sign in to the VM directly without SSH, you can enable the [Serial Console](https://docs.cloud.google.com/compute/docs/instances/interacting-with-serial-console) and sign in with a username and password.



## What's next

  * [Configure the disk](https://docs.cloud.google.com/compute/docs/import/configuring-imported-images) so that your image can take advantage of features within the Compute Engine environment.
  * After your image is ready for production, [create a final version](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images) of that custom image and [include the image in an image family](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#setting_families) so that you can manage updated versions of the custom image.
  * Some imports might fail because of boot disk issues. For more information, see [Troubleshooting boot disks](https://docs.cloud.google.com/compute/docs/troubleshooting/vm-startup#persistent_book_disks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
