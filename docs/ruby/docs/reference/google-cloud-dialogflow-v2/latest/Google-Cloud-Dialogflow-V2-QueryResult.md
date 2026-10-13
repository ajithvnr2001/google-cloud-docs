---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-QueryResult/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::QueryResult (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:21.671048+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::QueryResult (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-QueryResult/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::QueryResult (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::QueryResult.

Represents the result of conversational query or event processing.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #action
    
    
    def action() -> ::String

**Returns**

  * (::String) — The action name from the matched intent. 



### #action=
    
    
    def action=(value) -> ::String

**Parameter**

  * **value** (::String) — The action name from the matched intent. 



**Returns**

  * (::String) — The action name from the matched intent. 



### #all_required_params_present
    
    
    def all_required_params_present() -> ::Boolean

**Returns**

  * (::Boolean) — 

This field is set to:

    * `false` if the matched intent has required parameters and not all of the required parameter values have been collected.
    * `true` if all required parameter values have been collected, or if the matched intent doesn't contain any required parameters.



### #all_required_params_present=
    
    
    def all_required_params_present=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — 

This field is set to:

    * `false` if the matched intent has required parameters and not all of the required parameter values have been collected.
    * `true` if all required parameter values have been collected, or if the matched intent doesn't contain any required parameters.



**Returns**

  * (::Boolean) — 

This field is set to:

    * `false` if the matched intent has required parameters and not all of the required parameter values have been collected.
    * `true` if all required parameter values have been collected, or if the matched intent doesn't contain any required parameters.



### #cancels_slot_filling
    
    
    def cancels_slot_filling() -> ::Boolean

**Returns**

  * (::Boolean) — Indicates whether the conversational query triggers a cancellation for slot filling. For more information, see the [cancel slot filling documentation](https://cloud.google.com/dialogflow/es/docs/intents-actions-parameters#cancel). 



### #cancels_slot_filling=
    
    
    def cancels_slot_filling=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Indicates whether the conversational query triggers a cancellation for slot filling. For more information, see the [cancel slot filling documentation](https://cloud.google.com/dialogflow/es/docs/intents-actions-parameters#cancel). 



**Returns**

  * (::Boolean) — Indicates whether the conversational query triggers a cancellation for slot filling. For more information, see the [cancel slot filling documentation](https://cloud.google.com/dialogflow/es/docs/intents-actions-parameters#cancel). 



### #diagnostic_info
    
    
    def diagnostic_info() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — 

Free-form diagnostic information for the associated detect intent request. The fields of this data can change without notice, so you should not write code that depends on its structure. The data may contain:

    * webhook call latency
    * webhook errors



### #diagnostic_info=
    
    
    def diagnostic_info=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — 

Free-form diagnostic information for the associated detect intent request. The fields of this data can change without notice, so you should not write code that depends on its structure. The data may contain:

    * webhook call latency
    * webhook errors



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — 

Free-form diagnostic information for the associated detect intent request. The fields of this data can change without notice, so you should not write code that depends on its structure. The data may contain:

    * webhook call latency
    * webhook errors



### #fulfillment_messages
    
    
    def fulfillment_messages() -> ::Array<::Google::Cloud::Dialogflow::V2::Intent::Message>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::V2::Intent::Message](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Intent-Message)>) — The collection of rich messages to present to the user. 



### #fulfillment_messages=
    
    
    def fulfillment_messages=(value) -> ::Array<::Google::Cloud::Dialogflow::V2::Intent::Message>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dialogflow::V2::Intent::Message](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Intent-Message)>) — The collection of rich messages to present to the user. 



**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::V2::Intent::Message](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Intent-Message)>) — The collection of rich messages to present to the user. 



### #fulfillment_text
    
    
    def fulfillment_text() -> ::String

**Returns**

  * (::String) — The text to be pronounced to the user or shown on the screen. Note: This is a legacy field, `fulfillment_messages` should be preferred. 



### #fulfillment_text=
    
    
    def fulfillment_text=(value) -> ::String

**Parameter**

  * **value** (::String) — The text to be pronounced to the user or shown on the screen. Note: This is a legacy field, `fulfillment_messages` should be preferred. 



**Returns**

  * (::String) — The text to be pronounced to the user or shown on the screen. Note: This is a legacy field, `fulfillment_messages` should be preferred. 



### #intent
    
    
    def intent() -> ::Google::Cloud::Dialogflow::V2::Intent

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::Intent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Intent)) — The intent that matched the conversational query. Some, not all fields are filled in this message, including but not limited to: `name`, `display_name`, `end_interaction` and `is_fallback`. 



### #intent=
    
    
    def intent=(value) -> ::Google::Cloud::Dialogflow::V2::Intent

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::V2::Intent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Intent)) — The intent that matched the conversational query. Some, not all fields are filled in this message, including but not limited to: `name`, `display_name`, `end_interaction` and `is_fallback`. 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::Intent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Intent)) — The intent that matched the conversational query. Some, not all fields are filled in this message, including but not limited to: `name`, `display_name`, `end_interaction` and `is_fallback`. 



### #intent_detection_confidence
    
    
    def intent_detection_confidence() -> ::Float

**Returns**

  * (::Float) — The intent detection confidence. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation. If there are `multiple knowledge_answers` messages, this value is set to the greatest `knowledgeAnswers.match_confidence` value in the list. 



### #intent_detection_confidence=
    
    
    def intent_detection_confidence=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The intent detection confidence. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation. If there are `multiple knowledge_answers` messages, this value is set to the greatest `knowledgeAnswers.match_confidence` value in the list. 



**Returns**

  * (::Float) — The intent detection confidence. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation. If there are `multiple knowledge_answers` messages, this value is set to the greatest `knowledgeAnswers.match_confidence` value in the list. 



### #language_code
    
    
    def language_code() -> ::String

**Returns**

  * (::String) — The language that was triggered during intent detection. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes. 



### #language_code=
    
    
    def language_code=(value) -> ::String

**Parameter**

  * **value** (::String) — The language that was triggered during intent detection. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes. 



**Returns**

  * (::String) — The language that was triggered during intent detection. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes. 



### #output_contexts
    
    
    def output_contexts() -> ::Array<::Google::Cloud::Dialogflow::V2::Context>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::V2::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Context)>) — The collection of output contexts. If applicable, `output_contexts.parameters` contains entries with name `<parameter name>.original` containing the original parameter values before the query. 



### #output_contexts=
    
    
    def output_contexts=(value) -> ::Array<::Google::Cloud::Dialogflow::V2::Context>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dialogflow::V2::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Context)>) — The collection of output contexts. If applicable, `output_contexts.parameters` contains entries with name `<parameter name>.original` containing the original parameter values before the query. 



**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::V2::Context](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-Context)>) — The collection of output contexts. If applicable, `output_contexts.parameters` contains entries with name `<parameter name>.original` containing the original parameter values before the query. 



### #parameters
    
    
    def parameters() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — 

The collection of extracted parameters.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

    * MapKey type: string
    * MapKey value: parameter name
    * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
    * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



### #parameters=
    
    
    def parameters=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — 

The collection of extracted parameters.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

    * MapKey type: string
    * MapKey value: parameter name
    * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
    * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — 

The collection of extracted parameters.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

    * MapKey type: string
    * MapKey value: parameter name
    * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
    * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



### #query_text
    
    
    def query_text() -> ::String

**Returns**

  * (::String) — 

The original conversational query text:

    * If natural language text was provided as input, `query_text` contains a copy of the input.
    * If natural language speech audio was provided as input, `query_text` contains the speech recognition result. If speech recognizer produced multiple alternatives, a particular one is picked.
    * If automatic spell correction is enabled, `query_text` will contain the corrected user input.



### #query_text=
    
    
    def query_text=(value) -> ::String

**Parameter**

  * **value** (::String) — 

The original conversational query text:

    * If natural language text was provided as input, `query_text` contains a copy of the input.
    * If natural language speech audio was provided as input, `query_text` contains the speech recognition result. If speech recognizer produced multiple alternatives, a particular one is picked.
    * If automatic spell correction is enabled, `query_text` will contain the corrected user input.



**Returns**

  * (::String) — 

The original conversational query text:

    * If natural language text was provided as input, `query_text` contains a copy of the input.
    * If natural language speech audio was provided as input, `query_text` contains the speech recognition result. If speech recognizer produced multiple alternatives, a particular one is picked.
    * If automatic spell correction is enabled, `query_text` will contain the corrected user input.



### #sentiment_analysis_result
    
    
    def sentiment_analysis_result() -> ::Google::Cloud::Dialogflow::V2::SentimentAnalysisResult

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::SentimentAnalysisResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SentimentAnalysisResult)) — The sentiment analysis result, which depends on the `sentiment_analysis_request_config` specified in the request. 



### #sentiment_analysis_result=
    
    
    def sentiment_analysis_result=(value) -> ::Google::Cloud::Dialogflow::V2::SentimentAnalysisResult

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::V2::SentimentAnalysisResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SentimentAnalysisResult)) — The sentiment analysis result, which depends on the `sentiment_analysis_request_config` specified in the request. 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::SentimentAnalysisResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-SentimentAnalysisResult)) — The sentiment analysis result, which depends on the `sentiment_analysis_request_config` specified in the request. 



### #speech_recognition_confidence
    
    
    def speech_recognition_confidence() -> ::Float

**Returns**

  * (::Float) — The Speech recognition confidence between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.

This field is not guaranteed to be accurate or set. In particular this field isn't set for [StreamingDetectIntent][] since the streaming endpoint has separate confidence estimates per portion of the audio in StreamingRecognitionResult. 




### #speech_recognition_confidence=
    
    
    def speech_recognition_confidence=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The Speech recognition confidence between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.

This field is not guaranteed to be accurate or set. In particular this field isn't set for [StreamingDetectIntent][] since the streaming endpoint has separate confidence estimates per portion of the audio in StreamingRecognitionResult. 




**Returns**

  * (::Float) — The Speech recognition confidence between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.

This field is not guaranteed to be accurate or set. In particular this field isn't set for [StreamingDetectIntent][] since the streaming endpoint has separate confidence estimates per portion of the audio in StreamingRecognitionResult. 




### #webhook_payload
    
    
    def webhook_payload() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — If the query was fulfilled by a webhook call, this field is set to the value of the `payload` field returned in the webhook response. 



### #webhook_payload=
    
    
    def webhook_payload=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — If the query was fulfilled by a webhook call, this field is set to the value of the `payload` field returned in the webhook response. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Struct)) — If the query was fulfilled by a webhook call, this field is set to the value of the `payload` field returned in the webhook response. 



### #webhook_source
    
    
    def webhook_source() -> ::String

**Returns**

  * (::String) — If the query was fulfilled by a webhook call, this field is set to the value of the `source` field returned in the webhook response. 



### #webhook_source=
    
    
    def webhook_source=(value) -> ::String

**Parameter**

  * **value** (::String) — If the query was fulfilled by a webhook call, this field is set to the value of the `source` field returned in the webhook response. 



**Returns**

  * (::String) — If the query was fulfilled by a webhook call, this field is set to the value of the `source` field returned in the webhook response. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
