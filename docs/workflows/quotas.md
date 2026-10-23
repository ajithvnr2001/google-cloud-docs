---
url: https://docs.cloud.google.com/workflows/quotas/
title: Quotas and limits \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:31.863530+00:00
---

# Quotas and limits  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Resources ](https://docs.cloud.google.com/workflows/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Workflows.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Workflows resources. System limits can't be changed. 

## Quotas

Workflows enforces the following quotas for each Google Cloud project. You can increase or decrease these quotas:

Quota | Description | Value  
---|---|---  
Total workflows | The maximum number of workflows you can deploy per project | 10,000  
Concurrent executions | The maximum number of active workflow executions per region, per project. Concurrent executions are executions that have started and not yet completed or failed, including any that are waiting on callbacks or are sleeping. Once the quota is reached, and with execution backlogging enabled by default (with some exceptions), executions are created in a `QUEUED` state. If execution backlogging is disabled, or if the quota for backlogged executions is reached, any new executions fail with an HTTP `429 Too many requests` status code. For more information, see [ Manage execution backlogging](https://docs.cloud.google.com/workflows/docs/executing-workflow#manage_execution_backlogging). | 10,000  
Backlogged executions | The maximum number of backlogged workflow executions per region, per project. For more information, see [ Manage execution backlogging](https://docs.cloud.google.com/workflows/docs/executing-workflow#manage_execution_backlogging). | 100,000  
Workflow API requests | The maximum number of API requests (`create`, `update`, `list`, `get`, `delete`) from all workflows in your project (per minute per location) | 1,200  
Execution API get requests | The maximum number of requests to [`get`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions/get) workflow executions from all workflows in your project (per minute per location) | 6,000  
Execution API list requests | The maximum number of requests to [`list`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions/list) workflow executions from all workflows in your project (per minute per location) | 1,200  
Execution API write requests | The maximum number of requests to [`create`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions/create) and [`cancel`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions/cancel) workflow executions (including Eventarc-triggered executions) from all workflows in your project (per minute per location). If Eventarc-triggered executions exceed this maximum, the events are retried following the [Eventarc retry policy](https://docs.cloud.google.com/eventarc/docs/retry-events). | 6,000  
Execution API get step entries requests | The maximum number of requests to [`get`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.stepEntries/get) a step entry from a workflow execution (per minute per location) | 6,000  
Execution API list step entries requests | The maximum number of requests to [`list`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.stepEntries/list) step entries from a workflow execution (per minute per location) | 1,200  
Execution API export data requests | The maximum number of requests to [`export data`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions/exportData) from a workflow execution (per minute per location) | 10  
HTTP requests to [callback endpoints](https://docs.cloud.google.com/workflows/docs/creating-callback-endpoints) | The maximum number of `SendHttpCallback` API requests made on execution resources from all workflows in your project (per minute per location) | 1,500  
Execution API list callback requests | The maximum number of requests to [`list`](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions.callbacks/list) callbacks from a workflow execution (per minute per location) | 300  
  
## Quota increase requests

To increase or decrease quotas, use the Google Cloud console. For more information, see [Requesting a higher quota](https://docs.cloud.google.com/docs/quota_detail/view_manage#requesting_higher_quota).

## Monitor quota usage

You can query and monitor quota usage metrics. For an example, see [Monitor quota metrics](https://docs.cloud.google.com/workflows/docs/monitor#quota-metrics) which demonstrates how to query the total consumed allocation quota for Workflows. For information about how to monitor quota usage metrics, see [Chart and monitor quota metrics](https://docs.cloud.google.com/monitoring/alerts/using-quota-metrics).

## Step limits

Workflows enforces the following step limits for each workflow. You can't request changes to these limits:

Limit | Description | Value  
---|---|---  
Assignments per step | The maximum number of [assignments](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#assign-step) that may be performed in a single step | 50  
Conditions per switch | The maximum number of conditions that may be evaluated in a single [switch block](https://docs.cloud.google.com/workflows/docs/reference/syntax/conditions) | 50  
Maximum call stack depth | The maximum number of levels of calling functions; for example, when a subworkflow calls itself or another subworkflow; or, standard library function calls that in turn call other functions | 20  
Minimum steps | The minimum number of steps within a workflow | 1  
Maximum steps | The maximum number of steps that may be performed in a single workflow executionFor more information about what is considered a step, see [Optimize usage](https://docs.cloud.google.com/workflows/docs/best-practice#optimize-usage). | 100,000  
  
## Parallel step limits

Workflows enforces the following limits when using parallel steps. You can't request changes to these limits:

Limit | Description | Value  
---|---|---  
Branches per step | The maximum number of branches supported within a [parallel step](https://docs.cloud.google.com/workflows/docs/reference/syntax/parallel-steps) | 10  
Parallel depth | The maximum depth that parallel steps can be nested | 2  
Concurrent branches and iterations | The maximum number of branches and iterations that can concurrently execute within a single workflow execution before further branches and iterations are automatically queued to wait for one or more running threads to complete. There is no total thread count limit; however, all other limits apply.  | 20  
Uncaught exceptions within a parallel step | The maximum number of unhandled exceptions that can be raised during the execution of the workflow (in total) | 100  
  
## Resource limits

Workflows enforces the following usage limits. You can't request changes to these limits:

Limit | Description | Value  
---|---|---  
Source code size | The maximum size of the YAML or JSON file that defines your workflow | 128 KB  
Response size | The maximum size of an HTTP response (if saved to a variable, the memory limit for variables applies) | 2 MB  
Expression length | The maximum number of characters in a single [expression](https://docs.cloud.google.com/workflows/docs/reference/syntax/expressions) | 400 characters  
Data size | The maximum cumulative size for variables, arguments, and events: | 512 KB  
  
  * Maximum amount of memory that you can use for all [variables](https://docs.cloud.google.com/workflows/docs/reference/syntax/variables#variable-sizes) that you define in a single execution of a given workflow

  
  
  * Maximum size of the [arguments](https://docs.cloud.google.com/workflows/docs/reference/syntax/runtime-args) you can pass when creating a workflow execution

  
  
  * Maximum size of the Eventarc payload you can pass when triggering a workflow execution with [events](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc)

  
Maximum [string](https://docs.cloud.google.com/workflows/docs/reference/syntax/strings) length in bytes using UTF-8 encoding | 256 KB  
Environment variables | The maximum size for a [ user-defined environment variable](https://docs.cloud.google.com/workflows/docs/use-environment-variables) definition string (`KEY=value`); a maximum of 20 variables can be defined | 4 KiB  
Execution duration | The maximum duration (from start time to end time) for a workflow execution; any workflow that passes this limit ends with a time-out error | 1 year  
Execution retention | The maximum retention period (after a workflow execution completes) of an execution's history and results | 90 days  
Deduplication window | The deduplication window to ensure exactly-once processing when triggering a workflow execution with [events](https://docs.cloud.google.com/workflows/docs/trigger-workflow-eventarc) | 24 hours  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
