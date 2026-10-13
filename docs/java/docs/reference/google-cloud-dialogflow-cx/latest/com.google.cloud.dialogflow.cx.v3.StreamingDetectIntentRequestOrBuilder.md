---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequestOrBuilder
title: Interface StreamingDetectIntentRequestOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:43.349575+00:00
---

# Interface StreamingDetectIntentRequestOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.StreamingDetectIntentRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface StreamingDetectIntentRequestOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.7  0.13.1  0.12.1  0.11.5 
    
    
    public interface StreamingDetectIntentRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEnableDebuggingInfo()
    
    
    public abstract boolean getEnableDebuggingInfo()

If true, `StreamingDetectIntentResponse.debugging_info` will get populated.

`bool enable_debugging_info = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableDebuggingInfo.  
  
### getEnablePartialResponse()
    
    
    public abstract boolean getEnablePartialResponse()

Enable partial detect intent response. If this flag is not enabled, response stream still contains only one final `DetectIntentResponse` even if some `Fulfillment`s in the agent have been configured to return partial responses.

`bool enable_partial_response = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enablePartialResponse.  
  
### getOutputAudioConfig()
    
    
    public abstract OutputAudioConfig getOutputAudioConfig()

Instructs the speech synthesizer how to generate the output audio.

`.google.cloud.dialogflow.cx.v3.OutputAudioConfig output_audio_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[OutputAudioConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfig)` | The outputAudioConfig.  
  
### getOutputAudioConfigOrBuilder()
    
    
    public abstract OutputAudioConfigOrBuilder getOutputAudioConfigOrBuilder()

Instructs the speech synthesizer how to generate the output audio.

`.google.cloud.dialogflow.cx.v3.OutputAudioConfig output_audio_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[OutputAudioConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.OutputAudioConfigOrBuilder)` |   
  
### getQueryInput()
    
    
    public abstract QueryInput getQueryInput()

Required. The input specification.

` .google.cloud.dialogflow.cx.v3.QueryInput query_input = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[QueryInput](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInput)` | The queryInput.  
  
### getQueryInputOrBuilder()
    
    
    public abstract QueryInputOrBuilder getQueryInputOrBuilder()

Required. The input specification.

` .google.cloud.dialogflow.cx.v3.QueryInput query_input = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[QueryInputOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryInputOrBuilder)` |   
  
### getQueryParams()
    
    
    public abstract QueryParameters getQueryParams()

The parameters of this query.

`.google.cloud.dialogflow.cx.v3.QueryParameters query_params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QueryParameters](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParameters)` | The queryParams.  
  
### getQueryParamsOrBuilder()
    
    
    public abstract QueryParametersOrBuilder getQueryParamsOrBuilder()

The parameters of this query.

`.google.cloud.dialogflow.cx.v3.QueryParameters query_params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QueryParametersOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.QueryParametersOrBuilder)` |   
  
### getResponseView()
    
    
    public abstract DetectIntentResponseView getResponseView()

Optional. Specifies which fields in the QueryResult to return. If not set, the default is DETECT_INTENT_RESPONSE_VIEW_FULL.

` .google.cloud.dialogflow.cx.v3.DetectIntentResponseView response_view = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[DetectIntentResponseView](https://docs.cloud.google.com/java/docs/reference/google-cloud-dialogflow-cx/latest/com.google.cloud.dialogflow.cx.v3.DetectIntentResponseView)` | The responseView.  
  
### getResponseViewValue()
    
    
    public abstract int getResponseViewValue()

Optional. Specifies which fields in the QueryResult to return. If not set, the default is DETECT_INTENT_RESPONSE_VIEW_FULL.

` .google.cloud.dialogflow.cx.v3.DetectIntentResponseView response_view = 16 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for responseView.  
  
### getSession()
    
    
    public abstract String getSession()

The name of the session this query is sent to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. Note: session must be set in the first request.

For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

`string session = 1 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The session.  
  
### getSessionBytes()
    
    
    public abstract ByteString getSessionBytes()

The name of the session this query is sent to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters. Note: session must be set in the first request.

For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

`string session = 1 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for session.  
  
### hasOutputAudioConfig()
    
    
    public abstract boolean hasOutputAudioConfig()

Instructs the speech synthesizer how to generate the output audio.

`.google.cloud.dialogflow.cx.v3.OutputAudioConfig output_audio_config = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the outputAudioConfig field is set.  
  
### hasQueryInput()
    
    
    public abstract boolean hasQueryInput()

Required. The input specification.

` .google.cloud.dialogflow.cx.v3.QueryInput query_input = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the queryInput field is set.  
  
### hasQueryParams()
    
    
    public abstract boolean hasQueryParams()

The parameters of this query.

`.google.cloud.dialogflow.cx.v3.QueryParameters query_params = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the queryParams field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
