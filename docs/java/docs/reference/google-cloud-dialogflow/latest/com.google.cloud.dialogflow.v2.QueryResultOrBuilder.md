---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResultOrBuilder
title: Interface QueryResultOrBuilder (4.105.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:05.227709+00:00
---

# Interface QueryResultOrBuilder (4.105.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.QueryResultOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface QueryResultOrBuilder (4.105.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.105.0 (latest)  4.101.0  4.100.0  4.99.0  4.97.0  4.94.0  4.93.0  4.91.0  4.89.0  4.88.0  4.87.0  4.86.0  4.84.0  4.82.0  4.81.0  4.80.0  4.79.0  4.78.0  4.76.0  4.74.0  4.73.0  4.70.0  4.69.0  4.68.0  4.66.0  4.65.0  4.64.0  4.63.0  4.62.0  4.61.0  4.60.0  4.59.0  4.58.0  4.57.0  4.55.0  4.54.0  4.53.0  4.52.0  4.51.0  4.50.0  4.49.0  4.48.0  4.47.0  4.46.0  4.45.0  4.43.0  4.42.0  4.41.0  4.40.0  4.39.0  4.38.0  4.37.0  4.36.0  4.35.0  4.34.0  4.33.0  4.30.0  4.29.0  4.28.0  4.27.0  4.26.0  4.25.0  4.24.0  4.23.0  4.22.0  4.21.0  4.20.0  4.19.0  4.18.0  4.17.0  4.15.0  4.14.0  4.13.0  4.12.0  4.11.0  4.10.0  4.9.1  4.8.6  4.7.5  4.6.0  4.5.11  4.4.0  4.3.1 
    
    
    public interface QueryResultOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAction()
    
    
    public abstract String getAction()

The action name from the matched intent.

`string action = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The action.  
  
### getActionBytes()
    
    
    public abstract ByteString getActionBytes()

The action name from the matched intent.

`string action = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for action.  
  
### getAllRequiredParamsPresent()
    
    
    public abstract boolean getAllRequiredParamsPresent()

This field is set to:

  * `false` if the matched intent has required parameters and not all of the required parameter values have been collected.
  * `true` if all required parameter values have been collected, or if the matched intent doesn't contain any required parameters.



`bool all_required_params_present = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allRequiredParamsPresent.  
  
### getCancelsSlotFilling()
    
    
    public abstract boolean getCancelsSlotFilling()

Indicates whether the conversational query triggers a cancellation for slot filling. For more information, see the [cancel slot filling documentation](https://cloud.google.com/dialogflow/es/docs/intents-actions-parameters#cancel).

`bool cancels_slot_filling = 21;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The cancelsSlotFilling.  
  
### getDiagnosticInfo()
    
    
    public abstract Struct getDiagnosticInfo()

Free-form diagnostic information for the associated detect intent request. The fields of this data can change without notice, so you should not write code that depends on its structure. The data may contain:

  * webhook call latency
  * webhook errors



`.google.protobuf.Struct diagnostic_info = 14;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The diagnosticInfo.  
  
### getDiagnosticInfoOrBuilder()
    
    
    public abstract StructOrBuilder getDiagnosticInfoOrBuilder()

Free-form diagnostic information for the associated detect intent request. The fields of this data can change without notice, so you should not write code that depends on its structure. The data may contain:

  * webhook call latency
  * webhook errors



`.google.protobuf.Struct diagnostic_info = 14;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getFulfillmentMessages(int index)
    
    
    public abstract Intent.Message getFulfillmentMessages(int index)

The collection of rich messages to present to the user.

`repeated .google.cloud.dialogflow.v2.Intent.Message fulfillment_messages = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Intent.Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message)` |   
  
### getFulfillmentMessagesCount()
    
    
    public abstract int getFulfillmentMessagesCount()

The collection of rich messages to present to the user.

`repeated .google.cloud.dialogflow.v2.Intent.Message fulfillment_messages = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getFulfillmentMessagesList()
    
    
    public abstract List<Intent.Message> getFulfillmentMessagesList()

The collection of rich messages to present to the user.

`repeated .google.cloud.dialogflow.v2.Intent.Message fulfillment_messages = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Message](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.Message)>` |   
  
### getFulfillmentMessagesOrBuilder(int index)
    
    
    public abstract Intent.MessageOrBuilder getFulfillmentMessagesOrBuilder(int index)

The collection of rich messages to present to the user.

`repeated .google.cloud.dialogflow.v2.Intent.Message fulfillment_messages = 7;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Intent.MessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent.MessageOrBuilder)` |   
  
### getFulfillmentMessagesOrBuilderList()
    
    
    public abstract List<? extends Intent.MessageOrBuilder> getFulfillmentMessagesOrBuilderList()

The collection of rich messages to present to the user.

`repeated .google.cloud.dialogflow.v2.Intent.Message fulfillment_messages = 7;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.v2.Intent.MessageOrBuilder>` |   
  
### getFulfillmentText()
    
    
    public abstract String getFulfillmentText()

The text to be pronounced to the user or shown on the screen. Note: This is a legacy field, `fulfillment_messages` should be preferred.

`string fulfillment_text = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The fulfillmentText.  
  
### getFulfillmentTextBytes()
    
    
    public abstract ByteString getFulfillmentTextBytes()

The text to be pronounced to the user or shown on the screen. Note: This is a legacy field, `fulfillment_messages` should be preferred.

`string fulfillment_text = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for fulfillmentText.  
  
### getIntent()
    
    
    public abstract Intent getIntent()

The intent that matched the conversational query. Some, not all fields are filled in this message, including but not limited to: `name`, `display_name`, `end_interaction` and `is_fallback`.

`.google.cloud.dialogflow.v2.Intent intent = 11;`

**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Intent)` | The intent.  
  
### getIntentDetectionConfidence()
    
    
    public abstract float getIntentDetectionConfidence()

The intent detection confidence. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation. If there are `multiple knowledge_answers` messages, this value is set to the greatest `knowledgeAnswers.match_confidence` value in the list.

`float intent_detection_confidence = 12;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The intentDetectionConfidence.  
  
### getIntentOrBuilder()
    
    
    public abstract IntentOrBuilder getIntentOrBuilder()

The intent that matched the conversational query. Some, not all fields are filled in this message, including but not limited to: `name`, `display_name`, `end_interaction` and `is_fallback`.

`.google.cloud.dialogflow.v2.Intent intent = 11;`

**Returns**  
---  
**Type** | **Description**  
`[IntentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.IntentOrBuilder)` |   
  
### getLanguageCode()
    
    
    public abstract String getLanguageCode()

The language that was triggered during intent detection. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes.

`string language_code = 15;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageCode.  
  
### getLanguageCodeBytes()
    
    
    public abstract ByteString getLanguageCodeBytes()

The language that was triggered during intent detection. See [Language Support](https://cloud.google.com/dialogflow/docs/reference/language) for a list of the currently supported language codes.

`string language_code = 15;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageCode.  
  
### getOutputContexts(int index)
    
    
    public abstract Context getOutputContexts(int index)

The collection of output contexts. If applicable, `output_contexts.parameters` contains entries with name `<parameter name>.original` containing the original parameter values before the query.

`repeated .google.cloud.dialogflow.v2.Context output_contexts = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Context)` |   
  
### getOutputContextsCount()
    
    
    public abstract int getOutputContextsCount()

The collection of output contexts. If applicable, `output_contexts.parameters` contains entries with name `<parameter name>.original` containing the original parameter values before the query.

`repeated .google.cloud.dialogflow.v2.Context output_contexts = 10;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOutputContextsList()
    
    
    public abstract List<Context> getOutputContextsList()

The collection of output contexts. If applicable, `output_contexts.parameters` contains entries with name `<parameter name>.original` containing the original parameter values before the query.

`repeated .google.cloud.dialogflow.v2.Context output_contexts = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.Context)>` |   
  
### getOutputContextsOrBuilder(int index)
    
    
    public abstract ContextOrBuilder getOutputContextsOrBuilder(int index)

The collection of output contexts. If applicable, `output_contexts.parameters` contains entries with name `<parameter name>.original` containing the original parameter values before the query.

`repeated .google.cloud.dialogflow.v2.Context output_contexts = 10;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContextOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.ContextOrBuilder)` |   
  
### getOutputContextsOrBuilderList()
    
    
    public abstract List<? extends ContextOrBuilder> getOutputContextsOrBuilderList()

The collection of output contexts. If applicable, `output_contexts.parameters` contains entries with name `<parameter name>.original` containing the original parameter values before the query.

`repeated .google.cloud.dialogflow.v2.Context output_contexts = 10;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.v2.ContextOrBuilder>` |   
  
### getParameters()
    
    
    public abstract Struct getParameters()

The collection of extracted parameters.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

  * MapKey type: string
  * MapKey value: parameter name
  * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
  * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



`.google.protobuf.Struct parameters = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The parameters.  
  
### getParametersOrBuilder()
    
    
    public abstract StructOrBuilder getParametersOrBuilder()

The collection of extracted parameters.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

  * MapKey type: string
  * MapKey value: parameter name
  * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
  * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



`.google.protobuf.Struct parameters = 4;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getQueryText()
    
    
    public abstract String getQueryText()

The original conversational query text:

  * If natural language text was provided as input, `query_text` contains a copy of the input.
  * If natural language speech audio was provided as input, `query_text` contains the speech recognition result. If speech recognizer produced multiple alternatives, a particular one is picked.
  * If automatic spell correction is enabled, `query_text` will contain the corrected user input.



`string query_text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The queryText.  
  
### getQueryTextBytes()
    
    
    public abstract ByteString getQueryTextBytes()

The original conversational query text:

  * If natural language text was provided as input, `query_text` contains a copy of the input.
  * If natural language speech audio was provided as input, `query_text` contains the speech recognition result. If speech recognizer produced multiple alternatives, a particular one is picked.
  * If automatic spell correction is enabled, `query_text` will contain the corrected user input.



`string query_text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for queryText.  
  
### getSentimentAnalysisResult()
    
    
    public abstract SentimentAnalysisResult getSentimentAnalysisResult()

The sentiment analysis result, which depends on the `sentiment_analysis_request_config` specified in the request.

`.google.cloud.dialogflow.v2.SentimentAnalysisResult sentiment_analysis_result = 17; `

**Returns**  
---  
**Type** | **Description**  
`[SentimentAnalysisResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SentimentAnalysisResult)` | The sentimentAnalysisResult.  
  
### getSentimentAnalysisResultOrBuilder()
    
    
    public abstract SentimentAnalysisResultOrBuilder getSentimentAnalysisResultOrBuilder()

The sentiment analysis result, which depends on the `sentiment_analysis_request_config` specified in the request.

`.google.cloud.dialogflow.v2.SentimentAnalysisResult sentiment_analysis_result = 17; `

**Returns**  
---  
**Type** | **Description**  
`[SentimentAnalysisResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow/latest/com.google.cloud.dialogflow.v2.SentimentAnalysisResultOrBuilder)` |   
  
### getSpeechRecognitionConfidence()
    
    
    public abstract float getSpeechRecognitionConfidence()

The Speech recognition confidence between 0.0 and 1.0. A higher number indicates an estimated greater likelihood that the recognized words are correct. The default of 0.0 is a sentinel value indicating that confidence was not set.

This field is not guaranteed to be accurate or set. In particular this field isn't set for [StreamingDetectIntent][] since the streaming endpoint has separate confidence estimates per portion of the audio in StreamingRecognitionResult.

`float speech_recognition_confidence = 2;`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The speechRecognitionConfidence.  
  
### getWebhookPayload()
    
    
    public abstract Struct getWebhookPayload()

If the query was fulfilled by a webhook call, this field is set to the value of the `payload` field returned in the webhook response.

`.google.protobuf.Struct webhook_payload = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The webhookPayload.  
  
### getWebhookPayloadOrBuilder()
    
    
    public abstract StructOrBuilder getWebhookPayloadOrBuilder()

If the query was fulfilled by a webhook call, this field is set to the value of the `payload` field returned in the webhook response.

`.google.protobuf.Struct webhook_payload = 9;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getWebhookSource()
    
    
    public abstract String getWebhookSource()

If the query was fulfilled by a webhook call, this field is set to the value of the `source` field returned in the webhook response.

`string webhook_source = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The webhookSource.  
  
### getWebhookSourceBytes()
    
    
    public abstract ByteString getWebhookSourceBytes()

If the query was fulfilled by a webhook call, this field is set to the value of the `source` field returned in the webhook response.

`string webhook_source = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for webhookSource.  
  
### hasDiagnosticInfo()
    
    
    public abstract boolean hasDiagnosticInfo()

Free-form diagnostic information for the associated detect intent request. The fields of this data can change without notice, so you should not write code that depends on its structure. The data may contain:

  * webhook call latency
  * webhook errors



`.google.protobuf.Struct diagnostic_info = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the diagnosticInfo field is set.  
  
### hasIntent()
    
    
    public abstract boolean hasIntent()

The intent that matched the conversational query. Some, not all fields are filled in this message, including but not limited to: `name`, `display_name`, `end_interaction` and `is_fallback`.

`.google.cloud.dialogflow.v2.Intent intent = 11;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the intent field is set.  
  
### hasParameters()
    
    
    public abstract boolean hasParameters()

The collection of extracted parameters.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

  * MapKey type: string
  * MapKey value: parameter name
  * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
  * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



`.google.protobuf.Struct parameters = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the parameters field is set.  
  
### hasSentimentAnalysisResult()
    
    
    public abstract boolean hasSentimentAnalysisResult()

The sentiment analysis result, which depends on the `sentiment_analysis_request_config` specified in the request.

`.google.cloud.dialogflow.v2.SentimentAnalysisResult sentiment_analysis_result = 17; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sentimentAnalysisResult field is set.  
  
### hasWebhookPayload()
    
    
    public abstract boolean hasWebhookPayload()

If the query was fulfilled by a webhook call, this field is set to the value of the `payload` field returned in the webhook response.

`.google.protobuf.Struct webhook_payload = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the webhookPayload field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
