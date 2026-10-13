---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-UpdateQueueRequest/
title: Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::UpdateQueueRequest (v0.20.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:55.901492+00:00
---

# Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::UpdateQueueRequest (v0.20.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-UpdateQueueRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::UpdateQueueRequest (v0.20.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.2 (latest)  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.0  0.13.1  0.12.3  0.11.0  0.10.2  0.9.0  0.8.0  0.7.0  0.6.6 

Reference documentation and code samples for the Cloud Tasks V2beta3 API class Google::Cloud::Tasks::V2beta3::UpdateQueueRequest.

Request message for [UpdateQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_update_queue_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#update_queue \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #queue
    
    
    def queue() -> ::Google::Cloud::Tasks::V2beta3::Queue

**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Queue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue)) — Required. The queue to create or update.

The queue's [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue#Google__Cloud__Tasks__V2beta3__Queue_name_instance_ "Google::Cloud::Tasks::V2beta3::Queue#name \(method\)") must be specified.

Output only fields cannot be modified using UpdateQueue. Any value specified for an output only field will be ignored. The queue's [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue#Google__Cloud__Tasks__V2beta3__Queue_name_instance_ "Google::Cloud::Tasks::V2beta3::Queue#name \(method\)") cannot be changed. 




### #queue=
    
    
    def queue=(value) -> ::Google::Cloud::Tasks::V2beta3::Queue

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta3::Queue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue)) — Required. The queue to create or update.

The queue's [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue#Google__Cloud__Tasks__V2beta3__Queue_name_instance_ "Google::Cloud::Tasks::V2beta3::Queue#name \(method\)") must be specified.

Output only fields cannot be modified using UpdateQueue. Any value specified for an output only field will be ignored. The queue's [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue#Google__Cloud__Tasks__V2beta3__Queue_name_instance_ "Google::Cloud::Tasks::V2beta3::Queue#name \(method\)") cannot be changed. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Queue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue)) — Required. The queue to create or update.

The queue's [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue#Google__Cloud__Tasks__V2beta3__Queue_name_instance_ "Google::Cloud::Tasks::V2beta3::Queue#name \(method\)") must be specified.

Output only fields cannot be modified using UpdateQueue. Any value specified for an output only field will be ignored. The queue's [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue#Google__Cloud__Tasks__V2beta3__Queue_name_instance_ "Google::Cloud::Tasks::V2beta3::Queue#name \(method\)") cannot be changed. 




### #update_mask
    
    
    def update_mask() -> ::Google::Protobuf::FieldMask

**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-FieldMask)) — A mask used to specify which fields of the queue are being updated.

If empty, then all fields will be updated. 




### #update_mask=
    
    
    def update_mask=(value) -> ::Google::Protobuf::FieldMask

**Parameter**

  * **value** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-FieldMask)) — A mask used to specify which fields of the queue are being updated.

If empty, then all fields will be updated. 




**Returns**

  * ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-FieldMask)) — A mask used to specify which fields of the queue are being updated.

If empty, then all fields will be updated. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
