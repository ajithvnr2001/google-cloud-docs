---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-messages-notifications/
title: Agent messages & notifications \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:20.946733+00:00
---

# Agent messages & notifications  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-messages-notifications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Agent messages & notifications Stay organized with collections  Save and categorize content based on your preferences. 

You can customize agent notifications for calls and chats, both globally and at the queue level. Options include:

  * Setting the frequency and tone for alerts.

  * Uploading custom tones.

  * Configuring whisper announcement settings that provide context before a call starts.




With these settings you can customize your notifications and messages to help improve your agents' responsiveness and efficiency.

## Configure call messages and notifications globally

To configure call messages and notifications globally, follow these steps:

  1. Go to **Settings** > **Call**.

  2. Navigate to the **Agent Call Messages & Notifications** section.

  3. Under **General** , configure the following settings:

     1. **Use whisper for calls** : Once a call is assigned to the Agent, they will hear an audible message stating the call type and queue: "{Call Type} from {Queue Name}."

**Whisper read speed** : Increase or decrease the speed at which the whisper message is read. Duration of call whisper message is included in Wait Time metrics.

     2. **Use countdown for calls** : Plays an audible message to the agent counting down seconds until the caller is live on the phone: "You're up - call starting in 3,2,1."

  4. **Incoming call notification** : Click each option to hear the tone. Select the tone for agents to hear for incoming calls. You can also upload a custom tone.

  5. **Call notification frequency** : Choose for the agent to only hear the notification tone one time, or repeated after a specified number of seconds have passed. If you select **Notify agent until call is picked up or no calls are available** , you can select or change the number of seconds between notifications.

  6. Activate the **Enable SMS Notification** slider to allow SMS notifications to the agent for any incoming calls to the phone number specified in the agent's CCAI Platform user profile.

  7. Click **Set Notifications** to save your changes.




## Configure chat notifications globally

To configure chat notifications globally, follow these steps:

  1. Go to **Settings > Chat**.

  2. Navigate to **Agent Chat Notifications**.

  3. Under **New Chat Notification** , click each option to hear the tone. Select the tone that agents will hear for incoming chats.

  4. Under **Notification Frequency** , you can choose for the agent to only hear the notification tone once, or repeatedly after a specified number of seconds have passed.

  5. If you select **Notify agent until chat is picked up or no chats are available** , you can select or change the number of seconds between notifications.

  6. Under **New Message Notification** , click each option to hear the tone. Select the tone that agents will hear for new messages in an existing chat.

  7. Click **Save Notification** to save your changes.




## Configure whisper announcements at the queue level

By configuring whisper announcements at the queue level, you can provide information to agents that is specific to a queue prior to a call starting.

**Note:** When you configure whisper settings for a queue, all child queues of that queue inherit the settings.

To configure whisper announcements at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu** , and then click **Settings > Queue**.

  2. Depending on the type of queue you are editing, click either **IVR (Interactive Voice Response)** , **Mobile** , or **Web**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane for your queue, go to the **Whisper Announcement** section, and then click **Configure**.

  5. Click the **Whisper Announcement** toggle to the on position.

  6. Select one of the following whisper announcement types:

     * **Queue name** : CCAI Platform reads the queue name before the call starts.

     * **Text-to-speech** : enter text for CCAI Platform to read before the call starts.

     * **Upload Audio Recording** : upload an audio file for CCAI Platform to play before the call starts.

  7. Optional: In the **Whisper read speed** box, select a playback speed.

  8. Optional: Click the **Use countdown for calls** toggle to the on or off position. If you turn on this setting, CCAI Platform plays a message to the agent that counts down the seconds until the call starts—for example, "You're up - call starts in 3, 2, 1."

  9. Click **Save**.




## Custom notification tones

You can upload custom tones for the following notification types:

**Agent call messages & notifications**:

  * Incoming call notification



**Agent chat notifications** :

  * New message notification
  * New chat notification



Under **Settings > Chat > Agent Chat Notifications**, you will see **Select the tone you would like to use** under each notification type. Clicking **Custom tone** lets you upload a `.mp3` audio file and preview it. The `.mp3` file can be deleted or replaced with other custom tones. The uploaded tone remains available even if you choose a default tone.

## Settings recommendations

  * Use a longer ringtone and more frequent notification if:

    * Agents are often multitasking and not always waiting to take a call

    * In an open office or louder environment

    * Agents might listen to music from their computer

  * Use a shorter ringtone if:

    * Agents are always alert and waiting for calls

    * Higher call frequency

  * Call whisper:

    * Use this when the queue selection and type of call highly impact the first communication from the agent

    * Increase speed of whisper for decreased wait time impact

  * For very low second count SLAs:

    * Only use whisper and countdown if necessary as the duration of these messages contributes to the wait time for calls



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
