---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/primary-pool/
title: Manage the Primary pool of the backup/recovery appliance \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:45.070880+00:00
---

# Manage the Primary pool of the backup/recovery appliance  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/primary-pool/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage the Primary pool of the backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Every backup/recovery appliance has one primary pool that contains metadata and log files for the backup/recovery appliance. No user data or backups are stored in the primary pool.

## Create a disk to use with Primary pool

You can expand the existing primary pool by adding extra disks.

The following are the permissions required to create a disk to use with a primary pool:

  * `compute.disks.create` on the project before you can create a new disk
  * `compute.instances.attachDisk` on the virtual machine (VM) instance
  * `compute.disks.use` permission on the disk to attach



Use the following instructions to create a disk to use with a primary pool:

  1. In the Google Cloud console, go to the **VM instances** page and locate your backup/recovery appliance.
  2. Check the box and click the name of the instance where you want to add a disk.
  3. On the **VM instance details** page, click **Edit**.
  4. Under **Additional disks** , click **Add new disk**.
  5. Specify the following:

     * **Name** : Enter a name for the disk using the existing disk naming as a model.
     * **Source** : Select the **Blank** for the **Source type**.
     * **Disk type** : Select a disk type that matches the existing disks in the primary pool.
     * **Size** : We recommend primary pool disks are always 200GB in size.
     * **Snapshot schedule** : Leave the snapshot schedule to default.
     * **Encryption** : You can specify the encryption as Google-managed encryption key (GMEK) or customer-managed encryption key (CMEK). Always use the same encryption type for all disks in the primary pool.
  6. Click **Save** to complete the disk's configuration.

  7. Click **Save** to apply your changes to the instance and add the new disk.


**Note:** Don't resize existing disks that are already assigned to the appliance. Always add new disks if additional capacity is required.

When you have added an additional disk to the appliance proceed to expand the existing primary pool.

### Expand the primary pool

To expand an existing primary pool, first you need to create a new disk, and then follow these steps:

  1. Click the **Manage** tab and select **Appliances** from the drop-down menu.
  2. Select an appliance and click **Configure Appliance** to open the Appliance Configuration page.
  3. From the left panel, select **Storage Pools**.
  4. Select the **Primary** tab. The Primary Pools page opens.
  5. Find the pool and select the pencil icon. The Manage Primary Pool window opens.
  6. Select the **MDisk(s)** to include in this pool from the list of unmanaged disks by clicking on the appropriate + symbol. Use the search option to find the required MDisk(s). Selected MDisks appear in the right-hand panel. You can hold the mouse cursor over an MDisk record to see its status, including UID, controller, capacity, and more.
  7. Click **Submit**. A warning dialog appears. Type PROCEED to confirm.
  8. Click **Confirm**.

**Note:** You cannot shrink an existing pool by removing MDisks. You can only expand a pool.



### Impact of disabling or deleting CMEKs

If a backup/recovery appliance uses persistent disks that are encrypted with Customer Managed Encryption Keys (CMEK) then:

  * If the key version is rotated, the attached disk will remain encrypted with the older key version. See [Rotate your Cloud Key Management Service encryption key for a persistent disk](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#rotate_encryption).
  * If the key version in use by any disk attached to the backup/recovery appliance is disabled or deleted then the backup/recovery appliance won't be able to power on. See [Disabling or deleting CMEKs](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#impact_of_disabling_or_deleting_cmeks).



#### View key version

To determine which key version is in use by a backup/recovery appliance:

  1. Go to **Compute Engine** > **VM instances**.
  2. Locate the backup/recovery appliance and select the instance name to open the details view for that instance.
  3. Go to the **Storage** section and review all attached disks.
  4. Select each disks name to view the key version.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
