---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-CropHint/
title: Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::CropHint (v0.16.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:49:54.295425+00:00
---

# Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::CropHint (v0.16.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-CropHint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1p4beta1 API - Class Google::Cloud::Vision::V1p4beta1::CropHint (v0.16.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.16.1 (latest)  0.16.0  0.15.1  0.14.1  0.13.0  0.12.1  0.11.1  0.10.0  0.9.0  0.8.1  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Cloud Vision V1p4beta1 API class Google::Cloud::Vision::V1p4beta1::CropHint.

Single crop hint that is used to generate a new crop when serving an image.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #bounding_poly
    
    
    def bounding_poly() -> ::Google::Cloud::Vision::V1p4beta1::BoundingPoly

**Returns**

  * ([::Google::Cloud::Vision::V1p4beta1::BoundingPoly](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-BoundingPoly)) — The bounding polygon for the crop region. The coordinates of the bounding box are in the original image's scale. 



### #bounding_poly=
    
    
    def bounding_poly=(value) -> ::Google::Cloud::Vision::V1p4beta1::BoundingPoly

**Parameter**

  * **value** ([::Google::Cloud::Vision::V1p4beta1::BoundingPoly](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-BoundingPoly)) — The bounding polygon for the crop region. The coordinates of the bounding box are in the original image's scale. 



**Returns**

  * ([::Google::Cloud::Vision::V1p4beta1::BoundingPoly](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p4beta1/latest/Google-Cloud-Vision-V1p4beta1-BoundingPoly)) — The bounding polygon for the crop region. The coordinates of the bounding box are in the original image's scale. 



### #confidence
    
    
    def confidence() -> ::Float

**Returns**

  * (::Float) — Confidence of this being a salient region. Range [0, 1]. 



### #confidence=
    
    
    def confidence=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Confidence of this being a salient region. Range [0, 1]. 



**Returns**

  * (::Float) — Confidence of this being a salient region. Range [0, 1]. 



### #importance_fraction
    
    
    def importance_fraction() -> ::Float

**Returns**

  * (::Float) — Fraction of importance of this salient region with respect to the original image. 



### #importance_fraction=
    
    
    def importance_fraction=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Fraction of importance of this salient region with respect to the original image. 



**Returns**

  * (::Float) — Fraction of importance of this salient region with respect to the original image. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
