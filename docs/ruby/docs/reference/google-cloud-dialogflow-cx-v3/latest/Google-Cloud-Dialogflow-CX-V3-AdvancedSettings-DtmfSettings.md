---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings-DtmfSettings/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::AdvancedSettings::DtmfSettings (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:51.986396+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::AdvancedSettings::DtmfSettings (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AdvancedSettings-DtmfSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::AdvancedSettings::DtmfSettings (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::AdvancedSettings::DtmfSettings.

Define behaviors for DTMF (dual tone multi frequency).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #enabled
    
    
    def enabled() -> ::Boolean

**Returns**

  * (::Boolean) — If true, incoming audio is processed for DTMF (dual tone multi frequency) events. For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a "3" was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance). 



### #enabled=
    
    
    def enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If true, incoming audio is processed for DTMF (dual tone multi frequency) events. For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a "3" was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance). 



**Returns**

  * (::Boolean) — If true, incoming audio is processed for DTMF (dual tone multi frequency) events. For example, if the caller presses a button on their telephone keypad and DTMF processing is enabled, Dialogflow will detect the event (e.g. a "3" was pressed) in the incoming audio and pass the event to the bot to drive business logic (e.g. when 3 is pressed, return the account balance). 



### #endpointing_timeout_duration
    
    
    def endpointing_timeout_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Endpoint timeout setting for matching dtmf input to regex. 



### #endpointing_timeout_duration=
    
    
    def endpointing_timeout_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Endpoint timeout setting for matching dtmf input to regex. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Endpoint timeout setting for matching dtmf input to regex. 



### #finish_digit
    
    
    def finish_digit() -> ::String

**Returns**

  * (::String) — The digit that terminates a DTMF digit sequence. 



### #finish_digit=
    
    
    def finish_digit=(value) -> ::String

**Parameter**

  * **value** (::String) — The digit that terminates a DTMF digit sequence. 



**Returns**

  * (::String) — The digit that terminates a DTMF digit sequence. 



### #interdigit_timeout_duration
    
    
    def interdigit_timeout_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Interdigit timeout setting for matching dtmf input to regex. 



### #interdigit_timeout_duration=
    
    
    def interdigit_timeout_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Interdigit timeout setting for matching dtmf input to regex. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Protobuf-Duration)) — Interdigit timeout setting for matching dtmf input to regex. 



### #max_digits
    
    
    def max_digits() -> ::Integer

**Returns**

  * (::Integer) — Max length of DTMF digits. 



### #max_digits=
    
    
    def max_digits=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Max length of DTMF digits. 



**Returns**

  * (::Integer) — Max length of DTMF digits. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
