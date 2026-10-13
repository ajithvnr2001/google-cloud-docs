---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/detectIntent/
title: Method: projects.locations.agents.sessions.detectIntent \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:16.958721+00:00
---

# Method: projects.locations.agents.sessions.detectIntent  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/detectIntent/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.sessions.detectIntent Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Processes a natural language query and returns structured, actionable data as a result. This method is not idempotent, because it may cause session entity types to be updated, which in turn might affect results of future queries.

Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version).

### HTTP request

`POST https://{endpoint}/v3/{session=projects/*/locations/*/agents/*/sessions/*}:detectIntent`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`session` |  `string` Required. The name of the session this query is sent to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<Session ID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters.For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session).Note: Always use agent versions for production traffic. See [Versions and environments](https://cloud.google.com/dialogflow/cx/docs/concept/version). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `session`:

  * `dialogflow.sessions.detectIntent`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "queryParams": {
        object ([QueryParameters](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters))
      },
      "queryInput": {
        object ([QueryInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#QueryInput))
      },
      "outputAudioConfig": {
        object ([OutputAudioConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/OutputAudioConfig))
      },
      "responseView": enum ([DetectIntentResponseView](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DetectIntentResponseView))
    }  
  
Fields  
---  
`queryParams` |  `object (`[QueryParameters](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters)`)` The parameters of this query.  
`queryInput` |  `object (`[QueryInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#QueryInput)`)` Required. The input specification.  
`outputAudioConfig` |  `object (`[OutputAudioConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/OutputAudioConfig)`)` Instructs the speech synthesizer how to generate the output audio.  
`responseView` |  `enum (`[DetectIntentResponseView](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DetectIntentResponseView)`)` Optional. Specifies which fields in the `[QueryResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryResult)` to return. If not set, the default is DETECT_INTENT_RESPONSE_VIEW_FULL.  
  
### Response body

If successful, the response body contains an instance of `[DetectIntentResponse](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DetectIntentResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-10 UTC."],[],[]] 
