---
url: https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1beta1/projects.locations.wasmPlugins.versions/list/
title: Method: projects.locations.wasmPlugins.versions.list \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:39.092426+00:00
---

# Method: projects.locations.wasmPlugins.versions.list  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1beta1/projects.locations.wasmPlugins.versions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Reference ](https://docs.cloud.google.com/service-extensions/docs/apis)



Send feedback 

#  Method: projects.locations.wasmPlugins.versions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * IAM Permissions



Lists `WasmPluginVersion` resources in a given project and location.

### HTTP request

`GET https://networkservices.googleapis.com/v1beta1/{parent=projects/*/locations/*/wasmPlugins/*}/versions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The `WasmPlugin` resource whose `WasmPluginVersion`s are listed, specified in the following format: `projects/{project}/locations/global/wasmPlugins/{wasmPlugin}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `networkservices.wasmPlugins.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum number of `WasmPluginVersion` resources to return per call. If not specified, at most 50 `WasmPluginVersion` resources are returned. The maximum value is 1000; values above 1000 are coerced to 1000.  
`pageToken` |  `string` The value returned by the last `ListWasmPluginVersionsResponse` call. Indicates that this is a continuation of a prior `versions.list` call, and that the next page of data is to be returned.  
  
### Request body

The request body must be empty.

### Response body

Response returned by the `versions.list` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "wasmPluginVersions": [
        {
          object ([WasmPluginVersion](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1beta1/projects.locations.wasmPlugins.versions#WasmPluginVersion))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`wasmPluginVersions[]` |  `object (`[WasmPluginVersion](https://docs.cloud.google.com/service-extensions/docs/reference/rest/v1beta1/projects.locations.wasmPlugins.versions#WasmPluginVersion)`)` List of `WasmPluginVersion` resources.  
`nextPageToken` |  `string` If there might be more results than those appearing in this response, then `nextPageToken` is included. To get the next set of results, call this method again using the value of `nextPageToken` as `pageToken`.  
`unreachable[]` |  `string` Unreachable resources. Populated when the request attempts to list all resources across all supported locations, while some locations are temporarily unavailable.  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `networkservices.wasmPlugins.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
