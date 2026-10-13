---
url: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/listSpokes/
title: Method: projects.locations.global.hubs.listSpokes \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:08.375067+00:00
---

# Method: projects.locations.global.hubs.listSpokes  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/listSpokes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Reference ](https://docs.cloud.google.com/network-connectivity/docs/apis)



Send feedback 

#  Method: projects.locations.global.hubs.listSpokes Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * SpokeView
  * Try it!



Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

### HTTP request

`GET https://networkconnectivity.googleapis.com/v1/{name=projects/*/locations/global/hubs/*}:listSpokes`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the hub. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `networkconnectivity.hubs.listSpokes`

  
  
### Query parameters

Parameters  
---  
`spokeLocations[]` |  `string` A list of locations. Specify one of the following: `[global]`, a single region (for example, `[us-central1]`), or a combination of values (for example, `[global, us-central1, us-west1]`). If the spokeLocations field is populated, the list of results includes only spokes in the specified location. If the spokeLocations field is not populated, the list of results includes spokes in all locations.  
`pageSize` |  `integer` The maximum number of results to return per page.  
`pageToken` |  `string` The page token.  
`filter` |  `string` An expression that filters the list of results.  
`orderBy` |  `string` Sort the results by name or createTime.  
`view` |  `enum (`[SpokeView](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/listSpokes#SpokeView)`)` The view of the spoke to return. The view that you use determines which spoke fields are included in the response.  
  
### Request body

The request body must be empty.

### Response body

The response for `[HubService.ListHubSpokes](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.hubs/listSpokes#google.cloud.networkconnectivity.v1.HubService.ListHubSpokes)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "spokes": [
        {
          object ([Spoke](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`spokes[]` |  `object (`[Spoke](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/Shared.Types/Spoke)`)` The requested spokes. The spoke fields can be partially populated based on the `view` field in the request message.  
`nextPageToken` |  `string` The token for the next page of the response. To see more results, use this value as the pageToken for your next request. If this value is empty, there are no more results.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## SpokeView

Enum that controls which spoke fields are included in the response.

Enums  
---  
`SPOKE_VIEW_UNSPECIFIED` | The spoke view is unspecified. When the spoke view is unspecified, the API returns the same fields as the `BASIC` view.  
`BASIC` | Includes `name`, `createTime`, `hub`, `uniqueId`, `state`, `reasons`, and `spokeType`. This is the default value.  
`DETAILED` | Includes all spoke fields except `labels`. You can use the `DETAILED` view only when you set the `spokeLocations` field to `[global]`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
