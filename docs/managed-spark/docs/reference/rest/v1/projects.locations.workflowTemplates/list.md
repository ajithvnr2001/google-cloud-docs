---
url: https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/list/
title: Method: projects.locations.workflowTemplates.list \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:22.863958+00:00
---

# Method: projects.locations.workflowTemplates.list  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.locations.workflowTemplates/list/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Reference ](https://docs.cloud.google.com/managed-spark/docs/reference)



Send feedback 

#  Method: projects.locations.workflowTemplates.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Lists workflows that match the specified filter in the request.

### HTTP request

`GET https://dataproc.googleapis.com/v1/{parent=projects/*/locations/*}/workflowTemplates`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the region or location, as described in <https://cloud.google.com/apis/design/resource_names>.

  * For `projects.regions.workflowTemplates,list`, the resource name of the region has the following format: `projects/{projectId}/regions/{region}`
  * For `projects.locations.workflowTemplates.list`, the resource name of the location has the following format: `projects/{projectId}/locations/{location}`

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `dataproc.workflowTemplates.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of results to return in each response.  
`pageToken` |  `string` Optional. The page token, returned by a previous call, to request the next page of results.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListWorkflowTemplatesResponse](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ListWorkflowTemplatesResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dataproc`
  * ` https://www.googleapis.com/auth/dataproc.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
