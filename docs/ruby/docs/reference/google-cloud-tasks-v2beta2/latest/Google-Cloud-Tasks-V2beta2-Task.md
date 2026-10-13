---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Task/
title: Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::Task (v0.18.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:27.488446+00:00
---

# Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::Task (v0.18.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2beta2 API - Class Google::Cloud::Tasks::V2beta2::Task (v0.18.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.18.2 (latest)  0.18.1  0.17.0  0.16.1  0.15.0  0.14.1  0.13.0  0.12.1  0.11.3  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.5 

Reference documentation and code samples for the Cloud Tasks V2beta2 API class Google::Cloud::Tasks::V2beta2::Task.

A unit of scheduled work.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_engine_http_request
    
    
    def app_engine_http_request() -> ::Google::Cloud::Tasks::V2beta2::AppEngineHttpRequest

**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpRequest)) — App Engine HTTP request that is sent to the task's target. Can be set only if [app_engine_http_target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Queue#Google__Cloud__Tasks__V2beta2__Queue_app_engine_http_target_instance_ "Google::Cloud::Tasks::V2beta2::Queue#app_engine_http_target \(method\)") is set on the queue.

An App Engine task is a task that has [AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpRequest "Google::Cloud::Tasks::V2beta2::AppEngineHttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `app_engine_http_request`, `pull_message`, `http_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #app_engine_http_request=
    
    
    def app_engine_http_request=(value) -> ::Google::Cloud::Tasks::V2beta2::AppEngineHttpRequest

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta2::AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpRequest)) — App Engine HTTP request that is sent to the task's target. Can be set only if [app_engine_http_target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Queue#Google__Cloud__Tasks__V2beta2__Queue_app_engine_http_target_instance_ "Google::Cloud::Tasks::V2beta2::Queue#app_engine_http_target \(method\)") is set on the queue.

An App Engine task is a task that has [AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpRequest "Google::Cloud::Tasks::V2beta2::AppEngineHttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `app_engine_http_request`, `pull_message`, `http_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpRequest)) — App Engine HTTP request that is sent to the task's target. Can be set only if [app_engine_http_target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Queue#Google__Cloud__Tasks__V2beta2__Queue_app_engine_http_target_instance_ "Google::Cloud::Tasks::V2beta2::Queue#app_engine_http_target \(method\)") is set on the queue.

An App Engine task is a task that has [AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-AppEngineHttpRequest "Google::Cloud::Tasks::V2beta2::AppEngineHttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `app_engine_http_request`, `pull_message`, `http_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that the task was created.

`create_time` will be truncated to the nearest second. 




### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that the task was created.

`create_time` will be truncated to the nearest second. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — Output only. The time that the task was created.

`create_time` will be truncated to the nearest second. 




### #http_request
    
    
    def http_request() -> ::Google::Cloud::Tasks::V2beta2::HttpRequest

**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-HttpRequest)) — HTTP request that is sent to the task's target.

An HTTP task is a task that has [HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-HttpRequest "Google::Cloud::Tasks::V2beta2::HttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `http_request`, `app_engine_http_request`, `pull_message`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #http_request=
    
    
    def http_request=(value) -> ::Google::Cloud::Tasks::V2beta2::HttpRequest

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta2::HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-HttpRequest)) — HTTP request that is sent to the task's target.

An HTTP task is a task that has [HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-HttpRequest "Google::Cloud::Tasks::V2beta2::HttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `http_request`, `app_engine_http_request`, `pull_message`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-HttpRequest)) — HTTP request that is sent to the task's target.

An HTTP task is a task that has [HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-HttpRequest "Google::Cloud::Tasks::V2beta2::HttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `http_request`, `app_engine_http_request`, `pull_message`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — 

Optionally caller-specified in [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-CloudTasks-Client#Google__Cloud__Tasks__V2beta2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2beta2::CloudTasks::Client#create_task \(method\)").

The task name.

The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`

    * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling [ListLocations][google.cloud.location.Locations.ListLocations]. For more information, see https://cloud.google.com/about/locations/.
    * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.
    * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Optionally caller-specified in [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-CloudTasks-Client#Google__Cloud__Tasks__V2beta2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2beta2::CloudTasks::Client#create_task \(method\)").

The task name.

The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`

    * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling [ListLocations][google.cloud.location.Locations.ListLocations]. For more information, see https://cloud.google.com/about/locations/.
    * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.
    * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.



**Returns**

  * (::String) — 

Optionally caller-specified in [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-CloudTasks-Client#Google__Cloud__Tasks__V2beta2__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2beta2::CloudTasks::Client#create_task \(method\)").

The task name.

The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`

    * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling [ListLocations][google.cloud.location.Locations.ListLocations]. For more information, see https://cloud.google.com/about/locations/.
    * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.
    * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.



### #pull_message
    
    
    def pull_message() -> ::Google::Cloud::Tasks::V2beta2::PullMessage

**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::PullMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-PullMessage)) — [LeaseTasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-CloudTasks-Client#Google__Cloud__Tasks__V2beta2__CloudTasks__Client_lease_tasks_instance_ "Google::Cloud::Tasks::V2beta2::CloudTasks::Client#lease_tasks \(method\)") to process the task. Can be set only if [pull_target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Queue#Google__Cloud__Tasks__V2beta2__Queue_pull_target_instance_ "Google::Cloud::Tasks::V2beta2::Queue#pull_target \(method\)") is set on the queue.

A pull task is a task that has [PullMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-PullMessage "Google::Cloud::Tasks::V2beta2::PullMessage \(class\)") set.

Note: The following fields are mutually exclusive: `pull_message`, `app_engine_http_request`, `http_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #pull_message=
    
    
    def pull_message=(value) -> ::Google::Cloud::Tasks::V2beta2::PullMessage

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta2::PullMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-PullMessage)) — [LeaseTasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-CloudTasks-Client#Google__Cloud__Tasks__V2beta2__CloudTasks__Client_lease_tasks_instance_ "Google::Cloud::Tasks::V2beta2::CloudTasks::Client#lease_tasks \(method\)") to process the task. Can be set only if [pull_target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Queue#Google__Cloud__Tasks__V2beta2__Queue_pull_target_instance_ "Google::Cloud::Tasks::V2beta2::Queue#pull_target \(method\)") is set on the queue.

A pull task is a task that has [PullMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-PullMessage "Google::Cloud::Tasks::V2beta2::PullMessage \(class\)") set.

Note: The following fields are mutually exclusive: `pull_message`, `app_engine_http_request`, `http_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::PullMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-PullMessage)) — [LeaseTasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-CloudTasks-Client#Google__Cloud__Tasks__V2beta2__CloudTasks__Client_lease_tasks_instance_ "Google::Cloud::Tasks::V2beta2::CloudTasks::Client#lease_tasks \(method\)") to process the task. Can be set only if [pull_target](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Queue#Google__Cloud__Tasks__V2beta2__Queue_pull_target_instance_ "Google::Cloud::Tasks::V2beta2::Queue#pull_target \(method\)") is set on the queue.

A pull task is a task that has [PullMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-PullMessage "Google::Cloud::Tasks::V2beta2::PullMessage \(class\)") set.

Note: The following fields are mutually exclusive: `pull_message`, `app_engine_http_request`, `http_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #schedule_time
    
    
    def schedule_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — The time when the task is scheduled to be attempted.

For App Engine queues, this is when the task will be attempted or retried.

For pull queues, this is the time when the task is available to be leased; if a task is currently leased, this is the time when the current lease expires, that is, the time that the task was leased plus the [lease_duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-LeaseTasksRequest#Google__Cloud__Tasks__V2beta2__LeaseTasksRequest_lease_duration_instance_ "Google::Cloud::Tasks::V2beta2::LeaseTasksRequest#lease_duration \(method\)").

`schedule_time` will be truncated to the nearest microsecond. 




### #schedule_time=
    
    
    def schedule_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — The time when the task is scheduled to be attempted.

For App Engine queues, this is when the task will be attempted or retried.

For pull queues, this is the time when the task is available to be leased; if a task is currently leased, this is the time when the current lease expires, that is, the time that the task was leased plus the [lease_duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-LeaseTasksRequest#Google__Cloud__Tasks__V2beta2__LeaseTasksRequest_lease_duration_instance_ "Google::Cloud::Tasks::V2beta2::LeaseTasksRequest#lease_duration \(method\)").

`schedule_time` will be truncated to the nearest microsecond. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Protobuf-Timestamp)) — The time when the task is scheduled to be attempted.

For App Engine queues, this is when the task will be attempted or retried.

For pull queues, this is the time when the task is available to be leased; if a task is currently leased, this is the time when the current lease expires, that is, the time that the task was leased plus the [lease_duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-LeaseTasksRequest#Google__Cloud__Tasks__V2beta2__LeaseTasksRequest_lease_duration_instance_ "Google::Cloud::Tasks::V2beta2::LeaseTasksRequest#lease_duration \(method\)").

`schedule_time` will be truncated to the nearest microsecond. 




### #status
    
    
    def status() -> ::Google::Cloud::Tasks::V2beta2::TaskStatus

**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::TaskStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-TaskStatus)) — Output only. The task status. 



### #status=
    
    
    def status=(value) -> ::Google::Cloud::Tasks::V2beta2::TaskStatus

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta2::TaskStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-TaskStatus)) — Output only. The task status. 



**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::TaskStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-TaskStatus)) — Output only. The task status. 



### #view
    
    
    def view() -> ::Google::Cloud::Tasks::V2beta2::Task::View

**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::Task::View](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Task-View)) — Output only. The view specifies which subset of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Task "Google::Cloud::Tasks::V2beta2::Task \(class\)") has been returned. 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::Tasks::V2beta2::Task::View

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta2::Task::View](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Task-View)) — Output only. The view specifies which subset of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Task "Google::Cloud::Tasks::V2beta2::Task \(class\)") has been returned. 



**Returns**

  * ([::Google::Cloud::Tasks::V2beta2::Task::View](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Task-View)) — Output only. The view specifies which subset of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta2/latest/Google-Cloud-Tasks-V2beta2-Task "Google::Cloud::Tasks::V2beta2::Task \(class\)") has been returned. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
