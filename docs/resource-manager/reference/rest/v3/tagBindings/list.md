---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/list/
title: Method: tagBindings.list \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:31.295327+00:00
---

# Method: tagBindings.list  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: tagBindings.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the TagBindings for the given Google Cloud resource, as specified with `parent`.

NOTE: The `parent` field is expected to be a full resource name: <https://cloud.google.com/apis/design/resource_names#fullResourceName>

### HTTP request

`GET https://cloudresourcemanager.googleapis.com/v3/tagBindings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`parent` |  `string` Required. The full resource name of a resource for which you want to list existing TagBindings. E.g. "//cloudresourcemanager.googleapis.com/projects/123"  
`pageSize` |  `integer` Optional. The maximum number of TagBindings to return in the response. The server allows a maximum of 300 TagBindings to return. If unspecified, the server will use 100 as the default.  
`pageToken` |  `string` Optional. A pagination token returned from a previous call to `tagBindings.list` that indicates where this listing should continue from.  
  
### Request body

The request body must be empty.

### Response body

The tagBindings.list response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "tagBindings": [
        {
          object ([TagBinding](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings#TagBinding))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`tagBindings[]` |  `object (`[TagBinding](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings#TagBinding)`)` A possibly paginated list of TagBindings for the specified resource.  
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
