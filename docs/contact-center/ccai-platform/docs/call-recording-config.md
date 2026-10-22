---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording-config/
title: Call recording configuration \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:22.347096+00:00
---

# Call recording configuration  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording-config/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call recording configuration Stay organized with collections  Save and categorize content based on your preferences. 

Calls can be recorded in mono and in stereo to and from your contact center. For more information on recording in stereo, contact support.

If Call Recording is enabled, there are various messages that can be played by default for inbound and outbound calls.

In most cases, call recordings are stored in the CRM, and playback is available in the CRM record where the recording is stored.

## Configuration details

  * Calls transferred to a third party are recorded; however, once the agent leaves the call, the remainder of the call between the end-user and the 3rd party is redacted.

  * Call recording can be paused for sensitive information using call redaction.

  * With Secure Payments, callers are taken through a payment flow and call recording is automatically paused

  * Call recordings are saved as .mp3 files unless otherwise requested.




## Global call recording settings

**Note:** Depending on the overall settings you have enabled, some of the following options might not be available. To verify which options you have available please contact Support.

  1. Go to **Settings >Call >Call Details**.



## Use call recording

Enable inbound call or agent initiated outbound recording for the environment by default.

Outbound call recording configuration options will show when this is enabled.

### Record callback outbound calls

When the Callback overcapacity option is enabled, this setting will enable Callback and scheduled call recordings.

  * **Enable Call Recording Redaction for agents** : Enables Call Redaction.

  * **Play Call Recording Messages** : Plays a message to the caller receiving the outbound call from an agent. Message name is **Record an Outbound Call Message** and can be set up in **Settings** **>** **Languages & Messages**.




### Record agent-initiated outbound calls

Enables calls recording for Agent initiated calls:

  * Dialed outbound calls

  * Short call callbacks - For more information see [Call recovery features](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recovery-features).

  * Hang Up And Callbacks - For more information see [Call recovery features](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recovery-features).

  * Add a third party calls (while the agent remains on the call)




**Enable Call Recording Redaction for agents** : Enables Call Redaction to be used on outbound calls.

**Play Call Recording Message** : Plays a message to the caller receiving the outbound call from an agent. Message name is Record an Outbound Call Message can be set up in **Settings** **>** **Languages & Messages**.

### Ask permission to record

  1. Use this setting to choose whether or not to record an outbound call started by an agent.

  2. To enable this option go to **Calls > Call Recording** and check the checkbox **Record Agent Initiated Outbound Calls.**

  3. To use this option for outbound calls, the **Ask Permission to Record** option **must** be activated.




### Record message sequence

The _Ask Permission to Record Message_ recording is configurable at **Settings > Languages and Messages > Ask to Record**.

This section lets you specify the order in which your User permission and Call Recording messages are played for the end-user.

For example, since outbound calls don't have an introduction message, you can have the call recording play for consumers before the consent to record (user permission) so they know who is calling (call recording).

  * **Play Ask Permission to Record Message before Call Recording Message**

  * **Play Call Recording Message before Ask Permission to Record Message**


**Note:** Recording message and Ask Permission to Record messages are played in the configured order for:

  * Callback outbound calls - if the queue is configured for asking to record.

  * Agent initiated outbound calls - if the Ask permission to record is enabled.




### Recording separation

Recording separation lets you to choose to receive separate call recordings for each call segment rather than all of them in a single file. The ability to keep separate call records for each conversation segment allows for more flexible call analysis and, potentially, more efficient issue resolution. Better record analysis lets you identify specific portions of the conversation where issues might have occurred, allowing you to provide more targeted training and coaching.

To enable this feature, select the **Recording Separation** checkbox and select **Per segment**. If you choose **None** , you will still receive call recordings as a single file.

### Use dual channel recording settings

Enable dual channel recording to record your call using two separate channels, for example an end-user channel and an agent channel.

With each party's audio separated into its own track, it's easier to use transcription and keyword analysis to examine the content of a recording. There is also an advantage in the quality of the voice recording when played back. When analyzing calls, dual-channel recordings allow your call centre managers and quality supervisors to concentate on a single channel (only the end-user or only the agent).

**Note:** Configuration will affect calls from all channels, for example, IVR, Web (Callbacks), Mobile.

This can be enabled at **Settings > Call > Call Details > Call Recording > Use Dual Channel Recording**.

  * Selecting the checkbox will record all calls as dual channel audio recordings.

  * Unchecking the checkbox will record all calls as single channel audio recording.




## Record settings at the queue level

  1. Go to **Settings > Queue.**

  2. Click **Edit / View** for the channel you want to set up**.**

  3. Select the menu option that you want to set recording options for.

**Note:** If you have sub-queues, you'll need to set the recording option in the sub-queue.
  4. Choose a recording option for the particular queue selected.

**Record** : Records all calls

**Do Not Record** : Does not record any calls for the queue

**Ask Permission to Record** : Asks the caller for permission to record




**Channel**

**Note: This setting behaves different based on channel**

**IVR**

When using the **Ask Permission to Record** option, you will need to add the **Ask to Record** message found on the **IVR Message Setup** page. The caller will need to press 1 to not be recorded - any other entries or a lack of pressing one will result in the call being recorded.

**Mobile SDK**

  1. Click **Set Call Recording Option** to save your recording choice for the queue.

**Note:** These recording options only work if your call center settings support recording calls.

## Listen to call recordings

Once the call has been recorded, the recording will most likely be saved in your CRM, depending on your configuration. The following are examples of where it could show up in your CRM.

### Zendesk

The recording shows in an audio player as part of the private comment.

### Salesforce

The call recording shows as an attachment to the case or in the CCAI Platform Session object.

### Kustomer

The recording will show inline within the Kustomer conversation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
