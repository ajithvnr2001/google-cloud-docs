---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/kustomer/
title: Kustomer \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:06.239694+00:00
---

# Kustomer  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/kustomer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Kustomer Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) supports integration with the Kustomer CRM. This document outlines the features and integration between the two platforms.

## Kustomer click to call

The CCAI Platform integration allows Kustomer agents to click-to-call from inside the Kustomer platform.

### Click-to-call

Use call **Phone** in the side panel near any phone number to fill it out in the agent adapter (see image below), then click **Call**.

**Note:** Phone numbers in the timeline and conversations are not clickable.

This is the intended behavior by Kustomer.

![Click to call button](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc4d33eaf.png)

## Create custom fields

To better structure your data in your Kustomer CRM, Admins can add custom Account and Record fields in Developer Settings. The following custom fields are available:

  * Account Custom Fields
  * Custom User ID
  * Record Custom Fields
  * Queue Name
  * Session Type 
  * Session ID
  * From Phone Number
  * Call Duration
  * Hold Time
  * Wait Time
  * CSAT Rating
  * CSAT Comment
  * Customer Menu Selection
  * Email using In-Web



### Create custom fields for Account and Record in Developer Settings

  1. In the CCAI Platform portal, go to **Developer Settings** > **Custom fields** for Account and Record.

  2. Click **Create**.

  3. After you select **Create** in CCAI Platform portal, the custom fields are created in Kustomer. The data is pushed into the new fields for all sessions that occur after the custom fields were created. The custom fields will appear in the Message section, under **Additional Information** in Kustomer.




## Kustomer synching agent status inheritance

**Note:** Requires integration with CCAI Platform mobile SDK or web SDK.

The CCAI Platform Agent Status Inheritance feature gives admins the ability to map Kustomer agent statuses to CCAI Platform agent status. Once mapped, it allows real-time agent statuses updates from Kustomer to CCAI Platform.

Custom mapping allows for flexibility to match each organization's distinct processes and status settings. For example: Agents handling email in the CRM can be configured to define the agent's status as 'unavailable' in CCAI Platform.

This also provides a single mechanism for manual and system updated statuses to be set, allowing agents to determine their status from just one place (Kustomer).

**Important** : Kustomer must be configured (see Step 1: Kustomer Configuration below) before CCAI Platform Agent Status Inheritance is enabled (see Step 2: Enabling CRM Agent Status Inheritance in the CCAI Platform Portal).

### Agent status inheritance

The agent status sync is a one way sync from Kustomer to CCAI Platform. As a result, the following requirements must be met in order for this sync to occur:

  * Kustomer needs to update the CCAI Platform App for your org.

  * For Status Sync: <Customer> should use its own unique user in Kustomer and CCAI Platform Portal for each agent and make sure they don't use a shared user.

  * To make the sync work - you can be logged in only in a single Kustomer instance (tab, computer, etc.) with the same user ID. If you sign in to Kustomer from several computers or in multiple tabs using the same user, the sync won't work because it does not know which instance to update.

  * The CCAI Platform status can be changed using a drop-down menu in the lower left corner of the Kustomer CRM page.

  * You must login to both Kustomer and Agent Adapter inside Kustomer CRM with the same email address. This is how the sync occurs.

  * It's not possible to apply status at login because Kustomer does not provide a backend API to fetch the user's status.


|   
---|---  
![Call adapter](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc4d5d99c.png) | ![Chat adapter](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc4d8961e.png)  
  
#### Step 1: Kustomer configuration

User statuses allow agents to notify their teams when they are available. Refer to [Kustomer User Statuses](https://help.kustomer.com/tags/User%20Status) for more information.

  1. To add a user go to **Settings** > **Users** > **Teams**.

  2. Click the edit beside the Team to be configured (see image below).

  3. Switch the **Enable Team Routing** toggle to On.

  4. Under **Settings** > **Platform** > **Queues & Routing**, custom statuses can be added under **User Statuses**.




#### Step 2: Enabling CRM agent status inheritance in the CCAI Platform portal

Now that Kustomer has been configured (Step 1), agent status inheritance needs to be enabled in CCAI Platform.

Contact support for assistance with this step (Step 2).

#### Step 3: CCAI Platform administrator configuration

  1. To configure in the CCAI Platform portal, go to **Settings** > **Developer Settings** > **Agent Status**.

  2. Switch the **Kustomer User Status Inheritance** toggle to On.

  3. Under **Agent Status Prioritization** , choose an option: 

     * **The latest status change is applied whether from CRM or CCAI Platform**
     * **CRM always overrides agents' next status**
  4. Click **Set Status Prioritization**.




## Agent experience in Kustomer

CCAI Platform integrates with the Kustomer CRM to provide for a seamless agent experience and customer resolution.

### Requirements

  * Kustomer App

  * Kustomer CCAI Platform Installation




### The agent adapter

The agent adapter appears in your Kustomer App.

When making or receiving calls or chats, the CCAI Platform Kustomer integration will automatically pop up with related conversation records.

Note that:

  * The adapter can be minimized while in use.

  * The contents of the conversation side panel will vary dependent on your Kustomer workflows.

  * The conversation will auto-assign to the agent answering the call.




### Standard data

When the call record is created, CCAI Platform will automatically include standard data in the conversation fields. This includes the Call ID, Language, and Inbound Menu selection. After the call, it will automatically update with the recording.

### Custom data

If you use Custom Data from CCAI Platform SDKs, the information must be mapped over to specific Kustomer fields on the right-side panel.

![Example session for custom data](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162c7fc4e4169d.png)

## Kustomer + CCAI Platform rules and behaviors

The following should be noted when Kustomer and CCAI Platform are integrated.

  * Ticket creation:

    * When a mobile SDK call or chat comes in.

    * When an IVR call is answered by an agent.

    * When an outbound call is placed, and the most recent session for that user is not in Open status, CCAI Platform creates a new session in Kustomer.

    * When a user calls in but abandons the call, CCAI Platform creates a session in Kustomer.

    * When a user leaves a **voicemail** , CCAI Platform creates a voicemail session in Kustomer even if there is an Open status session from the same customer.

  * Ticket updates:

    * When there is a **call/chat** from the same customer, same menu selection, and same channel as a current session in Open status, CCAI Platform appends the call or chat to the open session (applies to Open status only).

    * When an **outbound call** is placed, if the most recent session with that user is in Open status, CCAI Platform will append the outbound call to the Open session for follow-up cases.

    * When an **inbound/outbound call** ends, CCAI Platform updates the session w/ attached call recording file in Kustomer when call recording is enabled.

    * When a **call/chat is transferred** , CCAI Platform assigns the session to the agent who the call is transferred to.

    * When an agent uses the "Hang Up and call back" option from the widget, CCAI Platform appends the call to the open session.

    * When a call is less than 10 seconds, and the agent uses the "Callback" button, CCAI Platform appends the call to the open session.

    * When a **SmartAction** is completed, CCAI Platform updates the session with action results and shared files in Kustomer.

    * When a **SmartAction** fails due to an error on the user's side (i.e. fingerprint access not enabled), CCAI Platform updates the session in Kustomer with the error message.

    * When the company uses **custom field mapping** (set up from the CCAI Platform portal), the data coming in from Mobile or Web SDK will be placed in the designated field in the CRM.

    * When end user rates an **Mobile call or chat** , CCAI Platform adds rating score to the session.

    * When an agent **reads/dismiss/calls back from voicemail** , CCAI Platform updates session.

  * Contact creation

    * When an **IVR call** comes in with a new phone number, CCAI Platform creates a customer in Kustomer.

    * When the new app user (new identifier) starts the **CCAI Platform Mobile SDK** , CCAI Platform creates a customer in Kustomer.

  * Contact update

    * Customer assignment is updated when the call is assigned to the agent, if the customer is newly created.
  * Phone number

    * Send the phone number (including the country code) as a note in the conversation.
  * Chat transcript

    * A file is attached and appears in **Comments**.



## Manage CCAI Platform in Kustomer

For more information about installation see the [App installation and configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/kustomer/) section in Kustomer.

These steps guide you through how to update your app in your Kustomer account:

  1. Upgrade the UJET App in Kustomer, in the Kustomer application go to **Manage Apps** > **Manage your apps** > **Installed Apps** > **Attention required**.

  2. Click **UJET**.

  3. Click **Upgrade**.




## Manage agent status

You can manage agent status syncing between CCAI Platform and Kustomer using either a **one-way** sync (from Kustomer to CCAI Platform) or a **bi-directional** sync between the two platforms.

### Status mapping

Status mapping provides the ability to define how agent statuses in Kustomer correspond to agent statuses in CCAI Platform. Understanding and setting up these mappings is essential to ensure seamless synchronization of agent statuses between the two platforms.

  * **Many-to-one relation** : The mapping from Kustomer to CCAI Platform and follows a many-to-one relationship. Multiple agent statuses in one platform can map to a single status in the other.

  * **Flexibility** : There are no restrictions imposed on the mappings, giving you complete flexibility to define how statuses align between the two platforms. The choice of mappings is entirely at your discretion.

  * **Meaningful mappings** : It's essential to ensure that the mappings you establish between Kustomer and CCAI Platform are meaningful to your operations. Verify that your mappings accurately represent the agent statuses and their corresponding actions.




#### Map Kustomer statuses in CCAI Platform

User status **must be configured in your Kustomer account/platform** before you can follow the steps to map them to CCAI Platform statuses in our system. See the [Kustomer documentation](https://help.kustomer.com/en_us/user-statuses-H1qvvNnD7) for configuration details.

**Note:** There are no default statuses mapped; this is entirely up to you to define.

  1. In CCAI Platform portal, go to **Settings > Developer Settings > Agent Status Inheritance**.

  2. Toggle **Agent Status Inheritance** to **On**.

  3. Set the status inheritance:

     * **Status Inheritance at Login** : This field is inactive. There is no requirement to make a selection.

     * **Agent Status Prioritization** : his field is inactive. There is no requirement to make a selection.

  4. Set the status mapping, under **Status Mapping** click **Manage**.

     * The user statuses you have configured in Kustomer will appear as Kustomer statuses.

     * Map the Kustomer statuses to your CCAI Platform statuses using the drop-down menu.

  5. Click **Save** to save your changes.




**Example mapping configuration:**

Kustomer Status 1 → CCAI Platform Status A

Kustomer Status 2 → CCAI Platform Status A

Kustomer Status 3 → CCAI Platform Status B

Kustomer Status 4 → CCAI Platform Status D

In this example, an agent will be mapped to Status A in CCAI Platform when they are in Status 1 or 2 in Kustomer. If they are in Status 3 in Kustomer, they will be mapped to Status B in CCAI Platform, and so on.

### One-way sync from Kustomer to CCAI Platform

A one-way sync maps user status from Kustomer to CCAI Platform.

  * Create a unique user for each of your agents in both Kustomer and CCAI Platform. Make sure that no agents share a user.

  * Agents must sign in to both Kustomer and the CCAI Platform agent adapter inside the Kustomer CRM using the same email address. This is how the sync works.

  * Agents must be signed in to only a single Kustomer instance (tab, computer, and so on). If agents are logged in to Kustomer from several computers or in multiple tabs using the same user information, the sync won't work because it won't know which instance to update.

  * CCAI Platform status can be changed using a drop-down menu in the lower left corner of the Kustomer CRM page.




### Bi-directional (two-way) sync

You can streamline the management of agent statuses across Kustomer and CCAI Platform using the Agent Status Inheritance feature. Whenever an agent updates their status in Kustomer, CCAI Platform will reflect the mapped version of that status in our system.

  * User status _must be configured_ in your Kustomer account or platform in order for them to show up in our platform to map with our agent statuses. See the [Kustomer documentation](https://help.kustomer.com/en_us/user-statuses-H1qvvNnD7) for configuration details.

  * **Team Routing** and **External Queues** must be enabled and configured in your Kustomer account or platform. These sections are available in **Kustomer Routing Profile** > **General configurations**.

  * Each team that links to a CCAI Platform queue must have the Kustomer External Queues pointed to CCAI Platform. To do this select CCAI Platform from the External Queues drop-down. For the steps to enable team routing and select the external queues, see the Kustomer [Route conversations to agents](https://help.kustomer.com/routing-profiles-H1tz3ITv7) documentation.

  * To ensure that agent status syncs with CCAI Platform, agents need to set their selected team to the team linked to the external queue. It doesn't matter if they are part of multiple teams, because having External Queues enabled for additional teams won't affect this behavior.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
