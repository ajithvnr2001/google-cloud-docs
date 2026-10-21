---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations
title: REST Resource: projects.locations.apps.conversations \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:30.536310+00:00
---

# REST Resource: projects.locations.apps.conversations  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.conversations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Conversation
    * JSON representation
  * Conversation.Turn
    * JSON representation
  * Span
    * JSON representation
  * Conversation.ChannelType
  * Conversation.Source
  * Conversation.InputType
  * Methods



## Resource: Conversation

A conversation represents an interaction between an end user and the CES app.

JSON representation  
---  
      
    
    {
      "name": string,
      "startTime": string,
      "endTime": string,
      "turns": [
        {
          object ([Conversation.Turn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Conversation.Turn))
        }
      ],
      "turnCount": integer,
      "channelType": enum ([Conversation.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Conversation.ChannelType)),
      "source": enum ([Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Conversation.Source)),
      "inputTypes": [
        enum ([Conversation.InputType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Conversation.InputType))
      ],
      "entryAgent": string,
      "deployment": string,
      "appVersion": string,
      "languageCode": string,
      "messages": [
        {
          object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/conversations/{conversation}`  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the conversation was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the conversation was completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`turns[]` |  `object (`[Conversation.Turn](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Conversation.Turn)`)` Required. The turns in the conversation.  
`turnCount` |  `integer` Output only. The number of turns in the conversation.  
`channelType  
**(deprecated)**` |  `enum (`[Conversation.ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Conversation.ChannelType)`)` This item is deprecated!DEPRECATED. Please use `[inputTypes](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Conversation.FIELDS.input_types)` instead.  
`source` |  `enum (`[Conversation.Source](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Conversation.Source)`)` Output only. Indicate the source of the conversation.  
`inputTypes[]` |  `enum (`[Conversation.InputType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Conversation.InputType)`)` Output only. The input types of the conversation.  
`entryAgent` |  `string` Output only. The agent that initially handles the conversation. If not specified, the conversation is handled by the root agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`deployment` |  `string` Output only. The deployment of the app used for processing the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/deployments/{deployment}`  
`appVersion` |  `string` Output only. The version of the app used for processing the conversation. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`languageCode` |  `string` Output only. The language code of the conversation.  
`messages[]  
**(deprecated)**` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message)`)` This item is deprecated!Deprecated. Use turns instead.  
  
## Conversation.Turn

All information about a single turn in the conversation.

JSON representation  
---  
      
    
    {
      "messages": [
        {
          object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message))
        }
      ],
      "rootSpan": {
        object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Span))
      },
      "userIntendedText": string
    }  
  
Fields  
---  
`messages[]` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Message)`)` Optional. List of messages in the conversation turn, including user input, agent responses and intermediate events during the processing.  
`rootSpan` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Span)`)` Optional. The root span of the action processing.  
`userIntendedText` |  `string` Optional. The intended ground-truth text from the Simulated Caller (Polysynth). Only populated when word error rate metrics are enabled.  
  
## Span

A span is a unit of work or a single operation during the request processing.

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
          object ([Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Span))
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
`childSpans[]` |  `object (`[Span](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations#Span)`)` Output only. The child spans that are nested under this span.  
  
## Conversation.ChannelType

The channel type of the conversation.

Enums  
---  
`CHANNEL_TYPE_UNSPECIFIED` | Unspecified channel type.  
`TEXT` | The conversation only contains text messages between the end user and the agent.  
`AUDIO` | The conversation contains audio messages between the end user and the agent.  
`MULTIMODAL` | The conversation multi-modal messages (e.g. image) between the end user and the agent.  
  
## Conversation.Source

The source of the conversation.

Enums  
---  
`SOURCE_UNSPECIFIED` | Unspecified source.  
`LIVE` | The conversation is from the live end user.  
`SIMULATOR` | The conversation is from the simulator.  
`EVAL` | The conversation is from the evaluation.  
`AGENT_TOOL` | The conversation is from an agent tool. Agent tool runs the agent in a separate session, which is persisted for testing and debugging purposes.  
  
## Conversation.InputType

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
  
## Methods  
  
---  
  
### `[batchDelete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations/batchDelete)`

|  Batch deletes the specified conversations.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations/delete)`

|  Deletes the specified conversation.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations/get)`

|  Gets details of the specified conversation.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.conversations/list)`

|  Lists conversations in the given app.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-29 UTC."],[],[]] 
