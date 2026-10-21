---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/backup-policies/create/
title: gcloud beta netapp backup-policies create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:48.571980+00:00
---

# gcloud beta netapp backup-policies create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/netapp/backup-policies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta netapp backup-policies create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta netapp backup-policies create - create a Cloud NetApp Backup Policy 
SYNOPSIS
    

`gcloud beta netapp backup-policies create` (`BACKUP_POLICY` : `--location`=`LOCATION`) [`--async`] [`--description`=`DESCRIPTION`] [`--enabled`=`ENABLED`] [`--labels`=[`KEY`=`VALUE`,…]] [`--daily-backup-limit`=`DAILY_BACKUP_LIMIT` `--monthly-backup-limit`=`MONTHLY_BACKUP_LIMIT` `--weekly-backup-limit`=`WEEKLY_BACKUP_LIMIT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Creates a Backup Policy for Cloud NetApp Volumes. 
EXAMPLES
     The following command creates a Backup Policy named BACKUP_POLICY with all possible arguments: 
    
    
    gcloud beta netapp backup-policies create BACKUP_POLICY --location=us-central1 --enabled=true --daily-backup-limit=3 --weekly-backup-limit=5 --monthly-backup-limit=2 --description="first backup policy" --labels=key1=val1

POSITIONAL ARGUMENTS
    

Backup policy resource - The Backup Policy to create The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup_policy` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKUP_POLICY`
     ID of the backup_policy or fully qualified identifier for the backup_policy. 

To set the `backup_policy` attribute: 

  * provide the argument `backup_policy` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the backup_policy. 

To set the `location` attribute: 

  * provide the argument `backup_policy` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line; 
  * set the property `netapp/location`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--description`=`DESCRIPTION`
     A description of the Cloud NetApp Backup Policy 
`--enabled`=`ENABLED`
     The Boolean value indiciating whether backups are made automatically according to the schedules. If enabled, this will be applied to all volumes that have this backup policy attached and enforced on the volume level. If not specified, the default is true. 
`--labels`=[`KEY`=`VALUE`,…]
     List of label KEY=VALUE pairs to add. 

Keys must start with a lowercase character and contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. Values must contain only hyphens (`-`), underscores (`_`), lowercase characters, and numbers. 

Add backup limit arguments. 
`--daily-backup-limit`=`DAILY_BACKUP_LIMIT`
     Maximum number of daily backups to keep. Note that the minimum daily backup limit is 2. 
`--monthly-backup-limit`=`MONTHLY_BACKUP_LIMIT`
     Number of monthly backups to keep. Note that the sum of daily, weekly and monthly backups should be greater than 1 
`--weekly-backup-limit`=`WEEKLY_BACKUP_LIMIT`
     Number of weekly backups to keep. Note that the sum of daily, weekly and monthly backups should be greater than 1 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. This variant is also available: 
    
    
    [gcloud netapp backup-policies create](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/backup-policies/create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
