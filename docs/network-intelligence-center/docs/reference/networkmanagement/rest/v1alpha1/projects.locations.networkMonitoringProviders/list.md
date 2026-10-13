---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders/list/
title: Method: projects.locations.networkMonitoringProviders.list \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:42.091716+00:00
---

# Method: projects.locations.networkMonitoringProviders.list  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  Method: projects.locations.networkMonitoringProviders.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists `[NetworkMonitoringProviders](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)` for a given project and location.

### HTTP request

`GET https://networkmanagement.googleapis.com/v1alpha1/{parent=projects/*/locations/*}/networkMonitoringProviders`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ListNetworkMonitoringProvidersRequest. Format: `projects/{project}/locations/{location}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of monitoring points to return. The service may return fewer than this value. If unspecified, at most 20 monitoring points will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `ListMonitoringPoints` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `ListMonitoringPoints` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing NetworkMonitoringProviders

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "networkMonitoringProviders": [
        {
          object ([NetworkMonitoringProvider](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`networkMonitoringProviders[]` |  `object (`[NetworkMonitoringProvider](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1alpha1/projects.locations.networkMonitoringProviders#NetworkMonitoringProvider)`)` The list of NetworkMonitoringProvider  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-network-insights`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `networkmanagement.providers.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-17 UTC."],[],[]] 
