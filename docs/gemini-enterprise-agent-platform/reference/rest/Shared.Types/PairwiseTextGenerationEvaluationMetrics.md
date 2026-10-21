---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/PairwiseTextGenerationEvaluationMetrics/
title: PairwiseTextGenerationEvaluationMetrics \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:26:04.011894+00:00
---

# PairwiseTextGenerationEvaluationMetrics  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/PairwiseTextGenerationEvaluationMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  PairwiseTextGenerationEvaluationMetrics Stay organized with collections  Save and categorize content based on your preferences. 

Metrics for general pairwise text generation evaluation results.

Fields  
  
`modelWinRate` `number` Percentage of time the autorater decided the model had the better response. | `baselineModelWinRate` `number` Percentage of time the autorater decided the baseline model had the better response. | `humanPreferenceModelWinRate` `number` Percentage of time humans decided the model had the better response. | `humanPreferenceBaselineModelWinRate` `number` Percentage of time humans decided the baseline model had the better response. | `truePositiveCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of examples where both the autorater and humans decided that the model had the better response. | `falsePositiveCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of examples where the autorater chose the model, but humans preferred the baseline model. | `falseNegativeCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of examples where the autorater chose the baseline model, but humans preferred the model. | `trueNegativeCount` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of examples where both the autorater and humans decided that the model had the worse response. | `accuracy` `number` Fraction of cases where the autorater agreed with the human raters. | `precision` `number` Fraction of cases where the autorater and humans thought the model had a better response out of all cases where the autorater thought the model had a better response. True positive divided by all positive. | `recall` `number` Fraction of cases where the autorater and humans thought the model had a better response out of all cases where the humans thought the model had a better response. | `f1Score` `number` Harmonic mean of precision and recall. | `cohensKappa` `number` A measurement of agreement between the autorater and human raters that takes the likelihood of random agreement into account. | JSON representation  
---  
      
    
    {
      "modelWinRate": number,
      "baselineModelWinRate": number,
      "humanPreferenceModelWinRate": number,
      "humanPreferenceBaselineModelWinRate": number,
      "truePositiveCount": string,
      "falsePositiveCount": string,
      "falseNegativeCount": string,
      "trueNegativeCount": string,
      "accuracy": number,
      "precision": number,
      "recall": number,
      "f1Score": number,
      "cohensKappa": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
