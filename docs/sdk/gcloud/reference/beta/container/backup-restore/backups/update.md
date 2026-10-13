---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backups/update/
title: gcloud beta container backup-restore backups update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:06.679759+00:00
---

# gcloud beta container backup-restore backups update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/backups/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta container backup-restore backups update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta container backup-restore backups update - update a backup 
SYNOPSIS
    

`gcloud beta container backup-restore backups update` (`BACKUP` : `--backup-plan`=`BACKUP_PLAN` `--location`=`LOCATION`) [`--async`] [`--delete-lock-days`=`DELETE_LOCK_DAYS`] [`--description`=`DESCRIPTION`] [`--etag`=`ETAG`] [`--retain-days`=`RETAIN_DAYS`] [`--update-labels`=[`KEY`=`VALUE`,…]] [`--clear-labels` | `--remove-labels`=[`KEY`,…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Update a Backup for GKE backup. 
EXAMPLES
     To update a backup ``my-backup`` in project ``my-project`` in location ``us-central1`` under backup plan ``my-backup-plan`` to add new description, run: 
    
    
    gcloud beta container backup-restore backups update 'my-backup' --backup-plan=my-backup-plan --project=my-project --location=us-central1 --description="New description"

POSITIONAL ARGUMENTS
    

Backup resource - Name of the backup to update. The name may be provided either as a relative name, e.g. `projects/<project>/locations/<location>/backupPlans/<backupPlan>/backups/<backup>` or as a single ID name (with the parent resources provided via options or through properties), e.g. `BACKUP --project=<project> --location=<location> --backup-plan=<backupPlan>`. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKUP`
     ID of the backup or fully qualified identifier for the backup. 

To set the `backup` attribute: 

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
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--delete-lock-days`=`DELETE_LOCK_DAYS`
     Delete lock days specifies the number of days from the createTime of this Backup before which deletion will be blocked. Must be >= the value in the backup plan. If not specified, inherited from the backup plan. Manual creation of a backup with this field unspecified causes the service to use the value of backupPlan.RetentionPolicy.backupDeleteBlockDays. Creation of a backup with this field set to a value SMALLER than backupPlan.RetentionPolicy.backupDeleteBlockDays results in an invalid response from the service. This field MUST be an int value between 0-90(inclusive). This field may only be INCREASED in an update command, or an invalid response will be returned by the service. 
`--description`=`DESCRIPTION`
     Optional text description for the backup. 
`--etag`=`ETAG`
     The etag is used for optimistic concurrency control as a way to help prevent simultaneous updates or deletes of a resource from overwriting each other. 
`--retain-days`=`RETAIN_DAYS`
     Retain days specifies the desired number of days from the createTime of this backup after which it will be automatically deleted. If not specified or set to 0, it means the backup will NOT be automatically deleted. Manual creation of a backup with this field unspecified causes the service to use the value of backupPlan.retentionPolicy.backupRetainDays. Creation of a backup with this field set to a value SMALLER than deleteLockDays results in an invalid response from the service. This field may ONLY be increased in an Update command, or an invalid response will be returned by the service immediately. Default to 0. 
`--update-labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to update. If a label exists, its value is modified. Otherwise, a new label is created. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

At most one of these can be specified: 

`--clear-labels`
     Remove all labels. If `--update-labels` is also specified then `--clear-labels` is applied first. 

For example, to remove all labels: 
    
    
    gcloud beta container backup-restore backups update --clear-labels

To remove all existing labels and create two new labels, ``foo`` and ``baz``: 
    
    
    gcloud beta container backup-restore backups update --clear-labels --update-labels foo=bar,baz=qux

`--remove-labels`=[`KEY`,…]
     List of label keys to remove. If a label does not exist it is silently ignored. If `--update-labels` is also specified then `--update-labels` is applied first. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `gkebackup/v1` API. The full documentation for this API can be found at: <https://cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke>
NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud alpha container backup-restore backups update](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/backup-restore/backups/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-23 UTC."],[],[]] 
