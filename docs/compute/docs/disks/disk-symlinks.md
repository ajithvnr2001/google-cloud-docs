---
url: https://docs.cloud.google.com/compute/docs/disks/disk-symlinks/
title: Use symbolic links to access disks attached to a Linux compute instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:58.412027+00:00
---

# Use symbolic links to access disks attached to a Linux compute instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/disk-symlinks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Use symbolic links to access disks attached to a Linux compute instance Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

When you attach a disk to a Compute Engine instance that uses a Linux OS, Google Cloud automatically creates a symbolic link (symlink) for the disk. To access Persistent Disk volumes or Local SSD disks in your compute instance, use the symlinks. These symlinks are predictable and remain consistent across reboots. Google Cloud creates symlinks for all disks attached to a compute instance in `/dev/disk/by-id`.

This document explains how to identify the correct symlinks for the disks attached to a Linux compute instance.

## Format of symbolic links

Symlinks are created in `/dev/disk/by-id` when a disk is attached to the compute instance, either during or after instance creation. The symlink names are created as follows:

**Persistent Disk and Google Cloud Hyperdisk**

The symlinks are created using the following rules:

  * If you specified a custom device name when you created the disk: `google-DEVICE_NAME`
  * If you didn't specify a custom device name when you created the disk: 
    * Boot disk: `google-INSTANCE_NAME`
    * Non-boot disk: `google-DISK_NAME`



After you format the disk, the symlink is appended with `-partN`, where N is the partition number, for example `google-data-disk-part1`.

**Local SSD disks**

Local SSD symlinks have different formats depending on the disk interface.

  * SCSI: 
    * If you specified a custom device name when you created the disk: `google-DEVICE_NAME`
    * If you didn't specify a custom device name when you created the disk: `google-local-ssd-N`, where N is the Local SSD disk number, starting from 0.
  * NVMe: The symlinks are named `google-local-nvme-ssd-N`, where N is the SSD number, starting from 0.



After you format a Local SSD disk, the symlink is appended with `-partN`, where N is the partition number, for example, `google-local-nvme-ssd-0-part1`.

**Device symlinks**

Compute Engine creates additional symlinks in the directory based on the disk type and interface, for example `scsi-0Google_PersistentDisk_DEVICE_NAME`. These links perform the same function as the symlinks mentioned previously.

**Example 1: C3 instance with attached Local SSD**

Assume you created a compute instance with the following properties:

  * Instance name: `instance-1`
  * Machine series: C3
  * Disk interface type: NVMe for both Persistent Disk and Local SSD
  * Additional disks: none
  * Attached Local SSD disks: 2
  * Custom device names used: none



Compute Engine creates the following symlinks for that compute instance:
    
    
    ls -l /dev/disk/by-id/google-*
    
    
    
    google-instance-1 -> ../../nvme2n1
    google-instance-1-part1 -> ../../nvme2n1p1
    google-instance-1-part14 -> ../../nvme2n1p14
    google-instance-1-part15 -> ../../nvme2n1p15
    google-local-nvme-ssd-0 -> ../../nvme0n1
    google-local-nvme-ssd-1 -> ../../nvme1n1
    

In this example, the Persistent Disk boot disk symlink is `google-instance-1`, which is based on the instance name. The boot disk is formatted and has the operating system installed on it. The boot disk has 3 partitions: part1, part14, and part 15\. The attached Local SSD disks are not formatted, so only a single symlink was created for each Local SSD disk.

**Example 2: N2 instance with attached NVMe Local SSD and extra Persistent Disk**

Assume you created a compute instance with the following properties:

  * Instance name: `instance-2`
  * Machine series: N2
  * Disk interface type: SCSI for Persistent Disk and NVMe for Local SSD
  * Additional disks: 1 Persistent Disk named `extra-scsi-disk`
  * Attached Local SSD disks: 2
  * Custom device names used: none



The following symlinks are created for that compute instance:
    
    
    ls -l /dev/disk/by-id/google-*
    
    
    
    google-extra-scsi-disk -> ../../sdb
    google-instance-2 -> ../../sda
    google-instance-2-part1 -> ../../sda1
    google-instance-2-part14 -> ../../sda14
    google-instance-2-part15 -> ../../sda15
    google-local-nvme-ssd-0 -> ../../nvme0n1
    google-local-nvme-ssd-0-part1 -> ../../nvme0n1p1
    google-local-nvme-ssd-1 -> ../../nvme0n2
    

In this example, the Persistent Disk boot disk symlink is `google-instance-2`, which is based on the instance name. The boot disk is formatted and has the OS image installed on it. The boot disk has 3 partitions: part1, part14, and part 15. The first Local SSD disk is also partitioned, with a single partition, so there is an additional symlink created for that disk partition. The additional Persistent Disk added to the compute instance has the symlink `google-extra-scsi-disk`, which is based the disk name. The extra Persistent Disk and second Local SSD disk are not formatted, so only a single symlink is listed for those disks.

## What's next

  * Learn how to [use persistent device names](https://docs.cloud.google.com/compute/docs/disks/set-persistent-device-name-in-linux-vm).
  * Format and mount your new disks on: 
    * [Linux instances](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux).
    * [Windows instances](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-windows).
  * Learn about benchmarking disk performance: 
    * [for Linux](https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-linux).
    * [for Windows](https://docs.cloud.google.com/compute/docs/disks/benchmarking-pd-performance-windows).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
