---
url: https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks/delete/
title: gcloud beta tasks delete \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:41:31.844252+00:00
---

# gcloud beta tasks delete  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud beta tasks delete Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud beta tasks delete - delete a task or multiple tasks from a queue 
SYNOPSIS
    

`gcloud beta tasks delete` [`TASK` …] [`--failed-tasks-file`=`FAILED_TASKS_FILE`] [`--from-file`=`FROM_FILE`] [`--location`=`LOCATION`] [`--queue`=`QUEUE`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(BETA)` Delete a task or multiple tasks from a queue. 
EXAMPLES
     To delete a task: 
    
    
    gcloud beta tasks delete --queue=my-queue my-task

To delete multiple tasks: 
    
    
    gcloud beta tasks delete --queue=my-queue task1 task2 task3

POSITIONAL ARGUMENTS
    

[`TASK` …]
     The task to delete. 
FLAGS
    

`--failed-tasks-file`=`FAILED_TASKS_FILE`
     Path to a file to output JSON details of tasks that failed or were skipped during batch deletion. 
`--from-file`=`FROM_FILE`
     Path to a file containing task IDs/names to delete, one per line or in JSON/YAML format. 
`--location`=`LOCATION`
     The location where we want to manage the queue or task. If not specified, uses the location of the current project's App Engine app if there is an associated app. 
`--queue`=`QUEUE`
     The queue the task belongs to. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in beta and might change without notice. These variants are also available: 
    
    
    [gcloud tasks delete](https://docs.cloud.google.com/sdk/gcloud/reference/tasks/delete)
    
    
    [gcloud alpha tasks delete](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/delete)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
