---
url: https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/delete/
title: gcloud backup-dr backup-vaults delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:41:26.369335+00:00
---

# gcloud backup-dr backup-vaults delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud backup-dr backup-vaults delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud backup-dr backup-vaults delete - delete the specified Backup Vault 
SYNOPSIS
    

`gcloud backup-dr backup-vaults delete` (`BACKUP_VAULT` : `--location`=`LOCATION`) [`--allow-missing`] [`--no-async`] [`--ignore-backup-plan-references`] [`--ignore-inactive-datasources`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Delete the specified Backup Vault. 
EXAMPLES
     To delete a backup vault ``BACKUP_VAULT`` in location ``MY_LOCATION``, run: 
    
    
    gcloud backup-dr backup-vaults delete BACKUP_VAULT --location=MY_LOCATION

To override restrictions against the deletion of a backup vault ``BACKUP_VAULT`` containing inactive datasources in location ``MY_LOCATION``, run: 
    
    
    gcloud backup-dr backup-vaults delete BACKUP_VAULT --location=MY_LOCATION --ignore-inactive-datasources

To override restrictions against the deletion of a backup vault ``BACKUP_VAULT`` containing backup plan references in location ``MY_LOCATION``, run: 
    
    
    gcloud backup-dr backup-vaults delete BACKUP_VAULT --location=MY_LOCATION --ignore-backup-plan-references

POSITIONAL ARGUMENTS
    

Backup Vault resource - Name of the backup vault to delete. Before you delete, take a look at the prerequisites [here](https://cloud.google.com/backup-disaster-recovery/docs/configuration/decommission). The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup_vault` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKUP_VAULT`
     ID of the Backup Vault or fully qualified identifier for the Backup Vault. 

To set the `name` attribute: 

  * provide the argument `backup_vault` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Backup Vault. 

To set the `location` attribute: 

  * provide the argument `backup_vault` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


FLAGS
    

`--allow-missing`
     Allow idempotent deletion of backup vault. The request will still succeed in case the backup vault does not exist. 
`--no-async`
     Wait for the operation in progress to complete. 
`--ignore-backup-plan-references`
     If set, the following restrictions against deletion of the backup vault instance can be overridden: * deletion of a backup vault instance being actively referenced by a backup plan. 
`--ignore-inactive-datasources`
     If set, the following restrictions against deletion of the backup vault instance can be overridden: * deletion of a backup vault instance containing no backups,but still contains empty datasources. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the backupdr/v1 API. The full documentation for this API can be found at: <https://cloud.google.com/backup-disaster-recovery>
BRIEF
     Deletes a specific backup vault 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha backup-dr backup-vaults delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-vaults/delete)
    
    
    [gcloud beta backup-dr backup-vaults delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/backup-vaults/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
