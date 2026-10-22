---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-waiting/
title: Call waiting \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:35.632857+00:00
---

# Call waiting  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-waiting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call waiting Stay organized with collections  Save and categorize content based on your preferences. 

The call waiting feature enables agents to manage multiple inbound calls from different channels simultaneously. This enables agents to address a consumer call as well as a [direct inbound call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#direct-phone-numbers) from another agent (for example, to take a consult) at the same time.

Agents can seamlessly switch between calls, accept or decline incoming calls, and continue ongoing conversations without interruptions. This helps reduce missed or unanswered calls, shortens customer wait times, and ensures important communication is never missed. By streamlining communication processes, call waiting boosts overall efficiency and improves operational performance.

Call concurrency settings can be configured globally, at the queue level, and at the agent level to tailor how many calls each agent can handle simultaneously.

Agents can only receive **one call** at a time from the same direct number, extension number, or queue, even with call concurrency enabled. Agents are not able to take multiple consumer calls at once with this feature.

Here are some important things to consider:

  * [Auto answer](https://docs.cloud.google.com/contact-center/ccai-platform/docs/auto_answer) applies to direct inbound calls only if no other calls are active. If the agent is on a call, auto-answer does not activate.
  * When a call is placed on hold, agents can switch between active and on-hold calls. The longest on-hold call automatically becomes the next active call when one ends.

  * If a [direct number](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#direct-phone-numbers) is enabled, an agent in the wrap-up state is considered to still be on an active call, which contributes to their concurrency limit. This ensures agents have the necessary time to complete their post-call tasks effectively before taking on new calls.




## Permissions

Permissions for viewing and editing call waiting are given for the following groups:

  * View call waiting - manager and administrator

  * Edit call waiting - administrator




## Enable call waiting globally

Setting concurrency lets you determine the limit of inbound calls that a given agent can handle simultaneously.

**Note:** Admins can configure the number of inbound calls an agent is allowed to handle at the same time. The call concurrency limit can be set between 1 and 3 calls.

To enable call waiting globally, follow these steps:

  1. Go to **Settings** > **Call**.

  2. Scroll to **Direct Inbound**.

  3. Select the **Call Concurrency** checkbox.

  4. Choose the number of concurrent calls allowed (up to a maximum of 3).




This lets queues and agents to handle concurrent calls, with the default call limit set globally.

## Enable call waiting at the queue level

To enable call waiting at the queue level, follow these steps:

  1. Go to **Settings** > **Queue**.

  2. Select **Edit/View** in the IVR Queue.

  3. Scroll to **Inbound phone numbers**.

  4. Click **Configure**.

  5. Toggle Call Concurrency **on/off**.




Agents assigned to this queue are able to take concurrent calls based on the global limit.

## Enable call waiting at the agent level

To enable call waiting at the agent level, follow these steps:

  1. Go to **Settings** > **Users & Teams Settings**.

  2. Search for the agent you want to add to call waiting.

  3. Select **Edit User**.

  4. Go to the **Preferences** section.

  5. Toggle on **Call Concurrency**.

  6. Select a max concurrency number.




This setting overrides the global concurrency limit for the selected agent.

## Edit a phone number to allow for concurrent calls

  1. Go to **Settings** > **Call**.

  2. Click **Phone Number Management**.

  3. Search for the selected phone number.

  4. Select **Edit** phone number.

  5. Ensure **Set as a direct number** is selected.

  6. Check the **Set as a concurrent number** checkbox.

  7. Click **Save**.




You can also enable call waiting on a phone number when adding a new [direct phone number](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#direct-phone-numbers).

## Deflection settings

  * Queue and agent level deflection settings are honored for concurrent numbers. Deflection settings controls how unanswered or declined calls are managed.



## Agent experience

Agents can efficiently manage multiple inbound calls, switch between them, and deflect calls when necessary. Agents can:

  * **Receive New Calls** : agents can answer additional incoming calls while already on a call.

  * **Switch Between Calls** : when switching to another call, the current call is automatically placed on hold. The new call becomes active, allowing for transitions between conversations. The Agent Adapter has banners that indicate the current call sessions. Click these banners to switch between calls as needed.

    * These banners show a hold timer so the agent is always aware of how long the other calls have been holding.
  * **Manage Active Calls** : agents can perform various actions, such as ending a call, transferring it, or adding another participant to the conversation.




A single direct incoming call appears as the following in your call adapter.

![The indication for a single direct incoming call.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/single-direct-incoming-call.png)

Multiple incoming calls appears as the following, along with the length of time they have been on hold.

![The indications for multiple incoming calls on hold.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/multiple-calls-on-hold.png)

**Note:**

  * **Warm transfers** (transferring a call with a consultation) don't count toward the call concurrency limit.
  * **Cold transfers** (transferring a call without consultation) reduce the number of ongoing calls being handled.



## Reporting

  * **Average call concurrency** : The average number of calls handled simultaneously by an agent during a given time period.

  * Additional data such as call **offer, answer, decline, and deflection** metrics are also be available.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
