---
url: https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update/
title: gcloud backup-dr backup-vaults update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:41:26.213198+00:00
---

# gcloud backup-dr backup-vaults update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/backup-vaults/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud backup-dr backup-vaults update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud backup-dr backup-vaults update - update a Backup and DR backup vault 
SYNOPSIS
    

`gcloud backup-dr backup-vaults update` (`BACKUP_VAULT` : `--location`=`LOCATION`) [`--access-restriction`=`ACCESS_RESTRICTION`] [`--no-async`] [`--backup-min-enforced-retention`=`BACKUP_MIN_ENFORCED_RETENTION`] [`--description`=`DESCRIPTION`] [`--effective-time`=`EFFECTIVE_TIME`] [`--force-update`] [`--force-update-access-restriction`] [`--unlock-backup-min-enforced-retention`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a Backup and DR backup vault. 
EXAMPLES
     To update a backup vault BACKUP_VAULT in location MY_LOCATION with one update field, run: 
    
    
    gcloud backup-dr backup-vaults update BACKUP_VAULT --location=MY_LOCATION --effective-time="2024-03-22"

To update a backup vault BACKUP_VAULT in location MY_LOCATION with multiple update fields, run: 
    
    
    gcloud backup-dr backup-vaults update BACKUP_VAULT --location=MY_LOCATION --backup-min-enforced-retention="400000s" --description="Updated backup vault"

POSITIONAL ARGUMENTS
    

Backup Vault resource - Name of the existing backup vault to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

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
    

`--access-restriction`=`ACCESS_RESTRICTION`
     Authorize certain sources and destinations for data being sent into, or restored from the current backup vault. 

Access restrictions can be modified to be more or less restrictive. 
    
    
    ::: More restrictive access restriction update will fail by default if there will be non compliant Data Sources.
    To allow such updates, use the --force-update-access-restriction flag.
    :::  For Google Cloud Console resources, the following changes are allowed to make access restrictions more restrictive:
        *   `UNRESTRICTED` to `WITHIN_PROJECT` / `WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA` / `WITHIN_ORGANIZATION`
        *   `WITHIN_PROJECT` to `WITHIN_ORGANIZATION` / `WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA`
    
    
    ::: For Management Server resources, the following changes are allowed to make access restrictions more restrictive:
        *   `UNRESTRICTED` to `WITHIN_PROJECT` / `WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA` / `WITHIN_ORGANIZATION`
        *   `WITHIN_PROJECT` to `WITHIN_ORGANIZATION` / `WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA`
    
    
    :::   For both Google Cloud Console and Management Server resources, the following changes are allowed to make access restrictions more restrictive:
        *   `UNRESTRICTED` to `WITHIN_PROJECT` / `WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA` / `WITHIN_ORGANIZATION`
        *   `WITHIN_PROJECT` to `WITHIN_ORGANIZATION` / `WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA`
    
    
    ::: For Google Cloud Console resources,  the following changes are allowed to make access restrictions less restrictive:
        *   `WITHIN_ORGANIZATION` to `UNRESTRICTED` / `WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA`
        *   `WITHIN_PROJECT` to `UNRESTRICTED`
        *   `WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA` to `UNRESTRICTED`
    
    
    ::: For Management Server resources, the following changes are allowed to make access restrictions less restrictive:
        *   `WITHIN_ORG_BUT_UNRESTRICTED_FOR_BA` to `UNRESTRICTED`

`ACCESS_RESTRICTION` must be one of: `within-project`, `within-org`, `unrestricted`, `within-org-but-unrestricted-for-ba`. 

`--no-async`
     Wait for the operation in progress to complete. 
`--backup-min-enforced-retention`=`BACKUP_MIN_ENFORCED_RETENTION`
     Backups will be kept for this minimum period before they can be deleted. Once the effective time is reached, the enforced retention period cannot be decreased or removed. The value must be specified in relative time format (e.g. p1d, p1m, p1m1d). 
`--description`=`DESCRIPTION`
     Optional description for the backup vault (2048 characters or less). 
`--effective-time`=`EFFECTIVE_TIME`
     The time at which the enforced retention period becomes locked. This flag is mutually exclusive with --unlock-backup-min-enforced-retention. 
`--force-update`
     If set, allow update to extend the minimum enforced retention for backup vault. This overrides the restriction against conflicting retention periods. This conflict may occur when the expiration schedule defined by the associated backup plan is shorter than the minimum retention set by the backup vault. 
`--force-update-access-restriction`
     If set, the access restriction can be updated even if there are non-compliant data sources. Backups for those data sources will fail afterward. 
`--unlock-backup-min-enforced-retention`
     Removes the lock on the backup minimum enforced retention period, and resets the effective time. When unlocked, the enforced retention period can be changed at any time. This flag is mutually exclusive with --effective-time. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the backupdr/v1 API. The full documentation for this API can be found at: <https://cloud.google.com/backup-disaster-recovery>
BRIEF
     Updates a Backup and DR backup vault. 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha backup-dr backup-vaults update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-vaults/update)
    
    
    [gcloud beta backup-dr backup-vaults update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/backup-vaults/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
