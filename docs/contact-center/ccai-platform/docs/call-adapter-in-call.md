---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-in-call/
title: In-call interface \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:35.512649+00:00
---

# In-call interface  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-in-call/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  In-call interface Stay organized with collections  Save and categorize content based on your preferences. 

When you're in a call, the **Call** tab in the call adapter is active by default. The **Call** tab contains buttons for actions that you can take during a call. The **Details** tab contains information about the call and connects to the CRM that you're using.

The following image shows call adapter during a call.

## Call tab during a call

The **Call** tab contains the following buttons. Some buttons are optional and appear only if your administrator has enabled them.

  * **Mute** : mutes your microphone but keeps the call going

  * **Hold** : places the caller on hold

**Note:** An optional hold time counter displays if your administrator has configured it to display. For more information, see [Configure call details](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Agent___Team_Configuration#configure_call_details).
  * **Transfer/Add** : this button provides you with three options for transferring or conferencing calls, visible as tabs across the top of the screen: Queue, Agent, or Outside line. In each case you have the option of transferring or adding your selection to the call. For a warm transfer, stay on the call until the transfer is completed, and then click **End call**. For a cold transfer, end the call to complete the transfer after selecting the destination. Cold transfers can only be sent to agents or final leaf queues.

  * **Redact** (Optional): click this button to stop recording. You will see a banner showing that the call is redacted and the duration of the selection.

  * **Agent Assist** (Optional): this button opens the Agent Assist menu, which will optionally display the Knowledge Assist and Live Transcripts options.

  * **Knowledge Assist** (Optional): displays a list of relevant articles, if any. If there are no relevant articles the list will be blank. Select an article to open and read it.

  * **Live Transcript** (Optional): displays speech bubbles for each message to and from the end-user.

  * **SmartActions** (Optional): most SmartActions are only available when the end-user calls in using Mobile SDK. Which options are available depends on your organization's configuration. Click the SmartActions button to open the SmartActions menu. Here you will find options to:

    * Request payment
    * Request verification
    * Request a photo
    * Request a video
    * Request text input
    * Request a screenshot
    * Begin a Co-browse session
    * Use the Virtual Task Assistant
    * Send SMS messages to install or open apps
  * **Hang up & Call back**: click this button to hang up and call the end-user back. This will create a new outbound call and you will see an _Account details_ record in the _In-Call_ menu until the call connects.

  * **End call** : terminates the call

  * **Keypad** : displays the **Keypad** screen during a call. The **Keypad** screen generates DTMF tones from your computer keyboard input. When you type or paste data into the **Enter input** field on the **Keypad** screen, the system processes each character as a DTMF signal audible to all call participants. The system supports both standard digits and alphanumeric strings. The system converts letters that you enter into their corresponding DTMF tones—for example, `ABC` plays as `222`.




## Details tab during a call

The **Details** tab appears during a call. It contains information about the call and includes the following sections:

  * **Notes** : lets you write a note about the call. This note is saved to your CRM when the call ends.

  * **SDK custom data** : displays custom data for this call from the web or mobile SDKs. For more information, see [View session data in the agent adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-data-agent-adapter).

  * **VA session variables** : displays virtual agent session variables for this call. If there are multiple virtual agent interactions during the call, each interaction is listed. Clicking an interaction displays the session variables for that interaction. For more information, see [View session data in the agent adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-data-agent-adapter).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
