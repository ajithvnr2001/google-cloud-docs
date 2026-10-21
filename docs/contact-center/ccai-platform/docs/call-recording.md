---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording/
title: Call recording \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:44:05.937441+00:00
---

# Call recording  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call recording Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to configure call recordings.

Contact Center AI Platform (CCAI Platform) can record the following call types:

  * **Inbound calls** : This includes inbound calls that are routed to a queue, direct inbound calls, and end-user to agent calls.

  * **Callback outbound calls** : These calls are automatically initiated by the system, and include the following:

    * Callbacks requested from a queue due to overcapacity

    * Calls scheduled by an end-user

  * **Agent-initiated outbound calls** : These include the following:

    * Calls dialed using the call adapter dial pad

    * Calls made using click-to-call from a CRM record

    * Callbacks from a voicemail

    * Calls made using "Hang Up and Callback"

    * Calls where an agent adds a third party




Laws can require that callers know when they are being recorded. You can configure CCAI Platform to play announcements for requesting consent to record and for indicating that a call will be recorded. This is enabled by default. Consult your legal team to determine the recording announcements that are required for your users.

## Upload audio files for call recording messages

You can upload audio files that play to an end-user before call recording begins. Audio files can be in `MP3` or `WAV` format.

To upload audio files for recording calls, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Languages & Messages**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **Audible Messages > Call Messages**.

  3. To upload an audio file for recording inbound calls, do the following:

     1. For **Record a Call Message** , click **Upload Audio Recording for recording a call**.

     2. Navigate to your audio file, and then click **Open**.

  4. To upload an audio file for recording outbound calls, do the following:

     1. For **Record an Outbound Call Message** , click **Upload Audio Recording for recording an outbound call**.

     2. Navigate to your audio file, and then click **Open**.

  5. Click **Save**.




## Store call recordings

You can store call recordings in your CRM or in external storage. Call recordings are saved as MP3 files. When a recorded call ends, the system immediately queues the recording file for upload to your CRM or external storage. After the upload completes, the system permanently deletes the recording file from CCAI Platform temporary storage. For more information, see Call recording data management.

### CRM storage

If you've configured CCAI Platform to upload recording files to a CRM, playback of recording files is typically available within the CRM record associated with the interaction. Here's how recordings are handled in the following CRMs:

  * **Zendesk** : The recording appears in an audio player as part of a private ticket comment.

  * **Salesforce** : The recording is attached to the case or is available in the CCAI Platform session object.

  * **Kustomer** : The recording displays inline within the Kustomer conversation.




### External storage

You can configure CCAI Platform to upload recording files to external storage. For more information, see [External storage](https://docs.cloud.google.com/contact-center/ccai-platform/docs/external-storage).

If you store recording files in Cloud Storage, your [bucket retention policy](https://docs.cloud.google.com/storage/docs/using-bucket-lock) could block call recording merge and overwrite attempts. You can temporarily resolve this by turning on [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning).

## Configure call recording at the global level

To configure call recording at the global level, follow these steps. For more information, see [Call details](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#call-details).

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **Call Details > Call Recording**.

  3. Select the **Use Call Recording** checkbox.

  4. To configure recording for [inbound](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#inbound-routing-options) calls, do the following. For more information, hold the pointer over info.

     1. Select the **Record Inbound Calls** checkbox.

     2. Optional: Select the **Enable Call Recording Redaction for agents** checkbox. For more information, see Call recording redaction.

     3. Optional: Select the **Play Call Recording Message** checkbox. The **Ask User Permission To Record** checkbox appears.

     4. Optional: Select the **Ask User Permission To Record** checkbox. This prompts the user for their consent before recording can begin. For information about configuring the **Ask Permission to Record** message, see [Configure IVR messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-ivr-messages).

  5. To configure recording for callback outbound calls, do the following. For more information, hold the pointer over info.

     1. Select the **Record Callback Outbound Calls** checkbox.

     2. Optional: Select the **Enable Call Recording Redaction for agents** checkbox. For more information, see Call recording redaction.

     3. Optional: Select the **Play Call Recording Message** checkbox.

  6. To configure recording for agent-initiated outbound calls, do the following. For more information, hold the pointer over info.

     1. Select the **Record Agent Initiated Outbound Calls** checkbox.

     2. Optional: Select the **Enable Call Recording Redaction for agents** checkbox. For more information, see Call recording redaction.

     3. Optional: Select the **Play Call Recording Message** checkbox. The **Ask User Permission To Record** checkbox appears.

     4. Optional: Select the **Ask User Permission To Record** checkbox. This prompts the user for their consent before recording can begin. For information about configuring the **Ask Permission to Record** message, see [Configure IVR messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-ivr-messages).

  7. Optional: Select any of the following recording options:

     * **Record Direct Inbound Calls**. For more information, see [Direct phone numbers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/direct-phone-numbers).

     * **Record Agent-to-Agent Calls**. For more information, see [Agent to agent calling](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#agent-to-agent-calling).

     * **Record Consumer-to-Agent Calls**. For more information, see [End-user to agent calling](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#end-user-to-agent-calling).

  8. Optional: Select any of the following options to continue recording after a party leaves a call:

     * **Continue call recording when the consumer leaves the call**. This checkbox is active only when the **Allow a consumer to leave a call without ending the call (additional charges may apply)** checkbox is selected. For more information, see Allow parties to leave calls without ending them.

     * **Continue call recording to Third Party Numbers after the agent leaves the call**. This checkbox is active only when the **Allow an agent to leave a call after adding a 3rd party without ending the call (additional charges may apply)** checkbox is selected. For more information, see Allow parties to leave calls without ending them.

     * **Continue call recording to Emergency Numbers after the agent leaves the call**. This checkbox is active only when the **Allow an agent to leave a call after adding a 3rd party without ending the call (additional charges may apply)** checkbox is selected. For more information, see Allow parties to leave calls without ending them.

  9. Optional: Select **Use Dual Channel Recording** checkbox. For more information, see [Use dual channel recording settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording-config#dual-channel-recording-settings).

  10. For **Recording Separation** , select one of the following options:

     * **None** : The entire call recording is in a single file.

     * **Per Segment** : The call recording is split into separate files, one for each call segment. A new call segment is created every time there's a call transfer.

  11. For **Recording Message Sequence for Outbound Calls** , select one of the following options:

     * **Play Ask Permission to Record message before Call Recording message** : This plays the **Ask Permission To Record** message before the **Record an Outbound call** message. For information about configuring the **Record an Outbound call** message, see Upload audio files for call recording messages.

     * **Play Call Recording message before Ask Permission to Record message** : This plays the **Record an Outbound call** message before the **Ask Permission To Record** message. You can use this configuration to identify your company in the first message before asking for consent to record in the second message.

  12. Click **Save Call Details**.




## Configure call recording at the queue level

Queue-level settings override global settings.

To configure call recording at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**. The **Queue Menu Settings** page appears.

  2. Depending on the channel that you want, do one of the following:

     * In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

     * In the **Mobile** pane, click **Edit / View**.

     * In the **Web** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the settings pane, for **Call Recording Settings** , click **Configure**. The **Call Recording Settings** pane appears.

  5. To configure recording for [inbound](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#inbound-routing-options) calls, do the following. For more information, hold the pointer over info.

     1. In the **Inbound Call Recording** section, select the **Record Inbound Calls** checkbox.

     2. Optional: Select the **Enable Call Recording Redaction for agents** checkbox. For more information, see Call recording redaction.

     3. Optional: Select the **Play Call Recording Message** checkbox. The **Ask User Permission To Record** checkbox appears.

     4. Optional: Select the **Ask User Permission To Record** checkbox. This prompts the user for their consent before recording can begin. For information about configuring the **Ask Permission to Record** message, see [Configure IVR messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-ivr-messages).

  6. To configure recording for callback outbound calls, do the following. For more information, hold the pointer over info.

     1. In the **Callback Outbound Call Recording** section, select the **Record Callback Outbound Calls** checkbox.

     2. Optional: Select the **Enable Call Recording Redaction for agents** checkbox. For more information, see Call recording redaction.

     3. Optional: Select the **Play Call Recording Message** checkbox.

  7. To configure recording for agent-initiated outbound calls, do the following. For more information, hold the pointer over info.

     1. In the **Agent Initiated Outbound Call Recording** section, select the **Record Agent Initiated Outbound Calls** checkbox.

     2. Optional: Select the **Enable Call Recording Redaction for agents** checkbox. For more information, see Call recording redaction.

     3. Optional: Select the **Play Call Recording Message** checkbox. The **Ask User Permission To Record** checkbox appears.

     4. Optional: Select the **Ask User Permission To Record** checkbox. This prompts the user for their consent before recording can begin. For information about configuring the **Ask Permission to Record** message, see [Configure IVR messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-ivr-messages).

  8. Click **Save**.




## Allow parties to leave calls without ending them

You can control whether an agent or end-user can leave a call without ending it.

To allow parties to leave calls without ending them, do the following:

  1. In the CCAI Platform portal, click **Settings > Call**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to **Call Details > Leave Ongoing Calls with 3rd Parties**.

  3. Select one or both of the following checkboxes:

     * **Allow an agent to leave a call after adding a 3rd party without ending the call (additional charges may apply)**.

     * **Allow a consumer to leave a call without ending the call (additional charges may apply)**.




## Call recording redaction

When you enable call recording redaction, a **Pause** button appears in the call adapter. This lets agents pause a call recording to avoid capturing sensitive information such as credit card data or personal data. You can enable call recording redaction for inbound calls, callback outbound calls, and agent-initiated outbound calls, at both the global and queue level. For more information, see Configure call recording at the global level and Configure call recording at the queue level.

If you implement [Secure Payments](https://docs.cloud.google.com/contact-center/ccai-platform/docs/secure-payments-add-providers), call recording pauses when the payment flow begins and resumes when it ends.

## Call recording data management

When a recorded call ends, the system immediately queues the recording file for upload to your CRM or external storage. After the upload completes, the system permanently deletes the recording file from CCAI Platform temporary storage. The system securely retains the recording file, which is only accessible using authenticated CRM keys.

Most recording file uploads are instantaneous. In rare cases, however, uploads can be delayed. When this occurs, the system uses a retry mechanism with an exponential backoff. All recordings are deleted from CCAI Platform temporary storage after seven days, regardless of upload status.

### Handling large files

If a recording file exceeds 50 MB, the system splits it into smaller files. The system attaches the files to the CRM ticket in the correct order.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
