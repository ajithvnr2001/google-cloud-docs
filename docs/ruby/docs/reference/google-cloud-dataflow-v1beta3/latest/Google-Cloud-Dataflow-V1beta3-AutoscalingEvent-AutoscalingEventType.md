---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-AutoscalingEvent-AutoscalingEventType/
title: Dataflow V1beta3 API - Module Google::Cloud::Dataflow::V1beta3::AutoscalingEvent::AutoscalingEventType (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:57.356500+00:00
---

# Dataflow V1beta3 API - Module Google::Cloud::Dataflow::V1beta3::AutoscalingEvent::AutoscalingEventType (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-AutoscalingEvent-AutoscalingEventType/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Module Google::Cloud::Dataflow::V1beta3::AutoscalingEvent::AutoscalingEventType (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API module Google::Cloud::Dataflow::V1beta3::AutoscalingEvent::AutoscalingEventType.

Indicates the type of autoscaling event.

## Constants 

### TYPE_UNKNOWN

**value:** 0  
Default type for the enum. Value should never be returned.

### TARGET_NUM_WORKERS_CHANGED

**value:** 1  
The TARGET_NUM_WORKERS_CHANGED type should be used when the target worker pool size has changed at the start of an actuation. An event should always be specified as TARGET_NUM_WORKERS_CHANGED if it reflects a change in the target_num_workers.

### CURRENT_NUM_WORKERS_CHANGED

**value:** 2  
The CURRENT_NUM_WORKERS_CHANGED type should be used when actual worker pool size has been changed, but the target_num_workers has not changed.

### ACTUATION_FAILURE

**value:** 3  
The ACTUATION_FAILURE type should be used when we want to report an error to the user indicating why the current number of workers in the pool could not be changed. Displayed in the current status and history widgets.

### NO_CHANGE

**value:** 4  
Used when we want to report to the user a reason why we are not currently adjusting the number of workers. Should specify both target_num_workers, current_num_workers and a decision_message.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
