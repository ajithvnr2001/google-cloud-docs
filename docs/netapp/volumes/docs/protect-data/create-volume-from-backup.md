---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-volume-from-backup/
title: Create a new volume from an existing backup \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:32.527615+00:00
---

# Create a new volume from an existing backup  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-volume-from-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a new volume from an existing backup Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to create a new volume from an existing backup.

## Considerations

  * You can restore backups in in-region backup vaults to any pool within the backup region.

  * For backups stored in cross-region backup vaults, you can only restore backups locally, either from the source vault to the source region or from the destination vault to the destination region. You can't restore to any other region. Note that this isn't available for the Flex File service level.

  * If you have set a Minimum enforced retention policy on a backup vault that contains the backup, the backup can't be deleted before the scheduled date in the **Deletable on** field. For more information, see [Prevent backup deletion](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#prevent_backup_deletion).

  * When restoring a backup of a large capacity volume, the new volume is automatically created as a large capacity volume.

  * The restored volume size must be at least 20% larger than the volume's used capacity in the backup; you can resize the volume after the restore completes.

  * You can restore backups stored in a CMEK-enabled backup vault only if the associated encryption key is accessible.




## Create a new volume from a backup

### Console

  1. Go to **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Data protection** , click **Backups**.

  3. In the **Backups** page, select the backup you want to open.

  4. At the top of the page, click **Create new volume from backup**.

  5. In the **Volume name** field, enter a name for the volume. The name must be unique to the region, use lowercase letters, numbers, hyphens, and start with a letter. Your choice is permanent.

  6. Optional: in the **Description** field, enter a description for the volume.

  7. In the **Storage pool details** section, select an existing storage pool or create a new storage pool.

For backups in in-region vaults, all storage pools in the region are available.

For backups in cross-region vaults, all storage pools in the Flex Unified, Standard, Premium, and Extreme service levels are available.

  8. Under **Volume details** , enter a share name in the **Share name** field. The share name must be unique to the region.

  9. In the **Capacity** field, enter the capacity of the volume.

     1. For backups where the source volume still exists, the **Capacity** field is auto-populated with the source volume size and can't be changed.

You can use [Google Cloud CLI command](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-volume-from-backup#gcloud) to specify a different size.

     2. For backups where the source volume no longer exists, specify the new volume size in GiB. The capacity must be larger than the **Volume usage size (restored)** size of the backup.

  10. Optional: select **Enable auto-tiering** if the storage pool you are restoring to has auto-tiering enabled. You can also enable this later in [volume settings](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering#edit-auto-tiering-parameters).

  11. Under the **Protocol(s)** drop-down menu, select the protocol.

     1. For backups where the source volume still exists, the **Protocol(s)** field is auto-populated with the source volume protocols and can't be changed.

     2. For backups where the source volume no longer exists, specify the same protocols as the original source volume.

**Important:** The protocols must match the protocols of the source volume. Otherwise, the volume creation will fail.
  12. For NFS volumes, complete the following steps:

**Important:** The protocols must match the protocols of the source volume. Otherwise, the volume creation will fail.
     1. Click **Block volume from deletion when clients are connected** in the **Configuration for selected protocol(s)** for volumes used as GCVE datastores.

**Important:** This setting is permanent, you can't change it later.
     2. Under **Export rules** , complete the following steps:

        1. Click **Add rule** to add a list of allowed clients, their associated access level (read and write, or read only), and their root access. For more information, see [Volume access control using export policies](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients#volume_access_control_using_export_policies).

        2. Click **Done**.

  13. For SMB volumes, complete the following steps:

**Important:** The protocols must match the protocols of the source volume. Otherwise, the volume creation will fail.
     1. For backups where the source volume still exists, SMB protocol options aren't displayed. However, you can change them later after the volume is created, or use the Google Cloud CLI command to restore the volume and specify the SMB options.

     2. For backups where the source volume no longer exists, choose any optional protocol configurations. For more information about protocol options, see [Create a new volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume).

  14. For iSCSI volumes, complete the following steps:

**Important:** The protocols must match the protocols of the source volume. Otherwise, the volume creation will fail.
     1. For backups where the source volume still exists, the iSCSI protocol is automatically selected.

     2. For backups where the source volume no longer exists, choose iSCSI protocol. For more information about protocol options, see [Create a new volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume).

  15. Optional: under **Snapshot configuration** , configure a schedule for volume snapshots:

     1. If you want to make your snapshot directory visible to clients, select the **Make snapshot directory visible** checkbox.

     2. If you want to allow scheduled snapshots, select the **Allow scheduled snapshots** checkbox.

     3. Using the **Hourly, Daily, Weekly, and Monthly** tabs, configure your snapshot schedule:

For each interval (hourly, daily, weekly, or monthly), use the **Snapshots To Keep** field to enter the amount of snapshots you want to keep. Use the **Hour (UTC)** and **Minute (UTC)** fields to enter when the snapshots will be retained.

  16. Optional: under **Backup configuration** , assign a backup policy and backup vault to set up scheduled backups for the new volume.

     1. Select the **Allow scheduled backups** checkbox.

     2. Use the **Backup policy** drop-down to choose an existing backup policy or create a new one.

     3. Use the **Backup vault** drop-down to choose an existing backup vault or create a new one.

  17. Under the **Labels** section, click **Add labels** to add relevant labels to your volume.

  18. Click **Create**.




### gcloud

Create a new volume from a backup:
    
    
    gcloud netapp volumes create VOLUME_NAME \
      --location=LOCATION \
      --capacity=CAPACITY \
      --protocols=PROTOCOLS \
      --share-name=SHARE_NAME \
      --storage-pool=STORAGE_POOL \
      --source-backup=SOURCE_BACKUP \
      --description=DESCRIPTION

Replace the following information:

  * `VOLUME_NAME`: the name of the new volume to restore the backup to.

  * `LOCATION`: the location you want to create the volume in.

  * `CAPACITY`: the size for the new volume. The capacity must be larger than the **Volume usage size (restored)** of the backup.

  * `PROTOCOLS`: used for the original volume the backup was taken from.

  * `SHARE_NAME`: the share name for the new volume.

  * `STORAGE_POOL`: name of the storage pool within `LOCATION` to host the volume.

  * `SOURCE_BACKUP`: resource name of the backup to restore. Format as projects/`PROJECT_ID`/locations/ `LOCATION`/backupVaults/`BACKUP_VAULT_ID`/ backups/`BACKUP_ID`

  * `DESCRIPTION`: the description for the volume.




You can add other protocol-specific options such as export policies or snapshot policies. For more options, see [Google Cloud SDK documentation for NetApp Volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/create).

### ONTAP-mode

Identify the required ONTAP commands in the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/).

### Before you begin

Review the following prerequisites before you restore a volume from a backup:

  * To perform a complete backup restore, create a data protection volume by using the ONTAP-mode APIs.

  * To perform a selective file restore, create a read-write volume.




Complete the following steps:

  1. [Create a new data protection (DP) volume of `type=DP`](https://docs.netapp.com/us-en/ontap-cli//volume-create.html#parameters).

     * Make sure the data protection volume has enough capacity for the restored backup.

     * Set the appropriate security style for the data being restored.

  2. Restore a volume in ONTAP-mode:
         
         gcloud netapp storage-pools restore-volume STORAGE_POOL \
          --location=LOCATION \
          --backup=BACKUP_NAME \
          --volume-uuid=VOLUME_UUID \
          [--files=FILE1,FILE2,...] \
          [--destination-path=DESTINATION_PATH] \
          [--async]

Replace the following information:

     * `STORAGE_POOL`: the name of the ONTAP-mode storage pool where the volume resides.

     * `LOCATION`: the location where you want to create the volume.

     * `BACKUP_NAME`: the resource name of the backup to restore. Format as projects/`PROJECT_NAME`/locations/ `LOCATION`/backupVaults/`BACKUP_VAULT_NAME`/ backups/`BACKUP_NAME`

     * `VOLUME_UUID`: the universally unique identifier (UUID) of the volume to which you want to restore the backup.

     * `FILE1, FILE2`: the absolute path of the files you want to restore.

     * `DESTINATION_PATH`: the location in the destination volume where you want to restore the files.




### Example: Restore to ONTAP-mode volume
    
    
    gcloud netapp storage-pools restore-volume my-storage-pool \
    --location=us-central1 \
    --backup="projects/my-project/locations/us-central1/backupVaults/bv-1/backups/backup-to-restore-from" \
    --volume-uuid="d5084fb3-4796-11f1-a62a-b125d7b38361"
    

### Example: Selective file restore to ONTAP-mode volume
    
    
    gcloud netapp storage-pools restore-volume my-storage-pool \
    --location=us-central1 \
    --backup="projects/my-project/locations/us-central1/backupVaults/bv-1/backups/backup-to-restore-from" \
    --volume-uuid="d5084fb3-4796-11f1-a62a-b125d7b38361" \
    --files="/path/to/your/file1.txt,/path/to/your/other/file2.dat" \
    --destination-path="/my_restore_destination"
    

## What's next

[Manage your backups](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
