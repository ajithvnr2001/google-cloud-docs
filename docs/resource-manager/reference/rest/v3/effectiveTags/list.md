---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/effectiveTags/list/
title: Method: effectiveTags.list \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:39:09.456345+00:00
---

# Method: effectiveTags.list  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/effectiveTags/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: effectiveTags.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * EffectiveTag
    * JSON representation
  * Try it!



Return a list of effective tags for the given Google Cloud resource, as specified in `parent`.

### HTTP request

`GET https://cloudresourcemanager.googleapis.com/v3/effectiveTags`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`parent` |  `string` Required. The full resource name of a resource for which you want to list the effective tags. E.g. "//cloudresourcemanager.googleapis.com/projects/123"  
`pageSize` |  `integer` Optional. The maximum number of effective tags to return in the response. The server allows a maximum of 300 effective tags to return in a single page. If unspecified, the server will use 100 as the default.  
`pageToken` |  `string` Optional. A pagination token returned from a previous call to `effectiveTags.list` that indicates from where this listing should continue.  
  
### Request body

The request body must be empty.

### Response body

The response of effectiveTags.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "effectiveTags": [
        {
          object ([EffectiveTag](https://docs.cloud.google.com/resource-manager/reference/rest/v3/effectiveTags/list#EffectiveTag))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`effectiveTags[]` |  `object (`[EffectiveTag](https://docs.cloud.google.com/resource-manager/reference/rest/v3/effectiveTags/list#EffectiveTag)`)` A possibly paginated list of effective tags for the specified resource.  
`nextPageToken` |  `string` Pagination token.If the result set is too large to fit in a single response, this token is returned. It encodes the position of the current result cursor. Feeding this value into a new list request with the `pageToken` parameter gives the next page of the results.When `nextPageToken` is not filled in, there is no next page and the list returned is the last page in the result set.Pagination tokens have a limited lifetime.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## EffectiveTag

An EffectiveTag represents a tag that applies to a resource during policy evaluation. Tags can be either directly bound to a resource or inherited from its ancestor. EffectiveTag contains the name and namespacedName of the tag value and tag key, with additional fields of `inherited` to indicate the inheritance status of the effective tag.

JSON representation  
---  
      
    
    {
      "tagValue": string,
      "namespacedTagValue": string,
      "tagKey": string,
      "namespacedTagKey": string,
      "tagKeyParentName": string,
      "inherited": boolean
    }  
  
Fields  
---  
`tagValue` |  `string` Resource name for TagValue in the format `tagValues/456`.  
`namespacedTagValue` |  `string` The namespaced name of the TagValue. Can be in the form `{organizationId}/{tag_key_short_name}/{tag_value_short_name}` or `{projectId}/{tag_key_short_name}/{tag_value_short_name}` or `{projectNumber}/{tag_key_short_name}/{tag_value_short_name}`.  
`tagKey` |  `string` The name of the TagKey, in the format `tagKeys/{id}`, such as `tagKeys/123`.  
`namespacedTagKey` |  `string` The namespaced name of the TagKey. Can be in the form `{organizationId}/{tag_key_short_name}` or `{projectId}/{tag_key_short_name}` or `{projectNumber}/{tag_key_short_name}`.  
`tagKeyParentName` |  `string` The parent name of the tag key. Must be in the format `organizations/{organizationId}` or `projects/{projectNumber}`  
`inherited` |  `boolean` Indicates the inheritance status of a tag value attached to the given resource. If the tag value is inherited from one of the resource's ancestors, inherited will be true. If false, then the tag value is directly attached to the resource, inherited will be false.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
