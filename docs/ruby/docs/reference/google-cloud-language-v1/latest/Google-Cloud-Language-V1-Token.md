---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-Token/
title: Natural Language V1 API - Class Google::Cloud::Language::V1::Token (v1.7.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:53.418687+00:00
---

# Natural Language V1 API - Class Google::Cloud::Language::V1::Token (v1.7.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-Token/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Natural Language V1 API - Class Google::Cloud::Language::V1::Token (v1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.11.0  0.10.2  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.5 

Reference documentation and code samples for the Natural Language V1 API class Google::Cloud::Language::V1::Token.

Represents the smallest syntactic building block of the text.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #dependency_edge
    
    
    def dependency_edge() -> ::Google::Cloud::Language::V1::DependencyEdge

**Returns**

  * ([::Google::Cloud::Language::V1::DependencyEdge](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-DependencyEdge)) — Dependency tree parse for this token. 



### #dependency_edge=
    
    
    def dependency_edge=(value) -> ::Google::Cloud::Language::V1::DependencyEdge

**Parameter**

  * **value** ([::Google::Cloud::Language::V1::DependencyEdge](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-DependencyEdge)) — Dependency tree parse for this token. 



**Returns**

  * ([::Google::Cloud::Language::V1::DependencyEdge](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-DependencyEdge)) — Dependency tree parse for this token. 



### #lemma
    
    
    def lemma() -> ::String

**Returns**

  * (::String) — [Lemma](https://en.wikipedia.org/wiki/Lemma_%28morphology%29) of the token. 



### #lemma=
    
    
    def lemma=(value) -> ::String

**Parameter**

  * **value** (::String) — [Lemma](https://en.wikipedia.org/wiki/Lemma_%28morphology%29) of the token. 



**Returns**

  * (::String) — [Lemma](https://en.wikipedia.org/wiki/Lemma_%28morphology%29) of the token. 



### #part_of_speech
    
    
    def part_of_speech() -> ::Google::Cloud::Language::V1::PartOfSpeech

**Returns**

  * ([::Google::Cloud::Language::V1::PartOfSpeech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-PartOfSpeech)) — Parts of speech tag for this token. 



### #part_of_speech=
    
    
    def part_of_speech=(value) -> ::Google::Cloud::Language::V1::PartOfSpeech

**Parameter**

  * **value** ([::Google::Cloud::Language::V1::PartOfSpeech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-PartOfSpeech)) — Parts of speech tag for this token. 



**Returns**

  * ([::Google::Cloud::Language::V1::PartOfSpeech](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-PartOfSpeech)) — Parts of speech tag for this token. 



### #text
    
    
    def text() -> ::Google::Cloud::Language::V1::TextSpan

**Returns**

  * ([::Google::Cloud::Language::V1::TextSpan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-TextSpan)) — The token text. 



### #text=
    
    
    def text=(value) -> ::Google::Cloud::Language::V1::TextSpan

**Parameter**

  * **value** ([::Google::Cloud::Language::V1::TextSpan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-TextSpan)) — The token text. 



**Returns**

  * ([::Google::Cloud::Language::V1::TextSpan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-language-v1/latest/Google-Cloud-Language-V1-TextSpan)) — The token text. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
