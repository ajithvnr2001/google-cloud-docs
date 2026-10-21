---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/search/
title: Method: projects.locations.collections.dataObjects.search \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:34:34.942911+00:00
---

# Method: projects.locations.collections.dataObjects.search  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.collections.dataObjects.search Stay organized with collections  Save and categorize content based on your preferences. 

Searches data objects.

### HTTP request

`POST https://vectorsearch.googleapis.com/v1beta/{parent}/dataObjects:search`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the Collection for which to search. Format: `projects/{project}/locations/{location}/collections/{collection}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "pageSize": integer,
      "pageToken": string,
    
      // Union field search_type can be only one of the following:
      "vectorSearch": {
        object ([VectorSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/VectorSearch))
      },
      "semanticSearch": {
        object ([SemanticSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SemanticSearch))
      },
      "textSearch": {
        object ([TextSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/TextSearch))
      }
      // End of list of possible types for union field search_type.
    }  
  
Fields  
---  
`pageSize` |  `integer` Optional. The standard list page size. Only supported for KNN. If not set, up to search_type.top_k results will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. The standard list page token. Typically obtained via `[SearchDataObjectsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse#FIELDS.next_page_token)` of the previous `[DataObjectSearchService.SearchDataObjects](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/search#google.cloud.vectorsearch.v1beta.DataObjectSearchService.SearchDataObjects)` call.  
Union field `search_type`. The query to search for. `search_type` can be only one of the following:  
`vectorSearch` |  `object (`[VectorSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/VectorSearch)`)` A vector search operation.  
`semanticSearch` |  `object (`[SemanticSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SemanticSearch)`)` A semantic search operation.  
`textSearch` |  `object (`[TextSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/TextSearch)`)` Optional. A text search operation.  
  
### Response body

If successful, the response body contains an instance of `[SearchDataObjectsResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `vectorsearch.dataObjects.search`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
