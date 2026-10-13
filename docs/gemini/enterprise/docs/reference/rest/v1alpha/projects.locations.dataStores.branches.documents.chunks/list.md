---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.branches.documents.chunks/list/
title: Method: projects.locations.dataStores.branches.documents.chunks.list \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:42:32.512451+00:00
---

# Method: projects.locations.dataStores.branches.documents.chunks.list  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.branches.documents.chunks/list/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.dataStores.branches.documents.chunks.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes



Gets a list of `[Chunk](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk)`s.

### HTTP request

Choose an endpoint:

globalus

  
`GET https://discoveryengine.googleapis.com/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*/documents/*}/chunks`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent document resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}/branches/{branch}/documents/{document}`.If the caller does not have permission to list `[Chunk](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk)`s under this document, regardless of whether or not this document exists, a `PERMISSION_DENIED` error is returned.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Maximum number of `[Chunk](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.dataStores.branches.documents.chunks#Chunk)`s to return. If unspecified, defaults to 100. The maximum allowed value is 1000. Values above 1000 will be coerced to 1000.If this field is negative, an `INVALID_ARGUMENT` error is returned.  
`pageToken` |  `string` A page token `[ListChunksResponse.next_page_token](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/ListChunksResponse#FIELDS.next_page_token)`, received from a previous `[ChunkService.ListChunks](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.branches.documents.chunks/list#google.cloud.discoveryengine.v1alpha.ChunkService.ListChunks)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[ChunkService.ListChunks](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.dataStores.branches.documents.chunks/list#google.cloud.discoveryengine.v1alpha.ChunkService.ListChunks)` must match the call that provided the page token. Otherwise, an `INVALID_ARGUMENT` error is returned.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListChunksResponse](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/ListChunksResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
