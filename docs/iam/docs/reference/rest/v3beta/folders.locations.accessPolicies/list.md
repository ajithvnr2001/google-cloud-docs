---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/list/
title: Method: folders.locations.accessPolicies.list \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:29.437620+00:00
---

# Method: folders.locations.accessPolicies.list  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.accessPolicies/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: folders.locations.accessPolicies.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Lists access policies.

### HTTP request

`GET https://iam.googleapis.com/v3beta/{parent=folders/*/locations/*}/accessPolicies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource, which owns the collection of access policy resources.Format: `projects/{projectId}/locations/{location}` `projects/{projectNumber}/locations/{location}` `folders/{folderId}/locations/{location}` `organizations/{organizationId}/locations/{location}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of access policies to return. The service may return fewer than this value.If unspecified, at most 50 access policies will be returned. Valid value ranges from 1 to 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `accessPolicies.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `accessPolicies.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListAccessPoliciesResponse](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/ListAccessPoliciesResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-12 UTC."],[],[]] 
