---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec/
title: SearchSpec \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:01.366594+00:00
---

# SearchSpec  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  SearchSpec Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SearchParams
    * JSON representation
  * SearchResultList
    * JSON representation
  * SearchResult
    * JSON representation
  * UnstructuredDocumentInfo
    * JSON representation
  * DocumentContext
    * JSON representation
  * ExtractiveSegment
    * JSON representation
  * ExtractiveAnswer
    * JSON representation
  * ChunkInfo
    * JSON representation
  * DocumentMetadata
    * JSON representation



Search specification.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "searchParams": {
        object ([SearchParams](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#SearchParams))
      },
      "searchResultList": {
        object ([SearchResultList](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#SearchResultList))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Search parameters to control the search behavior. Or provide search result list to generate answer. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`searchParams` |  `object (`[SearchParams](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#SearchParams)`)` Search parameters.  
`searchResultList` |  `object (`[SearchResultList](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#SearchResultList)`)` Search result list.  
End of mutually exclusive fields.  
  
## SearchParams

Search parameters.

JSON representation  
---  
      
    
    {
      "maxReturnResults": integer,
      "filter": string,
      "boostSpec": {
        object (BoostSpec)
      },
      "orderBy": string,
      "searchResultMode": enum ([SearchResultMode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/ContentSearchSpec#SearchResultMode)),
      "dataStoreSpecs": [
        {
          object ([DataStoreSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/DataStoreSpec))
        }
      ]
    }  
  
Fields  
---  
`maxReturnResults` |  `integer` Number of search results to return. The default value is 10.  
`filter` |  `string` The filter syntax consists of an expression language for constructing a predicate from one or more fields of the documents being filtered. Filter expression is case-sensitive. This will be used to filter search results which may affect the Answer response.If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.Filtering in Vertex AI Search is done by mapping the LHS filter key to a key property defined in the Vertex AI Search backend -- this mapping is defined by the customer in their schema. For example a media customers might have a field 'name' in their schema. In this case the filter would look like this: filter --> name:'ANY("king kong")'For more information about filtering including syntax and filter operators, see [Filter](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)  
`boostSpec` |  `object (`BoostSpec`)` Boost specification to boost certain documents in search results which may affect the answer query response. For more information on boosting, see [Boosting](https://cloud.google.com/retail/docs/boosting#boost)  
`orderBy` |  `string` The order in which documents are returned. Documents can be ordered by a field in an `[Document](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents#Document)` object. Leave it unset if ordered by relevance. `orderBy` expression is case-sensitive. For more information on ordering, see [Ordering](https://cloud.google.com/retail/docs/filter-and-order#order)If this field is unrecognizable, an `INVALID_ARGUMENT` is returned.  
`searchResultMode` |  `enum (`[SearchResultMode](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/ContentSearchSpec#SearchResultMode)`)` Specifies the search result mode. If unspecified, the search result mode defaults to `DOCUMENTS`. See [parse and chunk documents](https://cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents)  
`dataStoreSpecs[]` |  `object (`[DataStoreSpec](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/DataStoreSpec)`)` Specs defining dataStores to filter on in a search call and configurations for those dataStores. This is only considered for engines with multiple dataStores use case. For single dataStore within an engine, they should use the specs at the top level.  
  
## SearchResultList

Search result list.

JSON representation  
---  
      
    
    {
      "searchResults": [
        {
          object ([SearchResult](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#SearchResult))
        }
      ]
    }  
  
Fields  
---  
`searchResults[]` |  `object (`[SearchResult](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#SearchResult)`)` Search results.  
  
## SearchResult

Search result.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "unstructuredDocumentInfo": {
        object ([UnstructuredDocumentInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#UnstructuredDocumentInfo))
      },
      "chunkInfo": {
        object ([ChunkInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#ChunkInfo))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Search result content. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`unstructuredDocumentInfo` |  `object (`[UnstructuredDocumentInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#UnstructuredDocumentInfo)`)` Unstructured document information.  
`chunkInfo` |  `object (`[ChunkInfo](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#ChunkInfo)`)` Chunk information.  
End of mutually exclusive fields.  
  
## UnstructuredDocumentInfo

Unstructured document information.

JSON representation  
---  
      
    
    {
      "document": string,
      "uri": string,
      "title": string,
      "documentContexts": [
        {
          object ([DocumentContext](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#DocumentContext))
        }
      ],
      "extractiveSegments": [
        {
          object ([ExtractiveSegment](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#ExtractiveSegment))
        }
      ],
      "extractiveAnswers": [
        {
          object ([ExtractiveAnswer](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#ExtractiveAnswer))
        }
      ]
    }  
  
Fields  
---  
`document` |  `string` Document resource name.  
`uri` |  `string` URI for the document.  
`title` |  `string` Title.  
`documentContexts[]` |  `object (`[DocumentContext](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#DocumentContext)`)` List of document contexts. The content will be used for Answer Generation. This is supposed to be the main content of the document that can be long and comprehensive.  
`extractiveSegments[]` |  `object (`[ExtractiveSegment](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#ExtractiveSegment)`)` List of extractive segments.  
`extractiveAnswers[]  
**(deprecated)**` |  `object (`[ExtractiveAnswer](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#ExtractiveAnswer)`)` This item is deprecated!Deprecated: This field is deprecated and will have no effect on the Answer generation. Please use documentContexts and extractiveSegments fields. List of extractive answers.  
  
## DocumentContext

Document context.

JSON representation  
---  
      
    
    {
      "pageIdentifier": string,
      "content": string
    }  
  
Fields  
---  
`pageIdentifier` |  `string` Page identifier.  
`content` |  `string` Document content to be used for answer generation.  
  
## ExtractiveSegment

Extractive segment. [Guide](https://cloud.google.com/generative-ai-app-builder/docs/snippets#extractive-segments) Answer generation will only use it if documentContexts is empty. This is supposed to be shorter snippets.

JSON representation  
---  
      
    
    {
      "pageIdentifier": string,
      "content": string
    }  
  
Fields  
---  
`pageIdentifier` |  `string` Page identifier.  
`content` |  `string` Extractive segment content.  
  
## ExtractiveAnswer

Extractive answer. [Guide](https://cloud.google.com/generative-ai-app-builder/docs/snippets#get-answers)

JSON representation  
---  
      
    
    {
      "pageIdentifier": string,
      "content": string
    }  
  
Fields  
---  
`pageIdentifier` |  `string` Page identifier.  
`content` |  `string` Extractive answer content.  
  
## ChunkInfo

Chunk information.

JSON representation  
---  
      
    
    {
      "chunk": string,
      "content": string,
      "documentMetadata": {
        object ([DocumentMetadata](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#DocumentMetadata))
      }
    }  
  
Fields  
---  
`chunk` |  `string` Chunk resource name.  
`content` |  `string` Chunk textual content.  
`documentMetadata` |  `object (`[DocumentMetadata](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/SearchSpec#DocumentMetadata)`)` Metadata of the document from the current chunk.  
  
## DocumentMetadata

Document metadata contains the information of the document of the current chunk.

JSON representation  
---  
      
    
    {
      "uri": string,
      "title": string
    }  
  
Fields  
---  
`uri` |  `string` Uri of the document.  
`title` |  `string` Title of the document.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-03 UTC."],[],[]] 
