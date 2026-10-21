---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoObjectTrackingMetrics/
title: VideoObjectTrackingMetrics \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:18:27.895895+00:00
---

# VideoObjectTrackingMetrics  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoObjectTrackingMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VideoObjectTrackingMetrics Stay organized with collections  Save and categorize content based on your preferences. 

Model evaluation metrics for video object tracking problems. Evaluates prediction quality of both labeled bounding boxes and labeled tracks (i.e. series of bounding boxes sharing same label and instance id).

Fields  
  
`boundingBoxMetrics[]` `object (`[BoundingBoxMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/BoundingBoxMetrics)`)` The bounding boxes match metrics for each intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. | `trackMetrics[]` `object (`[TrackMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TrackMetrics)`)` UNIMPLEMENTED. The tracks match metrics for each intersection-over-union threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 and each label confidence threshold 0.05,0.10,...,0.95,0.96,0.97,0.98,0.99 pair. | `evaluatedFrameCount` `integer` UNIMPLEMENTED. The number of video frames used to create this evaluation. | `evaluatedBoundingBoxCount` `integer` UNIMPLEMENTED. The total number of bounding boxes (i.e. summed over all frames) the ground truth used to create this evaluation had. | `evaluatedTrackCount` `integer` UNIMPLEMENTED. The total number of tracks (i.e. as seen across all frames) the ground truth used to create this evaluation had. | `boundingBoxMeanAveragePrecision` `number` The single metric for bounding boxes evaluation: the `meanAveragePrecision` averaged over all `boundingBoxMetrics`. | `trackMeanAveragePrecision` `number` UNIMPLEMENTED. The single metric for tracks accuracy evaluation: the `meanAveragePrecision` averaged over all `trackMetrics`. | `trackMeanBoundingBoxIou` `number` UNIMPLEMENTED. The single metric for tracks bounding box iou evaluation: the `meanBoundingBoxIou` averaged over all `trackMetrics`. | `trackMeanMismatchRate` `number` UNIMPLEMENTED. The single metric for tracking consistency evaluation: the `meanMismatchRate` averaged over all `trackMetrics`. | JSON representation  
---  
      
    
    {
      "boundingBoxMetrics": [
        {
          object ([BoundingBoxMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/BoundingBoxMetrics))
        }
      ],
      "trackMetrics": [
        {
          object ([TrackMetrics](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/TrackMetrics))
        }
      ],
      "evaluatedFrameCount": integer,
      "evaluatedBoundingBoxCount": integer,
      "evaluatedTrackCount": integer,
      "boundingBoxMeanAveragePrecision": number,
      "trackMeanAveragePrecision": number,
      "trackMeanBoundingBoxIou": number,
      "trackMeanMismatchRate": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
