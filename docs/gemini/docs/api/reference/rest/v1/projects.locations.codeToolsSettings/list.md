---
url: https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings/list/
title: Method: projects.locations.codeToolsSettings.list \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:19.079061+00:00
---

# Method: projects.locations.codeToolsSettings.list  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ API and references ](https://docs.cloud.google.com/gemini/docs/api-and-reference)



Send feedback 

#  Method: projects.locations.codeToolsSettings.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists CodeToolsSettings in a given project and location.

### HTTP request

`GET https://cloudaicompanion.googleapis.com/v1/{parent=projects/*/locations/*}/codeToolsSettings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ListCodeToolsSettingsRequest  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filtering results.  
`orderBy` |  `string` Optional. Hint for how to order the results.  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing CodeToolsSettings

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "codeToolsSettings": [
        {
          object ([CodeToolsSetting](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings#CodeToolsSetting))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`codeToolsSettings[]` |  `object (`[CodeToolsSetting](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings#CodeToolsSetting)`)` The list of CodeToolsSetting  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `cloudaicompanion.codeToolsSettings.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-09 UTC."],[],[]] 
