---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options/
title: gcloud dataflow jobs update-options \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:27:11.555053+00:00
---

# gcloud dataflow jobs update-options  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/update-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataflow jobs update-options Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataflow jobs update-options - update pipeline options on-the-fly for running Dataflow jobs 
SYNOPSIS
    

`gcloud dataflow jobs update-options` `JOB_ID` [`--autoscaling-max-num-workers`=`AUTOSCALING_MAX_NUM_WORKERS`, `--autoscaling-max-workers`=`AUTOSCALING_MAX_NUM_WORKERS`] [`--autoscaling-min-num-workers`=`AUTOSCALING_MIN_NUM_WORKERS`, `--autoscaling-min-workers`=`AUTOSCALING_MIN_NUM_WORKERS`] [`--autoscaling-schedule`=`AUTOSCALING_SCHEDULE`] [`--autoscaling-schedule-duration-seconds`=`AUTOSCALING_SCHEDULE_DURATION_SECONDS`] [`--autoscaling-schedule-priority`=`AUTOSCALING_SCHEDULE_PRIORITY`] [`--autoscaling-schedule-timezone`=`AUTOSCALING_SCHEDULE_TIMEZONE`] [`--autoscaling-worker-utilization-hint`=`AUTOSCALING_WORKER_UTILIZATION_HINT`] [`--max-num-workers`=`MAX_NUM_WORKERS`] [`--min-num-workers`=`MIN_NUM_WORKERS`] [`--region`=`REGION_ID`] [`--set-schedule`=`SET_SCHEDULE` | `--unset-schedule`=`UNSET_SCHEDULE` | `--unset-schedules`] [`--unset-worker-utilization-hint` | `--worker-utilization-hint`=`WORKER_UTILIZATION_HINT`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     This command can modify properties of running Dataflow jobs. Currently, only updating autoscaling settings for Streaming Engine jobs is supported. 

Adjust the autoscaling settings for Streaming Engine Dataflow jobs by providing at-least one of --min-num-workers or --max-num-workers or \--worker-utilization-hint (or all 3), or --unset-worker-utilization-hint (which cannot be run at the same time as --worker-utilization-hint but works with the others). Allow a few minutes for the changes to take effect. 

Note that autoscaling settings can only be modified on-the-fly for Streaming Engine jobs. Attempts to modify batch job or Streaming Appliance jobs will fail. 

EXAMPLES
     Modify autoscaling settings to scale between 5-10 workers: 
    
    
    gcloud dataflow jobs update-options --min-num-workers=5 --max-num-workers=10

Require a job to use at least 2 workers: 
    
    
    gcloud dataflow jobs update-options --min-num-workers=2

Require a job to use at most 20 workers: 
    
    
    gcloud dataflow jobs update-options --max-num-workers=20

Adjust the hint of target worker utilization to 70% for horizontal autoscaling: 
    
    
    gcloud dataflow jobs update-options --worker-utilization-hint=0.7

"Unset" worker utilization hint so that horizontal scaling will rely on its default CPU utilization target: 
    
    
    gcloud dataflow jobs update-options --unset-worker-utilization-hint

POSITIONAL ARGUMENTS
    

`JOB_ID`
     Job ID to operate on. 
FLAGS
    

`--autoscaling-max-num-workers`=`AUTOSCALING_MAX_NUM_WORKERS`, `--autoscaling-max-workers`=`AUTOSCALING_MAX_NUM_WORKERS`
     Maximum worker count when schedule is active. 
`--autoscaling-min-num-workers`=`AUTOSCALING_MIN_NUM_WORKERS`, `--autoscaling-min-workers`=`AUTOSCALING_MIN_NUM_WORKERS`
     Minimum worker count when schedule is active. 
`--autoscaling-schedule`=`AUTOSCALING_SCHEDULE`
     Crontab expression specifying when the schedule starts. 
`--autoscaling-schedule-duration-seconds`=`AUTOSCALING_SCHEDULE_DURATION_SECONDS`
     Duration in seconds for which the schedule will be active. 
`--autoscaling-schedule-priority`=`AUTOSCALING_SCHEDULE_PRIORITY`
     Priority of the schedule. If two schedules overlap, the one with the higher priority will be used. 
`--autoscaling-schedule-timezone`=`AUTOSCALING_SCHEDULE_TIMEZONE`
     Time zone for the schedule from tz database (e.g., America/Los_Angeles). 
`--autoscaling-worker-utilization-hint`=`AUTOSCALING_WORKER_UTILIZATION_HINT`
     Target worker utilization hint when schedule is active. 
`--max-num-workers`=`MAX_NUM_WORKERS`
     Upper-bound for autoscaling, between 1-1000. Only supported for streaming-engine jobs. 
`--min-num-workers`=`MIN_NUM_WORKERS`
     Lower-bound for autoscaling, between 1-1000. Only supported for streaming-engine jobs. 
`--region`=`REGION_ID`
     Region ID of the job's regional endpoint. Defaults to 'us-central1'. 
At most one of these can be specified: 

`--set-schedule`=`SET_SCHEDULE`
     Unique identifier for the autoscaling schedule to create or update. 
`--unset-schedule`=`UNSET_SCHEDULE`
     Unique identifier of the autoscaling schedule to remove. 
`--unset-schedules`
     Remove all autoscaling schedules from the job. 
At most one of these can be specified: 

`--unset-worker-utilization-hint`
     Unset --worker-utilization-hint. This causes the job autoscaling to fall back to internal tunings if they exist, or otherwise use the default hint value. 
`--worker-utilization-hint`=`WORKER_UTILIZATION_HINT`
     Target CPU utilization for autoscaling, ranging from 0.1 to 0.9. Only supported for streaming-engine jobs with autoscaling enabled. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     These variants are also available: 
    
    
    [gcloud alpha dataflow jobs update-options](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/dataflow/jobs/update-options)
    
    
    [gcloud beta dataflow jobs update-options](https://docs.cloud.google.com/sdk/gcloud/reference/beta/dataflow/jobs/update-options)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
