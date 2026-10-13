---
url: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations/list/
title: Method: projects.locations.list \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:29.024307+00:00
---

# Method: projects.locations.list  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration)
  * [ Reference ](https://docs.cloud.google.com/network-security-integration/docs/apis)



Send feedback 

#  Method: projects.locations.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists information about the supported locations for this service.

### HTTP request

`GET https://networksecurity.googleapis.com/v1/{name=projects/*}/locations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The resource that owns the locations collection, if applicable.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` A filter to narrow down results to a preferred subset. The filtering language accepts strings like `"displayName=tokyo"`, and is documented in more detail in [AIP-160](https://google.aip.dev/160).  
`pageSize` |  `integer` The maximum number of results to return. If not set, the service selects a default.  
`pageToken` |  `string` A page token received from the `nextPageToken` field in the response. Send that page token to receive the subsequent page.  
`extraLocationTypes[]` |  `string` Optional. Do not use this field. It is unsupported and is ignored unless explicitly documented otherwise. This is primarily for internal usage.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListLocationsResponse](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/Shared.Types/ListLocationsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-23 UTC."],[],[]] 
