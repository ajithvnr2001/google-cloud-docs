---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/operations/list/
title: Method: operations.list \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:25.859225+00:00
---

# Method: operations.list  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/operations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: operations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes



Lists service operations that match the specified filter in the request.

### HTTP request

`GET https://servicemanagement.googleapis.com/v1/operations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`name` |  `string` Not used.  
`filter` |  `string` A string for filtering `[Operations](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/operations#Operation)`. The following filter fields are supported:

  * serviceName: Required. Only `=` operator is allowed.
  * startTime: The time this job was started, in ISO 8601 format. Allowed operators are `>=`, `>`, `<=`, and `<`.
  * status: Can be `done`, `in_progress`, or `failed`. Allowed operators are `=`, and `!=`.

Filter expression supports conjunction (AND) and disjunction (OR) logical operators. However, the serviceName restriction must be at the top-level and can only be combined with other restrictions via the AND logical operator.Examples:

  * `serviceName={some-service}.googleapis.com`
  * `serviceName={some-service}.googleapis.com AND startTime>="2017-02-01"`
  * `serviceName={some-service}.googleapis.com AND status=done`
  * `serviceName={some-service}.googleapis.com AND (status=done OR startTime>="2017-02-01")`

  
`pageSize` |  `integer` The maximum number of operations to return. If unspecified, defaults to 50. The maximum value is 100.  
`pageToken` |  `string` The standard list page token.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

The response message for `[Operations.ListOperations](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/operations/list#google.longrunning.Operations.ListOperations)`.

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/operations#Operation))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/operations#Operation)`)` A list of operations that matches the specified filter in the request.  
`nextPageToken` |  `string` The standard List next-page token.  
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
