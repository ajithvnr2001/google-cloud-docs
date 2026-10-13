---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1/latest/Google-Cloud-VideoIntelligence-V1-TextSegment/
title: Cloud Video Intelligence V1 API - Class Google::Cloud::VideoIntelligence::V1::TextSegment (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:07:27.046414+00:00
---

# Cloud Video Intelligence V1 API - Class Google::Cloud::VideoIntelligence::V1::TextSegment (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1/latest/Google-Cloud-VideoIntelligence-V1-TextSegment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Video Intelligence V1 API - Class Google::Cloud::VideoIntelligence::V1::TextSegment (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.2  0.12.0  0.11.2  0.10.0  0.9.1  0.8.0  0.7.0  0.6.5 

Reference documentation and code samples for the Cloud Video Intelligence V1 API class Google::Cloud::VideoIntelligence::V1::TextSegment.

Video segment level annotation results for text detection.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #confidence
    
    
    def confidence() -> ::Float

**Returns**

  * (::Float) — Confidence for the track of detected text. It is calculated as the highest over all frames where OCR detected text appears. 



### #confidence=
    
    
    def confidence=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Confidence for the track of detected text. It is calculated as the highest over all frames where OCR detected text appears. 



**Returns**

  * (::Float) — Confidence for the track of detected text. It is calculated as the highest over all frames where OCR detected text appears. 



### #frames
    
    
    def frames() -> ::Array<::Google::Cloud::VideoIntelligence::V1::TextFrame>

**Returns**

  * (::Array<[::Google::Cloud::VideoIntelligence::V1::TextFrame](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1/latest/Google-Cloud-VideoIntelligence-V1-TextFrame)>) — Information related to the frames where OCR detected text appears. 



### #frames=
    
    
    def frames=(value) -> ::Array<::Google::Cloud::VideoIntelligence::V1::TextFrame>

**Parameter**

  * **value** (::Array<[::Google::Cloud::VideoIntelligence::V1::TextFrame](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1/latest/Google-Cloud-VideoIntelligence-V1-TextFrame)>) — Information related to the frames where OCR detected text appears. 



**Returns**

  * (::Array<[::Google::Cloud::VideoIntelligence::V1::TextFrame](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1/latest/Google-Cloud-VideoIntelligence-V1-TextFrame)>) — Information related to the frames where OCR detected text appears. 



### #segment
    
    
    def segment() -> ::Google::Cloud::VideoIntelligence::V1::VideoSegment

**Returns**

  * ([::Google::Cloud::VideoIntelligence::V1::VideoSegment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1/latest/Google-Cloud-VideoIntelligence-V1-VideoSegment)) — Video segment where a text snippet was detected. 



### #segment=
    
    
    def segment=(value) -> ::Google::Cloud::VideoIntelligence::V1::VideoSegment

**Parameter**

  * **value** ([::Google::Cloud::VideoIntelligence::V1::VideoSegment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1/latest/Google-Cloud-VideoIntelligence-V1-VideoSegment)) — Video segment where a text snippet was detected. 



**Returns**

  * ([::Google::Cloud::VideoIntelligence::V1::VideoSegment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video_intelligence-v1/latest/Google-Cloud-VideoIntelligence-V1-VideoSegment)) — Video segment where a text snippet was detected. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
