---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore/
title: Restore a disk from a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:20.141149+00:00
---

# Restore a disk from a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore a disk from a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This page helps you to restore disks from a backup vault in the Google Cloud console.

## Required roles

To get the permissions that you need to restore a disk from a backup vault, ask your administrator to grant you the following IAM roles on the project, the target project, the Backup and DR service agent, and the Cloud KMS key: 

  * Restore a disk: 
    * [Backup and DR Restore User ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`)
    * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)
  * Grant roles to the service agent: [Backup and DR Disk Operator ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.diskOperator) (`roles/backupdr.diskOperator`) 
  * Use customer-managed encryption keys (CMEK) (optional): [Cloud KMS CryptoKey Encrypter/Decrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to restore a disk from a backup vault. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to restore a disk from a backup vault:

  * Restore a disk: 
    * `backupdr.bvbackups.restore`
    * `backupdr.compute.restoreFromBackupVault`
    * `backupdr.backupVaults.get`
    * `backupdr.backupVaults.list`
    * `backupdr.bvbackups.list`
    * `backupdr.bvdataSources.get`
    * `backupdr.bvdataSources.list`
    * `backupdr.bvbackups.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Restore disks

Use the following instructions to restore disks used by a Compute Engine instance.

**Note:** By default, a disk restored from a CMEK-encrypted snapshot will use the source disk's KMS key for encryption. Consequently, the Compute Service Account of the target project (where the restored disk is being created) must have the Cloud Key Management Service `CryptoKey Encrypter` (`roles/cloudkms.cryptoKeyEncrypter`) role on that source key.

For more information on CMEK permissioning see [Customer-managed encryption keys (CMEK){](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek#permissions_required_to_use_cmek)

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

All Compute Engine instances with vaulted backups are listed here. Disks are labeled **Disks** in the **Resource type** column.

  2. Select the backup to restore. Either from the backup details page for the backup, or from the more_vert menu for the disk:

     1. Select the disk **Resource type**.
     2. Select a **Resource name**.
     3. Browse to select the backup to restore.
     4. The **Restore project name** is prepopulated with the current project, but you can browse to a different project if you want to restore elsewhere.
     5. Click **Restore**. You can view and monitor the restore job from the Notifications bell.
     6. The restored disk appears in the Compute Engine **Storage** > **Disks** list, with the original name followed by a time and date stamp.



###  gcloud 

  1. If not already granted, grant the `Backup and DR Disk Operator` (`roles/backupdr.DiskOperator`) IAM role to the disk being recovered.

  2. To get the backup vault service account, use the following command.
         
         gcloud backup-dr backup-vaults describe BACKUPVAULT_NAME
           --location=LOCATION
         

Replace the following:

     * BACKUPVAULT_NAME: the backup vault name you want to restore data from.
     * LOCATION: the location of the backup vault.
  3. To restore a disk, use the following commands.

     * Restore a disk in the same project as the workload project with backup ID.
           
           gcloud backup-dr backups restore disk test-backup-id \
             --project=PROJECT \
             --location=LOCATION \
             --backup-vault=BACKUPVAULT_NAME \
             --data-source=DATA_SOURCE\
             --name=NAME \
             --target-zone=TARGET_ZONE \
             --target-project=TARGET_PROJECT
           

     * Restore a disk in the same project as the workload project with backup full resource URL.
           
           gcloud backup-dr backups restore disk projects/test-project-id/locations/us-central1/backupVaults/test-vault/dataSources/test-ds/backups/test-backup-id \
             --name=NAME \
             --target-zone=TARGET_ZONE \
             --target-project=TARGET_PROJECT
           

Replace the following:

       * PROJECT: the name of the backup vault project.
       * LOCATION: the location of the backup vault.
       * BACKUPVAULT_NAME: the backup vault name you want to restore data from.
       * DATA_SOURCE: the data source name you want to restore data from.
       * NAME: the name of the restored disk.
       * TARGET_ZONE: the region the disk is restored in.
       * TARGET_PROJECT: the project the disk is restored in.



## Perform a selective disk restore from a Compute Engine instance backup

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

All Compute Engine instances with vaulted backups are listed here.

  2. Select the backup vault, then select the data source corresponding to the Compute Engine instance.

  3. Choose the specific Compute Engine instance backup version and click **Restore**.

The **Restore a backup** page displays.

  4. From the **Resource type** drop-down menu, select **Compute Engine**.

  5. In the **Resource name** field, select **Browse**.

The **Select a resource** pane displays.

  6. Select the resource for which you want to perform the restore operation.

  7. Click **Done**.

  8. From the **Backup** field, click **Browse**.

The **Select a backup** pane displays.

  9. Select the backup that you want to use for the restore operation.

  10. Click **Done**.

  11. In the **Restore scope** section, click the **Restore scope** drop-down menu, and select the disk you want to restore.

The **Source disk properties** displays.

  12. **Optional** : To edit the restored disk's properties, click **Edit properties**.

     1. In the **Disk configuration** pane, make the changes you want to the disk, then click **Save**.
  13. In the **Choose the restore destination** section, use the **Restore project name** field to select a restore project for the restored resource.

  14. Click **Restore**.




###  gcloud 

  1. To restore a disk from a Compute Engine instance backup, use the `gcloud backup-dr backups restore disk` command:
         
         gcloud backup-dr backups restore disk COMPUTE_INSTANCE_BACKUP_NAME \
         --name=DISK_NAME \
         --target-project=TARGET_PROJECT_NAME \
         [--source-instance-boot-disk | --source-instance-disk-device-name=SOURCE_DISK_DEVICE_NAME] \
         [--target-zone=TARGET_ZONE_NAME | --target-region=TARGET_REGION_NAME --replica-zones=ZONE_NAME] \
         [DISK_OVERRIDE_FLAGS...] \
         [--async]
         

Replace the following:

     * COMPUTE_INSTANCE_BACKUP_NAME: the name of the Compute Engine instance backup you want to restore from.

     * DISK_NAME: the name of the restored disk.

     * TARGET_PROJECT_NAME: the project the disk is restored in.

     * SOURCE_DISK_DEVICE_NAME: the device name of the source data disk to restore.

     * TARGET_ZONE_NAME: the zone the disk is restored in for zonal disks.

     * TARGET_REGION_NAME: the region the disk is restored in for regional disks.

     * ZONE_NAME: the replica zones for regional disks.




## What's next

  * For more information on CMEK permissioning see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek#permissions_required_to_use_cmek).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
