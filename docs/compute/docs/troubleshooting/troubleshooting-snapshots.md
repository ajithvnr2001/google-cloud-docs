---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-snapshots/
title: Troubleshooting standard disk snapshots \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:48.766062+00:00
---

# Troubleshooting standard disk snapshots  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-snapshots/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting standard disk snapshots Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This page shows you how to resolve issues with [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots).

## VSS snapshot errors

This section lists issues that you might encounter when backing up your disks with [Windows VSS snapshots](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot), and provides suggestions for how to fix them.

### VSS snapshot failed

The following error might occur when you attempt to create a VSS snapshot of a disk:
    
    
    Guest Consistent Snapshot failed (Detail: Failure within guest).
    Verify you are running the latest image version and agent.
    

This error can occur for several reasons. Some of the most common causes of this error are:

  * **The VM is running an outdated version of the guest environment.**

To resolve this issue, [install the latest version of the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#update-guest) and then reattempt to create the snapshot.

  * **Multiple disks are attached to the same snapshot schedule.** When multiple disks are attached to the same snapshot schedule, Compute Engine starts each snapshot at the same time. In some cases, this might cause snapshots to fail.

To resolve this issue, [create multiple snapshot schedules](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots#create_snapshot_schedule) that run at different times, and spread your disks across those schedules.




### Failure to boot VM after creating VSS snapshot of a boot disk

When you create a VSS snapshot, Windows Server marks the source disk as read-only. When you create a new persistent disk from the VSS snapshot, that disk is also set to read-only mode, which might cause issues.

For example, if you create a VM instance with a new boot disk that is based on a VSS snapshot of a boot disk, the read-only flag on the new boot disk prevents the VM instance from booting correctly. In this scenario, the VM might fail to boot with the following errors:

  * Failed to open disk
        

  * Status: 0xC0000225 Info: The boot selection failed because a required device is inaccessible.
        

  * ERROR: (gcloud.beta.compute.instances.create) Could not fetch resource:
         - Internal error. Please try again or contact Google Support.
        

  * No startup scripts to run.
        




To resolve these errors, remove the read-only flag from any new disk that you create from a VSS snapshot. For more information, see [Marking your disk as available for read and write](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#read-only).

## Snapshot frequency errors

This section lists issues that you might encounter when creating frequent disk snapshots and provides suggestions for how to fix them.

### Creating snapshots from persistent disks

If you try to snapshot your disk more than once during a ten minute period, or if you issue more than six burst snapshot requests in 60 minutes, you see the following error:
    
    
    "code": "RESOURCE_OPERATION_RATE_EXCEEDED",
    "message": "Operation rate exceeded for resource 'projects/project-id/zones/zone-id/disks/disk-name'. Too frequent operations from the source resource."
    

To resolve this issue, take a snapshot of the disk at most once per hour as a best practice. Avoid taking snapshots more often than that. The easiest way to achieve this is to set up a snapshot schedule. For more information, see [Best practices for creating snapshots from persistent disks](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#freq-create-snaps).

### Creating new zonal persistent disks from snapshots

If you try to create a new zonal persistent disk from the same snapshot in the same zone, more than six times in 60 minutes, you see the following error:
    
    
    "code": "RESOURCE_OPERATION_RATE_EXCEEDED",
    "message": "Operation rate exceeded for resource 'projects/project-id/zones/zone-id/disks/disk-name'. Too frequent operations from the source resource."
    

To resolve this issue, create an image from the snapshot instead of repeatedly restoring the snapshot in the same zone to create many persistent disks.

Then, use the image to create new disks. For more information, see [Best practices for creating new zonal persistent disks from snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#freq-create-disks).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
