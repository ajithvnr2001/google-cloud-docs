---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/BoundingBoxMetrics/
title: BoundingBoxMetrics \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:32:51.057716+00:00
---

# BoundingBoxMetrics  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/BoundingBoxMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  BoundingBoxMetrics Stay organized with collections  Save and categorize content based on your preferences. 

Bounding box matching model metrics for a single intersection-over-union threshold and multiple label match confidence thresholds.

Fields  
  
`confidenceMetrics[]` `object (`[ConfidenceMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/BoundingBoxMetrics#ConfidenceMetrics)`)` Metrics for each label-match confidenceThreshold from 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. Precision-recall curve is derived from them. | `iouThreshold` `number` The intersection-over-union threshold value used to compute this metrics entry. | `meanAveragePrecision` `number` The mean average precision, most often close to `auPrc`. | JSON representation  
---  
      
    
    {
      "confidenceMetrics": [
        {
          object ([ConfidenceMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/BoundingBoxMetrics#ConfidenceMetrics))
        }
      ],
      "iouThreshold": number,
      "meanAveragePrecision": number
    }  
  
## ConfidenceMetrics

Metrics for a single confidence threshold.

Fields  
  
`confidenceThreshold` `number` The confidence threshold value used to compute the metrics. | `recall` `number` Recall under the given confidence threshold. | `precision` `number` Precision under the given confidence threshold. | `f1Score` `number` The harmonic mean of recall and precision. | JSON representation  
---  
      
    
    {
      "confidenceThreshold": number,
      "recall": number,
      "precision": number,
      "f1Score": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
