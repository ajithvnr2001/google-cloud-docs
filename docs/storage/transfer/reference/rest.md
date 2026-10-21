---
url: https://docs.cloud.google.com/storage/transfer/reference/rest/
title: Storage Transfer API \u00a0|\u00a0 Storage Transfer Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:56:04.406213+00:00
---

# Storage Transfer API  |  Storage Transfer Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/transfer/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Storage Transfer Service ](https://docs.cloud.google.com/storage-transfer/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/storage-transfer/docs/apis)



Send feedback 

#  Storage Transfer API Stay organized with collections  Save and categorize content based on your preferences. 

Transfers data from external data sources to a Google Cloud Storage bucket or between Google Cloud Storage buckets.

## Service: storagetransfer.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery document:

  * <https://storagetransfer.googleapis.com/$discovery/rest?version=v1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://storagetransfer.googleapis.com`



## REST Resource: [v1.googleServiceAccounts](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts)

Methods  
---  
`[get](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/googleServiceAccounts/get)` |  `GET /v1/googleServiceAccounts/{projectId}`   
Returns the Google service account that is used by Storage Transfer Service to access buckets in the project where transfers run or in other projects.  
  
## REST Resource: [v1.projects.agentPools](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools)

Methods  
---  
`[create](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools/create)` |  `POST /v1/projects/{projectId}/agentPools`   
Creates an agent pool resource.  
`[delete](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools/delete)` |  `DELETE /v1/{name=projects/*/agentPools/*}`   
Deletes an agent pool.  
`[get](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools/get)` |  `GET /v1/{name=projects/*/agentPools/*}`   
Gets an agent pool.  
`[list](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools/list)` |  `GET /v1/projects/{projectId}/agentPools`   
Lists agent pools.  
`[patch](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/projects.agentPools/patch)` |  `PATCH /v1/{agentPool.name=projects/*/agentPools/*}`   
Updates an existing agent pool resource.  
  
## REST Resource: [v1.transferJobs](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs)

Methods  
---  
`[create](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/create)` |  `POST /v1/transferJobs`   
Creates a transfer job that runs periodically.  
`[delete](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/delete)` |  `DELETE /v1/{jobName=transferJobs/**}`   
Deletes a transfer job.  
`[get](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/get)` |  `GET /v1/{jobName=transferJobs/**}`   
Gets a transfer job.  
`[list](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/list)` |  `GET /v1/transferJobs`   
Lists transfer jobs.  
`[patch](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/patch)` |  `PATCH /v1/{jobName=transferJobs/**}`   
Updates a transfer job.  
`[run](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferJobs/run)` |  `POST /v1/{jobName=transferJobs/**}:run`   
Starts a new operation for the specified transfer job.  
  
## REST Resource: [v1.transferOperations](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations/cancel)` |  `POST /v1/{name=transferOperations/**}:cancel`   
Cancels a transfer.  
`[get](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations/get)` |  `GET /v1/{name=transferOperations/**}`   
Gets the latest state of a long-running operation.  
`[list](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations/list)` |  `GET /v1/{name=transferOperations}`   
Lists transfer operations.  
`[pause](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations/pause)` |  `POST /v1/{name=transferOperations/**}:pause`   
Pauses a transfer operation.  
`[resume](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/transferOperations/resume)` |  `POST /v1/{name=transferOperations/**}:resume`   
Resumes a transfer operation that is paused.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
