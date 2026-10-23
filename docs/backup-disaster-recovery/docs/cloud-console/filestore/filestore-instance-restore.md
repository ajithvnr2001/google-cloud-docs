---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-restore/
title: Restore a Filestore instance from a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:44.894479+00:00
---

# Restore a Filestore instance from a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore a Filestore instance from a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This page helps you to restore a Filestore instance from a backup vault in the Google Cloud console.

## Before you begin

  * Grant the following IAM roles for the user who performs the restore in the backup vault project.

    * Backup and DR Restore User (`roles/backupdr.restoreUser`) for both backup vault.
    * Filestore Editor (`roles/file.editor`) for only the target.

These predefined roles contain the permissions required to access the backup vault in the Filestore project. For specific permissions, see the following list.

    * `backupdr.bvbackups.useReadOnlyForFilestoreInstance`
    * `backupdr.backupVaults.get`
    * `backupdr.backupVaults.list`
    * `backupdr.bvbackups.list`
    * `backupdr.bvdataSources.get`
    * `backupdr.bvdataSources.list`
    * `backupdr.bvbackups.get`

To restore an instance, a user must have the following permissions:

    * `backupdr.bvbackups.useReadOnlyForFilestoreInstance` on the backup resource.

    * `file.instances.create` on the target project where the instance will be restored.




For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Caution:** If your backups are stored in a CMEK-enabled backup vault, you cannot restore a backup if the **Cloud KMS CryptoKey Encrypter/Decrypter** (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) IAM role is revoked from the Backup and DR service agent (P4SA) of the vault project on the backup vault's KMS key. 

## Considerations

  * By default, a Filestore instance restored from a CMEK-encrypted backup will be restored as a GMEK instance unless a CMEK key is specified during restore.

  * Because Cloud Key Management Service keys are regional, when you create a new instance and restore a backup to a different region, you must provide a different Cloud Key Management Service key from that target region. This does not apply when restoring to an existing instance.

  * Backups can be restored even if the original workload project is deleted, because decryption permissions are anchored to the Backup and DR service agent (P4SA) in the vault project.




## Limitations

  * **Cross-project restore monitoring** : Backup and DR doesn't support monitoring cross-project Filestore restores. If you restore a Filestore backup to a different project, the restore operation runs, but its progress and completion status don't appear in the Backup and DR **Jobs** page in the vault project. To check the status of a cross-project restore, go to the target project and check the status of the Filestore instance.

  * **Regional availability for restore monitoring** : you can monitor restore jobs only in regions where both Filestore and Backup and DR are available.




## Restore a Filestore instance

Use the following instructions to restore a Filestore instance. You can check the status of the restore job from the **Jobs** page. For more information, see [Monitor backup and restore jobs in Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console).

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

All Filestore instances with vaulted backups are listed here.

  2. Select the instance to restore and click the action icon to select the **Restore** action. The **Restore page** appears.

  3. On the **Restore** page, verify that the instance you want to restore is listed in the **Resource name** field.

  4. In the **Backup** field, click **Browse**.

  5. Select the backup that you want to restore from and click **Done**.

  6. In the **Restore project name** field the current project is prepopulated, but you can click **Browse** to choose another project.

  7. Click **Continue**.

     * The **Restore backup to a new instance** page appears. The instance properties are pre-populated based on the source instance properties. You can modify the properties of the new instance.
  8. Click **Restore** to create a new Filestore instance from the selected backup.

  9. To view the status of the restore job, go to the Backup and DR **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/backupdr/jobs)




###  gcloud 

  1. To get the backup vault service account, use the following command.
         
         gcloud backup-dr backup-vaults describe BACKUPVAULT_NAME \
             --location=LOCATION
         

Replace the following:

     * BACKUPVAULT_NAME: the backup vault name you want to restore data from.
     * LOCATION: the location of the backup vault.
  2. To restore a Filestore instance, use the following commands.

The restore command is run from the Filestore service.
         
         gcloud filestore instances create INSTANCE_NAME \
           --file-share="capacity=CAPACITY,name=SHARE_NAME,source-backupdr-backup=BACKUPDR_BACKUP_FULL_PATH" \
           --network="name=default" \
           --location=LOCATION \
           --project=PROJECT_NAME \
           --tier=TIER
         

Replace the following:

     * `INSTANCE_NAME`: The name of the Filestore instance to create.
     * `CAPACITY`: The capacity of the file share.
     * `SHARE_NAME`: The name of the file share.
     * `BACKUPDR_BACKUP_FULL_PATH`: The full path of the Backup and DR backup to restore from.
     * `LOCATION`: The location to create the Filestore instance in.
     * `PROJECT_NAME`: The project to create the Filestore instance in.
     * `TIER`: The tier of the Filestore instance.



## Monitor restore jobs

When you restore a Filestore instance, Backup and DR automatically tracks the job. You can monitor the progress and status of the job in the Google Cloud console.

To view the progress and status of the restore job:

  1. In the Google Cloud console, go to the Backup and DR **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/backupdr/jobs)

  2. Look for the job with the **Resource type** set to `Filestore` and **Job category** set to `Restore`.




You can view restore job logs in the backup vault project where the backup is stored. You can view the details of a job on the Backup and DR **Jobs** page and in Cloud Logging.

For more information, see [Monitor backup and restore jobs in Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console).

## What's next

  * [Back up Filestore instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-backup)
  * [Manage data sources in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-datasource-manage)
  * [Manage backups in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage)
  * [Monitor backup and restore jobs in Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
