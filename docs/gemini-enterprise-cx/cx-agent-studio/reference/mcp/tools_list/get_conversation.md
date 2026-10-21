---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation/
title: MCP Tools Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:07.971175+00:00
---

# MCP Tools Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Tools Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_conversation`

Gets details of the specified conversation.

The following code sample shows how to use `curl` to call the `get_conversation` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_conversation",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `AgentService.GetConversation`.

### GetConversationRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "source": enum ([Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Input.Schema.Source))
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the conversation to retrieve.  
`source  
**(deprecated)**` |  `enum (`[Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Input.Schema.Source)`)` This item is deprecated!Optional. Indicate the source of the conversation. If not set, all source will be searched.  
  
### Source

The source of the conversation.

Enums  
---  
`SOURCE_UNSPECIFIED` | Unspecified source.  
`LIVE` | The conversation is from the live end user.  
`SIMULATOR` | The conversation is from the simulator.  
`EVAL` | The conversation is from the evaluation.  
`AGENT_TOOL` | The conversation is from an agent tool. Agent tool runs the agent in a separate session, which is persisted for testing and debugging purposes.  
  
## Output Schema

A conversation represents an interaction between an end user and the CES app.

### Conversation

JSON representation  
---  
      
    
    {
      "name": string,
      "startTime": string,
      "endTime": string,
      "turns": [
        {
          object ([Turn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Output.Schema.Turn))
        }
      ],
      "turnCount": integer,
      "channelType": enum ([ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Output.Schema.ChannelType)),
      "source": enum ([Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Input.Schema.Source)),
      "inputTypes": [
        enum ([InputType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Output.Schema.InputType))
      ],
      "entryAgent": string,
      "deployment": string,
      "appVersion": string,
      "languageCode": string,
      "messages": [
        {
          object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Message))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}`  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the conversation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the conversation was completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`turns[]` |  `object (`[Turn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Output.Schema.Turn)`)` Required. The turns in the conversation.  
`turnCount` |  `integer` Output only. The number of turns in the conversation.  
`channelType  
**(deprecated)**` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Output.Schema.ChannelType)`)` This item is deprecated!DEPRECATED. Please use `input_types` instead.  
`source` |  `enum (`[Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Input.Schema.Source)`)` Output only. Indicate the source of the conversation.  
`inputTypes[]` |  `enum (`[InputType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Output.Schema.InputType)`)` Output only. The input types of the conversation.  
`entryAgent` |  `string` Output only. The agent that initially handles the conversation. If not specified, the conversation is handled by the root agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`deployment` |  `string` Output only. The deployment of the app used for processing the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`appVersion` |  `string` Output only. The version of the app used for processing the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`languageCode` |  `string` Output only. The language code of the conversation.  
`messages[]  
**(deprecated)**` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Message)`)` This item is deprecated!Deprecated. Use turns instead.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### Turn

JSON representation  
---  
      
    
    {
      "messages": [
        {
          object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Message))
        }
      ],
      "rootSpan": {
        object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Output.Schema.Span))
      },
      "userIntendedText": string
    }  
  
Fields  
---  
`messages[]` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Message)`)` Optional. List of messages in the conversation turn, including user input, agent responses and intermediate events during the processing.  
`rootSpan` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Output.Schema.Span)`)` Optional. The root span of the action processing.  
`userIntendedText` |  `string` Optional. The intended ground-truth text from the Simulated Caller (Polysynth). Only populated when word error rate metrics are enabled.  
  
### Message

JSON representation  
---  
      
    
    {
      "role": string,
      "chunks": [
        {
          object ([Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Chunk))
        }
      ],
      "eventTime": string
    }  
  
Fields  
---  
`role` |  `string` Optional. The role within the conversation, e.g., user, agent.  
`chunks[]` |  `object (`[Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Chunk)`)` Optional. Content of the message as a series of chunks.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Timestamp when the message was sent or received. Should not be used if the message is part of an `[example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Example)`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Chunk

JSON representation  
---  
      
    
    {
    
      // Union field data can be only one of the following:
      "text": string,
      "transcript": string,
      "blob": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Blob))
      },
      "payload": {
        object
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Image))
      },
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolResponse))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AgentTransfer))
      },
      "updatedVariables": {
        object
      },
      "defaultVariables": {
        object
      }
      // End of list of possible types for union field data.
    }  
  
Fields  
---  
Union field `data`. Chunk data. `data` can be only one of the following:  
`text` |  `string` Optional. Text data.  
`transcript` |  `string` Optional. Transcript associated with the audio.  
`blob` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Blob)`)` Optional. Blob data.  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom payload data.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Image)`)` Optional. Image data.  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolCall)`)` Optional. Tool execution request.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolResponse)`)` Optional. Tool execution response.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AgentTransfer)`)` Optional. Agent transfer event.  
`updatedVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents variables that were updated in the conversation, keyed by variable names.  
`defaultVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents default variables at the start of the conversation, keyed by variable names.  
  
### Blob

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
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### Image

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
  
### ToolCall

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
    
      // Union field tool_identifier can be only one of the following:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool))
      }
      // End of list of possible types for union field tool_identifier.
    }  
  
Fields  
---  
`id` |  `string` Optional. The unique identifier of the tool call. If populated, the client should return the execution result with the matching ID in `ToolResponse`.  
`displayName` |  `string` Output only. Display name of the tool.  
`args` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The input parameters and values for the tool in JSON object format.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool)`)` Optional. The toolset tool to execute.  
  
### ToolsetTool

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
  
### ToolResponse

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
    
      // Union field tool_identifier can be only one of the following:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool))
      }
      // End of list of possible types for union field tool_identifier.
    }  
  
Fields  
---  
`id` |  `string` Optional. The matching ID of the `[tool call](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolCall)` the response is for.  
`displayName` |  `string` Output only. Display name of the tool.  
`response` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. The tool execution result in JSON object format. Use "output" key to specify tool response and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as tool execution result.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool that got executed. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool)`)` Optional. The toolset tool that got executed.  
  
### AgentTransfer

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
  
### Span

JSON representation  
---  
      
    
    {
      "name": string,
      "startTime": string,
      "endTime": string,
      "duration": string,
      "attributes": {
        object
      },
      "childSpans": [
        {
          object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Output.Schema.Span))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the span.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The start time of the span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The end time of the span.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The duration of the span.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`attributes` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. Key-value attributes associated with the span.  
`childSpans[]` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_conversation#Output.Schema.Span)`)` Output only. The child spans that are nested under this span.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### ChannelType

The channel type of the conversation.

Enums  
---  
`CHANNEL_TYPE_UNSPECIFIED` | Unspecified channel type.  
`TEXT` | The conversation only contains text messages between the end user and the agent.  
`AUDIO` | The conversation contains audio messages between the end user and the agent.  
`MULTIMODAL` | The conversation multi-modal messages (e.g. image) between the end user and the agent.  
  
### Source

The source of the conversation.

Enums  
---  
`SOURCE_UNSPECIFIED` | Unspecified source.  
`LIVE` | The conversation is from the live end user.  
`SIMULATOR` | The conversation is from the simulator.  
`EVAL` | The conversation is from the evaluation.  
`AGENT_TOOL` | The conversation is from an agent tool. Agent tool runs the agent in a separate session, which is persisted for testing and debugging purposes.  
  
### InputType

Type of the input message.

Enums  
---  
`INPUT_TYPE_UNSPECIFIED` | Unspecified input type.  
`INPUT_TYPE_TEXT` | Text input.  
`INPUT_TYPE_EVENT` | Event input.  
`INPUT_TYPE_AUDIO` | Audio input.  
`INPUT_TYPE_IMAGE` | Image input.  
`INPUT_TYPE_BLOB` | Blob input.  
`INPUT_TYPE_TOOL_RESPONSE` | Client function tool response input.  
`INPUT_TYPE_VARIABLES` | Variables input.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
