---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-wait-time/
title: Wait time SMS \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:17.538528+00:00
---

# Wait time SMS  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-wait-time/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Wait time SMS Stay organized with collections  Save and categorize content based on your preferences. 

This feature allows your team to send SMS messages to callers who are waiting to be connected to an agent. By enabling this feature, the caller will be able to provide necessary and important information to the agent using SMS. Ultimately, by enabling your callers to provide information about the reason they are calling in, the agent can make use of the information collected for a faster resolution time.

Wait time SMS includes the following capabilities:

  * Sending preset, custom text messages while the caller is waiting in queue on IVR calls using SMS.

  * Make the best use of your caller's time by using time spent waiting in queue proactively.

  * Opening the SMS channel for the caller to send multimedia messages with relevant content.

  * By enabling the customer to provide crucial information to the agent or company before connecting with an agent, you can expect a decrease in average handle time.




## User flows

The caller and the agent have a unique experience while using this feature. While the agent's experience is always the same, the caller has the option of whether or not they will take part in the SMS exchange.

### User flow: caller

The following are the steps over the caller user flow:

  1. Caller dials into your IVR.

  2. Caller enters the queue after selecting the queue or being placed in a queue by a direct access point. More info in [Direct Access Points](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup/index.md#UUID-afeb7774-cb09-60c3-01d0-362b3843a7b6).

  3. Overcapacity limit has been reached by the queue (settings can be adjusted in [Call settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings.md#UUID-5471c8bb-7f98-93fc-ebfc-70e8d560c6b8)).

  4. Caller is played the configured overcapacity options (settings can be adjusted in [Call Settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings.md#UUID-5471c8bb-7f98-93fc-ebfc-70e8d560c6b8)) and selects "keep waiting."

If anything but "keep waiting" is selected, the caller won't continue on this flow (for example if Callback is selected).

  5. Caller is played **Ask for Consent to Send Wait Time SMS** message.

If response = No, the caller stays in queue and is not asked again.

If response = YES, the "Wait Time SMS Sent" message is played.

  6. Caller is sent an SMS with the content of **Global Wait Time SMS Message Sent to Caller's Device** message.

  7. The caller can reply with any number of text or multimedia messages.

  8. The call is assigned to an agent and connected with the information they shared available to the agent in the agent's CRM ticket.




### User flow: agent

The following are the steps over the agent user flow:

  1. Agent is assigned a call.

  2. Agent will see a banner on the call adapter alerting "Wait Time SMS Received."

     * Agent can click the green banner to view the messages.

     * Agent can view the messages sent as comments in the CRM ticket.




## Configuration

Steps to set up this feature:

  1. Enable and configure global setting.

  2. Set up messages and configurations.

  3. Enable queue level settings.




### Enable and configure global settings

  1. In the CCAI Platform portal, go to **Settings** > **In Call SMS**.

  2. Enable In Call SMS, and Wait Time SMS.

  3. The interval at which the wait time SMS consent message will be played is based on the global announcement setting. Click **Edit announcement** intervals and you will be taken to the Call Settings page. This setting is called **Universal Caller Announcement Intervals**.

**Note:** Changes to the universal caller announcement intervals are global and will impact other announcements in the platform such as Over Capacity wait options and Estimated Wait announcements when enabled.
  4. Check the box to limit the number of times the SMS consent message is played. When enabled, set the threshold for the number of times the caller will hear the message.

  5. For more specific controls of when callers should receive the option to use Wait Time SMS, enable the option by clicking the box. Then set the minimum and maximum wait time that needs to be reached, based on estimated wait time for the caller to hear the option to use Wait Time SMS.




### CRM record creation and abandoned call settings

CCAI Platform creates a record when the call is initiated, and not before. Depending on your settings (Operation Management), CCAI Platform may create a CRM record for all abandoned calls, so even if no call takes place you have a record of this.

In an ideal scenario, the caller will call in, choose to participate in Wait Time SMS, and the messages will be shared with the Agent - however, this is not always how things play out. In the scenario where the caller chooses to participate in Wait Time SMS, then abandons the call before being connected to an agent, you can choose to create a ticket if the system otherwise wouldn't create one.

  1. Go to **Settings** > **Operation Management.**

  2. To enable ticket or case creation for abandoned calls only when SMS has been received, mark the box next to **Create CRM ticket for abandoned calls** and also mark **Abandoned calls with SMS data**.




### Setting up messages

Default message setup is made from the In Call SMS settings, but can also be customized for each queue. Individual queue settings or messages will override general messages and settings.

  1. In the CCAI Platform portal, go to **Settings** > **In Call SMS** .

  2. If you are using multiple languages in your IVR, repeat the following steps for each active language you will be using SMS for. Refer to the Global Numbers section of [In call SMS](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms-in-call) for more information.

  3. Set up the **Ask for Consent** Message by either entering text to be read to the caller, or by uploading a custom file by clicking on **Upload** in the bottom-right. The message must contain two options for the caller - "press 1" to approve SMS messages be sent to their phone, and "press 2" to deny SMS messages be sent to their phone. Refer (Consent message details)(#consent-message).

  4. Set up the **Wait Time SMS Sent** message by either entering text to be read to the caller, or by uploading a custom file by clicking on **Upload** in the bottom right. The content of this message should inform the caller that they will receive a message based on the phone number they dialed in from, and to check that message for the next steps.

  5. Compose the text message which will be sent once the caller accepts the SMS message channel by entering text in the field. Use your brand name, and ask for important details as specifically as possible.




#### Consent message details

Consent messages are provided to the end user in order to be able to notify them of the ability to opt out.

Wait Time SMS consent message won't be triggered if:

  * The call is deflected to other option rather than "keep waiting".

  * Wait Time SMS is disabled globally or for the selected queue.

  * Caller already allowed or denied Wait Time SMS.

  * The max number of tries is reached.




The following are the caller's text responses are received and processed by CCAI Platform.

  * Digit=1, the caller has allowed SMS

    * wait_time_sms_status = allowed

wait_time_sms_status = allowed

    * Send SMS

    * Call stays in queue

  * Digit=2, the caller has denied SMS

    * wait_time_sms_status = denied

    * Call stays in queue

  * Other Digits, considered wrong selection

    * "Incorrect Selected Number" message is played

    * Consent message repeated

  * No Digits, caller has made no selection

    * 10 seconds response time is allowed

10 seconds response time is allowed

    * wait_time_sms_status = no_response

    * Call is sent back to queue

    * If applicable, message will be repeated at the interval set by the **Universal Caller Announcement** setting.


**Note:** when the Wait Time SMS Consent message and Wait Time SMS Sent message is being played, the caller is temporarily removed from the queue, meaning the agent won't be able to pick up the call when the caller is listening to the message.

### Enable and configure queue-specific settings

  1. In the CCAI Platform portal, go to **Settings** > **Queue** > **IVR** > **Edit / View**.

  2. Click the name of the queue to select it.

  3. Toggle **In Call SMS** to **On** (if it isn't already).

  4. Mark the checkbox to enable **Wait Time SMS**.

  5. If you want to use a queue-specific setting and messages, click **Customize for this queue**. There you can customize:

     * Wait Time SMS based on estimated wait time (Custom).

     * Audible Messages.

     * The Wait time SMS message.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
