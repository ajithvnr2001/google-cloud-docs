---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/memorystore/instances/reschedule-maintenance/
title: gcloud beta memorystore instances reschedule-maintenance \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:42.091937+00:00
---

# gcloud beta memorystore instances reschedule-maintenance  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/memorystore/instances/reschedule-maintenance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta memorystore instances reschedule-maintenance Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta memorystore instances reschedule-maintenance - reschedule maintenance window for an instance 
SYNOPSIS
    

`gcloud beta memorystore instances reschedule-maintenance` (`INSTANCE` : `--location`=`LOCATION`) `--reschedule-type`=`RESCHEDULE_TYPE` [`--async`] [`--schedule-time`=`SCHEDULE_TIME`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Reschedule maintenance window for an instance. 
EXAMPLES
     To reschedule maintenance window for an instance with the name `my-instance` in region `us-central-1` with immediate, run: 
    
    
    gcloud beta memorystore instances reschedule-maintenance `my-instance` --project=my-project --location=us-central1 --reschedule-type=IMMEDIATE

POSITIONAL ARGUMENTS
    

Instance resource - Name of the instance to reschedule maintenance for: `projects/{project}/locations/{location_id}/instances/{instance}` The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`INSTANCE`
     ID of the instance or fully qualified identifier for the instance. 

To set the `instance` attribute: 

  * provide the argument `instance` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--location`=`LOCATION`
     The location id of the instance resource. 

To set the `location` attribute: 

  * provide the argument `instance` on the command line with a fully specified name; 
  * provide the argument `--location` on the command line. 


REQUIRED FLAGS
    

`--reschedule-type`=`RESCHEDULE_TYPE`
     If reschedule type is SPECIFIC_TIME, schedule_time must be set. `RESCHEDULE_TYPE` must be one of: 

`immediate`
     If the user wants to schedule the maintenance to happen now. 
`specific-time`
     If the user wants to reschedule the maintenance to a specific time. 
OPTIONAL FLAGS
    

`--async`
     Return immediately, without waiting for the operation in progress to complete. 
`--schedule-time`=`SCHEDULE_TIME`
     Timestamp when the maintenance shall be rescheduled to if reschedule_type=SPECIFIC_TIME, in RFC 3339 format. Example: `2012-11-15T16:19:00.094Z`. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

API REFERENCE
     This command uses the `memorystore/v1beta` API. The full documentation for this API can be found at: <https://cloud.google.com/memorystore/>
NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud memorystore instances reschedule-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/memorystore/instances/reschedule-maintenance)
    
    
    [gcloud alpha memorystore instances reschedule-maintenance](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/memorystore/instances/reschedule-maintenance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
