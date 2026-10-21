---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextEmbeddingPredictionParams/
title: TextEmbeddingPredictionParams \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:31:35.865739+00:00
---

# TextEmbeddingPredictionParams  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextEmbeddingPredictionParams/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  TextEmbeddingPredictionParams Stay organized with collections  Save and categorize content based on your preferences. 

Prediction model parameters for Text Embedding. Text embeddings are numerical representations of text that capture semantic meaning, used for tasks like semantic search, classification, and clustering.

Fields  
  
`autoTruncate` `boolean` Optional. Whether to silently truncate inputs longer than the maximum input token limit. This behavior is enabled by default. If this option is set to false, inputs longer than the limit will cause an INVALID_ARGUMENT error. | `outputDimensionality` `integer` Parameter to reduce the dimensionality of the output embedding. Some models support this feature, which can reduce storage and computation costs. If you specify this parameter, you must use a value supported by the model. If the model does not support it, or if you specify an unsupported dimension, the request will fail with an `INVALID_ARGUMENT` error. | JSON representation  
---  
      
    
    {
      "autoTruncate": boolean,
      "outputDimensionality": integer
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
