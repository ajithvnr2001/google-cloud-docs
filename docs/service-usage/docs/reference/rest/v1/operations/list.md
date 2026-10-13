---
url: https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/operations/list/
title: Method: operations.list \u00a0|\u00a0 Service Usage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:47.355221+00:00
---

# Method: operations.list  |  Service Usage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/operations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Usage ](https://docs.cloud.google.com/service-usage)
  * [ Reference ](https://docs.cloud.google.com/service-usage/docs/apis)



Send feedback 

#  Method: operations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

### HTTP request

`GET https://serviceusage.googleapis.com/v1/operations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`name` |  `string` The name of the operation's parent resource.  
`filter` |  `string` The standard list filter.  
`pageSize` |  `integer` The standard list page size.  
`pageToken` |  `string` The standard list page token.  
`returnPartialSuccess` |  `boolean` When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the `[ListOperationsResponse.unreachable](https://docs.cloud.google.com/service-usage/docs/reference/rest/Shared.Types/ListOperationsResponse#FIELDS.unreachable)` field.This can only be `true` when reading across collections. For example, when `parent` is set to `"projects/example/locations/-"`.This field is not supported by default and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListOperationsResponse](https://docs.cloud.google.com/service-usage/docs/reference/rest/Shared.Types/ListOperationsResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-10 UTC."],[],[]] 
