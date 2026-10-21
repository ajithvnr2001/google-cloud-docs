---
url: https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot/
title: Create a Windows application consistent disk snapshot \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:28:22.703148+00:00
---

# Create a Windows application consistent disk snapshot  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a Windows application consistent disk snapshot Stay organized with collections  Save and categorize content based on your preferences. 

Windows 

In Compute Engine, you can use [standard snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots) to back up your disk data. Because snapshots are incremental, you can create them with higher performance and lower total storage charges compared to creating complete disk images.

**Application consistent** snapshots capture the state of application data at the time of backup with all application transactions completed and all pending writes flushed to the disk. On Windows virtual machine (VM) instances, you use the Volume Shadow Copy Service (VSS) to create application consistent snapshots without first stopping the instance or detaching the disk from your VM.

**Caution:** If you have enabled BitLocker on a boot disk that is based on a [Shielded VM](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm) image, you can restore a snapshot of that boot disk to another disk, but you can't decrypt the restored instance. This is because the vTPM containing the BitLocker keys is only available to the VM that originated the snapshot. For more information, see [Using BitLocker with Shielded VM images](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#using-bitlocker).

## Before you begin

  * [Create a Windows instance](https://docs.cloud.google.com/compute/docs/instances/windows/creating-managing-windows-instances).
  * Review the [best practices for creating snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices).
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

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles and permissions

To get the permissions that you need to create a Windows VSS snapshot, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create a Windows VSS snapshot. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create a Windows VSS snapshot:

  * `compute.snapshots.create` on the project
  * `compute.disks.createSnapshot` on the disk



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Supported disk types

You can create VSS snapshots for Persistent Disk volumes attached to Windows instances.

Hyperdisk volumes don't support `guest-flush` or (VSS). To create application consistent snapshots for Hyperdisk volumes, you must manually pause the application before you create the snapshot as described in Create a snapshot without using VSS.

## Limitations

Disk snapshots on Windows have the following limitations:

  * VSS snapshots work only on Windows instances with image version `v20160810` and newer. For instances with older images, create a snapshot without using VSS.
  * The attached disk must use an NTFS, exFAT, or ReFS file system.
  * VSS snapshots help to preserve your data only if you are running VSS-aware applications that can coordinate to create a consistent backup of your data.
  * If the VSS snapshot operation does not complete within 300 seconds, the snapshot fails with a timeout error.
  * VSS snapshots aren't supported for Hyperdisk volumes. You must Create a snapshot without using VSS.

**Important:** When you create a VSS snapshot, Windows Server marks the volume in the snapshot as read-only. Any disks that you create from the VSS snapshot are also in read-only mode. For more information about how to work around this restriction, see Create a writable disk from a VSS snapshot.

## Create a Windows VSS snapshot

You can create Volume Shadow Copy Service (VSS) snapshots without having to stop the instance or detach the disk from your VM. VSS snapshots are intended for backup and recovery purposes on systems with VSS-aware apps.

VSS snapshots are the same price as normal Persistent Disk or Hyperdisk snapshots, and charge only for the [total size of the snapshot](https://docs.cloud.google.com/compute/disks-image-pricing#persistent_disk_snapshots).

### Create the snapshot

**Caution:** If you try to create a snapshot from a disk and the snapshot creation process fails, you won't be able to delete the original disk until you capture a clean snapshot. This failsafe helps to prevent the accidental deletion of source data in the event of an unsuccessful backup. 

###  Console 

  1. Go to the **Create a Snapshot** page in the Google Cloud console.

[Go to the Create a Snapshot page](https://console.cloud.google.com/compute/snapshotsAdd)
  2. Enter a snapshot **Name**.
  3. Select a **Snapshot type**. The default is a `STANDARD` snapshot, which is the best option for long-term back up and disaster recovery.

Choose **Archive snapshot** for more cost-efficient data retention.

  4. Optional: Enter a **Description** of the snapshot.
  5. Under **Source disk** , select the existing disk that you want to create a snapshot of.
  6. In the **Location** section, [choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location).

The predefined or customized default location defined in your snapshot settings is automatically selected. Optionally, you can override the snapshot settings and store your snapshots in a custom storage location by doing the following:

     1. Choose the type of storage location that you want for your snapshot.

        * Choose [**Multi-regional**](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) for higher availability at a higher cost.
        * Choose [**Regional snapshots**](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) for more control over the physical location of your data at a lower cost.
     2. In the **Select location** field, select the specific region or multi-region that you want to use. To use the region or multi-region that is closest to your source disk, select **Based on disk's location**. 
  7. Check the **Enable application consistent snapshot** option.
  8. Click **Create** to create the snapshot.



###  gcloud 

To create a VSS snapshot, use the [`gcloud compute snapshots create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create) and include the `--guest-flush` flag.

You can create your snapshot in the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). 

  * To create a snapshot in the predefined or customized default location configured in your snapshot settings, use the [`gcloud compute snapshots create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/snapshots/create).
        
        gcloud compute snapshots create SNAPSHOT_NAME \
            --source-disk-zone=SOURCE_ZONE \
            --source-disk=SOURCE_DISK_NAME \
            --snapshot-type=SNAPSHOT_TYPE \
            --guest-flush
        

  * Alternatively, to override the snapshot settings and create a snapshot in a custom storage location, include the `--storage-location` flag to indicate where to store your snapshot.
        
        gcloud compute snapshots create SNAPSHOT_NAME \
            --source-disk-zone=SOURCE_ZONE \
            --source-disk=SOURCE_DISK_NAME \
            --snapshot-type=SNAPSHOT_TYPE \
            --storage-location=STORAGE_LOCATION \
            --guest-flush
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regionally scoped snapshot in an allowed region, include the `--region` flag to indicate where to create your snapshot.
        
        gcloud beta compute snapshots create SNAPSHOT_NAME \
            --region=SNAPSHOT_SCOPE_REGION
            --source-disk=SOURCE_DISK_NAME \
            --source-disk-zone=SOURCE_ZONE \
            --snapshot-type=SNAPSHOT_TYPE
        




Replace the following:

  * SNAPSHOT_NAME: A name for the snapshot.
  * SOURCE_ZONE: The zone of the source disk. 
  * SOURCE_DISK_NAME: The name of the disk volume from which you want to create a snapshot. 
  * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a `STANDARD` snapshot is created.
  * STORAGE_LOCATION: Optional: For globally scoped snapshots, the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `--storage-location` parameter only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * SNAPSHOT_SCOPE_REGION: Optional: For regionally scoped snapshots, the region that the snapshot is scoped to. If you include this parameter, you can't use the `--storage-location` parameter. The STORAGE_LOCATION is automatically set to the SNAPSHOT_SCOPE_REGION.


**Note:** Google recommends using the `gcloud compute snapshots create` command instead of the [`gcloud compute disks snapshot` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/snapshot) because it supports more features, such as creating snapshots in a project different from the source disk project. 

To create a VSS snapshot of a regional Persistent Disk, in the previous examples replace `--source-disk-zone=` with `--source-disk-region=`, and specify the region where your regional Persistent Disk is located.

The Google Cloud CLI waits until the operation returns a status of `READY`, `FAILED`, or reaches the maximum timeout and returns the last known details of the snapshot.

###  REST 

When creating a snapshot, to indicate that you want to create a VSS snapshot, include the `guestFlush` property in the request body for your `POST` request to the [`compute.snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/snapshots/insert).

You can create your snapshot in the storage location policy defined by your [snapshot settings](https://docs.cloud.google.com/compute/docs/disks/snapshot-settings) or using an alternative storage location of your choice. For more information, see [Choose your snapshot storage location](https://docs.cloud.google.com/compute/docs/disks/snapshots#selecting_a_storage_location). 

  * To create a snapshot in the predefined or customized default location configured in your snapshot settings, make a `POST` request to the [`snapshots.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/beta/snapshots/insert):
        
        POST https://compute.googleapis.com/compute/beta/projects/DESTINATION_PROJECT_ID/global/snapshots
        {
          "name": "SNAPSHOT_NAME",
          "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
          "snapshotType": "SNAPSHOT_TYPE",
          "guestFlush": true,
        }
        

  * Alternatively, to override the snapshot settings and create a snapshot in a custom storage location, make a `POST` request to the `snapshots.insert` method and include the `storageLocations` property in your request:
        
        POST https://compute.googleapis.com/compute/beta/projects/DESTINATION_PROJECT_ID/global/snapshots
        {
          "name": "SNAPSHOT_NAME",
          "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
          "snapshotType": "SNAPSHOT_TYPE",
          "storageLocations": [
              "STORAGE_LOCATION"
          ],
          "guestFlush": true,
        }
        

  * ([Preview](https://cloud.google.com/products/#product-launch-stages)) To create a regionally scoped snapshot in an allowed region, make a `POST` request to the `snapshots.insert` method and define the creation region:
        
        POST https://compute.googleapis.com/compute/beta/projects/DESTINATION_PROJECT_ID/regions/SNAPSHOT_SCOPE_REGION/snapshots
        {
            "name": "SNAPSHOT_NAME",
            "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
            "snapshotType": "SNAPSHOT_TYPE"
        }
        




Replace the following:

  * DESTINATION_PROJECT_ID: The ID of project in which you want to create the snapshot.
  * SNAPSHOT_NAME: A name for the snapshot.
  * SOURCE_PROJECT_ID: The ID of the source disk project.
  * SOURCE_ZONE: The zone of the source disk. 
  * SOURCE_DISK_NAME: The name of the disk from which you want to create a snapshot. 
  * SNAPSHOT_TYPE: The snapshot type, either **STANDARD** or **ARCHIVE**. If a snapshot type is not specified, a `STANDARD` snapshot is created.
  * STORAGE_LOCATION: Optional: For globally scoped snapshots, the [Cloud Storage multi-region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-mr) or the [Cloud Storage region](https://docs.cloud.google.com/storage/docs/bucket-locations#location-r) where you want to store your snapshot. You can specify only one storage location.

Use the `storageLocations` parameter only when you want to override the predefined or customized default storage location configured in your snapshot settings.

  * SNAPSHOT_SCOPE_REGION: Optional: For regionally scoped snapshots, the region that the snapshot is scoped to. If you include this parameter, you can't use the `storageLocations` parameter. The STORAGE_LOCATION is automatically set to the SNAPSHOT_SCOPE_REGION.


**Note:** Google recommends using the `snapshots.insert` method instead of the [`disks.createSnapshot` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/createSnapshot) because it supports more features, such as creating snapshots in a project different from the source disk project. 

To create a VSS snapshot of a regional Persistent Disk, in the `POST` requests shown previously, replace the following line: 
    
    
    "sourceDisk": "projects/SOURCE_PROJECT_ID/zones/SOURCE_ZONE/disks/SOURCE_DISK_NAME",
    

Use this line instead when creating a snapshot of a regional Persistent Disk: 
    
    
    "sourceDisk": "projects/SOURCE_PROJECT_ID/regions/SOURCE_REGION/disks/SOURCE_DISK_NAME",
    

### Create a writable disk from a VSS snapshot

When you create a VSS snapshot, Windows Server marks the volume in the snapshot as read-only. When you create a new disk from the VSS snapshot, that disk is also set to read-only mode.

This might cause issues. For example, if you create a VM instance with a new boot disk from a VSS snapshot of an existing boot disk, the read-only flag on the new boot disk prevents the VM from booting correctly.

To work around this issue, remove the read-only flag from any new disk that you create from a VSS snapshot using the following steps:

  1. Make sure the disk is attached to a VM:

     * If the disk that you created from the VSS snapshot is a **non-boot data disk** , you can attach the disk to any new or existing VM.
     * If the disk that you created from the VSS snapshot is a **boot disk** and you want to use it to boot a VM, then you must temporarily attach the disk to a separate, existing VM. After you complete the following steps, you can detach the disk from that VM and use it to boot a new VM instance.
  2. [Sign in to the Windows VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows) that the disk is attached to.

  3. Open a PowerShell command prompt and run the `diskpart` tool.
         
         PS C:\> diskpart
         

  4. Identify the disk that you want to mount.
         
         DISKPART> list disk
         

  5. Use the `select disk` command to select the disk.
         
         DISKPART> select disk DISK_NUMBER
         

Replace `DISK_NUMBER` with the number of the disk that you want to mount.

  6. Mount the disk.
         
         DISKPART> online disk
         

  7. List all the volumes in the disk.
         
         DISKPART> list volume
         

  8. Select the new volume.
         
         DISKPART> select volume VOLUME_NUMBER
         

Replace `VOLUME_NUMBER` with the number of the volume to configure as read and write.

  9. Clear the read-only flag.
         
         DISKPART> attr volume clear readonly hidden nodefaultdriveletter shadowcopy
         

  10. Exit the `diskpart` tool.
         
         DISKPART> exit
         

  11. If the disk is a boot disk for another VM, sync the boot disk files with the new disk signature.
         
         PS C:\> bcdboot DRIVE_LETTERWindows /s DRIVE_LETTER
         

Replace `DRIVE_LETTER` with the drive letter for the volume that you want to sync. For example, `F` for `F:\`.




## Create a snapshot without using VSS

In some situations, you might want to create snapshots of disks that are attached to Windows VMs without using VSS.

To create a disk snapshot on a Windows VM without using VSS, do the following:

  1. Prepare your system for a clean snapshot
  2. Create the snapshot
  3. Remount your disk



### Prepare your system for a clean snapshot

Before you create a disk snapshot, make sure that you are taking a snapshot that is consistent with the state that you want for the disk. If you take a snapshot of your disk in an "unclean" state, it may force a disk check and possibly lead to data loss. Consider syncing and unmounting your file system.

#### Sync the file system

If unmounting your disk is not an option, such as in scenarios where an application might be writing data to the disk, you can sync your file system to flush the disk buffers. To sync your file system:

  1. Sign in to your Windows VM.
  2. Download and install the [Sync](https://learn.microsoft.com/en-us/sysinternals/downloads/sync) tool from Microsoft.
  3. Stop your applications from writing to the disk.
  4. Open an elevated command prompt window.
  5. In the command line window, run:
         
         PS C:\> sync DRIVE_LETTER
         

Replace `DRIVE_LETTER` with the drive letter for the volume that you want to sync. For example, `F` for `F:\`.




#### Unmount the disk

  1. Sign in to your Windows VM.

  2. Open a PowerShell command prompt and run the `diskpart` tool.
         
         PS C:\> diskpart
         

  3. Identify the disk that you want to unmount and snapshot.
         
         DISKPART> list disk
         

  4. Next, select the disk using the disk number that you just found.
         
         DISKPART> select disk DISK_NUMBER
         

Replace `DISK_NUMBER` with the number of the disk that you want to remount.

  5. Unmount the disk.
         
         DISKPART> offline disk
         




### Create a snapshot

  * If your disk is located in a single zone (zonal Persistent Disk or Hyperdisk), follow the steps in [Create a snapshot of a zonal Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#create_zonal_snapshot).
  * Alternatively, if your Persistent Disk is located in a multiple zones, follow the steps in [Create a snapshot of a regional Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#create_regional_snapshot).



### Remount your disk

  1. Sign in to your Windows VM.

  2. Open a PowerShell command prompt and run the `diskpart` tool.
         
         PS C:\> diskpart
         

  3. Identify the disk that you want to mount.
         
         DISKPART> list disk
         

  4. Use the `select disk` command to select the disk.
         
         DISKPART> select disk DISK_NUMBER
         

Replace `DISK_NUMBER` with the number of the disk that you want to mount.

  5. Mount the disk.
         
         DISKPART> online disk
         




## What's next

  * If you took a snapshot of a boot disk, you can [create a VM from a snapshot](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#createsnapshot).
  * To learn how to configure Windows Server so that you can use it to create customized Windows Server images for your VMs or instance templates, read [Create custom Windows Server images](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
