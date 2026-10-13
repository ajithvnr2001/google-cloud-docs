---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions/detectIntent/
title: Method: projects.agent.sessions.detectIntent \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:14.377665+00:00
---

# Method: projects.agent.sessions.detectIntent  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions/detectIntent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.agent.sessions.detectIntent Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause contexts and session entity types to be updated, which in turn might affect results of future queries.

If you might use [Agent Assist](https://cloud.google.com/dialogflow/docs/#aa) or other CCAI products now or in the future, consider using `[AnalyzeContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/analyzeContent#google.cloud.dialogflow.v2.Participants.AnalyzeContent)` instead of `sessions.detectIntent`. `AnalyzeContent` has additional functionality for Agent Assist and other CCAI products.

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

### HTTP request

`POST https://{endpoint}/v2/{session=projects/*/agent/sessions/*}:detectIntent`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`session` |  `string` Required. The name of the session this query is sent to. Format: `projects/<Project ID>/agent/sessions/<Session ID>`, or `projects/<Project ID>/agent/environments/<Environment ID>/users/<User ID>/sessions/<Session ID>`. If `Environment ID` is not specified, we assume default 'draft' environment (`Environment ID` might be referred to as environment name at some places). If `User ID` is not specified, we are using "-". It's up to the API caller to choose an appropriate `Session ID` and `User Id`. They can be a random number or some type of user and session identifiers (preferably hashed). The length of the `Session ID` and `User ID` must not exceed 36 characters.For more information, see the [API interactions guide](https://cloud.google.com/dialogflow/docs/api-overview).Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `session`:

  * `dialogflow.sessions.detectIntent`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "queryParams": {
        object ([QueryParameters](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/QueryParameters))
      },
      "queryInput": {
        object ([QueryInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/QueryInput))
      },
      "outputAudioConfig": {
        object ([OutputAudioConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/OutputAudioConfig))
      },
      "outputAudioConfigMask": string,
      "inputAudio": string
    }  
  
Fields  
---  
`queryParams` |  `object (`[QueryParameters](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/QueryParameters)`)` The parameters of this query.  
`queryInput` |  `object (`[QueryInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/QueryInput)`)` Required. The input specification. It can be set to:

  1. an audio config which instructs the speech recognizer how to process the speech audio,
  2. a conversational query in the form of text, or
  3. an event that specifies which intent to trigger.

  
`outputAudioConfig` |  `object (`[OutputAudioConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/OutputAudioConfig)`)` Instructs the speech synthesizer how to generate the output audio. If this field is not set and agent-level speech synthesizer is not configured, no output audio is generated.  
`outputAudioConfigMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Mask for `[outputAudioConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions/detectIntent#body.request_body.FIELDS.output_audio_config)` indicating which settings in this request-level config should override speech synthesizer settings defined at agent-level.If unspecified or empty, `[outputAudioConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.sessions/detectIntent#body.request_body.FIELDS.output_audio_config)` replaces the agent-level config in its entirety.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`inputAudio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The natural language speech audio to be processed. This field should be populated iff `queryInput` is set to an input audio config. A single request can contain up to 1 minute of speech audio data.A base64-encoded string.  
  
### Response body

If successful, the response body contains an instance of `[DetectIntentResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/DetectIntentResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
