---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/smart-actions/
title: Pre-session SmartActions \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:15.937519+00:00
---

# Pre-session SmartActions  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/smart-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Pre-session SmartActions Stay organized with collections  Save and categorize content based on your preferences. 

Pre-session SmartActions (Verification, Images, Videos, Text Input) can be used to gather consumer information prior to starting a mobile support session.

With Pre-session SmartActions enabled, you can verify a consumer's identity, gather support request-related information, and gather assets before the consumer enters a support queue.

Pre-session SmartActions can be configured to be optional conditional based on the estimated wait time in the queue.

The following contact channels are supported:

  * Chat

  * Instant Calls (from the Mobile channel)

  * Email




## Prerequisites

In order to enable the Pre-session SmartActions, you must have the following:

  * A valid CCAI Platform account with Admin role assigned,

  * A valid Legacy, Pro, Enterprise, or Digital License Package, and

  * An integrated CCAI Platform Mobile SDK version 0.39 or higher.




## Administrator configuration

To configure SmartActions, follow these steps.

### Step 1: Enable the pre-session Smart Action for the environment

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management** > **Pre-session SmartActions** section.

  2. Toggle ON the **Pre-session SmartAction** switch.




### Step 2: Configure Pre-session SmartActions for a specific queue

  1. In the CCAI Platform portal, go to **Settings** > **Queue** > **Mobile**.

  2. Select a queue to enable the feature.

  3. In the Queue Settings panel on the right, go to the **Pre-session SmartActions** section.

  4. Turn **ON** the **Pre-session Smart Action toggle** switch. Pre-session Smart Action queue configurations are displayed.

  5. Navigate to the **Custom Copy & Feature Enablement** sub-section and expand the sub-section. Pre-session SmartActions selection options are displayed.

  6. Select the checkboxes of the SmartActions you want to enable as pre-session SmartActions for the specific queue.

  7. Click the **Save** button. The Pre-session Smart Action feature is now enabled for the specific mobile queue.




## Optional Configuration

The following scenarios can be optionally configured.

### Scenario 1: Smart Action based on estimated wait time across all mobile queues

Trigger the Pre-session Smart Action only when Estimated Wait Time is greater configured time limits across all Mobile queues.

  1. In the CCAI Platform portal, on the **Operation Management** page, navigate to the **Pre-session SmartActions** section.

  2. Under the **Time Limit** configurations, select the **Estimated Wait Time** lower limit which the Pre-session SmartActions must not be triggered.

  3. Select the **Do not display** checkbox.

  4. Click the **Set** button. The **Pre-session Smart Action** feature will now be triggered in all mobile queues only when the queue estimated wait time is below the set threshold.


**Note:** This conditional feature will be applicable for only Chat and Call support flows. Email support flow will always display Pre-session SmartActions.

### Scenario 2: Smart Action based on estimated wait time in a specific mobile queue

Trigger the Pre-session Smart Action only when Estimated Wait Time is greater configured time limits in a specific Mobile queue.

  1. In the CCAI Platform portal, go to **Settings** > **Queue** > **Mobile**.

  2. Click a specific queue for which you want to set up the **Estimated Wait Time** limit.

  3. On the **Queue Settings** panel, navigate to the **Pre-session SmartActions** section.

  4. Under the **Time Limit** configurations, select the **Estimated Wait Time** limit which the Pre-session SmartActions must not be triggered.

  5. Select the **Do not display** checkbox.

  6. Click the **Save** button. The Pre-session Smart Action feature will now be triggered in the specific mobile queue only when the queue estimated wait time is below the set threshold.


**Note:** This will be applicable for only Chat and Call support flows. Email support flow will always display Pre-session SmartActions.

### Scenario 3: Smart Action as optional step in specific mobile queue

Trigger the Pre-session SmartActions as an optional step in the Mobile support flow in a specific mobile queue.

  1. In the CCAI Platform portal, go to **Settings** > **Queue** > **Mobile**.

  2. Navigate to the **Queue Settings** page of the mobile queue where you want to set up the **Estimated Wait Time** limit by clicking on the name of the queue.

  3. On the **Queue Settings** panel on the right, navigate to the **Pre-session SmartActions** section.

  4. Under the **Flow Skip** configurations, select the **Optional** checkbox.

  5. Click the **Save** button. The Pre-session Smart Action flow in the specific mobile queue will now be optional in the mobile support flow and can be skipped if necessary.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
