---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus/
title: Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::AttemptStatus (v0.18.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:15.627169+00:00
---

# Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::AttemptStatus (v0.18.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::AttemptStatus (v0.18.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.2 (latest)  0.18.1  0.17.0  0.16.1  0.15.0  0.14.1  0.13.0  0.12.1  0.11.3  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.5 

Reference documentation and code samples for the Cloud Tasks V2beta2 API class Google::Cloud::Tasks::V2beta2::AttemptStatus.

The status of a task attempt.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #dispatch_time
    
    
    def dispatch_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that this attempt was dispatched.

`dispatch_time` will be truncated to the nearest microsecond. 




### #dispatch_time=
    
    
    def dispatch_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that this attempt was dispatched.

`dispatch_time` will be truncated to the nearest microsecond. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that this attempt was dispatched.

`dispatch_time` will be truncated to the nearest microsecond. 




### #response_status
    
    
    def response_status() -> ::Google::Rpc::Status

**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Rpc-Status)) — Output only. The response from the target for this attempt.

If the task has not been attempted or the task is currently running then the response status is unset. 




### #response_status=
    
    
    def response_status=(value) -> ::Google::Rpc::Status

**Parameter**

  * **value** ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Rpc-Status)) — Output only. The response from the target for this attempt.

If the task has not been attempted or the task is currently running then the response status is unset. 




**Returns**

  * ([::Google::Rpc::Status](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Rpc-Status)) — Output only. The response from the target for this attempt.

If the task has not been attempted or the task is currently running then the response status is unset. 




### #response_time
    
    
    def response_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that this attempt response was received.

`response_time` will be truncated to the nearest microsecond. 




### #response_time=
    
    
    def response_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that this attempt response was received.

`response_time` will be truncated to the nearest microsecond. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that this attempt response was received.

`response_time` will be truncated to the nearest microsecond. 




### #schedule_time
    
    
    def schedule_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that this attempt was scheduled.

`schedule_time` will be truncated to the nearest microsecond. 




### #schedule_time=
    
    
    def schedule_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that this attempt was scheduled.

`schedule_time` will be truncated to the nearest microsecond. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that this attempt was scheduled.

`schedule_time` will be truncated to the nearest microsecond. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
