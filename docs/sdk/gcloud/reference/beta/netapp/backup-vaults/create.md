---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/backup-vaults/create/
title: gcloud beta netapp backup-vaults create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:51.207771+00:00
---

# gcloud beta netapp backup-vaults create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/backup-vaults/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta netapp backup-vaults create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta netapp backup-vaults create - create a Cloud NetApp Backup Vault 
SYNOPSIS
    

`gcloud beta netapp backup-vaults create` (`BACKUP_VAULT` : `--location`=`LOCATION`) [`--async`] [`--backup-region`=`BACKUP_REGION`] [`--backup-retention-policy`=[`backup-minimum-enforced-retention-days`=`BACKUP-MINIMUM-ENFORCED-RETENTION-DAYS`],[`daily-backup-immutable`=`DAILY-BACKUP-IMMUTABLE`],[`manual-backup-immutable`=`MANUAL-BACKUP-IMMUTABLE`],[`monthly-backup-immutable`=`MONTHLY-BACKUP-IMMUTABLE`],[`weekly-backup-immutable`=`WEEKLY-BACKUP-IMMUTABLE`]] [`--backup-vault-type`=`BACKUP_VAULT_TYPE`] [`--[no-]cross-project-vault`] [`--description`=`DESCRIPTION`] [`--kms-config`=`KMS_CONFIG`] [`--labels`=[`KEY`=`VALUE`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Create a Cloud NetApp Backup Vault. 
EXAMPLES
     The following command creates a Backup Vault named BACKUP_VAULT asynchronously using the specified arguments: 
    
    
    gcloud beta netapp backup-vaults create BACKUP_VAULT --location=LOCATION --async --description="test" The following command creates a Backup Vault named CMEK_BACKUP_VAULT with a KMS config:
    
    
    gcloud beta netapp backup-vaults create CMEK_BACKUP_VAULT --location=LOCATION --kms-config=projects/PROJECT/locations/LOCATION/kmsConfigs/KMS_CONFIG

POSITIONAL ARGUMENTS
    

Backup vault resource - The Backup Vault to create The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
`--backup-region`=`BACKUP_REGION`
     String indicating backup location for the Backup Vault 
`--backup-retention-policy`=[`backup-minimum-enforced-retention-days`=`BACKUP-MINIMUM-ENFORCED-RETENTION-DAYS`],[`daily-backup-immutable`=`DAILY-BACKUP-IMMUTABLE`],[`manual-backup-immutable`=`MANUAL-BACKUP-IMMUTABLE`],[`monthly-backup-immutable`=`MONTHLY-BACKUP-IMMUTABLE`],[`weekly-backup-immutable`=`WEEKLY-BACKUP-IMMUTABLE`]
     Backup Retention Policy of the Backup Vault. 

Backup Retention Policy allows you to configure the retention policy for backups created within this vault. It consists of several fields that govern how long backups are kept and what type of backups are immutable. 

`--backup-vault-type`=`BACKUP_VAULT_TYPE`
     String indicating the type of backup vault. The supported values are: 'IN_REGION','CROSS_REGION' 
`--[no-]cross-project-vault`
     Indicates whether the backup vault is a cross project vault. Use `--cross-project-vault` to enable and `--no-cross-project-vault` to disable. 
`--description`=`DESCRIPTION`
     A description of the Cloud NetApp Backup Vault 
Kms config resource - The resource name of the KMS Config to use for encrypting backups within this backup vault. Format: projects/{project_id}/locations/{location}/kmsConfigs/{kms_config_id} This represents a Cloud resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `--kms-config` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



To set the `location` attribute: 

  * provide the argument `--kms-config` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


`--kms-config`=`KMS_CONFIG`
     ID of the kms_config or fully qualified identifier for the kms_config. 

To set the `kms_config` attribute: 

  * provide the argument `--kms-config` on the command line. 


`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud netapp backup-vaults create](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-vaults/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
