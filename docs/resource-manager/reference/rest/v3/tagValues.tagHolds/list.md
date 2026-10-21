---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues.tagHolds/list/
title: Method: tagValues.tagHolds.list \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:33.922036+00:00
---

# Method: tagValues.tagHolds.list  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues.tagHolds/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: tagValues.tagHolds.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists TagHolds under a TagValue.

### HTTP request

`GET https://cloudresourcemanager.googleapis.com/v3/{parent=tagValues/*}/tagHolds`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the parent TagValue. Must be of the form: `tagValues/{tag-value-id}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of TagHolds to return in the response. The server allows a maximum of 300 TagHolds to return. If unspecified, the server will use 100 as the default.  
`pageToken` |  `string` Optional. A pagination token returned from a previous call to `tagHolds.list` that indicates where this listing should continue from.  
`filter` |  `string` Optional. Criteria used to select a subset of TagHolds parented by the TagValue to return. This field follows the syntax defined by aip.dev/160; the `holder` and `origin` fields are supported for filtering. Currently only `AND` syntax is supported. Some example queries are:

  * `holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group`
  * `origin = 35678234`
  * `holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group AND origin = 35678234`

  
  
### Request body

The request body must be empty.

### Response body

The tagHolds.list response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "tagHolds": [
        {
          object ([TagHold](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues.tagHolds#TagHold))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`tagHolds[]` |  `object (`[TagHold](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues.tagHolds#TagHold)`)` A possibly paginated list of TagHolds.  
`nextPageToken` |  `string` Pagination token.If the result set is too large to fit in a single response, this token is returned. It encodes the position of the current result cursor. Feeding this value into a new list request with the `pageToken` parameter gives the next page of the results.When `nextPageToken` is not filled in, there is no next page and the list returned is the last page in the result set.Pagination tokens have a limited lifetime.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
