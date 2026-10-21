---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextEmbedding/
title: TextEmbedding \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:36:10.645570+00:00
---

# TextEmbedding  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextEmbedding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  TextEmbedding Stay organized with collections  Save and categorize content based on your preferences. 

An embedding is a vector (list) of floating-point numbers that represents the semantic meaning of text. Embeddings can be used to compare text for similarity, classify text, or cluster text. Text with similar meaning will have similar embedding vectors.

Fields  
  
`values[]` `number` The embedding vector. The size of the vector is fixed and determined by the model used for embedding generation. | `statistics` `object (`[Statistics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextEmbedding#Statistics)`)` Statistics about the input text. | JSON representation  
---  
      
    
    {
      "values": [
        number
      ],
      "statistics": {
        object ([Statistics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextEmbedding#Statistics))
      }
    }  
  
## Statistics

Statistics about the input text.

Fields  
  
`tokenCount` `integer` The number of tokens in the input text. | `truncated` `boolean` Whether the input text was truncated. If true, the embedding was generated from a truncated version of the input text. This can happen if the input text was longer than the model's input token limit. | JSON representation  
---  
      
    
    {
      "tokenCount": integer,
      "truncated": boolean
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
