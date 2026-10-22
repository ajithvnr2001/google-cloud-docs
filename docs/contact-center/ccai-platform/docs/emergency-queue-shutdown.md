---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/emergency-queue-shutdown/
title: Emergency queue shutdown \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:24.061654+00:00
---

# Emergency queue shutdown  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/emergency-queue-shutdown/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Emergency queue shutdown Stay organized with collections  Save and categorize content based on your preferences. 

The emergency queue shutdown capability lets you temporarily shut down one or more queues during unexpected events such as system issues, a sudden lack of staff, a building emergency, or unplanned maintenance. You can configure the experience of end-users that are on a call, in a queue, or transferring at the moment you shut down a queue. This lets you manage only the affected queues without affecting the rest of your contact center.

By default, this capability is inactive. Contact Google Cloud Support to turn it on for your instance.

## Automatic reset

When you shut down a queue, it automatically resets to normal operation depending on the following:

  * **If you've configured hours of operation** , the queue resets to normal operations at the start of the next business day.

  * **If you haven't configured hours of operation** , the queue resets to normal operations at 12:00 AM the following day.




## Configure the global emergency message

The global emergency message is the default message for any queues that don't have a message configured.

To configure the global emergency message, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Languages & Messages**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Audible Messages** pane, go to the **Emergency Shutdown Message** section.

  3. Do one of the following:

     * To change the text-to-speech message, edit the text in the text field.

     * To upload an audio recording to read out instead of using the text-to-speech message, click **Upload audio recording** and then upload an MP3 or WAV file with your message.

  4. Click **Save**.




## Configure emergency shutdown for a queue

You can configure specific emergency shutdown behavior for one or more queues, including custom messages and redirect logic.

To configure emergency queue shutdown for a queue, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, go to the **Emergency Shutdown** section, and click the toggle to the on position.

  5. Do one of the following:

     * To change the text-to-speech message, edit the text in the text field.

     * To upload an audio recording to read out instead of using the text-to-speech message, click **Upload audio recording** and then upload an MP3 or WAV file with your message.

  6. In the **Calls in progress** list, select one of the following:

     * **Do not play emergency message and continue call** : The call continues normally and the shutdown doesn't interrupt the conversation.

     * **Play emergency message and redirect to Overcapacity Deflection** : The system plays the message and does an overcapacity deflection.

     * **Play emergency message and redirect to After Hours Deflection** : The system plays the message and does an after hours deflection.

  7. In the **Queued and Transferred Calls** list, select one of the following:

     * **Play emergency message and end call** : The system plays the message and disconnects.

     * **Play emergency message and redirect to Overcapacity Deflection** : The system plays the message and does an overcapacity deflection.

     * **Play emergency message and redirect to After Hours Deflection** : The system plays the message and does an after hours deflection.

  8. Click **Save Emergency Shutdown**.




## The emergency shutdown API

You can use the emergency shutdown API to programmatically do the following:

  * Turn on or off the emergency queue shutdown capability for one or more queues.

  * Provide a queue-specific emergency message.

  * Determine how in-progress and queued calls are handled.




The API lets external apps, such as an incident management system, shut down queues automatically.

### Enable the emergency shutdown API

To enable the emergency shutdown API, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Enable Remote Shutdown via API** pane and click the toggle to the on position.




### Use the API

For more information about using the API, see [Emergency shutdown](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-emergency-shutdown).

## Reporting and auditing

The system tracks emergency shutdown activity to help you monitor emergency shutdowns:

  * **Audit logging**. When emergency queue shutdown is turned on or off, the system records data such as who made the change, the timestamp, and the action (turned on or off). If the emergency shutdown API is used, the system logs the request payload and the emergency message.

  * **Deflection reason**. Calls deflected when a queue is shut down are tagged with the following reason: "deflected due to emergency shutdown". You can use this tag in analytics to determine how many calls were affected.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
