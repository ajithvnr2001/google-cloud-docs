---
url: https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.lbRouteExtensions/list/
title: Method: projects.locations.lbRouteExtensions.list \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:00.246271+00:00
---

# Method: projects.locations.lbRouteExtensions.list  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.lbRouteExtensions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Reference ](https://docs.cloud.google.com/service-extensions/docs/apis)



Send feedback 

#  Method: projects.locations.lbRouteExtensions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * IAM Permissions



Lists `LbRouteExtension` resources in a given project and location.

### HTTP request

`GET https://networkservices.googleapis.com/v1/{parent=projects/*/locations/*}/lbRouteExtensions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location from which the `LbRouteExtension` resources are listed. These values are specified in the following format: `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. The server might return fewer items than requested. If unspecified, the server picks an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results that the server returns.  
`filter` |  `string` Optional. Filtering results.  
`orderBy` |  `string` Optional. Hint about how to order the results.  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing `LbRouteExtension` resources.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "lbRouteExtensions": [
        {
          object ([LbRouteExtension](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.lbRouteExtensions#LbRouteExtension))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`lbRouteExtensions[]` |  `object (`[LbRouteExtension](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1/projects.locations.lbRouteExtensions#LbRouteExtension)`)` The list of `LbRouteExtension` resources.  
`nextPageToken` |  `string` A token identifying a page of results that the server returns.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `networkservices.lbRouteExtensions.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
