---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1/latest/Google-Cloud-Speech-V1-UpdatePhraseSetRequest/
title: Cloud Speech-to-Text V1 API - Class Google::Cloud::Speech::V1::UpdatePhraseSetRequest (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:40:10.487477+00:00
---

# Cloud Speech-to-Text V1 API - Class Google::Cloud::Speech::V1::UpdatePhraseSetRequest (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1/latest/Google-Cloud-Speech-V1-UpdatePhraseSetRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Speech-to-Text V1 API - Class Google::Cloud::Speech::V1::UpdatePhraseSetRequest (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.17.0  0.16.2  0.15.0  0.14.0  0.13.1  0.12.1  0.11.0  0.10.2  0.9.0  0.8.0  0.7.3 

Reference documentation and code samples for the Cloud Speech-to-Text V1 API class Google::Cloud::Speech::V1::UpdatePhraseSetRequest.

Message sent by the client for the `UpdatePhraseSet` method.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #phrase_set
    
    
    def phrase_set() -> ::Google::Cloud::Speech::V1::PhraseSet

**Returns**

  * ([::Google::Cloud::Speech::V1::PhraseSet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1/latest/Google-Cloud-Speech-V1-PhraseSet)) — Required. The phrase set to update.

The phrase set's `name` field is used to identify the set to be updated. Format:

`projects/{project}/locations/{location}/phraseSets/{phrase_set}`

Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. 




### #phrase_set=
    
    
    def phrase_set=(value) -> ::Google::Cloud::Speech::V1::PhraseSet

**Parameter**

  * **value** ([::Google::Cloud::Speech::V1::PhraseSet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1/latest/Google-Cloud-Speech-V1-PhraseSet)) — Required. The phrase set to update.

The phrase set's `name` field is used to identify the set to be updated. Format:

`projects/{project}/locations/{location}/phraseSets/{phrase_set}`

Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. 




**Returns**

  * ([::Google::Cloud::Speech::V1::PhraseSet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1/latest/Google-Cloud-Speech-V1-PhraseSet)) — Required. The phrase set to update.

The phrase set's `name` field is used to identify the set to be updated. Format:

`projects/{project}/locations/{location}/phraseSets/{phrase_set}`

Speech-to-Text supports three locations: `global`, `us` (US North America), and `eu` (Europe). If you are calling the `speech.googleapis.com` endpoint, use the `global` location. To specify a region, use a [regional endpoint](https://cloud.google.com/speech-to-text/docs/endpoints) with matching `us` or `eu` location value. 




### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1/latest/Google-Protobuf-FieldMask)) — The list of fields to be updated. 



### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1/latest/Google-Protobuf-FieldMask)) — The list of fields to be updated. 



**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1/latest/Google-Protobuf-FieldMask)) — The list of fields to be updated. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
