---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/backup-vaults/backups/describe/
title: gcloud beta netapp backup-vaults backups describe \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:51.026474+00:00
---

# gcloud beta netapp backup-vaults backups describe  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/backup-vaults/backups/describe/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta netapp backup-vaults backups describe Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta netapp backup-vaults backups describe - describe a Cloud NetApp Backup 
SYNOPSIS
    

`gcloud beta netapp backup-vaults backups describe` (`BACKUP` : `--location`=`LOCATION`) [`--backup-vault`=`BACKUP_VAULT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Describe a Cloud NetApp Backup. 
EXAMPLES
     The following command describes a Backup named BACKUP in the given location and backup vault: 
    
    
    gcloud beta netapp backup-vaults backups describe NAME --location=us-central1 --backup-vault=BACKUP_VAULT

POSITIONAL ARGUMENTS
    

Backup resource - The Backup to describe. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `backup_vault` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--backup-vault` on the command line. 



This must be specified. 

`BACKUP`
     ID of the backup or fully qualified identifier for the backup. 

To set the `backup` attribute: 

  * provide the argument `backup` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the backup. 

To set the `location` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


FLAGS
    

Backup vault resource - The Backup Vault that the Backup is stored in This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--backup-vault` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--backup-vault` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


`--backup-vault`=`BACKUP_VAULT`
     ID of the backup_vault or fully qualified identifier for the backup_vault. 

To set the `backup_vault` attribute: 

  * provide the argument `--backup-vault` on the command line. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud netapp backup-vaults backups describe](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/backups/describe)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
