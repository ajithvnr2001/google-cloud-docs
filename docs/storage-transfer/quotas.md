---
url: https://docs.cloud.google.com/storage-transfer/quotas/
title: Quotas & Limits \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:49.179131+00:00
---

# Quotas & Limits  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage-transfer/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/storage-transfer/docs/resources)



Send feedback 

#  Quotas & Limits Stay organized with collections  Save and categorize content based on your preferences. 

This document contains current API restrictions and usage quotas on use of Storage Transfer Service. This page is updated when there are changes to these restrictions and usage quotas.

**Note:** Storage Transfer Service supports URL lists with a maximum size of 128 MB. See [Creating a URL List](https://docs.cloud.google.com/storage-transfer/docs/create-url-list).

## Concurrent transferOperations limit

The following table describes the limit for concurrent in-progress [`transferOperations`](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations):

Maximum in-progress `transferOperations` | Applies to  
---|---  
200 | project  
**Note:** When the number of in-progress `transferOperations` in a project reaches the limit, new and resumed `transferOperations` beyond the limit are placed in `QUEUED` [status](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations#status). As in-progress `transferOperations` complete, any `QUEUED` `transferOperations` are moved to `IN_PROGRESS` status.

## Rate quotas

Storage Transfer Service enforces rate quotas on all requests made. These quotas apply on a per-project basis; requests made through Google Cloud CLI, Google Cloud console, and Cloud Client Libraries also count towards these rate quotas.

This table provides the metric, API methods, and default limits for each quota:

Metric | API methods | Default limits  
---|---|---  
`storagetransfer.googleapis.com/create_requests` | 

  * `projects.agentPools.create`
  * `transferJobs.create`

| 

  * 600 requests/min/project
  * 5000 requests/day/project

  
`storagetransfer.googleapis.com/read_requests` | 

  * `googleServiceAccounts.get`
  * `projects.agentPools.get`
  * `projects.agentPools.list`
  * `transferJobs.get`
  * `transferJobs.list`
  * `transferOperations.get`
  * `transferOperations.list`

| 

  * 1500 requests/min/project

  
`storagetransfer.googleapis.com/update_requests` | 

  * `projects.agentPools.patch`
  * `transferJobs.patch`

| 

  * 600 requests/min/project

  
`storagetransfer.googleapis.com/delete_requests` | 

  * `projects.agentPools.delete`
  * `transferJobs.delete`

| 

  * 600 requests/min/project

  
`storagetransfer.googleapis.com/operation_requests` | 

  * `transferOperations.cancel`
  * `transferOperations.pause`
  * `transferOperations.resume`

| 

  * 900 requests/min/project

  
  
## Adjusting quotas

For information on adjusting quotas, see [Manage quota values](https://docs.cloud.google.com/docs/quotas/overview#manage_quota_values).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
