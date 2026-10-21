---
url: https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/backup-plan-associations/delete/
title: gcloud backup-dr backup-plan-associations delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:41:24.548484+00:00
---

# gcloud backup-dr backup-plan-associations delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/backup-dr/backup-plan-associations/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud backup-dr backup-plan-associations delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud backup-dr backup-plan-associations delete - delete the specified backup plan association 
SYNOPSIS
    

`gcloud backup-dr backup-plan-associations delete` (`BACKUP_PLAN_ASSOCIATION` : `--location`=`LOCATION` `--workload-project`=`WORKLOAD_PROJECT`) [`--async`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Delete the specified backup plan association. 
EXAMPLES
     To delete a backup plan association `sample-bpa` in project `sample-project` and location `us-central1` , run: 
    
    
    gcloud backup-dr backup-plan-associations delete sample-bpa --project=sample-project --location=us-central1

POSITIONAL ARGUMENTS
    

Backup Plan Association resource - Name of the backup plan association to delete. The arguments in this group can be used to specify the attributes of this resource. 

This must be specified. 

`BACKUP_PLAN_ASSOCIATION`
     ID of the Backup Plan Association or fully qualified identifier for the Backup Plan Association. 

To set the `name` attribute: 

  * provide the argument `backup_plan_association` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location of the Backup Plan Association. 

To set the `location` attribute: 

  * provide the argument `backup_plan_association` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


`--workload-project`=`WORKLOAD_PROJECT`
     Cloud project id for the Backup Plan Association. 

To set the `workload-project` attribute: 

  * provide the argument `backup_plan_association` on the command line with a fully specified name; 
  * provide the argument `--workload-project` on the command line; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 


FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. The default is `True`. Enabled by default, use `--no-async` to disable. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

BRIEF
     Delete a specific backup plan association 
NOTES
     These variants are also available: 
    
    
    [gcloud alpha backup-dr backup-plan-associations delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backup-plan-associations/delete)
    
    
    [gcloud beta backup-dr backup-plan-associations delete](https://docs.cloud.google.com/sdk/gcloud/reference/beta/backup-dr/backup-plan-associations/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
