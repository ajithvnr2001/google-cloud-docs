---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextExtractionEvaluationMetrics/
title: TextExtractionEvaluationMetrics \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:16:13.253937+00:00
---

# TextExtractionEvaluationMetrics  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextExtractionEvaluationMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  TextExtractionEvaluationMetrics Stay organized with collections  Save and categorize content based on your preferences. 

Metrics for text extraction evaluation results.

Fields  
  
`confidenceMetrics[]` `object (`[ConfidenceMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextExtractionEvaluationMetrics#ConfidenceMetrics)`)` Metrics that have confidence thresholds. Precision-recall curve can be derived from them. | `confusionMatrix` `object (`[ConfusionMatrix](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ConfusionMatrix)`)` Confusion matrix of the evaluation. Only set for Models where number of AnnotationSpecs is no more than 10. Only set for ModelEvaluations, not for ModelEvaluationSlices. | JSON representation  
---  
      
    
    {
      "confidenceMetrics": [
        {
          object ([ConfidenceMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TextExtractionEvaluationMetrics#ConfidenceMetrics))
        }
      ],
      "confusionMatrix": {
        object ([ConfusionMatrix](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ConfusionMatrix))
      }
    }  
  
## ConfidenceMetrics

Fields  
  
`confidenceThreshold` `number` Metrics are computed with an assumption that the Model never returns predictions with score lower than this value. | `recall` `number` Recall (True Positive Rate) for the given confidence threshold. | `precision` `number` Precision for the given confidence threshold. | `f1Score` `number` The harmonic mean of recall and precision. | JSON representation  
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
