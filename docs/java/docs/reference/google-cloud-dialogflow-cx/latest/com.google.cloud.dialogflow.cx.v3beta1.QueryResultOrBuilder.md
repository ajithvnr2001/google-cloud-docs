---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.QueryResultOrBuilder
title: Interface QueryResultOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:43.954906+00:00
---

# Interface QueryResultOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.QueryResultOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface QueryResultOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public interface QueryResultOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdvancedSettings()
    
    
    public abstract AdvancedSettings getAdvancedSettings()

Returns the current advanced settings including IVR settings. Even though the operations configured by these settings are performed by Dialogflow, the client may need to perform special logic at the moment. For example, if Dialogflow exports audio to Google Cloud Storage, then the client may need to wait for the resulting object to appear in the bucket before proceeding.

`.google.cloud.dialogflow.cx.v3beta1.AdvancedSettings advanced_settings = 21;`

**Returns**  
---  
**Type** | **Description**  
`[AdvancedSettings](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.AdvancedSettings)` | The advancedSettings.  
  
### getAdvancedSettingsOrBuilder()
    
    
    public abstract AdvancedSettingsOrBuilder getAdvancedSettingsOrBuilder()

Returns the current advanced settings including IVR settings. Even though the operations configured by these settings are performed by Dialogflow, the client may need to perform special logic at the moment. For example, if Dialogflow exports audio to Google Cloud Storage, then the client may need to wait for the resulting object to appear in the bucket before proceeding.

`.google.cloud.dialogflow.cx.v3beta1.AdvancedSettings advanced_settings = 21;`

**Returns**  
---  
**Type** | **Description**  
`[AdvancedSettingsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.AdvancedSettingsOrBuilder)` |   
  
### getAllowAnswerFeedback()
    
    
    public abstract boolean getAllowAnswerFeedback()

Indicates whether the Thumbs up/Thumbs down rating controls are need to be shown for the response in the Dialogflow Messenger widget.

`bool allow_answer_feedback = 32;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The allowAnswerFeedback.  
  
### getCurrentFlow()
    
    
    public abstract Flow getCurrentFlow()

The current Flow. Some, not all fields are filled in this message, including but not limited to `name` and `display_name`.

`.google.cloud.dialogflow.cx.v3beta1.Flow current_flow = 31;`

**Returns**  
---  
**Type** | **Description**  
`[Flow](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.Flow)` | The currentFlow.  
  
### getCurrentFlowOrBuilder()
    
    
    public abstract FlowOrBuilder getCurrentFlowOrBuilder()

The current Flow. Some, not all fields are filled in this message, including but not limited to `name` and `display_name`.

`.google.cloud.dialogflow.cx.v3beta1.Flow current_flow = 31;`

**Returns**  
---  
**Type** | **Description**  
`[FlowOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.FlowOrBuilder)` |   
  
### getCurrentPage()
    
    
    public abstract Page getCurrentPage()

The current Page. Some, not all fields are filled in this message, including but not limited to `name` and `display_name`.

`.google.cloud.dialogflow.cx.v3beta1.Page current_page = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Page](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.Page)` | The currentPage.  
  
### getCurrentPageOrBuilder()
    
    
    public abstract PageOrBuilder getCurrentPageOrBuilder()

The current Page. Some, not all fields are filled in this message, including but not limited to `name` and `display_name`.

`.google.cloud.dialogflow.cx.v3beta1.Page current_page = 7;`

**Returns**  
---  
**Type** | **Description**  
`[PageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.PageOrBuilder)` |   
  
### getDataStoreConnectionSignals()
    
    
    public abstract DataStoreConnectionSignals getDataStoreConnectionSignals()

Optional. Data store connection feature output signals. Filled only when data stores are involved in serving the query.

` .google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals data_store_connection_signals = 35 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DataStoreConnectionSignals](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals)` | The dataStoreConnectionSignals.  
  
### getDataStoreConnectionSignalsOrBuilder()
    
    
    public abstract DataStoreConnectionSignalsOrBuilder getDataStoreConnectionSignalsOrBuilder()

Optional. Data store connection feature output signals. Filled only when data stores are involved in serving the query.

` .google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals data_store_connection_signals = 35 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DataStoreConnectionSignalsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignalsOrBuilder)` |   
  
### getDiagnosticInfo()
    
    
    public abstract Struct getDiagnosticInfo()

The free-form diagnostic info. For example, this field could contain webhook call latency. The fields of this data can change without notice, so you should not write code that depends on its structure.

One of the fields is called "Alternative Matched Intents", which may aid with debugging. The following describes these intent results:

  * The list is empty if no intent was matched to end-user input.
  * Only intents that are referenced in the currently active flow are included.
  * The matched intent is included.
  * Other intents that could have matched end-user input, but did not match because they are referenced by intent routes that are out of [scope](https://cloud.google.com/dialogflow/cx/docs/concept/handler#scope), are included.
  * Other intents referenced by intent routes in scope that matched end-user input, but had a lower confidence score.



`.google.protobuf.Struct diagnostic_info = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The diagnosticInfo.  
  
### getDiagnosticInfoOrBuilder()
    
    
    public abstract StructOrBuilder getDiagnosticInfoOrBuilder()

The free-form diagnostic info. For example, this field could contain webhook call latency. The fields of this data can change without notice, so you should not write code that depends on its structure.

One of the fields is called "Alternative Matched Intents", which may aid with debugging. The following describes these intent results:

  * The list is empty if no intent was matched to end-user input.
  * Only intents that are referenced in the currently active flow are included.
  * The matched intent is included.
  * Other intents that could have matched end-user input, but did not match because they are referenced by intent routes that are out of [scope](https://cloud.google.com/dialogflow/cx/docs/concept/handler#scope), are included.
  * Other intents referenced by intent routes in scope that matched end-user input, but had a lower confidence score.



`.google.protobuf.Struct diagnostic_info = 10;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getDtmf()
    
    
    public abstract DtmfInput getDtmf()

If a DTMF was provided as input, this field will contain a copy of the DtmfInput.

`.google.cloud.dialogflow.cx.v3beta1.DtmfInput dtmf = 23;`

**Returns**  
---  
**Type** | **Description**  
`[DtmfInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.DtmfInput)` | The dtmf.  
  
### getDtmfOrBuilder()
    
    
    public abstract DtmfInputOrBuilder getDtmfOrBuilder()

If a DTMF was provided as input, this field will contain a copy of the DtmfInput.

`.google.cloud.dialogflow.cx.v3beta1.DtmfInput dtmf = 23;`

**Returns**  
---  
**Type** | **Description**  
`[DtmfInputOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.DtmfInputOrBuilder)` |   
  
### getGenerativeInfo()
    
    
    public abstract GenerativeInfo getGenerativeInfo()

The information of a query if handled by generative agent resources.

`.google.cloud.dialogflow.cx.v3beta1.GenerativeInfo generative_info = 33;`

**Returns**  
---  
**Type** | **Description**  
`[GenerativeInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.GenerativeInfo)` | The generativeInfo.  
  
### getGenerativeInfoOrBuilder()
    
    
    public abstract GenerativeInfoOrBuilder getGenerativeInfoOrBuilder()

The information of a query if handled by generative agent resources.

`.google.cloud.dialogflow.cx.v3beta1.GenerativeInfo generative_info = 33;`

**Returns**  
---  
**Type** | **Description**  
`[GenerativeInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.GenerativeInfoOrBuilder)` |   
  
### getIntent() (deprecated)
    
    
    public abstract Intent getIntent()

**Deprecated.** _google.cloud.dialogflow.cx.v3beta1.QueryResult.intent is deprecated. See google/cloud/dialogflow/cx/v3beta1/session.proto;l=1111_

The Intent that matched the conversational query. Some, not all fields are filled in this message, including but not limited to: `name` and `display_name`. This field is deprecated, please use QueryResult.match instead.

`.google.cloud.dialogflow.cx.v3beta1.Intent intent = 8 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[Intent](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.Intent)` | The intent.  
  
### getIntentDetectionConfidence() (deprecated)
    
    
    public abstract float getIntentDetectionConfidence()

**Deprecated.** _google.cloud.dialogflow.cx.v3beta1.QueryResult.intent_detection_confidence is deprecated. See google/cloud/dialogflow/cx/v3beta1/session.proto;l=1122_

The intent detection confidence. Values range from 0.0 (completely uncertain) to 1.0 (completely certain). This value is for informational purpose only and is only used to help match the best intent within the classification threshold. This value may change for the same end-user expression at any time due to a model retraining or change in implementation. This field is deprecated, please use QueryResult.match instead.

`float intent_detection_confidence = 9 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[float](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The intentDetectionConfidence.  
  
### getIntentOrBuilder() (deprecated)
    
    
    public abstract IntentOrBuilder getIntentOrBuilder()

The Intent that matched the conversational query. Some, not all fields are filled in this message, including but not limited to: `name` and `display_name`. This field is deprecated, please use QueryResult.match instead.

`.google.cloud.dialogflow.cx.v3beta1.Intent intent = 8 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[IntentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.IntentOrBuilder)` |   
  
### getLanguageCode()
    
    
    public abstract String getLanguageCode()

The language that was triggered during intent detection. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes.

`string language_code = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The languageCode.  
  
### getLanguageCodeBytes()
    
    
    public abstract ByteString getLanguageCodeBytes()

The language that was triggered during intent detection. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes.

`string language_code = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for languageCode.  
  
### getMatch()
    
    
    public abstract Match getMatch()

Intent match result, could be an intent or an event.

`.google.cloud.dialogflow.cx.v3beta1.Match match = 15;`

**Returns**  
---  
**Type** | **Description**  
`[Match](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.Match)` | The match.  
  
### getMatchOrBuilder()
    
    
    public abstract MatchOrBuilder getMatchOrBuilder()

Intent match result, could be an intent or an event.

`.google.cloud.dialogflow.cx.v3beta1.Match match = 15;`

**Returns**  
---  
**Type** | **Description**  
`[MatchOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.MatchOrBuilder)` |   
  
### getParameters()
    
    
    public abstract Struct getParameters()

The collected session parameters.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

  * MapKey type: string
  * MapKey value: parameter name
  * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
  * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



`.google.protobuf.Struct parameters = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The parameters.  
  
### getParametersOrBuilder()
    
    
    public abstract StructOrBuilder getParametersOrBuilder()

The collected session parameters.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

  * MapKey type: string
  * MapKey value: parameter name
  * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
  * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



`.google.protobuf.Struct parameters = 3;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getQueryCase()
    
    
    public abstract QueryResult.QueryCase getQueryCase()

**Returns**  
---  
**Type** | **Description**  
`[QueryResult.QueryCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.QueryResult.QueryCase)` |   
  
### getResponseMessages(int index)
    
    
    public abstract ResponseMessage getResponseMessages(int index)

The list of rich messages returned to the client. Responses vary from simple text messages to more sophisticated, structured payloads used to drive complex logic.

`repeated .google.cloud.dialogflow.cx.v3beta1.ResponseMessage response_messages = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResponseMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ResponseMessage)` |   
  
### getResponseMessagesCount()
    
    
    public abstract int getResponseMessagesCount()

The list of rich messages returned to the client. Responses vary from simple text messages to more sophisticated, structured payloads used to drive complex logic.

`repeated .google.cloud.dialogflow.cx.v3beta1.ResponseMessage response_messages = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getResponseMessagesList()
    
    
    public abstract List<ResponseMessage> getResponseMessagesList()

The list of rich messages returned to the client. Responses vary from simple text messages to more sophisticated, structured payloads used to drive complex logic.

`repeated .google.cloud.dialogflow.cx.v3beta1.ResponseMessage response_messages = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ResponseMessage](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ResponseMessage)>` |   
  
### getResponseMessagesOrBuilder(int index)
    
    
    public abstract ResponseMessageOrBuilder getResponseMessagesOrBuilder(int index)

The list of rich messages returned to the client. Responses vary from simple text messages to more sophisticated, structured payloads used to drive complex logic.

`repeated .google.cloud.dialogflow.cx.v3beta1.ResponseMessage response_messages = 4; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResponseMessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.ResponseMessageOrBuilder)` |   
  
### getResponseMessagesOrBuilderList()
    
    
    public abstract List<? extends ResponseMessageOrBuilder> getResponseMessagesOrBuilderList()

The list of rich messages returned to the client. Responses vary from simple text messages to more sophisticated, structured payloads used to drive complex logic.

`repeated .google.cloud.dialogflow.cx.v3beta1.ResponseMessage response_messages = 4; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3beta1.ResponseMessageOrBuilder>` |   
  
### getSentimentAnalysisResult()
    
    
    public abstract SentimentAnalysisResult getSentimentAnalysisResult()

The sentiment analyss result, which depends on [`analyze_query_text_sentiment`] [google.cloud.dialogflow.cx.v3beta1.QueryParameters.analyze_query_text_sentiment], specified in the request.

` .google.cloud.dialogflow.cx.v3beta1.SentimentAnalysisResult sentiment_analysis_result = 17; `

**Returns**  
---  
**Type** | **Description**  
`[SentimentAnalysisResult](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.SentimentAnalysisResult)` | The sentimentAnalysisResult.  
  
### getSentimentAnalysisResultOrBuilder()
    
    
    public abstract SentimentAnalysisResultOrBuilder getSentimentAnalysisResultOrBuilder()

The sentiment analyss result, which depends on [`analyze_query_text_sentiment`] [google.cloud.dialogflow.cx.v3beta1.QueryParameters.analyze_query_text_sentiment], specified in the request.

` .google.cloud.dialogflow.cx.v3beta1.SentimentAnalysisResult sentiment_analysis_result = 17; `

**Returns**  
---  
**Type** | **Description**  
`[SentimentAnalysisResultOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.SentimentAnalysisResultOrBuilder)` |   
  
### getText()
    
    
    public abstract String getText()

If natural language text was provided as input, this field will contain a copy of the text.

`string text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The text.  
  
### getTextBytes()
    
    
    public abstract ByteString getTextBytes()

If natural language text was provided as input, this field will contain a copy of the text.

`string text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for text.  
  
### getTraceBlocks(int index)
    
    
    public abstract TraceBlock getTraceBlocks(int index)

Optional. Contains the sequence of trace blocks from the current conversation turn. Trace blocks are ordered chronologically and contain detailed traces of runtime behavior such as tool calls, LLM calls, flow and playbook invocations, agent utterances and user utterances.

` repeated .google.cloud.dialogflow.cx.v3beta1.TraceBlock trace_blocks = 37 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TraceBlock](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.TraceBlock)` |   
  
### getTraceBlocksCount()
    
    
    public abstract int getTraceBlocksCount()

Optional. Contains the sequence of trace blocks from the current conversation turn. Trace blocks are ordered chronologically and contain detailed traces of runtime behavior such as tool calls, LLM calls, flow and playbook invocations, agent utterances and user utterances.

` repeated .google.cloud.dialogflow.cx.v3beta1.TraceBlock trace_blocks = 37 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTraceBlocksList()
    
    
    public abstract List<TraceBlock> getTraceBlocksList()

Optional. Contains the sequence of trace blocks from the current conversation turn. Trace blocks are ordered chronologically and contain detailed traces of runtime behavior such as tool calls, LLM calls, flow and playbook invocations, agent utterances and user utterances.

` repeated .google.cloud.dialogflow.cx.v3beta1.TraceBlock trace_blocks = 37 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TraceBlock](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.TraceBlock)>` |   
  
### getTraceBlocksOrBuilder(int index)
    
    
    public abstract TraceBlockOrBuilder getTraceBlocksOrBuilder(int index)

Optional. Contains the sequence of trace blocks from the current conversation turn. Trace blocks are ordered chronologically and contain detailed traces of runtime behavior such as tool calls, LLM calls, flow and playbook invocations, agent utterances and user utterances.

` repeated .google.cloud.dialogflow.cx.v3beta1.TraceBlock trace_blocks = 37 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TraceBlockOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3beta1.TraceBlockOrBuilder)` |   
  
### getTraceBlocksOrBuilderList()
    
    
    public abstract List<? extends TraceBlockOrBuilder> getTraceBlocksOrBuilderList()

Optional. Contains the sequence of trace blocks from the current conversation turn. Trace blocks are ordered chronologically and contain detailed traces of runtime behavior such as tool calls, LLM calls, flow and playbook invocations, agent utterances and user utterances.

` repeated .google.cloud.dialogflow.cx.v3beta1.TraceBlock trace_blocks = 37 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dialogflow.cx.v3beta1.TraceBlockOrBuilder>` |   
  
### getTranscript()
    
    
    public abstract String getTranscript()

If natural language speech audio was provided as input, this field will contain the transcript for the audio.

`string transcript = 12;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The transcript.  
  
### getTranscriptBytes()
    
    
    public abstract ByteString getTranscriptBytes()

If natural language speech audio was provided as input, this field will contain the transcript for the audio.

`string transcript = 12;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for transcript.  
  
### getTriggerEvent()
    
    
    public abstract String getTriggerEvent()

If an event was provided as input, this field will contain the name of the event.

`string trigger_event = 14;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The triggerEvent.  
  
### getTriggerEventBytes()
    
    
    public abstract ByteString getTriggerEventBytes()

If an event was provided as input, this field will contain the name of the event.

`string trigger_event = 14;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for triggerEvent.  
  
### getTriggerIntent()
    
    
    public abstract String getTriggerIntent()

If an intent was provided as input, this field will contain a copy of the intent identifier. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>`.

`string trigger_intent = 11 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The triggerIntent.  
  
### getTriggerIntentBytes()
    
    
    public abstract ByteString getTriggerIntentBytes()

If an intent was provided as input, this field will contain a copy of the intent identifier. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>`.

`string trigger_intent = 11 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for triggerIntent.  
  
### getWebhookDisplayNames(int index)
    
    
    public abstract String getWebhookDisplayNames(int index)

The list of webhook display names in the order of call sequence.

`repeated string webhook_display_names = 26;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The webhookDisplayNames at the given index.  
  
### getWebhookDisplayNamesBytes(int index)
    
    
    public abstract ByteString getWebhookDisplayNamesBytes(int index)

The list of webhook display names in the order of call sequence.

`repeated string webhook_display_names = 26;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the webhookDisplayNames at the given index.  
  
### getWebhookDisplayNamesCount()
    
    
    public abstract int getWebhookDisplayNamesCount()

The list of webhook display names in the order of call sequence.

`repeated string webhook_display_names = 26;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of webhookDisplayNames.  
  
### getWebhookDisplayNamesList()
    
    
    public abstract List<String> getWebhookDisplayNamesList()

The list of webhook display names in the order of call sequence.

`repeated string webhook_display_names = 26;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the webhookDisplayNames.  
  
### getWebhookIds(int index)
    
    
    public abstract String getWebhookIds(int index)

The list of webhook ids in the order of call sequence.

`repeated string webhook_ids = 25;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The webhookIds at the given index.  
  
### getWebhookIdsBytes(int index)
    
    
    public abstract ByteString getWebhookIdsBytes(int index)

The list of webhook ids in the order of call sequence.

`repeated string webhook_ids = 25;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the webhookIds at the given index.  
  
### getWebhookIdsCount()
    
    
    public abstract int getWebhookIdsCount()

The list of webhook ids in the order of call sequence.

`repeated string webhook_ids = 25;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of webhookIds.  
  
### getWebhookIdsList()
    
    
    public abstract List<String> getWebhookIdsList()

The list of webhook ids in the order of call sequence.

`repeated string webhook_ids = 25;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the webhookIds.  
  
### getWebhookLatencies(int index)
    
    
    public abstract Duration getWebhookLatencies(int index)

The list of webhook latencies in the order of call sequence.

`repeated .google.protobuf.Duration webhook_latencies = 27;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` |   
  
### getWebhookLatenciesCount()
    
    
    public abstract int getWebhookLatenciesCount()

The list of webhook latencies in the order of call sequence.

`repeated .google.protobuf.Duration webhook_latencies = 27;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getWebhookLatenciesList()
    
    
    public abstract List<Duration> getWebhookLatenciesList()

The list of webhook latencies in the order of call sequence.

`repeated .google.protobuf.Duration webhook_latencies = 27;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)>` |   
  
### getWebhookLatenciesOrBuilder(int index)
    
    
    public abstract DurationOrBuilder getWebhookLatenciesOrBuilder(int index)

The list of webhook latencies in the order of call sequence.

`repeated .google.protobuf.Duration webhook_latencies = 27;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getWebhookLatenciesOrBuilderList()
    
    
    public abstract List<? extends DurationOrBuilder> getWebhookLatenciesOrBuilderList()

The list of webhook latencies in the order of call sequence.

`repeated .google.protobuf.Duration webhook_latencies = 27;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.protobuf.DurationOrBuilder>` |   
  
### getWebhookPayloads(int index)
    
    
    public abstract Struct getWebhookPayloads(int index)

The list of webhook payload in WebhookResponse.payload, in the order of call sequence. If some webhook call fails or doesn't return any payload, an empty `Struct` would be used instead.

`repeated .google.protobuf.Struct webhook_payloads = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` |   
  
### getWebhookPayloadsCount()
    
    
    public abstract int getWebhookPayloadsCount()

The list of webhook payload in WebhookResponse.payload, in the order of call sequence. If some webhook call fails or doesn't return any payload, an empty `Struct` would be used instead.

`repeated .google.protobuf.Struct webhook_payloads = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getWebhookPayloadsList()
    
    
    public abstract List<Struct> getWebhookPayloadsList()

The list of webhook payload in WebhookResponse.payload, in the order of call sequence. If some webhook call fails or doesn't return any payload, an empty `Struct` would be used instead.

`repeated .google.protobuf.Struct webhook_payloads = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)>` |   
  
### getWebhookPayloadsOrBuilder(int index)
    
    
    public abstract StructOrBuilder getWebhookPayloadsOrBuilder(int index)

The list of webhook payload in WebhookResponse.payload, in the order of call sequence. If some webhook call fails or doesn't return any payload, an empty `Struct` would be used instead.

`repeated .google.protobuf.Struct webhook_payloads = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getWebhookPayloadsOrBuilderList()
    
    
    public abstract List<? extends StructOrBuilder> getWebhookPayloadsOrBuilderList()

The list of webhook payload in WebhookResponse.payload, in the order of call sequence. If some webhook call fails or doesn't return any payload, an empty `Struct` would be used instead.

`repeated .google.protobuf.Struct webhook_payloads = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.protobuf.StructOrBuilder>` |   
  
### getWebhookStatuses(int index)
    
    
    public abstract Status getWebhookStatuses(int index)

The list of webhook call status in the order of call sequence.

`repeated .google.rpc.Status webhook_statuses = 13;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` |   
  
### getWebhookStatusesCount()
    
    
    public abstract int getWebhookStatusesCount()

The list of webhook call status in the order of call sequence.

`repeated .google.rpc.Status webhook_statuses = 13;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getWebhookStatusesList()
    
    
    public abstract List<Status> getWebhookStatusesList()

The list of webhook call status in the order of call sequence.

`repeated .google.rpc.Status webhook_statuses = 13;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<com.google.rpc.Status>` |   
  
### getWebhookStatusesOrBuilder(int index)
    
    
    public abstract StatusOrBuilder getWebhookStatusesOrBuilder(int index)

The list of webhook call status in the order of call sequence.

`repeated .google.rpc.Status webhook_statuses = 13;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getWebhookStatusesOrBuilderList()
    
    
    public abstract List<? extends StatusOrBuilder> getWebhookStatusesOrBuilderList()

The list of webhook call status in the order of call sequence.

`repeated .google.rpc.Status webhook_statuses = 13;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.rpc.StatusOrBuilder>` |   
  
### getWebhookTags(int index)
    
    
    public abstract String getWebhookTags(int index)

The list of webhook tags in the order of call sequence.

`repeated string webhook_tags = 29;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The webhookTags at the given index.  
  
### getWebhookTagsBytes(int index)
    
    
    public abstract ByteString getWebhookTagsBytes(int index)

The list of webhook tags in the order of call sequence.

`repeated string webhook_tags = 29;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the webhookTags at the given index.  
  
### getWebhookTagsCount()
    
    
    public abstract int getWebhookTagsCount()

The list of webhook tags in the order of call sequence.

`repeated string webhook_tags = 29;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of webhookTags.  
  
### getWebhookTagsList()
    
    
    public abstract List<String> getWebhookTagsList()

The list of webhook tags in the order of call sequence.

`repeated string webhook_tags = 29;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the webhookTags.  
  
### hasAdvancedSettings()
    
    
    public abstract boolean hasAdvancedSettings()

Returns the current advanced settings including IVR settings. Even though the operations configured by these settings are performed by Dialogflow, the client may need to perform special logic at the moment. For example, if Dialogflow exports audio to Google Cloud Storage, then the client may need to wait for the resulting object to appear in the bucket before proceeding.

`.google.cloud.dialogflow.cx.v3beta1.AdvancedSettings advanced_settings = 21;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the advancedSettings field is set.  
  
### hasCurrentFlow()
    
    
    public abstract boolean hasCurrentFlow()

The current Flow. Some, not all fields are filled in this message, including but not limited to `name` and `display_name`.

`.google.cloud.dialogflow.cx.v3beta1.Flow current_flow = 31;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the currentFlow field is set.  
  
### hasCurrentPage()
    
    
    public abstract boolean hasCurrentPage()

The current Page. Some, not all fields are filled in this message, including but not limited to `name` and `display_name`.

`.google.cloud.dialogflow.cx.v3beta1.Page current_page = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the currentPage field is set.  
  
### hasDataStoreConnectionSignals()
    
    
    public abstract boolean hasDataStoreConnectionSignals()

Optional. Data store connection feature output signals. Filled only when data stores are involved in serving the query.

` .google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionSignals data_store_connection_signals = 35 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dataStoreConnectionSignals field is set.  
  
### hasDiagnosticInfo()
    
    
    public abstract boolean hasDiagnosticInfo()

The free-form diagnostic info. For example, this field could contain webhook call latency. The fields of this data can change without notice, so you should not write code that depends on its structure.

One of the fields is called "Alternative Matched Intents", which may aid with debugging. The following describes these intent results:

  * The list is empty if no intent was matched to end-user input.
  * Only intents that are referenced in the currently active flow are included.
  * The matched intent is included.
  * Other intents that could have matched end-user input, but did not match because they are referenced by intent routes that are out of [scope](https://cloud.google.com/dialogflow/cx/docs/concept/handler#scope), are included.
  * Other intents referenced by intent routes in scope that matched end-user input, but had a lower confidence score.



`.google.protobuf.Struct diagnostic_info = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the diagnosticInfo field is set.  
  
### hasDtmf()
    
    
    public abstract boolean hasDtmf()

If a DTMF was provided as input, this field will contain a copy of the DtmfInput.

`.google.cloud.dialogflow.cx.v3beta1.DtmfInput dtmf = 23;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dtmf field is set.  
  
### hasGenerativeInfo()
    
    
    public abstract boolean hasGenerativeInfo()

The information of a query if handled by generative agent resources.

`.google.cloud.dialogflow.cx.v3beta1.GenerativeInfo generative_info = 33;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the generativeInfo field is set.  
  
### hasIntent() (deprecated)
    
    
    public abstract boolean hasIntent()

**Deprecated.** _google.cloud.dialogflow.cx.v3beta1.QueryResult.intent is deprecated. See google/cloud/dialogflow/cx/v3beta1/session.proto;l=1111_

The Intent that matched the conversational query. Some, not all fields are filled in this message, including but not limited to: `name` and `display_name`. This field is deprecated, please use QueryResult.match instead.

`.google.cloud.dialogflow.cx.v3beta1.Intent intent = 8 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the intent field is set.  
  
### hasMatch()
    
    
    public abstract boolean hasMatch()

Intent match result, could be an intent or an event.

`.google.cloud.dialogflow.cx.v3beta1.Match match = 15;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the match field is set.  
  
### hasParameters()
    
    
    public abstract boolean hasParameters()

The collected session parameters.

Depending on your protocol or client library language, this is a map, associative array, symbol table, dictionary, or JSON object composed of a collection of (MapKey, MapValue) pairs:

  * MapKey type: string
  * MapKey value: parameter name
  * MapValue type: If parameter's entity type is a composite entity then use map, otherwise, depending on the parameter value type, it could be one of string, number, boolean, null, list or map.
  * MapValue value: If parameter's entity type is a composite entity then use map from composite entity property names to property values, otherwise, use parameter value.



`.google.protobuf.Struct parameters = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the parameters field is set.  
  
### hasSentimentAnalysisResult()
    
    
    public abstract boolean hasSentimentAnalysisResult()

The sentiment analyss result, which depends on [`analyze_query_text_sentiment`] [google.cloud.dialogflow.cx.v3beta1.QueryParameters.analyze_query_text_sentiment], specified in the request.

` .google.cloud.dialogflow.cx.v3beta1.SentimentAnalysisResult sentiment_analysis_result = 17; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sentimentAnalysisResult field is set.  
  
### hasText()
    
    
    public abstract boolean hasText()

If natural language text was provided as input, this field will contain a copy of the text.

`string text = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the text field is set.  
  
### hasTranscript()
    
    
    public abstract boolean hasTranscript()

If natural language speech audio was provided as input, this field will contain the transcript for the audio.

`string transcript = 12;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transcript field is set.  
  
### hasTriggerEvent()
    
    
    public abstract boolean hasTriggerEvent()

If an event was provided as input, this field will contain the name of the event.

`string trigger_event = 14;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the triggerEvent field is set.  
  
### hasTriggerIntent()
    
    
    public abstract boolean hasTriggerIntent()

If an intent was provided as input, this field will contain a copy of the intent identifier. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/intents/<IntentID>`.

`string trigger_intent = 11 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the triggerIntent field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
