---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/prevent-email-reassignment/
title: Prevent email reassignment \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:27.352011+00:00
---

# Prevent email reassignment  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/prevent-email-reassignment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Prevent email reassignment Stay organized with collections  Save and categorize content based on your preferences. 

You can configure Contact Center AI Platform (CCAI Platform) to prevent agents from reassigning emails to other agents. You configure this at the queue level.

## Prevent agents from reassigning emails to other agents

To prevent agents from reassigning emails to other agents, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Email** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, for **Transfer Restrictions** , click **Configure**. The **Transfer Restrictions** pane appears.

  5. Select the **Do not allow email re-assignment from one agent to another** checkbox, and then click **Save**.




## Email reassignment behavior

When you prevent agents from reassigning emails to other agents in a queue, you can expect the following behavior:

  * When agents reply to emails, the **Assign to** field in the agent adapter is deactivated.

  * Agents can assign unassigned emails to themselves in the agent adapter's email list view.

  * Users with the Admin or Manager role can reassign emails from one agent to another in the agent adapter's email list view.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
