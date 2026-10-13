---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-TaskStatus/
title: Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::TaskStatus (v0.18.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:39.632325+00:00
---

# Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::TaskStatus (v0.18.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-TaskStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::TaskStatus (v0.18.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.2 (latest)  0.18.1  0.17.0  0.16.1  0.15.0  0.14.1  0.13.0  0.12.1  0.11.3  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.5 

Reference documentation and code samples for the Cloud Tasks V2beta2 API class Google::Cloud::Tasks::V2beta2::TaskStatus.

Status of the task.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #attempt_dispatch_count
    
    
    def attempt_dispatch_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of attempts dispatched.

This count includes attempts which have been dispatched but haven't received a response. 




### #attempt_dispatch_count=
    
    
    def attempt_dispatch_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. The number of attempts dispatched.

This count includes attempts which have been dispatched but haven't received a response. 




**Returns**

  * (::Integer) — Output only. The number of attempts dispatched.

This count includes attempts which have been dispatched but haven't received a response. 




### #attempt_response_count
    
    
    def attempt_response_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of attempts which have received a response.

This field is not calculated for [pull tasks][google.cloud.tasks.v2beta2.PullMessage]. 




### #attempt_response_count=
    
    
    def attempt_response_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. The number of attempts which have received a response.

This field is not calculated for [pull tasks][google.cloud.tasks.v2beta2.PullMessage]. 




**Returns**

  * (::Integer) — Output only. The number of attempts which have received a response.

This field is not calculated for [pull tasks][google.cloud.tasks.v2beta2.PullMessage]. 




### #first_attempt_status
    
    
    def first_attempt_status() -> ::Google::Cloud::Tasks::V2beta2::AttemptStatus

**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::AttemptStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus)) — Output only. The status of the task's first attempt.

Only [dispatch_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus#Google__Cloud__Tasks__V2beta2__AttemptStatus_dispatch_time_instance_ "Google::Cloud::Tasks::V2beta2::AttemptStatus#dispatch_time \(method\)") will be set. The other [AttemptStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus "Google::Cloud::Tasks::V2beta2::AttemptStatus \(class\)") information is not retained by Cloud Tasks.

This field is not calculated for [pull tasks][google.cloud.tasks.v2beta2.PullMessage]. 




### #first_attempt_status=
    
    
    def first_attempt_status=(value) -> ::Google::Cloud::Tasks::V2beta2::AttemptStatus

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta2::AttemptStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus)) — Output only. The status of the task's first attempt.

Only [dispatch_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus#Google__Cloud__Tasks__V2beta2__AttemptStatus_dispatch_time_instance_ "Google::Cloud::Tasks::V2beta2::AttemptStatus#dispatch_time \(method\)") will be set. The other [AttemptStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus "Google::Cloud::Tasks::V2beta2::AttemptStatus \(class\)") information is not retained by Cloud Tasks.

This field is not calculated for [pull tasks][google.cloud.tasks.v2beta2.PullMessage]. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::AttemptStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus)) — Output only. The status of the task's first attempt.

Only [dispatch_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus#Google__Cloud__Tasks__V2beta2__AttemptStatus_dispatch_time_instance_ "Google::Cloud::Tasks::V2beta2::AttemptStatus#dispatch_time \(method\)") will be set. The other [AttemptStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus "Google::Cloud::Tasks::V2beta2::AttemptStatus \(class\)") information is not retained by Cloud Tasks.

This field is not calculated for [pull tasks][google.cloud.tasks.v2beta2.PullMessage]. 




### #last_attempt_status
    
    
    def last_attempt_status() -> ::Google::Cloud::Tasks::V2beta2::AttemptStatus

**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::AttemptStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus)) — Output only. The status of the task's last attempt.

This field is not calculated for [pull tasks][google.cloud.tasks.v2beta2.PullMessage]. 




### #last_attempt_status=
    
    
    def last_attempt_status=(value) -> ::Google::Cloud::Tasks::V2beta2::AttemptStatus

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta2::AttemptStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus)) — Output only. The status of the task's last attempt.

This field is not calculated for [pull tasks][google.cloud.tasks.v2beta2.PullMessage]. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::AttemptStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AttemptStatus)) — Output only. The status of the task's last attempt.

This field is not calculated for [pull tasks][google.cloud.tasks.v2beta2.PullMessage]. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
