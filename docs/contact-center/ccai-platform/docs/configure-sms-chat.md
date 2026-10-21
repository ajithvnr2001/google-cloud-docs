---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-sms-chat/
title: Configure SMS chat \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:33.429208+00:00
---

# Configure SMS chat  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-sms-chat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure SMS chat Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to configure deflections and greeting messages for SMS chat.

## Set SMS chat deflections

If your administrator has enabled this capability, you can configure your own SMS chat deflection settings using the agent adapter. For information about enabling agents to configure SMS settings, see [Direct SMS numbers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/direct-sms-numbers).

To set SMS chat deflections, follow these steps:

  1. In the CCAI Platform portal, click ![The open chat icon](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-chat.png)**Chat**. The chat adapter appears.

  2. Click more_vert **Options > Agent SMS deflections**. The **Agent SMS deflections** pane appears.

  3. Click **After hours deflection**. The **After hours deflection** pane appears.

  4. Click the **After hours deflection** toggle to the on position.

  5. To configure chat availability hours, do the following:

     1. Click **Chat availability hours**. The **Chat availability hours** pane appears.

     2. To configure the time zone, do the following:

        1. Click **Time Zone**. The **Time Zone** pane appears.

        2. Click the time zone that you want.

        3. Click chevron_left **Back** to return to the **Chat availability hours** screen.

     3. For **Days and hours of operation** , select one of the following:

        * **24 hour operation**. This indicates that you're available 24 hours a day.

        * **Weekdays / Weekends**. Select whether you're available on weekdays, weekends, or both. Then configure your times of availability.

        * **S / M / T / W / T / F / S**. Select the days that you're available, and then configure your times of availability.

     4. To set the holidays that you observe, click **Holidays to Observe**. The holidays that your company observes appear, organized by country. Do one of the following:

        * To make yourself unavailable for all of a country's holidays, select the checkbox for that country.

        * To make yourself unavailable for only some of a country's holidays, do the following:

          1. Click expand_more **Expand more**.

          2. Select the individual holidays that you're unavailable for.

     5. Click chevron_left **Back** to return to the **Chat availability hours** pane.

     6. Click **Save chat availability hours**.

     7. Click chevron_left **Back** to return to the **After hours deflection** pane.

  6. In the **Message** field, enter your after hours deflection message.

  7. Click **Save after hours deflection**.




## Set SMS chat greeting messages

If your administrator has enabled this capability, you can configure the greeting message that displays to an end-user when they contact you with an SMS chat. For information about enabling agents to configure SMS chat greeting messages, see [Direct SMS numbers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/direct-sms-numbers).

To set a SMS chat greeting message, follow these steps:

  1. In the CCAI Platform portal, click ![The open chat icon](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-chat.png)**Chat**. The chat adapter appears.

  2. Click more_vert **Options > Agent SMS messages**. The **Agent SMS messages** pane appears.

  3. Enter a greeting message in the text field.

  4. Optional: To prevent your greeting message from being sent after hours, click the **Skip greeting message after hours** checkbox.

  5. Click **Save SMS messages**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
