---
url: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes/list/
title: Method: projects.locations.global.policyBasedRoutes.list \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:04.657586+00:00
---

# Method: projects.locations.global.policyBasedRoutes.list  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Reference ](https://docs.cloud.google.com/network-connectivity/docs/apis)



Send feedback 

#  Method: projects.locations.global.policyBasedRoutes.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists policy-based routes in a given project and location.

### HTTP request

`GET https://networkconnectivity.googleapis.com/v1beta/{parent=projects/*/locations/global}/policyBasedRoutes`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource's name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `networkconnectivity.policyBasedRoutes.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of results per page that should be returned.  
`pageToken` |  `string` The page token.  
`filter` |  `string` A filter expression that filters the results listed in the response.  
`orderBy` |  `string` Sort the results by a certain order.  
  
### Request body

The request body must be empty.

### Response body

Response for `[PolicyBasedRoutingService.ListPolicyBasedRoutes](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes/list#google.cloud.networkconnectivity.v1beta.PolicyBasedRoutingService.ListPolicyBasedRoutes)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "policyBasedRoutes": [
        {
          object ([PolicyBasedRoute](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#PolicyBasedRoute))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`policyBasedRoutes[]` |  `object (`[PolicyBasedRoute](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1beta/projects.locations.global.policyBasedRoutes#PolicyBasedRoute)`)` Policy-based routes to be returned.  
`nextPageToken` |  `string` The next pagination token in the List response. It should be used as pageToken for the following request. An empty value means no more result.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
