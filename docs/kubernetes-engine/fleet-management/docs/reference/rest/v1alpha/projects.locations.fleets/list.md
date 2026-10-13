---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.fleets/list/
title: Method: projects.locations.fleets.list \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:05.612369+00:00
---

# Method: projects.locations.fleets.list  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.fleets/list/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.fleets.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Returns all fleets within an organization or a project that the caller has access to.

### HTTP request

`GET https://gkehub.googleapis.com/v1alpha/{parent=projects/*/locations/*}/fleets`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The organization or project to list for Fleets under, in the format `organizations/*/locations/*` or `projects/*/locations/*`.  
  
### Query parameters

Parameters  
---  
`pageToken` |  `string` Optional. A page token, received from a previous `fleets.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `fleets.list` must match the call that provided the page token.  
`pageSize` |  `integer` Optional. The maximum number of fleets to return. The service may return fewer than this value. If unspecified, at most 200 fleets will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListFleetsResponse](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/ListFleetsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-12 UTC."],[],[]] 
