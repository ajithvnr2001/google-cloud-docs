---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/volumes/restore-backup-files/
title: gcloud beta netapp volumes restore-backup-files \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:56.239736+00:00
---

# gcloud beta netapp volumes restore-backup-files  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/volumes/restore-backup-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta netapp volumes restore-backup-files Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta netapp volumes restore-backup-files - restore specific files from a backup to a Volume 
SYNOPSIS
    

`gcloud beta netapp volumes restore-backup-files` (`VOLUME` : `--location`=`LOCATION`) `--file-list`=`FILE_LIST`,[`FILE_LIST`,…] (`--backup`=`BACKUP` : `--backup_vault`=`BACKUP_VAULT`) [`--async`] [`--restore-destination-path`=`RESTORE_DESTINATION_PATH`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Restore specific files from a backup to a Volume 
EXAMPLES
     The following command restores file1.txt and file2.txt from the given backup to a Volume named NAME to the directory /path/to/destination/directory. 
    
    
    gcloud beta netapp volumes restore-backup-files NAME --location=us-central1 --backup=backup-1 --file-list=file1.txt,file2.txt --restore-destination-path=/path/to/destination/directory

POSITIONAL ARGUMENTS
    

Volume resource - The Volume to restore into. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `volume` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`VOLUME`
     ID of the volume or fully qualified identifier for the volume. 

To set the `volume` attribute: 

  * provide the argument `volume` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the volume. 

To set the `location` attribute: 

  * provide the argument `volume` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


REQUIRED FLAGS
    

`--file-list`=`FILE_LIST`,[`FILE_LIST`,…]
     List of files to be restored in the form of their absolute path as in source volume. 
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
`--restore-destination-path`=`RESTORE_DESTINATION_PATH`
     Name of the absolute directory path in the destination volume.. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud netapp volumes restore-backup-files](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/restore-backup-files)
    
    
    [gcloud alpha netapp volumes restore-backup-files](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/netapp/volumes/restore-backup-files)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
