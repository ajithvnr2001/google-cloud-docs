---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-chat-session-data/
title: QM chat session event data \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:52.537635+00:00
---

# QM chat session event data  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-chat-session-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  QM chat session event data Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the chat session event data that Contact Center AI Platform (CCAI Platform) can export to your quality management (QM) application. QM chat event data supports the web SDK and the mobile SDKs. For more information about integrating CCAI Platform with your QM application, see [QM and SIPREC integration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-siprec-integration).

For call session event data, see [QM call session event data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-call-session-data).

## Chat session events and triggers

Certain session events trigger the export of chat session data to your QM application. This section lists the chat event types and includes a session event payload example for each one.

### Chat started

This event is triggered when a human agent or a virtual agent starts a chat. The event payload contains the initial state of the chat, including information about the queue, participants, and the initiator.

The following code sample shows the event payload:
    
    
    {
      "queue_path_ids": "7/26",
      "queue_path_names": "Test/calls",
      "language": "en",
      "support_number": null,
      "session_type_v2": "In-web",
      "chat_id": 138,
      "state": "waiting",
      "direction": "incoming",
      "initiator": "end_user_5",
      "participants": [
        {
          "state": "connected",
          "type": "external",
          "dn": "end_user_5"
        }
      ]
    }
    

### Chat waiting for assignment

This event is triggered when a chat session enters a queue and is waiting for assignment.

The following code sample shows the event payload:
    
    
    {
      "queue_path_ids": "7/23",
      "queue_path_names": "Test/virtual",
      "language": "en",
      "session_type_v2": "In-web",
      "chat_id": 196,
      "state": "waiting",
      "direction": "incoming",
      "initiator": "end_user_5",
      "participants": [
        {
          "state": "connected",
          "type": "external",
          "dn": "end_user_5"
        }
      ]
    }
    

### Chat accepted

This event is triggered when a human agent or a virtual agent accepts a chat. This is an optional, intermediate event before an agent connects with a chat.

The following code sample shows an event payload for a human agent:
    
    
    {
      "queue_path_ids": "7/26",
      "queue_path_names": "Test/calls",
      "language": "en",
      "session_type_v2": "In-web",
      "chat_id": 167,
      "state": "connected",
      "direction": "incoming",
      "initiator": "agent_1",
      "participants": [
        {
          "state": "connected",
          "type": "external",
          "media_id": "MB0d0540e638354714a43d64e9be9677b6",
          "dn": "end_user_5"
        },
        {
          "state": "accepted",
          "type": "agent",
          "media_id": "MBd9670cb0cddd424c814194795527ae3a",
          "agent_number": "Uno numero",
          "name": "Admin UJET",
          "alias": "super_agent",
          "dn": "agent_1"
        }
      ]
    }
    

The following code sample shows an event payload for a virtual agent:
    
    
    {
      "queue_path_ids": "7/23",
      "queue_path_names": "Test/virtual",
      "language": "en",
      "session_type_v2": "In-web",
      "chat_id": 196,
      "state": "connected",
      "direction": "incoming",
      "initiator": "virtual_agent_2",
      "participants": [
        {
          "state": "connected",
          "type": "external",
          "media_id": "MBdfcdab9220f94f1486008a165db3f31a",
          "dn": "end_user_5"
        },
        {
          "state": "accepted",
          "type": "virtual_agent",
          "media_id": "MBea10421d150b4d22b675de17070bc383",
          "dn": "virtual_agent_2"
        }
      ]
    }
    

### Chat connected

This event is triggered when a chat is connected to a human agent or a virtual agent. This can be an auto-connection or a human agent manually connecting.

The following code sample shows an event payload for a human agent:
    
    
    {
      "queue_path_ids": "7/26",
      "queue_path_names": "Test/calls",
      "language": "en",
      "session_type_v2": "In-web",
      "chat_id": 114,
      "state": "connected",
      "direction": "incoming",
      "initiator": "end_user_5",
      "participants": [
        {
          "state": "connected",
          "type": "external",
          "media_id": "MB7a504ce7f418447bb4a48b8f3fa609d0",
          "dn": "end_user_5"
        },
        {
          "state": "connected",
          "type": "agent",
          "agent_number": "Uno numero",
          "name": "Admin UJET",
          "alias": "super_agent",
          "dn": "agent_1"
        }
      ]
    }
    

The following code sample shows an event payload for a virtual agent:
    
    
    {
      "queue_path_ids": "7/23",
      "queue_path_names": "Test/virtual",
      "language": "en",
      "session_type_v2": "In-web",
      "chat_id": 196,
      "state": "connected",
      "direction": "incoming",
      "initiator": "virtual_agent_2",
      "participants": [
        {
          "state": "connected",
          "type": "external",
          "dn": "end_user_5"
        },
        {
          "state": "connected",
          "type": "virtual_agent",
          "dn": "virtual_agent_2"
        }
      ],
      "connected_at": "2024-09-13T14:04:17.000-07:00"
    }
    

### Chat dismissed

This event is triggered when a chat session is canceled or terminated before a full connection is established—for example, it wasn't accepted or it ended prematurely.

The following code sample shows the event payload:
    
    
    {
      "queue_path_ids": "7/26",
      "queue_path_names": "Test/calls",
      "language": "en",
      "session_type_v2": "In-web",
      "chat_id": 197,
      "state": "dismissed",
      "direction": "incoming",
      "initiator": "agent_1",
      "participants": [
        {
          "state": "dismissed",
          "type": "external",
          "media_id": "MB444f542e9b9c4f89a8369bb2430357ad",
          "dn": "end_user_5"
        },
        {
          "state": "dismissed",
          "type": "agent",
          "media_id": "MB7e657411b2284f95b2cf31ef5e6dc83c",
          "agent_number": "Uno numero",
          "name": "Admin UJET",
          "alias": "super_agent",
          "dn": "agent_1"
        }
      ]
    }
    

### Chat resumed

This event is triggered when a previously paused or suspended chat session is resumed. The payload contains the state of the chat when it's resumed.

The following code sample shows the event payload:
    
    
    {
      "session_type_v2": "In-web",
      "chat_id": 198,
      "state": "resumed",
      "direction": "incoming",
      "initiator": "end_user_5",
      "participants": [
        {
          "state": "resumed",
          "type": "external",
          "media_id": "MB320da61121bc4fc48ea099759f679333",
          "dn": "end_user_5"
        },
        {
          "state": "resumed",
          "type": "agent",
          "media_id": "MBbe5db89a01ab4814a8e7830daf3d30fa",
          "agent_number": "Uno numero",
          "name": "Admin UJET",
          "alias": "super_agent",
          "dn": "agent_1"
        }
      ]
    }
    

### Participant left the chat

This event is triggered when one or more participants leave a chat session. This can be an end-user, a human agent, or a virtual agent leaving the chat. The payload contains the state of the chat when the participants left it.

The following code sample shows the event payload for an end-user leaving a chat:
    
    
    {
      "session_type_v2": "In-web",
      "chat_id": 169,
      "state": "participantDisconnect",
      "direction": "incoming",
      "initiator": "end_user_5",
      "participants": [
        {
          "state": "disconnected",
          "type": "external",
          "media_id": "MB4dd73370bc564cf18f5347233523ef44",
          "dn": "end_user_5"
        },
        {
          "state": "disconnected",
          "type": "agent",
          "media_id": "MBba370f84cf914992b05e9aab03730c4b",
          "agent_number": "Uno numero",
          "name": "Admin UJET",
          "alias": "super_agent",
          "dn": "agent_1"
        }
      ]
    }
    

The following code sample shows the event payload for a human agent leaving a chat:
    
    
    {
      "queue_path_ids": "7/26",
      "queue_path_names": "Test/calls",
      "language": "en",
      "session_type_v2": "In-web",
      "chat_id": 169,
      "state": "participantDisconnect",
      "direction": "incoming",
      "initiator": "agent_1",
      "participants": [
        {
          "state": "connected",
          "type": "external",
          "media_id": "MB4dd73370bc564cf18f5347233523ef44",
          "dn": "end_user_5"
        },
        {
          "state": "disconnected",
          "type": "agent"
          "media_id": "MBba370f84cf914992b05e9aab03730c4b",
          "agent_number": "Uno numero",
          "name": "Admin UJET",
          "alias": "super_agent",
          "dn": "agent_1"
        }
      ]
    }
    

The following code sample shows the event payload for a virtual agent leaving a chat:
    
    
    {
      "queue_path_ids": "7/23",
      "queue_path_names": "Test/virtual",
      "language": "en",
      "session_type_v2": "In-web",
      "chat_id": 196,
      "state": "participantDisconnect",
      "direction": "incoming",
      "initiator": "virtual_agent_2",
      "participants": [
        {
          "state": "disconnected",
          "type": "external",
          "media_id": "MBdfcdab9220f94f1486008a165db3f31a",
          "dn": "end_user_5"
        },
        {
          "state": "disconnected",
          "type": "virtual_agent",
          "media_id": "MBea10421d150b4d22b675de17070bc383",
          "dn": "virtual_agent_2"
        }
      ]
    }
    

### Chat ended

This event is triggered when a chat session ends. This can be an end-user, a human agent, or a virtual agent ending the chat. The payload contains the state of the chat when it ends, including the participants and the timestamps for when the chat connected and ended.

The following code sample shows the event payload for a human agent and end-user leaving a chat:
    
    
    {
      "queue_path_ids": "7/26",
      "queue_path_names": "Test/calls",
      "language": "en",
      "support_number": null,
      "session_type_v2": "In-web",
      "chat_id": 127,
      "state": "disconnected",
      "direction": "incoming",
      "initiator": "end_user_5",
      "participants": [
        {
          "state": "disconnected",
          "type": "external",
          "media_id": "MB4a0a435e759c43369098ee7f2d0271f0",
          "dn": "end_user_5"
        },
        {
          "state": "disconnected",
          "type": "agent",
          "media_id": "MBa4afeafb5bcc4a279f51db76f3b98deb",
          "agent_number": "Uno numero",
          "name": "Admin UJET",
          "alias": "super_agent",
          "dn": "agent_1"
        }
      ],
      "connected_at": "2024-08-27T17:06:37.000-07:00",
      "ends_at": "2024-08-27T17:06:59.000-07:00"
    }
    

The following code sample shows the event payload for a virtual agent and end-user leaving a chat:
    
    
    {
      "queue_path_ids": "7/23",
      "queue_path_names": "Test/virtual",
      "language": "en",
      "session_type_v2": "In-web",
      "chat_id": 190,
      "state": "disconnected",
      "direction": "incoming",
      "initiator": "end_user_5",
      "participants": [
        {
          "state": "disconnected",
          "type": "external",
          "media_id": "MB6ea6204b6a0448428d88e9976fd856d4",
          "dn": "end_user_5"
        },
        {
          "state": "disconnected",
          "type": "virtual_agent",
          "media_id": "MBc6a2b72c99534a68990caf622b65571a",
          "dn": "virtual_agent_2"
        }
      ],
      "connected_at": "2024-09-12T10:50:51.000-07:00",
      "ends_at": "2024-09-12T11:54:08.000-07:00"
    }
    

The following code sample shows the event payload for a chat ended while waiting in queue:
    
    
    {
      "queue_path_ids": "7/26",
      "queue_path_names": "Test/calls",
      "language": "en",
      "support_number": null,
      "session_type_v2": "In-web",
      "chat_id": 141,
      "state": "disconnected",
      "direction": "incoming",
      "initiator": "end_user_5",
      "participants": [
        {
          "state": "disconnected",
          "type": "external",
          "media_id": "MB65670b2c44534af3860fad35be88ac41",
          "dn": "end_user_5"
        }
      ],
      "connected_at": "",
      "ends_at": "2024-08-29T14:41:16.000-07:00"
    }
    

## Chat session event fields

The following tables describe the fields in the session data that Contact Center AI Platform exports to your QM application.

### General fields

**Field name** | **Values** | **Description** | **Condition**  
---|---|---|---  
`type` | 

  * `AgentState`
  * `ChatState`

| The event type of the overall JSON payload. | 

  * Passes `AgentState` for agent related events.
  * Passes `ChatState` for chat related events.

  
`item` |  | The object with event information. |   
  
### Chat state fields

**Field Name** | **Values** | **Description** | **Condition**  
---|---|---|---  
`chat_id` | 

  * The chat ID

| Available in the `item` object.The chat session's identifier in the Contact Center AI Platform system. | 

  * Passes the value of the ID field in the main object in the Contact Center AI Platform session metadata.

  
`state` | 

  * `waiting`
  * `connected`
  * `disconnected`
  * `dismissed`
  * `resumed`
  * `participantDisconnect`
  * `transferred`

| Available in the `item` object.The current state of the chat session. |   
`direction` | 

  * `incoming`

| Available in the `item` object.The direction of the chat session from the contact center perspective. | 

  * Passes `incoming` when the chat session is inbound.

  
`initiator` | 

  * `agent_1`
  * `virtual_agent_2`
  * `end_user_5`

| Available in the `item` object.The identifier of the party that initializes the chat state. | 

  * For human agents Passes the value of the ID field in the `agent_info` object in the session metadata.


  * For virtual agents Passes the value of the `virtual_agent_id` field in the `participants` object in the session metadata.


  * For end-users Passes the value of the ID field in the `end_user` object in the session metadata.

  
`queue_path_ids` | 

  * A path of queue IDs

| Available in the `item` object.The queue path navigated by the end-user before reaching the first agent of the call.This value is constructed using the queue IDs of the navigated queue. | 

  * This applies only to incoming chats.

  
`queue_path_names` | 

  * A path of queue names

| Available in the `item` object.The queue path navigated by the end-user before reaching the first agent of the call.This value is constructed using the queue names of the navigated queue. | 

  * This applies only to incoming chats.

  
`language` | 

  * The language code

| Available in the `item` object.The language code of the end-user's selected language. | 

  * This applies only to incoming chats.

  
`queue_uuid` | 

  * The queue ID

| Available in the `item` object.The UUID of the queue that the chat has been routed to. | 

  * This applies only to incoming and queue transferred chats.

  
`tenant` | 

  * The instance name

| Available in the `item` object.The name of the instance hosting the chat. |   
`event_id` | 

  * The event ID

| Available in the `item` object.An identifier for the chat session. |   
`timestamp` | 

  * A UNIX timestamp

| Available in the `item` object.A timestamp for the chat in Unix epoch time |   
`session_type_v2` | 

  * `In-web`

| Available in the `item` object.Indicates a web SDK chat session. |   
`support_number` | 

  * NULL

|  | 

  * Not applicable for chat.

  
`connected_at` | 

  * The date and time

| Available in the `item` object.The date and time the chat session began. |   
`ends_at` | 

  * The date and time

| Available in the `item` object.The date and time the chat session ended. |   
`participants` |  | Available in the `item` object.An object containing the call participant's information. |   
`participant_id` | 

  * `agent_id`
  * `virtual_agent_id`

| Available in the `participants` object.The identifier of the chat participant. | 

  * For human agents Passes the value of the ID field in the `agent_info` object in the session metadata.


  * For virtual agents Passes the value in the `virtual_agent_id` field in the `participants` object in the session metadata


  * For end-users Passes the value of the ID field in the `end_user` object in the session metadata.


  * For third-parties Passes the phone number of the third-party, if available. Else, passes the `null` value.

  
`type` | 

  * `external`
  * `agent`
  * `virtual_agent`

| Available in the `participants` object.The type of the call participant. | 

  * Passes `agent` when the chat participant is an agent.
  * Passes `external` when the chat participant is an end-user or a third-party.
  * Passes `virtual_agent` when the chat participant is a virtual agent.

  
`state` | 

  * `connected`
  * `disconnected`
  * `accepted`
  * `dismissed`
  * `resumed`

| Available in the `participants` object.The participant's current state in the chat conference.  
|   
`media_id` | 

  * `twilio_mediaID`
  * `nexmo_mediaID`

| Available in the `participants` object.The identifier for chat session media from the carrier. | 

  * Passes the `twilio_mediaID` when the initiator chats into or chats from a Twilio number.
  * Passes the `nexmo_mediaID` when the initiator chats into or chats from a Nexmo number.

  
`dn` | 

  * `end_user_1`
  * `agent_1`

| Available in the `participants` object.The directory number of the participant. |   
`agent_number` |  | Available in the `participants` object. The agent's number. |   
`name` |  | Available in the `participants` object. The agent's name. |   
`alias` |  | Available in the `participants` object. The agent's alias. |   
  
## Chat session transfers

Chat session transfers are not distinct chat events. Rather, they are payloads that indicate that a chat session transfer has occurred. This section shows a chat session transfer payload that's triggered when an agent leaves a chat. In this example, the `initiator` field value is `agent_1`, indicating that agent 1 initiated the transfer. In the `participants` array, `agent_1` has a state of `disconnected` and `agent_2` has a state of `connected`. This indicates that the session has been transferred from agent 1 to agent 2, with agent 1 leaving the chat and agent 2 joining. The value of the overall `state` field in this example is `participantDisconnect`, but you could model your system to have an overall state of `transferred` or `connected` if you prefer. You could also model your system to have additional fields to more explicitly represent a session transfer—for example, `transfer_id` or a dedicated transfer event type.

The following code sample show an event payload for a session transfer:
    
    
    {
      "queue_path_ids": "7/26",
      "queue_path_names": "Test/calls",
      "language": "en",
      "session_type_v2": "In-web",
      "chat_id": 208,
      "state": "participantDisconnect",
      "direction": "incoming",
      "initiator": "agent_1",
      "participants": [
        {
          "state": "connected",
          "type": "external",
          "media_id": "MBed9193af0a82486cbad069925b5a0b18",
          "dn": "end_user_5"
        },
        {
          "state": "disconnected",
          "type": "agent",
          "media_id": "MB05685c80e6af444faa1de5c5e48a26c7",
          "agent_number": "Uno numero",
          "name": "Admin UJET",
          "alias": "super_agent",
          "dn": "agent_1"
        },
        {
          "state": "connected",
          "type": "agent",
          "media_id": "MB5caad80c7d94477d9db9c5f1c3662768",
          "agent_number": "420",
          "name": "ajay1 ujet",
          "alias": "ajay1-alias",
          "dn": "agent_2"
        }
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
