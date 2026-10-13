---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments/create/
title: Method: projects.locations.zones.interconnectAttachments.create \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:56:16.578731+00:00
---

# Method: projects.locations.zones.interconnectAttachments.create  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments/create/




#  Method: projects.locations.zones.interconnectAttachments.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a new InterconnectAttachment in a given project and location.

### HTTP request

`POST https://edgenetwork.googleapis.com/v1/{parent=projects/*/locations/*/zones/*}/interconnectAttachments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Value for parent.  
  
### Query parameters

Parameters  
---  
`interconnectAttachmentId` |  `string` Required. Id of the requesting object If auto-generating Id server-side, remove this field and interconnectAttachmentId from the method_signature of Create RPC  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body contains an instance of `[InterconnectAttachment](https://docs.cloud.google.com/distributed-cloud/edge/1.7.1/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments#InterconnectAttachment)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/distributed-cloud/edge/1.7.1/docs/reference/network/rest/v1/projects.locations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
