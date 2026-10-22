---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-call-session-data/
title: QM call session event data \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:03.973290+00:00
---

# QM call session event data  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-call-session-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  QM call session event data Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the call session event data that Contact Center AI Platform (CCAI Platform) can export to your quality management (QM) application. For more information about integrating CCAI Platform with your QM application, see [QM and SIPREC integration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-siprec-integration).

For chat session event data, see [QM chat session event data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-chat-session-data).

## Call session events and triggers

Certain call session events trigger the export of call session data to your QM application. This section lists the call event types and the actions that trigger each one. It also includes a session event payload example for each session event type.

### Agent logs in

This event is triggered by the following actions:

  * An agent signs in to the agent adapter using the Contact Center AI Platform portal.

  * An agent signs in to the agent adapter using a CRM.




The following code sample shows the event payload:
    
    
    {
     "type" : "AgentState",
     "item" : {
      "ParticipantID" : "1234",
      "Email" : "some.email@domain.com",
      "State" : "login"
     }
    }
    

### Agent logs out

This event is triggered by the following actions:

  * An agent signs out of the agent adapter using the Contact Center AI Platform portal.

  * An agent signs our of the agent adapter using a CRM.




The following code sample shows the event payload:
    
    
    {
     "type" : "AgentState",
     "item" : {
      "ParticipantID" : "1234",
      "Email" : "some.email@domain.com",
      "State" : "logout"
     }
    }
    

### Inbound call is projected

This event is triggered when an end-user places a call to the contact center and the call is projected to an agent.

This event applies only when the call is projected for deltacast. Multicast projections don't trigger events. Only the first deltacast projection for the call in a cascade group triggers an event.

This event includes call projections received through call transfers, redirects, and deflections.

The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "ringing",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "connected"
       },
       {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "ringing"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Inbound call is answered

This event is triggered when an agent answers a projected call.

This event applies when the call is answered by an agent for both deltacast or multicast projections. This event applies for calls received and answered through call redirects and deflections.

The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "connected",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "connected"
       },
      {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "connected"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Outbound call is ringing

This event is triggered by the following actions:

  * An agent dials a new outbound call and the call is ringing for an end-user.

  * An agent dials an add-party call and the call is ringing for a third party.




The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "e9dd62bb",
      "State" : "dialing",
      "Direction" : "outgoing",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "connected"
       },
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "connected"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Outbound call is answered

This event is triggered by the following actions:

  * An end-user answers an outbound call.

  * A third party answers a add-party call.




The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "e9dd62bb",
      "State" : "connected",
      "Direction" : "outgoing",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "connected"
       },
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "connected"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Call is placed on hold

This event is triggered by the following actions:

  * An agent places a end-user on hold.

  * An agent places a third party on hold.




The following code sample shows the event payload:
    
    
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "held",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "held"
       },
      {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "connected"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Call is removed from on hold

This event is triggered by the following actions:

  * An agent removes an end-user from on hold.

  * An agent removes a third party from on hold.




The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "connected",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "connected"
       },
      {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "connected"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Cold transfer is initiated and accepted

This event is triggered by the following actions:

  * An agent places a cold transfer call to another agent and the transfer is accepted.

  * An agent places a cold transfer call to another queue and the transfer is accepted by an agent from that queue.

  * An agent cold invites another agent to a call conference and the other agent accepts and joins the call conference.




The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "transferred",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "connected"
       },
      {
        "ParticipantID" : "4321",
        "Type" : "agent",
        "State" : "connected"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Warm transfer is initiated and accepted

This event is triggered by the following actions:

  * An agent places a warm transfer call to another agent and the transfer is accepted.

  * An agent places a warm transfer call to another queue and the transfer is accepted by an agent from that queue.

  * An agent warm invites another agent to a call conference and the other other accepts and joins the call conference.




The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "conferenced",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "connected"
       },
      {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "connected"
      },
      {
        "ParticipantID" : "4321",
        "Type" : "agent",
        "State" : "connected"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Agent leaves a call conference

This event is triggered when an agent in a call conference leaves the call conference without ending it.

The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "participantDisconnect",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "connected"
       },
      {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "disconnected"
      },
      {
        "ParticipantID" : "4321",
        "Type" : "agent",
        "State" : "connected"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Call is muted

This event is triggered by the following actions:

  * An agent mutes a call.

  * An agent mutes other participants in a call.




This event applies for all calls.

The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "connected",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,\
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "connected"
       },
      {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "muted"
      },
      {
        "ParticipantID" : "4321",
        "Type" : "agent",
        "State" : "muted"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Call is unmuted

This event is triggered by the following actions:

  * An agent unmutes a call.

  * An agent unmutes other participants in a call.




This event applies for all calls.

The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "connected",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "connected"
       },
      {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "unmuted"
      },
      {
        "ParticipantID" : "4321",
        "Type" : "agent",
        "State" : "unmuted"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Call is redacted

This event is triggered when an agent redacts a call.

The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "connected",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "redacted"
       },
      {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "redacted"
      }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Call is unredacted

This event is triggered when an agent unredacts a call.

The following code sample shows the event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "connected",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "unredacted"
       },
      {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "unredacted"
      }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

### Call is ended

This event is triggered by the following actions:

  * An end-user ends a call.

  * An agent ends a call.




This event applies for all calls.

The following code sample shows the inbound call event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "846802bf90d1",
      "State" : "disconnected",
      "Direction" : "incoming",
      "Initiator" : "+123456789",
      "Queue_path_ids": "1/2/3",
      "Queue_path_names" : "support/orders/status",
      "Language" : "en",
      "Queue_uuid" : 3,
      "Recording_permitted" : true,
      "Participants" :
      [
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "disconnected"
       },
       {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "disconnected"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

The following code sample shows the outbound call event payload:
    
    
    {
     "type" : "CallState",
     "item" : {
      "CallID" : "e9dd62bb",
      "State" : "disconnected",
      "Direction" : "outgoing",
      "Initiator" : "1234",
      "Participants" :
      [
       {
        "ParticipantID" : "1234",
        "Type" : "agent",
        "State" : "disconnected"
       },
       {
        "ParticipantID" : "+123456789",
        "Type" : "external",
        "State" : "disconnected"
       }
      ],
      "MediaID" : "208188811_124248155@67.231.1.110"
     }
    }
    

## Call session event fields

The following tables describe the fields in the session data that Contact Center AI Platform exports to your QM application.

### General fields

Field name | Allowed values | Description | Effect  
---|---|---|---  
`type` | 

  * `AgentState`
  * `CallState`

| The event type of the overall JSON payload. | 

  * Passes `AgentState` for agent related events.
  * Passes `CallState` for call related events.

  
`item` |  | The object with event information. |   
  
### Agent state fields

Field name | Values | Description | Behavior  
---|---|---|---  
`ParticipantID` | An agent ID | Available in the `item` object.The agent's identifier in the Contact Center AI Platform system. | 

  * Passes the value of the ID field in the `agent_info` object in the Contact Center AI Platform session metadata.

  
`Email` | An email address | Available in the `item` object.The agent's email address. | 

  * Passes the value of the email field in the `agent_info` object in the session metadata.

  
`State` | 

  * `login`
  * `logout`

| Available in the `item` object.The agent's state at the time of the event. | 

  * Passes `login` when the agent is signed in.
  * Passes `logout` when the agent is signed out.

  
  
### Call state fields

Field name | Values | Description | Behavior  
---|---|---|---  
`CallID` | The call ID | Available in the `item` object.The call session's identifier in the Contact Center AI Platform system. | 

  * Passes the value of the ID field in the main object in the Contact Center AI Platform session metadata.

  
`State` | 

  * `dialing`
  * `waiting`
  * `ringing`
  * `connected`
  * `redirected`
  * `deflected`
  * `transferred`
  * `conferenced`
  * `disconnected`

| Available in the `item` object.The current state of the call session. | 

  * Passes `dialing` when an outbound call is in a ringing state for agent or end-user.
  * Passes `waiting` when the call is placed in the queue for projection to agents.
  * Passes `ringing` when an inbound/transferred call is in projecting state for the agent.
  * Passes `connected` when the agent or end-user is connected to the call conference.
  * Passes `redirected` when the call is automatically redirected without getting projected to agents.
  * Passes `transferred` when the call is cold-transferred from agent to another.
  * Passes `conferenced` when the call is warm-transferred from agent to another.
  * Passes `disconnected` when the agent or end-user has left the call conference.

  
`Direction` | 

  * `incoming`
  * `outgoing`

| Available in the `item` object.The direction of the call session from the contact center perspective. | 

  * Passes `incoming` when the call session is inbound.
  * Passes `outgoing` when the call session is outbound.

  
`Initiator` | 

  * The agent ID
  * The virtual agent ID
  * The end-user's phone number

| Available in the `item` object.The identifier of the party that initializes the call state. | 

  * For human agents Passes the value of the ID field in the `agent_info` object in the session metadata.


  * For virtual agents Passes the value of the `virtual_agent_id` field in the participants object in the session metadata.


  * For end-users Passes the phone number of the end-user, if available.Else, passes the value of the ID field in the `end_user` object in the session metadata.

  
`Queue_path_ids` | A path of queue IDs | Available in the `item` object.The queue path navigated by the end-user before reaching the first agent of the call.This value is constructed using the queue IDs of the navigated queue. | This applies only for incoming calls.  
`Queue_path_names` | A path of queue names | Available in the `item` object.The queue path navigated by the end-user before reaching the first agent of the call.This value is constructed using the queue names of the navigated queue. | This applies only for incoming calls.  
`Language` | The language code | Available in the `item` object.The language code of the end-user's selected language. | This applies only for incoming calls.  
`Queue_uuid` | The queue ID | Available in the `item` object.The UUID of the queue that the call reaches. | This applies only for incoming calls and queue transferred calls.  
`Recording_permitted` | A boolean | Available in the `item` object.Indicates if call recording is allowed for the specific call | 

  * Passes `true` if call recording is allowed.
  * Passes `false` if call recording is not allowed.

  
`Custom_headers` | custom headers | Available in the `item` object.This field is used to pass custom data such as SIP headers |   
`Participants` |  | This object is nested in the `item` object.An object containing the call participant's information. |   
`ParticipantID` | 

  * `agent_id`
  * `virtual_agent_id`
  * `consumer_phoneNumber`
  * `thirdParty_phoneNumber`

| Available in the `Participants` object. The identifier of the call participant. | 

  * For human agents
Passes the value of the ID field in the `agent_info` object in the Contact Center AI Platform session metadata. 

  * For virtual agents
Passes the value of the `virtual_agent_id` field in the participants object in the Contact Center AI Platform session metadata 

  * For end-users
Passes the phone number of the end-user, if available.Else, passes the value of the `id` field in the `end_user object` in the Contact Center AI Platform session metadata. 

  * For third-parties
Passes the phone number of the third-party, if available.Else, Passes the value: `null`. 
  
`Type` | 

  * `agent`
  * `external`

| Available in the `Participants` object.The type of the call participant. | 

  * Passes `agent` when the call participant is a Contact Center AI Platform agent.
  * Passes `external` when the call participant is an end-user or third-party.

  
`State` | 

  * `dialing`
  * `ringing`
  * `connected`
  * `held`
  * `disconnected`
  * `callback`
  * `deflected`
  * `transferred`
  * `redacted`
  * `unredacted`
  * `muted`
  * `unmuted`

| Available in the `Participants` object.The participant's current state in the call conference.  
| 

  * Passes `dialing` when an outbound call segment is in ringing state for the agent or end-user or third-party.
  * Passes `ringing` when an inbound or transferred call segment is in projecting state for the agent.
  * Passes `connected` when the agent or end-user or third-party is connected to the call conference.
  * Passes `held` when the end-user or third-party is put on hold in the call conference by the agent.
  * Passes `disconnected` when the agent or end-user or third-party has left the call conference.
  * Passes `redacted` when the call redaction is enabled in the agent or end-user or third-party call segment
  * Passes `unredacted` when the call redaction is disabled in the agent or end-user or third-party call segment
  * Passes `muted` when the agent is placed on mute
  * Passes `unmuted` when the agent is removed from mute

  
`MediaID` | 

  * `twilio_mediaID`
  * `nexmo_mediaID`

| Available in the `Participants` object.The identifier for call session media from the carrier. | 

  * Passes the `twilio_mediaID` when the initiator calls into or calls from a Twilio number
  * Passes the `nexmo_mediaID` when the initiator calls into or calls from a Nexmo number

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
