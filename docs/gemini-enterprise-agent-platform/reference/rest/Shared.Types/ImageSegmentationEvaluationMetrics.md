---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationEvaluationMetrics/
title: ImageSegmentationEvaluationMetrics \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:13:51.695267+00:00
---

# ImageSegmentationEvaluationMetrics  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationEvaluationMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  ImageSegmentationEvaluationMetrics Stay organized with collections  Save and categorize content based on your preferences. 

Metrics for image segmentation evaluation results.

Fields  
  
`confidenceMetricsEntries[]` `object (`[ConfidenceMetricsEntry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationEvaluationMetrics#ConfidenceMetricsEntry)`)` Metrics for each confidenceThreshold in 0.00,0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 Precision-recall curve can be derived from it. | JSON representation  
---  
      
    
    {
      "confidenceMetricsEntries": [
        {
          object ([ConfidenceMetricsEntry](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ImageSegmentationEvaluationMetrics#ConfidenceMetricsEntry))
        }
      ]
    }  
  
## ConfidenceMetricsEntry

Fields  
  
`confusionMatrix` `object (`[ConfusionMatrix](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ConfusionMatrix)`)` Confusion matrix for the given confidence threshold. | `confidenceThreshold` `number` Metrics are computed with an assumption that the model never returns predictions with score lower than this value. | `recall` `number` Recall (True Positive Rate) for the given confidence threshold. | `precision` `number` Precision for the given confidence threshold. | `diceScoreCoefficient` `number` DSC or the F1 score, The harmonic mean of recall and precision. | `iouScore` `number` The intersection-over-union score. The measure of overlap of the annotation's category mask with ground truth category mask on the DataItem. | JSON representation  
---  
      
    
    {
      "confusionMatrix": {
        object ([ConfusionMatrix](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/ConfusionMatrix))
      },
      "confidenceThreshold": number,
      "recall": number,
      "precision": number,
      "diceScoreCoefficient": number,
      "iouScore": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
