---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnalyzeContentRequest/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::AnalyzeContentRequest (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:01.636371+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::AnalyzeContentRequest (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AnalyzeContentRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::AnalyzeContentRequest (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::AnalyzeContentRequest.

The request message for [Participants.AnalyzeContent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Participants-Client#Google__Cloud__Dialogflow__V2__Participants__Client_analyze_content_instance_ "Google::Cloud::Dialogflow::V2::Participants::Client#analyze_content \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #assist_query_params
    
    
    def assist_query_params() -> ::Google::Cloud::Dialogflow::V2::AssistQueryParameters

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::AssistQueryParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AssistQueryParameters)) — Parameters for a human assist query. 



### #assist_query_params=
    
    
    def assist_query_params=(value) -> ::Google::Cloud::Dialogflow::V2::AssistQueryParameters

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::V2::AssistQueryParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AssistQueryParameters)) — Parameters for a human assist query. 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::AssistQueryParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AssistQueryParameters)) — Parameters for a human assist query. 



### #audio_input
    
    
    def audio_input() -> ::Google::Cloud::Dialogflow::V2::AudioInput

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::AudioInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AudioInput)) — The natural language speech audio to be processed.

Note: The following fields are mutually exclusive: `audio_input`, `text_input`, `event_input`, `suggestion_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #audio_input=
    
    
    def audio_input=(value) -> ::Google::Cloud::Dialogflow::V2::AudioInput

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::V2::AudioInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AudioInput)) — The natural language speech audio to be processed.

Note: The following fields are mutually exclusive: `audio_input`, `text_input`, `event_input`, `suggestion_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::V2::AudioInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AudioInput)) — The natural language speech audio to be processed.

Note: The following fields are mutually exclusive: `audio_input`, `text_input`, `event_input`, `suggestion_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cx_parameters
    
    
    def cx_parameters() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — Additional parameters to be put into Dialogflow CX session parameters. To remove a parameter from the session, clients should explicitly set the parameter value to null.

Note: this field should only be used if you are connecting to a Dialogflow CX agent. 




### #cx_parameters=
    
    
    def cx_parameters=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — Additional parameters to be put into Dialogflow CX session parameters. To remove a parameter from the session, clients should explicitly set the parameter value to null.

Note: this field should only be used if you are connecting to a Dialogflow CX agent. 




**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — Additional parameters to be put into Dialogflow CX session parameters. To remove a parameter from the session, clients should explicitly set the parameter value to null.

Note: this field should only be used if you are connecting to a Dialogflow CX agent. 




### #event_input
    
    
    def event_input() -> ::Google::Cloud::Dialogflow::V2::EventInput

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::EventInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-EventInput)) — An input event to send to Dialogflow.

Note: The following fields are mutually exclusive: `event_input`, `text_input`, `audio_input`, `suggestion_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #event_input=
    
    
    def event_input=(value) -> ::Google::Cloud::Dialogflow::V2::EventInput

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::V2::EventInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-EventInput)) — An input event to send to Dialogflow.

Note: The following fields are mutually exclusive: `event_input`, `text_input`, `audio_input`, `suggestion_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::V2::EventInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-EventInput)) — An input event to send to Dialogflow.

Note: The following fields are mutually exclusive: `event_input`, `text_input`, `audio_input`, `suggestion_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #participant
    
    
    def participant() -> ::String

**Returns**

  * (::String) — Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 



### #participant=
    
    
    def participant=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 



**Returns**

  * (::String) — Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. 



### #query_params
    
    
    def query_params() -> ::Google::Cloud::Dialogflow::V2::QueryParameters

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::QueryParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-QueryParameters)) — Parameters for a Dialogflow virtual-agent query. 



### #query_params=
    
    
    def query_params=(value) -> ::Google::Cloud::Dialogflow::V2::QueryParameters

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::V2::QueryParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-QueryParameters)) — Parameters for a Dialogflow virtual-agent query. 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::QueryParameters](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-QueryParameters)) — Parameters for a Dialogflow virtual-agent query. 



### #reply_audio_config
    
    
    def reply_audio_config() -> ::Google::Cloud::Dialogflow::V2::OutputAudioConfig

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::OutputAudioConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-OutputAudioConfig)) — Speech synthesis configuration. The speech synthesis settings for a virtual agent that may be configured for the associated conversation profile are not used when calling AnalyzeContent. If this configuration is not supplied, speech synthesis is disabled. 



### #reply_audio_config=
    
    
    def reply_audio_config=(value) -> ::Google::Cloud::Dialogflow::V2::OutputAudioConfig

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::V2::OutputAudioConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-OutputAudioConfig)) — Speech synthesis configuration. The speech synthesis settings for a virtual agent that may be configured for the associated conversation profile are not used when calling AnalyzeContent. If this configuration is not supplied, speech synthesis is disabled. 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::OutputAudioConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-OutputAudioConfig)) — Speech synthesis configuration. The speech synthesis settings for a virtual agent that may be configured for the associated conversation profile are not used when calling AnalyzeContent. If this configuration is not supplied, speech synthesis is disabled. 



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if a `request_id` is provided. 



### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if a `request_id` is provided. 



**Returns**

  * (::String) — A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if a `request_id` is provided. 



### #suggestion_input
    
    
    def suggestion_input() -> ::Google::Cloud::Dialogflow::V2::SuggestionInput

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::SuggestionInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestionInput)) — An input representing the selection of a suggestion.

Note: The following fields are mutually exclusive: `suggestion_input`, `text_input`, `audio_input`, `event_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #suggestion_input=
    
    
    def suggestion_input=(value) -> ::Google::Cloud::Dialogflow::V2::SuggestionInput

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::V2::SuggestionInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestionInput)) — An input representing the selection of a suggestion.

Note: The following fields are mutually exclusive: `suggestion_input`, `text_input`, `audio_input`, `event_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::V2::SuggestionInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SuggestionInput)) — An input representing the selection of a suggestion.

Note: The following fields are mutually exclusive: `suggestion_input`, `text_input`, `audio_input`, `event_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text_input
    
    
    def text_input() -> ::Google::Cloud::Dialogflow::V2::TextInput

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-TextInput)) — The natural language text to be processed.

Note: The following fields are mutually exclusive: `text_input`, `audio_input`, `event_input`, `suggestion_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #text_input=
    
    
    def text_input=(value) -> ::Google::Cloud::Dialogflow::V2::TextInput

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::V2::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-TextInput)) — The natural language text to be processed.

Note: The following fields are mutually exclusive: `text_input`, `audio_input`, `event_input`, `suggestion_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::V2::TextInput](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-TextInput)) — The natural language text to be processed.

Note: The following fields are mutually exclusive: `text_input`, `audio_input`, `event_input`, `suggestion_input`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
