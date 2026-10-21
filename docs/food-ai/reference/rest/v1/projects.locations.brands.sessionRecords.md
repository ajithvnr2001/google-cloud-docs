---
url: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords
title: REST Resource: projects.locations.brands.sessionRecords \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:38:06.158250+00:00
---

# REST Resource: projects.locations.brands.sessionRecords  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Reference ](https://docs.cloud.google.com/food-ai/apis)



Send feedback 

#  REST Resource: projects.locations.brands.sessionRecords Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SessionRecord
    * JSON representation
  * Interaction
    * JSON representation
  * UserUtterance
    * JSON representation
  * AgentUtterance
    * JSON representation
  * ResolveOrder
    * JSON representation
  * ResolveOrderInput
    * JSON representation
  * ResolveOrderOutput
    * JSON representation
  * SubmitOrder
  * MatchIntent
    * JSON representation
  * MatchIntentInput
    * JSON representation
  * MatchIntentOutput
    * JSON representation
  * ClientExecution
    * JSON representation
  * ClientExecutionInput
    * JSON representation
  * ClientExecutionOutput
    * JSON representation
  * ClientOrderUpdate
    * JSON representation
  * UpsellAttemptRecord
    * JSON representation
  * TrafficType
  * Methods



## Resource: SessionRecord

Represents a single session record.

JSON representation  
---  
      
    
    {
      "name": string,
      "sessionStartTime": string,
      "storeId": string,
      "laneId": string,
      "interactions": [
        {
          object ([Interaction](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#Interaction))
        }
      ],
      "outcomeLabel": string,
      "outcomeGroupLabel": string,
      "audioRecordingPath": string,
      "order": {
        object ([Order](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order))
      },
      "sessionDuration": string,
      "upsellAttemptRecords": [
        {
          object ([UpsellAttemptRecord](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#UpsellAttemptRecord))
        }
      ],
      "audioRecording": string,
      "trafficType": enum ([TrafficType](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#TrafficType)),
      "channelType": enum ([ChannelType](https://docs.cloud.google.com/food-ai/reference/rest/v1/ChannelType))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the SessionRecord. Format: projects/{project}/locations/{location}/brands/{brand}/sessionRecords/{sessionRecord}  
`sessionStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the session started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`storeId` |  `string` Immutable. The ID of the store where the order was placed.  
`laneId` |  `string` Immutable. The lane ID of the order session.  
`interactions[]` |  `object (`[Interaction](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#Interaction)`)` Output only. The conversation turns.  
`outcomeLabel` |  `string` Output only. The final outcome label of the order.  
`outcomeGroupLabel` |  `string` Output only. The group label for the outcome.  
`audioRecordingPath` |  `string` Output only. Path to the full audio recording.  
`order` |  `object (`[Order](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order)`)` Output only. The order associated with the session record.  
`sessionDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. Total duration of the session.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`upsellAttemptRecords[]` |  `object (`[UpsellAttemptRecord](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#UpsellAttemptRecord)`)` Output only. Upsells performed during the session.  
`audioRecording` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. Audio recording for the session. This field is only populated when calling sessionRecords.get.A base64-encoded string.  
`trafficType` |  `enum (`[TrafficType](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#TrafficType)`)` Output only. The traffic type for the session.  
`channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/food-ai/reference/rest/v1/ChannelType)`)` Output only. The type of channel used for the session (e.g. drive-through, mobile app, phone call).  
  
## Interaction

Represents a single interaction in a turn in the conversation.

JSON representation  
---  
      
    
    {
      "turnPosition": string,
    
      // Union field interaction can be only one of the following:
      "userUtterance": {
        object ([UserUtterance](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#UserUtterance))
      },
      "agentUtterance": {
        object ([AgentUtterance](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#AgentUtterance))
      },
      "resolveOrder": {
        object ([ResolveOrder](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrder))
      },
      "submitOrder": {
        object ([SubmitOrder](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#SubmitOrder))
      },
      "matchIntent": {
        object ([MatchIntent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntent))
      },
      "clientExecution": {
        object ([ClientExecution](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecution))
      },
      "clientOrderUpdate": {
        object ([ClientOrderUpdate](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ClientOrderUpdate))
      }
      // End of list of possible types for union field interaction.
    }  
  
Fields  
---  
`turnPosition` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Turn position in the conversation.  
Union field `interaction`. The type of interaction. `interaction` can be only one of the following:  
`userUtterance` |  `object (`[UserUtterance](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#UserUtterance)`)` User utterance.  
`agentUtterance` |  `object (`[AgentUtterance](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#AgentUtterance)`)` Agent utterance.  
`resolveOrder` |  `object (`[ResolveOrder](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrder)`)` ResolveOrder call performed by the agent  
`submitOrder` |  `object (`[SubmitOrder](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#SubmitOrder)`)` SubmitOrder call performed by the agent  
`matchIntent` |  `object (`[MatchIntent](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntent)`)` MatchIntent call performed by the agent  
`clientExecution` |  `object (`[ClientExecution](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecution)`)` ClientExecution call performed by the agent  
`clientOrderUpdate` |  `object (`[ClientOrderUpdate](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ClientOrderUpdate)`)` Client-initiated order state update  
  
## UserUtterance

The user utterance.

JSON representation  
---  
      
    
    {
      "text": string,
      "createTime": string
    }  
  
Fields  
---  
`text` |  `string` The text of the user utterance.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the user utterance occurred.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## AgentUtterance

The agent utterance.

JSON representation  
---  
      
    
    {
      "text": string,
      "createTime": string
    }  
  
Fields  
---  
`text` |  `string` The text of the agent utterance.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the agent utterance occurred.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ResolveOrder

The resolve order interaction.

JSON representation  
---  
      
    
    {
      "input": {
        object ([ResolveOrderInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrderInput))
      },
      "output": {
        object ([ResolveOrderOutput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrderOutput))
      }
    }  
  
Fields  
---  
`input` |  `object (`[ResolveOrderInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrderInput)`)` The input for the resolve order action.  
`output` |  `object (`[ResolveOrderOutput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ResolveOrderOutput)`)` The output for the resolve order action.  
  
## ResolveOrderInput

The input for the resolve order interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the resolve order interaction.  
  
## ResolveOrderOutput

The output for the resolve order interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the resolve order interaction output.  
  
## SubmitOrder

This type has no fields.

The submit order interaction.

## MatchIntent

The match intent interaction.

JSON representation  
---  
      
    
    {
      "input": {
        object ([MatchIntentInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntentInput))
      },
      "output": {
        object ([MatchIntentOutput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntentOutput))
      }
    }  
  
Fields  
---  
`input` |  `object (`[MatchIntentInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntentInput)`)` The input for the match intent interaction.  
`output` |  `object (`[MatchIntentOutput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#MatchIntentOutput)`)` The output for the match intent interaction.  
  
## MatchIntentInput

The input for the match intent interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the match intent interaction input.  
  
## MatchIntentOutput

The output for the match intent interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the match intent interaction output.  
  
## ClientExecution

The client execution interaction.

JSON representation  
---  
      
    
    {
      "toolName": string,
      "input": {
        object ([ClientExecutionInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecutionInput))
      },
      "output": {
        object ([ClientExecutionOutput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecutionOutput))
      }
    }  
  
Fields  
---  
`toolName` |  `string` The tool name for the client execution interaction.  
`input` |  `object (`[ClientExecutionInput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecutionInput)`)` The input for the client execution interaction.  
`output` |  `object (`[ClientExecutionOutput](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords#ClientExecutionOutput)`)` The output for the client execution interaction.  
  
## ClientExecutionInput

The input for the client execution interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the client execution interaction input.  
  
## ClientExecutionOutput

The output for the client execution interaction.

JSON representation  
---  
      
    
    {
      "payload": {
        object
      }
    }  
  
Fields  
---  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The payload for the client execution interaction output.  
  
## ClientOrderUpdate

Client-initiated order state update.

JSON representation  
---  
      
    
    {
      "order": {
        object ([Order](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order))
      }
    }  
  
Fields  
---  
`order` |  `object (`[Order](https://docs.cloud.google.com/food-ai/reference/rest/v1/Order)`)` An order state update sent by the client.  
  
## UpsellAttemptRecord

Represents an upsell attempt. This data is used to display upsell information in the console order history, namely upsell type, turn id, and whether the upsell was accepted, and is populated from Spanner based on processed logs.

JSON representation  
---  
      
    
    {
      "turnId": integer,
      "upsellType": string,
      "accepted": boolean
    }  
  
Fields  
---  
`turnId` |  `integer` Output only. ID of the turn in which the upsell opportunity occurred.  
`upsellType` |  `string` Output only. The type of upsell event.  
`accepted` |  `boolean` Output only. Whether the upsell was accepted.  
  
## TrafficType

The traffic type for the session. This is used to label the monitoring, logging, and observability metrics.

Enums  
---  
`TRAFFIC_TYPE_UNSPECIFIED` | The traffic type is not specified.  
`EXTERNAL` | The traffic is from an external client.  
`INTEGRATION_TEST` | The traffic is from an integration test.  
`EVAL` | The traffic is from the eval tool.  
`PROBER` | The traffic is from the prober.  
`MANUAL_TEST` | The traffic is from manual testing.  
`INTERNAL_TOOL` | The traffic is from an internal tool.  
`CONSOLE` | The traffic is from the food AI console.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords/delete)`

|  Deletes an SessionRecord.  
  
### `[get](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords/get)`

|  Gets a specific SessionRecord.  
  
### `[list](https://docs.cloud.google.com/food-ai/reference/rest/v1/projects.locations.brands.sessionRecords/list)`

|  Lists SessionRecords for a given brand.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-21 UTC."],[],[]] 
