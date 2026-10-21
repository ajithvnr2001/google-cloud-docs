---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/batch-create/
title: gcloud alpha tasks batch-create \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:28.834470+00:00
---

# gcloud alpha tasks batch-create  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/batch-create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha tasks batch-create Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha tasks batch-create - create multiple tasks from a file in a single batch operation 
SYNOPSIS
    

`gcloud alpha tasks batch-create` `--queue`=`QUEUE` `--tasks-from-file`=`TASKS_FROM_FILE` [`--dry-run`] [`--failed-tasks-file`=`FAILED_TASKS_FILE`] [`--location`=`LOCATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` Create multiple tasks from a file in a single batch operation. 
EXAMPLES
     To create multiple tasks from a JSON or YAML file: 
    
    
    gcloud alpha tasks batch-create --queue=my-queue --tasks-from-file=tasks.yaml

REQUIRED FLAGS
    

`--queue`=`QUEUE`
     The queue the tasks belong to. 
`--tasks-from-file`=`TASKS_FROM_FILE`
     Path to a JSON or YAML file containing a list of tasks to create, or - to read from stdin. 
OPTIONAL FLAGS
    

`--dry-run`
     If set to true, validates the task specifications without creating the tasks. 
`--failed-tasks-file`=`FAILED_TASKS_FILE`
     Optional path to a file where a JSON record of failed tasks will be written. 
`--location`=`LOCATION`
     The location where we want to manage the queue or task. If not specified, uses the location of the current project's App Engine app if there is an associated app. 
GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta tasks batch-create](https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks/batch-create)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
