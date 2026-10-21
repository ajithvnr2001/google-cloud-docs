---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionInput/
title: SessionInput \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:41.887111+00:00
---

# SessionInput  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionInput/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  SessionInput Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ToolResponses
    * JSON representation
  * Event
    * JSON representation



Input for the session.

JSON representation  
---  
      
    
    {
      "willContinue": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string,
      "dtmf": string,
      "audio": string,
      "toolResponses": {
        object ([ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionInput#ToolResponses))
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#Image))
      },
      "blob": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#Blob))
      },
      "variables": {
        object
      },
      "event": {
        object ([Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionInput#Event))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`willContinue` |  `boolean` Optional. A flag to indicate if the current message is a fragment of a larger input in the bidi streaming session.When set to `true`, the agent defers processing until it receives a subsequent message where `willContinue` is `false`, or until the system detects an endpoint in the audio input.NOTE: This field does not apply to audio and DTMF inputs, as they are always processed automatically based on the endpointing signal.  
The type of the input. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` Optional. Text data from the end user.  
`dtmf` |  `string` Optional. DTMF digits from the end user.  
`audio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. Audio data from the end user.A base64-encoded string.  
`toolResponses` |  `object (`[ToolResponses](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionInput#ToolResponses)`)` Optional. Execution results for the tool calls from the client.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#Image)`)` Optional. Image data from the end user.  
`blob` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#Blob)`)` Optional. Blob data from the end user.  
`variables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Contextual variables for the session, keyed by name. Only variables declared in the app will be used by the CES agent.Unrecognized variables will still be sent to the [Dialogflow agent][Agent.RemoteDialogflowAgent] as additional session parameters.  
`event` |  `object (`[Event](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/SessionInput#Event)`)` Optional. Event input.  
End of mutually exclusive fields.  
  
## ToolResponses

Execution results for the requested tool calls from the client.

JSON representation  
---  
      
    
    {
      "toolResponses": [
        {
          object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolResponse))
        }
      ]
    }  
  
Fields  
---  
`toolResponses[]` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolResponse)`)` Optional. The list of tool execution results.  
  
## Event

Event input.

JSON representation  
---  
      
    
    {
      "event": string,
      "variables": {
        object
      }
    }  
  
Fields  
---  
`event` |  `string` Required. The name of the event.  
`variables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Additional variables associated with the event.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
