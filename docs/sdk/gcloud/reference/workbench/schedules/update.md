---
url: https://docs.cloud.google.com/sdk/gcloud/reference/workbench/schedules/update/
title: gcloud workbench schedules update \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:23:37.036748+00:00
---

# gcloud workbench schedules update  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/workbench/schedules/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud workbench schedules update Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud workbench schedules update - update a schedule 
SYNOPSIS
    

`gcloud workbench schedules update` (`SCHEDULE` : `--region`=`REGION`) (`--cron-schedule`=`CRON_SCHEDULE` `--display-name`=`DISPLAY_NAME` `--enable-queueing` `--end-time`=`END_TIME` `--max-concurrent-runs`=`MAX_CONCURRENT_RUNS` `--max-runs`=`MAX_RUNS` `--start-time`=`START_TIME`) [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Update a Workbench notebook execution schedule. 
EXAMPLES
     To update the cron schedule and max runs of a schedule with id `my-schedule`, in region `us-central1`, run: 
    
    
    gcloud workbench schedules update my-schedule --region=us-central1 --cron-schedule='TZ=America/Los_Angeles 0 0 * * 0' --max-runs=2

POSITIONAL ARGUMENTS
    

Schedule resource - Unique, system-generated resource name of the schedule to update. The arguments in this group can be used to specify the attributes of this resource. (NOTE) Some attributes are not given arguments in this group but can be set in other ways. 

To set the `project` attribute: 

  * provide the argument `schedule` on the command line with a fully specified name; 
  * provide the argument `--project` on the command line; 
  * set the property `core/project`. 



This must be specified. 

`SCHEDULE`
     ID of the schedule or fully qualified identifier for the schedule. 

To set the `name` attribute: 

  * provide the argument `schedule` on the command line. 



This positional argument must be specified if any of the other arguments in this group are specified. 

`--region`=`REGION`
     Cloud region for the schedule. 

To set the `region` attribute: 

  * provide the argument `schedule` on the command line with a fully specified name; 
  * provide the argument `--region` on the command line; 
  * set the property `colab/region`. 


REQUIRED FLAGS
    

Configuration of the schedule. 

At least one of these must be specified: 

`--cron-schedule`=`CRON_SCHEDULE`
     Cron schedule (https://en.wikipedia.org/wiki/Cron) to launch scheduled runs. To explicitly set a timezone to the cron tab, apply a prefix in the cron tab: "CRON_TZ=${IANA_TIME_ZONE}" or "TZ=${IANA_TIME_ZONE}". The ${IANA_TIME_ZONE} may only be a valid string from IANA time zone database. For example, "CRON_TZ=America/New_York 1 * * * `", or "TZ=America/New_York 1 * * * `". 
`--display-name`=`DISPLAY_NAME`
     The display name of the schedule. 
`--enable-queueing`
     Enables new scheduled runs to be queued when max_concurrent_runs limit is reached. If set to true, new runs will be queued instead of skipped. 
`--end-time`=`END_TIME`
     Timestamp after which no new runs can be scheduled. If specified, the schedule will be completed when either end_time is reached or when scheduled_run_count >= max_run_count. If neither end time nor max_run_count is specified, new runs will keep getting scheduled until this Schedule is paused or deleted. Must be in the RFC 3339 (https://www.rfc-editor.org/rfc/rfc3339.txt) format. E.g. "2026-01-01T00:00:00Z" or "2026-01-01T00:00:00-05:00" 
`--max-concurrent-runs`=`MAX_CONCURRENT_RUNS`
     Maximum number of runs that can be started concurrently for this Schedule. This is the limit for starting the scheduled requests and not the execution of the notebook execution jobs created by the requests. 
`--max-runs`=`MAX_RUNS`
     The max runs for the schedule. 
`--start-time`=`START_TIME`
     The timestamp after which the first run can be scheduled. Defaults to the schedule creation time. Must be in the RFC 3339 (https://www.rfc-editor.org/rfc/rfc3339.txt) format. E.g. "2026-01-01T00:00:00Z" or "2026-01-01T00:00:00-05:00" 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This variant is also available: 
    
    
    [gcloud beta workbench schedules update](https://docs.cloud.google.com/sdk/gcloud/reference/beta/workbench/schedules/update)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
