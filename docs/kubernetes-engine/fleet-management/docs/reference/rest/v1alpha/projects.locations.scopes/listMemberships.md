---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/listMemberships/
title: Method: projects.locations.scopes.listMemberships \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:11.732550+00:00
---

# Method: projects.locations.scopes.listMemberships  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.scopes/listMemberships/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.scopes.listMemberships Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists Memberships bound to a Scope. The response includes relevant Memberships from all regions.

### HTTP request

`GET https://gkehub.googleapis.com/v1alpha/{scopeName=projects/*/locations/*/scopes/*}:listMemberships`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`scopeName` |  `string` Required. Name of the Scope, in the format `projects/*/locations/global/scopes/*`, to which the Memberships are bound. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `scopeName`:

  * `gkehub.scopes.listBoundMemberships`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. Lists Memberships that match the filter expression, following the syntax outlined in <https://google.aip.dev/160>. Currently, filtering can be done only based on Memberships's `name`, `labels`, `createTime`, `updateTime`, and `uniqueId`.  
`pageSize` |  `integer` Optional. When requesting a 'page' of resources, `pageSize` specifies number of resources to return. If unspecified or set to 0, all resources will be returned. Pagination is currently not supported; therefore, setting this field does not have any impact for now.  
`pageToken` |  `string` Optional. Token returned by previous call to `scopes.listMemberships` which specifies the position in the list from where to continue listing the resources.  
  
### Request body

The request body must be empty.

### Response body

List of Memberships bound to a Scope.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "memberships": [
        {
          object ([Membership](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#Membership))
        }
      ],
      "unreachable": [
        string
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`memberships[]` |  `object (`[Membership](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.memberships#Membership)`)` The list of Memberships bound to the given Scope.  
`unreachable[]` |  `string` List of locations that could not be reached while fetching this list.  
`nextPageToken` |  `string` A token to request the next page of resources from the `scopes.listMemberships` method. The value of an empty string means that there are no more resources to return.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-12 UTC."],[],[]] 
