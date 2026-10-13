---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1p1beta1/latest/Google-Cloud-Speech-V1p1beta1-ListPhraseSetRequest/
title: Cloud Speech-to-Text V1p1beta1 API - Class Google::Cloud::Speech::V1p1beta1::ListPhraseSetRequest (v0.30.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:03.104394+00:00
---

# Cloud Speech-to-Text V1p1beta1 API - Class Google::Cloud::Speech::V1p1beta1::ListPhraseSetRequest (v0.30.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1p1beta1/latest/Google-Cloud-Speech-V1p1beta1-ListPhraseSetRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Speech-to-Text V1p1beta1 API - Class Google::Cloud::Speech::V1p1beta1::ListPhraseSetRequest (v0.30.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.1 (latest)  0.30.0  0.29.1  0.28.0  0.27.1  0.26.0  0.25.0  0.24.1  0.23.0  0.22.0  0.21.1  0.20.2  0.19.0  0.18.1  0.17.1  0.16.0  0.15.3  0.14.0  0.13.0  0.12.4 

Reference documentation and code samples for the Cloud Speech-to-Text V1p1beta1 API class Google::Cloud::Speech::V1p1beta1::ListPhraseSetRequest.

Message sent by the client for the `ListPhraseSet` method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #page_size
    
    
    def page_size() -> ::Integer

**Returns**

  * (::Integer) — The maximum number of phrase sets to return. The service may return fewer than this value. If unspecified, at most 50 phrase sets will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000\. 



### #page_size=
    
    
    def page_size=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The maximum number of phrase sets to return. The service may return fewer than this value. If unspecified, at most 50 phrase sets will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000\. 



**Returns**

  * (::Integer) — The maximum number of phrase sets to return. The service may return fewer than this value. If unspecified, at most 50 phrase sets will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000\. 



### #page_token
    
    
    def page_token() -> ::String

**Returns**

  * (::String) — A page token, received from a previous `ListPhraseSet` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListPhraseSet` must match the call that provided the page token. 




### #page_token=
    
    
    def page_token=(value) -> ::String

**Parameter**

  * **value** (::String) — A page token, received from a previous `ListPhraseSet` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListPhraseSet` must match the call that provided the page token. 




**Returns**

  * (::String) — A page token, received from a previous `ListPhraseSet` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListPhraseSet` must match the call that provided the page token. 




### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. The parent, which owns this collection of phrase set. Format:

`projects/{project}/locations/{location}`

Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. 




### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The parent, which owns this collection of phrase set. Format:

`projects/{project}/locations/{location}`

Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. 




**Returns**

  * (::String) — Required. The parent, which owns this collection of phrase set. Format:

`projects/{project}/locations/{location}`

Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
