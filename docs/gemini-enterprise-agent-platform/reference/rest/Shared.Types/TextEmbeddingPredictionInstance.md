---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextEmbeddingPredictionInstance/
title: TextEmbeddingPredictionInstance \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:32:40.181127+00:00
---

# TextEmbeddingPredictionInstance  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextEmbeddingPredictionInstance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  TextEmbeddingPredictionInstance Stay organized with collections  Save and categorize content based on your preferences. 

Prediction input format for Text Embedding. An embedding is a numerical representation (a vector of floating-point numbers) of text that captures its semantic meaning, enabling tasks like semantic search, classification, and clustering. LINT.IfChange

Fields  
  
`content` `string` The text passage to generate the embedding for. This can be a phrase, sentence, or document. | `title` `string` The title for the text passage in the `content` field. If you are embedding documents for the `RETRIEVAL_DOCUMENT` task type, providing a title can improve the quality of the embedding. | `taskType` `enum (`[TaskType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TaskType)`)` The task that the generated embeddings will be used for. The model uses this hint to generate embeddings that are optimized for your use case. If not set, the default task type is used. | JSON representation  
---  
      
    
    {
      "content": string,
      "title": string,
      "taskType": enum ([TaskType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TaskType))
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
