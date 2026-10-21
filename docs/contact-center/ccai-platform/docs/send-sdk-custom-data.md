---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-sdk-custom-data/
title: Send SDK custom data \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:26.854811+00:00
---

# Send SDK custom data  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-sdk-custom-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Send SDK custom data Stay organized with collections  Save and categorize content based on your preferences. 

You can send SDK custom data to the [session metadata file](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-session-metadata), to a CRM record, or both, depending on your requirements. This custom data can come from the [web SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk#chat-unsigned-custom-data), the [Android SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#send-custom-data-to-your-crm) or the [iOS SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#send-custom-data-to-your-crm). You can send custom data globally and at the queue level.

## Send SDK custom data globally

To send SDK custom data globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Data Parameters** pane.

  3. Do one of the following, or both, depending on your requirements:

     * For **Send SDK custom data to session metadata file** , select the type of SDK custom data that you want to send to the session metadata file.

     * For **Send SDK custom data to CRM record** , select the type of SDK custom data that you want to send to a CRM record.

  4. Click **Save Data Parameters**.




## Send SDK custom data at the queue level

To send SDK custom data at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Mobile** or **Web** pane (depending on your channel), click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, go to **SDK custom data settings** , and then click **Configure**. The **SDK Custom Data Settings** pane appears.

  5. Do one of the following, or both, depending on your requirements:

     * For **Send SDK custom data to session metadata file** , select the type of SDK custom data that you want to send to the session metadata file.

     * For **Send SDK custom data to CRM record** , select the type of SDK custom data that you want to send to a CRM record.

  6. Click **Save**.




## What's next

  * [View session data in the agent adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-data-agent-adapter)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
