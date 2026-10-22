---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-chat-settings/
title: SMS chat settings \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:09.314405+00:00
---

# SMS chat settings  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-chat-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  SMS chat settings Stay organized with collections  Save and categorize content based on your preferences. 

To configure SMS Chat, start by reviewing the global and SMS chat settings in the CCAI Platform portal.

## Configuring global chat settings

Go to **Settings** > **Chat** and review the **Global Chat Settings** , which apply to all chat channels (Mobile, Web, and SMS):

### Dismissed chat auto response

If you turn on the **Inactive Chats** dismissal feature, a default **Dismissed Chat Auto Response** is provided. This response is sent only when a consumer replies to a dismissed SMS chat.

### Chat shortcuts

In order to help agents comply with consumer privacy regulations, create at least one chat shortcut that covers the requirements of an opt-in message. Agents should use this shortcut as their first message when sending an Outbound SMS chat.

  1. Navigate to the **Chat Shortcuts** section and click **View all shortcuts** :

  2. Click **Add Shortcut:**

  3. Optionally enter a **Category** if you want to group this shortcut with others.

  4. Enter a **Shortcut Keyword**.

  5. Enter your **Message** text and click **Save**.




For more information on chat shortcuts, see [Chat settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-shortcuts).

## Turning on SMS chat

  1. Go to **Settings** > **Chat.**

  2. From the left navigation, click **SMS**.

  3. Toggle **Use SMS Chat** to **On** :

  4. If you want agents to have the ability to initiate SMS chat sessions, navigate to **Outbound SMS** and toggle **On:**




### Configuring SMS expiration and timeout settings

SMS Chat has its own expiration and timeout settings:

Chat expiration applies to only incoming SMS chats. These global settings are overridden if you set them on the queue level.

## Configuring SMS Commands

In order to comply with consumer privacy laws, certain SMS command words are preconfigured and cannot be changed, as shown in the first three rows of this table:

|   
---|---  
**Consumer command** | **Behavior**  
STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT | Turn off all messages and be placed on a don't contact list  
START, YES, UNSTOP | Opt in to receiving messages. If previously placed on a don't contact list, be removed from that list  
HELP, INFO | Receive support contact information  
BACK (configurable) | Go back to the previous menu selection  
EXIT (configurable) | End the chat. If "exit" is the first message sent by the consumer, no chat is created  
  
Two default command words, BACK and EXIT, are provided to help consumers navigate SMS queues. Administrators can change or add to these keywords:

  1. Go to **Settings** > **Chat**.

  2. From the left navigation, click **SMS**.

  3. Go to **SMS End User Commands**.

  4. Enter command words then click **SET COMMANDS:**




Use any combination of characters as long as they don't conflict with queue names or protected words, as listed in the previous table.

## Adding SMS phone numbers

Add and verify the numbers on the **Phone Number Management** page.

Upon your first-time activating a valid US (+1) phone number, the following section displays. Enter your number in the field and click **Activate**. This section does not display if you have already enabled SMS messaging and entered a valid number.

![phone number management](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162fa5dc07812e.png)

Keep these points in mind:

  * If you are using the **In Call SMS** feature, you cannot reuse those phone numbers for SMS Chat.

  * Each incoming number can be assigned to _one queue only_. Each queue can have multiple incoming numbers, as long as each number is unique.

  * Incoming numbers can be used as outbound numbers but outbound numbers cannot be used for incoming numbers.

  * Outbound numbers can be assigned to multiple queues and each queue can have multiple outbound numbers.

  * SMS numbers can have different sending limits.




To add the SMS phone numbers:

  1. Go to **Chat** > **Settings**.

  2. From the left navigation, click **SMS**.

  3. Go to **SMS Phone Number Settings** and click **Phone Number Management** :

  4. On the Phone Number Management page, click **Add a Number:**

  5. Add the unique phone number including country code:

     * Leave **Set as the global outbound number** unchecked.

     * Add a **Label** that helps you identify the number.

     * Repeat for each phone number.

  6. Select all of your new phone numbers and click **Verify**. A number must be verified before you can assign it to a queue.

Once the system has verified a phone number, the status is displayed as, **Verified for Only SMS Messaging**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
