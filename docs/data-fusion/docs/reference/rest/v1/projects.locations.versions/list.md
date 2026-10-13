---
url: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.versions/list/
title: Method: projects.locations.versions.list \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:17:09.656416+00:00
---

# Method: projects.locations.versions.list  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.versions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Reference ](https://docs.cloud.google.com/data-fusion/docs/reference)



Send feedback 

#  Method: projects.locations.versions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists possible versions for Data Fusion instances in the specified project and location.

### HTTP request

`GET https://datafusion.googleapis.com/v1/{parent=projects/*/locations/*}/versions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location for which to retrieve instance information in the format projects/{project}/locations/{location}.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of items to return.  
`pageToken` |  `string` The nextPageToken value to use if there are additional results to retrieve for this list request.  
`latestPatchOnly` |  `boolean` Whether or not to return the latest patch of every available minor version. If true, only the latest patch will be returned. Ex. if allowed versions is [6.1.1, 6.1.2, 6.2.0] then response will be [6.1.2, 6.2.0]  
  
### Request body

The request body must be empty.

### Response body

Response message for the list available versions request.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "availableVersions": [
        {
          object ([Version](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances#Version))
        }
      ],
      "nextPageToken": string,
      "versions": [
        {
          object ([Version](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances#Version))
        }
      ]
    }  
  
Fields  
---  
`availableVersions[]  
**(deprecated)**` |  `object (`[Version](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances#Version)`)` This item is deprecated!Represents a list of versions that are supported. Deprecated: Use versions field instead.  
`nextPageToken` |  `string` Token to retrieve the next page of results or empty if there are no more results in the list.  
`versions[]` |  `object (`[Version](https://docs.cloud.google.com/data-fusion/docs/reference/rest/v1/projects.locations.instances#Version)`)` Represents a list of all versions.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-20 UTC."],[],[]] 
