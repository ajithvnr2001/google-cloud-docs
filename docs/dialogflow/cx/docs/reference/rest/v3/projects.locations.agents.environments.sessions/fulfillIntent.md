---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions/fulfillIntent/
title: Method: projects.locations.agents.environments.sessions.fulfillIntent \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:04.469216+00:00
---

# Method: projects.locations.agents.environments.sessions.fulfillIntent  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions/fulfillIntent/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  Method: projects.locations.agents.environments.sessions.fulfillIntent Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Fulfills a matched intent returned by `[sessions.matchIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/matchIntent#google.cloud.dialogflow.cx.v3.Sessions.MatchIntent)`. Must be called after `[sessions.matchIntent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/matchIntent#google.cloud.dialogflow.cx.v3.Sessions.MatchIntent)`, with input from `[MatchIntentResponse](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/MatchIntentResponse)`. Otherwise, the behavior is undefined.

### HTTP request

`POST https://{endpoint}/v3/{matchIntentRequest.session=projects/*/locations/*/agents/*/environments/*/sessions/*}:fulfillIntent`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`matchIntentRequest.session` |  `string` Required. The name of the session this query is sent to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/sessions/<SessionID>` or `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/environments/<EnvironmentID>/sessions/<SessionID>`. If `Environment ID` is not specified, we assume default 'draft' environment. It's up to the API caller to choose an appropriate `Session ID`. It can be a random number or some type of session identifiers (preferably hashed). The length of the `Session ID` must not exceed 36 characters.For more information, see the [sessions guide](https://cloud.google.com/dialogflow/cx/docs/concept/session). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `session`:

  * `dialogflow.sessions.detectIntent`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "matchIntentRequest": {
        "session": string,
        "queryParams": {
          "timeZone": string,
          "geoLocation": {
            object ([LatLng](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#LatLng))
          },
          "sessionEntityTypes": [
            {
              object ([SessionEntityType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.environments.sessions.entityTypes#SessionEntityType))
            }
          ],
          "payload": {
            object
          },
          "parameters": {
            object
          },
          "parameterScope": string,
          "currentPage": string,
          "disableWebhook": boolean,
          "analyzeQueryTextSentiment": boolean,
          "webhookHeaders": {
            string: string,
            ...
          },
          "flowVersions": [
            string
          ],
          "currentPlaybook": string,
          "llmModelSettings": {
            object ([LlmModelSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/LlmModelSettings))
          },
          "channel": string,
          "sessionTtl": string,
          "endUserMetadata": {
            object
          },
          "searchConfig": {
            object ([SearchConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#SearchConfig))
          },
          "populateDataStoreConnectionSignals": boolean
        },
        "queryInput": {
          "languageCode": string,
    
          // The following is a list of mutually exclusive fields. At most one of the
          // fields will be set in a response:
          "text": {
            object ([TextInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#TextInput))
          },
          "intent": {
            object ([IntentInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#IntentInput))
          },
          "audio": {
            object ([AudioInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#AudioInput))
          },
          "event": {
            object ([EventInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#EventInput))
          },
          "dtmf": {
            object ([DtmfInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#DtmfInput))
          },
          "toolCallResult": {
            object ([ToolCallResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#ToolCallResult))
          }
          // End of mutually exclusive fields.
        },
        "persistParameterChanges": boolean
      },
      "match": {
        object ([Match](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match))
      },
      "outputAudioConfig": {
        object ([OutputAudioConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/OutputAudioConfig))
      }
    }  
  
Fields  
---  
`matchIntentRequest.queryParams` |  `object (`[QueryParameters](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters)`)` The parameters of this query.  
`matchIntentRequest.queryInput` |  `object (`[QueryInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ConversationTurn#QueryInput)`)` Required. The input specification.  
`matchIntentRequest.persistParameterChanges` |  `boolean` Persist session parameter changes from `queryParams`.  
`match` |  `object (`[Match](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Match)`)` The matched intent/event to fulfill.  
`outputAudioConfig` |  `object (`[OutputAudioConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/OutputAudioConfig)`)` Instructs the speech synthesizer how to generate output audio.  
  
### Response body

If successful, the response body contains an instance of `[FulfillIntentResponse](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/FulfillIntentResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/dialogflow`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
