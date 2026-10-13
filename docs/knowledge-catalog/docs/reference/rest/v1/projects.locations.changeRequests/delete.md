---
url: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.changeRequests/delete/
title: Method: projects.locations.changeRequests.delete \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:38:38.132150+00:00
---

# Method: projects.locations.changeRequests.delete  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/reference/rest/v1/projects.locations.changeRequests/delete/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  Method: projects.locations.changeRequests.delete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Deletes a ChangeRequest.

Behavior depends on the caller's permissions and the resource's state: 1. Callers with `dataplex.changeRequests.delete` can only delete ChangeRequests in the `NEW` state. 2. Callers with the `dataplex.changeRequests.adminDelete` permission can delete ChangeRequests regardless of their state.

### HTTP request

`DELETE https://dataplex.googleapis.com/v1/{name=projects/*/locations/*/changeRequests/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the ChangeRequest to delete. Format: projects/{projectNumber}/locations/{locationId}/changeRequests/{change_request_id}  
  
### Query parameters

Parameters  
---  
`etag` |  `string` Optional. The etag of the ChangeRequest.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dataplex.read-write`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource:

  * `dataplex.changeRequests.adminDelete`
  * `dataplex.changeRequests.delete`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-21 UTC."],[],[]] 
