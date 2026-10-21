---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-call-blending/
title: Call blending \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:25.942095+00:00
---

# Call blending  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-call-blending/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call blending Stay organized with collections  Save and categorize content based on your preferences. 

With call blending, the system automatically transitions agents between handling outbound campaign calls and inbound IVR calls, based on real-time queue conditions that you configure on your IVR queues. When you're using the same pool of agents to handle outbound campaigns and inbound IVR calls, call blending lets you prioritize inbound call handling during peak periods.

You can configure call blending for a queue using blending conditions. These blending conditions are _agent availability_ , _queue depth_ , and _SLA_. If you configure multiple blending conditions, you can combine these conditions using the following operators:

  * **AND** : All blending conditions must be met before call blending goes into effect.

  * **OR** : At least one of the blending conditions must be met before call blending goes into effect.




When call blending goes into effect for an IVR queue, agents that are assigned to that queue stop being offered calls from all campaign queues that they're assigned to. These agents can then handle inbound calls from the IVR queues that they're assigned to. When call blending is no longer in effect for the queue, agents resume receiving new outbound campaign calls.

**Note:** If an agent is on a campaign call or is reserved for a campaign call when call blending goes into effect, they complete their call or receive the reserved call. After finishing their campaign call, if call blending is still in effect, they stop receiving new campaign calls until call blending is no longer in effect.

## Considerations

Here are some considerations to keep in mind when using call blending:

  * **Call blending has no effect on queue priority**. Queue priority rules are independent of call blending. Queue priority rules are in effect regardless of whether call blending is in effect.

  * **Campaign call-backs are ordinary inbound calls**. If an end-user calls your contact center as a result of a campaign call that they received, the call is treated like any other inbound call. The call enters an inbound queue and is prioritized like all other inbound calls.




## Permissions

Any administrator with **Settings > Queue > All other features** permission can configure these settings. No new permissions are needed.

## Configure call blending

You can configure call blending at the queue level. There's no global configuration.

**Important:** Availability preferences set for agents or teams are overridden by the queue blending configuration when call blending is in effect.

To configure call blending, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **IVR (Interactive Voice Response)** pane, click **Edit / View**.

  3. Click the queue that you want to edit.

  4. In the **Settings** pane, for **Inbound and Outbound Campaign Call Blending** , click **Configure**.

  5. Click the **Blending condition** toggle to the on position.

  6. Select one or more of the following blending conditions and configure each threshold:

     * **Agent availability check**. Blending condition is met when the number of available agents falls below this threshold.

     * **Queue depth**. Blending condition is met when the number of callers in the queue exceeds this threshold.

     * **SLA**. Blending condition is met when the queue falls below these SLA thresholds.

  7. If you select two or more blending conditions, the operator field appears. Select one of the following operators:

     * **AND**. All blending conditions must be met before call blending goes into effect.

     * **OR**. At least one of the blending conditions must be met before call blending goes into effect.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
