---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections.peeringRoutes/list/
title: Method: projects.locations.privateConnections.peeringRoutes.list \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:51:20.417689+00:00
---

# Method: projects.locations.privateConnections.peeringRoutes.list  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections.peeringRoutes/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  Method: projects.locations.privateConnections.peeringRoutes.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists the private connection routes exchanged over a peering connection.

### HTTP request

`GET https://vmwareengine.googleapis.com/v1/{parent=projects/*/locations/*/privateConnections/*}/peeringRoutes`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the private connection to retrieve peering routes from. Resource names are schemeless URIs that follow the conventions in <https://cloud.google.com/apis/design/resource_names>. For example: `projects/my-project/locations/us-west1/privateConnections/my-connection`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of peering routes to return in one page. The service may return fewer than this value. The maximum value is coerced to 1000. The default value of this field is 500.  
`pageToken` |  `string` A page token, received from a previous `peeringRoutes.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `peeringRoutes.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[VmwareEngine.ListPrivateConnectionPeeringRoutes](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.privateConnections.peeringRoutes/list#google.cloud.vmwareengine.v1.VmwareEngine.ListPrivateConnectionPeeringRoutes)`

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "peeringRoutes": [
        {
          object ([PeeringRoute](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/PeeringRoute))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`peeringRoutes[]` |  `object (`[PeeringRoute](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/PeeringRoute)`)` A list of peering routes.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
