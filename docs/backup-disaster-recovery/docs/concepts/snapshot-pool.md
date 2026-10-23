---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/snapshot-pool/
title: Manage the Snapshot pool of the backup/recovery appliance \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:23.411985+00:00
---

# Manage the Snapshot pool of the backup/recovery appliance  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/snapshot-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage the Snapshot pool of the backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Every backup/recovery appliance has one snapshot pool that contains your most recent production data backups and restored backups. The snapshot pool provides instant access to your data.

The snapshot pool (sometimes referred to as the performance pool) holds golden copies of application data at the points in time specified in a backup plan. The amount of data consumed is determined by whether an existing snapshot can be used.

The snapshot pool often contains hundreds or even thousands of volumes called VDisks. It's important to manage snapshot pool usage, as jobs begin to fail if the snapshot pool is overfull. Snapshot pool consumption is detailed in Understand snapshot pool consumption.

This section includes:

  * Expand snapshot pool

  * Stage disks

  * Understand snapshot pool consumption

  * VDisks

  * VDisk consumption




## Expand snapshot pools

You can expand existing snapshot pools by adding extra disks. You can also add additional storage pools for snapshot storage. You might do this so you can use a mix of storage classes (such as a pool with Standard Disk and a pool with SSD) or to keep different groups of applications separate from each other.

### Create a disk to use with a snapshot pool

The following are the permissions required to create a disk to use with a snapshot pool:

  * `compute.disks.create` on the project before you can create a new disk
  * `compute.instances.attachDisk` on the virtual machine (VM) instance
  * `compute.disks.use` permission on the disk to attach



Use the following instructions to create a disk to use with a snapshot pool:

  1. In the Google Cloud console, go to the **VM instances** page and locate your backup/recovery appliance.
  2. Check the box and click the name of the instance where you want to add a disk.
  3. On the **VM instance details** page, click **Edit**.
  4. Under **Additional disks** , click **Add new disk**.
  5. Specify the following:

     * **Name** : Enter a name for the disk using the existing disk naming as a model.
     * **Source** : Select the **Blank** for the **Source type**.
     * **Disk type** : Select a disk type that matches either the existing disks in the snapshot pool you are resizing or the type of disk you want in the new snapshot pool.
     * **Size** : We recommend snapshot pool disks are always 4096GB (4TB) in size.
     * **Snapshot schedule** : Leave the snapshot schedule to default.
     * **Encryption** : You can specify the encryption as Google-managed encryption key (GMEK) or Customer-managed encryption key (CMEK). Always use the same encryption type for all disks in the same snapshot pool.
  6. Click **Save** to complete the disk's configuration.

  7. Click **Save** to apply your changes to the instance and add the new disk.


**Note:** Don't resize existing disks that are already assigned to the appliance. Always add new disks if additional capacity is required.

When you have added an additional disk to the appliance you can proceed to either expand an existing snapshot pool or create a new snapshot pool.

### Expand an existing snapshot pool

To expand an existing snapshot pool, first you need to [create a new disk](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/snapshot-pool#disk), and then follow these steps:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.
  2. Select an appliance and click **Configure Appliance** to open the Appliance Configuration page.
  3. From the left panel, select **Storage Pools**.
  4. Select the **Snapshot** tab. The Snapshot Pools page opens.
  5. Find the pool and select the pencil icon in the upper right corner of the pool tile. The Manage Snapshot Pool window opens.
  6. Select the **MDisk(s)** to include in this pool from the list of unmanaged disks by clicking on the appropriate + symbol. Use the search option to find the required MDisk(s). Selected MDisks appear in the right-hand panel. You can hold the mouse cursor over an MDisk record to see its status, including UID, controller, and capacity.
  7. Click **Submit**. A warning dialog appears. Type PROCEED to confirm.
  8. Click **Confirm**.

**Note:** You cannot shrink an existing pool by removing MDisks. You can only expand a pool.

### Create a new snapshot pool

To create a new snapshot pool, first you need to [create a new disk](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/snapshot-pool#disk), and then follow these steps:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.
  2. Select an appliance and click **Configure Appliance** to open the Appliance Configuration page.
  3. From the left panel, select **Storage Pools**.
  4. Select the **Snapshot** tab. The Snapshot Pools page opens.
  5. Click **Click to add pool**. The Create Pool page opens.
  6. Enter a **Name** for the storage pool.
  7. If required, modify the default **Warning** limit.
  8. Select the **MDisk(s)** to include in this pool from the list of unmanaged disks by clicking on the appropriate + symbol. Use the search option to find the required MDisk(s). Selected MDisks appear in the right-hand panel.
  9. Click **Submit**.
  10. A warning dialog appears. Type **PROCEED** to confirm.
  11. Click **Confirm**. The newly created pool is listed under the snapshot pool page.

**Note:** Due to system limitations, the safe thresholds are set 90% for all pools and are not subject to modification.

### Delete an existing snapshot pool

Before deleting an existing snapshot pool ensure that:

  * There are no backup plan profiles specifying the pool.
  * There are no backups resident in the pool. All backups need to be expired.



To delete an existing snapshot pool:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.
  2. Select an appliance and click **Configure Appliance** to open the Appliance Configuration page.
  3. From the left panel, select **Storage Pools**.
  4. Select the Snapshot tab. The Snapshot Pools page opens. Find the pool and select the rubbish bin icon in the upper right corner of the pool tile.
  5. A warning dialog appears. Type **DELETE** to confirm.
  6. Click **Confirm**. Provided the pool is not in use by any backup plan profiles and contains no backups, then the pool will be deleted.

**Note:** You cannot delete the default snapshot pool act_per_pool000. Only additional snapshot pools can be deleted.



### Impact of disabling or deleting CMEKs

If a backup/recovery appliance uses persistent disks that are encrypted with Customer Managed Encryption Keys (CMEK) then:

  * If the key version is rotated, the attached disk will remain encrypted with the older key version. See [Rotate your Cloud Key Management Service encryption key for a persistent disk](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#rotate_encryption).
  * If the key version in use by any disk attached to the backup/recovery appliance is disabled or deleted then the backup/recovery appliance won't be able to power on. See [Disabling or deleting CMEKs](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#impact_of_disabling_or_deleting_cmeks).



#### View key version

To determine which key version is in use by a backup/recovery appliance:

  1. Go to **Compute Engine** > **VM instances**.
  2. Locate the backup/recovery appliance and select the instance name to open the details view for that instance.
  3. Go to the Storage section and review all attached disks.
  4. Select each disks name to view the key version.



## Staging disks

A staging disk is a VDisk created when an application is first protected. It is a copy of the production data as of the last backup invoked by the application's backup plan. Each staging disk is associated with a number of snapshots on their own snapshot VDisks. The number of snapshots for each application or VM is determined by the backup plan frequency of snapshot and retention period.

Because a staging disk is a complete copy of the production application or VM, each staging disk requires as much storage space in the Snapshot Pool as the protected application or VM requires in its production storage. Snapshots made from the staging disk reference the data in the staging disk, so they are much smaller. As subsequent backups change blocks in the staging disk, the original blocks are "pushed" into the snapshot VDisks, so the snapshot appears to have constant content but contains more and more blocks over time.

### Staging disks for VMware VMs and out-of-band applications

When you protect a VM or an application, copies of the selected backup are put into a dedicated virtual staging disk in the snapshot pool. Backup and DR creates a snapshot from the backup on the staging disk, and stores the snapshot in the snapshot pool for the time specified in the backup plan.

Staging disks for backups are allocated from the snapshot pool. The VDisk is thin-provisioned. Each snapshot created of that staging disk also consumes snapshot pool space, the amount depending on the application change rate.

An exception for Direct-to-OnVault Protection for VMware VMs

VMware VMs protected direct-to-OnVault don't go through a staging disk because the appliance can get changed-block information directly from the VMware layer. All other applications get changed-block information either from Oracle RMAN or the Backup and DR agent (using a Backup and DR staging disk).

## Understand snapshot pool consumption

The snapshot Pool contains both the staging disks and the snapshot disks for every protected application or VM, plus any clones and mount backups that you make.

The snapshot Pool holds virtual disks, or VDisks. VDisks and VDisk consumption are explained in VDisks. Snapshot Pool space is consumed by four different kinds of VDisk:

  * **Staging VDisks** : Staging VDisks, usually called staging disks, hold the Backup and DR golden copy of the application. Staging disks are retained for as long as an application is protected and at least one snapshot exists. See Staging Disks.

  * **Snapshot VDisks** : These are used to preserve the state of staging disks at specific points in time. Snapshots are retained until their expiration time, but the last snapshot will never expire unless the application is unprotected or it is explicitly expired.

  * **Mountable VDisk** : Mountable VDisks are mountable backups created at restore time from a snapshot on a snapshot disk.

  * **Clone VDisks** : Clone disks are full copies of an application's production data. Clone disks are not automatically expired.




## VDisks

Backup and DR uses logical VDisks (virtual disks or volumes) to virtualize data from hosts. VDisks are taken from a pool of managed disks (MDisks) presented to a backup/recovery appliance from one or more arrays.

From the VDisks, the data can be cloned, mounted, and recovered, presented for test and development work, and manipulated in other tasks. VDisks are created as needed on physical disk arrays.

There is a fixed limit of VDisks per backup/recovery appliance. As you create protection policies, your appliance will warn you when a configuration may exceed VDisk limits.

## VDisk consumption

In general, each protected application or VM requires one or more VDisks for the staging disk plus the same number more VDisks per snapshot. In addition, note these rules:

  * VM-level backups with a snapshot backup plan consume one VDisk for each virtual disk in the VM.

  * File system backups in a Windows environment consume one VDisk for each protected file system.

  * File system backups in a Unix environment consume a VDisk for every 833GB protected times 1+(number of retained snapshots). You can adjust the 833GB value by changing Staging Disk Granularity in Details & Settings.

  * Mounts, LiveClones, and Clones of non-VM applications consume VDisks.

  * On Linux systems, filesystems and Oracle databases consume one VDisk plus another for every additional 2TB data is being protected.

  * SQL Server databases consume one VDisk for every volume that hosts the database.

  * Each snapshot of a VDisk consumes one VDisk per snapshot per protected disk.

  * Snapshots show peak usage, as new snapshots are created before old snapshots are expired.

  * After failover and syncback, the failback operation cleans out all the syncback and failover VDisks.

VDisks are thin-provisioned, and can grow over time.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
