---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-record-creation/
title: CRM record creation \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:45.262088+00:00
---

# CRM record creation  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-record-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  CRM record creation Stay organized with collections  Save and categorize content based on your preferences. 

You can integrate a CRM with Contact Center AI Platform (CCAI Platform) to create and update records, also known as cases or tickets.

As an administrator, you can configure and control aspects of record creation on the **CRM Record Creation Details** pane of the CCAI Platform portal. You can find the **CRM Record Creation Details** pane by clicking **Settings** > **Operation Management**.

## CRM record creation details

The **Append call or chat session to latest open [CRM Record] in the same leaf queue** : Select this option and CCAI Platform will append sessions to an existing open record if it came in from the same exact queue ("leaf queue).

Salesforce: by default, this applies when a Case/Account/Opportunity is in **New** , **Working** , **Escalated** , or another non-closed status.

Secondary option to append to a closed case within a configurable duration. Click to enable and enter the number of days the case can be closed but still have a new session appended.

After appending the session, the case status is changed to default the open status.

**Delay call record until call is connected:** Standard record creation takes place when the call is _assigned_. When this setting is enabled, record creation takes place when the call is _connected_ to an agent, after it has been assigned. Enabling this feature covers the edge case where callers abandon the call after the call has been assigned to an agent but before the call is connected to the agent. When this setting is combined with the abandoned call setting, only calls that are connected to an agent will trigger record creation.

Because record creation normally occurs when the call is assigned, ticket or case creation will appear to be delayed 5-10 seconds. Such a change should be communicated to agents.

**Delay chat case creation until chat has a minimum of ___ messages sent by consumer** : By default, records are created when a chat is assigned to an Agent, then the chat is connected to an Agent. If the consumer doesn't send messages, empty records are created. Enabling this option:

Delays record creation until the consumer sends the set number of messages, preventing empty records.

Record pop for the Agent in the CRM is delayed 5-10 seconds after the set number of messages are received. Such change should be communicated to agents.

**Create CRM tickets for abandoned calls** : Creates a new CRM record even if the caller abandons a call before reaching an agent. This is recommended if you would like to report on "who" abandoned the call since CCAI Platform does not store specific caller information.

**Create CRM tickets for abandoned chats**

  * **When disabled** : Tickets are not created for abandoned or short abandoned chats. Short abandoned chats are based on the [short abandon setting](https://docs.cloud.google.com/contact-center/ccai-platform/docs/amandon) for chats.

  * **When enabled** : Two options appear:

  * **All abandoned chats** : Tickets will be created for short abandoned and abandoned chats.

  * **Abandoned chats with a minimum of ____ messages sent by user** : Tickets will only be created for abandoned chats with the set number of chat messages.


**Note:** Abandoned chats are defined as chats that are ended or canceled by the consumer prior to the chat getting connected with an agent. Consumer clicks on "End chat."

## CRM record title

To customize the title of your records (tickets/cases), adjust the text in this section.

Customization variables can be included in the title and will pull in available information:

### CALL_TYPE

  * IVR Call

  * Incoming Call (App)

  * Incoming Call (Web)

  * Voice Scheduled (App)

  * Scheduled Call (Web)

  * Outbound Call




### CALL_ID

: CCAI Platform Call ID value

### MENU_PATH

: Menu end-user selected

### PHONE_NUMBER

: Phone number dialed

### LANGUAGE

: Language selected or routed to based on dialed number and associated DAP.

### TIMESTAMP

: Time session started

## CRM record tags

Along with the configured record titles, you can add tags with the session type name to CRM records. It will allow you to sort between different session types by how records are tagged. CRM record tags are available for Zendesk, Kustomer, and Freshdesk.

### Examples for how each CRM applies the session types as tags

  * Zendesk: Voice Inbound (IVR) → voice_inbound_ivr

  * Kustomer: Voice Inbound (IVR) → Voice Inbound - IVR

  * Freshdesk: Messaging Inbound (Web Chat) → Messaging Inbound (Web Chat)




### Configuration options

  * **Add session type tags to cases** : Add a tag to the record with the session type, for example, Scheduled Call (Web) or Incoming Call (App).

  * **Add CCAI Platform tag to cases** : Adds the tag "UJET" to all cases created by the CCAI Platform integration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
