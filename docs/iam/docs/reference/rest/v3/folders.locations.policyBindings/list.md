---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings/list/
title: Method: folders.locations.policyBindings.list \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:22.632769+00:00
---

# Method: folders.locations.policyBindings.list  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: folders.locations.policyBindings.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Lists policy bindings.

### HTTP request

`GET https://iam.googleapis.com/v3/{parent=folders/*/locations/*}/policyBindings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource, which owns the collection of policy bindings.Format:

  * `projects/{projectId}/locations/{location}`
  * `projects/{projectNumber}/locations/{location}`
  * `folders/{folderId}/locations/{location}`
  * `organizations/{organizationId}/locations/{location}`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of policy bindings to return. The service may return fewer than this value.The default value is 50. The maximum value is 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `policyBindings.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `policyBindings.list` must match the call that provided the page token.  
`filter` |  `string` Optional. An expression for filtering the results of the request. Filter rules are case insensitive. Some eligible fields for filtering are the following:

  * `target`
  * `policy`

Some examples of filter queries:

  * `target:ex*`: The binding target's name starts with "ex".
  * `target:example`: The binding target's name is `example`.
  * `policy:example`: The binding policy's name is `example`.

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListPolicyBindingsResponse](https://docs.cloud.google.com/iam/docs/reference/rest/v3/ListPolicyBindingsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `iam.policybindings.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-12 UTC."],[],[]] 
