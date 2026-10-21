---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/backups/update/
title: gcloud beta backup-dr backups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:09:02.112658+00:00
---

# gcloud beta backup-dr backups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/backups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta backup-dr backups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta backup-dr backups update - update the specified Backup 
SYNOPSIS
    

`gcloud beta backup-dr backups update` (`BACKUP` : `--backup-vault`=`BACKUP_VAULT` `--data-source`=`DATA_SOURCE` `--location`=`LOCATION`) [`--async`] [`--clear-labels` | `--remove-labels`=`KEY`,[`KEY`,…] | `--update-labels`=[`KEY`=`VALUE`,…]] [`--enforced-retention-end-time`=`ENFORCED_RETENTION_END_TIME` `--expire-time`=`EXPIRE_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update the specified Backup. 
EXAMPLES
     To update the enforced retention of a backup sample-backup in backup vault sample-vault, data source sample-ds, project sample-project and location us-central1, run: 
    
    
    gcloud beta backup-dr backups update sample-backup --backup-vault=sample-vault --data-source=sample-ds --project=sample-project --location=us-central1 --enforced-retention-end-time="2025-02-14T01:10:20Z"

To update the labels on a backup named `my-backup` in the `test-bv` vault and `us-central1` location, run: 
    
    
    gcloud beta backup-dr backups update my-backup --backup-vault=test-bv --location=us-central1 --update-labels=env=prod,team=storage

To remove the `env` label from the same backup, run: 
    
    
    gcloud beta backup-dr backups update my-backup --backup-vault=test-bv --location=us-central1 --remove-labels=env

To clear all labels from the backup, run: 
    
    
    gcloud beta backup-dr backups update my-backup --backup-vault=test-bv --location=us-central1 --clear-labels

POSITIONAL ARGUMENTS
    

Backup resource - Name of the backup to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKUP`
     ID of the Backup or fully qualified identifier for the Backup. 

To set the `name` attribute: 

  * provide the argument `backup` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--backup-vault`=`BACKUP_VAULT`
     The ID of the Backup Vault. 

To set the `backup-vault` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--backup-vault` on the command line. 


`--data-source`=`DATA_SOURCE`
     The ID of the Data Source. 

To set the `data-source` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--data-source` on the command line. 


`--location`=`LOCATION`
     The location of the Backup. 

To set the `location` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
At most one of these can be specified: 

`--clear-labels`
     Remove all labels from the backup. 

If the backup has no labels, this operation is a no-op. 

`--remove-labels`=`KEY`,[`KEY`,…]
     A list of label keys to remove from the backup. 

If a label does not exist, it is silently ignored. 

`--update-labels`=[`KEY`=`VALUE`,…]
     A list of labels to apply to the backup. 

Keys must start with a lowercase letter and contain only lowercase letters, numbers, and hyphens, and must be between 1 and 63 characters long. Values must contain only lowercase letters, numbers, and hyphens, and must be between 0 and 63 characters long. 

For example: `--update-labels=env=prod,team=storage`

Update Backup Flags 
`--enforced-retention-end-time`=`ENFORCED_RETENTION_END_TIME`
     Backups cannot be deleted until this time or later. This period can be extended, but not shortened. It should be specified in the format of "YYYY-MM-DD". 

  * For backup configured with a backup appliance, there are additional restrictions: 1. Enforced retention cannot be extended past the expiry time. 2. Enforced retention can only be updated for finalized backups. 


`--expire-time`=`EXPIRE_TIME`
     The date when this backup is automatically expired. This date can be extended, but not shortened. It should be specified in the format of "YYYY-MM-DD". 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

BRIEF
     Updates a specific backup 
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud backup-dr backups update](https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/backups/update)
    
    
    [gcloud alpha backup-dr backups update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
