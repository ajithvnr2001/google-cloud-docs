---
url: https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/projects.locations.entitlements.grants/list/
title: Method: projects.locations.entitlements.grants.list \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:18:20.293676+00:00
---

# Method: projects.locations.entitlements.grants.list  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/projects.locations.entitlements.grants/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.locations.entitlements.grants.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Lists grants for a given entitlement.

### HTTP request

`GET https://privilegedaccessmanager.googleapis.com/v1/{parent=projects/*/locations/*/entitlements/*}/grants`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource which owns the grants.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. The server may return fewer items than requested. If unspecified, the server picks an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results.  
`orderBy` |  `string` Optional. Hint for how to order the results  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListGrantsResponse](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/ListGrantsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `privilegedaccessmanager.grants.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-26 UTC."],[],[]] 
