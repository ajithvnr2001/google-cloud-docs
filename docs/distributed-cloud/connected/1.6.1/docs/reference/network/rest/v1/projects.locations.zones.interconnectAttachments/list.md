---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments/list/
title: Method: projects.locations.zones.interconnectAttachments.list \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:20.642051+00:00
---

# Method: projects.locations.zones.interconnectAttachments.list  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments/list/




#  Method: projects.locations.zones.interconnectAttachments.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists InterconnectAttachments in a given project and location.

### HTTP request

`GET https://edgenetwork.googleapis.com/v1/{parent=projects/*/locations/*/zones/*}/interconnectAttachments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ListInterconnectAttachmentsRequest  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` A token identifying a page of results the server should return.  
`filter` |  `string` Filtering results  
`orderBy` |  `string` Hint for how to order the results  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing InterconnectAttachments

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "interconnectAttachments": [
        {
          object ([InterconnectAttachment](https://docs.cloud.google.com/distributed-cloud/edge/1.6.1/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments#InterconnectAttachment))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`interconnectAttachments[]` |  `object (`[InterconnectAttachment](https://docs.cloud.google.com/distributed-cloud/edge/1.6.1/docs/reference/network/rest/v1/projects.locations.zones.interconnectAttachments#InterconnectAttachment)`)` The list of InterconnectAttachment  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
