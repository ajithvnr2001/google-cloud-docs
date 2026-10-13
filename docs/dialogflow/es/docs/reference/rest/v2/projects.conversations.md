---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations
title: REST Resource: projects.conversations \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:32:22.203757+00:00
---

# REST Resource: projects.conversations  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.conversations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Conversation
    * JSON representation
    * LifecycleState
    * ConversationPhoneNumber
      * JSON representation
    * ConversationStage
    * TelephonyConnectionInfo
      * JSON representation
    * SipHeader
      * JSON representation
    * MimeContent
      * JSON representation
    * ContextReference
      * JSON representation
    * ContextContent
      * JSON representation
    * ContentFormat
    * UpdateMode
    * GeneratorContext
      * JSON representation
    * GeneratorType
  * Methods



## Resource: Conversation

Represents a conversation. A conversation is an interaction between an agent, including live agents and Dialogflow agents, and a support customer. Conversations can include phone calls and text-based chat sessions.

JSON representation  
---  
      
    
    {
      "name": string,
      "lifecycleState": enum ([LifecycleState](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.LifecycleState)),
      "conversationProfile": string,
      "phoneNumber": {
        object ([ConversationPhoneNumber](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ConversationPhoneNumber))
      },
      "startTime": string,
      "endTime": string,
      "conversationStage": enum ([ConversationStage](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ConversationStage)),
      "telephonyConnectionInfo": {
        object ([TelephonyConnectionInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.TelephonyConnectionInfo))
      },
      "initialConversationProfile": {
        object ([ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile))
      },
      "ingestedContextReferences": {
        string: {
          object ([ContextReference](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ContextReference))
        },
        ...
      },
      "initialGeneratorContexts": {
        string: {
          object ([GeneratorContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.GeneratorContext))
        },
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The unique identifier of this conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`lifecycleState` |  `enum (`[LifecycleState](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.LifecycleState)`)` Output only. The current state of the Conversation.  
`conversationProfile` |  `string` Required. The Conversation Profile to be used to configure this Conversation. This field cannot be updated. Format: `projects/<Project ID>/locations/<Location ID>/conversationProfiles/<Conversation Profile ID>`.  
`phoneNumber` |  `object (`[ConversationPhoneNumber](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ConversationPhoneNumber)`)` Output only. It will not be empty if the conversation is to be connected over telephony.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the conversation was started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the conversation was finished.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`conversationStage` |  `enum (`[ConversationStage](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ConversationStage)`)` Optional. The stage of a conversation. It indicates whether the virtual agent or a human agent is handling the conversation.If the conversation is created with the conversation profile that has Dialogflow config set, defaults to `[ConversationStage.VIRTUAL_AGENT_STAGE](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ConversationStage.ENUM_VALUES.VIRTUAL_AGENT_STAGE)`; Otherwise, defaults to `[ConversationStage.HUMAN_ASSIST_STAGE](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ConversationStage.ENUM_VALUES.HUMAN_ASSIST_STAGE)`.If the conversation is created with the conversation profile that has Dialogflow config set but explicitly sets conversationStage to `[ConversationStage.HUMAN_ASSIST_STAGE](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ConversationStage.ENUM_VALUES.HUMAN_ASSIST_STAGE)`, it skips `[ConversationStage.VIRTUAL_AGENT_STAGE](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ConversationStage.ENUM_VALUES.VIRTUAL_AGENT_STAGE)` stage and directly goes to `[ConversationStage.HUMAN_ASSIST_STAGE](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ConversationStage.ENUM_VALUES.HUMAN_ASSIST_STAGE)`.  
`telephonyConnectionInfo` |  `object (`[TelephonyConnectionInfo](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.TelephonyConnectionInfo)`)` Output only. The telephony connection information.  
`initialConversationProfile` |  `object (`[ConversationProfile](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversationProfiles#ConversationProfile)`)` Optional. Output only. The initial conversation profile to be used to configure this conversation, which is a copy of the conversation profile config read at conversation creation time.  
`ingestedContextReferences` |  `map (key: string, value: object (`[ContextReference](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ContextReference)`))` Output only. The context reference updates provided by external systems.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`initialGeneratorContexts` |  `map (key: string, value: object (`[GeneratorContext](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.GeneratorContext)`))` Output only. A map with generator name as key and generator context as value.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### LifecycleState

Enumeration of the completion status of the conversation.

Enums  
---  
`LIFECYCLE_STATE_UNSPECIFIED` | Unknown.  
`IN_PROGRESS` | Conversation is currently open for media analysis.  
`COMPLETED` | Conversation has been completed.  
  
### ConversationPhoneNumber

Represents a phone number for telephony integration. It allows for connecting a particular conversation over telephony.

JSON representation  
---  
      
    
    {
      "countryCode": integer,
      "phoneNumber": string
    }  
  
Fields  
---  
`countryCode` |  `integer` Output only. Desired country code for the phone number.  
`phoneNumber` |  `string` Output only. The phone number to connect to this conversation.  
  
### ConversationStage

Enumeration of the different conversation stages a conversation can be in. Reference: <https://cloud.google.com/agent-assist/docs/basics#conversation_stages>

Enums  
---  
`CONVERSATION_STAGE_UNSPECIFIED` | Unknown. Should never be used after a conversation is successfully created.  
`VIRTUAL_AGENT_STAGE` | The conversation should return virtual agent responses into the conversation.  
`HUMAN_ASSIST_STAGE` | The conversation should not provide responses, just listen and provide suggestions.  
  
### TelephonyConnectionInfo

The information about phone calls connected via phone gateway to the conversation.

JSON representation  
---  
      
    
    {
      "dialedNumber": string,
      "sdp": string,
      "sipHeaders": [
        {
          object ([SipHeader](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.SipHeader))
        }
      ],
      "extraMimeContents": [
        {
          object ([MimeContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.MimeContent))
        }
      ]
    }  
  
Fields  
---  
`dialedNumber` |  `string` Output only. The number dialed to connect this call in E.164 format.  
`sdp` |  `string` Optional. SDP of the call. It's initially the SDP answer to the incoming call, but maybe later updated for the purpose of making the link active, etc.  
`sipHeaders[]` |  `object (`[SipHeader](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.SipHeader)`)` Output only. The SIP headers from the initial SIP INVITE.  
`extraMimeContents[]` |  `object (`[MimeContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.MimeContent)`)` Output only. The mime content from the initial SIP INVITE.  
  
### SipHeader

The SIP headers from the initial SIP INVITE.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Optional. The name of the header.  
`value` |  `string` Optional. The value of the header.  
  
### MimeContent

The mime content from the initial SIP INVITE.

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "content": string
    }  
  
Fields  
---  
`mimeType` |  `string` Optional. The mime type of the content.  
`content` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Optional. The content payload.A base64-encoded string.  
  
### ContextReference

Represents a section of ingested context information.

JSON representation  
---  
      
    
    {
      "contextContents": [
        {
          object ([ContextContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ContextContent))
        }
      ],
      "updateMode": enum ([UpdateMode](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.UpdateMode)),
      "languageCode": string,
      "createTime": string
    }  
  
Fields  
---  
`contextContents[]` |  `object (`[ContextContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ContextContent)`)` Required. The list of content updates for a context reference.  
`updateMode` |  `enum (`[UpdateMode](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.UpdateMode)`)` Required. The mode in which context reference contents are updated.  
`languageCode` |  `string` Optional. The language of the information ingested, defaults to "en-US" if not set.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the context reference was first created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### ContextContent

Contents ingested.

JSON representation  
---  
      
    
    {
      "content": string,
      "contentFormat": enum ([ContentFormat](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ContentFormat)),
      "ingestionTime": string,
      "answerRecord": string
    }  
  
Fields  
---  
`content` |  `string` Required. The information ingested in a single request.  
`contentFormat` |  `enum (`[ContentFormat](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.ContentFormat)`)` Required. The format of the ingested string.  
`ingestionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when this information was incorporated into the relevant context reference.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`answerRecord` |  `string` Optional. The answer record of the tool execution result. Format: `projects/<Project ID>/locations/<Location ID>/answerRecords/<Answer Record ID>`.  
  
### ContentFormat

Represents the format of the ingested string.

Enums  
---  
`CONTENT_FORMAT_UNSPECIFIED` | Unspecified content format.  
`JSON` | Content was provided in JSON format.  
`PLAIN_TEXT` | Content was provided as plain text.  
  
### UpdateMode

Represents the mode in which context reference contents are updated.

Enums  
---  
`UPDATE_MODE_UNSPECIFIED` | Unspecified update mode.  
`APPEND` | Context content updates are applied in append mode.  
`OVERWRITE` | Context content updates are applied in overwrite mode.  
  
### GeneratorContext

Represents the context of a generator.

JSON representation  
---  
      
    
    {
      "generatorType": enum ([GeneratorType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.GeneratorType))
    }  
  
Fields  
---  
`generatorType` |  `enum (`[GeneratorType](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations#Conversation.GeneratorType)`)` Output only. The type of the generator.  
  
### GeneratorType

The available generator types.

Enums  
---  
`GENERATOR_TYPE_UNSPECIFIED` | Unspecified generator type.  
`FREE_FORM` | Free form generator type.  
`AGENT_COACHING` | Agent coaching generator type.  
`SUMMARIZATION` | Summarization generator type.  
`TRANSLATION` | Translation generator type.  
`AGENT_FEEDBACK` | Agent feedback generator type.  
`CUSTOMER_MESSAGE_GENERATION` | Customer message generation generator type.  
  
## Methods  
  
---  
  
### `[complete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations/complete)`

|  Completes the specified conversation.  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations/create)`

|  Creates a new conversation.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations/get)`

|  Retrieves the specific conversation.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.conversations/list)`

|  Returns the list of all conversations in the specified project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
