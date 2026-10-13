---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-VideoActionRecognitionPredictionResult/
title: Vision AI V1 API - Class Google::Cloud::VisionAI::V1::VideoActionRecognitionPredictionResult (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:02.554009+00:00
---

# Vision AI V1 API - Class Google::Cloud::VisionAI::V1::VideoActionRecognitionPredictionResult (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-VideoActionRecognitionPredictionResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vision AI V1 API - Class Google::Cloud::VisionAI::V1::VideoActionRecognitionPredictionResult (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.1  1.2.0  1.1.1  1.0.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vision AI V1 API class Google::Cloud::VisionAI::V1::VideoActionRecognitionPredictionResult.

Prediction output format for Video Action Recognition.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #actions
    
    
    def actions() -> ::Array<::Google::Cloud::VisionAI::V1::VideoActionRecognitionPredictionResult::IdentifiedAction>

**Returns**

  * (::Array<[::Google::Cloud::VisionAI::V1::VideoActionRecognitionPredictionResult::IdentifiedAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-VideoActionRecognitionPredictionResult-IdentifiedAction)>) — All of the actions identified in the time range. 



### #actions=
    
    
    def actions=(value) -> ::Array<::Google::Cloud::VisionAI::V1::VideoActionRecognitionPredictionResult::IdentifiedAction>

**Parameter**

  * **value** (::Array<[::Google::Cloud::VisionAI::V1::VideoActionRecognitionPredictionResult::IdentifiedAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-VideoActionRecognitionPredictionResult-IdentifiedAction)>) — All of the actions identified in the time range. 



**Returns**

  * (::Array<[::Google::Cloud::VisionAI::V1::VideoActionRecognitionPredictionResult::IdentifiedAction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Cloud-VisionAI-V1-VideoActionRecognitionPredictionResult-IdentifiedAction)>) — All of the actions identified in the time range. 



### #segment_end_time
    
    
    def segment_end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Protobuf-Timestamp)) — The end, inclusive, of the video's time segment in which the actions have been identified. Particularly, if the end is the same as the start, it means the identification happens on a specific video frame. 



### #segment_end_time=
    
    
    def segment_end_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Protobuf-Timestamp)) — The end, inclusive, of the video's time segment in which the actions have been identified. Particularly, if the end is the same as the start, it means the identification happens on a specific video frame. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Protobuf-Timestamp)) — The end, inclusive, of the video's time segment in which the actions have been identified. Particularly, if the end is the same as the start, it means the identification happens on a specific video frame. 



### #segment_start_time
    
    
    def segment_start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Protobuf-Timestamp)) — The beginning, inclusive, of the video's time segment in which the actions have been identified. 



### #segment_start_time=
    
    
    def segment_start_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Protobuf-Timestamp)) — The beginning, inclusive, of the video's time segment in which the actions have been identified. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision_ai-v1/latest/Google-Protobuf-Timestamp)) — The beginning, inclusive, of the video's time segment in which the actions have been identified. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
