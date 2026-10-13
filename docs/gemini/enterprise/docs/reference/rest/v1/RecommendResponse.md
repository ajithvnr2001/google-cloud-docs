---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/RecommendResponse/
title: RecommendResponse \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:13.779769+00:00
---

# RecommendResponse  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/RecommendResponse/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  RecommendResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * RecommendationResult
    * JSON representation



Response message for Recommend method.

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([RecommendationResult](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/RecommendResponse#RecommendationResult))
        }
      ],
      "attributionToken": string,
      "missingIds": [
        string
      ],
      "validateOnly": boolean
    }  
  
Fields  
---  
`results[]` |  `object (`[RecommendationResult](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/RecommendResponse#RecommendationResult)`)` A list of recommended Documents. The order represents the ranking (from the most relevant Document to the least).  
`attributionToken` |  `string` A unique attribution token. This should be included in the `[UserEvent](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.userEvents#UserEvent)` logs resulting from this recommendation, which enables accurate attribution of recommendation model performance.  
`missingIds[]` |  `string` IDs of documents in the request that were missing from the default Branch associated with the requested ServingConfig.  
`validateOnly` |  `boolean` True if `[RecommendRequest.validate_only](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/recommend#body.request_body.FIELDS.validate_only)` was set.  
  
## RecommendationResult

RecommendationResult represents a generic recommendation result with associated metadata.

JSON representation  
---  
      
    
    {
      "id": string,
      "document": {
        object ([Document](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents#Document))
      },
      "metadata": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`id` |  `string` Resource ID of the recommended Document.  
`document` |  `object (`[Document](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents#Document)`)` Set if `returnDocument` is set to true in `[RecommendRequest.params](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/recommend#body.request_body.FIELDS.params)`.  
`metadata` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Additional Document metadata or annotations.Possible values:

  * `score`: Recommendation score in double value. Is set if `returnScore` is set to true in `[RecommendRequest.params](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.dataStores.servingConfigs/recommend#body.request_body.FIELDS.params)`.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-08 UTC."],[],[]] 
