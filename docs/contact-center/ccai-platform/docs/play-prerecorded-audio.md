---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/play-prerecorded-audio/
title: Play pre-recorded audio \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:21.627831+00:00
---

# Play pre-recorded audio  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/play-prerecorded-audio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Play pre-recorded audio Stay organized with collections  Save and categorize content based on your preferences. 

With Dialogflow CX, you can let virtual agents respond with pre-recorded audio. This lets you use high-quality audio files instead of standard text-to-speech. This capability is available for all voice channels, including inbound and outbound calls. It's available for support virtual agents, task virtual agents, and post-session virtual agents. Barge-in is not supported during pre-recorded audio playback.

**Important:** Configure **No speech timeout** in Dialogflow CX to be at least two or three seconds longer than your longest audio file. This helps prevent a timeout event while the audio is still playing to the end-user. For more information, see [No speech timeout](https://docs.cloud.google.com/dialogflow/cx/docs/concept/advanced-speech#no-speech-timeout).

For more information, see [Play prerecorded audio](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#audio).

## Before you begin

Host your audio files in a publicly-accessible service such as Cloud Storage. The audio file must be in WAV format.

## Configure pre-recorded audio for virtual agent responses

To configure pre-recorded audio for virtual agent responses, follow these steps:

  1. Go to the Conversational Agents console.

[Conversational Agents console](https://conversational-agents.cloud.google.com/projects)

  2. Select the project that contains your agent.

  3. Select your agent.

  4. In the navigation menu, click **Flows**.

  5. Click the flow that you want.

  6. In the flow pane, click the page that you want.

  7. For **Entry fulfillment** , click **Edit Fulfillment**. The **Fulfillment** dialog appears.

  8. Click **Add dialogue response > Play pre-recorded audio**.

  9. In the **Play pre-recorded audio** field, enter the full, publicly-accessible URL for your WAV file—for example, `https://storage.googleapis.com/YOUR_BUCKET/YOUR_AUDIO_FILE.wav`.

  10. Optional: Add additional dialog response types. You can use the arrow_upward **Move up** and arrow_downward **Move down** arrows to reorder the dialog responses.

  11. Click **Save**.




## Failure handling

If playback of pre-recorded audio fails (due to an inaccessible URI or a malformed audio file, for example), you can expect the following behavior:

  * The system silently skips that fulfillment segment so that the end-user isn't aware of the failure.

  * Other fulfillments in the same response are processed as expected.

  * The system logs an error that includes the following:

    * Timestamp

    * Session ID

    * Virtual agent ID

    * Error code or error message




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
