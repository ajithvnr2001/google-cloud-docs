---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-TextDetectionParams/
title: Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::TextDetectionParams (v0.16.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:50.029255+00:00
---

# Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::TextDetectionParams (v0.16.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-TextDetectionParams/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::TextDetectionParams (v0.16.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.1 (latest)  0.16.0  0.15.1  0.14.1  0.13.0  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Cloud Vision V1p4beta1 API class Google::Cloud::Vision::V1p4beta1::TextDetectionParams.

Parameters for text detections. This is used to control TEXT_DETECTION and DOCUMENT_TEXT_DETECTION features.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #advanced_ocr_options
    
    
    def advanced_ocr_options() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of advanced OCR options to fine-tune OCR behavior. 



### #advanced_ocr_options=
    
    
    def advanced_ocr_options=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of advanced OCR options to fine-tune OCR behavior. 



**Returns**

  * (::Array<::String>) — A list of advanced OCR options to fine-tune OCR behavior. 



### #enable_text_detection_confidence_score
    
    
    def enable_text_detection_confidence_score() -> ::Boolean

**Returns**

  * (::Boolean) — By default, Cloud Vision API only includes confidence score for DOCUMENT_TEXT_DETECTION result. Set the flag to true to include confidence score for TEXT_DETECTION as well. 



### #enable_text_detection_confidence_score=
    
    
    def enable_text_detection_confidence_score=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — By default, Cloud Vision API only includes confidence score for DOCUMENT_TEXT_DETECTION result. Set the flag to true to include confidence score for TEXT_DETECTION as well. 



**Returns**

  * (::Boolean) — By default, Cloud Vision API only includes confidence score for DOCUMENT_TEXT_DETECTION result. Set the flag to true to include confidence score for TEXT_DETECTION as well. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
