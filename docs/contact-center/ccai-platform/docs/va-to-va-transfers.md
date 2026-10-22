---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-to-va-transfers/
title: Virtual agent to virtual agent transfers \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:59.116723+00:00
---

# Virtual agent to virtual agent transfers  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-to-va-transfers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Virtual agent to virtual agent transfers Stay organized with collections  Save and categorize content based on your preferences. 

With Contact Center AI Platform, a virtual agent can transfer a chat session to another virtual agent without intervention by a human agent. This improves scalability for complex multi-flow virtual agent designs. Virtual agent to virtual agent transfers don't work with deflections.

The following two types of virtual agent to virtual agent transfers are available:

  * By queue: routes a session to the queue that the destination virtual agent is assigned to

  * By direct transfer: routes a session directly to a destination virtual agent




## Terminology

The following list defines terms used in virtual agent to virtual agent transfers.

  * **Support virtual agent** : A virtual agent that can handle support cases and other complex use cases, similar to a human agent. This is often just called a virtual agent. For more information, see [About virtual agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent).

  * **Virtual task assistant** : A virtual agent that performs simpler, repetitive tasks. For more information, see [Create virtual task assistants](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-task-assistants).

  * **Transfer** : The reassignment of an agent handling a session.

  * **Session variables** : Variables from intent and end-user responses. Session variables are stored for a session and persist until the session ends.

  * **Data parameters** : Parameters passed to a virtual agent when a session starts.




## Virtual agent to virtual agent transfers by queue

You can transfer a chat session from one virtual agent to another by routing the session to the queue that the destination virtual agent is assigned to. The following transfer types are supported for virtual agent to virtual agent transfers by queue:

  * Support virtual agent to support virtual agent

  * Virtual task assistant to support virtual agent




### Custom payload

You configure virtual agents to transfer chat sessions to other virtual agents using custom payloads. For more information, see [Virtual agent custom payloads](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload).

The following is an example of a custom payload for a virtual agent to virtual agent transfer by queue:
    
    
    {
      "ujet": {
        "type": "action",
        "action": "escalation",
        "escalation_reason": "by_virtual_agent",
        "allow_virtual_agent": true,
        "menu_id": QUEUE_ID,
        "language": LANGUAGE
      }
    }
    

Replace the following:

  * `QUEUE_ID`: the ID of the queue that the chat session is transferred to

  * `LANGUAGE`: the two-letter language code for the destination virtual agent's language




#### Pass session data

If you want to pass session data from the source virtual agent to the destination virtual agent, include the `session_variable` property in your custom payload.

The following is an example of the `session_variable` property:
    
    
    "session_variable": {
      "capture_target": "payload",
      "capture_type": ["data_parameters"],
      "payload": {
        "value_one": "$session.params.payload_value_one",
        "value_two": "$session.params.payload_value_two"
      }
    }
    

When the virtual agent triggers the custom payload, the chat session is routed to the virtual agent assigned to the specified queue, if that virtual agent is available. The source virtual agent leaves the chat and the destination virtual agent joins. A transfer message is displayed to the end-user unless transfer messages are hidden.

If the transfer fails, the end-user is transferred to a human agent assigned to the same queue. If there are no human agents assigned to the queue or no human agents are available, the chat ends.

## Virtual agent to virtual agent direct transfer

You can transfer a chat session by routing it directly to a destination virtual agent. The following transfer types are supported for virtual agent to virtual agent direct transfers:

  * Support virtual agent to support virtual agent

  * Support virtual agent to virtual task assistant

  * Virtual task assistant to virtual task assistant

  * Virtual task assistant to support virtual agent




### Get the agent ID for a virtual agent

To create a custom payload for a virtual agent to virtual agent direct transfer, you need the agent ID for the destination virtual agent.

To get the agent ID for a virtual agent, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Virtual Agent**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Virtual Agents** pane, click edit **Edit** next to the virtual agent that you want. An editing dialog for the virtual agent appears. The agent ID is the number after the final slash in the page's URL.




### Custom payload

You configure virtual agents to transfer chat sessions to other virtual agents using custom payloads. For more information, see [Virtual agent custom payloads](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload).

The following is an example of a custom payload for a virtual agent to virtual agent direct transfer:
    
    
    {
      "ujet": {
        "type": "action",
        "action": "direct",
        "escalation_reason": "by_virtual_agent",
        "allow_virtual_agent": true,
        "agent_id": AGENT_ID,
        "language": "LANGUAGE"
      }
    }
    

Replace the following:

  * `AGENT_ID`: the ID of the virtual agent that the chat session is transferred to. To get the agent ID, see Get the agent ID for a virtual agent.

  * `LANGUAGE`: The two-letter language code for the destination virtual agent's language.




#### Pass session data

If you want to pass session data from the source virtual agent to the destination virtual agent, include the `session_variable` property in your custom payload.

The following is an example of the `session_variable` property:
    
    
    "session_variable": {
      "capture_target": "payload",
      "capture_type": ["data_parameters"],
      "payload": {
        "value_one": "$session.params.payload_value_one",
        "value_two": "$session.params.payload_value_two"
      }
    }
    

When the virtual agent triggers the custom payload, it initiates a direct transfer to the virtual agent specified by the agent ID. A transfer message is displayed to the end-user unless transfer messages are hidden.

The following describes the behavior when chat sessions are transferred directly to a virtual task assistant:

  * **Virtual task assistant to virtual task assistant** : The source virtual task assistant leaves the chat and the destination virtual task assistant joins. The last human agent or support virtual agent in the session remains. Messages between the end-user and the destination virtual task assistant are not visible to a human agent that remains in the session.

  * **Support virtual agent to virtual task assistant** : The source support virtual agent remains in the chat session when the destination virtual task assistant joins the chat.




If the transfer fails, the end-user is transferred to a human agent assigned to the same queue. If there are no human agents assigned to the queue or no human agents are available, the chat ends.

## Hide transfer messages in chat sessions

You can configure your instance to suppress transfer messages that display to the end-user during a virtual agent to virtual agent transfer. This makes it appear to the end-user that they are speaking to the same virtual agent after the transfer. To prevent the end-user from seeing the virtual agent's name change during a transfer, give the source and destination virtual agents the same name and alias.

When you hide transfer messages, chat transfer system messages still appear in the agent adapter and in CRM transcripts.

To hide transfer messages in chat sessions, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Chat**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Web & Mobile Chat Settings** pane.

  3. For **Transfers** , select the **Hide chat transfer system messages to consumers for VA to VA transfers** checkbox.

  4. Click **Save Chat Details**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
