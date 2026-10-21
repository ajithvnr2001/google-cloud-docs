---
url: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/queues/create-app-engine-queue/
title: gcloud alpha tasks queues create-app-engine-queue \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:25.534050+00:00
---

# gcloud alpha tasks queues create-app-engine-queue  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/queues/create-app-engine-queue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Reference ](https://docs.cloud.google.com/sdk/docs/libraries-reference)



Send feedback 

#  gcloud alpha tasks queues create-app-engine-queue Stay organized with collections  Save and categorize content based on your preferences. 

NAME
    

gcloud alpha tasks queues create-app-engine-queue - create a Cloud Tasks queue 
SYNOPSIS
    

`gcloud alpha tasks queues create-app-engine-queue` `QUEUE` [`--location`=`LOCATION`] [`--max-attempts`=`MAX_ATTEMPTS`] [`--max-backoff`=`MAX_BACKOFF`] [`--max-concurrent-tasks`=`MAX_CONCURRENT_TASKS`] [`--max-doublings`=`MAX_DOUBLINGS`] [`--max-retry-duration`=`MAX_RETRY_DURATION`] [`--max-tasks-dispatched-per-second`=`MAX_TASKS_DISPATCHED_PER_SECOND`] [`--min-backoff`=`MIN_BACKOFF`] [`--routing-override`=`KEY`:`VALUE`,[…]] [`GCLOUD_WIDE_FLAG …`]
DESCRIPTION
     `(ALPHA)` `(DEPRECATED)` This command group is deprecated. Use `[gcloud alpha tasks queues create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/queues/create)` instead 

`(ALPHA)` `(DEPRECATED)` Create a Cloud Tasks queue. 

This command group is deprecated. Use `[gcloud alpha tasks queues create](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/tasks/queues/create)` instead 

The flags available to this command represent the fields of a queue that are mutable. 

EXAMPLES
     To create a Cloud Tasks queue: 
    
    
    gcloud alpha tasks queues create-app-engine-queue my-queue --max-attempts=10 --max-retry-duration=5s --max-doublings=4 --min-backoff=1s --max-backoff=10s --max-tasks-dispatched-per-second=100 --max-concurrent-tasks=10 --routing-override=service:abc

POSITIONAL ARGUMENTS
    

`QUEUE`
     The queue to create. 
FLAGS
    

`--location`=`LOCATION`
     The location where we want to manage the queue or task. If not specified, uses the location of the current project's App Engine app if there is an associated app. 
`--max-attempts`=`MAX_ATTEMPTS`
     The maximum number of attempts per task in the queue. 
`--max-backoff`=`MAX_BACKOFF`
     The maximum amount of time to wait before retrying a task after it fails. Must be a string that ends in 's', such as "5s". 
`--max-concurrent-tasks`=`MAX_CONCURRENT_TASKS`
     The maximum number of concurrent tasks that Cloud Tasks allows to be dispatched for this queue. After this threshold has been reached, Cloud Tasks stops dispatching tasks until the number of outstanding requests decreases. 
`--max-doublings`=`MAX_DOUBLINGS`
     The time between retries will double maxDoublings times. 

A tasks retry interval starts at minBackoff, then doubles maxDoublings times, then increases linearly, and finally retries retries at intervals of maxBackoff up to maxAttempts times. 

For example, if minBackoff is 10s, maxBackoff is 300s, and maxDoublings is 3, then the a task will first be retried in 10s. The retry interval will double three times, and then increase linearly by 2^3 * 10s. Finally, the task will retry at intervals of maxBackoff until the task has been attempted maxAttempts times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s. 

`--max-retry-duration`=`MAX_RETRY_DURATION`
     The time limit for retrying a failed task, measured from when the task was first run. Once the `--max-retry-duration` time has passed and the task has been attempted --max-attempts times, no further attempts will be made and the task will be deleted. 

Must be a string that ends in 's', such as "5s". 

`--max-tasks-dispatched-per-second`=`MAX_TASKS_DISPATCHED_PER_SECOND`
     The maximum rate at which tasks are dispatched from this queue. 
`--min-backoff`=`MIN_BACKOFF`
     The minimum amount of time to wait before retrying a task after it fails. Must be a string that ends in 's', such as "5s". 
`--routing-override`=`KEY`:`VALUE`,[…]
     If provided, the specified App Engine route is used for all tasks in the queue, no matter what is set is at the task-level. 

KEY must be at least one of: [service, version, instance]. Any missing keys will use the default. 

GCLOUD WIDE FLAGS
     These flags are available to all commands: `[--access-token-file](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file)`, `[--account](https://docs.cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)`, `[--configuration](https://docs.cloud.google.com/sdk/gcloud/reference#--configuration)`, `[--flags-file](https://docs.cloud.google.com/sdk/gcloud/reference#--flags-file)`, `[--flatten](https://docs.cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://docs.cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://docs.cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`, `[--log-http](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http)`, `[--project](https://docs.cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://docs.cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://docs.cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://docs.cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`, `[--verbosity](https://docs.cloud.google.com/sdk/gcloud/reference#--verbosity)`. 

Run `$ [gcloud help](https://docs.cloud.google.com/sdk/gcloud/reference)` for details. 

NOTES
     This command is currently in alpha and might change without notice. If this command fails with API permission errors despite specifying the correct project, you might be trying to access an API with an invitation-only early access allowlist. This variant is also available: 
    
    
    [gcloud beta tasks queues create-app-engine-queue](https://docs.cloud.google.com/sdk/gcloud/reference/beta/tasks/queues/create-app-engine-queue)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-27 UTC."],[],[]] 
