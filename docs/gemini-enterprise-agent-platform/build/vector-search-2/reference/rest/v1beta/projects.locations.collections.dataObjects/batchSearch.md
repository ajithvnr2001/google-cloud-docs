---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch/
title: Method: projects.locations.collections.dataObjects.batchSearch \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:53:03.476410+00:00
---

# Method: projects.locations.collections.dataObjects.batchSearch  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.collections.dataObjects.batchSearch Stay organized with collections  Save and categorize content based on your preferences. 

Batch searches data objects.

### HTTP request

`POST https://vectorsearch.googleapis.com/v1beta/{parent}/dataObjects:batchSearch`

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
          object ([Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#Search))
        }
      ],
      "combine": {
        object ([CombineResultsOptions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#CombineResultsOptions))
      }
    }  
  
Fields  
---  
`searches[]` |  `object (`[Search](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#Search)`)` Required. A list of search requests to execute in parallel.  
`combine` |  `object (`[CombineResultsOptions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#CombineResultsOptions)`)` Optional. Options for combining the results of the batch search operations.  
  
### Response body

A response from a batch search operation.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([SearchDataObjectsResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse))
        }
      ]
    }  
  
Fields  
---  
`results[]` |  `object (`[SearchDataObjectsResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse)`)` Output only. A list of search responses, one for each request in the batch. If a ranker is used, a single ranked list of results is returned.  
  
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
Union field `search_type`. The type of search to perform. `search_type` can be only one of the following:  
`vectorSearch` |  `object (`[VectorSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/VectorSearch)`)` A vector-based search.  
`semanticSearch` |  `object (`[SemanticSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SemanticSearch)`)` A semantic search.  
`textSearch` |  `object (`[TextSearch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/TextSearch)`)` A text search operation.  
  
## CombineResultsOptions

Options for combining the results of the batch search operations.

JSON representation  
---  
      
    
    {
      "ranker": {
        object ([Ranker](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#Ranker))
      },
      "outputFields": {
        object ([OutputFields](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/OutputFields))
      },
      "topK": integer
    }  
  
Fields  
---  
`ranker` |  `object (`[Ranker](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#Ranker)`)` Required. The ranker to use for combining the results.  
`outputFields` |  `object (`[OutputFields](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/OutputFields)`)` Optional. Mask specifying which fields to return.  
`topK` |  `integer` Optional. The number of results to return. If not set, a default value will be used.  
  
## Ranker

Defines a ranker to combine results from multiple searches.

JSON representation  
---  
      
    
    {
    
      // Union field ranker can be only one of the following:
      "rrf": {
        object ([ReciprocalRankFusion](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#ReciprocalRankFusion))
      }
      // End of list of possible types for union field ranker.
    
      // Union field reranker can be only one of the following:
      "vertexRanker": {
        object ([VertexRanker](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#VertexRanker))
      }
      // End of list of possible types for union field reranker.
    }  
  
Fields  
---  
Union field `ranker`. The ranking method to use. `ranker` can be only one of the following:  
`rrf` |  `object (`[ReciprocalRankFusion](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#ReciprocalRankFusion)`)` Reciprocal Rank Fusion ranking.  
Union field `reranker`. The reranker to use for final ranking of the results combined by the ranker. `reranker` can be only one of the following:  
`vertexRanker` |  `object (`[VertexRanker](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#VertexRanker)`)` Optional. Vertex AI ranking.  
  
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
  
## VertexRanker

Defines a ranker using the Vertex AI ranking service. See <https://cloud.google.com/generative-ai-app-builder/docs/ranking> for details.

JSON representation  
---  
      
    
    {
      "model": string,
      "topN": integer,
    
      // Union field record_spec can be only one of the following:
      "textRecordSpec": {
        object ([TextRecordSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#TextRecordSpec))
      }
      // End of list of possible types for union field record_spec.
    }  
  
Fields  
---  
`model` |  `string` Required. The model used for ranking documents. The list of available models is described in <https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking#models>. Currently, only `semantic-ranker-fast@latest` is supported.  
`topN` |  `integer` Required. The number of documents to be processed for ranking.  
Union field `record_spec`. The record specification for ranking. At least one record spec must be set. `record_spec` can be only one of the following:  
`textRecordSpec` |  `object (`[TextRecordSpec](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/batchSearch#TextRecordSpec)`)` The record spec for text search.  
  
## TextRecordSpec

The record spec for text search.

JSON representation  
---  
      
    
    {
      "query": string,
      "titleTemplate": string,
      "contentTemplate": string
    }  
  
Fields  
---  
`query` |  `string` Required. The query against which the records are ranked and scored.  
`titleTemplate` |  `string` Optional. The template used to generate the record's title.  
`contentTemplate` |  `string` Optional. The template used to generate the record's content.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
