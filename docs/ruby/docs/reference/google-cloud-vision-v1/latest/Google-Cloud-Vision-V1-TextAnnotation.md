---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-TextAnnotation/
title: Cloud Vision V1 API - Class Google::Cloud::Vision::V1::TextAnnotation (v1.7.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:38.172342+00:00
---

# Cloud Vision V1 API - Class Google::Cloud::Vision::V1::TextAnnotation (v1.7.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-TextAnnotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Vision V1 API - Class Google::Cloud::Vision::V1::TextAnnotation (v1.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.1 (latest)  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.1  1.1.0  1.0.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.1  0.10.0  0.9.0  0.8.0  0.7.0  0.6.4 

Reference documentation and code samples for the Cloud Vision V1 API class Google::Cloud::Vision::V1::TextAnnotation.

TextAnnotation contains a structured representation of OCR extracted text. The hierarchy of an OCR extracted text structure is like this: TextAnnotation -> Page -> Block -> Paragraph -> Word -> Symbol Each structural component, starting from Page, may further have their own properties. Properties describe detected languages, breaks etc.. Please refer to the [TextAnnotation.TextProperty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-TextAnnotation-TextProperty "Google::Cloud::Vision::V1::TextAnnotation::TextProperty \(class\)") message definition below for more detail.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #pages
    
    
    def pages() -> ::Array<::Google::Cloud::Vision::V1::Page>

**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::Page](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-Page)>) — List of pages detected by OCR. 



### #pages=
    
    
    def pages=(value) -> ::Array<::Google::Cloud::Vision::V1::Page>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Vision::V1::Page](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-Page)>) — List of pages detected by OCR. 



**Returns**

  * (::Array<[::Google::Cloud::Vision::V1::Page](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-vision-v1/latest/Google-Cloud-Vision-V1-Page)>) — List of pages detected by OCR. 



### #text
    
    
    def text() -> ::String

**Returns**

  * (::String) — UTF-8 text detected on the pages. 



### #text=
    
    
    def text=(value) -> ::String

**Parameter**

  * **value** (::String) — UTF-8 text detected on the pages. 



**Returns**

  * (::String) — UTF-8 text detected on the pages. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
