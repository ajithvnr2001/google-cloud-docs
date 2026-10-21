---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagQuery/
title: RagQuery \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:47:10.836502+00:00
---

# RagQuery  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  RagQuery Stay organized with collections  Save and categorize content based on your preferences. 

A query to retrieve relevant contexts.

Fields  
  
`similarityTopK  
**(deprecated)**` `integer` This item is deprecated!Optional. The number of contexts to retrieve. | `ranking  
**(deprecated)**` `object (`[Ranking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagQuery#Ranking)`)` This item is deprecated!Optional. Configurations for hybrid search results ranking. | `ragRetrievalConfig` `object (`[RagRetrievalConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample#RagRetrievalConfig)`)` Optional. The retrieval config for the query. | `query` `Union type`  
  
The query to retrieve contexts. Currently only text query is supported. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`text` `string` Optional. The query in text format to get relevant contexts. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "similarityTopK": integer,
      "ranking": {
        object ([Ranking](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagQuery#Ranking))
      },
      "ragRetrievalConfig": {
        object ([RagRetrievalConfig](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/GeminiExample#RagRetrievalConfig))
      },
    
      // query
      "text": string
      // Union type
    }  
  
## Ranking

Configurations for hybrid search results ranking.

Fields  
  
`alpha` `number` Optional. Alpha value controls the weight between dense and sparse vector search results. The range is [0, 1], while 0 means sparse vector search only and 1 means dense vector search only. The default value is 0.5 which balances sparse and dense vector search equally. | JSON representation  
---  
      
    
    {
      "alpha": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
