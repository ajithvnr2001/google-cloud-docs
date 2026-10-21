---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup-vault/
title: Manage your backup vault \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:33.475755+00:00
---

# Manage your backup vault  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage your backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to manage your backup vault.

## Considerations

You can only change the description and labels associated with your backup vault after it's created.

## View backup vault

Use the following instructions to view backup vault using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Backup vaults** from the **Data protection** menu.

  3. From the list of created backup vaults, select the backup vault you want to see details for. The Backup vaults page opens. You can review the following details:

     * **Resource type** : displays the resource type.

     * **State** : describes the state of the backup including whether it's ready, creating, updating, deleting, or experiencing an error.

     * **Description** : displays the optional description.

     * **Name** : lists the name of the backup vault.

     * **Type** : specifies if the vault is **In-region** or **Cross-region**.

     * **Region** (in-region vaults only): specifies the vault's region.

     * **Source region** (cross-region vaults only): specifies the vault's source region and associated backup vault.

     * **Destination region** (cross-region vaults only): specifies the vault's destination region and associated backup vault.

     * **Prevent backup deletion** : displays the minimum backup retention time set for the backup vault and the types of backups that are retained.

     * **Encryption** : displays the key management option selected.

       * Google-managed encryption key

       * Customer-managed encryption key (CMEK)

     * **Key** (CMEK vaults only): displays the details of the customer-managed key used to encrypt the backup vault.

     * **Rotation status** (CMEK vaults only): displays the status of the encryption operation on the backup vault. The status is updated whenever the encryption key is rotated.

The following are the possible states:

       * **Pending**

       * **In-progress**

       * **Completed**

       * **Failed**

     * **Created** : lists the date and time the backup vault was created.

     * **Labels** : displays optional labels.

     * **Backups** : displays a table of backups stored in the backup vault. For each backup, the table lists the following:

Backup information | Description  
---|---  
**Status** | The status of the backup including whether it's ready, creating, updating, deleting, or experiencing an error.  
**Name** | The name of the backup.  
**Volume** | The name of the volume the backup was taken from.  
**Location** | Where the backup data is stored.  
**Type** | Specifies whether the backup is manual or scheduled.  
**Size** | The size of the backup in GiB.  
**Creation date** | The date the backup was created.  
  
To view actions for a backup, click more_vert **Show more** icon.

     * **Associated Volumes** : displays a list of volumes that are associated with the backup vault. Volumes within storage pools that have ONTAP-mode enabled aren't displayed. Each volume displays the following:

       * **Status** : the status of the volume.

       * **Volume name** : the name of the volume.

       * **Utilization** : the amount of used capacity versus available capacity in the volume.

       * **Labels** : displays optional labels.

To view actions for a volume, click more_vert **Show more** icon.




### gcloud

To view all the backup vaults:
    
    
     gcloud netapp backup-vaults list

To lookup a specific backup vault:
    
    
     gcloud netapp backup-vaults describe VAULT_NAME \
      --location=LOCATION

Replace the following information:

  * `VAULT_NAME`: the name of the backup vault.

  * `LOCATION`: the location of the backup vault.




### ONTAP-mode

To list volumes and their associated backup configurations in an ONTAP-mode storage pool:
    
    
     gcloud netapp storage-pools list-backup-configs STORAGE_POOL \
      --location=LOCATION

Replace the following information:

  * `STORAGE_POOL`: the name of the ONTAP-mode storage pool where the volume resides.

  * `LOCATION`: the location of the ONTAP-mode storage pool.




## Edit a backup vault

Use the following instructions to edit a backup vault using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Backup vaults** from the **Data protection** menu.

  3. In the **Backup vaults** page, select the backup vault you want to edit.

  4. Click **Edit**.

  5. Make any applicable changes.

  6. Click **Save**.




### gcloud

To edit a backup vault:
    
    
     gcloud netapp backup-vaults update VAULT_NAME \
      --location=LOCATION

Replace the following information:

  * `VAULT_NAME`: the name of the backup vault.

  * `LOCATION`: the location of the backup vault.




For more information, see [Google Cloud SDK documentation for NetApp Volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/update).

## Assign a volume to your backup vault

Use the following instructions to assign a volume to your backup vault using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes** from the **Storage** menu.

  3. In the **Volumes** page, select the volume you want to create a backup for.

  4. In the volume details page, click the **Backups** tab.

  5. Click **Assign backup policy**.

  6. Select the backup vault to store your backups in from the **Backup vault** menu.

**Note:** CMEK-enabled backup vaults aren't available for the Flex File service level.
  7. Click **Assign**.

**Note:** If the backup vault assigned to the volume has a specified minimum retention period, any manual backups performed are also assigned that minimum retention value. For more information, see [Prevent backup deletion](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#prevent_backup_deletion).



### gcloud

To assign a volume to a backup vault, add the backup vault to the volume configuration:
    
    
     gcloud netapp volumes update VOLUME_NAME \
      --location=LOCATION \
      --backup-config=backup-vault=VAULT_RESOURCE_PATH

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `LOCATION`: the location of the volume.

  * `VAULT_RESOURCE_PATH`: full resource path of the backup vault. Format as `projects/PROJECT_ID/locations/VAULT_LOCATION/backupVaults/VAULT_NAME`




## Unassign a volume from your backup vault

Use the following instructions to unassign a volume from your backup vault.

### Considerations

  * You must first unassign the volume's backup policy before you can disassociate the volume from the backup vault.

  * You can't unassign a volume from a backup vault until you delete all backups of the associated volume.




Use the following instructions to unassign a volume from your backup vault using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Backup vaults** from the **Data protection** menu.

  3. In the **Backup vaults** page, click the backup vault you want to unassign a volume from.

  4. Click the **Associated volumes** tab.

  5. For the volume you want to unassign from the backup vault, click **Show more**.

  6. Click **Unassign volume**.

A message appears that prompts you to confirm you want to unassign the volume from the backup vault.

  7. To confirm that you want to unassign the volume from the backup vault, click **Unassign**.




### gcloud

To unassign a volume from a backup vault, remove the backup vault from the volume configuration:
    
    
     gcloud netapp volumes update VOLUME_NAME \
      --location=LOCATION \
      --backup-config=backup-vault=

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `LOCATION`: the location of the volume.




## Delete a backup vault

Before you delete a backup vault, you must do the following:

  * [Unassign all backup policies](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup-policy#unassign_a_backup_policy_from_a_volume) from the volume associated with the backup vault. For more information about backup vaults, see View backup vault.

  * [Unassign all volumes from the backup vault](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup-vault#unassign_a_volume_from_your_backup_vault).

  * [Remove all backups contained in a vault](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup#delete_a_backup). The latest backup of a volume can only be deleted after all other backups of the volume have been deleted.




Use the following instructions to delete a backup vault using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Backup vaults** from the **Data protection** menu.

  3. From your list of backup vaults, click the backup vault you want to delete.

  4. Click **Delete**.

A message appears asking you to delete the backup vault.

  5. In the **Backup vault** field, enter the name of the backup vault you want to delete.

  6. Click **Delete**.




### gcloud
    
    
     gcloud netapp backup-vaults delete VAULT_NAME \
      --location=LOCATION

Replace the following information:

  * `VAULT_NAME`: the name of the backup vault.

  * `LOCATION`: the location of the backup vault.




For more information, see [Google Cloud SDK documentation for NetApp Volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/delete).

## What's next

Manage your [backup policies](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
