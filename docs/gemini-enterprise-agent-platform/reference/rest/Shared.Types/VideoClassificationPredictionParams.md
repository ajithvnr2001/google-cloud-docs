---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoClassificationPredictionParams/
title: VideoClassificationPredictionParams \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:36:41.458369+00:00
---

# VideoClassificationPredictionParams  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoClassificationPredictionParams/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VideoClassificationPredictionParams Stay organized with collections  Save and categorize content based on your preferences. 

Prediction model parameters for Video Classification.

Fields  
  
`confidenceThreshold` `number` The Model only returns predictions with at least this confidence score. Default value is 0.0 | `maxPredictions` `integer` The Model only returns up to that many top, by confidence score, predictions per instance. If this number is very high, the Model may return fewer predictions. Default value is 10,000. | `segmentClassification` `boolean` Set to true to request segment-level classification. Agent Platform returns labels and their confidence scores for the entire time segment of the video that user specified in the input instance. Default value is true | `shotClassification` `boolean` Set to true to request shot-level classification. Agent Platform determines the boundaries for each camera shot in the entire time segment of the video that user specified in the input instance. Agent Platform then returns labels and their confidence scores for each detected shot, along with the start and end time of the shot. WARNING: Model evaluation is not done for this classification type, the quality of it depends on the training data, but there are no metrics provided to describe that quality. Default value is false | `oneSecIntervalClassification` `boolean` Set to true to request classification for a video at one-second intervals. Agent Platform returns labels and their confidence scores for each second of the entire time segment of the video that user specified in the input WARNING: Model evaluation is not done for this classification type, the quality of it depends on the training data, but there are no metrics provided to describe that quality. Default value is false | JSON representation  
---  
      
    
    {
      "confidenceThreshold": number,
      "maxPredictions": integer,
      "segmentClassification": boolean,
      "shotClassification": boolean,
      "oneSecIntervalClassification": boolean
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
