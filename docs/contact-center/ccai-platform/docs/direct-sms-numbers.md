---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/direct-sms-numbers/
title: Direct SMS numbers \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:10.904637+00:00
---

# Direct SMS numbers  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/direct-sms-numbers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Direct SMS numbers Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

This feature allows for inbound and outbound SMS communications directly between end-users and agents, streamlining the handling process and cutting down on wait times. Similar to [Direct Phone Numbers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#direct-phone-numbers), this feature allows customers to assign dedicated SMS numbers to agents, which consumers can access directly, ensuring seamless and direct text-based communication. This feature enhances the end-user experience by providing efficient SMS routing, customization options, and improved message management features.

## Prerequisites

The SMS feature must be turned **ON** in order to use Direct SMS numbers.

To turn on the SMS feature, follow these steps

  1. Go to **Settings > Chat > SMS**.

  2. Turn **Use SMS Chat** to **ON**.




## Add a direct SMS number

**Note:** A direct SMS number can only be assigned to one agent or one SMS queue. An agent can have up to 5 direct numbers assigned to them. A queue can have an unlimited number of direct numbers assigned to it.

To add a direct number to phone number management to assign to a queue or agent, follow these steps:

  1. Go to **Settings > Chat > SMS Phone Number Settings > Phone number management**.

  2. Select **\+ Add Number**.

  3. Enter the phone number (including country code).

  4. Select **Set as the direct number**.

  5. Create a label. This is used to identify the number added.

  6. Select **Add**.




Once added, direct numbers are indicated by a bold **Direct** tag next to the phone number in the phone number management area.

Direct SMS Numbers are marked as **Verified** status tag.

## Edit an existing number to mark as a direct SMS number

**Note:** Direct SMS numbers cannot be a shortcode or set as a global outbound number.

To edit an existing number, follow these steps:

  1. Go to **Settings > Chat > SMS Phone Number Settings > Phone number management**.

  2. Go to the phone number.

  3. Click the pencil icon on the far right of the phone numbers' row to edit the number.

  4. Select the **Set as a direct number** checkbox.

  5. Click **Save**.

  6. Click **Proceed**.




This saves the number as a direct SMS phone number and remove any outbound assignment for agents or queues.

## Unassign a direct SMS number

To unassign a number, follow these steps:

  1. Go to **Settings > Chat > SMS Phone Number Settings > Phone number management**.

  2. Select the phone number.

  3. Click the pencil icon on the far right of the phone numbers' row to edit the number.

  4. De-select the **Set as a direct number** checkbox.

  5. Click **Proceed**.




This removes the direct SMS number from any assigned queue or agent.

## Assign a direct number to a queue

Some information to note:

  * Phone numbers must be unique within all agents and SMS queues with direct numbers assigned.

  * If a number is assigned to an agent, it can't be assigned to an SMS queue.

  * If a number is assigned to an SMS queue, it can't be assigned to another SMS queue.

  * If a number is assigned to an IVR queue, it can be assigned to an SMS queue and vice versa.




To assign a direct number to a queue, follow these steps:

  1. Go to **Settings > Queue**.

  2. Click **Edit/View** on the SMS queue.

  3. Search for and select the required leaf queue.

  4. Go to **Inbound Phone Numbers** in the queue settings menu.

  5. Select **Configure**.

  6. Select **\+ Assign Number**.

  7. Select the required phone number from drop-downdown menu.

  8. Select **Assign**.

  9. Select **Save**.




## Assign a direct number to an agent

**Note:** A direct SMS phone number can only be assigned to an agent OR an SMS queue. Once marked as a direct SMS number, the same number cannot be used as a global outbound number.

To assign a direct number to an agent:

  1. Go to **Settings > Users > Teams**.

  2. Search for the required agent.

  3. Click the **Options** menu (three dots) to the right of the user's row.

  4. Select **Edit user**.

  5. Go to **Direct Inbound** in the edit user window.

  6. Click the **down arrow** to the left of the Direct Inbound option.

  7. Click **\+ Assign number**.

  8. Select the required phone number from the drop-down menu.

  9. Click **Assign**.

  10. Click **Update**.




## Bulk assign direct numbers

Phone numbers can be assigned to multiple agents at the same time using the [Bulk user management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management) feature.

  * A phone number must be unique within all Direct Inbound Number columns.

    * If it's not, then the respective error message is added to the error log file. 
      * Each direct inbound number must be unique for an agent.
  * If a phone number is not in the correct format or is not validated in our system, then it is ignored, and the respective error message is added to the error log file.

    * The phone number is in the incorrect format.

    * The phone number is not validated on the system.




## Configuring direct SMS numbers globally

To configure the settings for Direct SMS Numbers, there must be at least one dedicated direct inbound phone number assigned and validated for SMS.

### Direct numbers

To configure global settings for a direct number, follow these steps:

  1. Go to **Settings > Chat > Direct Numbers Global Settings**.

  2. Turn **ON** the **Global SMS after-hours deflection** setting.

  3. Once turned on, you can configure the hours of operation and the after-hours deflection message. When changes have been made, select **Save Direct Numbers Global Settings**.




### Direct inbound SMS

To configure direct inbound SMS, follow these steps:

  1. Go to **Settings > Chat > Direct Inbound SMS**.

  2. From here you can configure the **Missed Chat Threshold** and the **Unresponsive Threshold**. The default value for both is `2`.

  3. When changes have been made, select **Save Direct Inbound**.




## Configuring direct SMS numbers at a user or team level

### Teams Level

To configure SMS deflections at the team level, follow these steps:

  1. Go to **Settings > Users & Teams > Teams**.

  2. Choose the team you want to configure and select the **Edit** button (pencil icon).

  3. Go to **Agent SMS deflections > Agent After Hours Deflection >** Turn **ON**. This changes the inheritance status from **Global** to **Team** level. This can be reverted at any time by selecting **Reset to Global**.

  4. Once turned on, you can make changes to the hours of operation and the after-hours deflection message.

  5. Select **Update** to save changes.




### Users Level

To configure SMS deflections at the team level, follow these steps:

  1. Go to **Settings > Users & Teams > Users**.

  2. Choose the user you want to configure and select the **ellipsis button** (three dots) next to the user. Select **Edit User.**

  3. Go to **Agent SMS Deflections**. From here you can select if you wish for the agent to be able to configure their own extension deflection options in the **Agent Permission** section, and you can also turn on **Agent after-hours deflection.**

  4. Once **Agent after-hours deflection** is turned **ON** , the hours of operation and the after-hours deflection message can be configured.

  5. Select **Update** to save changes.




## Routing

It is recommended that each agent assigned a direct SMS number has a personal queue where all direct SMS chats to them are routed. 

If a chat is sent to an inbound SMS number assigned to a queue (one or more assigned direct SMS numbers), then all team members in that queue receives the SMS message.

## Reporting updates

A chat coming into or from a direct SMS number displays the following session types:

  * Messaging Inbound (SMS Direct)

    * Both to agents and to queues
  * Messaging Outbound (SMS Direct)

    * Both for agent's and queues' direct SMS numbers

**Note:** Any SMS session that starts as a direct inbound SMS session retains this session type regardless of transfer between agents and or to queues.

## Agent experience

For more information on agent experience, see [Configure SMS chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-sms-chat).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
