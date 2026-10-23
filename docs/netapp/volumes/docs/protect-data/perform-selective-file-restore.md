---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/perform-selective-file-restore/
title: Perform a selective file restore \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:11.016446+00:00
---

# Perform a selective file restore  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/perform-selective-file-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Perform a selective file restore Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to perform a [selective file restore](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#selective_file_restore).

## Before you begin

Review the following prerequisites before you perform a selective file restore:

  * **Snapshot configuration** : the snapshot directory of the target volume to which the restore is initiated must be visible. In the **Create new volume from backup** page, select the **Make snapshot directory visible** checkbox. For more information, see [Create a new volume](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-volume-from-backup#create_a_new_volume_from_a_backup).

  * **Google Cloud CLI version** : to access selective file restore, make sure your Google Cloud CLI version is at least **540.0.0**.

To verify and update Google Cloud CLI version:

    1. Check your Google Cloud CLI version:
           
           gcloud --version
           

    2. If your Google Cloud CLI version is older than 540.0.0, update it:
           
           gcloud components update
           




## Perform a selective file restore

You can use selective file restore to recover files in the following ways:

  * Restore files to the source volume and the same source directory.

  * Restore files to the source volume in a different directory.

  * Restore files to a new volume in a directory of your choice.




Selective file restore supports both in-region and cross-region backups. This procedure describes three different cases:

  * In-region restore to the source volume in the same source directory.

  * Cross-region restore to a new volume.

  * In-place restore to a new volume.




### Case 1: In-region restore to the source volume in the same source directory

Use the following instructions to perform an in-region selective file restore using the Google Cloud CLI.

### gcloud

To perform a selective file restore:
    
    
    gcloud netapp volumes restore-backup-files DESTINATION_VOLUME_NAME \
      --location=LOCATION --project=PROJECT_ID \
      --backup=projects/PROJECT_ID/locations/LOCATION/backupVaults/VAULT_NAME/backups/BACKUP_NAME \
      --file-list=FILE_LIST \
      --restore-destination-path=RESTORE_DESTINATION_PATH

Replace the following information:

  * `DESTINATION_VOLUME_NAME`: the name of the destination volume for the restore operation. This can be the original volume from which the backup was taken or a new volume.

  * `LOCATION`: the region where the volume resides.

  * `PROJECT_ID`: the ID of the project where the volume and storage pool is created.

  * `VAULT_NAME`: the name of the backup vault. Both in-region and cross-region backup vaults are supported.

  * `BACKUP_NAME`: the name of the backup which contains the files to be restored.

  * `FILE_LIST`: a comma-separated list of file paths in the chosen backup which needs to be restored.

  * `RESTORE_DESTINATION_PATH`: Optional: the specific path where the files will be restored. If no path is provided in this parameter, an in-place restore is performed.

**Note:** For the `--file-list` parameter, specify the source path of the files from the root of the mount point. Regardless of whether SMB or NFS protocol is used, the paths for source files and destination must follow UNIX representation.



Example:

Consider a selective file restore operation performed on a backup of a source volume named `sfr-demo-vol-1`. This source volume is backed up to `sfr-demo-backup-1` within the backup vault named `sfr-demo-vault-in-region`.

The source volume contains three text files:

  * `1.txt`

  * `2.txt`

  * `directory/3.txt`




A backup, `sfr-demo-backup-1`, has been identified within the in-region backup vault. The file `directory/3.txt` and its parent directory are removed from the source volume. A restore operation is then performed with specific parameters.

The file `directory/3.txt` from `sfr-demo-backup-1` will be restored to the source volume.

**Important:** Before running the restore operation, make sure that the destination directory `directory` is created in the source volume. Otherwise, the restore operation fails.

Restore the file:
    
    
    gcloud netapp volumes restore-backup-files sfr-demo-vol-1
    --location=us-central1 --project=my-project
    --backup=projects/my-project/locations/us-central1/backupVaults/sfr-demo-vault-in-region/backups/sfr-demo-backup-1
    --file-list=/directory/3.txt --restore-destination-path=/directory/

You will be prompted to confirm the restore operation:
    
    
    You are about to restore files from a backup to Volume
    projects/my-project/locations/us-central1/volumes/sfr-demo-vol-1.
    Are you sure?
    
    Do you want to continue (Y/n)? Y

The operation completes successfully:
    
    
    Waiting for [operation-1758048175178-63eef7cfac198-a94afb9b-913b60d5] to finish...done.
    '@type': type.googleapis.com/google.cloud.netapp.v1.RestoreBackupFilesResponse

### Case 2: Cross-region restore to a new volume in a new directory

Use the following instructions to perform a cross-region selective file restore using the Google Cloud CLI.

### gcloud

To perform a selective file restore:
    
    
    gcloud netapp volumes restore-backup-files DESTINATION_VOLUME_NAME \
      --location=LOCATION --project=PROJECT_ID \
      --backup=projects/PROJECT_ID/locations/LOCATION/backupVaults/VAULT_NAME/backups/BACKUP_NAME \
      --file-list=FILE_LIST \
      --restore-destination-path=RESTORE_DESTINATION_PATH

Replace the following information:

  * `DESTINATION_VOLUME_NAME`: the name of the destination volume for the restore operation. This can be the original volume from which the backup was taken or a new volume.

  * `LOCATION`: the region where the volume resides.

  * `PROJECT_ID`: the ID of the project where the volume and storage pool is created.

  * `VAULT_NAME`: the name of the backup vault. Both in-region and cross-region backup vaults are supported.

  * `BACKUP_NAME`: the name of the backup which contains the files to be restored.

  * `FILE_LIST`: a comma-separated list of file paths in the chosen backup which needs to be restored.

  * `RESTORE_DESTINATION_PATH`: Optional: the specific path where the files will be restored. If no path is provided in this parameter, an in-place restore is performed.

**Note:** For the `--file-list` parameter, specify the source path of the files from the root of the mount point. Regardless of whether SMB or NFS protocol is used, the paths for source files and destination must follow UNIX representation.



Example:

Consider a selective file restore operation performed on a backup of a source volume named `sfr-demo-vol-2`. This source volume is backed up to `sfr-demo-backup` within the backup vault named `sfr-demo-vault-cross-region`.

The source volume contains two text files:

  * `1.txt`

  * `2.txt`




A backup, `sfr-demo-backup`, has been identified in a cross-region backup vault, with `us-central1` as the source region and `us-east4` as the destination region. After the backup was created, the file `1.txt` was removed from the source volume.

The file `1.txt` from `sfr-demo-backup` will be restored to a new volume named `sfr-demo-vol-3` in a new directory called `test`.

**Important:** Before running the restore operation, make sure the destination directory `test` is created in a new volume `sfr-demo-vol-3`. Otherwise, the restore operation fails.

Restore the file:
    
    
    gcloud netapp volumes restore-backup-files sfr-demo-vol-3
    --location=us-central1 --project=my-project
    --backup=projects/my-project/locations/us-central1/backupVaults/sfr-demo-vault-cross-region/backups/sfr-demo-backup
    --file-list=/1.txt --restore-destination-path=/test

You will be prompted to confirm the restore operation:
    
    
    You are about to restore files from a backup to Volume
    projects/my-project/locations/us-central1/volumes/sfr-demo-vol-3.
    Are you sure?
    
    Do you want to continue (Y/n)? Y

After confirmation, the operation is successful.
    
    
    Waiting for [operation-1758050930422-63ef02134743f-8761c12f-b05a405e] to finish...done.
    '@type': type.googleapis.com/google.cloud.netapp.v1.RestoreBackupFilesResponse

### Case 3: In-place restore to a new volume

Use the following instructions to perform an in-place selective file restore using the Google Cloud CLI.

### gcloud

To perform a selective file restore:
    
    
    gcloud netapp volumes restore-backup-files DESTINATION_VOLUME_NAME \
      --location=LOCATION --project=PROJECT_ID \
      --backup=projects/PROJECT_ID/locations/LOCATION/backupVaults/VAULT_NAME/backups/BACKUP_NAME \
      --file-list=FILE_LIST

Replace the following information:

  * `DESTINATION_VOLUME_NAME`: the name of the destination volume for the restore operation. This can be the original volume from which the backup was taken or a new volume.

  * `LOCATION`: the region where the volume resides.

  * `PROJECT_ID`: the ID of the project where the volume and storage pool is created.

  * `VAULT_NAME`: the name of the backup vault. Both in-region and cross-region backup vaults are supported.

  * `BACKUP_NAME`: the name of the backup which contains the files to be restored.

  * `FILE_LIST`: a comma-separated list of file paths in the chosen backup which needs to be restored.

**Note:** For the `--file-list` parameter, specify the source path of the files from the root of the mount point. Regardless of whether SMB or NFS protocol is used, the paths for source files and destination must follow UNIX representation.



Example:

Consider a selective file restore operation performed on a backup of a source volume named `sfr-demo-vol-2`. This source volume is backed up to `sfr-demo-backup` within the backup vault named `sfr-demo-vault-cross-region`.

The source volume contains two text files:

  * `1.txt`

  * `2.txt`




A backup, `sfr-demo-backup`, has been identified in a cross-region backup vault, with `us-central1` as the source region and `us-east4` as the destination region. After the backup was created, the file `1.txt` was removed from the source volume.

The file `1.txt` from `sfr-demo-backup` will be restored to a new volume named `sfr-demo-vol-3`, but the directory for the restore operation won't be specified.

**Important:** Before running an in-place restore, make sure that the destination volume `sfr-demo-vol-3` has the exact directory where the file was originally backed up.

Restore the file:
    
    
    gcloud netapp volumes restore-backup-files sfr-demo-vol-3
    --location=us-central1 --project=my-project
    --backup=projects/my-project/locations/us-central1/backupVaults/sfr-demo-vault-cross-region/backups/sfr-demo-backup
    --file-list=/1.txt

You will be prompted to confirm the restore operation:
    
    
    You are about to restore files from a backup to Volume
    projects/my-project/locations/us-central1/volumes/sfr-demo-vol-3.
    Are you sure?
    
    Do you want to continue (Y/n)? Y

After confirmation, the operation is successful.
    
    
    Waiting for [operation-1758875604584-63fb0239d87b7-1035ba74-caed1838] to finish...done.
    '@type': type.googleapis.com/google.cloud.netapp.v1.RestoreBackupFilesResponse

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
