---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-backup/
title: Create a backup \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:55.016200+00:00
---

# Create a backup  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a backup Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to create a backup using Google Cloud NetApp Volumes.

## Considerations

  * NetApp Volumes supports a maximum of 1,000 backups per volume.

  * You must assign the volume you want to backup to a backup vault. All backups from that volume go to that vault.

  * NetApp Volumes lets you create scheduled backups by assigning a backup policy to a volume, or you can create manual backups of a volume using the Google Cloud console, Google Cloud CLI, or API.




## Create a manual backup

There are two ways to create a manual backup of an existing volume:

  * Volume-centric workflow

  * Backup-centric workflow




### Volume-centric workflow

  1. Go to **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Storage** , click **Volumes**.

  3. In the **Volumes** page, select the volume you want to create a backup for to expand its details.

  4. In the volume details page, click the **Backups** tab.

  5. Click **Create backup**.

  6. In the **Backup name** field, enter a name for the backup. The name you choose must be unique to the region, contain lowercase letters, numbers, and hyphens. The name cannot be changed after the backup has been created.

  7. Optional: in the **Description** field, enter a description for the backup.

  8. Under **Backup source** , choose a source to backup your data from:

     * **Volume's current state** : back up from the current state of a volume.

     * **Existing snapshot** : back up from an existing snapshot.

Use the **Snapshot** drop-down menu to select a previously created snapshot. If no snapshots have been taken on the volume, the volume's current state radio button is selected by default.

  9. Under **Backup location** , use the **Backup vault** drop-down menu to select a location to store your backups.

**Note:** For cross-region backup vaults, you must specify a source vault.**Note:** CMEK-enabled backup vaults aren't available for the Flex File service level.
  10. Optional: Under the **Labels** section, click **Add label** to enter labels for reporting and querying purposes.

  11. Click **Create**.




### Backup-centric workflow

### Console

  1. Go to **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Data protection** , click **Backups**.

  3. In the **Backups** page, click **Create**.

  4. In the **Backup name** field, enter a name for your backup. The name must be unique to the region, contain lowercase letters, numbers, hyphens, and start with a letter. Your choice is permanent.

  5. Optional: In the **Description** field, enter a description for the backup.

  6. Under **Volume details** , click **Select volume** to select a volume to be backed up.

  7. From the volumes list, select the volume you want to back up and click **Select**.

  8. Under **Backup source** , select a source for your backups:

     * **Volume's current state** : back up from the current state of a volume.

     * **Existing snapshot** : back up from an existing snapshot.

  9. Under **Backup location** , use the **Backup vault** drop-down menu to select a backup location.

**Note:** For cross-region backup vaults, you must specify a source vault.**Note:** CMEK-enabled backup vaults aren't available for the Flex File service level.
  10. Optional: in the **Labels** section, click **Add label** to enter labels for reporting and querying purposes.

  11. Click **Create**.




### gcloud

Use the following instructions to create a backup using Google Cloud CLI:

Create a backup:
    
    
     gcloud netapp backup-vaults backups create BACKUP_NAME \
       --location=LOCATION \
       --backup-vault=BACKUP_VAULT \
       --description=DESCRIPTION \
       --source-volume=SOURCE_VOLUME \
       --source-snapshot=SOURCE_SNAPSHOT \
       --labels=foo=bar

Replace the following information:

  * `BACKUP_NAME`: the name of your new backup.

  * `LOCATION`: the location in which you want to create the vault.

  * `BACKUP_VAULT`: the name of the backup vault.

  * `DESCRIPTION`: the description for the backup.

  * `SOURCE_VOLUME`: the resource name of the volume to back up.

  * `SOURCE_SNAPSHOT`: Optional: the resource name of the snapshot you want to use to create the backup.




For more options, see [Google Cloud SDK documentation for NetApp Volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups).

### ONTAP-mode

Identify the required ONTAP commands in the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/).

To create the backup by using Google Cloud CLI, you need the universally unique identifier (UUID) of the volume to back up. Complete the following steps:

  1. Identify the volume UUID. For more information about instructions, see [List all volumes of a storage pool](https://docs.cloud.google.com/netapp/volumes/docs/ontap/manage-ontap#list_all_volumes_of_a_storage_pool).

  2. Optional: if you want to back up a specific snapshot, identify the [snapshot's UUID](https://docs.cloud.google.com/netapp/volumes/docs/ontap/manage-ontap#list_all_snapshots_of_a_volume). For more information about instructions, see [View snapshot details](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/manage-snapshots#ontap-mode_1).

  3. Create a backup:
         
         gcloud netapp backup-vaults backups create BACKUP_NAME \
         --location=LOCATION \
         --backup-vault=projects/PROJECT_NAME/locations/LOCATION/backupVaults/BACKUP_VAULT_NAME \
         --description=DESCRIPTION \
         --ontap-source=storage-pool=projects/PROJECT_ID/locations/LOCATION/storagePools/STORAGE_POOL_NAME,volume-uuid=VOLUME_UUID,snapshot-uuid=SNAPSHOT_UUID

Replace the following information:

     * `BACKUP_NAME`: the name of your backup.

     * `LOCATION`: the location of the backup vault.

**Note:** For cross-region backup vaults, this is the location of the source vault.
     * `PROJECT_NAME`: the name of your project.

     * `BACKUP_VAULT_NAME`: the name of the backup vault where you want to create the backup.

     * `DESCRIPTION`: the description for the backup.

     * `PROJECT_ID`: the numeric ID of the project.

     * `STORAGE_POOL_NAME`: the name of the ONTAP-mode storage pool where the volume resides.

     * `VOLUME_UUID`: the UUID of the volume to back up.

     * `SNAPSHOT_UUID`: Optional: the UUID of the snapshot to create the backup from.




## What's next

[Create a new volume from an existing backup](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-volume-from-backup).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
