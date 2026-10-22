---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/direct-phone-numbers/
title: Direct phone numbers \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:13.671588+00:00
---

# Direct phone numbers  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/direct-phone-numbers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Direct phone numbers Stay organized with collections  Save and categorize content based on your preferences. 

A direct phone number is a dedicated, unique phone number that connects callers directly to a specific agent or IVR queue, bypassing the main menu tree. This facilitates faster communication for known contacts and creates distinct inbound channels for your teams.

A direct number is unique across your entire organization and can only be assigned to a single agent or a single queue at one time. This differs from [Direct Access Points (DAPs)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dap), which are only unique at the queue level. This uniqueness is reflected in reporting, where calls to direct numbers are logged with a unique session type for clear analysis.

This guide explains how to create, assign, and configure the behavior of direct phone numbers.

## Prerequisites

Before you begin, ensure the following requirements are met:

  * **Purchased numbers** : You must have available phone numbers in your account that can be designated as direct numbers.

  * **Administrator permissions** : You must have **Administrator** permissions to access **Settings > Call** and **Settings > Users & Teams**.

  * **Created agents** or **Created queues:** The agents or IVR queues that you assign numbers to must already exist in the system.




## Set up direct numbers

To add a direct number, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call > Phone Numbers > Phone Number Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Click **\+ Add Number**.

  3. Enter the phone number, including the country code.

  4. Select the **Set as the direct number** checkbox.

  5. Optional: Select the **Set as a concurrent number** checkbox to allow multiple simultaneous calls to this number, which is required for features like call waiting.

  6. In the **Label** field, enter a descriptive label.

  7. Click **Save**.




The number is added to your phone number list and tagged as **Direct** , making it available for assignment to an agent or queue.

To verify that the number has been added, look at the **Phone number management** list, and confirm that the newly added number has a **Direct** tag next to it.

### Assign a direct number to an agent

To assign a direct number to an agent, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Users & Teams**. If you don't see the **Settings** menu, click menu **Menu**.

     1. For the agent that you want to edit, click more_horiz **Edit user**.

     2. Go to the **Direct Inbound** section and expand it.

     3. Click **\+ Assign Number**.

     4. In the **Assign Number** field, select the direct number.

     5. Click **Assign** , then click **Update** to save the user's profile.




The agent can now receive calls directly on this number. An agent can have up to five direct numbers assigned.

You can call the direct number to confirm that the call is routed directly to the assigned agent's adapter.

### Assign a direct number to a queue

To assign a direct number to a queue, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Settings** pane, select **Edit/View** on the main IVR tree and navigate to the leaf queue.

  3. Click the queue that you want to edit.

     1. In the queue settings, find the **Inbound Phone Numbers** section and click **Configure**.

     2. Click **\+ Assign Number** and select the direct number.

     3. Click **Assign** , then click **Save**.

Calls to this number will now route directly to this queue, following the queue specific routing and deflection logic. A queue can have an unlimited number of direct numbers.




You can call the direct number and confirm that you enter the assigned queue flow—for example, you hear its specific hold music or agent search process.

## Configuring direct number behavior

### General call handling (global)

To configure default call handling, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call > Direct Inbound**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Configure these settings:

     * **Enable Declining call for direct inbound calls** : Select this checkbox to enable declining calls for direct inbound calls.

     * **Enable Auto-Answer for direct inbound calls to agents** : Select this checkbox to enable auto-answer for direct inbound calls to agents.

  3. Click **Save Direct Inbound**.




When the **Decline Button** is enabled, agents see a **Decline** button for incoming direct calls. When the setting is turned off, the button is hidden. For calls to a deltacast queue, a declined call proceeds to the next available agent.

When **Auto-Answer** is enabled, direct calls to an agent are answered automatically. Calls to a queue follow that queue's auto-answer setting.

To verify that "Declining call" is working, call an agent's direct number. Verify that the **Decline** button is visible. Turn it off and verify that the button is hidden.

To verify that "Auto-Answer" is enabled and working, call an agent's direct number. Verify that the call connects automatically without the agent clicking "Accept".

### Agent call deflections

Direct-to-agent calls follow the existing agent call deflection settings.

To set up agent call deflections, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Users & Teams**. If you don't see the **Settings** menu, click menu **Menu**.

  2. For the agent that you want to configure settings for, click more_horiz **Edit user**.

  3. Go to **Agent Call Deflections** , and then configure the following settings:

     * **Inheritance** : Deflection settings are inherited in the following order of precedence: **Global < Team < Agent**. The most specific setting takes precedence.

     * **Overcapacity Deflection** : If a direct call arrives when the agent is over capacity, the call is deflected according to the configured rule—for example, it's sent to voicemail or to a different queue.

     * **After Hours Deflection** : If a direct call arrives during the agent's configured after-hours, it's deflected as specified.

     * **Automatic Redirection** : If enabled, all direct calls to the agent are immediately redirected to the chosen destination.




To verify that agent call deflections are working, follow these steps:

  1. Set an "After Hours" deflection for a specific agent to deflect to voicemail.

  2. Call that agent's direct number during a time you have configured as "after hours."

  3. Verify that the call is immediately sent to the agent's voicemail as expected.




### Understanding call priority

The system uses the following logic to prioritize direct inbound calls.

Calls are prioritized as follows:

  1. **Direct-to-Agent Calls** : The call's priority is determined by the **Agent's queue priority setting** found in their user profile.

  2. **Direct-to-Queue Calls** : The call's priority is determined by the **Queue's priority setting** configured in the queue's menu settings.




To verify the call priority, follow these steps:

  1. Set a high queue priority in an agent's user profile.

  2. Ensure that agent is also a member of a low-priority queue.

  3. Simultaneously send one call to the agent's direct number and another call to the low-priority queue.

  4. Confirm that the direct call is offered to the agent before the queue call.




### Call recording

To record direct inbound calls, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Call > Call Details**. If you don't see the **Settings** menu, click menu **Menu**.

  2. For **Call Recording** , select the **Record Direct Inbound Calls** checkbox.

  3. Click **Save Call Details**.




This global setting enables call recording for all inbound calls, which includes calls made to direct phone numbers.

To verify that the setting is enabled, make a call to a direct number and confirm that a recording is generated for the session.

## Reporting

Calls made to or from a direct phone number are identified with the following session types for accurate reporting:

  * **Voice Inbound (Direct)** : for all inbound calls received from a direct number

  * **Voice Outbound (Direct)** : for all outbound calls made using a direct number as the caller ID

  * **Voice Internal** : for calls made between two direct numbers within your organization




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
