---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.sessions/streamRunSession/
title: Method: projects.locations.apps.sessions.streamRunSession \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:35.185059+00:00
---

# Method: projects.locations.apps.sessions.streamRunSession  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.sessions/streamRunSession/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.sessions.streamRunSession Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Initiates a single-turn interaction with the CES agent. Uses server-side streaming to deliver incremental results and partial responses as they are generated.

By default, complete responses (e.g., messages from callbacks or full LLM responses) are sent to the client as soon as they are available. To enable streaming individual text chunks directly from the model, set `[enableTextStreaming](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionConfig#FIELDS.enable_text_streaming)` to true.

### HTTP request

`POST https://ces.googleapis.com/v1/{config.session=projects/*/locations/*/apps/*/sessions/*}:streamRunSession`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`config.session` |  `string` Required. The unique identifier of the session. Format: `projects/{project}/locations/{location}/apps/{app}/sessions/{session}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "config": {
        "session": string,
        "inputAudioConfig": {
          "audioEncoding": enum ([AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionConfig#AudioEncoding)),
          "sampleRateHertz": integer,
          "noiseSuppressionLevel": string
        },
        "outputAudioConfig": {
          "audioEncoding": enum ([AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionConfig#AudioEncoding)),
          "sampleRateHertz": integer
        },
        "historicalContexts": [
          {
            "role": string,
            "chunks": [
              {
                object ([Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#Chunk))
              }
            ],
            "eventTime": string
          }
        ],
        "entryAgent": string,
        "deployment": string,
        "timeZone": string,
        "useToolFakes": boolean,
        "remoteDialogflowQueryParameters": {
          "webhookHeaders": {
            string: string,
            ...
          },
          "payload": {
            object
          },
          "endUserMetadata": {
            object
          }
        },
        "enableTextStreaming": boolean,
        "excludeDiagnosticInfo": boolean
      },
      "inputs": [
        {
          object ([SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionInput))
        }
      ]
    }  
  
Fields  
---  
`config.inputAudioConfig` |  `object (`[InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionConfig#InputAudioConfig)`)` Optional. Configuration for processing the input audio.  
`config.outputAudioConfig` |  `object (`[OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionConfig#OutputAudioConfig)`)` Optional. Configuration for generating the output audio.  
`config.historicalContexts[]` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message)`)` Optional. The historical context of the session, including user inputs, agent responses, and other messages. Typically, CES agent would manage session automatically so client doesn't need to explicitly populate this field. However, client can optionally override the historical contexts to force the session start from certain state.  
`config.entryAgent` |  `string` Optional. The entry agent to handle the session. If not specified, the session will be handled by the `[root agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.FIELDS.root_agent)` of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`config.deployment` |  `string` Optional. The deployment of the app to use for the session. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`config.timeZone` |  `string` Optional. The time zone of the user. If provided, the agent will use the time zone for date and time related variables. Otherwise, the agent will use the time zone specified in the App.time_zone_settings.The format is the IANA Time Zone Database time zone, e.g. "America/Los_Angeles".  
`config.useToolFakes` |  `boolean` Optional. Whether to use tool fakes for the session. If this field is set, the agent will attempt use tool fakes instead of calling the real tools.  
`config.remoteDialogflowQueryParameters` |  `object (`[SessionConfig.RemoteDialogflowQueryParameters](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionConfig#SessionConfig.RemoteDialogflowQueryParameters)`)` Optional. [QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters) to send to the remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent when the session control is transferred to the remote agent.  
`config.enableTextStreaming` |  `boolean` Optional. Whether to enable streaming text outputs from the model. By default, text outputs from the model are collected before sending to the client. NOTE: This is only supported for text (non-voice) sessions via `[sessions.streamRunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.sessions/streamRunSession#google.cloud.ces.v1.SessionService.StreamRunSession)` or `BidiRunSession`.  
`config.excludeDiagnosticInfo` |  `boolean` Optional. Whether to exclude diagnostic info from the session output.  
`inputs[]` |  `object (`[SessionInput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionInput)`)` Required. Inputs for the session.  
  
### Response body

If successful, the response body contains a stream of `[RunSessionResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/RunSessionResponse)` instances.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `session` resource:

  * `ces.sessions.runSession`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-23 UTC."],[],[]] 
