---
url: https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.workerPools/delete/
title: Method: projects.locations.workerPools.delete \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:36.494379+00:00
---

# Method: projects.locations.workerPools.delete  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.workerPools/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Reference ](https://docs.cloud.google.com/run/docs/apis)



Send feedback 

#  Method: projects.locations.workerPools.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Deletes a WorkerPool.

### HTTP request

`DELETE https://run.googleapis.com/v2/{name}`

### Path parameters

Parameters  
---  
`name` |  `string` Required. The full name of the WorkerPool. Format: `projects/{project}/locations/{location}/workerPools/{workerPool}`, where `{project}` can be project id or number. It takes the form `projects/{project}/locations/{location}/workerPools/{workerpool}`.  
  
### Query parameters

Parameters  
---  
`validateOnly` |  `boolean` Optional. Indicates that the request should be validated without actually deleting any resources.  
`etag` |  `string` A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/run/docs/reference/rest/v2/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-13 UTC."],[],[]] 
