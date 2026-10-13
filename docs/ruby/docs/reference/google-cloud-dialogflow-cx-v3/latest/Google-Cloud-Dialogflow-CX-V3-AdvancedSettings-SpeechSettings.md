---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings-SpeechSettings/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::AdvancedSettings::SpeechSettings (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:52.386274+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::AdvancedSettings::SpeechSettings (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings-SpeechSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::AdvancedSettings::SpeechSettings (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::AdvancedSettings::SpeechSettings.

Define behaviors of speech to text detection.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #endpointer_sensitivity
    
    
    def endpointer_sensitivity() -> ::Integer

**Returns**

  * (::Integer) — Sensitivity of the speech model that detects the end of speech. Scale from 0 to 100. 



### #endpointer_sensitivity=
    
    
    def endpointer_sensitivity=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Sensitivity of the speech model that detects the end of speech. Scale from 0 to 100. 



**Returns**

  * (::Integer) — Sensitivity of the speech model that detects the end of speech. Scale from 0 to 100. 



### #models
    
    
    def models() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Mapping from language to Speech-to-Text model. The mapped Speech-to-Text model will be selected for requests from its corresponding language. For more information, see [Speech models](https://cloud.google.com/dialogflow/cx/docs/concept/speech-models). 



### #models=
    
    
    def models=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Mapping from language to Speech-to-Text model. The mapped Speech-to-Text model will be selected for requests from its corresponding language. For more information, see [Speech models](https://cloud.google.com/dialogflow/cx/docs/concept/speech-models). 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Mapping from language to Speech-to-Text model. The mapped Speech-to-Text model will be selected for requests from its corresponding language. For more information, see [Speech models](https://cloud.google.com/dialogflow/cx/docs/concept/speech-models). 



### #no_speech_timeout
    
    
    def no_speech_timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Timeout before detecting no speech. 



### #no_speech_timeout=
    
    
    def no_speech_timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Timeout before detecting no speech. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Timeout before detecting no speech. 



### #use_timeout_based_endpointing
    
    
    def use_timeout_based_endpointing() -> ::Boolean

**Returns**

  * (::Boolean) — Use timeout based endpointing, interpreting endpointer sensitivity as seconds of timeout value. 



### #use_timeout_based_endpointing=
    
    
    def use_timeout_based_endpointing=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Use timeout based endpointing, interpreting endpointer sensitivity as seconds of timeout value. 



**Returns**

  * (::Boolean) — Use timeout based endpointing, interpreting endpointer sensitivity as seconds of timeout value. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
