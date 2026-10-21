---
url: https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/create/
title: Method: projects.locations.reportConfigs.create \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:52:37.789869+00:00
---

# Method: projects.locations.reportConfigs.create  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Method: projects.locations.reportConfigs.create Stay organized with collections  Save and categorize content based on your preferences. 

Creates a new inventory report configuration in a given project for a given location.

### HTTP request

`POST https://storageinsights.googleapis.com/v1/{parent=projects/*/locations/*}/reportConfigs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Value for parent.  
  
### Query parameters

Parameters  
---  
`requestId` |  `string` Optional. A unique identifier for your request. Specify the request ID if you need to retry the request. If you retry the request with the same ID within 60 minutes, the server ignores the request if it has already completed the original request.For example, if your initial request times out and you retry the request using the same request ID, the server recognizes the original request and does not process the new request.The request ID must be a valid UUID and cannot be a zero UUID (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body contains an instance of `[ReportConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#ReportConfig)`.

### Response body

If successful, the response body contains a newly created instance of `[ReportConfig](https://docs.cloud.google.com/storage/docs/insights/reference/rest/v1/projects.locations.reportConfigs#ReportConfig)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `storageinsights.reportConfigs.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
