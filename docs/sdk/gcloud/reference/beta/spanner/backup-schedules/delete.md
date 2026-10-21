---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/backup-schedules/delete/
title: gcloud beta spanner backup-schedules delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:39:38.145211+00:00
---

# gcloud beta spanner backup-schedules delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/spanner/backup-schedules/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta spanner backup-schedules delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta spanner backup-schedules delete - delete a Cloud Spanner backup schedule 
SYNOPSIS
    

`gcloud beta spanner backup-schedules delete` (`BACKUP_SCHEDULE` : `--database`=`DATABASE` `--instance`=`INSTANCE`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Delete a Cloud Spanner backup schedule. 
EXAMPLES
     To delete a Cloud Spanner backup schedule, run: 
    
    
    gcloud beta spanner backup-schedules delete backup-schedule-id --instance=instance-id --database=database-id

POSITIONAL ARGUMENTS
    

Backup schedule resource - The Cloud Spanner backup schedule to delete. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `backup_schedule` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`BACKUP_SCHEDULE`
     ID of the backup-schedule or fully qualified identifier for the backup-schedule. 

To set the `backup-schedule` attribute: 

  * provide the argument `backup_schedule` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--database`=`DATABASE`
     The Cloud Spanner database for the backup-schedule. 

To set the `database` attribute: 

  * provide the argument `backup_schedule` on the command line with a fully specified name; 
  * provide the argument `--database` on the command line. 


`--instance`=`INSTANCE`
     The Cloud Spanner instance for the backup-schedule. 

To set the `instance` attribute: 

  * provide the argument `backup_schedule` on the command line with a fully specified name; 
  * provide the argument `--instance` on the command line; 
  * set the property `spanner/instance`. 


GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud spanner backup-schedules delete](https://docs.cloud.google.com/sdk/gcloud/reference/spanner/backup-schedules/delete)
    
    
    [gcloud alpha spanner backup-schedules delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/spanner/backup-schedules/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
