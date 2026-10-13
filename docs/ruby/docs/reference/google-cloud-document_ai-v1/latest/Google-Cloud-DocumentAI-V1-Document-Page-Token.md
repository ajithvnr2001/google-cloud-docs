---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token/
title: Document AI V1 API - Class Google::Cloud::DocumentAI::V1::Document::Page::Token (v1.13.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:26.076308+00:00
---

# Document AI V1 API - Class Google::Cloud::DocumentAI::V1::Document::Page::Token (v1.13.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Document AI V1 API - Class Google::Cloud::DocumentAI::V1::Document::Page::Token (v1.13.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.1 (latest)  1.13.0  1.12.1  1.11.0  1.10.2  1.9.0  1.8.0  1.7.0  1.6.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.23.1  0.22.0  0.21.1  0.20.0  0.19.0  0.18.0  0.17.2  0.16.2  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.4 

Reference documentation and code samples for the Document AI V1 API class Google::Cloud::DocumentAI::V1::Document::Page::Token.

A detected token.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #detected_break
    
    
    def detected_break() -> ::Google::Cloud::DocumentAI::V1::Document::Page::Token::DetectedBreak

**Returns**

  * ([::Google::Cloud::DocumentAI::V1::Document::Page::Token::DetectedBreak](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token-DetectedBreak)) — Detected break at the end of a [Token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token "Google::Cloud::DocumentAI::V1::Document::Page::Token \(class\)"). 



### #detected_break=
    
    
    def detected_break=(value) -> ::Google::Cloud::DocumentAI::V1::Document::Page::Token::DetectedBreak

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1::Document::Page::Token::DetectedBreak](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token-DetectedBreak)) — Detected break at the end of a [Token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token "Google::Cloud::DocumentAI::V1::Document::Page::Token \(class\)"). 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1::Document::Page::Token::DetectedBreak](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token-DetectedBreak)) — Detected break at the end of a [Token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token "Google::Cloud::DocumentAI::V1::Document::Page::Token \(class\)"). 



### #detected_languages
    
    
    def detected_languages() -> ::Array<::Google::Cloud::DocumentAI::V1::Document::Page::DetectedLanguage>

**Returns**

  * (::Array<[::Google::Cloud::DocumentAI::V1::Document::Page::DetectedLanguage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-DetectedLanguage)>) — A list of detected languages together with confidence. 



### #detected_languages=
    
    
    def detected_languages=(value) -> ::Array<::Google::Cloud::DocumentAI::V1::Document::Page::DetectedLanguage>

**Parameter**

  * **value** (::Array<[::Google::Cloud::DocumentAI::V1::Document::Page::DetectedLanguage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-DetectedLanguage)>) — A list of detected languages together with confidence. 



**Returns**

  * (::Array<[::Google::Cloud::DocumentAI::V1::Document::Page::DetectedLanguage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-DetectedLanguage)>) — A list of detected languages together with confidence. 



### #layout
    
    
    def layout() -> ::Google::Cloud::DocumentAI::V1::Document::Page::Layout

**Returns**

  * ([::Google::Cloud::DocumentAI::V1::Document::Page::Layout](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Layout)) — [Layout](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Layout "Google::Cloud::DocumentAI::V1::Document::Page::Layout \(class\)") for [Token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token "Google::Cloud::DocumentAI::V1::Document::Page::Token \(class\)"). 



### #layout=
    
    
    def layout=(value) -> ::Google::Cloud::DocumentAI::V1::Document::Page::Layout

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1::Document::Page::Layout](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Layout)) — [Layout](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Layout "Google::Cloud::DocumentAI::V1::Document::Page::Layout \(class\)") for [Token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token "Google::Cloud::DocumentAI::V1::Document::Page::Token \(class\)"). 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1::Document::Page::Layout](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Layout)) — [Layout](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Layout "Google::Cloud::DocumentAI::V1::Document::Page::Layout \(class\)") for [Token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token "Google::Cloud::DocumentAI::V1::Document::Page::Token \(class\)"). 



### #provenance
    
    
    def provenance() -> ::Google::Cloud::DocumentAI::V1::Document::Provenance

**Returns**

  * ([::Google::Cloud::DocumentAI::V1::Document::Provenance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Provenance)) — The history of this annotation. 



### #provenance=
    
    
    def provenance=(value) -> ::Google::Cloud::DocumentAI::V1::Document::Provenance

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1::Document::Provenance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Provenance)) — The history of this annotation. 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1::Document::Provenance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Provenance)) — The history of this annotation. 



### #style_info
    
    
    def style_info() -> ::Google::Cloud::DocumentAI::V1::Document::Page::Token::StyleInfo

**Returns**

  * ([::Google::Cloud::DocumentAI::V1::Document::Page::Token::StyleInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token-StyleInfo)) — Text style attributes. 



### #style_info=
    
    
    def style_info=(value) -> ::Google::Cloud::DocumentAI::V1::Document::Page::Token::StyleInfo

**Parameter**

  * **value** ([::Google::Cloud::DocumentAI::V1::Document::Page::Token::StyleInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token-StyleInfo)) — Text style attributes. 



**Returns**

  * ([::Google::Cloud::DocumentAI::V1::Document::Page::Token::StyleInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-document_ai-v1/latest/Google-Cloud-DocumentAI-V1-Document-Page-Token-StyleInfo)) — Text style attributes. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
