---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoObjectTrackingAnnotation/
title: VideoObjectTrackingAnnotation \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:31:49.355925+00:00
---

# VideoObjectTrackingAnnotation  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/VideoObjectTrackingAnnotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  VideoObjectTrackingAnnotation Stay organized with collections  Save and categorize content based on your preferences. 

Annotation details specific to video object tracking.

Fields  
  
`timeOffset` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` A time (frame) of a video to which this annotation pertains. Represented as the duration since the video's start.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. | `xMin` `number` The leftmost coordinate of the bounding box. | `xMax` `number` The rightmost coordinate of the bounding box. | `yMin` `number` The topmost coordinate of the bounding box. | `yMax` `number` The bottommost coordinate of the bounding box. | `instanceId` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The instance of the object, expressed as a positive integer. Used to track the same object across different frames. | `annotationSpecId` `string` The resource id of the AnnotationSpec that this Annotation pertains to. | `displayName` `string` The display name of the AnnotationSpec that this Annotation pertains to. | JSON representation  
---  
      
    
    {
      "timeOffset": string,
      "xMin": number,
      "xMax": number,
      "yMin": number,
      "yMax": number,
      "instanceId": string,
      "annotationSpecId": string,
      "displayName": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-12 UTC."],[],[]] 
