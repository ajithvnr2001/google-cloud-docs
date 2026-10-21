---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/VectorSearch/
title: VectorSearch \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:20:58.493210+00:00
---

# VectorSearch  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/VectorSearch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VectorSearch Stay organized with collections  Save and categorize content based on your preferences. 

Defines a search operation using a query vector.

JSON representation  
---  
      
    
    {
      "searchField": string,
      "filter": {
        object
      },
      "outputFields": {
        object ([OutputFields](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/OutputFields))
      },
      "searchHint": {
        object ([SearchHint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/SearchHint))
      },
      "distanceMetric": enum ([DistanceMetric](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.indexes#DistanceMetric)),
    
      // Union field vector_type can be only one of the following:
      "vector": {
        object ([DenseVector](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects#DenseVector))
      },
      "sparseVector": {
        object ([SparseVector](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects#SparseVector))
      }
      // End of list of possible types for union field vector_type.
      "topK": integer
    }  
  
Fields  
---  
`searchField` |  `string` Required. The vector field to search.  
`filter` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. A JSON filter expression, e.g. {"genre": {"$eq": "sci-fi"}}, represented as a google.protobuf.Struct.  
`outputFields` |  `object (`[OutputFields](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/OutputFields)`)` Optional. Mask specifying which fields to return.  
`searchHint` |  `object (`[SearchHint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/SearchHint)`)` Optional. Sets the search hint. If no strategy is specified, the service will use an index if one is available, and fall back to the default KNN search otherwise.  
`distanceMetric` |  `enum (`[DistanceMetric](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.indexes#DistanceMetric)`)` Optional. The distance metric to use for the KNN search. If not specified, DOT_PRODUCT will be used as the default.  
Union field `vector_type`. Specifies the type of vector to use for the query. `vector_type` can be only one of the following:  
`vector` |  `object (`[DenseVector](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects#DenseVector)`)` A dense vector for the query.  
`sparseVector` |  `object (`[SparseVector](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1/projects.locations.collections.dataObjects#SparseVector)`)` A sparse vector for the query.  
`topK` |  `integer` Optional. The number of nearest neighbors to return.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
