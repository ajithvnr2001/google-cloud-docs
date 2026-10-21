---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backups/create/
title: gcloud beta container backup-restore backups create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:38:12.041418+00:00
---

# gcloud beta container backup-restore backups create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backups/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container backup-restore backups create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container backup-restore backups create - creates a backup 
SYNOPSIS
    

`gcloud beta container backup-restore backups create` (`BACKUP` : `--backup-plan`=`BACKUP_PLAN` `--location`=`LOCATION`) [`--delete-lock-days`=`DELETE_LOCK_DAYS`] [`--description`=`DESCRIPTION`] [`--labels`=[`KEY`=`VALUE`,…]] [`--retain-days`=`RETAIN_DAYS`] [`--async` | `--wait-for-completion`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Creates a Backup for GKE backup. 
EXAMPLES
     To create a backup ``my-backup`` in project ``my-project`` in location ``us-central1`` under backup plan ``my-backup-plan``, run: 
    
    
    gcloud beta container backup-restore backups create my-backup --project=my-project --location=us-central1 --backup-plan=my-backup-plan

To create a backup ``my-backup`` in project ``my-project`` in location ``us-central1`` under backup plan ``my-backup-plan`` and not wait for the resulting operation to finish, run: 
    
    
    gcloud beta container backup-restore backups create my-backup --project=my-project --location=us-central1 --backup-plan=my-backup-plan --async

To create a backup ``my-backup`` in project ``my-project`` in location ``us-central1`` under backup plan ``my-backup-plan`` and wait for the Backup
    
    
    to complete, run:
    
    
    gcloud beta container backup-restore backups create my-backup --project=my-project --location=us-central1 --backup-plan=my-backup-plan --wait-for-completion

POSITIONAL ARGUMENTS
    

Backup resource - Name of the backup to create. Once the backup is created, this name can't be changed. This must be 63 or fewer characters long and must be unique within the project, location, and backup plan. The name may be provided either as a relative name, e.g. `projects/<project>/locations/<location>/backupPlans/<backupPlan>/backups/<backup>` or as a single ID name (with the parent resources provided via options or through properties), e.g. `BACKUP --project=<project> --location=<location> --backup_plan=<backupPlan>`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKUP`
     ID of the backup or fully qualified identifier for the backup. 

To set the `name` attribute: 

  * provide the argument `backup` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--backup-plan`=`BACKUP_PLAN`
     Backup Plan name. 

To set the `backup-plan` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--backup-plan` on the command line; 
  * set the property `gkebackup/backup_plan`. 


`--location`=`LOCATION`
     Google Cloud location. 

To set the `location` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `gkebackup/location`. 


FLAGS
    

`--delete-lock-days`=`DELETE_LOCK_DAYS`
     Delete lock days specifies the number of days from the createTime of this Backup before which deletion will be blocked. Must be >= the value in the backup plan. If not specified, inherited from the backup plan. Manual creation of a backup with this field unspecified causes the service to use the value of backupPlan.RetentionPolicy.backupDeleteBlockDays. Creation of a backup with this field set to a value SMALLER than backupPlan.RetentionPolicy.backupDeleteBlockDays results in an invalid response from the service. This field MUST be an int value between 0-90(inclusive). This field may only be INCREASED in an update command, or an invalid response will be returned by the service. 
`--description`=`DESCRIPTION`
     Optional text description for the backup being created. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

`--retain-days`=`RETAIN_DAYS`
     Retain days specifies the desired number of days from the createTime of this backup after which it will be automatically deleted. If not specified or set to 0, it means the backup will NOT be automatically deleted. Manual creation of a backup with this field unspecified causes the service to use the value of backupPlan.retentionPolicy.backupRetainDays. Creation of a Backup with this field set to a value SMALLER than delete_lock_days results in an invalid response from the service. This field may ONLY be increased in an Update request, or an invalid response will be returned by the service immediately. Default to 0 if not provided. 
At most one of these can be specified: 

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--wait-for-completion`
     Wait for the created backup to complete. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha container backup-restore backups create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/backup-restore/backups/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
