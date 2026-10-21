---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SessionConfig/
title: SessionConfig \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:33:20.427327+00:00
---

# SessionConfig  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SessionConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  SessionConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SessionConfig.RemoteDialogflowQueryParameters
    * JSON representation



The configuration for the session.

JSON representation  
---  
      
    
    {
      "session": string,
      "inputAudioConfig": {
        object ([InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#InputAudioConfig))
      },
      "outputAudioConfig": {
        object ([OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#OutputAudioConfig))
      },
      "historicalContexts": [
        {
          object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message))
        }
      ],
      "entryAgent": string,
      "deployment": string,
      "timeZone": string,
      "useToolFakes": boolean,
      "remoteDialogflowQueryParameters": {
        object ([SessionConfig.RemoteDialogflowQueryParameters](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SessionConfig#SessionConfig.RemoteDialogflowQueryParameters))
      },
      "enableTextStreaming": boolean,
      "excludeDiagnosticInfo": boolean
    }  
  
Fields  
---  
`session` |  `string` Required. The unique identifier of the session. Format: `projects/{project}/locations/{location}/apps/{app}/sessions/{session}`  
`inputAudioConfig` |  `object (`[InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#InputAudioConfig)`)` Optional. Configuration for processing the input audio.  
`outputAudioConfig` |  `object (`[OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#OutputAudioConfig)`)` Optional. Configuration for generating the output audio.  
`historicalContexts[]` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message)`)` Optional. The historical context of the session, including user inputs, agent responses, and other messages. Typically, CES agent would manage session automatically so client doesn't need to explicitly populate this field. However, client can optionally override the historical contexts to force the session start from certain state.  
`entryAgent` |  `string` Optional. The entry agent to handle the session. If not specified, the session will be handled by the `[root agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps#App.FIELDS.root_agent)` of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`deployment` |  `string` Optional. The deployment of the app to use for the session. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`timeZone` |  `string` Optional. The time zone of the user. If provided, the agent will use the time zone for date and time related variables. Otherwise, the agent will use the time zone specified in the App.time_zone_settings.The format is the IANA Time Zone Database time zone, e.g. "America/Los_Angeles".  
`useToolFakes` |  `boolean` Optional. Whether to use tool fakes for the session. If this field is set, the agent will attempt use tool fakes instead of calling the real tools.  
`remoteDialogflowQueryParameters` |  `object (`[SessionConfig.RemoteDialogflowQueryParameters](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/SessionConfig#SessionConfig.RemoteDialogflowQueryParameters)`)` Optional. [QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters) to send to the remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent when the session control is transferred to the remote agent.  
`enableTextStreaming` |  `boolean` Optional. Whether to enable streaming text outputs from the model. By default, text outputs from the model are collected before sending to the client. NOTE: This is only supported for text (non-voice) sessions via `[StreamRunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.sessions/streamRunSession#google.cloud.ces.v1beta.SessionService.StreamRunSession)` or `BidiRunSession`.  
`excludeDiagnosticInfo` |  `boolean` Optional. Whether to exclude diagnostic info from the session output.  
  
## SessionConfig.RemoteDialogflowQueryParameters

[QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters) to send to the remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent when the session control is transferred to the remote agent.

JSON representation  
---  
      
    
    {
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
    }  
  
Fields  
---  
`webhookHeaders` |  `map (key: string, value: string)` Optional. The HTTP headers to be sent as webhookHeaders in [QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The payload to be sent in [QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters).  
`endUserMetadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The end user metadata to be sent in [QueryParameters](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#queryparameters).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-23 UTC."],[],[]] 
