---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TrackMetrics/
title: TrackMetrics \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:54:07.764762+00:00
---

# TrackMetrics  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TrackMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  TrackMetrics Stay organized with collections  Save and categorize content based on your preferences. 

UNIMPLEMENTED. Track matching model metrics for a single track match threshold and multiple label match confidence thresholds.

Fields  
  
`confidenceMetrics[]` `object (`[ConfidenceMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TrackMetrics#ConfidenceMetrics)`)` Metrics for each label-match `confidenceThreshold` from 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99. Precision-recall curve is derived from them. | `iouThreshold` `number` The intersection-over-union threshold value between bounding boxes across frames used to compute this metric entry. | `meanTrackingAveragePrecision` `number` The mean average precision over all confidence thresholds. | `meanBoundingBoxIou` `number` The mean bounding box iou over all confidence thresholds. | `meanMismatchRate` `number` The mean mismatch rate over all confidence thresholds. | JSON representation  
---  
      
    
    {
      "confidenceMetrics": [
        {
          object ([ConfidenceMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TrackMetrics#ConfidenceMetrics))
        }
      ],
      "iouThreshold": number,
      "meanTrackingAveragePrecision": number,
      "meanBoundingBoxIou": number,
      "meanMismatchRate": number
    }  
  
## ConfidenceMetrics

Metrics for a single confidence threshold.

Fields  
  
`confidenceThreshold` `number` The confidence threshold value used to compute the metrics. | `trackingPrecision` `number` Tracking precision. | `trackingRecall` `number` Tracking recall. | `boundingBoxIou` `number` Bounding box intersection-over-union precision. Measures how well the bounding boxes overlap between each other (e.g. complete overlap or just barely above iouThreshold). | `mismatchRate` `number` Mismatch rate, which measures the tracking consistency, i.e. correctness of instance id continuity. | JSON representation  
---  
      
    
    {
      "confidenceThreshold": number,
      "trackingPrecision": number,
      "trackingRecall": number,
      "boundingBoxIou": number,
      "mismatchRate": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
