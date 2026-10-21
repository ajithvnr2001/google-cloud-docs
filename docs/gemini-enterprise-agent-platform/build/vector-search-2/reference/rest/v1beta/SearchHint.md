---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchHint/
title: SearchHint \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:57:09.300776+00:00
---

# SearchHint  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchHint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  SearchHint Stay organized with collections  Save and categorize content based on your preferences. 

Represents a hint to the search index engine.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "useIndex": {
        object ([IndexHint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchHint#IndexHint))
      },
      "useKnn": boolean,
      "knnHint": {
        object ([KnnHint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchHint#KnnHint))
      },
      "indexHint": {
        object ([IndexHint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchHint#IndexHint))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The type of index to use. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`useIndex  
**(deprecated)**` |  `object (`[IndexHint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchHint#IndexHint)`)` This item is deprecated!Optional. Deprecated: Use `indexHint` instead. Specifies that the search should use a particular index.  
`useKnn  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Deprecated: Use `knnHint` instead. If set to true, the search will use the system's default K-Nearest Neighbor (KNN) index engine.  
`knnHint` |  `object (`[KnnHint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchHint#KnnHint)`)` Optional. If set, the search will use the system's default K-Nearest Neighbor (KNN) index engine.  
`indexHint` |  `object (`[IndexHint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchHint#IndexHint)`)` Optional. Specifies that the search should use a particular index.  
End of mutually exclusive fields.  
  
## IndexHint

Message to specify the index to use for the search.

JSON representation  
---  
      
    
    {
      "name": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "denseScannParams": {
        object ([DenseScannParams](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchHint#DenseScannParams))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the index to use for the search. The index must be in the same project, location, and collection. Format: `projects/{project}/locations/{location}/collections/{collection}/indexes/{index}`  
The parameters for the index. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`denseScannParams` |  `object (`[DenseScannParams](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchHint#DenseScannParams)`)` Optional. Dense ScaNN parameters.  
End of mutually exclusive fields.  
  
## DenseScannParams

Parameters for dense ScaNN.

JSON representation  
---  
      
    
    {
      "searchLeavesPct": integer,
      "initialCandidateCount": integer,
      "targetRecall": number
    }  
  
Fields  
---  
`searchLeavesPct` |  `integer` Optional. Dense ANN param overrides to control recall and latency. The percentage of leaves to search, in the range [0, 100]. Not supported for `STORAGE_OPTIMIZED` indexes. Cannot be set together with `targetRecall`.  
`initialCandidateCount` |  `integer` Optional. The number of initial candidates. Must be a positive integer (> 0). Not supported for `STORAGE_OPTIMIZED` indexes. Cannot be set together with `targetRecall`.  
`targetRecall` |  `number` Optional. The target recall for the search. Must be a double in the range [0, 1]. While the search aims to achieve this level of recall, it is not guaranteed.  
  
## KnnHint

This type has no fields.

KnnHint will be used if search should be explicitly done on system's default K-Nearest Neighbor (KNN) index engine.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
