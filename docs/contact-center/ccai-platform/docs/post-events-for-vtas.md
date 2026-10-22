---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/post-events-for-vtas/
title: Post events for virtual task assistants \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:57.873026+00:00
---

# Post events for virtual task assistants  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/post-events-for-vtas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Post events for virtual task assistants Stay organized with collections  Save and categorize content based on your preferences. 

The agent adapter can use the browser's [postMessage()](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) API to send events to the parent iFrame. These events can be consumed by Javascript in your parent iFrame and used to take various actions in your custom CRM implementation. To do this, your application needs to listen to the [MessageEvent](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent) in the parent window. Based on the events, your application can trigger actions such as opening a ticket tab for a specific session ID. Both the call adapter and chat adapter have specific events that can be used to enhance the CRM capabilities.

Contact Center AI Platform supports the following virtual task assistant events:

  * Virtual task assistant joined

  * Virtual task assistant left

  * Virtual task assistant custom session variables received




For a complete list of post events related to agent adapters, refer to [Agent adapters](https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm#agent_adapters).

## Virtual task assistant joined

This event is passed when the virtual task assistant joins a session.

**Data Fields**

  * `call_id`. The identifier for a voice (IVR) session.

  * `chat_id`. The identifier for a web or mobile chat session.

  * `campaign_id`: The identifier for a campaign call.

  * `campaign_name`: The name of the campaign.

  * `virtual_agent_id`: The identifier for a virtual task assistant.

  * `virtual_agent_name`: The name of the virtual task assistant.

  * `participant_id`: The participant identifier for the virtual task assistant.

  * `queue_id`: The identifier for the queue that the session originated from. This identifier is included only when the session originates from a queue.

  * `queue_path`: The path of the queue that the session originated from. This identifier is included only when the session originates from a queue.

  * `queue_language_id`: The language of the queue that the session originated from. This identifier is included only when the session originates from a queue.

  * `session_type`: The type of session—for example, messaging inbound through web chat.

  * `conversation_id`: The identifier for virtual agent sessions that use conversation profiles.

  * `session_id`: The identifier for virtual agent sessions that don't use conversation profiles.

  * `timestamp`: The date and time of an event.

  * `data_parameters`: The variables configured in the CCAI Platform portal and sent to the virtual task assistant.




**Payload sample**
    
    
    {
     "type": "Task_VA_Joined",
     "data": {
       "chat_id": 103646,
       "campaign_id": 1432,// omitted if not available
       "campaign_name": "Survey Movie", // omitted if not available
       "virtual_agent_id": 1,
       "virtual_agent_name": "name",
       "participant_id": 1,
       "queue_id": 8469, // omitted if not available
       "queue_path": "Developers / James", // omitted if not available
       "queue_language_id": "en", // omitted if not available
       "session_type": "Messaging Inbound (SMS)",
       "conversation_id": "12345",
       "session_id": "78534G4RT4284", // omitted if not available
       "timestamp": "1727853575",
       "data_parameters": {
         "param1": "one",
         "param2": "two"
       }
     }
    }
    

## Virtual task assistant left

This event is passed when the virtual task assistant leaves the session.

**Data fields**

  * `call_id`. The identifier for a voice (IVR) session.

  * `chat_id`. The identifier for a web or mobile chat session.

  * `campaign_id`: The identifier for a campaign call.

  * `campaign_name`: The name of the campaign.

  * `virtual_agent_id`: The identifier for a virtual task assistant.

  * `virtual_agent_name`: The name of the virtual task assistant.

  * `participant_id`: The participant identifier for the virtual task assistant.

  * `queue_id`: The identifier for the queue that the session originated from. This identifier is included only when the session originates from a queue.

  * `queue_path`: The path of the queue that the session originated from. This identifier is included only when the session originates from a queue.

  * `queue_language_id`: The language of the queue that the session originated from. This identifier is included only when the session originates from a queue.

  * `session_type`: The type of session—for example, messaging inbound through web chat.

  * `conversation_id`: The identifier for virtual agent sessions that use conversation profiles.

  * `session_id`: The identifier for virtual agent sessions that don't use conversation profiles.

  * `timestamp`: The date and time of an event.

  * `finish_reason`: The finish reason when the virtual agent session ends.

  * `data_parameters`: The variables configured in the CCAI Platform portal and sent to the virtual task assistant.

  * `captured_variables`: The session variables captured by the virtual task assistant.




**Payload sample**
    
    
    {
     "type": "Task_VA_Left",
     "data": {
       "chat_id": 103646,
       "campaign_id": 1432, // omitted if not available
       "campaign_name": "Survey Movie", // omitted if not available
       "virtual_agent_id": 1,
       "virtual_agent_name": "name",
       "participant_id": 1,
       "queue_id": 8469, // omitted if not available
       "queue_path": "Developers / James", // omitted if not available
       "queue_language_id": "en", // omitted if not available
       "session_type": "Messaging Inbound (SMS)",
       "conversation_id": "12345",
       "session_id": "78534G4RT4284", // omitted if not available
       "timestamp": "1727853575",
       "finish_reason": "Task VA failed", // Finish reason passed when the VTA session ends 
       "data_parameters": {
         "param1": "one",
         "param2": "two"
       },
       "captured_variables": [
         {
           "intent_name": null,
           "variables": {
               "testkey": "testvalue"
           },
           "captured_at": "2024-11-15 16:46:31 UTC",
           "timestamp": "1727853575"
         },
         {
           "intent_name": null,
           "variables": {
               "testkey2": "testvalue2"
           },
           "captured_at": "2024-11-15 16:46:31 UTC",
           "timestamp": "1727853575"
         }
       ]
     }
    }
    

## Virtual task assistant session variables received

This is be passed when the virtual task assistant sends a custom session variable payload.

**Data Fields**

  * `call_id`. The identifier for a voice (IVR) session.

  * `chat_id`. The identifier for a web or mobile chat session.

  * `campaign_id`: The identifier for a campaign call.

  * `campaign_name`: The name of the campaign.

  * `virtual_agent_id`: The identifier for a virtual task assistant.

  * `virtual_agent_name`: The name of the virtual task assistant.

  * `queue_id`: The identifier for the queue that the session originated from. This identifier is included only when the session originates from a queue.

  * `queue_path`: The path of the queue that the session originated from. This identifier is included only when the session originates from a queue.

  * `queue_language_id`: The language of the queue that the session originated from. This identifier is included only when the session originates from a queue.

  * `session_type`: The type of session—for example, messaging inbound through web chat.

  * `conversation_id`: The identifier for virtual agent sessions that use conversation profiles.

  * `session_id`: The identifier for virtual agent sessions that don't use conversation profiles.

  * `timestamp`: The date and time of an event.

  * `data_parameters`: The variables configured in the CCAI Platform portal and sent to the virtual task assistant.

  * `captured_variables`: The session variables captured by the virtual task assistant.




**Payload Sample**
    
    
    {
     "type": "Task_VA_Variables_Received",
     "data": {
       "chat_id": 103646,
       "campaign_id": 1432, // omitted if not available
       "campaign_name": "Survey Movie", // omitted if not available
       "virtual_agent_id": 1,
       "virtual_agent_name": "name",
       "participant_id": 1,
       "queue_id": 8469, // omitted if not available
       "queue_path": "Developers / James", // omitted if not available
       "queue_language_id": "en", // omitted if not available
       "session_type": "Messaging Inbound (SMS)",
       "conversation_id": "12345",
       "session_id": "78534G4RT4284", // omitted if not available
       "timestamp": "1727853575",
       "data_parameters": {
         "param1": "one",
         "param2": "two"
       },
       "captured_variables": [
         {
           "intent_name": null,
           "variables": {
               "testkey_1": "testvalue"
           },
           "captured_at": "2024-11-15 16:46:31 UTC",
           "timestamp": "1727853575"
         },
         {
           "intent_name": null,
           "variables": {
               "testkey_2": "testvalue2"
           },
           "captured_at": "2024-11-15 16:46:31 UTC",
           "timestamp" : "1727853575"
         }
       ]
     }
    }
    

## Dialogflow payload for custom session variables

The Dialogflow custom session variable payload supports virtual task assistant post events.

The properties that are available in the customer session variable payload include the following:

  * `capture_type:event`: Indicates that the values returned in the customer session variable payload must be passed in the virtual task assistant post events.

  * `capture_type:agent`: Indicates that the values returned in the customer session variable payload must be passed into the agent adapter.

  * `capture_type:comment`: Indicates that the values returned in the customer session variable payload must be passed into the CRM record as a comment. 

  * `invisible_to_adapter_events`. The values of the keys specified in this property must be excluded from the virtual task assistant post events.




**Payload sample**
    
    
    {
     "ujet": {
       "session_variable": {
         "payload": {
           "key_two": "$session.params.favfood",
           "key_three": "$session.params.budget",
           "key_one": "$session.params.location",
           "key_four": "$session.params.startdate",
           "key_five": "$session.params.enddate"
         },
         "capture_type": [
           "comment",
           "agent",
           "event"
         ],
         "capture_target": "payload",
         "invisible_to_agent": [
           "key_one",
           "key_two"
         ],
         "invisible_to_adapter_events": [
           "key_three",
           "key_two"
         ]
        }
      }
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
