---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagContexts/
title: RagContexts \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:32:23.747968+00:00
---

# RagContexts  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagContexts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  RagContexts Stay organized with collections  Save and categorize content based on your preferences. 

Relevant contexts for one query.

Fields  
  
`contexts[]` `object (`[Context](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagContexts#Context)`)` All its contexts. | JSON representation  
---  
      
    
    {
      "contexts": [
        {
          object ([Context](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagContexts#Context))
        }
      ]
    }  
  
## Context

A context of the query.

Fields  
  
`sourceUri` `string` If the file is imported from Cloud Storage or Google Drive, sourceUri will be original file URI in Cloud Storage or Google Drive; if file is uploaded, sourceUri will be file display name. | `sourceDisplayName` `string` The file display name. | `text` `string` The text chunk. | `distance  
**(deprecated)**` `number` This item is deprecated!The distance between the query dense embedding vector and the context text vector. | `sparseDistance  
**(deprecated)**` `number` This item is deprecated!The distance between the query sparse embedding vector and the context text vector. | `chunk` `object (`[RagChunk](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagChunk)`)` Context of the retrieved chunk. | `score` `number` According to the underlying Vector DB and the selected metric type, the score can be either the distance or the similarity between the query and the context and its range depends on the metric type.For example, if the metric type is COSINE_DISTANCE, it represents the distance between the query and the context. The larger the distance, the less relevant the context is to the query. The range is [0, 2], while 0 means the most relevant and 2 means the least relevant. | JSON representation  
---  
      
    
    {
      "sourceUri": string,
      "sourceDisplayName": string,
      "text": string,
      "distance": number,
      "sparseDistance": number,
      "chunk": {
        object ([RagChunk](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/RagChunk))
      },
      "score": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
