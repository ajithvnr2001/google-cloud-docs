---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-real-time-operations-and-monitoring/
title: Real-time operations and monitoring \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:41:03.317108+00:00
---

# Real-time operations and monitoring  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-real-time-operations-and-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Real-time operations and monitoring Stay organized with collections  Save and categorize content based on your preferences. 

Real time dashboards focus on high-level awareness, immediate operational shifts, and technical health for live environments.

## Operational use cases

Real-time dashboards can help you monitor the following operational use cases:

  * **Intraday resource rebalancing**. Analysts monitor the ratio of available agents to calls in queue to make immediate staffing adjustments.

  * **Performance accountability**. Managers filter by specific teams to ensure agents are in the correct status and adhering to their scheduled activities.

  * **Service level preservation**. Analysts identify queue spikes to proactively cancel offline activities like meetings or training.

  * **Floor awareness**. Wallboards provide a high-level, queue-focused view of health (SLA, number queuing, max wait time) to reduce agent stress.




## Key metrics

The following are some key metrics to monitor with your real-time dashboards:

  * **Total queued now**. Represents the number of customers waiting in queue to be connected to an agent. High counts lead to SLA degradation and increased customer frustration and potential abandons.

  * **Max queue wait time**. The longest duration a customer has been waiting in the current queue. Serves as a primary stress indicator; rising wait times signal a need for immediate resource shifting.

  * **Agent occupancy**. The percentage of time agents spend on active interactions versus being available. Helps balance agent burnout against cost-efficiency.




## Strategic investigation: Technical friction versus volume surges

You can use real-time dashboards—including prebuilt templates labeled "real-time" and custom dashboards that refresh in one minute or less—to investigate whether a performance drop is caused by technical friction or volume surges. Consider the following factors:

  * **IVR technical friction** : If **Total queued now** (from **Call Metrics (Live)**) is rising at the same time as **Failed sessions** (from **Call Session Metrics (Historical)**), the issue is likely technical friction in the IVR, not just a surge in call volume. Create a custom dashboard displaying these metrics side-by-side to monitor this.
  * **Wait-time VA impact** : If the _wait-time VA_ is active, be aware that calls it handles are prioritized to the top of the queue and counted as _Queue interactions_ rather than standard _Queue entries_. This distinction is important when analyzing queue metrics.



## Best practices

  * **Agent connectivity**. If an agent appears missing, check the **Agent Activity** dashboard; the reason **Agent put offline by system** indicates a network failure.

  * **Discrepancy in handled totals**. Use **Total queue answered** instead of **Total handled** (both from **Call Queue Metrics (Historical)**) for reconciling queue-specific interactions.

  * **Automatic sign-out**. Use a dedicated service account for wallboards to prevent inactivity timeouts.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
