---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/list/
title: Method: tagValues.list \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:36:32.292520+00:00
---

# Method: tagValues.list  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: tagValues.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all TagValues for a specific TagKey.

### HTTP request

`GET https://cloudresourcemanager.googleapis.com/v3/tagValues`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Query parameters

Parameters  
---  
`parent` |  `string` Required. Resource name for the parent of the TagValues to be listed, in the format `tagKeys/123` or `tagValues/123`.  
`pageSize` |  `integer` Optional. The maximum number of TagValues to return in the response. The server allows a maximum of 300 TagValues to return. If unspecified, the server will use 100 as the default.  
`pageToken` |  `string` Optional. A pagination token returned from a previous call to `tagValues.list` that indicates where this listing should continue from.  
  
### Request body

The request body must be empty.

### Response body

The tagValues.list response.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "tagValues": [
        {
          object ([TagValue](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues#TagValue))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`tagValues[]` |  `object (`[TagValue](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues#TagValue)`)` A possibly paginated list of TagValues that are direct descendants of the specified parent TagKey.  
`nextPageToken` |  `string` A pagination token returned from a previous call to `tagValues.list` that indicates from where listing should continue. This is currently not used, but the server may at any point start supplying a valid token.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
