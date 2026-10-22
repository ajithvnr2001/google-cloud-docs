---
url: https://docs.cloud.google.com/compute/docs/instances/sql-server/adding-sql-server-license-to-linux/
title: Add a SQL Server license to an existing Linux server \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:52.585285+00:00
---

# Add a SQL Server license to an existing Linux server  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/sql-server/adding-sql-server-license-to-linux/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Add a SQL Server license to an existing Linux server Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

Compute Engine lets you install SQL Server on Linux virtual machines (VM) instances and use pay-as-you-go (PAYG) licenses. This document describes how to use SQL Server on a Linux VM by doing the following:

  1. Add SQL Server license metadata to a boot disk
  2. Install SQL Server on Linux



## Billing

After adding a license string to the Linux VM's boot disk, you are billed according to the pricing of [SQL Server images](https://docs.cloud.google.com/compute/disks-image-pricing#sql_server_pricing).

## Limitations

  * You can only install SQL Server on the following Linux distributions:

    * Red Hat Enterprise Linux (RHEL)
    * SUSE Linux Enterprise Server (SLES)
    * Ubuntu



## Add a SQL Server license to a Linux Server

SQL Server license metadata on a boot disk allows Google Cloud to accurately track, bill, and report on SQL Server license usage. This metadata is required when using PAYG SQL Server licenses. Add a SQL Server license to an existing boot disk using the following procedure:

**Caution:** After you add a license to a VM, you cannot remove the license from the VM.

  1. Identify the license you want to add to a VM. For SQL Server, the license needs to match both the version and edition you want to run. For the list of valid SQL Server license strings, see the **License strings** tab in the [operating system details for SQL Server](https://docs.cloud.google.com/compute/docs/images/os-details#sql_server) document.

  2. Stop the VM:
         
         gcloud compute instances stop VM_NAME
         

Replace `VM_NAME` with the name of the VM instance to stop.

  3. Identify the boot disk:
         
         gcloud compute instances describe VM_NAME
         

Replace `VM_NAME` with the name of the VM.

  4. Verify that the output is similar to the following:
         
         disks:
         - autoDelete: true
           boot: true
           deviceName: BOOT_DISK_NAME
           diskSizeGb: '20'
           guestOsFeatures:
           - type: UEFI_COMPATIBLE
           index: 0
           interface: SCSI
           kind: compute#attachedDisk
           licenses:
           - BOOT_DISK_LICENSE_STRING
           mode: READ_WRITE
           source: https://www.googleapis.com/compute/v1/projects/PROJECT_NAME/zones/ZONE/disks/BOOT_DISK_NAME
           type: PERSISTENT
         

  5. Detach the boot disk:
         
         gcloud compute instances detach-disk VM_NAME --disk=BOOT_DISK_NAME
         

Replace the following:

     * `VM_NAME`: the name of the VM
     * `BOOT_DISK_NAME`: the name of the boot disk
  6. Clone the boot disk and add the additional license:
         
         gcloud compute disks create CLONED_BOOT_DISK_NAME \
           --licenses=SQL_SERVER_LICENSE \
           --source-disk=BOOT_DISK_NAME \
           --source-disk-zone=BOOT_DISK_ZONE \
           --zone=CLONED_BOOT_DISK_ZONE
         

Replace the following:

     * `CLONED_BOOT_DISK_NAME`: the name you want to give the cloned book disk
     * `SQL_SERVER_LICENSE`: the SQL Server license you want to add to the boot disk
     * `BOOT_DISK_NAME`: the name of the source boot disk that you want to clone
     * `BOOT_DISK_ZONE`: the zone of the source boot disk
     * `CLONED_BOOT_DISK_ZONE`: the zone in which you want to create the cloned boot disk
  7. Verify that the new disk has the correct license:
         
         gcloud compute disks describe CLONED_BOOT_DISK_NAME \
           --zone=CLONED_BOOT_DISK_ZONE
         

Replace the following:

     * `CLONED_BOOT_DISK_NAME`: the name of the cloned book disk
     * `CLONED_BOOT_DISK_ZONE`: the zone of the cloned boot disk
  8. Attach the new disk as the boot disk for the VM instance:
         
         gcloud compute instances attach-disk VM_NAME \
           --disk=CLONED_BOOT_DISK_NAME
           --boot
         

Replace the following:

     * `VM_NAME`: the name of the VM instance to which you want to attach the cloned boot disk
     * `CLONED_BOOT_DISK_NAME`: the name of the cloned book disk
  9. Verify that the VM's boot disk is the new cloned disk with SQL Server licensing.
         
         gcloud compute instances describe VM_NAME
         

Replace `VM_NAME` with the name of the VM.

  10. Start the VM instance.
         
         gcloud compute instances start VM_NAME
         

Replace `VM_NAME` with the name of the VM.

  11. (Optional) When you are sure that you don't want to revert back to the earlier boot disk, you can delete the disk.
         
         gcloud compute disks delete BOOT_DISK_NAME \
           --zone=BOOT_DISK_ZONE
         

Replace the following:

     * `BOOT_DISK_NAME`: the name of the boot disk that you want to delete
     * `BOOT_DISK_ZONE`: the zone of the boot disk



## Install SQL Server on Linux

For guidance on installing, updating, and uninstalling SQL Server on Linux, see [Installation guidance for SQL Server on Linux](https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-setup?view=sql-server-ver16).

## What's next

  * [Learn about licenses](https://docs.cloud.google.com/compute/docs/licenses/about)

  * [View the SQL Server tutorials](https://docs.cloud.google.com/compute/docs/tutorials#sql-server)

  * [View the supported editions of SQL Server](https://docs.cloud.google.com/compute/docs/images/os-details#sql_server)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
