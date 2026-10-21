---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-session-metadata/
title: Session metadata file \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:36:51.368194+00:00
---

# Session metadata file  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-session-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Session metadata file Stay organized with collections  Save and categorize content based on your preferences. 

For every voice and chat session, Contact Center AI Platform (CCAI Platform) stores the session details in a session metadata JSON file. The session metadata file can be stored in an [external storage](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage) service that you configure or it can be attached to a CRM record. This file contains many data attributes, including session information, transfers, handle duration, participants, and diagnostic information. The session metadata file can be parsed and used for post-session analysis and tracking.

The session metadata file is updated 15 minutes after the session has completed.

The session metadata file can be used in the following ways:

  * Delivered to your external storage service in JSON format

  * Used to update a CRM record using email

  * Attached to a record in the integrated CRM




## Sessions metadata content

**Data** | **Description** | **Example value**  
---|---|---  
Lang | Selected language | `en`  
Session ID | The identifier of an interaction. | `12345`  
Session type | **Call types**

  * Voice inbound: standard PSTN calls.
  * Voice inbound (IVR by Mobile): fallback PSTN calls made from the mobile SDK.
  * Voice inbound (Mobile): placed by end-users by an installed mobile SDK.
  * Voice callback (Web): initiated from the Web SDK.
  * Voice inbound (API): initiated using API.
  * Voice scheduled (Mobile): scheduled using an installed mobile SDK.
  * Voice scheduled (Web): scheduled using an installed Web SDK.
  * Voice outbound: initiated by an agent by dialing a number.
  * Voice outbound (API): initiated using API.
  * Voice Campaign: initiated by an outbound dialer (Campaign).

Chat Types

  * Messaging (Whatsapp): initiated through Whatsapp.
  * Messaging inbound (SMS)
  * Messaging outbound (SMS)
  * Messaging outbound (SMS by API)
  * Messaging (Web): initiated by an installed Web SDK.
  * Messaging (Mobile): initiated by an installed Mobile SDK.

See: [Session type terminology](https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-type-terminology) | Voice Inbound (IVR)  
Session status | 

  * scheduled (0): the call is scheduled to take place at a specific time in the future.
  * queued (1): the call is waiting in a queue, ready to be assigned to an available agent.
  * assigned (2): the call has been assigned to a specific agent for handling.
  * connecting (3): the agent is in the process of establishing a connection with the call.
  * switching (4): indicates the call is transitioning between different states.
  * connected (5): a successful connection has been established between the agent and the end-user.
  * finished (8): the call has been completed.
  * failed (9): the call has failed and the specific failure reason code is provided.
  * recovered (10): a previously failed call has been retried and successfully completed.
  * deflected (11): the call has been completed with a deflection.
  * selecting (12): the call is in the process of selecting options from a menu before being queued (applies to IVR calls only).
  * va_assigned (13): the call has been assigned to a virtual agent for handling.
  * va_connected (14): the call has been successfully connected to a virtual agent.
  * preview_pending (15): the initial status for a campaign call, indicating connection with the dialer for previewing customer data.
  * preview_ready (16): indicates that data has been received from preview dialer and the call is ready for further processing.
  * campaign_connecting (17): the adapter has notified that the agent intends to take the campaign call, and the connection process is underway.
  * campaign_connected (18): confirmation that the campaign call connection has been successfully established.
  * requeued (19): a call that was previously handled by an agent but failed and has been added to a queue for handling again.
  * predictive_waiting (20): the agent is waiting for a predictive campaign call to be connected.
  * progressive_waiting (21): the agent is waiting for a progressive campaign call to be connected.
  * preview_waiting (22): the agent is waiting for a preview campaign call to be connected.
  * campaign_dialing (23): the agent's campaign call is in the process of dialing out to the end user.
  * voicemail (80): the call is in a voicemail state.
  * voicemail_received (81): voicemail has been received from the caller and recorded.

| `81`  
Created | The date that the interaction (call or chat) was created in the platform. | `2023-09-11T09:42:01.000+03:00`  
Queued | For inbound sessions, show the queue that the call came through. Displays the queue name where the interaction waited.  | `2023-09-11T09:42:01.000+03:00`  
Assigned |  Time that an agent was assigned to the session. | `2023-09-11T09:42:01.000+03:00`  
Connected | This signifies that the interaction is connected (in a Connected status). This indicates that the call contains both an agent and an end-user. | `2023-09-11T09:42:01.000+03:00`  
Ended | The time call ended.  | `2023-09-11T09:42:01.000+03:00>`  
Scheduled | The call is scheduled to take place at a specific time in the future. | `2023-09-11T09:42:01.000+03:00`  
Updated | The last time this metadata was updated | `2023-09-11T09:42:01.000+03:00`  
Handle time (call or chat duration) | The amount of time that elapsed from when an agent was assigned a call, including before call work (BCW) for preview campaign calls, to when they ended the wrap-up phase | 245 seconds  
Hold duration or Hold time | The sum of time (in seconds) an agent placed a consumer on hold during an interaction. Hold is recorded in total for a single interaction. An agent that places a consumer on hold multiple times will only show the total hold duration for that interaction. When that agent transfers the call out, this would start a new interaction which would track its own hold time. | 23 seconds  
Answer type | Human agent or virtual agent |   
OutTicket ID | ID applied by the CRM | 12345  
OutTicket URL | URL from the CRM Ticket | `https://example.com/`  
Recording permission | Recording permission is captured for the entire session of a call and is stored along with the call record itself.Under the recording permission column in historical reporting the following values can appear:

  * Granted: The end-user opted into having the call recorded.
  * Denied: The end-user opted out of having the call recorded.
  * Not Asked: The end-user was not asked if they consented to being recorded.

| `granted`, `denied`, `not asked`  
Recording URL | The URL to the specific recording for this record. | `www.example.examplecrm.com/23453732`  
Support phone number | The public number as assigned to the queue that an end-user will contact. This is inbound only. | +12223334444  
Outbound number | This is the agent's outbound phone number as found in the individual call history report. The number from which the agent is dialing. | +12223335555  
Menu path | The leaf node of a menu path, with the menu type indicating which channel the interaction was routed through. |   
Menu path ID | The ID which represents a unique materialized menu path. A materialized menu path is the tree of queue IDs that a call goes through. | `2420/4563/6205`  
Queue priority | The queue priority routing order. | 1-8 (numeric value)  
CSAT Rating | The customer satisfaction scores (CSAT) awarded to the interaction. Captured after an interaction ends. | 1-4 (numeric value)  
Comment | The customer satisfaction comment (CSAT) awarded to the interaction. Captured after an interaction ends. | 'Great job, I love my agent'  
`va_assigned` | The call has been assigned to a virtual agent for handling. |   
`va_connected` | The call has been successfully connected to a virtual agent. |   
SmartActions | Verification status | Indicates whether the device owner or end-user verified through a SmartAction. |   
SmartActions | Photos and screenshots uploaded | Indicates whether the photos and screenshots were sent through a SmartAction. |   
SmartActions | Video files uploaded | Indicates whether video files uploaded were sent through a SmartAction. |   
SmartActions | Text input | Indicates whether text input was sent through a SmartAction.  
Selected menu and menu path | The ID which represents a unique materialized menu path. A materialized menu path is the tree of queue IDs that a call goes through. | `2420/4563/6205`  
Agent info | The name of the agent assigned to the interaction. | Noam B  
Transfer information | If the customer has been transferred during the call session. Shows if a customer was transferred to other agent/menu  
Deflection information | A state that occurs based on the queue configuration for overcapacity queues or after hour calls.Displays if the customer was deflected and to which channel.Deflection options include voicemail, schedule call among others. Deflection will vary based on channel (Web, IVR, Mobile). | `after_hours_message_only`  
Disposition Codes and Notes | The code that the agent applies to the interaction when it is finished, identifying the call or chat subject or the outcome.Notes are formatted with plain text.For more information, see [Disposition Notes, Codes & Lists](https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-note). | Resolved; Customer needed to know our hours of operation, provided them. Customer had no further questions.  
In call SMS | Send and receive photos, videos, and screenshots from end-users, as well as exchange texts through MMS and SMS.  
Wait time SMS | Send SMS messages to callers who are waiting to be connected to an agent.  
Participants | Agent, end-users and/or third parties who participated in a particular call(s).Each member of a call gets recorded as a call_participant. If the same user leaves and rejoins a new `call_participant` record is created. These records are stateful and typically not used for metrics.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
