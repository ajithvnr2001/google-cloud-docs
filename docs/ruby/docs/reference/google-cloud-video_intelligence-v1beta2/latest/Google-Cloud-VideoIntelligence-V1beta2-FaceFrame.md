---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1beta2/latest/Google-Cloud-VideoIntelligence-V1beta2-FaceFrame/
title: Cloud Video Intelligence V1beta2 API - Class Google::Cloud::VideoIntelligence::V1beta2::FaceFrame (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:13.864643+00:00
---

# Cloud Video Intelligence V1beta2 API - Class Google::Cloud::VideoIntelligence::V1beta2::FaceFrame (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1beta2/latest/Google-Cloud-VideoIntelligence-V1beta2-FaceFrame/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Video Intelligence V1beta2 API - Class Google::Cloud::VideoIntelligence::V1beta2::FaceFrame (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.1  0.11.0  0.10.2  0.9.2  0.8.0  0.7.1  0.6.0  0.5.0  0.4.5 

Reference documentation and code samples for the Cloud Video Intelligence V1beta2 API class Google::Cloud::VideoIntelligence::V1beta2::FaceFrame.

Video frame level annotation results for face detection.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #normalized_bounding_boxes
    
    
    def normalized_bounding_boxes() -> ::Array<::Google::Cloud::VideoIntelligence::V1beta2::NormalizedBoundingBox>

**Returns**

  * (::Array<[::Google::Cloud::VideoIntelligence::V1beta2::NormalizedBoundingBox](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1beta2/latest/Google-Cloud-VideoIntelligence-V1beta2-NormalizedBoundingBox)>) — Normalized Bounding boxes in a frame. There can be more than one boxes if the same face is detected in multiple locations within the current frame. 



### #normalized_bounding_boxes=
    
    
    def normalized_bounding_boxes=(value) -> ::Array<::Google::Cloud::VideoIntelligence::V1beta2::NormalizedBoundingBox>

**Parameter**

  * **value** (::Array<[::Google::Cloud::VideoIntelligence::V1beta2::NormalizedBoundingBox](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1beta2/latest/Google-Cloud-VideoIntelligence-V1beta2-NormalizedBoundingBox)>) — Normalized Bounding boxes in a frame. There can be more than one boxes if the same face is detected in multiple locations within the current frame. 



**Returns**

  * (::Array<[::Google::Cloud::VideoIntelligence::V1beta2::NormalizedBoundingBox](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1beta2/latest/Google-Cloud-VideoIntelligence-V1beta2-NormalizedBoundingBox)>) — Normalized Bounding boxes in a frame. There can be more than one boxes if the same face is detected in multiple locations within the current frame. 



### #time_offset
    
    
    def time_offset() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1beta2/latest/Google-Protobuf-Duration)) — Time-offset, relative to the beginning of the video, corresponding to the video frame for this location. 



### #time_offset=
    
    
    def time_offset=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1beta2/latest/Google-Protobuf-Duration)) — Time-offset, relative to the beginning of the video, corresponding to the video frame for this location. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1beta2/latest/Google-Protobuf-Duration)) — Time-offset, relative to the beginning of the video, corresponding to the video frame for this location. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
