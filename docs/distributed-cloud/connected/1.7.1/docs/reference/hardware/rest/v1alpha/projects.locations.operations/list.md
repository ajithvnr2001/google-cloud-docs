---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/hardware/rest/v1alpha/projects.locations.operations/list/
title: Method: projects.locations.operations.list \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:10.950627+00:00
---

# Method: projects.locations.operations.list  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/hardware/rest/v1alpha/projects.locations.operations/list/




#  Method: projects.locations.operations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

### HTTP request

`GET https://gdchardwaremanagement.googleapis.com/v1alpha/{name=projects/*/locations/*}/operations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` The name of the operation's parent resource.  
  
### Query parameters

Parameters  
---  
`filter` |  `string` The standard list filter.  
`pageSize` |  `integer` The standard list page size.  
`pageToken` |  `string` The standard list page token.  
  
### Request body

The request body must be empty.

### Response body

The response message for `[Operations.ListOperations](https://docs.cloud.google.com/distributed-cloud/edge/1.7.1/docs/reference/hardware/rest/v1alpha/projects.locations.operations/list#google.longrunning.Operations.ListOperations)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/distributed-cloud/edge/1.7.1/docs/reference/hardware/rest/v1alpha/projects.locations.operations#Operation))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/distributed-cloud/edge/1.7.1/docs/reference/hardware/rest/v1alpha/projects.locations.operations#Operation)`)` A list of operations that matches the specified filter in the request.  
`nextPageToken` |  `string` The standard List next-page token.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `gdchardwaremanagement.operations.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
