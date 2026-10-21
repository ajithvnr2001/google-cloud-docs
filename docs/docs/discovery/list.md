---
url: https://docs.cloud.google.com/docs/discovery/list/
title: Discovery Document: list \u00a0|\u00a0 Google APIs Discovery Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:39:58.223221+00:00
---

# Discovery Document: list  |  Google APIs Discovery Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/discovery/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Google APIs Discovery Service ](https://docs.cloud.google.com/docs/discovery)



#  Discovery Document: list Stay organized with collections  Save and categorize content based on your preferences. 

Retrieve the list of APIs supported at this endpoint.

The `discovery.apis.list` method returns the list of all APIs supported by the Google APIs Discovery Service. The data for each entry is a subset of the Discovery Document for that API, and the list provides a directory of supported APIs. If a specific API has multiple versions, each of the versions has its own entry in the list. 

## Request

### HTTP Request
    
    
    GET https://discovery.googleapis.com/discovery/v1/apis
    

### Parameters

Parameter Name | Value | Description  
---|---|---  
**Optional Parameters**  
`name` | `string` |  Only include APIs with the given name.   
`preferred` | `boolean` |  Return only the preferred version of an API.  "`false`" by default.  
  
### Request Body

Do not supply a request body with this method.

## Response

If successful, this method returns a response body with the following structure:
    
    
    {
      "kind": "discovery#directoryList",
      "discoveryVersion": "v1",
      "items": [
        {
          "kind": "discovery#directoryItem",
          "id": string,
          "name": string,
          "version": string,
          "title": string,
          "description": string,
          "discoveryRestUrl": string,
          "discoveryLink": string,
          "icons": {
            "x16": string,
            "x32": string
          },
          "documentationLink": string,
          "labels": [
            string
          ],
          "preferred": boolean
        }
      ]
    }

Property Name | Value | Description  
---|---|---  
`kind` | `string` | The fixed string discovery#directoryList  
`discoveryVersion` | `string` | Indicate the version of the Discovery API used to generate this doc.  
`items[]` | `list` | The individual directory entries. One entry per API/version pair.  
`items[].kind` | `string` | The kind for this response.  
`items[].id` | `string` | The ID of this API.  
`items[].name` | `string` | The name of the API.  
`items[].version` | `string` | The version of the API.  
`items[].title` | `string` | The title of this API.  
`items[].description` | `string` | The description of this API.  
`items[].discoveryRestUrl` | `string` | The url for the discovery REST document.  
`items[].discoveryLink` | `string` | A link to the discovery document.  
`items[].icons` | `object` | Links to 16x16 and 32x32 icons representing the API.  
`items[].icons.x16` | `string` | The url of the 16x16 icon.  
`items[].icons.x32` | `string` | The url of the 32x32 icon.  
`items[].documentationLink` | `string` | A link to human readable documentation for the API.  
`items[].labels[]` | `list` |  Labels for the status of this API, such as `limited_availability` or `deprecated`.   
`items[].preferred` | `boolean` | `true` if this version is the preferred version to use.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
