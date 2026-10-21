---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoObjectTrackingPredictionResult/
title: VideoObjectTrackingPredictionResult \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:10:16.731842+00:00
---

# VideoObjectTrackingPredictionResult  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoObjectTrackingPredictionResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VideoObjectTrackingPredictionResult Stay organized with collections  Save and categorize content based on your preferences. 

Prediction output format for Video Object Tracking.

Fields  
  
`id` `string` The resource id of the AnnotationSpec that had been identified. | `displayName` `string` The display name of the AnnotationSpec that had been identified. | `timeSegmentStart` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The beginning, inclusive, of the video's time segment in which the object instance has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with "s" appended at the end.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `timeSegmentEnd` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The end, inclusive, of the video's time segment in which the object instance has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with "s" appended at the end.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `confidence` `number` The Model's confidence in correction of this prediction, higher value means higher confidence. | `frames[]` `object (`[Frame](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoObjectTrackingPredictionResult#Frame)`)` All of the frames of the video in which a single object instance has been detected. The bounding boxes in the frames identify the same object. | JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "timeSegmentStart": string,
      "timeSegmentEnd": string,
      "confidence": number,
      "frames": [
        {
          object ([Frame](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoObjectTrackingPredictionResult#Frame))
        }
      ]
    }  
  
## Frame

The fields `xMin`, `xMax`, `yMin`, and `yMax` refer to a bounding box, i.e. the rectangle over the video frame pinpointing the found AnnotationSpec. The coordinates are relative to the frame size, and the point 0,0 is in the top left of the frame.

Fields  
  
`timeOffset` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` A time (frame) of a video in which the object has been detected. Expressed as a number of seconds as measured from the start of the video, with fractions up to a microsecond precision, and with "s" appended at the end.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `xMin` `number` The leftmost coordinate of the bounding box. | `xMax` `number` The rightmost coordinate of the bounding box. | `yMin` `number` The topmost coordinate of the bounding box. | `yMax` `number` The bottommost coordinate of the bounding box. | JSON representation  
---  
      
    
    {
      "timeOffset": string,
      "xMin": number,
      "xMax": number,
      "yMin": number,
      "yMax": number
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
