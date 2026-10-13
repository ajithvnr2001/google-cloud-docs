---
url: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/delete/
title: Method: projects.locations.jobs.delete \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:22.592677+00:00
---

# Method: projects.locations.jobs.delete  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storagebatchoperations/reference/rest/v1/projects.locations.jobs/delete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Method: projects.locations.jobs.delete Stay organized with collections  Save and categorize content based on your preferences. 

Deletes a batch job.

### HTTP request

`DELETE https://storagebatchoperations.googleapis.com/v1/{name=projects/*/locations/*/jobs/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The `name` of the job to delete. Format: `projects/{projectId}/locations/global/jobs/{jobId}`.  
  
### Query parameters

Parameters  
---  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID in case you need to retry your request. Requests with same `requestId` are ignored for at least 60 minutes since the first request. The request ID must be a valid UUID with the exception that zero UUID isn't supported (00000000-0000-0000-0000-000000000000).  
`force` |  `boolean` Optional. If set to true, any child bucket operations of the job are deleted. We recommend setting this to `true`. You can't mutate bucket operations directly, so only the `jobs.delete` permission is required to delete a job (and its child bucket operations).  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `storagebatchoperations.jobs.delete`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
