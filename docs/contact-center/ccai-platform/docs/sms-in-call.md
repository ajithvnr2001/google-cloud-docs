---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-in-call/
title: In call SMS \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:06.461037+00:00
---

# In call SMS  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-in-call/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  In call SMS Stay organized with collections  Save and categorize content based on your preferences. 

SMS blending enables Smart Actions during IVR calls for MMS capable numbers, allowing agents to receive photos, videos, and screenshots from consumers, as well as exchange text messages using MMS and SMS respectively.

## Key features

SMS usage is tracked in performance metrics, call history reports, and API data.

### Sending messages to callers

  * Agents can send preset or custom text messages during IVR calls using SMS (without the caller having a mobile app installed).

  * SMS messages can only be received by phones that can receive and send text messages.

**Note:** Agents should confirm consumer's device is capable of receiving SMS before initiating the session.
  * Agents can send text messages and links to mobile-friendly web pages (no pictures or videos at this time).




### Receiving messages from callers

  * Text messages, videos, and images (jpg, png, and gif) can be received.



## Enabling and configuring in call SMS

  1. Go to **Settings** > **In Call SMS**.

  2. Enable In Call SMS by toggling the switch to **ON**.




### Adding SMS phone numbers

Add and verify the numbers on the **Phone Number Management** page.

Upon your first-time activating a valid US (+1) phone number, the following section displays. Enter your number in the field and click **Activate**. This section does not display if you have already enabled SMS messaging and entered a valid number.

![Phone number activation display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162fa5dc07812e.png)

The following points should be considered:

  * If you are using the **In Call SMS** feature, you cannot reuse those phone numbers for SMS Chat.

  * Each incoming number can be assigned to _one queue only_. Each queue can have multiple incoming numbers, as long as each number is unique.

  * Incoming numbers can be used as outbound numbers but not conversely.

  * Outbound numbers can be assigned to multiple queues and each queue can have multiple outbound numbers.

  * SMS numbers can have different sending limits.




To add the SMS phone numbers:

  1. Go to **Chat > Settings.**

  2. From the left navigation, click **SMS.**

  3. Go to **SMS Phone Number Settings** and click **Phone Number Management:**

  4. On the Phone Number Management page, click **Add a Number:**

  5. Add the unique phone number including country code:

     * Leave **Set as the global outbound number** unchecked.

     * Add a **Label** that helps you identify the number.

     * Repeat for each phone number.

  6. Select all of your new phone numbers and click **Verify**. A number must be verified before you can assign it to a queue.

Once the system has verified a phone number, the status is displayed as, **Verified for Only SMS Messaging.**




## Set up feature options and messages

Messages and optional features for SMS In Call can be configured through the CCAI Platform portal.

### Non-US phone number configurations

As outlined in the CCAI Platform portal, there may be conflicts when sending messages out to non-US numbers, based on the global carrier's unique settings. Since it's not possible for CCAI Platform to know or predict compatibility, you choose to enable or disable this feature for non-US numbers.

Mark the settings for either **In Call SMS** or **Wait Time SMS** , respectively, then click **Set**.

### Preset messages by administrators

Messages set up in the CCAI Platform portal will be available for all Agents from within the Chat Adapter. The Agent will see the list of created messages and be able to click each message to send when appropriate.

  1. In the CCAI Platform portal, go to **Settings** > **In Call SMS**.

  2. Navigate to the **In Call SMS Session** > **Preset Messages by Admin** section.

  3. When enabled, the agent will only be able to select from the messages created by an Admin.

  4. To add new messages, first select the language of the message. If you are using multiple languages in your IVR, repeat the following steps for each active language you will be using SMS for.

  5. Click **Add SMS Message**.

  6. Enter the **label** of the SMS message as the Agent will see it in their widget/adapter, then enter the **SMS message** content and click **Save**. Be mindful of the character count of the message as most SMS messages cannot contain more than 160 characters in one message.

  7. Repeat these steps for each message you would like to be available for agents.




### Custom messages by Agent

Aside from the messages set up by an administrator, the Agent can also create their own text-based messages during the SMS exchange. To enable this feature, select the checkbox and click **Set**.

_Max characters per SMS message the agent can send: 918 characters._

#### Finished in call SMS session messages

SMS sessions are ended as soon as the call has ended, regardless of the reason for the call termination, and no new messages will be added to the ticket or case or available in the agent adapter. The following are two optional but recommended messages that can be customized and sent by default after the SMS session has completed.

  1. Go to **Settings** > **In Call SMS**.

  2. **Click the checkbox to enable** and **select the language** for the Closing SMS message.

  3. **Compose** the Closing SMS message to be sent to the caller as soon as the call has ended.

  4. Click **Set** to save the message and settings.

  5. **Click the checkbox to enable** and **select the language** for the SMS Auto Response message. This message will prevent any confusion that the caller may have if they try to start a new conversation or continue the existing conversation after the call has ended.

  6. **Compose** the SMS Auto Response message to be sent to the caller if they try to send any messages after the call has ended.

  7. Click **Set** to save the message and settings.




## Individual queue configuration

Once enabled for the environment, you can configure this feature on a queue-by-queue basis. Enable the feature for your chosen queue by going to **Settings** > **Queue** > **IVR** , then clicking on the specific queue to enable.

![SMS In call per queue](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162fa5dc116153.png)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
