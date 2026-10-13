---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features/list/
title: Method: projects.locations.features.list \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:14.526886+00:00
---

# Method: projects.locations.features.list  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features/list/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.features.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists Features in a given project and location.

### HTTP request

`GET https://gkehub.googleapis.com/v1beta/{parent=projects/*/locations/*}/features`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent (project and location) where the Features will be listed. Specified in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `gkehub.features.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` When requesting a 'page' of resources, `pageSize` specifies number of resources to return. If unspecified or set to 0, all resources will be returned.  
`pageToken` |  `string` Token returned by previous call to `features.list` which specifies the position in the list from where to continue listing the resources.  
`filter` |  `string` Lists Features that match the filter expression, following the syntax outlined in <https://google.aip.dev/160>.Examples:

  * Feature with the name "servicemesh" in project "foo-proj":


    
    
      name = "projects/foo-proj/locations/global/features/servicemesh"
    

  * Features that have a label called `foo`:


    
    
      labels.foo:*
    

  * Features that have a label called `foo` whose value is `bar`:


    
    
      labels.foo = bar
      
  
`orderBy` |  `string` One or more fields to compare and use to sort the output. See <https://google.aip.dev/132#ordering>.  
`returnPartialSuccess` |  `boolean` Optional. If set to true, the response will return partial results when some regions are unreachable and the unreachable field in Feature proto will be populated. If set to false, the request will fail when some regions are unreachable.  
  
### Request body

The request body must be empty.

### Response body

Response message for the `GkeHub.ListFeatures` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resources": [
        {
          object ([Feature](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features#Feature))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`resources[]` |  `object (`[Feature](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.features#Feature)`)` The list of matching Features  
`nextPageToken` |  `string` A token to request the next page of resources from the `features.list` method. The value of an empty string means that there are no more resources to return.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-12 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-12 UTC."],[],[]] 
