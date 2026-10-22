---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-level-target-metrics/
title: Queue level target metrics \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:36.313848+00:00
---

# Queue level target metrics  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-level-target-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Queue level target metrics Stay organized with collections  Save and categorize content based on your preferences. 

In addition to the global settings for target metrics, for further granularity, you can set queue-specific target metrics. Depending on the specific settings, each queue can also have specific targets for different channels.

## Global target metrics

Target metrics set at the global level on the **Settings** > **Operation Management** page will continue to be inherited by all queues by default.

To learn how to set up a global target metric, see [Target metrics](https://docs.cloud.google.com/contact-center/ccai-platform/docs/target-metrics).

## Target metric priority order

When a queue-specific target is set for a Top-level queue, all sub-queues will inherit the set target metric.

When a queue-specific target metric is set for a sub-queue, it will override both the global target metric and the Top-level queue target metric for the queue.

Priority order = Sub-queue Target > Top-level Queue Target > Global Target

Examples:

Targets Set | Resulting Targets  
---|---  
**Global Target = 70%** , **Top-level Queue 1 = None** , Queue 1a = None, Queue 1b = None, Queue 2a = None, Queue 2b = None, **Top-level Queue 2 = None** | **Global Target = 70%** , **Top-level Queue 1 = 70% (inherited from global)** , Queue 1a = 70% (inherited from global), Queue 1b = 70% (inherited from global), Queue 2a = 70% (inherited from global), Queue 2b = 70% (inherited from global), **Top-level Queue 2 = 70% (inherited from global)**  
**Global Target = 70%** , **Top-level Queue 1 = 65%** , Queue 1a = None, Queue 1b = 75%, Queue 2a = 65%, Queue 2b = None, **Top-level Queue 2 = None** | **Global Target = 70%** , **Top-level Queue 1 = 65%** , Queue 1a = 65% (inherited from Top-level), Queue 1b = 75%, Queue 2a = 65%, Queue 2b = 70% (inherited from global),**Top-level Queue 2 = None**  
**Global Target = None** , **Top-level Queue 1 = 65%** , Queue 1a = None, Queue 1b = None, Queue 2a = 60%, Queue 2b = 40%, **Top-level Queue 2 = None** | **Global Target = None** , **Top-level Queue 1 = 65%** , Queue 1a = 65% (inherited from Top-level), Queue 1b = 65% (inherited from Top-level), **Top-level Queue 2 = None** , Queue 2a = 60%, Queue 2b = 40%  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
