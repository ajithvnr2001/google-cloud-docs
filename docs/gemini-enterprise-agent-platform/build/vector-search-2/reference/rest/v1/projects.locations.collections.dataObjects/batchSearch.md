---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchSearch/
title: Method: projects.locations.collections.dataObjects.batchSearch \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:57:02.675815+00:00
---

# Method: projects.locations.collections.dataObjects.batchSearch  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchSearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.collections.dataObjects.batchSearch Stay organized with collections  Save and categorize content based on your preferences. 

Batch searches data objects.

### HTTP request

`POST https://vectorsearch.googleapis.com/v1/{parent}/dataObjects:batchSearch`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the Collection for which to search. Format: `projects/{project}/locations/{location}/collections/{collection}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "searches": [
        {
          object ([Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchSearch#Search))
        }
      ],
      "combine": {
        object ([CombineResultsOptions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchSearch#CombineResultsOptions))
      }
    }  
  
Fields  
---  
`searches[]` |  `object (`[Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchSearch#Search)`)` Required. A list of search requests to execute in parallel.  
`combine` |  `object (`[CombineResultsOptions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchSearch#CombineResultsOptions)`)` Optional. Options for combining the results of the batch search operations.  
  
### Response body

A response from a batch search operation.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([SearchDataObjectsResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/SearchDataObjectsResponse))
        }
      ]
    }  
  
Fields  
---  
`results[]` |  `object (`[SearchDataObjectsResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/SearchDataObjectsResponse)`)` Output only. A list of search responses, one for each request in the batch. If a ranker is used, a single ranked list of results is returned.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `vectorsearch.dataObjects.search`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## Search

A single search request within a batch operation.

JSON representation  
---  
      
    
    {
    
      // Union field search_type can be only one of the following:
      "vectorSearch": {
        object ([VectorSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/VectorSearch))
      },
      "semanticSearch": {
        object ([SemanticSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/SemanticSearch))
      },
      "textSearch": {
        object ([TextSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/TextSearch))
      }
      // End of list of possible types for union field search_type.
    }  
  
Fields  
---  
Union field `search_type`. The type of search to perform. `search_type` can be only one of the following:  
`vectorSearch` |  `object (`[VectorSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/VectorSearch)`)` A vector-based search.  
`semanticSearch` |  `object (`[SemanticSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/SemanticSearch)`)` A semantic search.  
`textSearch` |  `object (`[TextSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/TextSearch)`)` A text search operation.  
  
## CombineResultsOptions

Options for combining the results of the batch search operations.

JSON representation  
---  
      
    
    {
      "ranker": {
        object ([Ranker](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchSearch#Ranker))
      },
      "outputFields": {
        object ([OutputFields](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/OutputFields))
      },
      "topK": integer
    }  
  
Fields  
---  
`ranker` |  `object (`[Ranker](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchSearch#Ranker)`)` Required. The ranker to use for combining the results.  
`outputFields` |  `object (`[OutputFields](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/OutputFields)`)` Optional. Mask specifying which fields to return.  
`topK` |  `integer` Optional. The number of results to return. If not set, a default value will be used.  
  
## Ranker

Defines a ranker to combine results from multiple searches.

JSON representation  
---  
      
    
    {
    
      // Union field ranker can be only one of the following:
      "rrf": {
        object ([ReciprocalRankFusion](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchSearch#ReciprocalRankFusion))
      }
      // End of list of possible types for union field ranker.
    }  
  
Fields  
---  
Union field `ranker`. The ranking method to use. `ranker` can be only one of the following:  
`rrf` |  `object (`[ReciprocalRankFusion](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects/batchSearch#ReciprocalRankFusion)`)` Reciprocal Rank Fusion ranking.  
  
## ReciprocalRankFusion

Defines the Reciprocal Rank Fusion (RRF) algorithm for result ranking.

JSON representation  
---  
      
    
    {
      "weights": [
        number
      ]
    }  
  
Fields  
---  
`weights[]` |  `number` Required. The weights to apply to each search result set during fusion.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
