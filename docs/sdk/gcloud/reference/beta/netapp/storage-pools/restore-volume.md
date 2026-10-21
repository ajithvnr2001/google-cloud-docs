---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/storage-pools/restore-volume/
title: gcloud beta netapp storage-pools restore-volume \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:53.663753+00:00
---

# gcloud beta netapp storage-pools restore-volume  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/storage-pools/restore-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta netapp storage-pools restore-volume Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta netapp storage-pools restore-volume - restore a backup to a volume in a specified ONTAP-mode Storage Pool 
SYNOPSIS
    

`gcloud beta netapp storage-pools restore-volume` (`STORAGE_POOL` : `--location`=`LOCATION`) `--volume-uuid`=`VOLUME_UUID` (`--backup`=`BACKUP` : `--backup_vault`=`BACKUP_VAULT`) [`--async`] [`--file-list`=[`FILE_LIST`,…]] [`--restore-destination-path`=`RESTORE_DESTINATION_PATH`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Restores a backup to a volume within the specified Storage Pool. 

This command supports restoring from both Cloud NetApp Volumes backups and GCBDR (BackupDR) backups. 

This command supports both full backup restore and selective file restore: 

`Full Backup Restore`: The `--volume-uuid` must reference a Data Protection (DP) volume where the backup will be restored. 

`File Restore`: The `--volume-uuid` must reference a Read-Write (RW) volume where the file(s) from the backup will be restored. For file restore, `--file-list` and `--restore-destination-path` must be included in the request payload. 

For the complete backup restore, users should first create a Data Protection volume via the ONTAP Mode APIs whereas a Read-Write volume must be created first for selective file restore. 

EXAMPLES
     The following command restores full backup from a backup with full resource name `projects/my-project/locations/us-central1/backupVaults/my-vault/backups/backup-1` to an ONTAP-mode volume with UUID 5dc61a44-3d99-11f1-b8ff-39021cc41d7a in Storage Pool named NAME. 
    
    
    gcloud beta netapp storage-pools restore-volume NAME --location=us-central1 --backup=projects/my-project/locations/us-central1/backupVaults/my-vault/backups/backup-1 --volume-uuid=5dc61a44-3d99-11f1-b8ff-39021cc41d7a

The following command restores full backup from a GCBDR (BackupDR) backup with full resource name `projects/my-project/locations/us-central1/backupVaults/my-vault/dataSources/my-ds/backups/backup-1` to an ONTAP-mode volume with UUID 5dc61a44-3d99-11f1-b8ff-39021cc41d7a in Storage Pool named NAME. 
    
    
    gcloud beta netapp storage-pools restore-volume NAME --location=us-central1 --backup=projects/my-project/locations/us-central1/backupVaults/my-vault/dataSources/my-ds/backups/backup-1 --volume-uuid=5dc61a44-3d99-11f1-b8ff-39021cc41d7a

The following command restores file1.txt from the same backup to an ONTAP-mode volume with UUID 5dc61a44-3d99-11f1-b8ff-39021cc41d7a in Storage Pool named NAME to the directory /my_restore_destination. 
    
    
    gcloud beta netapp storage-pools restore-volume NAME --location=us-central1 --backup=projects/my-project/locations/us-central1/backupVaults/my-vault/backups/backup-1 --volume-uuid=5dc61a44-3d99-11f1-b8ff-39021cc41d7a --file-list=/path/to/file1.txt --restore-destination-path=/my_restore_destination

POSITIONAL ARGUMENTS
    

Storage pool resource - The Storage Pool to restore into. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `storage_pool` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`STORAGE_POOL`
     ID of the storage_pool or fully qualified identifier for the storage_pool. 

To set the `storage_pool` attribute: 

  * provide the argument `storage_pool` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the storage_pool. 

To set the `location` attribute: 

  * provide the argument `storage_pool` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


REQUIRED FLAGS
    

`--volume-uuid`=`VOLUME_UUID`
     The UUID of the ONTAP-mode volume to restore to. 
Backup resource - The Backup from which files are restored back to the Volume. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--backup` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--backup` on the command line with a fully specified name; 
  * set the property `netapp/location`. 



This must be specified. 

`--backup`=`BACKUP`
     ID of the backup or fully qualified identifier for the backup. 

To set the `backup` attribute: 

  * provide the argument `--backup` on the command line. 



This flag argument must be specified if any of the other arguments in this group are specified. 

`--backup_vault`=`BACKUP_VAULT`
     The Backup Vault of the backup. 

To set the `backup_vault` attribute: 

  * provide the argument `--backup` on the command line with a fully specified name; 
  * provide the argument `--backup_vault` on the command line; 
  * provide the argument `--backup-vault` on the command line. 


OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--file-list`=[`FILE_LIST`,…]
     List of files to be restored in the form of their absolute path as in source volume. 
`--restore-destination-path`=`RESTORE_DESTINATION_PATH`
     Name of the absolute directory path in the destination volume. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud netapp storage-pools restore-volume](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/restore-volume)
    
    
    [gcloud alpha netapp storage-pools restore-volume](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/netapp/storage-pools/restore-volume)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-22 UTC."],[],[]] 
