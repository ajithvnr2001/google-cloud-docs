---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes/list/
title: Method: projects.locations.meshes.list \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:53:43.063438+00:00
---

# Method: projects.locations.meshes.list  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes/list/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/service-mesh/v1.29/docs/apis)



Send feedback 

#  Method: projects.locations.meshes.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists Meshes in a given project and location.

### HTTP request

`GET https://networkservices.googleapis.com/v1/{parent=projects/*/locations/*}/meshes`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location from which the Meshes should be listed, specified in the format `projects/*/locations/*`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `networkservices.meshes.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum number of Meshes to return per call.  
`pageToken` |  `string` The value returned by the last `ListMeshesResponse` Indicates that this is a continuation of a prior `meshes.list` call, and that the system should return the next page of data.  
`returnPartialSuccess` |  `boolean` Optional. If true, allow partial responses for multi-regional Aggregated List requests. Otherwise if one of the locations is down or unreachable, the Aggregated List request will fail.  
  
### Request body

The request body must be empty.

### Response body

Response returned by the meshes.list method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "meshes": [
        {
          object ([Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes#Mesh))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`meshes[]` |  `object (`[Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes#Mesh)`)` List of Mesh resources.  
`nextPageToken` |  `string` If there might be more results than those appearing in this response, then `nextPageToken` is included. To get the next set of results, call this method again using the value of `nextPageToken` as `pageToken`.  
`unreachable[]` |  `string` Unreachable resources. Populated when the request opts into `returnPartialSuccess` and reading across collections e.g. when attempting to list all resources across all supported locations.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-25 UTC."],[],[]] 
