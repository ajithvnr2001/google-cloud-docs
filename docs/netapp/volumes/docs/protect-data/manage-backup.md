---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup/
title: Manage your backup \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:54:04.707280+00:00
---

# Manage your backup  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage your backup Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details for how to manage an existing backup.

## View a list of backups

Use the following instructions to view a list of backups.

### Considerations

Backups are stored only in the destination region of cross-regional vaults. However, the backups are listed separately by the source and destination regions of the vault.

Use the following instructions to view a backup using either the Google Cloud console or Google Cloud CLI:

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Data protection** , click **Backups**.

  3. You can review the following details for your backups:

     * **Status** : the state of the backup, including whether it's ready, creating, updating, deleting, or experiencing an error.

     * **Name** : the name of the backup.

     * **Volume** : the volume that is backed up. In ONTAP-mode, volume backups display the volume universally unique identifier (UUID) instead of the volume name.

     * **Volume location** : where the volume is located.

     * **Backup location** : where the backup is located.

     * **Backup vault** : the backup vault associated with the backup.

     * **Backup vault type** : the type of backup vault, in-region or cross-region vault associated with the backup.

     * **Deletable on** : the date and time the backup vault's retention period ends and the backup can be deleted.

     * **Created** : the date and time the backup was created.

     * **Type** : whether the backup is scheduled or manual.

     * **Size** : the size of the backup.

     * **Labels** : optional labels for the backup.

     * **Show more** : additional options such as viewing additional details, editing the backup, creating a volume from the backup, and deleting the backup.




### gcloud

View a list of backups:
    
    
      gcloud netapp backup-vaults backups list \
       --location=LOCATION \
       --backup-vault=BACKUP_VAULT

Replace the following information:

  * `LOCATION`: the location where you want to view the backup.

  * `BACKUP_VAULT`: the backup vault of the backup.




For more options, see [Google Cloud SDK documentation for NetApp Volumes](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups).

## Edit a backup

Use the following instructions to edit a backup using either the Google Cloud console or Google Cloud CLI:

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Data protection** , click **Backups**.

  3. In the **Backups** page, navigate to the backup you want to make changes to and click the **Show more** icon.

  4. Click **Edit**.

  5. Make the required changes to the backup.

  6. Click **Save**.




### gcloud

Edit a backup:
    
    
      gcloud netapp backup-vaults backups update BACKUP_NAME \
       --location=LOCATION \
       --backup-vault=BACKUP_VAULT \
       --description=DESCRIPTION \
       --update-labels=foo=bar \
       --clear-labels=foo=bar \
       --remove-labels=foo=bar

Replace the following information:

  * `BACKUP_NAME`: the name of the backup.

  * `LOCATION`: the location in which you want to edit the backup.

  * `BACKUP_VAULT`: the backup vault of the backup.

  * `DESCRIPTION`: the description for the backup.




For more options, see [Google Cloud SDK documentation for NetApp Volumes](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups).

## Delete a backup

You can't delete the latest backup of a volume unless the backup policy is first unassigned and all previous backups are deleted.

**Warning:** Backup deletion is irreversible. When you delete a backup, it's no longer recoverable.

Use the following instructions to delete a backup:

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Data protection** , click **Backups**.

  3. In the **Backups** field, navigate to the backup you want to delete and click the **Show more** icon on the volume.

**Note:** If the backup is delete protected, a **Deletable on** date is displayed. The backup can't be deleted before that scheduled date. For more information, see [Prevent backup deletion](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#prevent_backup_deletion).
  4. Click **Delete**.

  5. A confirmation dialog appears. Read through the warnings.

  6. To proceed, enter the name of the backup in the **Backup name** field and click **Delete**.




### gcloud

Delete a backup:
    
    
    gcloud netapp backup-vaults backups delete BACKUP_NAME \
     --location=LOCATION \
     --backup-vault=BACKUP_VAULT

Replace the following information:

  * `BACKUP_NAME`: the name of the backup.

  * `LOCATION`: the location from which you want to delete the backup.

  * `BACKUP_VAULT`: the backup vault of the backup.




If the backup is delete protected, listing the backup shows the `enforced_retention_end_time` parameter which specifies the expiry date. The backup can't be deleted before that scheduled date. For more information, see [Prevent backup deletion](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#prevent_backup_deletion).

For more options, see [Google Cloud SDK documentation for NetApp Volumes](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups).

### ONTAP-mode

Delete a backup:
    
    
    gcloud netapp backup-vaults backups delete BACKUP_NAME \
     --location=LOCATION \
     --backup-vault=BACKUP_VAULT

Replace the following information:

  * `BACKUP_NAME`: the name of the backup.

  * `LOCATION`: the location from which you want to delete the backup.

  * `BACKUP_VAULT`: the backup vault of the backup.




If the backup is delete protected, listing the backup shows the `enforced_retention_end_time` parameter which specifies the expiry date. The backup can't be deleted before that scheduled date. For more information, see [Prevent backup deletion](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#prevent_backup_deletion).

For more options, see [Google Cloud SDK documentation for NetApp Volumes](https://cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups).

## What's next

Manage your [backup vault](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup-vault).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
