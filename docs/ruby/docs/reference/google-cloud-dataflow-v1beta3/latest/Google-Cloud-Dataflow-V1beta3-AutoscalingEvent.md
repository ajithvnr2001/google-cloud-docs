---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-AutoscalingEvent/
title: Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::AutoscalingEvent (v0.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:51:57.269441+00:00
---

# Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::AutoscalingEvent (v0.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-AutoscalingEvent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataflow V1beta3 API - Class Google::Cloud::Dataflow::V1beta3::AutoscalingEvent (v0.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.1 (latest)  0.17.0  0.16.0  0.15.0  0.14.1  0.13.1  0.12.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Dataflow V1beta3 API class Google::Cloud::Dataflow::V1beta3::AutoscalingEvent.

A structured message reporting an autoscaling decision made by the Dataflow service.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #current_num_workers
    
    
    def current_num_workers() -> ::Integer

**Returns**

  * (::Integer) — The current number of workers the job has. 



### #current_num_workers=
    
    
    def current_num_workers=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The current number of workers the job has. 



**Returns**

  * (::Integer) — The current number of workers the job has. 



### #description
    
    
    def description() -> ::Google::Cloud::Dataflow::V1beta3::StructuredMessage

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::StructuredMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StructuredMessage)) — A message describing why the system decided to adjust the current number of workers, why it failed, or why the system decided to not make any changes to the number of workers. 



### #description=
    
    
    def description=(value) -> ::Google::Cloud::Dataflow::V1beta3::StructuredMessage

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::StructuredMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StructuredMessage)) — A message describing why the system decided to adjust the current number of workers, why it failed, or why the system decided to not make any changes to the number of workers. 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::StructuredMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-StructuredMessage)) — A message describing why the system decided to adjust the current number of workers, why it failed, or why the system decided to not make any changes to the number of workers. 



### #event_type
    
    
    def event_type() -> ::Google::Cloud::Dataflow::V1beta3::AutoscalingEvent::AutoscalingEventType

**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::AutoscalingEvent::AutoscalingEventType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-AutoscalingEvent-AutoscalingEventType)) — The type of autoscaling event to report. 



### #event_type=
    
    
    def event_type=(value) -> ::Google::Cloud::Dataflow::V1beta3::AutoscalingEvent::AutoscalingEventType

**Parameter**

  * **value** ([::Google::Cloud::Dataflow::V1beta3::AutoscalingEvent::AutoscalingEventType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-AutoscalingEvent-AutoscalingEventType)) — The type of autoscaling event to report. 



**Returns**

  * ([::Google::Cloud::Dataflow::V1beta3::AutoscalingEvent::AutoscalingEventType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Cloud-Dataflow-V1beta3-AutoscalingEvent-AutoscalingEventType)) — The type of autoscaling event to report. 



### #target_num_workers
    
    
    def target_num_workers() -> ::Integer

**Returns**

  * (::Integer) — The target number of workers the worker pool wants to resize to use. 



### #target_num_workers=
    
    
    def target_num_workers=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The target number of workers the worker pool wants to resize to use. 



**Returns**

  * (::Integer) — The target number of workers the worker pool wants to resize to use. 



### #time
    
    
    def time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Timestamp)) — The time this event was emitted to indicate a new target or current num_workers value. 



### #time=
    
    
    def time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Timestamp)) — The time this event was emitted to indicate a new target or current num_workers value. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataflow-v1beta3/latest/Google-Protobuf-Timestamp)) — The time this event was emitted to indicate a new target or current num_workers value. 



### #worker_pool
    
    
    def worker_pool() -> ::String

**Returns**

  * (::String) — A short and friendly name for the worker pool this event refers to. 



### #worker_pool=
    
    
    def worker_pool=(value) -> ::String

**Parameter**

  * **value** (::String) — A short and friendly name for the worker pool this event refers to. 



**Returns**

  * (::String) — A short and friendly name for the worker pool this event refers to. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
