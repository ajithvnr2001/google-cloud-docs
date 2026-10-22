---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-api/
title: SMS API \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:51.423166+00:00
---

# SMS API  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  SMS API Stay organized with collections  Save and categorize content based on your preferences. 

With Contact Center AI Platform (CCAI Platform), you can use the SMS API to handle inbound and outbound SMS messages.

## Authentication

To use the SMS API, you need a credential.

To create a credential for the SMS API, follow these steps:

  1. In the CCAI Platform portal, click **Settings** > **Developer Settings** > **API Credential management**.

  2. Click the **\+ Add API Credential** button. An **Add API Credential** message will open.

  3. Enter a **Name** for the Credential.

  4. Click **Create**.




## Outbound SMS API

The Outbound SMS API provides an endpoint for initiating outbound SMS messages. This lets you to programmatically send SMS messages to consumers.

There are three key points to consider when using this API:

  * This service is not designed to send out tens of thousands of messages at once. The aim is event- driven messaging.

  * Consumers can respond to the SMS message and initiate a support session.

  * This API won't work if you need to send multiple SMS messages to the same number within the same day.




### Use Cases

Outbound SMS API sample use cases are event-based. For example, if you want to notify the consumer that their order is ready for pickup AND give them the option to respond. An active session is created when an outbound SMS is sent; when the customer responds, he or she is routed to an agent.

**Note:** Long SMS messages are supported, but they will automatically be broken into multiple smaller messages.

The difference between this and Sessionless Outbound SMS API is that with sessionless, you only send the notification and if the consumer responds, they receive a default message (if configured) and are not routed to an agent.

Other potential use cases:

  * Account login.
  * Account activity.
  * Important account usage events.
  * Connected device issue detection.
  * ETA Notifications for on demand services, like deliveries and ride shares.
  * Appointment reminders.
  * Proactive service or account alerts.
  * Two factor authentication (requires customer has an existing code generator and service process).



### Outbound SMS API endpoint

The base URI for this new endpoint is:
    
    
    POST https://<subdomain>.<domain>/apps/api/v1/sms
    

## Inbound SMS support

Should an environment want to support inbound SMS responses, the outbound number also needs to be set up as an inbound SMS number that is assigned to a queue. Each SMS phone number can only be assigned to **one** queue. For more information see: [General SMS Chat Config](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms#config-sms-chat).

If an end-user replies to an SMS configured this way, they will be brought to the SMS queue menu that the inbound SMS phone number is assigned to. For more information see [SMS Messaging Chat Settings - Phone Number](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms#sms-chat-settings).

**Note:** Given the unique menu ID assignment for inbound SMS numbers, `menu_id` is not needed as an API input parameter (see the following API Operations section)

## API Operations

This section outlines the API operations, body parameters and response codes.

### Body and Params

The following fields should be included in the body of the API request:

Field Name | Type | Required | Description | Values | Notes  
---|---|---|---|---|---  
agent_id | Integer | No |  |  | The agent corresponding to this ID will be assigned to a new chat if a chat does not exist between the provided numbers. If the agent is connected to an existing chat the message will be sent on their behalf.  
agent_email | String | No | The agent's email address. |  |   
chat_type | String | Yes | SMS message | SMSAP |   
chat_subtype | String | Yes | api_initiated |  |   
end_user_number | String | Yes | Number the text message is to be sent to |  | Validation: valid phone number: `+18882468888` for a US phone number  
outbound_number | String | Yes | Outbound phone number to be used for sending the SMS message |  | Validation: a) phone number needs to be an SMS phone number associated with the tenant, b) missing phone number, c) phone number is incorrect format: `+18882468888` for a US phone number  
message | String | Yes | SMS message to be sent to consumer | Long messages: break long messages into multiple messages (should be covered in existing outbound SMS capability) | Validation: a) missing message, b) message exceeds maximum number of characters (by x)  
ticket_id | id | No | Will associate session to a specific CRM ticket ID | Note: invalid ticket IDs will be ignored. |   
  
### Error and Success

Case | Expected Result | Copy  
---|---|---  
SMS service is enabled  
Outbound SMS service is enabled  
chat_type value is 'OutboundSMSAPI'  
end_user_number is provided and well formed  
outbound_number is provided and well formed  
For non US phone numbers: non US phone number is enabled  
Message is provided  
No active chat between outbound_ number and end_user_number | success | (200) Success Response Sample  

    
    
    { 
      "id": 2415,
       "lang": "en",
       "chat_type": "SMS",
       "status": "selecting",
       "created_at": "2021-10-12T19:28:43.000Z",
       "queued_at": null,
       "assigned_at": null,
       "ends_at": null,   "wait_duration": 0,
       "chat_duration": 0,   "rating": null,
       "has_feedback": false, 
       "out_ticket_id": null,
       "out_ticket_url": null,
       "verified": false,
       "disconnected_by": "disconnected_by_unknown",
       "fail_reason": null,
       "selected_menu": null,
       "menu_path": null,
       "agent_info": null,
       "end_user": {       "id": 131,
           "identifier": null,
           "out_contact_id": null
       },
           "photos": [],
       "videos": [],
       "transfers": [],
       "participants":
     [
           {
               "id": 5594,
               "type": "end_user",
               "status": "connected",
               "chat_id": 2415,
               "user_id": null,
               "end_user_id": 131,
               "chat_duration": null,
               "connected_at": "2021-10-12T19:28:43.000Z",
               "ended_at": null,
               "fail_reason": "nothing"
           }
       ],
       "offer_type": null,
       "offer_events": [],
       "answer_type": "manual",
       "outbound_number": "+14151234567"
    }
      
  
Agent id and agent email are provided | error | Only one of `agent_id` or `agent_email` can be provided.  
Agent id or agent email is provided  
Agent is not connected to existing chat | error | Outbound SMS failed. Agent is not connected to chat.  
SMS service is not enabled | error | "SMS service is not enabled".  
Outbound SMS service is not enabled | error | "Outbound SMS service is not enabled"  
chat_type is not provided | error | "chat_type needs to be provided"  
chat_type is provided but is not set to 'sms' | error | "Valid chat_type needs to be provided"  
end_user_number is provided but not well formed | error | "end_user_number is invalid"   
(note: valid phone number: "+18882468888" for a US phone number)  
end_user_number is not provided | error | "end_user_number is required"  
outbound_number is provided but not well formed | error | "outbound_number is invalid"   
(note: valid phone number: "+18882468888" for a US phone number)  
outbound_number is provided but does not exist for that tenant | error | "outbound_number is not found"  
outbound_number is not provided | error | "outbound_number is required"  
outbound_number is a non US phone number and 'non US phone number service' is not enabled | error | "Non US phone number service is not enabled"   
**Note:** depends on **Non-US phone number** setting at **Settings > In Call SMS > Non-US Phone Number Configurations**  
Message is empty | error | "message is required"  
Active chat between outbound_ number and end_user_number | error | "Outbound SMS failed. Consumer is already in an active SMS session."  
ticket_id is filled but does not exist in CRM | error | "Ticket is not found"  
  
## SMS expiration

Outbound SMS messages are active as soon as they are sent.

**Any SMS chat needs to end before a new SMS chat session can be established** between a given outbound and consumer phone number. This includes outbound SMS messages sent using the API. Any outbound SMS will fail if there is an existing, active chat between the outbound and consumer phone numbers.

## Automatic chat timeout options

Automatic chat timeout options are configured in the **Settings > Chat > SMS Expiration & Global Timeout.** This provides controls for how long a chat session will remain active if there is no activity or progress in the chat session flow.

### Chat status distinctions

The following are distinctions between chat process state changes:

  * **Queue selecting state Chat Expiration** _Outbound chats sent using the API are considered in the queue selecting state until the consumer replies_

Any chat session that has not progressed beyond the queue selection state. This includes sent outbound SMS messages to which a consumer has not replied. It is possible to define how long a chat can remain in this state before it expires (message sent & consumer does not respond within timer - chat expires).

  * **Unanswered SMS chat expiration (during hours of operation)** The length of time a chat can remain unanswered in a queue before it expires within the set operation hours for the specific queue.

  * **Unanswered SMS chat expiration (during after hours)** The length of time a chat can remain unanswered in a queue before it expires outside of the set operation hours for the specific queue.

  * **Outbound SMS chat timeout** Outbound SMS chat sessions will automatically expire if there is **no** activity for [x] minutes.




## Chat status details

  * When an outbound SMS is sent using the API the chat is considered **active** but not **connected**

  * These **active** outbound SMS chats are considered to be in the **queue selecting state** until the consumer replies

  * Chats are considered **connected** once the consumer replies and an Agent is assigned to the chat




### Chat status impact on applied timers

  * **Active** chats sent using the API that have not had a response from the consumer are subject to the Queue selecting state timer

  * Chats connected to an agent are subject to the Outbound expiration timer

  * If a consumer replies to the initial message but an Agent is never assigned, the chat is not **connected** and is subject to the Unanswered Chat Expiration timer, inside or after operation hours


**Note:** Manual Outbound SMS messages can be initiated by an agent and are subject only to the outbound chat timeout.

Example API message flow and statuses:

  1. SMS message is sent using the API to consumer - chat is in _queue selecting state_ and is not connected to an Agent

  2. Queue selecting state chat expiration timer starts. Chat times out and is ended if the consumer does not reply within the timer threshold.

  3. Consumer replies to chat - chat is now connected to an Agent.

  4. Consumer sends last message - Outbound SMS chat timeout timer starts.

  5. Outbound SMS chat timeout timer threshold reached - chat is ended.




**No chat dismissal timer** \- for API initiated outbound SMS sessions, the **chat dismissal timer** does not operate so a chat dismissal event won't occur even after that chat comes in as an inbound chat when a consumer replies to the message.

## Response Definition

The API responds with a single call object, as seen in the model from /calls.

## Sessionless Outbound SMS API

CCAI Platform offers an Outbound SMS API that can support outbound SMS messages without any linked sessions.

This API call initiates non-session linked SMS messages that can be triggered during an existing workflow using CCAI Platform.

A sessionless sms is preferred in instances where just a one-time message is sent out to consumers and there is no need for a CRM ticket to open.

This Outbound SMS API provides the ability to send up to 500 messages per API call.

### Use Cases

Common use cases for a sessionless SMS can include the following:

  * One-time password setup.

  * Verification code.

  * Appointment reminders.

  * Feedback links.

  * Marketing or promotional messages.




Sessionless Outbound API and Outbound SMS API vary in that with Outbound SMS when a consumer responds, an active session is initiated and they can be routed to an agent. While they share similar use cases (delivery notifications, appointment reminders), the difference is in what happens when the consumer responds. They may receive a default don't reply notification with sessionless, but with outbound SMS, they will be routed to an agent.

### Sessionless Outbound SMS API endpoint

The base URI for this endpoint is:

`POST https://<subdomain>.<domain>/apps/api/v1/sessionless_sms`

### Add an API credential

  1. In the CCAI Platform portal, go to **Settings** > **Developer Settings** > **API Credential management**.

  2. Click the **\+ Add API Credential** button. An **Add API Credential** message will open.

  3. Enter a name for the credential **Name**.

  4. Click **Create**.




### Sending SMS messages

To send a sessionless outbound SMS, call `POST https://<subdomain>.<domain>/apps/api/v1/sessionless_sms` and pass the following request parameters:
    
    
    {
      "from_phone": <string>,
      "to_phones": <array[string]>,
      "messages": <array[string]>
    }
    

Field Name | Type | Required | Description | Notes  
---|---|---|---|---  
from_phone | String | Yes | The phone number from which the messages will be sent. | **Must be a valid US number.**  
The API call will return an error if:   
* the phone number is not an SMS phone number associated with the tenant  
* the from_phone field is empty  
* the phone number does not follow the correct format. For example, the following number is a valid US phone number: `+18882468888`  
to_phones | Array [String] | Yes | The phone numbers to which the messages will be sent. | To ensure the API call succeeds:  
* Confirm you have a valid phone number, such as `+18882468888`  
The maximum count of phone numbers is 100 per API call.  
messages | Array [String] | Yes | The messages to be sent. | The maximum count of separate messages you can send is 5.  
Each message has a limit of 320 characters and cannot exceed that limit.  
  
### API Responses

If the API call is successful, you will see:

  * code: 200

  * Request ID

Make sure you log the request ID in your system records. In case you need to troubleshoot an issue, support will need the request ID to assist.




If the API call fails, you will see:

  * code: 4xx

  * Error message




### SMS Limitations

  * The API processes a maximum of 300 messages per minute.

  * All unprocessed messages will expire in 2 hours.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
