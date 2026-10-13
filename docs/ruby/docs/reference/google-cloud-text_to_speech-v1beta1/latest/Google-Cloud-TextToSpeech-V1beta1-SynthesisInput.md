---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1beta1/latest/Google-Cloud-TextToSpeech-V1beta1-SynthesisInput/
title: Cloud Text-to-Speech V1beta1 API - Class Google::Cloud::TextToSpeech::V1beta1::SynthesisInput (v0.31.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:01:39.377602+00:00
---

# Cloud Text-to-Speech V1beta1 API - Class Google::Cloud::TextToSpeech::V1beta1::SynthesisInput (v0.31.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1beta1/latest/Google-Cloud-TextToSpeech-V1beta1-SynthesisInput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Text-to-Speech V1beta1 API - Class Google::Cloud::TextToSpeech::V1beta1::SynthesisInput (v0.31.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.31.1 (latest)  0.31.0  0.30.0  0.29.0  0.28.0  0.27.1  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.1  0.19.0  0.18.0  0.17.0  0.16.0  0.15.2  0.14.0  0.13.2  0.12.1  0.11.1  0.10.1  0.9.1  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Text-to-Speech V1beta1 API class Google::Cloud::TextToSpeech::V1beta1::SynthesisInput.

Contains text input to be synthesized. Either `text` or `ssml` must be supplied. Supplying both or neither returns [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]. The input size is limited to 5000 bytes.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #custom_pronunciations
    
    
    def custom_pronunciations() -> ::Google::Cloud::TextToSpeech::V1beta1::CustomPronunciations

**Returns**

  * ([::Google::Cloud::TextToSpeech::V1beta1::CustomPronunciations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1beta1/latest/Google-Cloud-TextToSpeech-V1beta1-CustomPronunciations)) — Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations.

The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported.

In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag. 




### #custom_pronunciations=
    
    
    def custom_pronunciations=(value) -> ::Google::Cloud::TextToSpeech::V1beta1::CustomPronunciations

**Parameter**

  * **value** ([::Google::Cloud::TextToSpeech::V1beta1::CustomPronunciations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1beta1/latest/Google-Cloud-TextToSpeech-V1beta1-CustomPronunciations)) — Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations.

The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported.

In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag. 




**Returns**

  * ([::Google::Cloud::TextToSpeech::V1beta1::CustomPronunciations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1beta1/latest/Google-Cloud-TextToSpeech-V1beta1-CustomPronunciations)) — Optional. The pronunciation customizations are applied to the input. If this is set, the input is synthesized using the given pronunciation customizations.

The initial support is for en-us, with plans to expand to other locales in the future. Instant Clone voices aren't supported.

In order to customize the pronunciation of a phrase, there must be an exact match of the phrase in the input types. If using SSML, the phrase must not be inside a phoneme tag. 




### #markup
    
    
    def markup() -> ::String

**Returns**

  * (::String) — Markup for Chirp 3: HD voices specifically. This field may not be used with any other voices.

Note: The following fields are mutually exclusive: `markup`, `text`, `ssml`, `multi_speaker_markup`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #markup=
    
    
    def markup=(value) -> ::String

**Parameter**

  * **value** (::String) — Markup for Chirp 3: HD voices specifically. This field may not be used with any other voices.

Note: The following fields are mutually exclusive: `markup`, `text`, `ssml`, `multi_speaker_markup`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — Markup for Chirp 3: HD voices specifically. This field may not be used with any other voices.

Note: The following fields are mutually exclusive: `markup`, `text`, `ssml`, `multi_speaker_markup`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #multi_speaker_markup
    
    
    def multi_speaker_markup() -> ::Google::Cloud::TextToSpeech::V1beta1::MultiSpeakerMarkup

**Returns**

  * ([::Google::Cloud::TextToSpeech::V1beta1::MultiSpeakerMarkup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1beta1/latest/Google-Cloud-TextToSpeech-V1beta1-MultiSpeakerMarkup)) — The multi-speaker input to be synthesized. Only applicable for multi-speaker synthesis.

Note: The following fields are mutually exclusive: `multi_speaker_markup`, `text`, `markup`, `ssml`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #multi_speaker_markup=
    
    
    def multi_speaker_markup=(value) -> ::Google::Cloud::TextToSpeech::V1beta1::MultiSpeakerMarkup

**Parameter**

  * **value** ([::Google::Cloud::TextToSpeech::V1beta1::MultiSpeakerMarkup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1beta1/latest/Google-Cloud-TextToSpeech-V1beta1-MultiSpeakerMarkup)) — The multi-speaker input to be synthesized. Only applicable for multi-speaker synthesis.

Note: The following fields are mutually exclusive: `multi_speaker_markup`, `text`, `markup`, `ssml`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::TextToSpeech::V1beta1::MultiSpeakerMarkup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-text_to_speech-v1beta1/latest/Google-Cloud-TextToSpeech-V1beta1-MultiSpeakerMarkup)) — The multi-speaker input to be synthesized. Only applicable for multi-speaker synthesis.

Note: The following fields are mutually exclusive: `multi_speaker_markup`, `text`, `markup`, `ssml`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #prompt
    
    
    def prompt() -> ::String

**Returns**

  * (::String) — This system instruction is supported only for controllable/promptable voice models. If this system instruction is used, we pass the unedited text to Gemini-TTS. Otherwise, a default system instruction is used. AI Studio calls this system instruction, Style Instructions. 



### #prompt=
    
    
    def prompt=(value) -> ::String

**Parameter**

  * **value** (::String) — This system instruction is supported only for controllable/promptable voice models. If this system instruction is used, we pass the unedited text to Gemini-TTS. Otherwise, a default system instruction is used. AI Studio calls this system instruction, Style Instructions. 



**Returns**

  * (::String) — This system instruction is supported only for controllable/promptable voice models. If this system instruction is used, we pass the unedited text to Gemini-TTS. Otherwise, a default system instruction is used. AI Studio calls this system instruction, Style Instructions. 



### #ssml
    
    
    def ssml() -> ::String

**Returns**

  * (::String) — The SSML document to be synthesized. The SSML document must be valid and well-formed. Otherwise the RPC will fail and return [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]. For more information, see [SSML](https://cloud.google.com/text-to-speech/docs/ssml).

Note: The following fields are mutually exclusive: `ssml`, `text`, `markup`, `multi_speaker_markup`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #ssml=
    
    
    def ssml=(value) -> ::String

**Parameter**

  * **value** (::String) — The SSML document to be synthesized. The SSML document must be valid and well-formed. Otherwise the RPC will fail and return [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]. For more information, see [SSML](https://cloud.google.com/text-to-speech/docs/ssml).

Note: The following fields are mutually exclusive: `ssml`, `text`, `markup`, `multi_speaker_markup`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The SSML document to be synthesized. The SSML document must be valid and well-formed. Otherwise the RPC will fail and return [google.rpc.Code.INVALID_ARGUMENT][google.rpc.Code.INVALID_ARGUMENT]. For more information, see [SSML](https://cloud.google.com/text-to-speech/docs/ssml).

Note: The following fields are mutually exclusive: `ssml`, `text`, `markup`, `multi_speaker_markup`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text
    
    
    def text() -> ::String

**Returns**

  * (::String) — The raw text to be synthesized.

Note: The following fields are mutually exclusive: `text`, `markup`, `ssml`, `multi_speaker_markup`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text=
    
    
    def text=(value) -> ::String

**Parameter**

  * **value** (::String) — The raw text to be synthesized.

Note: The following fields are mutually exclusive: `text`, `markup`, `ssml`, `multi_speaker_markup`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The raw text to be synthesized.

Note: The following fields are mutually exclusive: `text`, `markup`, `ssml`, `multi_speaker_markup`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
