---
url: https://docs.cloud.google.com/compute/docs/disks/set-persistent-device-name-in-linux-vm/
title: Best practice: Use persistent device names on a Linux VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:32.108890+00:00
---

# Best practice: Use persistent device names on a Linux VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/set-persistent-device-name-in-linux-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practice: Use persistent device names on a Linux VM Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

This document describes how to use persistent device naming on your Linux VM.

For VMs that use a Linux operating system, device names, for example `/dev/sda`, might change after you perform procedures such as the following:

  * Starting and stopping a VM
  * Detaching and reattaching disks
  * Changing machine types



This device name change occurs because device names are assigned from an available range once a VM starts or a device is attached. Detaching a device or stopping the VM frees up the device name. When the device is reattached or the VM restarted a new device name is then assigned from the available range. The Linux kernel does not guarantee device ordering across reboots.

A device name change might cause any applications or scripts that depend on the original device name to not work properly or it might cause the VM to not boot after a restart.

It is recommended that you use persistent device naming when referencing disks and partitions on your Linux VMs to avoid this issue. You can also use [symlinks](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks).

## Before you begin

  * Review device management for your Linux operating system: 
    * [Using UUIDs with Ubuntu](https://help.ubuntu.com/community/UsingUUID)
    * [Red Hat Device Management](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/storage_administration_guide/persistent_naming)
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




## Device naming on Linux VMs

The Linux device names for the disks attached to your VM depend on the interface that you choose when creating the disks. When you use the `lsblk` operating system command to view your disk devices, it displays the prefix `nvme` for disks attached with the NVMe interface, and the prefix `sd` for disks attached with the SCSI interface.

The ordering of the disk numbers or NVMe controllers is not predictable or consistent across VMs restarts. On the first boot, a persistent disk might be `nvme0n1` (or `sda` for SCSI). On the second boot, the device name for the same persistent disk might be `nvme2n1` or `nvme0n3` (or `sdc` for SCSI).

When accessing attached disks, you should use the symbolic links created in `/dev/disk/by-id/` instead. These names persist across reboots. For more information about symlinks, see [Symbolic links for disks attached to a VM](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks).

### SCSI device names

The format of a SCSI-attached disk device is `sda` for the first attached disk. The disk partitions appear as `sda1`. Each additional disk uses a sequential letter, such as `sdb` and `sdc`. When `sdz` is reached, the next disks added have the names such as `sdaa`, `sdab`, and `sdac`, up to `sddx`.

### NVMe device names

The format of a NVMe-attached disk device in Linux operating systems is `nvmenumbernnamespace`. The `number` represents the NVMe disk controller number and namespace is an NVMe namespace ID that is assigned by the NVMe disk controller. For partitions, pn is appended to the device name, where n is a number, starting with 1, that denotes the _n_ th partition.

The controller number starts at `0`. A single NVMe disk attached to your compute instance has a device name of `nvme0n1`. Most machine types use a single NVMe disk controller. The NVMe device names are then `nvme0n1`, `nvme0n2`, `nvme0n3`, and so on.

Local SSD disks attached to [third generation machine series](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) or later instances have a separate NVMe controller for each disk. On these VMs, the Local SSD NVMe-attached device names look like `nvme0n1`, `nvme1n1`, and `nvme2n1`. The number of attached Local SSD disks depends on the machine type of your VM.

Compute instances based on third generation machine series or later use NVMe for both Persistent Disk and Google Cloud Hyperdisk, and also Local SSD disks. Each VM has 1 NVMe controller for Persistent Disk and Hyperdisk and 1 NVMe controller for each Local SSD disk. The Persistent Disk and Hyperdisk NVMe controller has a single NVMe namespace for all attached disks. So, a third generation machine series instance with one Persistent Disk and one Hyperdisk (each with 2 partitions), and 2 unformatted Local SSD disks uses the following device names:

  * `nvme0n1` \- Persistent Disk
  * `nvme0n1p1`
  * `nvme0n1p2`
  * `nvme0n2` \- Hyperdisk
  * `nvme0n2p1`
  * `nvme0n2p2`
  * `nvme1n1` \- first Local SSD
  * `nvme2n1` \- second Local SSD



## Use persistent device naming

To configure a persistent device name, you assign a mount point name for the disk device in the `fstab` file. There are three ways to configure a persistent device name.

  * By using a [label](https://tldp.org/HOWTO/Partition/labels.html). This option requires that the file system supports labels and that you add a label to the disk partitions.
  * By using a partition or disk [UUID](https://www.linux.com/news/what-uuids-can-do-you/). A UUID is generated when a disk is created with a partition table, and the UUID is unique per partition.
  * By using a persistent disk ID (`/dev/disk/by-id`) for Persistent Disk or Google Cloud Hyperdisk, or a _[symlink](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks)_ , that is based on the disk resource name.



We recommend using the partition UUID or the symlink for Linux VMs.

###  Partition UUID 

To find the UUID for a disk, perform the following steps:

  1. [Connect](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) to your VM.
  2. If you don't know the device name for the disk, you can find the disk device name using the symlink.
         
         ls -l /dev/disk/by-id/google-*
         

The output is similar to the following:
         
         lrwxrwxrwx 1 root root  9 Oct 23 15:58 /dev/disk/by-id/google-my-vm -> ../../sda
           lrwxrwxrwx 1 root root 10 Oct 23 15:58 /dev/disk/by-id/google-my-vm-part1 -> ../../sda1
           lrwxrwxrwx 1 root root 11 Oct 23 15:58 /dev/disk/by-id/google-my-vm-part15 -> ../../sda15
           lrwxrwxrwx 1 root root  9 Oct 23 15:58 /dev/disk/by-id/google-my-vm-app-data -> ../../nvme0n1
           

  3. Retrieve the UUID of the partition for the disk by running one of the following commands:

     * `blkid`
           
           sudo  blkid -s UUID
           

The output is similar to the following:
           
           /dev/sda1: UUID="4f570f2d-fffe-4c7d-8d8f-af347af7612a"
           /dev/sda15: UUID="E0B2-DFAF"
           /dev/nvme0n1: UUID="9e617251-6a92-45ff-ba40-700a9bdeb03e"
           

     * `ls -l`
           
           sudo ls -l /dev/disk/by-uuid/
           

The output is similar to the following:
           
           lrwxrwxrwx 1 root root 10 Sep 22 18:12 4f570f2d-fffe-4c7d-8d8f-af347af7612a -> ../../sda1
           lrwxrwxrwx 1 root root 13 Sep 22 18:15 9e617251-6a92-45ff-ba40-700a9bdeb03e -> ../../nvme0n1
           lrwxrwxrwx 1 root root 11 Sep 22 18:12 E0B2-DFAF -> ../../sda15
           

  4. Add an entry for the UUID for your device in the `/etc/fstab` file.
         
         UUID=9e617251-6a92-45ff-ba40-700a9bdeb03e /data ext4 defaults 0 0
         

In this example, `/data` is the mount point and `ext4` is the file system type.

  5. Validate that the device is mounted properly by running `mount -av`.
         
         sudo mount -av

If the device is successfully mounted, the output is similar to the following:
         
         /                           : ignored
         /boot/efi                : already mounted
         mount: /data does not contain SELinux labels.
         You just mounted a file system that supports labels which does not
         contain labels, onto an SELinux box. It is likely that confine
         applications will generate AVC messages and not be allowed access to
         this filesystem.  For more details see restorecon(8) and mount(8).
         /data                    : successfully mounted
         




###  Persistent disk ID 

To find the disk device name by using the persistent disk ID, or symlink, complete the following steps:

  1. [Connect](https://docs.cloud.google.com/compute/docs/connect/standard-ssh) to your VM.
  2. Retrieve the ID on the disk by running the following command:
         
         sudo  ls -lh /dev/disk/by-id/google-*

The output is similar to the following:
         
         lrwxrwxrwx. 1 root root  9 May 16 17:34 google-disk-2 -> ../../sdb
         lrwxrwxrwx. 1 root root  9 May 16 09:09 google-persistent-disk-0 -> ../../sda
         lrwxrwxrwx. 1 root root 10 May 16 09:09 google-persistent-disk-0-part1 -> ../../sda1
         lrwxrwxrwx. 1 root root 10 May 16 09:09 google-persistent-disk-0-part2 -> ../../sda2
         

For `NVME` disks, the output is similar to the following:
         
         lrwxrwxrwx 1 root root 13 Jun  1 10:27 google-disk-3 -> ../../nvme0n2
         lrwxrwxrwx 1 root root 13 Jun  1 10:25 google-t2a -> ../../nvme0n1
         lrwxrwxrwx 1 root root 15 Jun  1 10:25 google-t2a-part1 -> ../../nvme0n1p1
         lrwxrwxrwx 1 root root 16 Jun  1 10:25 google-t2a-part15 -> ../../nvme0n1p15
         

  3. Add the symlink to the `/etc/fstab` file.
         
         /dev/disk/by-id/google-disk-2 /data ext4 defaults 0 0
         

**Note:** In this example, `/data` is the mount point and `ext4` is the file system type. 
  4. Validate that the device is mounted properly by running `mount -av`.
         
         sudo mount -av

If the device is successfully mounted, the output is similar to the following:
         
         /                           : ignored
         /boot/efi                : already mounted
         mount: /data does not contain SELinux labels.
         You just mounted a file system that supports labels which does
         not contain labels, onto an SELinux box. It is likely that confine
         applications will generate AVC messages and not be allowed access to this
         file system.  For more details see restorecon(8) and mount(8).
         /data                    : successfully mounted
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
