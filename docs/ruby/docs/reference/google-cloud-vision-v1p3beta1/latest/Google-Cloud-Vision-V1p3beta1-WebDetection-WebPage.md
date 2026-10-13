---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-WebDetection-WebPage/
title: Cloud Vision V1p3beta1 API - Class Google::Cloud::Vision::V1p3beta1::WebDetection::WebPage (v0.20.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:25.872509+00:00
---

# Cloud Vision V1p3beta1 API - Class Google::Cloud::Vision::V1p3beta1::WebDetection::WebPage (v0.20.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-WebDetection-WebPage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1p3beta1 API - Class Google::Cloud::Vision::V1p3beta1::WebDetection::WebPage (v0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.20.0  0.19.1  0.18.1  0.17.0  0.16.0  0.15.1  0.14.0  0.13.1  0.12.2  0.11.0  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.5 

Reference documentation and code samples for the Cloud Vision V1p3beta1 API class Google::Cloud::Vision::V1p3beta1::WebDetection::WebPage.

Metadata for web pages.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #full_matching_images
    
    
    def full_matching_images() -> ::Array<::Google::Cloud::Vision::V1p3beta1::WebDetection::WebImage>

**Returns**

  * (::Array<[::Google::Cloud::Vision::V1p3beta1::WebDetection::WebImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-WebDetection-WebImage)>) — Fully matching images on the page. Can include resized copies of the query image. 



### #full_matching_images=
    
    
    def full_matching_images=(value) -> ::Array<::Google::Cloud::Vision::V1p3beta1::WebDetection::WebImage>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Vision::V1p3beta1::WebDetection::WebImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-WebDetection-WebImage)>) — Fully matching images on the page. Can include resized copies of the query image. 



**Returns**

  * (::Array<[::Google::Cloud::Vision::V1p3beta1::WebDetection::WebImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-WebDetection-WebImage)>) — Fully matching images on the page. Can include resized copies of the query image. 



### #page_title
    
    
    def page_title() -> ::String

**Returns**

  * (::String) — Title for the web page, may contain HTML markups. 



### #page_title=
    
    
    def page_title=(value) -> ::String

**Parameter**

  * **value** (::String) — Title for the web page, may contain HTML markups. 



**Returns**

  * (::String) — Title for the web page, may contain HTML markups. 



### #partial_matching_images
    
    
    def partial_matching_images() -> ::Array<::Google::Cloud::Vision::V1p3beta1::WebDetection::WebImage>

**Returns**

  * (::Array<[::Google::Cloud::Vision::V1p3beta1::WebDetection::WebImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-WebDetection-WebImage)>) — Partial matching images on the page. Those images are similar enough to share some key-point features. For example an original image will likely have partial matching for its crops. 



### #partial_matching_images=
    
    
    def partial_matching_images=(value) -> ::Array<::Google::Cloud::Vision::V1p3beta1::WebDetection::WebImage>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Vision::V1p3beta1::WebDetection::WebImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-WebDetection-WebImage)>) — Partial matching images on the page. Those images are similar enough to share some key-point features. For example an original image will likely have partial matching for its crops. 



**Returns**

  * (::Array<[::Google::Cloud::Vision::V1p3beta1::WebDetection::WebImage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1p3beta1/latest/Google-Cloud-Vision-V1p3beta1-WebDetection-WebImage)>) — Partial matching images on the page. Those images are similar enough to share some key-point features. For example an original image will likely have partial matching for its crops. 



### #score
    
    
    def score() -> ::Float

**Returns**

  * (::Float) — (Deprecated) Overall relevancy score for the web page. 



### #score=
    
    
    def score=(value) -> ::Float

**Parameter**

  * **value** (::Float) — (Deprecated) Overall relevancy score for the web page. 



**Returns**

  * (::Float) — (Deprecated) Overall relevancy score for the web page. 



### #url
    
    
    def url() -> ::String

**Returns**

  * (::String) — The result web page URL. 



### #url=
    
    
    def url=(value) -> ::String

**Parameter**

  * **value** (::String) — The result web page URL. 



**Returns**

  * (::String) — The result web page URL. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
