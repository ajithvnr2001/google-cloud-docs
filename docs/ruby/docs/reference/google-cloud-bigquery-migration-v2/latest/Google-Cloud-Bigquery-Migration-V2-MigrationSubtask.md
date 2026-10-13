---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationSubtask/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationSubtask (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:06.465845+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationSubtask (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationSubtask/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationSubtask (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::MigrationSubtask.

A subtask for a migration which carries details about the configuration of the subtask. The content of the details should not matter to the end user, but is a contract between the subtask creator and subtask worker.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Timestamp)) — Output only. Time when the subtask was created. 



### #last_update_time
    
    
    def last_update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Timestamp)) — Output only. Time when the subtask was last updated. 



### #metrics
    
    
    def metrics() -> ::Array<::Google::Cloud::Bigquery::Migration::V2::TimeSeries>

**Returns**

  * (::Array<[::Google::Cloud::Bigquery::Migration::V2::TimeSeries](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-TimeSeries)>) — Output only. The metrics for the subtask. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — Output only. Immutable. The resource name for the migration subtask. The ID is server-generated.

Example: `projects/123/locations/us/workflows/345/subtasks/678`




### #processing_error
    
    
    def processing_error() -> ::Google::Rpc::ErrorInfo

**Returns**

  * ([::Google::Rpc::ErrorInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Rpc-ErrorInfo)) — Output only. An explanation that may be populated when the task is in FAILED state. 



### #resource_error_count
    
    
    def resource_error_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number or resources with errors. Note: This is not the total number of errors as each resource can have more than one error. This is used to indicate truncation by having a `resource_error_count` that is higher than the size of `resource_error_details`. 



### #resource_error_details
    
    
    def resource_error_details() -> ::Array<::Google::Cloud::Bigquery::Migration::V2::ResourceErrorDetail>

**Returns**

  * (::Array<[::Google::Cloud::Bigquery::Migration::V2::ResourceErrorDetail](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-ResourceErrorDetail)>) — Output only. Provides details to errors and issues encountered while processing the subtask. Presence of error details does not mean that the subtask failed. 



### #state
    
    
    def state() -> ::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask::State

**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationSubtask-State)) — Output only. The current state of the subtask. 



### #task_id
    
    
    def task_id() -> ::String

**Returns**

  * (::String) — The unique ID of the task to which this subtask belongs. 



### #task_id=
    
    
    def task_id=(value) -> ::String

**Parameter**

  * **value** (::String) — The unique ID of the task to which this subtask belongs. 



**Returns**

  * (::String) — The unique ID of the task to which this subtask belongs. 



### #type
    
    
    def type() -> ::String

**Returns**

  * (::String) — The type of the Subtask. The migration service does not check whether this is a known type. It is up to the task creator (i.e. orchestrator or worker) to ensure it only creates subtasks for which there are compatible workers polling for Subtasks. 



### #type=
    
    
    def type=(value) -> ::String

**Parameter**

  * **value** (::String) — The type of the Subtask. The migration service does not check whether this is a known type. It is up to the task creator (i.e. orchestrator or worker) to ensure it only creates subtasks for which there are compatible workers polling for Subtasks. 



**Returns**

  * (::String) — The type of the Subtask. The migration service does not check whether this is a known type. It is up to the task creator (i.e. orchestrator or worker) to ensure it only creates subtasks for which there are compatible workers polling for Subtasks. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
