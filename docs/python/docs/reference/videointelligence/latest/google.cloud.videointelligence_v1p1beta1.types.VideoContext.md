---
url: https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.types.VideoContext
title: Class VideoContext (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:04.214115+00:00
---

# Class VideoContext (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.types.VideoContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class VideoContext (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.0  2.19.0  2.18.0  2.17.0  2.16.2  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.1  2.6.1  2.5.1  2.4.0  2.3.3  2.2.0  2.1.0  2.0.0  1.16.3  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0 
    
    
    VideoContext(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Video context and/or feature-specific parameters.

## Attributes  
  
---  
**Name** | **Description**  
`segments` |  `MutableSequence[[google.cloud.videointelligence_v1p1beta1.types.VideoSegment](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.types.VideoSegment)]`   
Video segments to annotate. The segments may overlap and are not required to be contiguous or span the whole video. If unspecified, each video is treated as a single segment.   
`label_detection_config` |  `[google.cloud.videointelligence_v1p1beta1.types.LabelDetectionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.types.LabelDetectionConfig)`   
Config for LABEL_DETECTION.   
`shot_change_detection_config` |  `[google.cloud.videointelligence_v1p1beta1.types.ShotChangeDetectionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.types.ShotChangeDetectionConfig)`   
Config for SHOT_CHANGE_DETECTION.   
`explicit_content_detection_config` |  `[google.cloud.videointelligence_v1p1beta1.types.ExplicitContentDetectionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.types.ExplicitContentDetectionConfig)`   
Config for EXPLICIT_CONTENT_DETECTION.   
`speech_transcription_config` |  `[google.cloud.videointelligence_v1p1beta1.types.SpeechTranscriptionConfig](https://docs.cloud.google.com/python/docs/reference/videointelligence/latest/google.cloud.videointelligence_v1p1beta1.types.SpeechTranscriptionConfig)`   
Config for SPEECH_TRANSCRIPTION.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
