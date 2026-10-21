---
url: https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/delete/
title: gcloud sql instances delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:38:47.765749+00:00
---

# gcloud sql instances delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud sql instances delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud sql instances delete - deletes a Cloud SQL instance 
SYNOPSIS
    

`gcloud sql instances delete` `INSTANCE` [`--async`] [`--enable-final-backup`] [`--final-backup-description`=`FINAL_BACKUP_DESCRIPTION`] [`--final-backup-expiry-time`=`FINAL_BACKUP_EXPIRY_TIME` | `--final-backup-retention-days`=`FINAL_BACKUP_RETENTION_DAYS`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Deletes a Cloud SQL instance. 
POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--enable-final-backup`
     Enables the final backup to be taken at the time of instance deletion. 
`--final-backup-description`=`FINAL_BACKUP_DESCRIPTION`
     Provides description for the final backup going to be taken. 
At most one of these can be specified: 

`--final-backup-expiry-time`=`FINAL_BACKUP_EXPIRY_TIME`
     Specifies the time at which the final backup will expire. Maximum time allowed is 365 days. For instances managed by BackupDR, the maximum time allowed is 10 years (3653 days). Format: YYYY-MM-DDTHH:MM:SS. 
`--final-backup-retention-days`=`FINAL_BACKUP_RETENTION_DAYS`
     Specifies number of days to retain final backup. The valid range is between 1 and 365. For instances managed by BackupDR, the valid range is between 1 day and 10 years (3653 days). Default value is 30 days. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha sql instances delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/instances/delete)
    
    
    [gcloud beta sql instances delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/instances/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
