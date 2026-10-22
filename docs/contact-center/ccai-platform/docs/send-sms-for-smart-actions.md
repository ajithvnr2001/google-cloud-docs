---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-sms-for-smart-actions/
title: Send SMS to launch SmartActions \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:21.959328+00:00
---

# Send SMS to launch SmartActions  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-sms-for-smart-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Send SMS to launch SmartActions Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) can send SMS messages to the end-user to launch smart actions.

## Send SMS to launch App for smart actions during an IVR call

SmartActions (receiving photos, videos, screenshots, verifying customers, and receiving text input) are not typically available during an IVR call.

You can prompt the end-user to launch their app for your company.

Once the app is installed and launched, you can use these SmartActions with a customer **during an IVR call**.

### Prerequisites

  * **In Call SMS** is configured.

  * The caller has downloaded the app, if not send them a text message to download the app.




### How to send app open and download text messages

  1. Sign in to the agent call adapter.

  2. **Accept Call:** Clicking on the desktop notification will accept the call.

or

  3. **Accept Call:** Clicking **Click To Answer** will accept the call.

  4. Click the **Actions** button to present options for sending SMS to open or download your app.

  5. If the end-user doesn't have your app, click **Send SMS to Install App** to send them an app installation link.

  6. If the end-user has downloaded your app, click **Send SMS to Open App** to send an SMS link to open the app.

  7. Confirmations appear next to the SMS request you have sent.

  8. When the app is opened, the customer name and ID sync to the widget.

  9. Once the app is opened, SmartActions are now available during your IVR call.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
