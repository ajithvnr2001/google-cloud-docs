---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths/list/
title: Method: projects.locations.networkMonitoringProviders.networkPaths.list \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:43.910973+00:00
---

# Method: projects.locations.networkMonitoringProviders.networkPaths.list  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Method: projects.locations.networkMonitoringProviders.networkPaths.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists `[NetworkPaths](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#NetworkPath)` for a given network monitoring provider.

### HTTP request

`GET https://networkmanagement.googleapis.com/v1alpha1/{parent=projects/*/locations/*/networkMonitoringProviders/*}/networkPaths`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ListNetworkPathsRequest. Format: projects/{project}/locations/{location}/networkMonitoringProviders/{networkMonitoringProvider}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of network paths to return. The service may return fewer than this value. If unspecified, at most 20 network pathswill be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `networkPaths.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `networkPaths.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing NetworkPaths

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "networkPaths": [
        {
          object ([NetworkPath](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#NetworkPath))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`networkPaths[]` |  `object (`[NetworkPath](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders.networkPaths#NetworkPath)`)` The list of NetworkPath  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `networkmanagement.networkPaths.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-17 UTC."],[],[]] 
