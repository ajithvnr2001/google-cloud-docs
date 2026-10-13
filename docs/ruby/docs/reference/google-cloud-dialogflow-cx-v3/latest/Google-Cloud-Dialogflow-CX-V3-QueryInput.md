---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-QueryInput/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::QueryInput (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:20:22.968171+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::QueryInput (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-QueryInput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::QueryInput (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::QueryInput.

Represents the query input. It can contain one of:

  1. A conversational query in the form of text.

  2. An intent query that specifies which intent to trigger.

  3. Natural language speech audio to be processed.

  4. An event to be triggered.

  5. DTMF digits to invoke an intent and fill in parameter value.

  6. The results of a tool executed by the client.




## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #audio
    
    
    def audio() -> ::Google::Cloud::Dialogflow::CX::V3::AudioInput

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::AudioInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AudioInput)) — The natural language speech audio to be processed.

Note: The following fields are mutually exclusive: `audio`, `text`, `intent`, `event`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #audio=
    
    
    def audio=(value) -> ::Google::Cloud::Dialogflow::CX::V3::AudioInput

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::AudioInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AudioInput)) — The natural language speech audio to be processed.

Note: The following fields are mutually exclusive: `audio`, `text`, `intent`, `event`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::AudioInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AudioInput)) — The natural language speech audio to be processed.

Note: The following fields are mutually exclusive: `audio`, `text`, `intent`, `event`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dtmf
    
    
    def dtmf() -> ::Google::Cloud::Dialogflow::CX::V3::DtmfInput

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::DtmfInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DtmfInput)) — The DTMF event to be handled.

Note: The following fields are mutually exclusive: `dtmf`, `text`, `intent`, `audio`, `event`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #dtmf=
    
    
    def dtmf=(value) -> ::Google::Cloud::Dialogflow::CX::V3::DtmfInput

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::DtmfInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DtmfInput)) — The DTMF event to be handled.

Note: The following fields are mutually exclusive: `dtmf`, `text`, `intent`, `audio`, `event`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::DtmfInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DtmfInput)) — The DTMF event to be handled.

Note: The following fields are mutually exclusive: `dtmf`, `text`, `intent`, `audio`, `event`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #event
    
    
    def event() -> ::Google::Cloud::Dialogflow::CX::V3::EventInput

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::EventInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-EventInput)) — The event to be triggered.

Note: The following fields are mutually exclusive: `event`, `text`, `intent`, `audio`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #event=
    
    
    def event=(value) -> ::Google::Cloud::Dialogflow::CX::V3::EventInput

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::EventInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-EventInput)) — The event to be triggered.

Note: The following fields are mutually exclusive: `event`, `text`, `intent`, `audio`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::EventInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-EventInput)) — The event to be triggered.

Note: The following fields are mutually exclusive: `event`, `text`, `intent`, `audio`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #intent
    
    
    def intent() -> ::Google::Cloud::Dialogflow::CX::V3::IntentInput

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::IntentInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-IntentInput)) — The intent to be triggered.

Note: The following fields are mutually exclusive: `intent`, `text`, `audio`, `event`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #intent=
    
    
    def intent=(value) -> ::Google::Cloud::Dialogflow::CX::V3::IntentInput

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::IntentInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-IntentInput)) — The intent to be triggered.

Note: The following fields are mutually exclusive: `intent`, `text`, `audio`, `event`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::IntentInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-IntentInput)) — The intent to be triggered.

Note: The following fields are mutually exclusive: `intent`, `text`, `audio`, `event`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #language_code
    
    
    def language_code() -> ::String

**Returns**

  * (::String) — Required. The language of the input. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. Note that queries in the same session do not necessarily need to specify the same language. 



### #language_code=
    
    
    def language_code=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The language of the input. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. Note that queries in the same session do not necessarily need to specify the same language. 



**Returns**

  * (::String) — Required. The language of the input. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. Note that queries in the same session do not necessarily need to specify the same language. 



### #text
    
    
    def text() -> ::Google::Cloud::Dialogflow::CX::V3::TextInput

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TextInput)) — The natural language text to be processed.

Note: The following fields are mutually exclusive: `text`, `intent`, `audio`, `event`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text=
    
    
    def text=(value) -> ::Google::Cloud::Dialogflow::CX::V3::TextInput

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TextInput)) — The natural language text to be processed.

Note: The following fields are mutually exclusive: `text`, `intent`, `audio`, `event`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-TextInput)) — The natural language text to be processed.

Note: The following fields are mutually exclusive: `text`, `intent`, `audio`, `event`, `dtmf`, `tool_call_result`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #tool_call_result
    
    
    def tool_call_result() -> ::Google::Cloud::Dialogflow::CX::V3::ToolCallResult

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::ToolCallResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ToolCallResult)) — The results of a tool executed by the client.

Note: The following fields are mutually exclusive: `tool_call_result`, `text`, `intent`, `audio`, `event`, `dtmf`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #tool_call_result=
    
    
    def tool_call_result=(value) -> ::Google::Cloud::Dialogflow::CX::V3::ToolCallResult

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::ToolCallResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ToolCallResult)) — The results of a tool executed by the client.

Note: The following fields are mutually exclusive: `tool_call_result`, `text`, `intent`, `audio`, `event`, `dtmf`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::ToolCallResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ToolCallResult)) — The results of a tool executed by the client.

Note: The following fields are mutually exclusive: `tool_call_result`, `text`, `intent`, `audio`, `event`, `dtmf`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
