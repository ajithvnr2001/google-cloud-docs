---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms/
title: SMS messaging \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:49.625549+00:00
---

# SMS messaging  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  SMS messaging Stay organized with collections  Save and categorize content based on your preferences. 

_For pricing and implementation contact Support._

SMS Messaging is a way to chat with your consumers using text message. Because of its "anytime, anywhere" availability, SMS typically has higher engagement rates compared to other communication channels.

SMS Messaging provides the ability to:

  * Provide a seamless text messaging experience for your consumers.

  * Chat in multiple languages.

  * Receive images and videos from consumers.

  * Proactively reach out to consumers using outbound SMS.

  * Create flexible queues that route consumers to the correct agent.

  * Transfer chats between agents.

  * Implement multiple SMS support phone numbers for different business lines.




## Consumer experience

Receiving support through SMS should be like any other texting experience:

  1. A consumer sends a text to your incoming SMS support phone number or short code.

  2. The consumer receives an opt-in message, which covers requirements set forth by consumer privacy laws.

  3. If your SMS queue has multiple menu options, the consumer receives navigation instructions.

  4. An agent assigned to the queue responds to the consumer.




## Agent experience

SMS chats are handled by agents in the same Contact Center AI Platform (CCAI Platform) Adapter as Mobile and Web chats. From an agent's perspective, the experience is similar but there are notable differences related to consumer privacy.

## Agent statistics

SMS statistics are included in the following metrics:

  * Group statistics:

    * Your statistics

    * Team Average

  * Individual statistics:

    * Chats answered

    * Average duration




## Configuring SMS chat

To set up SMS chat, you need a phone number activated for SMS. If you don't have an activated SMS phone number, see Phone number activation for SMS.

### Chat settings

To configure chat settings for SMS, follow these steps:

  1. Turn on SMS chat.

  2. Configure SMS expiration and timeout settings.

  3. Configure SMS commands.

  4. To add SMS phone numbers, see Phone number activation for SMS.




For additional details, refer to [SMS chat settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-chat-settings)

### Queue settings

For SMS chat, you need to configure your queues.

To configure your queues for SMS, follow these steps:

  1. Click **Settings** > **Queues** > **SMS**.

  2. To configure queue level settings, to the following:

     * Hide any SMS queues that you don't need.

     * Specify any timeout and expiration settings.

     * Configure the system messages.

     * Add any menu keywords.

  3. Assign SMS numbers to queues.

  4. Assign agents and teams to SMS queues.




For more information, see [SMS messaging and queue settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#sms_messaging_and_queue_settings).

## SMS capabilities

Get a high-level overview of all the platform SMS features' capabilities using the following matrix:

| Blended SMS |  |  |  | Outbound SMS APIS (session based and session-less) |   
---|---|---|---|---|---|---  
| Wait time SMS | In call SMS | SMS channel | Pre-session SMS deflection | Outbound SMS API | Session-less SMS API  
The platform sends predefined messages | ✔ |  |  | ✔ | ✔ | ✔  
Agent can send custom messages |  | ✔ | ✔ |  |  |   
Agent can send predefined messages |  | ✔ | ✔ |  |  |   
Requires active IVR call | ✔ | ✔ |  |  |  |   
Starts with IVR, switches to SMS |  |  |  | ✔ |  |   
EWT threshold setting | ✔ |  |  | ✔ |  |   
Associated with an active session | ✔ | ✔ | ✔ | ✔ | ✔ |   
  
## CRM updates

When an incoming SMS chat is connected, or an outbound SMS chat is successfully sent, the CRM record is created or updated based on the consumer phone number.

  * If the phone number does not exist in the CRM, a new contact is created.

  * If the phone number exists in the CRM and is associated with a single contact, the CRM record is updated.

  * If the phone number is associated with multiple contacts, the agent is prompted to select an existing contact or create a new contact.




The following information is posted to the CRM record:

  * Chat ID, language, queue

  * Transfer began, failed, ended

  * Chat ended

  * Pictures and videos sent by the consumer




The chat transcript includes all SMS messages sent by the consumer, the agent, and the system (including queue selection messages & greeting messages.)

## Monitoring

Chat data is available on the following monitoring pages:

  * **Agents > Assigned Channel = Chats**:

This monitoring page displays aggregated real-time data from all chat channels.

  * **Chats** > **Ongoing Chats, Future Chats, Previous Chats** :

The **Queue** column identifies the chat channel.

The **Start Type** column identifies whether the chat was Manual Answer, Auto Answer, or Outbound.

  * **Queues** > **Chats** :

The **Queue Name** column identifies the chat channel.

The **Type Breakdown** column identifies the type of chat.




## Reporting

The following reports provide SMS Chat data:

  * **Users & Teams** > **Chat report**

  * **Calls & Chats** > **Chat Report**

  * **Queues** > **Chat Report**




SMS Chat data is also identified in both Performance Metrics and Individual Chat History reports.

Performance Metrics: The Type Breakdown column identifies Total SMS, Total Incoming SMS, and Total Outbound SMS.

Individual Chat History: The Type column identifies SMS and Outbound SMS.

## Phone number activation for SMS

Depending on the geographic location, existing numbers maybe able to be SMS activated. In other locations SMS specific numbers must be provided that are non geographic numbers. In all these cases you will need to contact Google Cloud support.

Numbers within the US can be activated for use with SMS, however, they have to follow the national 10 DLC (Digit Long Code) compliance process. "10DLC compliance" refers to a set of regulations established by US mobile carriers that govern how businesses can use standard 10-digit long code phone numbers (10DLC) to send text messages to customers, ensuring they are sending messages responsibly and with proper user consent, aiming to combat spam and protect consumers from fraudulent texts; essentially, it requires businesses to register their brand and campaigns with "The Campaign Registry" to send text messages using their regular phone numbers, and to adhere to guidelines regarding message content, opt-in procedures, and volume limits.

When a request is made to Google Cloud support to activate a US 10 digit phone number for SMS, specific information will need to be provided pertaining to the purpose and use of the phone number for SMS. Additional business information will also be requested. During the compliance validation phase, the business privacy policy pertaining to text messaging will be verified. The activation process can take several weeks to complete and so businesses are recommended to start this process as early as possible.

Once a phone number has been provided or activated by Google Cloud support, refer to [Adding phone numbers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-chat-settings#add-phone-numbers) to configure the phone number in CCAI Platform.

## SMS API

SMS messaging chat sessions can be tracked using the [Chat platform API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-chat) and invoked by the [SMS API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-api).

## SMS services

CCAI Platform offers several services that make use of the SMS channel. Each option has specific business needs it can solve and slightly different requirements and Capabilities.

  * **Blended SMS:** Requires an active IVR call for the duration of the SMS chat interaction.

    * In-call SMS

    * Wait time SMS

  * **SMS Channel:** SMS chats can be inbound and outbound independent of an IVR call.

    * **SMS inbound/outbound:** Phone number is provided to consumers and they can initiate SMS chat sessions by sending a text messages on their mobile device. Agents can also initiate outbound SMS chats.

    * **Pre-session SMS Deflection:** Caller dials into the IVR and then ends the IVR call to switch to the SMS channel.

  * **SMS to launch App:** Requires the Mobile SDK to already be installed in your company's app(s) and allows agents to prompt the opening of the app to utilize SmartActions.




### Blended SMS

_Requires an active IVR call for the duration of the SMS chat interaction._

#### Wait time SMS

This feature allows your team to send SMS messages to callers who are waiting to be connected to an agent. By enabling this feature, the caller will be able to provide necessary and important information to the agent in an SMS message. Ultimately, by enabling your callers to provide information about the reason for their call, the agent can make use of the information collected for a faster resolution time.

![Wait time SMS](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162fa5dc00ee7a.jpg)

#### In call SMS

During IVR calls, messages can be exchanged allowing agents to receive photos, videos, and screenshots from consumers, as well as exchange texts using MMS and SMS.

![In call SMS](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162fa5dc0121af.jpg)

For more information refer to [SMS Wait time SMS](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-wait-time).

### SMS channel

_SMS chats can be inbound and outbound independent of an IVR call._

SMS Messaging is a way to chat with your consumers using text messages. Implement multiple SMS support phone numbers for different business lines.

### Pre-session SMS

Caller dials into the IVR and then ends the IVR call to switch to the SMS channel.

Pre-session SMS Deflection provides you the ability to offer SMS chat support as an alternative option for IVR callers before the call is connected to an agent. This feature is configured at the IVR queue level and can be offered to callers conditionally based on the estimated wait times.

For more information refer to [Pre-session SMS Deflection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#pre-session_sms_deflection).

![Pre session SMS](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/162fa5dc0150c4.jpg)

### Send SMS to consumers to download your app

This feature allows agents to utilize Smart Actions by prompting the consumer to launch their app for your company. Once the app is installed and launched, Agents can use these SmartActions with a consumer during an IVR call.

For more information see [Send SMS to consumers to download Your app](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-download-app) and [Agent: Send SMS to Launch App for SmartActions during an IVR call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Sending_SMS_to_Launch_SmartActions/index.md#UUID-11c3da84-509c-e4ce-8b95-0f630f3a9ac0).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
