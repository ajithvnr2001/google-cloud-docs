---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/RunSessionResponse/
title: RunSessionResponse \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:33:02.712230+00:00
---

# RunSessionResponse  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/RunSessionResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  RunSessionResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * SessionOutput
    * JSON representation
  * ToolCalls
    * JSON representation
  * EndSession
    * JSON representation
  * SessionOutput.DiagnosticInfo
    * JSON representation



Response message for `[SessionService.RunSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.sessions/runSession#google.cloud.ces.v1beta.SessionService.RunSession)`.

JSON representation  
---  
      
    
    {
      "outputs": [
        {
          object ([SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/RunSessionResponse#SessionOutput))
        }
      ]
    }  
  
Fields  
---  
`outputs[]` |  `object (`[SessionOutput](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/RunSessionResponse#SessionOutput)`)` Outputs for the session.  
  
## SessionOutput

Output for the session.

JSON representation  
---  
      
    
    {
      "turnIndex": integer,
      "turnCompleted": boolean,
      "diagnosticInfo": {
        object ([SessionOutput.DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/RunSessionResponse#SessionOutput.DiagnosticInfo))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string,
      "audio": string,
      "toolCalls": {
        object ([ToolCalls](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/RunSessionResponse#ToolCalls))
      },
      "citations": {
        object ([Citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Citations))
      },
      "googleSearchSuggestions": {
        object ([GoogleSearchSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/GoogleSearchSuggestions))
      },
      "endSession": {
        object ([EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/RunSessionResponse#EndSession))
      },
      "payload": {
        object
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Image))
      },
      "progress": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`turnIndex` |  `integer` Indicates the sequential order of conversation turn to which this output belongs to, starting from 1.  
`turnCompleted` |  `boolean` If true, the CES agent has detected the end of the current conversation turn and will provide no further output for this turn.  
`diagnosticInfo` |  `object (`[SessionOutput.DiagnosticInfo](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/RunSessionResponse#SessionOutput.DiagnosticInfo)`)` Optional. Diagnostic information contains execution details during the processing of the input. Only populated in the last SessionOutput (with `turnCompleted=true`) for each turn.  
The type of the output. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` Output text from the CES agent.  
`audio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output audio from the CES agent.A base64-encoded string.  
`toolCalls` |  `object (`[ToolCalls](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/RunSessionResponse#ToolCalls)`)` Request for the client to execute the tools.  
`citations` |  `object (`[Citations](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Citations)`)` Citations that provide the source information for the agent's generated text.  
`googleSearchSuggestions` |  `object (`[GoogleSearchSuggestions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/GoogleSearchSuggestions)`)` The suggestions returned from Google Search as a result of invoking the `[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.tools#Tool.GoogleSearchTool)`.  
`endSession` |  `object (`[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/RunSessionResponse#EndSession)`)` Indicates the session has ended.  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Custom payload with structured output from the CES agent.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Image)`)` Output image from the CES agent.  
`progress` |  `string` Intermediate progress update from the CES agent.  
End of mutually exclusive fields.  
  
## ToolCalls

Request for the client to execute the tools and return the execution results before continuing the session.

JSON representation  
---  
      
    
    {
      "toolCalls": [
        {
          object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall))
        }
      ]
    }  
  
Fields  
---  
`toolCalls[]` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall)`)` Optional. The list of tool calls to execute.  
  
## EndSession

Indicates the session has terminated, due to either successful completion (e.g. user says "Good bye!" ) or an agent escalation.

The agent will not process any further inputs after session is terminated and the client should half-close and disconnect after receiving all remaining responses from the agent.

JSON representation  
---  
      
    
    {
      "metadata": {
        object
      }
    }  
  
Fields  
---  
`metadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Provides additional information about the end session signal, such as the reason for ending the session.  
  
## SessionOutput.DiagnosticInfo

Contains execution details during the processing.

JSON representation  
---  
      
    
    {
      "messages": [
        {
          object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message))
        }
      ],
      "rootSpan": {
        object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Span))
      }
    }  
  
Fields  
---  
`messages[]` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Message)`)` List of the messages that happened during the processing.  
`rootSpan` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Span)`)` A trace of the entire request processing, represented as a root span. This span can contain nested child spans for specific operations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
