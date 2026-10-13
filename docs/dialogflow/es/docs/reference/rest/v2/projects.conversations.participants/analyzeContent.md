---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/analyzeContent/
title: Method: projects.conversations.participants.analyzeContent \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:23.752377+00:00
---

# Method: projects.conversations.participants.analyzeContent  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations.participants/analyzeContent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  Method: projects.conversations.participants.analyzeContent Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Adds a text (chat, for example), or audio (phone recording, for example) message from a participant into the conversation.

Note: Always use agent versions for production traffic sent to virtual agents. See [Versions and environments](https://cloud.google.com/dialogflow/es/docs/agents-versions).

### HTTP request

`POST https://{endpoint}/v2/{participant=projects/*/conversations/*/participants/*}:analyzeContent`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`participant` |  `string` Required. The name of the participant this text comes from. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `participant`:

  * `dialogflow.participants.analyzeContent`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "replyAudioConfig": {
        object ([OutputAudioConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/OutputAudioConfig))
      },
      "queryParams": {
        object ([QueryParameters](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/QueryParameters))
      },
      "assistQueryParams": {
        object ([AssistQueryParameters](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/AssistQueryParameters))
      },
      "cxParameters": {
        object
      },
      "requestId": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "textInput": {
        object ([TextInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/TextInput))
      },
      "audioInput": {
        object ([AudioInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/AudioInput))
      },
      "eventInput": {
        object ([EventInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/EventInput))
      },
      "suggestionInput": {
        object ([SuggestionInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SuggestionInput))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`replyAudioConfig` |  `object (`[OutputAudioConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/OutputAudioConfig)`)` Speech synthesis configuration. The speech synthesis settings for a virtual agent that may be configured for the associated conversation profile are not used when calling participants.analyzeContent. If this configuration is not supplied, speech synthesis is disabled.  
`queryParams` |  `object (`[QueryParameters](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/QueryParameters)`)` Parameters for a Dialogflow virtual-agent query.  
`assistQueryParams` |  `object (`[AssistQueryParameters](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/AssistQueryParameters)`)` Parameters for a human assist query.  
`cxParameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Additional parameters to be put into Dialogflow CX session parameters. To remove a parameter from the session, clients should explicitly set the parameter value to null.Note: this field should only be used if you are connecting to a Dialogflow CX agent.  
`requestId` |  `string` A unique identifier for this request. Restricted to 36 ASCII characters. A random UUID is recommended. This request is only idempotent if a `requestId` is provided.  
Required. The input content. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`textInput` |  `object (`[TextInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/TextInput)`)` The natural language text to be processed.  
`audioInput` |  `object (`[AudioInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/AudioInput)`)` The natural language speech audio to be processed.  
`eventInput` |  `object (`[EventInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/EventInput)`)` An input event to send to Dialogflow.  
`suggestionInput` |  `object (`[SuggestionInput](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SuggestionInput)`)` An input representing the selection of a suggestion.  
End of mutually exclusive fields.  
  
### Response body

If successful, the response body contains an instance of `[AnalyzeContentResponse](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/AnalyzeContentResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
