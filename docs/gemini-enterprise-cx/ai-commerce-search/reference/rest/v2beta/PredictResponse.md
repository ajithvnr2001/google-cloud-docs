---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/PredictResponse/
title: PredictResponse \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:54:35.307854+00:00
---

# PredictResponse  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/PredictResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  PredictResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * PredictionResult
    * JSON representation



Response message for predict method.

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([PredictionResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/PredictResponse#PredictionResult))
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
`results[]` |  `object (`[PredictionResult](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/PredictResponse#PredictionResult)`)` A list of recommended products. The order represents the ranking (from the most relevant product to the least).  
`attributionToken` |  `string` A unique attribution token. This should be included in the `[UserEvent](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs.userEvents#UserEvent)` logs resulting from this recommendation, which enables accurate attribution of recommendation model performance.  
`missingIds[]` |  `string` IDs of products in the request that were missing from the inventory.  
`validateOnly` |  `boolean` True if the validateOnly property was set in the request.  
  
## PredictionResult

PredictionResult represents the recommendation prediction results.

JSON representation  
---  
      
    
    {
      "id": string,
      "metadata": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`id` |  `string` ID of the recommended product  
`metadata` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Additional product metadata / annotations.Possible values:

  * `product`: JSON representation of the product. Is set if `returnProduct` is set to true in `PredictRequest.params`.
  * `score`: Prediction score in double value. Is set if `returnScore` is set to true in `PredictRequest.params`.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
