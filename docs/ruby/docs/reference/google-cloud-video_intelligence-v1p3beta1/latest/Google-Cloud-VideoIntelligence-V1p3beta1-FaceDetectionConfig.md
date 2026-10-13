---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p3beta1/latest/Google-Cloud-VideoIntelligence-V1p3beta1-FaceDetectionConfig/
title: Cloud Video Intelligence V1p3beta1 API - Class Google::Cloud::VideoIntelligence::V1p3beta1::FaceDetectionConfig (v0.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:57.204555+00:00
---

# Cloud Video Intelligence V1p3beta1 API - Class Google::Cloud::VideoIntelligence::V1p3beta1::FaceDetectionConfig (v0.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1p3beta1/latest/Google-Cloud-VideoIntelligence-V1p3beta1-FaceDetectionConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Video Intelligence V1p3beta1 API - Class Google::Cloud::VideoIntelligence::V1p3beta1::FaceDetectionConfig (v0.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.1 (latest)  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.1  0.8.0  0.7.2  0.6.2  0.5.0  0.4.1  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Cloud Video Intelligence V1p3beta1 API class Google::Cloud::VideoIntelligence::V1p3beta1::FaceDetectionConfig.

Config for FACE_DETECTION.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #include_attributes
    
    
    def include_attributes() -> ::Boolean

**Returns**

  * (::Boolean) — Whether to enable face attributes detection, such as glasses, dark_glasses, mouth_open etc. Ignored if 'include_bounding_boxes' is set to false. 



### #include_attributes=
    
    
    def include_attributes=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether to enable face attributes detection, such as glasses, dark_glasses, mouth_open etc. Ignored if 'include_bounding_boxes' is set to false. 



**Returns**

  * (::Boolean) — Whether to enable face attributes detection, such as glasses, dark_glasses, mouth_open etc. Ignored if 'include_bounding_boxes' is set to false. 



### #include_bounding_boxes
    
    
    def include_bounding_boxes() -> ::Boolean

**Returns**

  * (::Boolean) — Whether bounding boxes are included in the face annotation output. 



### #include_bounding_boxes=
    
    
    def include_bounding_boxes=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether bounding boxes are included in the face annotation output. 



**Returns**

  * (::Boolean) — Whether bounding boxes are included in the face annotation output. 



### #model
    
    
    def model() -> ::String

**Returns**

  * (::String) — Model to use for face detection. Supported values: "builtin/stable" (the default if unset) and "builtin/latest". 



### #model=
    
    
    def model=(value) -> ::String

**Parameter**

  * **value** (::String) — Model to use for face detection. Supported values: "builtin/stable" (the default if unset) and "builtin/latest". 



**Returns**

  * (::String) — Model to use for face detection. Supported values: "builtin/stable" (the default if unset) and "builtin/latest". 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
