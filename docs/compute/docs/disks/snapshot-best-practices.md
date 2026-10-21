---
url: https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices/
title: Best practices for Compute Engine disk snapshots \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:53:19.460176+00:00
---

# Best practices for Compute Engine disk snapshots  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for Compute Engine disk snapshots Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

You can create Persistent Disk and Google Cloud Hyperdisk snapshots at any time, but you can create snapshots more quickly and with greater reliability if you use the following best practices.

## Security considerations

To prevent unintended privilege escalation, ensure that you only grant snapshot-related [Identity and Access Management (IAM) permissions](https://docs.cloud.google.com/iam/docs/overview#permissions) to principals that you trust to read and restore snapshot or instant snapshot data. The following permissions enable users to read and restore data from snapshots or instant snapshots:

  * `compute.snapshots.useReadOnly`
  * `compute.instantSnapshots.useReadOnly`



Any principal that has one of the preceding permissions can restore data from snapshots or instant snapshots in your project to a project that they control, including a project that is in a different organization. For example, if a bad actor were to obtain a snapshot IAM role in your project, they could restore the snapshot in their personal project and access the data contained in the snapshot.

To learn how to check the permissions a principal has, see [Determine which principals have certain roles or permissions](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#principal-query-all).

## Preparing for consistent snapshots

If you create a snapshot of your Persistent Disk or Hyperdisk while your application is running, the snapshot might not capture pending writes that are in transit from memory to disk. Because of these inconsistencies, the snapshot might not reflect the exact state of your application at the time you captured the snapshot. In this scenario, the snapshot is considered _crash consistent_ because it captures the state of the application as if the machine crashed at the time the snapshot was taken.

Optionally, you can pause the application, so that all application transactions complete and the system can flush all pending writes from memory to disk before the snapshot is captured. In this scenario, the snapshot is considered _application consistent_.

### Creating crash consistent snapshots

When you take a snapshot of a Persistent Disk or Hyperdisk volume, you don't need to take any additional steps to make your snapshot crash consistent. In particular, you don't need to pause your workload.

If your workload cannot tolerate a temporary pause, consider the following process for creating crash consistent snapshots:

  1. Capture a snapshot while applications are running, assuming there will be some application data inconsistencies.
  2. Verify that you can [restore](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot) your workload to an acceptable application state from the snapshot.
  3. Based on the previous step, either retain or delete the snapshot.



Crash-consistent snapshots will likely require replaying file system and application-level journals before use. Thus the quality of your snapshot depends on your application's ability to quickly recover from a crash-consistent state back to serving.

### Creating application consistent snapshots

Support for application consistent snapshots depends on the disk type and the operating system of the instance the disk is attached to, as follows.

  * **Instances using Hyperdisk** : Hyperdisk volumes don't support `guest-flush` or the Volume Shadow Copy Service (VSS). To create application consistent snapshots for Hyperdisk volumes, you must manually pause the application before you create the snapshot. For more information, see [Manually create application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#manual).

  * **Windows Server instances using Persistent Disk** : For disks that are attached to Windows Server instances, use [VSS snapshots](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot).

  * **Linux instances using Persistent Disk** : To achieve application consistency for snapshots of Persistent Disk volumes attached to Linux instances, create pre- and post-snapshot shell scripts to prepare your system for application consistency. Then create a snapshot with the `guest-flush` option enabled. This runs the pre- and post- scripts before and after the snapshot is captured. For instructions, see [Creating Linux application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots).




#### Manually create application consistent snapshots

In some scenarios, you might need to manually pause your applications to achieve application consistent snapshots.

For example, use this option if you require application consistency between multiple disks, or for Hyperdisk volumes. In this case, you must freeze all of the file systems on each disk and complete all of the snapshots for those disks before you resume your apps.

You don't need to stop your VMs. The application pause can involve, for example, freezing and unmounting your file system. After you manually pause your applications, resume your workloads only after the snapshot resource reaches the [`UPLOADING`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/snapshots/insert#body.request_body.FIELDS.status) status.

When you request a snapshot, check the status of the operation by calling the [`globalOperations.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations/get). The following table shows the relationship between the status of the snapshot operation and the status of the snapshot resource.

Operation status | Snapshot resource status  
---|---  
`PENDING` | No snapshot resource exists yet.  
`RUNNING` | `CREATING` or `UPLOADING`   
  
`CREATING`: Snapshot creation is not yet complete.   
`UPLOADING`: Snapshot has been created but is not yet saved to Cloud Storage.  
`DONE` | `FAILED` or `READY`.  
  
### Avoid temporary standard snapshots

To immediately create a copy of a disk in the same zone for verification or export, use [disk clones](https://docs.cloud.google.com/compute/docs/disks/clone-duplicate-disks) or [instant snapshots](https://docs.cloud.google.com/compute/docs/disks/instant-snapshots) instead of standard snapshots. Compared to disk clones and instant snapshots, standard snapshots have longer copy times for upload and download.

## Snapshot frequency limits

There are limits to how frequently you can take a snapshot of a disk.

### Creating snapshots from Persistent Disk or Hyperdisk

You can snapshot an individual disk at most 6 times every 60 minutes.

If the limit is exceeded, the operation fails and returns the following error:
    
    
    "code": "RESOURCE_OPERATION_RATE_EXCEEDED",
    "message": "Operation rate exceeded for resource 'projects/project-id/zones/zone-id/disks/disk-name'.
    Too frequent operations from the source resource."
    

This limit applies to the following operations:

  * [Creating snapshots of a Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#create_snapshots)
  * [Creating snapshots of a Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#create_hyperdisk_snapshots)
  * [Creating images from a Persistent Disk](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#create_image)
  * [Creating standard or archive snapshots from instant snapshots](https://docs.cloud.google.com/compute/docs/disks/convert-instant-snapshot)



This limit doesn't apply to the following operations:

  * [Create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots). Scheduled snapshots have separate [frequency considerations](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules#schedule_frequency) and don't contribute to the snapshot frequency limit.
  * [Manually importing boot disk images](https://docs.cloud.google.com/compute/docs/import/import-existing-image)



As a best practice, take a snapshot of the disk once per hour. Avoid taking snapshots more often than that. The easiest way to achieve this is to set up a snapshot schedule.

### Creating new zonal disks from snapshots

You can create a new zonal Persistent Disk or Hyperdisk from a given snapshot per target zone at most 6 times every 60 minutes. The target zone refers to the storage location of the new disk created from the snapshot. Google Cloud doesn't guarantee that you will be able to create disks from a snapshot at a rate faster than that, though you might be able to create disks more frequently if you haven't created any disks from the snapshot in the past hour.

Note that multiple snapshots of the same disks are considered distinct snapshots with respect to this frequency limit.

If this limit is exceeded, the operation fails and returns the following error:
    
    
    "code": "RESOURCE_OPERATION_RATE_EXCEEDED",
    "message": "Operation rate exceeded for resource 'projects/project-id/global/snapshots/snapshot-name'.
    Too frequent operations from the source resource."
    

This limit applies to the following operations:

  * [Creating new _zonal_ Persistent Disks from a snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-snapshot#create-disk-from-snapshot)



This limit _does not_ apply to the following operations:

  * Creating new _regional_ Persistent Disks from a snapshot.
  * Creating new zonal or regional Persistent Disks using an image as the source.



To create multiple disks from a snapshot, use the snapshot to create an image then create your disks from the image:

  1. [Create an image from the snapshot](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#create_image).
  2. [Create disks from the image](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks).



For non-boot disks, follow the instructions to [create persistent disks from the image](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) and use the following steps:

  * In the Google Cloud console, select **Image** as the disk **Source type**.
  * With the gcloud CLI, use the [`image` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create#--image).
  * If using REST, use the [`sourceImage` parameter](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/insert#body.request_body.FIELDS.source_image).



## Use existing snapshots as a baseline for subsequent snapshots

If you have existing snapshots of a disk (Persistent Disk or Hyperdisk), the system automatically uses them as a baseline for any subsequent snapshots that you create from that same disk.

  * Create a new snapshot from a disk before you delete the previous snapshot from that same disk. The system can create the new snapshot more quickly if it can use the previous snapshot and reads only the new or changed data from the disk.
  * Wait for new snapshots to finish before you take subsequent snapshots from the same disk. If you run two snapshots simultaneously on the same disk, they both start from the same baseline and duplicate effort. If you wait for the new snapshot to finish, any subsequent snapshots run more quickly because they only obtain the data that has changed since the last snapshot finished.

**Important:** Snapshots are [incremental](https://docs.cloud.google.com/compute/docs/disks/snapshots#incremental-snapshots) by default to avoid billing you for redundant data, to minimize use of storage space, and to decrease snapshot creation latency. However, to ensure the reliability of snapshot history, a snapshot might occasionally capture a full image of the disk.

## Schedule snapshots during off-peak hours

If you schedule regular snapshots for your disks (Persistent Disk or Hyperdisk), you can reduce the time that it takes to complete each snapshot by creating them during off-peak hours when possible.

  * Schedule automated snapshots during the business day in the zone where your disk is located. Snapshot creation typically peaks at the end of the business day.
  * Schedule automated snapshots early in the morning in the zone where your disk is located rather than immediately at midnight. Snapshot creation typically peaks at midnight.



## Organize your data on separate disks

If you create a snapshot of a disk (Persistent Disk or Hyperdisk), any data that you store on the disk is included in the snapshot. Larger amounts of data create larger snapshots, which cost more and take longer to create. To ensure that you create a snapshot of only the data you need, organize your data on separate disks.

  * Store critical data on a secondary, or data, disk rather than your boot disk. This lets you create a snapshot of your boot disks only when necessary or on a less frequent schedule.
  * If you create snapshots of your boot disks, store swap partitions, pagefiles, cache files, and non-critical logs on a separate disk. These files and partitions change frequently, and the snapshot process is likely to identify them as changed data that must be included in an incremental snapshot.
  * Reduce the number of snapshots that you need to create by keeping similar data together on one disk. Keep your operating system and volatile data separate from the data that you want to snapshot, but you don't need to distribute your critical data across multiple disks like you would for a physical machine. One large disk is able to achieve the same performance as multiple smaller disks of the same total size.



## Enable the `discard` option or run `fstrim` on your disk

On Linux instances, if you didn't format and mount your disks (Persistent Disk or Hyperdisk) with the discard option, run the `fstrim` command on the instance before you create a snapshot. The command removes blocks that the file system no longer needs, so that the system can create the snapshot more quickly and with a smaller size. To learn how to configure the discard option on your disks, see [Format and mount a non-boot disk on a Linux VM](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux).

## Create an image of a frequently used snapshot

If you are repeatedly using a snapshot in the same zone to create a disk (Persistent Disk or Hyperdisk), save networking costs by using the snapshot once and creating an image of that snapshot. Store this image and use it to create your disk and start a VM instance. For instructions, see [Creating a custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#creating_a_custom_image).

As a best practice, take a snapshot of the disk once per hour. Avoid taking snapshots more often than that. The easiest way to achieve this is to set up a [snapshot schedule](https://docs.cloud.google.com/compute/docs/disks/about-snapshot-schedules).

## Other best practices

  * Use [journaling file systems](https://en.wikipedia.org/wiki/Journaling_file_system) like `ext4` to reduce the risk that data is cached without actually being written to the persistent disk.
  * Create a snapshot of your data on a regular schedule to minimize data loss due to unexpected failure.



## What's next

  * Learn how to [create disk snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots).
  * Learn how to [view, list, share, and delete snapshots](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots).
  * Learn how to [create schedules for disk snapshots](https://docs.cloud.google.com/compute/docs/disks/scheduled-snapshots).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
