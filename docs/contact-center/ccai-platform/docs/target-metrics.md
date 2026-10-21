---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/target-metrics/
title: Target metrics \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:38.602410+00:00
---

# Target metrics  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/target-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Target metrics Stay organized with collections  Save and categorize content based on your preferences. 

Each contact center has a unique set of target metrics that are used to evaluate the efficiencies at goals for the operation. One set of target metrics can be set per environment, and those metrics will be used in dashboards and also show in the Agent Adapter.

These target metrics are set for all applicable channels and queues in the environment. Some metrics like Service Level and Chat Concurrency can also be set at the queue level, overriding this global setting.

## Metric details

  * **Repeat Contact Time Period** : Tracks the number of consumers who initiated multiple incoming sessions that finished in the same queue within the set time period.

  * **Service Level Target (SLA)** : Tracks call percentage of calls and chats answered within the set timeframe, shown in dashboards and reports. Used as the default target for all queues and can be overridden for each queue (Settings > Queue).

  * **Chat Concurrency** : (Chats only) Goal number of chats handled by an individual agent at a time. Used as the default target for all queues and can be overridden for each queue (Settings > Queue). This target is displayed on the Chat dashboard.

  * **Target Pick Up Time** : (Calls only) A target time countdown that agents see in their adapter during an incoming call. Once the target pickup time has been reached, the size of the countdown font grows in size.




## Configuration

  1. In the CCAI Platform portal, go to **Settings** > **Operation Management**.

  2. Navigate to the **Target Metrics** section.

  3. Set or edit the values for each metric.

  4. Click **Set Metrics** to save changes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
