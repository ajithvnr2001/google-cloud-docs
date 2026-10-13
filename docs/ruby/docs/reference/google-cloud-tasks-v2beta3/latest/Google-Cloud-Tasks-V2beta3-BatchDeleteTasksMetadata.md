---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-BatchDeleteTasksMetadata/
title: Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::BatchDeleteTasksMetadata (v0.20.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:00.225579+00:00
---

# Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::BatchDeleteTasksMetadata (v0.20.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-BatchDeleteTasksMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::BatchDeleteTasksMetadata (v0.20.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.2 (latest)  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.0  0.13.1  0.12.3  0.11.0  0.10.2  0.9.0  0.8.0  0.7.0  0.6.6 

Reference documentation and code samples for the Cloud Tasks V2beta3 API class Google::Cloud::Tasks::V2beta3::BatchDeleteTasksMetadata.

Metadata for the long-running operation returned by [BatchDeleteTasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_batch_delete_tasks_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#batch_delete_tasks \(method\)"). This message is used to hold metadata information about the batch delete tasks operation; that is, it is put in [google.longrunning.Operation.metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_metadata_instance_ "Google::Longrunning::Operation#metadata \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Timestamp)) — Output only. The time when the batch delete finished. 



### #failed_requests
    
    
    def failed_requests() -> ::Google::Protobuf::Map{::Integer => ::Google::Rpc::Status}

**Returns**

  * (::Google::Protobuf::Map{::Integer => ::Google::Rpc::Status}) — Output only. A map of failed requests, where the key is the index of the request in BatchDeleteTasksRequest.names and the value is the error status. 



### #start_time
    
    
    def start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Timestamp)) — Output only. The time when the batch delete started. 



### #state
    
    
    def state() -> ::Google::Cloud::Tasks::V2beta3::BatchDeleteTasksMetadata::State

**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::BatchDeleteTasksMetadata::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-BatchDeleteTasksMetadata-State)) — Output only. The state of the batch delete operation. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
