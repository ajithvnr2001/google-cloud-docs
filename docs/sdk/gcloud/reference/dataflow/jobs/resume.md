---
url: https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/resume/
title: gcloud dataflow jobs resume \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:27:10.362799+00:00
---

# gcloud dataflow jobs resume  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/dataflow/jobs/resume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud dataflow jobs resume Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud dataflow jobs resume - starts resuming all given jobs 
SYNOPSIS
    

`gcloud dataflow jobs resume` `JOB_ID` [`JOB_ID` …] [`--region`=`REGION_ID`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     Once resume is triggered, if eligible, the job will enter the `JOB_STATE_RUNNING` state if the operation is successful. If the operation is not successful or the job is already running, the job state will be unchanged. If a job is already in the `JOB_STATE_RUNNING` state, the command will succeed and do nothing. 
EXAMPLES
     To resume a single job, run: 
    
    
    gcloud dataflow jobs resume 2000-01-02_03_04_05-12345678901234567890 --region=us-central1

To resume multiple jobs, run: 
    
    
    gcloud dataflow jobs resume 2000-01-02_03_04_05-12345678901234567890 2000-12-11_10_09_08-09876543210987654321 --region=us-central1

POSITIONAL ARGUMENTS
    

`JOB_ID` [`JOB_ID` …]
     Job IDs to operate on. 
FLAGS
    

`--region`=`REGION_ID`
     Region ID of the jobs' regional endpoint. Defaults to 'us-central1'. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
