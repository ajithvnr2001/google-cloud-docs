---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/searchExamples/
title: Method: exampleStores.searchExamples \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:12:08.672694+00:00
---

# Method: exampleStores.searchExamples  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/searchExamples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: exampleStores.searchExamples Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.exampleStores.searchExamples

Search for similar Examples for given selection criteria.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{exampleStore}:searchExamples`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`exampleStore` `string` Required. The name of the ExampleStore resource that examples are retrieved from. Format: `projects/{project}/locations/{location}/exampleStores/{exampleStore}`

### Request body

The request body contains data with the following structure: | Fields  
  
`topK` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The number of similar examples to return. | `parameters` `Union type`  
  
The parameters to search for similar examples. This includes which value to use for similarity search and the filters that should be applied to the search. Filters limit which examples are considered as candidates for similarity search. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`storedContentsExampleParameters` `object (`[StoredContentsExampleParameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/searchExamples#StoredContentsExampleParameters)`)` The parameters of StoredContentsExamples to be searched. End of mutually exclusive fields.

### Response body

Response message for `[ExampleStoreService.SearchExamples](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/searchExamples#google.cloud.aiplatform.v1beta1.ExampleStoreService.SearchExamples)`. If successful, the response body contains data with the following structure: | Fields  
  
`results[]` `object (`[SimilarExample](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/searchExamples#SimilarExample)`)` The results of searching for similar examples. | JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([SimilarExample](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/searchExamples#SimilarExample))
        }
      ]
    }  
  
## StoredContentsExampleParameters

The metadata filters that will be used to search StoredContentsExamples. If a field is unspecified, then no filtering for that field will be applied

Fields  
  
`functionNames` `object (`[ExamplesArrayFilter](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExamplesArrayFilter)`)` Optional. The function names for filtering. | `query` `Union type`  
  
The query to use to retrieve similar StoredContentsExamples. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`searchKey` `string` The exact search key to use for retrieval. | `contentSearchKey` `object (`[ContentSearchKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/searchExamples#ContentSearchKey)`)` The chat history to use to generate the search key for retrieval. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "functionNames": {
        object ([ExamplesArrayFilter](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/ExamplesArrayFilter))
      },
    
      // query
      "searchKey": string,
      "contentSearchKey": {
        object ([ContentSearchKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.exampleStores/searchExamples#ContentSearchKey))
      }
      // Union type
    }  
  
## ContentSearchKey

The chat history to use to generate the search key for retrieval.

Fields  
  
`contents[]` `object (`[Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content)`)` Required. The conversation for generating a search key. | `searchKeyGenerationMethod` `object (`[SearchKeyGenerationMethod](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SearchKeyGenerationMethod)`)` Required. The method of generating a search key. | JSON representation  
---  
      
    
    {
      "contents": [
        {
          object ([Content](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/Content))
        }
      ],
      "searchKeyGenerationMethod": {
        object ([SearchKeyGenerationMethod](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/SearchKeyGenerationMethod))
      }
    }  
  
## SimilarExample

The result of the similar example.

Fields  
  
`example` `object (`[Example](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example)`)` The example that is similar to the searched query. | `similarityScore` `number` The similarity score of this example. | JSON representation  
---  
      
    
    {
      "example": {
        object ([Example](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/Example))
      },
      "similarityScore": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
