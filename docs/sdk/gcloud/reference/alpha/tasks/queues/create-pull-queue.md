---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/queues/create-pull-queue/
title: gcloud alpha tasks queues create-pull-queue \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:07.017379+00:00
---

# gcloud alpha tasks queues create-pull-queue  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/queues/create-pull-queue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha tasks queues create-pull-queue Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha tasks queues create-pull-queue - create a pull queue 
SYNOPSIS
    

`gcloud alpha tasks queues create-pull-queue` `QUEUE` [`--location`=`LOCATION`] [`--max-attempts`=`MAX_ATTEMPTS`] [`--max-retry-duration`=`MAX_RETRY_DURATION`] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` The flags available to this command represent the fields of a pull queue that are mutable. 

If you have early access to Cloud Tasks, refer to the following guide for more information about the different queue target types: <https://cloud.google.com/cloud-tasks/docs/queue-types>. For access, sign up here: <https://goo.gl/Ya0AZd>

EXAMPLES
     To create a Cloud Tasks pull queue: 
    
    
    gcloud alpha tasks queues create-pull-queue my-queue --max-attempts=10 --max-retry-duration=10s

POSITIONAL ARGUMENTS
    

`QUEUE`
     The queue to create. 
FLAGS
    

`--location`=`LOCATION`
     The location where we want to manage the queue or task. If not specified, uses the location of the current project's App Engine app if there is an associated app. 
`--max-attempts`=`MAX_ATTEMPTS`
     The maximum number of attempts per task in the queue. 
`--max-retry-duration`=`MAX_RETRY_DURATION`
     The time limit for retrying a failed task, measured from when the task was first run. Once the `--max-retry-duration` time has passed and the task has been attempted --max-attempts times, no further attempts will be made and the task will be deleted. 

Must be a string that ends in 's', such as "5s". 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta tasks queues create-pull-queue](https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks/queues/create-pull-queue)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
