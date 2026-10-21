---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse/
title: SearchDataObjectsResponse \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:44:13.866766+00:00
---

# SearchDataObjectsResponse  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  SearchDataObjectsResponse Stay organized with collections  Save and categorize content based on your preferences. 

Response for a search request.

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([SearchResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse#SearchResult))
        }
      ],
      "nextPageToken": string,
      "searchResponseMetadata": {
        object ([SearchResponseMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse#SearchResponseMetadata))
      }
    }  
  
Fields  
---  
`results[]` |  `object (`[SearchResult](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse#SearchResult)`)` Output only. The list of dataObjects that match the search criteria.  
`nextPageToken` |  `string` Output only. A token to retrieve next page of results. Pass to [DataObjectSearchService.SearchDataObjectsRequest.page_token][] to obtain that page.  
`searchResponseMetadata` |  `object (`[SearchResponseMetadata](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse#SearchResponseMetadata)`)` Output only. Metadata about the search execution.  
  
## SearchResult

A single search result.

JSON representation  
---  
      
    
    {
      "dataObject": {
        object ([DataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects#DataObject))
      },
      "distance": number
    }  
  
Fields  
---  
`dataObject` |  `object (`[DataObject](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects#DataObject)`)` Output only. The matching data object.  
`distance` |  `number` Output only. Similarity distance or ranker score returned by BatchSearchDataObjects.  
  
## SearchResponseMetadata

Metadata about the search execution.

JSON representation  
---  
      
    
    {
      "warnings": [
        {
          object ([Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/Shared.Types/ListOperationsResponse#Status))
        }
      ],
    
      // Union field index_type can be only one of the following:
      "usedIndex": {
        object ([IndexInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse#IndexInfo))
      },
      "usedKnn": boolean
      // End of list of possible types for union field index_type.
    }  
  
Fields  
---  
`warnings[]` |  `object (`[Status](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. Warnings or non-fatal errors that occurred during execution.  
Union field `index_type`. The type of index used. `index_type` can be only one of the following:  
`usedIndex` |  `object (`[IndexInfo](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/SearchDataObjectsResponse#IndexInfo)`)` Indicates that the search used a particular index.  
`usedKnn` |  `boolean` Output only. If true, the search used the system's default K-Nearest Neighbor (KNN) index engine.  
  
## IndexInfo

Message that indicates the index used for the search.

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the index used for the search. Format: `projects/{project}/locations/{location}/collections/{collection}/indexes/{index}`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
