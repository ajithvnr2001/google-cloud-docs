---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall/
title: ToolCall \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:13:06.859121+00:00
---

# ToolCall  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolCall/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  ToolCall Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Request for the client or the agent to execute the specified tool.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "args": {
        object
      },
      "parentToolCallId": string,
      "agentName": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`id` |  `string` Optional. The unique identifier of the tool call. If populated, the client should return the execution result with the matching ID in `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolResponse#FIELDS.id)`.  
`displayName` |  `string` Output only. Display name of the tool.  
`args` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The input parameters and values for the tool in JSON object format.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ToolsetTool)`)` Optional. The toolset tool to execute.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
