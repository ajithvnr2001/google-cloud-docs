---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoActionMetrics/
title: VideoActionMetrics \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:13:13.756498+00:00
---

# VideoActionMetrics  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoActionMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VideoActionMetrics Stay organized with collections  Save and categorize content based on your preferences. 

The Evaluation metrics given a specific `[precisionWindowLength](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoActionMetrics#FIELDS.precision_window_length)`.

Fields  
  
`confidenceMetrics[]` `object (`[ConfidenceMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoActionMetrics#ConfidenceMetrics)`)` Metrics for each label-match confidenceThreshold from 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. | `precisionWindowLength` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` This `[VideoActionMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoActionMetrics)` is calculated based on this prediction window length. If the predicted action's timestamp is inside the time window whose center is the ground truth action's timestamp with this specific length, the prediction result is treated as a true positive.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `meanAveragePrecision` `number` The mean average precision. | JSON representation  
---  
      
    
    {
      "confidenceMetrics": [
        {
          object ([ConfidenceMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoActionMetrics#ConfidenceMetrics))
        }
      ],
      "precisionWindowLength": string,
      "meanAveragePrecision": number
    }  
  
## ConfidenceMetrics

Metrics for a single confidence threshold.

Fields  
  
`confidenceThreshold` `number` Output only. The confidence threshold value used to compute the metrics. | `recall` `number` Output only. Recall for the given confidence threshold. | `precision` `number` Output only. Precision for the given confidence threshold. | `f1Score` `number` Output only. The harmonic mean of recall and precision. | JSON representation  
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
