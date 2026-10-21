---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/jobs/executions/
title: gcloud alpha run jobs executions \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:18:47.445815+00:00
---

# gcloud alpha run jobs executions  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/jobs/executions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha run jobs executions Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha run jobs executions - view and manage your Cloud Run jobs executions 
SYNOPSIS
    

`gcloud alpha run jobs executions` `GROUP` | `COMMAND` [`--region`=`REGION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` This set of commands can be used to view and manage your Cloud Run jobs executions. 
EXAMPLES
     To list your executions for a job, run: 
    
    
    [gcloud alpha run jobs executions list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/jobs/executions/list) --job=my-job

FLAGS
    

`--region`=`REGION`
     Region in which the resource can be found. Alternatively, set the property [run/region]. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

GROUPS
     ``GROUP`` is one of the following: 

`[logs](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/jobs/executions/logs)`
     `(ALPHA)` Read logs for Cloud Run jobs executions. 
`[tasks](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/jobs/executions/tasks)`
     `(ALPHA)` View and manage your Cloud Run jobs tasks. 
COMMANDS
     ``COMMAND`` is one of the following: 

`[cancel](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/jobs/executions/cancel)`
     `(ALPHA)` Cancel an execution. 
`[delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/jobs/executions/delete)`
     `(ALPHA)` Delete an execution. 
`[describe](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/jobs/executions/describe)`
     `(ALPHA)` Obtain details about executions. 
`[describe-latest](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/jobs/executions/describe-latest)`
     `(ALPHA)` Obtain details about the latest execution of a job. 
`[list](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/run/jobs/executions/list)`
     `(ALPHA)` List executions. 
NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. These variants are also available: 
    
    
    [gcloud run jobs executions](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/executions)
    
    
    [gcloud beta run jobs executions](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/jobs/executions)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
