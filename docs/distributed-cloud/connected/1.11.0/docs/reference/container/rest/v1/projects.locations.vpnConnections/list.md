---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections/list/
title: Method: projects.locations.vpnConnections.list \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:18.866578+00:00
---

# Method: projects.locations.vpnConnections.list  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections/list/




#  Method: projects.locations.vpnConnections.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists VPN connections in a given project and location.

### HTTP request

`GET https://edgecontainer.googleapis.com/v1/{parent=projects/*/locations/*}/vpnConnections`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent location, which owns this collection of VPN connections. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `edgecontainer.vpnConnections.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of resources to list.  
`pageToken` |  `string` A page token received from previous list request.  
`filter` |  `string` Only resources matching this filter will be listed.  
`orderBy` |  `string` Specifies the order in which resources will be listed.  
  
### Request body

The request body must be empty.

### Response body

List of VPN connections in a location.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "vpnConnections": [
        {
          object ([VpnConnection](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#VpnConnection))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`vpnConnections[]` |  `object (`[VpnConnection](https://docs.cloud.google.com/distributed-cloud/edge/1.11.0/docs/reference/container/rest/v1/projects.locations.vpnConnections#VpnConnection)`)` VpnConnections in the location.  
`nextPageToken` |  `string` A token to retrieve next page of results.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
