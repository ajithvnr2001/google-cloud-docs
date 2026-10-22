---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/zendesk/
title: Zendesk \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:57.028199+00:00
---

# Zendesk  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/zendesk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Zendesk Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) provides integration with the Zendesk CRM. This document outlines how to perform this integration. 

## Flexible outbound dialing

Flexible Outbound Dialing provides flexibility and granularity when associating outbound calls to tickets and contacts. Admins can configure which options Agents have access to for better control of each company's individual processes and goals.

**Note:** If **Do not create a ticket** is selected, call data won't be stored in CCAI Platform or your CRM.

Flexible Outbound Dialing gives Agents the ability to:

  * Select from tickets associated with the selected contact

  * Configure an option to create a ticket and not create a new ticket for each outbound call

  * Handle multiple matching contacts

  * Dial a phone number without adding the dialed number to the selected contact record




You can call a separate number by selecting the **Call a separate number** option from the agent adapter's outbound calling options. This lets an agent call a different number than the phone number the agent used to find the CRM account or record.

### Prerequisites

  * You must have the Talk Partner Edition plan for all agents (https://www.zendesk.com/talk/talk-partner-edition/)

  * Minimum Zendesk package v1.4.




### Configuration Considerations

  * Settings dependencies like settings for appending calls or chats to existing cases impact this feature. See CCAI Platform portal settings that can impact the agent experience.

  * When Team-based Outbound Call Ticket Entry feature is used, some sections of this feature will be blocked. Details in Interactions with other features.

  * Configuration saved in **Settings** > **Operation Management** so "Use entered number to make call" can be overridden by agent selection in the Call menu of Zendesk.

  * If **Do not create a ticket** is selected, call data won't be stored in CCAI Platform or your CRM.




### CCAI Platform portal configuration

Configuration of Zendesk CRM requires changes in to CCAI Platform. The following sections outline the necessary configuration changes needed.

#### Custom configuration - Operation Management

![Multiple accounts window](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f267cf654.png)

  1. Go to **Settings** > **Operation Management**.

  2. In the Multiple Account or Cases section, enable or disable:

**Prompt agents to select open case from list (when applicable)** :

**Disabled:** most recent open ticket associated with the contact will be auto-selected.

**Enabled** : agent will be prompted to select from all open tickets associated with the contact.

**Note:** In Ticket Creation Details, if "Don't append call or chat session to any existing open case" is enabled this option won't be editable.

When this option is enabled, **Allow agent to select "Create a new case" option for outbound calls** can be enabled. When disabled the agent must use an existing open ticket.

**Allow agent to select "Do not create a case" option for outbound calls**

Don't enable this option if your compliance regulations or standards require all call recordings to be accessed as CCAI Platform won't be able to retrieve call recordings of calls where a ticket is not created.

**Allow "Use entered number to make call" option**

     1. **Disabled** : Outbound calls can only be placed to numbers that are stored on the account or contact object.

**Note:** Configuration for "Use entered number to make call" can be overridden by agent selection in the Call menu of Zendesk. See "Use entered number to make call" option for details.
     2. **Enabled** : Agents can select the Contact ID, then enter a number not saved to the Contact to place a call. The numbers won't be stored against the Contact.




### Agent adapter experience

The following is an example of the agent call adapter with all options described previously in Custom configuration - Operation Management enabled:

![Agent call adapter](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f267d5795.png)

  * **Language and outbound number selection** dictates which number will show when the caller answers the call as well as how the call shows in reporting.

  * **Phone number** : Shows current selected, associated, or entered phone number to which the call will be placed. The placeholder number (415) 123-4567 will show when no number is selected/entered.

  * **Dialpad icon** : Opens the phone number input screen where you can enter or paste a phone number.

  * **Use entered number to make call** : See "Use entered number to make call" option. _May not be present based on settings._

  * **Contact ID field** : Displays the contact record the call will be associated with.

  * **Ticket ID field** : Displays the selected ticket. _May not be present based on settings._

Once Contact and Ticket ID are selected/populated, **Call** places the outbound call.

  * **Cancel** : Brings you back to the main Agent Adapter UI.




#### Agent adapter variables

The agent adapter will display different options and different views based on your Operation Management settings.

##### CCAI Platform settings that can impact the agent experience

  * Don't append call or chat session to any existing open case

  * Prompt agents to select open case from list (when applicable)

  * Allow agent to select **Create a new case** option for outbound calls

  * Allow agent to select "Don't create a case" option for outbound calls

  * Allow "Use entered number to make call" option




##### CRM data impacting the agent experience

  * Number of contacts with the same phone number

    * No Contact with phone number

    * Only one Contact with phone number

    * Multiple Contacts with phone number

  * Number of open tickets

    * No ticket

    * Only one ticket

    * Multiple tickets




### Placing an outbound call

The following sections provide guidance on the various ways to place outbound calls from Zendesk.

#### Call from contact in Zendesk

  1. In the CRM, click the contact name from a ticket or by searching for a contact.

  2. Click the **phone number** and select **Call this number**.

The phone number and contact will populate in the Agent Adapter.

  3. Click **Call** in the Agent Adapter.




#### Call from a ticket

  1. Select the ticket you want to use to call the requester.

  2. Above the new comment field, click **Call**.

  3. Select an existing telephone number. The phone number and contact will populate in the Agent Adapter.

  4. Click **Call**.




#### Dialed outbound call

  1. From the Agent Adapter, click **Dial** to view the outbound call screen.

  2. Click the **Dial** icon.

  3. Enter **+[country code]** phone number using your keyboard, or paste a copied number.

  4. Click **Next**.

  5. Click **Call**.




#### "Use entered number to make call" option

A specific account might have multiple locations or contacts, and not all phone numbers are saved to the contact. In this situation, your agents may need to dial out to numbers that aren't saved within the contact/user. This option allows for an agent to dial out to a number not saved to the contact while still associating the call with the contact. The number dialed will be saved in the comments of the Ticket.

  1. From Zendesk, locate the ticket you want to associate the call to.

  2. Click **Call.**

  3. Click **Enter new number** and the "Use entered number to make call" checkbox will be selected and the ticket ID will populate in the Adapter.

  4. From the Agent Adapter, click the **dialpad** icon to edit the number.

  5. Paste or enter the phone number in the phone number field.

  6. Click **Next**.

  7. Click **Call**.

  8. The call will be listed on the open Ticket.




### Interactions with other features

The following sections outline the interactions for additional features.

#### Team-based outbound call ticket entry

When this feature is enabled globally, and for the team to which the agent is assigned:

  * Call menu on a ticket: allows agent to select a number and the Agent Adapter will populate the ticket ID, fulfilling the requirement of entering a ticket ID.

  * Call menu on a ticket: **Enter a new number** option is not compatible with this feature and will result in an error in the Adapter.

  * Click to dial from contact: Clicking on the phone number of a contact is not compatible with this feature and will result in an error in the Adapter.




## Zendesk default rules and behaviors

Once the CCAI Platform package is installed in your Zendesk instance, CCAI Platform has a specific set of interactions with Zendesk which are either performed by default or can be customized from various settings in the CCAI Platform Portal.

### Ticket creation

  * When a **Mobile or Web SDK chat** is assigned to an agent, CCAI Platform:

    * Performs a contact lookup based on the passed contact parameters and either uses an existing contact of creates a new record

    * Creates a ticket in Zendesk with ticket title that can be customized in **Settings > Operation Management**

    * Assigns the ticket to the agent

    * Includes any information available in ticket description (Custom Data, selected menu path, Web user info, etc)

  * IVR, Mobile, and Web calls

  * **Multiple Matching contacts for IVR calls**

    * Ticket creation is unsuccessful if the agent does not select a contacts when presented with multiple matching contact records. CCAI Platform checks ticket status at the end of the call and if ticket creation failure is detected, the most recently created contact with the same phone number is auto-selected, the ticket is created, and attached to that specific contact record.
  * When an **outbound call** is placed, and the most recent ticket for that user is not in Open status, CCAI Platform creates a new ticket in Zendesk

  * When a user **calls** in but abandons the call, CCAI Platform creates a ticket in Zendesk. This can be disabled at **Settings > Operations Management**.

  * When a user leaves a **voicemail** , CCAI Platform creates a voicemail ticket in Zendesk even if there is an Open status ticket from the same customer

    * [CRM Default User](https://docs.cloud.google.com/contact-center/ccai-platform/More_Integrations/index.md#UUID-8db227c3-1678-87aa-936f-7d38ea02e88e) should be set up in order to avoid random agent assignment

    * The voicemail ticket can be reused by a new IVR call or outbound call




### Ticket updates

  * When there is an incoming **call/chat** from the same customer, same menu selection, and same channel as a current ticket in New, Open, Pending, and On-Hold status, CCAI Platform appends the call or chat to the open ticket. This can be disabled at **Settings > Operations Management**.

  * **Outbound calls** will be appended to an existing ticket and the ticket status will be set to Open if the call meets both of these requirements:

    * Was originally created from a CCAI Platform call

    * Has the status of New, Open, Pending, and On-Hold

An **optional feature** for appending tickets is available: Zendesk: Team-based Outbound Call Ticket Entry.

  * CCAI Platform **appends a call** to an open ticket when:

    * An agent uses the "Hang up and call back" option from the adapter

    * A call is less than 10 seconds, and the agent uses the **Callback** button, CCAI Platform appends the call to the open ticket

  * When an **inbound/outbound call** ends, CCAI Platform updates the ticket with the call recording file in Zendesk when call recording is enabled.

    * **Merging behavior:** If the Agent is on a call that creates a ticket, ticket A, and while the call is still on-going the Agent creates a new ticket, Ticket B, and merges the ticket (A is merged to B), then ticket B will be updated when the call ends. The 'call_finished' event and the Call Recording will be logged in ticket B.
  * When a **call/chat is transferred** , CCAI Platform assigns the ticket to the agent who the call is transferred to

  * When a **SmartAction** is completed, CCAI Platform updates the ticket with action results and shared files in Zendesk

  * When a **SmartAction** fails due to an error on the user's side (ex. fingerprint access not enabled), CCAI Platform updates the ticket in Zendesk with a record of the error message

  * When a customer uses **custom field mapping** (set up from the Admin Portal), the data coming in from mobile or web SDK will be placed in the designated field in the CRM

    * If no mapping field is found, an indication will be noted in the ticket that there was no field found as designated
  * When an end-user **rates** a Mobile call/chat, CCAI Platform adds rating score to the ticket

  * When an agent **reads/dismiss/calls back from voicemail** , CCAI Platform updates ticket

  * Optional: When **API Direct Access Points** are used, CCAI Platform can post the API Response data as key-value pairs or JSON format as a comment. The option can be found in **Settings > Developer Settings**




### Contact creation

  * When an **IVR call** comes in with a new phone number, CCAI Platform creates a contact in Zendesk

  * When the new app user (new identifier) starts the **CCAI Platform SDK** Mobile, CCAI Platform creates a contact in Zendesk

  * When a new or unauthenticated user initiates a call or chat through the web SDK, CCAI Platform creates a new contact




#### Multiple matching contacts for IVR calls

Ticket creation is unsuccessful if the agent does not select any contacts when presented with multiple matching contact records. CCAI Platform checks ticket status at the end of the call and if ticket creation failure is detected, the most recently created contact with the same phone number is auto-selected, the ticket is created, and attached to that specific contact record.

## Zendesk: Custom ticket fields for SDKs

In order to better track call details, CCAI Platform offers an option to automatically create a few chat or call specific fields which update when a call is completed. If the information is available for the CCAI Platform session, the custom field will be automatically filled out.

**Only available for Mobile and Web SDK calls/chats.**

### Included fields and details

Some tickets will have multiple calls associated, depending on your settings in Operation Management. The fields will reflect the session data from the most recent call or chat associated to the ticket.

  * Filled out at the beginning of the session

    * **Session type:** call, chat, Web, Mobile

    * **"From" phone number:** shows the number the agent used to dial outbound

  * Filled out when the session is complete

    * **Call duration:** length of call including hold time

    * **Wait time:** length of time between when call is queued and connected to an agent

    * **Queue name:** name of the last queue that the session was assigned to

    * **Call/Chat ID:** CCAI Platform unique ID of the call or chat

    * **Hold time:** length of aggregate hold time in this session

    * **Customer Satisfaction rating:** Available when using Web and Mobile standard CSAT score

  * If the mobile SDK is being used, SmartAction data will show:

    * **Verification:** result of verification SmartAction

    * **Customer Text Feedback**




### CCAI Platform portal configuration

  1. Go to **Settings > Developer Settings**.

  2. Under **Custom Field for Contact and Ticket** , click **Create**.

  3. You can now rearrange and control the new custom ticket fields if you are a Zendesk Admin and tickets will now contain these fields. Information will auto-update when the call is completed.

![Rearrange ticket fields](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f267db6bb.png)




## Zendesk: Team-based outbound call ticket entry

When an outbound call is made in Zendesk, by default a new ticket will be created. With this feature, when the ticket number of the existing ticket is entered, the outbound call is placed based on contact or ticket information, and the call is logged to the open ticket.

For a more integrated option, see Flexible outbound dialing.

### Behavior when enabled

  1. When an agent launches the CCAI Platform adapter and clicks to dial an outbound call, they will be prompted to enter a ticket ID.

**_Configuration option_** : Entering the ticket ID can be made optional or required.

  2. Once the ticket ID is entered, CCAI Platform will check the phone number associated with the contact and dial out.

**_Configuration option_** : The dialed number can be configured to pull from a custom ticket field instead of the default number in the contact

  3. The outbound call activity will be added to the existing ticket if the existing ticket has a status of New, Open, On-hold, or Pending

     * A ticket cannot be associated if the existing ticket is in Solved status or Closed status.



### Enabling this feature

The use of this feature requires **3 steps** to enable:

  1. **Enabling the setting per-team:** Each team needs to be specifically set up for use of this feature in the Agent and Team settings

  2. **Assigning the Enabled Team to a Queue:** Teams need to be assigned to receive calls

  3. **Setting a default outbound number on the associated Queue**




#### Team configuration

  1. Go to **Settings > Users & Teams**.

  2. Hold the pointer over the team you want to add the ticket association setting to and click the **edit** icon.

  3. Mark the checkbox for **Enable Ticket ID**.

![Enable ticket ID display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f26813b97.png)

  4. If you want this to be required, mark the **Required** box.

  5. Click **Add** to save.




#### Queue configuration

  1. Go to **Settings > Queue** and select **IVR**.

  2. Click the queue that you would like the ticket feature to be used with.

  3. Click to enable **Instant Voice Call.**

![Enable instant voice call display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f268188e4.png)

  4. Click **Assign Agents**

  5. Add the teams by entering the team name and selecting the name when it appears.

  6. Click **Save**.

![Add teams display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f2683cfbe.png)




#### Outbound number assignment

  1. Ensure an outbound number is assigned.

![Assign outbound number display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f26869941.png)

  2. Refer to Multiple Outbound for more options.




### Optional ticket field configuration

This section outlines the stages to configure the ticket field.

#### Outbound call - custom phone number lookup for ticket ID by agent (Team option)

By default, when the ticket number is entered, CCAI Platform will look for the default phone number of the contact who is the Requestor on the ticket. To change this and use another phone number for all outbound calls with this feature, follow these steps:

  1. From the Admin portal, go to **Settings > Developer settings**.

  2. Scroll to **Outbound Ticket Settings**.

  3. Mark the checkbox and select the Contact Field from the available fields that you want CCAI Platform to pull the phone number to dial from.

![Contact field display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f2688f394.png)

  4. The available fields can be found in your Zendesk environment in **Settings > Ticket Fields > Field ID**.

![Field ID display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f26894dcf.png)

  5. Click **Save Changes**.




## CRM API batching - Zendesk

Due to [CRM Rate Limiting](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-rate-limits), CCAI Platform offers configuration options to reduce the volume of API requests made to Zendesk during call and chat interactions. This is accomplished by batching certain API service requests across call or chat sessions over a period of time.

### Configuration options

  * **API services** : The two most frequently utilized API services are available for batching.

    * Add Comment: Estimated 37% of API volume

    * Update assignment / ticket: Estimated 12% of API volume

  * **Batching frequency** : Configurable from 1 to 60 seconds, with a default of 10 seconds. Sessions are batched over the specific batching frequency duration, or for the selected time: For example, 5 seconds, all "add comment" and "update assignment/ticket" requests are batched across all sessions.




### Enabling API batching

_Admin permissions needed for this action._

  1. In the CCAI Platform portal, go to **Settings > Developer Settings.**

  2. Enter the **API Token** from Zendesk.

![API token in developer settings](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f268b0493.png)

  3. Fill in the **Batching frequency** in seconds. The recommendation is 10 seconds.

  4. Check boxes for batching APIs.

  5. Click **Save Changes.**




## CCAI Platform agent experience in Zendesk

A brief overview of the expected behavior of CCAI Platform in the Zendesk CRM.

### Requirements

  * Zendesk

  * CCAI Platform App Installed




### Access the agent adapter

The icon to access the agent adapter will show on the top right of your Zendesk utility bar.

![Zendesk utility bar](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f268b5c66.png)

When making or receiving calls or chats, the Zendesk integration will automatically pop the related or created ticket.

![Zendesk popup](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f268bb2ef.png)

**Other Notes:**

  * The adapter can be minimized while in use.

  * The ticket side panel and tags will vary depending on your Zendesk triggers.

  * The ticket will auto-assign to the agent answering the call.




### Standard data

Immediately on creation, CCAI Platform will provide standard data to the ticket as an internal comment. This includes the call ID, language, and inbound menu (queue) selection. After the call, a comment with the recording will be created.

### Custom data

If using custom data from the CCAI Platform SDKs, the information will create an internal comment in the ticket. You can also map the custom data directly to fields in Zendesk using the CCAI Platform integration. These mapped fields can show in the left side bar.

![Custom data mapping](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162e3f268c1c53.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
