---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-historical-and-sla-deep-dives/
title: Historical analysis and service level deep-dives \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:38.371479+00:00
---

# Historical analysis and service level deep-dives  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-historical-and-sla-deep-dives/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Historical analysis and service level deep-dives Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses performance trends, root-cause analysis, and long-term planning.

## Analysis use cases

  * **SLA failure root cause**. Analysts compare current periods against previous thresholds to pinpoint exactly when service levels dropped.

  * **Short abandon tracking**. The _Queue interval dashboard_ is the primary source for identifying callers who disconnect quickly within the IVR. Short abandons are not included in the SLA calculation if you have configured the platform to eliminate them using a threshold.

  * **FCR and training analysis**. Managers track transfer frequency and _Third-party time_ to identify training gaps or routing errors.

  * **Trend identification**. Planners use drillable data points to identify recurring daily or weekly call patterns.




## Key metrics

  * **Short abandons** (from **Call Queue Metrics (Historical)**). Callers who disconnect within a narrow time window (for example, 5-10 seconds). A high volume of short-abandons often indicate a confusing IVR or technical issues

  * **Third-party time** (from **Third Party Calls (Historical)**). The amount of time that interactions are connected to a third party. Essential for tracking the cost and efficiency of external handoffs.

  * **Queue Entries (distinct interactions)** (from **Call Queue Metrics (Historical)**). The number of end-users that enter the contact center through a queue. This number doesn't include transfers. This number provides the most accurate view of actual customer volume and demand.




## Strategic investigation: volume metric reconciliation

  * **Sessions versus interactions**. A session represents the total system touchpoint. _Queue interactions_ include the entry plus other touchpoints like the _Virtual assistant_.

  * **Entries versus interactions**. A _Queue entry_ counts a call regardless of transfers. A _Queue interaction_ includes transfers and touchpoints.

  * **Unique volume**. Use _Queue entries_ to see unique customer volume without transfer inflation.




## Complex troubleshooting: identifying ghost SLA drops

  * **Short abandon logic**. Check for _Short abandons_ ; they are not included in _Queue entries_ (both from _Call Queue Metrics (Historical)_) and strictly excluded from SLA calculations.

  * **Transfer loops**. Review the Transfers dashboard for the same _Call ID_ across different queues; this indicates the interaction is "bouncing" between queues.

  * **Deflection patterns**. Review data in the Deflections dashboard. A callback deflection won't be identified in the _perf va_ table because the virtual agent drops the call into a queue first.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
