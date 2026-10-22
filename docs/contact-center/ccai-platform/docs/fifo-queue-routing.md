---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/fifo-queue-routing/
title: First in first out queue routing \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:13.524403+00:00
---

# First in first out queue routing  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/fifo-queue-routing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  First in first out queue routing Stay organized with collections  Save and categorize content based on your preferences. 

By default, Contact Center AI Platform (CCAI Platform) prioritizes transferred sessions over incoming calls and chats. If you want all calls or chats to be treated in a first in first out (FIFO) manner, regardless of whether they are transferred, you can turn on FIFO queue routing. Transferred sessions include transferred calls and chats and virtual agent escalations. FIFO queue routing applies to the IVR, mobile, and web channels. You can apply FIFO queue routing globally and at the queue level.

## Turn on FIFO queue routing globally

To turn on FIFO queue routing globally, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Go to the **Routing** pane.

  3. Under **First In First Out (FIFO) Queue Routing** , do one of the following, or both, depending on your requirements:

     * To turn on FIFO queuing for calls, click the **Calls** toggle to the on position.

     * To turn on FIFO queuing for chats, click the **Chats** toggle to the on position.

  4. Click **Save Routing**.




## Turn on FIFO queue routing at the queue level

To turn on FIFO queue routing at the queue level, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. Do one of the following, depending on your requirements:

     * To edit an IVR queue, do the following:

       1. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

       2. Click the queue that you want to edit.

       3. In the **Settings** pane, next to **Routing** , click **Configure**.

       4. Under **First In First Out (FIFO) Queue Routing** , click the **Calls** toggle to the on position, and then click **Save**.

     * To edit a mobile queue, do the following:

       1. In the **Mobile** pane, click **Edit / View**.

       2. Click the queue that you want to edit.

       3. In the **Settings** pane, next to **Routing** , click **Configure**.

       4. Under **First In First Out (FIFO) Queue Routing** , do one of the following, or both, depending on your requirements:

          * Click the **Calls** toggle to the on position.

          * Click the **Chats** toggle to the on position.

       5. Click **Save**.

     * To edit a web queue, do the following:

       1. In the **Web** pane, click **Edit / View**.

       2. Click the queue that you want to edit.

       3. In the **Settings** pane, next to **Routing** , click **Configure**.

       4. Under **First In First Out (FIFO) Queue Routing** , do one of the following, or both, depending on your requirements:

          * Click the **Calls** toggle to the on position.

          * Click the **Chats** toggle to the on position.

       5. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
