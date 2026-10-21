---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message/
title: Message \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:40.748751+00:00
---

# Message  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Message Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Chunk
    * JSON representation
  * Blob
    * JSON representation
  * Image
    * JSON representation
  * ToolCall
    * JSON representation
  * ToolsetTool
    * JSON representation
  * ToolResponse
    * JSON representation
  * AgentTransfer
    * JSON representation



A message within a conversation.

JSON representation  
---  
      
    
    {
      "role": string,
      "chunks": [
        {
          object ([Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#Chunk))
        }
      ],
      "eventTime": string
    }  
  
Fields  
---  
`role` |  `string` Optional. The role within the conversation, e.g., user, agent.  
`chunks[]` |  `object (`[Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#Chunk)`)` Optional. Content of the message as a series of chunks.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Timestamp when the message was sent or received. Should not be used if the message is part of an `[example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.examples#Example)`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Chunk

A chunk of content within a message.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string,
      "transcript": string,
      "blob": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#Blob))
      },
      "payload": {
        object
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#Image))
      },
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolResponse))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#AgentTransfer))
      },
      "updatedVariables": {
        object
      },
      "defaultVariables": {
        object
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Chunk data. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` Optional. Text data.  
`transcript` |  `string` Optional. Transcript associated with the audio.  
`blob` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#Blob)`)` Optional. Blob data.  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom payload data.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#Image)`)` Optional. Image data.  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolCall)`)` Optional. Tool execution request.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolResponse)`)` Optional. Tool execution response.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#AgentTransfer)`)` Optional. Agent transfer event.  
`updatedVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents variables that were updated in the conversation, keyed by variable names.  
`defaultVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents default variables at the start of the conversation, keyed by variable names.  
End of mutually exclusive fields.  
  
## Blob

Represents a blob input or output in the conversation.

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the blob.A base64-encoded string.  
  
## Image

Represents an image input or output in the conversation.

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string,
      "altText": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data. Supported image types includes: * image/png * image/jpeg * image/webp  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the image.A base64-encoded string.  
`altText` |  `string` Optional. The alternative text for the image.  
  
## ToolCall

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
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolsetTool))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`id` |  `string` Optional. The unique identifier of the tool call. If populated, the client should return the execution result with the matching ID in `[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolResponse.FIELDS.id)`.  
`displayName` |  `string` Output only. Display name of the tool.  
`args` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The input parameters and values for the tool in JSON object format.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolsetTool)`)` Optional. The toolset tool to execute.  
End of mutually exclusive fields.  
  
## ToolsetTool

A tool that is created from a toolset.

JSON representation  
---  
      
    
    {
      "toolset": string,
      "toolId": string
    }  
  
Fields  
---  
`toolset` |  `string` Required. The resource name of the Toolset from which this tool is derived. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`toolId` |  `string` Optional. The tool ID to filter the tools to retrieve the schema for.  
  
## ToolResponse

The execution result of a specific tool from the client or the agent.

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "response": {
        object
      },
      "parentToolCallId": string,
      "agentName": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolsetTool))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`id` |  `string` Optional. The matching ID of the `[tool call](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolCall)` the response is for.  
`displayName` |  `string` Output only. Display name of the tool.  
`response` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. The tool execution result in JSON object format. Use "output" key to specify tool response and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as tool execution result.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
The identifier of the tool that got executed. It could be either a persisted tool or a tool from a toolset. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message#ToolsetTool)`)` Optional. The toolset tool that got executed.  
End of mutually exclusive fields.  
  
## AgentTransfer

Represents an event indicating the transfer of a conversation to a different agent.

JSON representation  
---  
      
    
    {
      "targetAgent": string,
      "displayName": string
    }  
  
Fields  
---  
`targetAgent` |  `string` Required. The agent to which the conversation is being transferred. The agent will handle the conversation from this point forward. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`displayName` |  `string` Output only. Display name of the agent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
