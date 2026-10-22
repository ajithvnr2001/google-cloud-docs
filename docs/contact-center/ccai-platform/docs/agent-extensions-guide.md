---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-extensions-guide/
title: Agent extensions guide \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:27.763736+00:00
---

# Agent extensions guide  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-extensions-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent extensions guide Stay organized with collections  Save and categorize content based on your preferences. 

Agent extensions allow agents to be assigned a phone number extension for agent to agent and end-user to agent calling.

This document walks you through the Call Adapter functions directly impacted by the addition of agent extensions.

## Dial pad and extension directory

If you are an agent with an extension assigned, you are able to dial extensions. The dial pad communicates this in the number entry field. There will also be two tabs, Dialpad and Directory, at the top of the dialer.

  * To dial a known extension, enter the star key and extension number.

  * To dial an external number, enter the number as normal.




## Access the extension directory

To use the extension directory, click the **Directory** tab. The default view shows all agent extensions and an indicator of the agent's availability.

  * An empty circle indicates the agent is unavailable.
  * A green filled circle indicates the agent is available.

  * You can use the search field to search for an agent by name or extension.

  * You can filter the list to show only available agents.




## Search the extension directory

Click in the search field and begin typing a name in order to search for an agent extension. A list will appear showing all agents that meet the search criteria along with their availability.

If no agents meet the search criteria, a message will appear indicating that there are no available agents to contact.

## Receive an internal call

When an internal call comes in from another agent, the agent's name and extension appear under **Calling from** on the **Incoming call** screen.

You can click **Answer** to answer the call, or **Decline** to decline the call. When you receive an internal call, the **Agent Assist** and **Smart Actions** buttons do not appear on the **Call** screen.

## Set deflections for extension calls

If your administrator gives you permissions, you can set deflections for agent to agent calls or end-user to agent calls.

### Set after-hours deflections

You can set deflections for extension calls that are made outside your working hours.

To set after-hours deflections, follow these steps:

  1. In the CCAI Platform portal, click call **Call**. The call adapter appears.

  2. Click more_vert **Options**. The **Options** pane appears.

  3. Next to **Agent Deflections** , click chevron_right **Forward**. The **Agent Deflections** pane appears.

  4. Next to **After hours deflection** , click chevron_right **Forward**. The **After hours deflection** pane appears.

  5. Click the **After hours deflection** toggle to the on position.

  6. To set your call availability hours, do the following:

     1. Next to **Call availability hours** , click chevron_right **Forward**. The **Call availability hours** pane appears.

     2. To set your call availability hours, do the following:

        1. Next to **Time Zone** , click chevron_right **Forward**.

        2. Select your time zone, and then click chevron_left **Back**.

     3. Under **Days and Hours of Operation** , select one of the following:

        * **24 hour operation**.

        * **Weekdays / Weekends** : Set your weekday availability hours, your weekend availability hours, or both.

        * **S / M / T / W / T / F / S** : For each day that falls within your availability hours, select the day and set the hours.

     4. To select the holidays to observe, do the following:

        1. Next to **Holidays to Observe** , click chevron_right **Forward**. The **Select Holidays** pane appears.

        2. Select the holidays that you want to fall outside of your working hours. Your administrator configures the available holidays. For more information, see [Holidays](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hours-of-operation#holidays).

        3. Click chevron_left **Back**.

     5. Click **Save call availability hours**. The **After hours deflection** pane appears.

  7. Under **Options** , select one of the following:

     * **Message**. The message options appear. Do one of the following: 
       * Enter a text-to-speech message.
       * Select **Upload audio recording** , and then upload an audio recording file with your message.
     * **Phone number or Outbound SIP transfer**. Select one of the following options that appear: 
       * **Phone number**. In the field that appears, enter the phone number that you want calls deflected to.
       * **Extension number**. In the field that appears, enter the agent extension that you want calls deflected to.
       * **SIP URI Address**. In the field that appears, enter the SIP URI address that you want calls deflected to.
       * **Select from contact list**. To select from a contact list, do the following: 
         1. Next to **Select SIP URI** , click chevron_right **Forward**. The **Select SIP URI** pane appears.
         2. Select the contact that you want the call deflected to, and then click chevron_left **Back**. The **After hours deflection pane appears**. **Note:** The contacts that appear are from your personal contact list. For more information, see [Contact lists](https://docs.cloud.google.com/contact-center/ccai-platform/docs/contact-list). 
     * **Voicemail**. The message options appear. Do one of the following: 
       * Enter a text-to-speech message.
       * Select **Upload audio recording** , and then upload an audio recording file with your message.
  8. Click **Save deflection**.

  9. Click close **Close** to return to the **Call** tab.




### Set overcapacity deflections

You can set deflections that redirect extension calls when you're at capacity.

To set overcapacity deflections, follow these steps:

  1. In the CCAI Platform portal, click call **Call**. The call adapter appears.

  2. Click more_vert **Options**. The **Options** pane appears.

  3. Next to **Automatic redirections** , click, chevron_right **Forward**. The **Automatic redirections** pane appears.

  4. Click the **Automatic redirections** toggle to the on position.

  5. Under **Options** , select one of the following:

     * **Message**. The message options appear. Do one of the following: 
       * Enter a text-to-speech message.
       * Select **Upload audio recording** , and then upload an audio recording file with your message.
     * **Phone number or Outbound SIP transfer**. Select one of the following options that appear: 
       * **Phone number**. In the field that appears, enter the phone number that you want calls deflected to.
       * **Extension number**. In the field that appears, enter the agent extension that you want calls deflected to.
       * **SIP URI Address**. In the field that appears, enter the SIP URI address that you want calls deflected to.
       * **Select from contact list**. To select from a contact list, do the following: 
         1. Next to **Select SIP URI** , click chevron_right **Forward**. The **Select SIP URI** pane appears.
         2. Select the contact that you want the call deflected to, and then click chevron_left **Back**. The **After hours deflection pane appears**. **Note:** The contacts that appear are from your personal contact list. For more information, see [Contact lists](https://docs.cloud.google.com/contact-center/ccai-platform/docs/contact-list). 
     * **Voicemail**. The message options appear. Do one of the following: 
       * Enter a text-to-speech message.
       * Select **Upload audio recording** , and then upload an audio recording file with your message.
     * **Keep Waiting**. Calls continue to ring until the caller hangs up.
  6. Click **Save deflection**.

  7. Click close **Close** to return to the **Call** tab.




### Set automatic redirections

You can set deflections that automatically redirect extension calls.

To set automatic redirections, follow these steps:

  1. In the CCAI Platform portal, click call **Call**. The call adapter appears.

  2. Click more_vert **Options**. The **Options** pane appears.

  3. Next to **Automatic redirections** , click chevron_right **Forward**. The **Automatic redirections** pane appears.

  4. Click the **Automatic redirections** toggle to the on position.

  5. Under **Options** , select one of the following:

     * **Message**. The message options appear. Do one of the following: 
       * Enter a text-to-speech message.
       * Select **Upload audio recording** , and then upload an audio recording file with your message.
     * **Phone number or Outbound SIP transfer**. Select one of the following options that appear: 
       * **Phone number**. In the field that appears, enter the phone number that you want calls deflected to.
       * **Extension number**. In the field that appears, enter the agent extension that you want calls deflected to.
       * **SIP URI Address**. In the field that appears, enter the SIP URI address that you want calls deflected to.
       * **Select from contact list**. To select from a contact list, do the following: 
         1. Next to **Select SIP URI** , click chevron_right **Forward**. The **Select SIP URI** pane appears.
         2. Select the contact that you want the call deflected to, and then click chevron_left **Back**. The **After hours deflection pane appears**. **Note:** The contacts that appear are from your personal contact list. For more information, see [Contact lists](https://docs.cloud.google.com/contact-center/ccai-platform/docs/contact-list). 
     * **Voicemail**. The message options appear. Do one of the following: 
       * Enter a text-to-speech message.
       * Select **Upload audio recording** , and then upload an audio recording file with your message.
  6. Click **Save deflection**.

  7. Click close **Close** to return to the **Call** tab.




## Call history

If you have an extension assigned to you, your **Call History** screen will contain an extra tab, **Internal**. This Internal tab will show all calls originating from internal extensions, regardless of the call status.

Answered calls, missed calls, and deflected calls have their own separate icons indicating the status of the call.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
