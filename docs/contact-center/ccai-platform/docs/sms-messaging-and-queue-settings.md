---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-messaging-and-queue-settings/
title: SMS messaging and queue settings \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:43.159657+00:00
---

# SMS messaging and queue settings  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-messaging-and-queue-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  SMS messaging and queue settings Stay organized with collections  Save and categorize content based on your preferences. 

Once SMS Messaging is enabled and you have configured chat settings, you can begin setting up SMS messaging queues.

## SMS menu structure

SMS chat queues can have a single queue structure or a set of nested queues.

For multi-language queues, set up a top-level queue for each language so that consumers are first prompted to select a language.

Example:

Please text a number to select a menu. Text 1 for English Text 2 for French Text 3 for Korean **1** You have selected English support. Please text a number to select a menu. Text 1 for Payments Text 2 for Billing Text 3 for All other enquiries  
---  
  
When naming your queues, keep in mind that you cannot use protected SMS command words in queue names, including:

  * STOP, STOPALL, UNSUBSCRIBE, CANCEL, END, QUIT

  * START, YES, UNSTOP

  * HELP, INFO

  * Command words for EXIT (configurable on Chat settings page)

  * Command words for BACK (configurable on Chat settings page)




If you try to name the queue using a protected word, an error message is displayed.

## Add and edit SMS queues

To add and edit SMS queues:

  1. Go to **Settings > Queue > SMS Messaging**.

  2. Click **Edit**.

  3. If you have queues set up in another channel (IVR, Mobile, or Web), you can copy their structure by clicking **Copy Queue From**. This replaces any existing queues in the SMS channel.

  4. To create a new queue, click into the **New Item** line and type the first queue name.

  5. To create additional queues:

     1. Press **enter** to create a new queue.

     2. Press **enter + tab** to create a branch or leaf queue.

     3. Press **shift + tab** to go back.

  6. To delete a queue, click **X** next to the queue name.

  7. To move queues up or down, click the grid icon next to a queue name and drag to the new location.

  8. Click **Done** to save your new queue structure.




## Configure queue-level settings

SMS settings can be applied at the top, sub-queue, or leaf queue level. Top-level queue settings are inherited by sub queues unless they are overridden by their own settings.

### Hide SMS queues

There is an option to hide an SMS queue so that end-users are not presented with the menu option for that queue. If the queue has an incoming number assigned, messages sent to that number are delivered, even if the queue is hidden.

### Timeout and expiration settings

Global timeout settings for SMS chats are configured on the **Settings > Chat** page but you can override them at the queue level.

### SMS system messages

Two types of system messages can be configured for SMS chats, **Greeting** and **After Hour**.

  * **Greeting message:** The greeting message is sent as soon as an incoming SMS message is received. If the queue has multiple sub-queues, the greeting message is sent before the sub queue selection message.

The greeting message is especially important because your first contact with the end-user using SMS needs to include standard opt-in text. For more information, see [SMS messaging and privacy](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-consumer-privacy).

To provide consumers with an estimated wait time as part of your greeting message, use the dynamic variable, @{EWT_minutes}. This variable can be used only at the leaf queue level.

  * **After hour message** : The after hours message is sent when an incoming SMS message is received outside of the Operation Hours, as set on the **Settings > Support Center Details** page.




Every queue can have its own hours of operation. To set these hours, go to **Settings > Support Center Details > Add Custom Operation Hours.**

The concept of overcapacity and after hour deflection does not apply to SMS chat.

## Queue keywords

When an end-user texts a Top-level queue, the system automatically prompts the end-user to enter a number associated with a sub queue (based on the order in which you have listed your queues on the **Queue Menu Setting** page.)

You can also add keywords to queues. When the keyword is entered by the end-user, they are taken directly to that queue. In this example, the keyword "pay" has been assigned to the Payments queue.

## Assign SMS numbers to queues

If you have not yet added and verified SMS phone numbers on the Phone Number Management page, see [Adding SMS numbers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/SMS#UUID-97218631-64c9-0b26-7d47-629ab39d12e0).

You can assign incoming and outbound SMS numbers to top-level, sub-queue, and leaf queues. Keep the following in mind:

  * Incoming SMS phone numbers can be assigned to only one queue (a queue can have multiple incoming numbers as long as they are not used for any other queue.)

  * Outbound SMS phone numbers can be assigned to any number of queues and a queue can have any number of outbound phone numbers. Agents are prompted to pick one when initiating an outbound chat.

  * Any agents assigned to the queue can use any of the outbound phone numbers; therefore, If you want an agent to have their own number, they must have their own leaf queue.

  * If a end-use sends a text to a phone number that is not assigned to a queue, they won't receive a response.




Every SMS queue settings page has an option to assign incoming and outbound numbers. The drop-down list displays any SMS number that is verified and available to be used.

When adding outbound numbers, be sure to toggle **Outbound SMS** to **On**.

### Assign agents and teams to SMS queues

As with any call and chat queue, agents and teams are assigned at the leaf queue level.

For more information, see [Setting Up and Assigning Agents to Channels and Queues](https://docs.cloud.google.com/contact-center/ccai-platform/docs/setup-agents-channels).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
