---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/reschedule-maintenance/
title: gcloud alpha sql reschedule-maintenance \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:26:07.136152+00:00
---

# gcloud alpha sql reschedule-maintenance  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/sql/reschedule-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha sql reschedule-maintenance Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha sql reschedule-maintenance - reschedule a Cloud SQL instance's maintenance 
SYNOPSIS
    

`gcloud alpha sql reschedule-maintenance` `INSTANCE` `--reschedule-type`=`RESCHEDULE_TYPE` [`--schedule-time`=`SCHEDULE_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` gcloud alpha sql reschedule-maintenance reschedules a Cloud SQL instance's maintenance. 
EXAMPLES
     To run maintenance on instance `my-instance` immediately, run: 
    
    
    gcloud alpha sql reschedule-maintenance my-instance --reschedule-type=IMMEDIATE

To reschedule maintenance on instance `my-instance` to the next available window, run: 
    
    
    gcloud alpha sql reschedule-maintenance my-instance --reschedule-type=NEXT_AVAILABLE_WINDOW

To reschedule maintenance on instance `my-instance` to 2019-11-07 at 4:00 am UTC, run: 
    
    
    gcloud alpha sql reschedule-maintenance my-instance --reschedule-type=SPECIFIC_TIME --schedule-time=2019-11-07T04:00Z

POSITIONAL ARGUMENTS
    

`INSTANCE`
     Cloud SQL instance ID. 
REQUIRED FLAGS
    

`--reschedule-type`=`RESCHEDULE_TYPE`
     The type of reschedule operation to perform. `RESCHEDULE_TYPE` must be one of: `IMMEDIATE`, `NEXT_AVAILABLE_WINDOW`, `SPECIFIC_TIME`. 
OPTIONAL FLAGS
    

`--schedule-time`=`SCHEDULE_TIME`
     When specifying SPECIFIC_TIME, the date and time at which to schedule the maintenance in ISO 8601 format. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud sql reschedule-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/sql/reschedule-maintenance)
    
    
    [gcloud beta sql reschedule-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/beta/sql/reschedule-maintenance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
