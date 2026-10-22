---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage/
title: Manage backups in the Google Cloud console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:21.718635+00:00
---

# Manage backups in the Google Cloud console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage backups in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to list, view, update, and delete backups in the Google Cloud console.

In a data source, each backup represents the state of the protected resource at a specific point in time. These backups are created based on the schedules defined in backup plans. Additionally, you can initiate on-demand backups whenever needed.

## Before you begin

To get the permissions that you need to list and view backups, ask your administrator to grant you the [Backup and DR Backup Vault Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultViewer) (`roles/backupdr.backupvaultViewer`) IAM role on your backup vault project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list and view backups. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list and view backups:

  * `backupdr.bvbackups.list`
  * `backupdr.bvbackups.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List backups

Use the following instructions to list backups.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-resources)

  2. In the list of scheduled backups, click the name of the scheduled backup you want to view the backup details of.




###  gcloud 

  1. List the backups.
         
         gcloud backup-dr backups list \
           --backup-vault=BACKUPVAULT_NAME \
           --project=PROJECT_ID \
           --location=LOCATION \
           --data-source=DATA_SOURCE
         

Replace the following:

     * `BACKUPVAULT_NAME`: the name of the backup vault used to store backups.
     * `PROJECT_ID`: the name of the project.
     * `LOCATION`: the location of the backup vault.
     * `DATA_SOURCE`: the ID of the data source that you want to list backups.



## View backups

Use the following instructions to view backups.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-resources)

  2. In the list of scheduled backups, click the name of the scheduled backup you want to view the backup details of.

The backup details page displays a list of backups along with their creation times, the backup type - scheduled or on-demand, the associated backup rule, and the backup expiration date.




###  gcloud 

  1. Get the backup ID that is part of a data source.
         
         gcloud backup-dr backups list \
           --backup-vault=BACKUPVAULT_NAME \
           --project=PROJECT_ID \
           --location=LOCATION \
           --data-source=DATA_SOURCE
         

Replace the following:

     * `BACKUPVAULT_NAME`: the name of the backup vault used to store backups.
     * `PROJECT_ID`: the name of the project.
     * `LOCATION`: the location of the backup vault.
     * `DATA_SOURCE`: the ID of the data source for which you want to list backups.
  2. View the backups.
         
         gcloud backup-dr backups describe BACKUP_ID \
           --backup-vault=BACKUPVAULT_NAME \
           --project=PROJECT_ID \
           --location=LOCATION \
           --data-source=DATA_SOURCE
         

Replace the following:

     * `BACKUP_ID`: the ID of the backup.
     * `PROJECT_ID`: the name of the project.
     * `LOCATION`: the location of the backup plan association.
     * `DATA_SOURCE`: the ID of the data source for which you want to view backups.



## Update a backup ([gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) only)

You can only update backups using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

You can update the labels, enforced retention, or expiration time of a backup. Labels are key-value pairs that help you organize and identify your backups.

To get the permission that you need to update a backup, ask your administrator to grant you the [Backup and DR Backup vault Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`) IAM role on your backup vault project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `backupdr.bvbackups.update` permission, which is required to update a backup. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

###  gcloud 

  1. Update a backup.
         
         gcloud backup-dr backups update BACKUP_ID \
           --backup-vault=BACKUPVAULT_NAME \
           --project=PROJECT_ID \
           --location=LOCATION \
           --data-source=DATA_SOURCE \
           --update-labels=LABELS \
           --enforced-retention-end-time=RETENTION_DATE \
           --expire-time=EXPIRATION_DATE
         

Replace the following:

     * `BACKUP_ID`: the ID of the backup.
     * `BACKUPVAULT_NAME`: the name of the backup vault used to store backups.
     * `PROJECT_ID`: the name of the project.
     * `LOCATION`: the location of the backup vault.
     * `DATA_SOURCE`: the ID of the data source.
     * `LABELS`: the labels to apply to the backup as comma-separated key-value pairs, such as `env=prod,team=storage`.
     * `RETENTION_DATE`: the date until which the backup cannot be deleted, in "YYYY-MM-DDTHH:MM:SSZ" format. This period can be extended but not shortened.
     * `EXPIRATION_DATE`: the date when the backup expires, in "YYYY-MM-DDTHH:MM:SSZ" format. This date can be extended but not shortened.
  2. To remove labels, use the `--remove-labels` flag with a list of keys, or use `--clear-labels` to remove all labels.




## Delete a backup

You can delete a backup only if the backup has exceeded its minimum enforced retention period. After deletion, the backup is no longer available for restore.

To get the permission that you need to delete a backup, ask your administrator to grant you the [Backup Vault Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupvaultAdmin) (`roles/backupdr.backupvaultAdmin`) IAM role on your backup vault project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `backupdr.bvbackups.delete` permission, which is required to delete a backup. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** Backup and DR may not immediately delete all backup data at the time defined by the corresponding backup plan or when a backup is manually expired. The reported storage size after deletion will be reconciled over time.

Use the following instructions to delete a backup.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-resources)

  2. Click the name of the scheduled backup you want to delete.

  3. From the backups section, select a backup and then click the more_vert icon.

  4. Select **Delete**.

  5. In the overlay window that appears, confirm you want to delete the backup.

  6. Click **Delete**.




###  gcloud 

  1. Get the backup ID that is part of a data source.
         
         gcloud backup-dr backups list \
           --backup-vault=BACKUPVAULT_NAME \
           --project=PROJECT_ID \
           --location=LOCATION \
           --data-source=DATA_SOURCE
         

Replace the following:

     * `BACKUPVAULT_NAME`: the name of the backup vault used to store backups.
     * `PROJECT_ID`: the name of the project.
     * `LOCATION`: the location of the backup vault.
     * `DATA_SOURCE`: the ID of the data source that you want to list backups.
  2. Delete a backup.
         
         gcloud backup-dr backups delete BACKUP_ID \
           --backup-vault=BACKUPVAULT_NAME \
           --project=PROJECT_ID \
           --location=LOCATION \
           --data-source=DATA_SOURCE
         

Replace the following: 

     * `BACKUP_ID`: the ID of the backup.
     * `BACKUPVAULT_NAME`: the name of the backup vault where the backups are stored.
     * `PROJECT_ID`: the name of the project.
     * `LOCATION`:the location of the backup.
     * `DATA_SOURCE`: the ID of the data source that you want to delete a backup from.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
