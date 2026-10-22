---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/let-agents-transfer-email-sessions-to-a-queue/
title: Transfer email sessions to a queue \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:00.041814+00:00
---

# Transfer email sessions to a queue  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/let-agents-transfer-email-sessions-to-a-queue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Transfer email sessions to a queue Stay organized with collections  Save and categorize content based on your preferences. 

You can configure Contact Center AI Platform (CCAI Platform) so that agents can [transfer an email session from one queue to another](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#transfer-email-session-from-one-queue-to-another). When an agent transfers an email session between queues, the session ID is maintained and a new email session isn't created. This is in contrast to when an [agent assigns an email directly to another agent](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#assign-email-sessions-to-another-agent). In that case, a new email session is created.

You can also prevent a queue from receiving email transfers.

## Turn on email transfers

To turn on email transfers, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Email**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **General** pane, for **Email Management** , select the **Enable Email Transfer Between Queues** checkbox.

  3. Click **Save**.




## Prevent a queue from receiving email transfers

You can configure any queue to prevent it from receiving email session transfers.

To prevent a queue from receiving email transfers, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Email** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, for **Allow incoming Email Transfers** , click the toggle to the off position.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
