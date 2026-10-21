---
url: https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/update/
title: gcloud netapp backup-vaults update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:18:12.277786+00:00
---

# gcloud netapp backup-vaults update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud netapp backup-vaults update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud netapp backup-vaults update - update a Cloud NetApp Volumes Backup Vault 
SYNOPSIS
    

`gcloud netapp backup-vaults update` (`BACKUP_VAULT` : `--location`=`LOCATION`) [`--async`] [`--backup-retention-policy`=[`backup-minimum-enforced-retention-days`=`BACKUP-MINIMUM-ENFORCED-RETENTION-DAYS`],[`daily-backup-immutable`=`DAILY-BACKUP-IMMUTABLE`],[`manual-backup-immutable`=`MANUAL-BACKUP-IMMUTABLE`],[`monthly-backup-immutable`=`MONTHLY-BACKUP-IMMUTABLE`],[`weekly-backup-immutable`=`WEEKLY-BACKUP-IMMUTABLE`]] [`--description`=`DESCRIPTION`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Updates a Backup Vault 
EXAMPLES
     The following command updates a Backup Vault instance named BACKUP_VAULT 
    
    
    gcloud netapp backup-vaults update BACKUP_VAULT --location=us-central1 --description="new description" --update-labels=newkey=newval

To update a Backup Vault named BACKUP_VAULT asynchronously, run the following command: 
    
    
    gcloud netapp backup-vaults update BACKUP_VAULT --async --location=us-central1 --description="new description" --update-labels=newkey=newval

POSITIONAL ARGUMENTS
    

Backup vault resource - The Backup Vault to update The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup_vault` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKUP_VAULT`
     ID of the backup_vault or fully qualified identifier for the backup_vault. 

To set the `backup_vault` attribute: 

  * provide the argument `backup_vault` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the backup_vault. 

To set the `location` attribute: 

  * provide the argument `backup_vault` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--backup-retention-policy`=[`backup-minimum-enforced-retention-days`=`BACKUP-MINIMUM-ENFORCED-RETENTION-DAYS`],[`daily-backup-immutable`=`DAILY-BACKUP-IMMUTABLE`],[`manual-backup-immutable`=`MANUAL-BACKUP-IMMUTABLE`],[`monthly-backup-immutable`=`MONTHLY-BACKUP-IMMUTABLE`],[`weekly-backup-immutable`=`WEEKLY-BACKUP-IMMUTABLE`]
     Backup Retention Policy of the Backup Vault. 

Backup Retention Policy allows you to configure the retention policy for backups created within this vault. It consists of several fields that govern how long backups are kept and what type of backups are immutable. 

`--description`=`DESCRIPTION`
     A description of the Cloud NetApp Backup Vault 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud netapp backup-vaults update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud netapp backup-vaults update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta netapp backup-vaults update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/backup-vaults/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
