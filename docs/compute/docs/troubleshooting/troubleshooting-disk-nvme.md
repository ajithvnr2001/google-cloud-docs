---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-disk-nvme/
title: Troubleshooting NVMe disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:47:13.229378+00:00
---

# Troubleshooting NVMe disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-disk-nvme/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting NVMe disks Stay organized with collections  Save and categorize content based on your preferences. 

This document lists errors that you might encounter when using disks with the nonvolatile memory express (NVMe) interface.

You can use the NVMe interface for Local SSDs and persistent disks (Persistent Disk or Google Cloud Hyperdisk). Only the most recent machine series, such as Tau T2A, M3, C3, C3D, and H3 use the [NVMe](http://wikipedia.org/wiki/NVM_Express) interface for Persistent Disk. Confidential VMs also use NVMe for Persistent Disk. All other Compute Engine machine series use the [SCSI](http://wikipedia.org/wiki/SCSI) disk interface for persistent disks.

## I/O operation timeout error

If you are encountering I/O timeout errors, latency could be exceeding the default timeout parameter for I/O operations submitted to NVMe devices.

**Error message** : 
    
    
    [1369407.045521] nvme nvme0: I/O 252 QID 2 timeout, aborting
    [1369407.050941] nvme nvme0: I/O 253 QID 2 timeout, aborting
    [1369407.056354] nvme nvme0: I/O 254 QID 2 timeout, aborting
    [1369407.061766] nvme nvme0: I/O 255 QID 2 timeout, aborting
    [1369407.067168] nvme nvme0: I/O 256 QID 2 timeout, aborting
    [1369407.072583] nvme nvme0: I/O 257 QID 2 timeout, aborting
    [1369407.077987] nvme nvme0: I/O 258 QID 2 timeout, aborting
    [1369407.083395] nvme nvme0: I/O 259 QID 2 timeout, aborting
    [1369407.088802] nvme nvme0: I/O 260 QID 2 timeout, aborting
    ...
    

**Resolution** :

To resolve this issue, increase the value of the timeout parameter.

**Note:** Most of the operating system images provided by Google already include this change.

  1. View the current value of the timeout parameter.

     1. Determine which NVMe controller is used by the persistent disk or Local SSD volume. 
            
            ls -l /dev/disk/by-id
            

     2. Display the `io_timeout` setting, specified in seconds, for the disk. 
            
            cat /sys/class/nvme/CONTROLLER_ID/NAMESPACE/queue/io_timeout
            

Replace the following: 
        * `CONTROLLER_ID`: the ID of the NVMe disk controller, for example, `nvme1`
        * `NAMESPACE`: the namespace of the NVMe disk, for example, `nvme1n1`

If you only have a single disk that uses NVMe, then use the command: 
    
    cat /sys/class/nvme/nvme0/nvme0n1/queue/io_timeout
    

  2. To increase the timeout parameter for I/O operations submitted to NVMe devices, add the following line to the `/lib/udev/rules.d/65-gce-disk-naming.rules` file, and then restart the VM:
         
         KERNEL=="nvme*n*", ENV{DEVTYPE}=="disk", ATTRS{model}=="nvme_card-pd", ATTR{queue/io_timeout}="4294967295"
         




## Detached disks still appear in the operating system of a compute instance

On VMs that use Linux kernel version 6.0 to 6.2, operations involving the Compute Engine API method `instances.detachDisk` or the `gcloud compute instances detach-disk` command might not work as expected. The Google Cloud console shows the device as removed, the compute instance metadata (`compute disks describe` command) shows the device as removed, but the device mount point and any symlinks created by udev rules are still visible in the guest operating system.

**Error message** :

Attempting to read from the detached disk on the VM results in I/O errors:
    
    
    sudo head /dev/nvme0n3
    
    head: error reading '/dev/nvme0n3': Input/output error
    

**Issue** :

Operating system images that use a Linux 6.0-6.2 kernel but don't include a backport of a [NVMe fix](https://github.com/torvalds/linux/commit/0dd6fff2aad4e35633fef1ea72838bec5b47559a) fail to recognize when an NVMe disk is detached.

**Resolution** :

Reboot the VM to complete the process of removing the disk.

To avoid this issue, use an operating system with a Linux kernel version that doesn't have this problem:

  * 5.19 or older
  * 6.3 or newer



You can use the `uname -r` command in the guest OS to view the Linux kernel version.

## What's next?

  * Learn about [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks).
  * Learn about [Local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd).
  * [Configure disks to meet performance requirements](https://docs.cloud.google.com/compute/docs/disks/performance).
  * Learn about [symlinks](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
