---
url: https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.workerpools/create/
title: Method: namespaces.workerpools.create \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:20:27.592282+00:00
---

# Method: namespaces.workerpools.create  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.workerpools/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Reference ](https://docs.cloud.google.com/run/docs/apis)



Send feedback 

#  Method: namespaces.workerpools.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Creates a new WorkerPool. WorkerPool creation will trigger a new deployment. Use workerpools.get, and check workerPool.status to determine if the WorkerPool is ready.

### HTTP request

`POST https://run.googleapis.com/apis/run.googleapis.com/v1/{parent}/workerpools`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource's parent. In Cloud Run, it may be one of the following:

  * `{project_id_or_number}`
  * `namespaces/{project_id_or_number}`
  * `namespaces/{project_id_or_number}/workerpools`
  * `projects/{project_id_or_number}/locations/{region}`
  * `projects/{project_id_or_number}/regions/{region}` It takes the form `namespaces/{namespace}`.

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `run.workerpools.create`

  
  
### Query parameters

Parameters  
---  
`dryRun` |  `string` Indicates that the server should validate the request and populate default values without persisting the request. Supported values: `all`  
  
### Request body

The request body contains an instance of `[WorkerPool](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.workerpools#WorkerPool)`.

### Response body

If successful, the response body contains a newly created instance of `[WorkerPool](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.workerpools#WorkerPool)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
