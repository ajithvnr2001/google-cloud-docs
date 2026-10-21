---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig.SemanticSimilarityMetricsConfig
title: EvaluationMetricsConfig.SemanticSimilarityMetricsConfig \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:07:29.760863+00:00
---

# EvaluationMetricsConfig.SemanticSimilarityMetricsConfig  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationMetricsConfig.SemanticSimilarityMetricsConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  EvaluationMetricsConfig.SemanticSimilarityMetricsConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Configuration for similarity metrics for the evaluation. To disable the metric, set the message but do not set the `enableSemanticSimilarityMetrics` field to true (or explicitly set it to false). To unset the configuration and fallback to the default behavior, omit the message entirely.

JSON representation  
---  
      
    
    {
      "enableSemanticSimilarityMetrics": boolean
    }  
  
Fields  
---  
`enableSemanticSimilarityMetrics` |  `boolean` Optional. Whether to calculate semantic similarity metrics for the evaluation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
