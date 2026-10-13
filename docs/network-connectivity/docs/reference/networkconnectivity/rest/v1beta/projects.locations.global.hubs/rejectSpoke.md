---
url: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs/rejectSpoke/
title: Method: projects.locations.global.hubs.rejectSpoke \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:30:58.471385+00:00
---

# Method: projects.locations.global.hubs.rejectSpoke  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.hubs/rejectSpoke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Reference ](https://docs.cloud.google.com/network-connectivity/docs/apis)



Send feedback 

#  Method: projects.locations.global.hubs.rejectSpoke Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

### HTTP request

`POST https://networkconnectivity.googleapis.com/v1beta/{name=projects/*/locations/global/hubs/*}:rejectSpoke`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the hub from which to reject the spoke.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "spokeUri": string,
      "requestId": string,
      "details": string
    }  
  
Fields  
---  
`spokeUri` |  `string` Required. The URI of the spoke to reject from the hub.  
`requestId` |  `string` Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
`details` |  `string` Optional. Additional information provided by the hub administrator.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
