---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task/
title: Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::Task (v0.20.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:09.960138+00:00
---

# Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::Task (v0.20.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::Task (v0.20.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.2 (latest)  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.0  0.13.1  0.12.3  0.11.0  0.10.2  0.9.0  0.8.0  0.7.0  0.6.6 

Reference documentation and code samples for the Cloud Tasks V2beta3 API class Google::Cloud::Tasks::V2beta3::Task.

A unit of scheduled work.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_engine_http_request
    
    
    def app_engine_http_request() -> ::Google::Cloud::Tasks::V2beta3::AppEngineHttpRequest

**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineHttpRequest)) — HTTP request that is sent to the App Engine app handler.

An App Engine task is a task that has [AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineHttpRequest "Google::Cloud::Tasks::V2beta3::AppEngineHttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `app_engine_http_request`, `http_request`, `pull_message`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #app_engine_http_request=
    
    
    def app_engine_http_request=(value) -> ::Google::Cloud::Tasks::V2beta3::AppEngineHttpRequest

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta3::AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineHttpRequest)) — HTTP request that is sent to the App Engine app handler.

An App Engine task is a task that has [AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineHttpRequest "Google::Cloud::Tasks::V2beta3::AppEngineHttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `app_engine_http_request`, `http_request`, `pull_message`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineHttpRequest)) — HTTP request that is sent to the App Engine app handler.

An App Engine task is a task that has [AppEngineHttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineHttpRequest "Google::Cloud::Tasks::V2beta3::AppEngineHttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `app_engine_http_request`, `http_request`, `pull_message`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Timestamp)) — Output only. The time that the task was created.

`create_time` will be truncated to the nearest second. 




### #create_time=
    
    
    def create_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Timestamp)) — Output only. The time that the task was created.

`create_time` will be truncated to the nearest second. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Timestamp)) — Output only. The time that the task was created.

`create_time` will be truncated to the nearest second. 




### #dispatch_count
    
    
    def dispatch_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of attempts dispatched.

This count includes attempts which have been dispatched but haven't received a response. 




### #dispatch_count=
    
    
    def dispatch_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. The number of attempts dispatched.

This count includes attempts which have been dispatched but haven't received a response. 




**Returns**

  * (::Integer) — Output only. The number of attempts dispatched.

This count includes attempts which have been dispatched but haven't received a response. 




### #dispatch_deadline
    
    
    def dispatch_deadline() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — The deadline for requests sent to the worker. If the worker does not respond by this deadline then the request is cancelled and the attempt is marked as a `DEADLINE_EXCEEDED` failure. Cloud Tasks will retry the task according to the [RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig "Google::Cloud::Tasks::V2beta3::RetryConfig \(class\)").

Note that when the request is cancelled, Cloud Tasks will stop listening for the response, but whether the worker stops processing depends on the worker. For example, if the worker is stuck, it may not react to cancelled requests.

The default and maximum values depend on the type of request:

    * For [HTTP tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-HttpRequest "Google::Cloud::Tasks::V2beta3::HttpRequest \(class\)"), the default is 10 minutes. The deadline must be in the interval [15 seconds, 30 minutes].

    * For [App Engine tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineHttpRequest "Google::Cloud::Tasks::V2beta3::AppEngineHttpRequest \(class\)"), 0 indicates that the request has the default deadline. The default deadline depends on the [scaling type](https://cloud.google.com/appengine/docs/standard/go/how-instances-are-managed#instance_scaling) of the service: 10 minutes for standard apps with automatic scaling, 24 hours for standard apps with manual and basic scaling, and 60 minutes for flex apps. If the request deadline is set, it must be in the interval [15 seconds, 24 hours 15 seconds]. Regardless of the task's `dispatch_deadline`, the app handler will not run for longer than than the service's timeout. We recommend setting the `dispatch_deadline` to at most a few seconds more than the app handler's timeout. For more information see [Timeouts](https://cloud.google.com/tasks/docs/creating-appengine-handlers#timeouts).

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `dispatch_deadline` will be truncated to the nearest millisecond. The deadline is an approximate deadline. 




### #dispatch_deadline=
    
    
    def dispatch_deadline=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — The deadline for requests sent to the worker. If the worker does not respond by this deadline then the request is cancelled and the attempt is marked as a `DEADLINE_EXCEEDED` failure. Cloud Tasks will retry the task according to the [RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig "Google::Cloud::Tasks::V2beta3::RetryConfig \(class\)").

Note that when the request is cancelled, Cloud Tasks will stop listening for the response, but whether the worker stops processing depends on the worker. For example, if the worker is stuck, it may not react to cancelled requests.

The default and maximum values depend on the type of request:

    * For [HTTP tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-HttpRequest "Google::Cloud::Tasks::V2beta3::HttpRequest \(class\)"), the default is 10 minutes. The deadline must be in the interval [15 seconds, 30 minutes].

    * For [App Engine tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineHttpRequest "Google::Cloud::Tasks::V2beta3::AppEngineHttpRequest \(class\)"), 0 indicates that the request has the default deadline. The default deadline depends on the [scaling type](https://cloud.google.com/appengine/docs/standard/go/how-instances-are-managed#instance_scaling) of the service: 10 minutes for standard apps with automatic scaling, 24 hours for standard apps with manual and basic scaling, and 60 minutes for flex apps. If the request deadline is set, it must be in the interval [15 seconds, 24 hours 15 seconds]. Regardless of the task's `dispatch_deadline`, the app handler will not run for longer than than the service's timeout. We recommend setting the `dispatch_deadline` to at most a few seconds more than the app handler's timeout. For more information see [Timeouts](https://cloud.google.com/tasks/docs/creating-appengine-handlers#timeouts).

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `dispatch_deadline` will be truncated to the nearest millisecond. The deadline is an approximate deadline. 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — The deadline for requests sent to the worker. If the worker does not respond by this deadline then the request is cancelled and the attempt is marked as a `DEADLINE_EXCEEDED` failure. Cloud Tasks will retry the task according to the [RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig "Google::Cloud::Tasks::V2beta3::RetryConfig \(class\)").

Note that when the request is cancelled, Cloud Tasks will stop listening for the response, but whether the worker stops processing depends on the worker. For example, if the worker is stuck, it may not react to cancelled requests.

The default and maximum values depend on the type of request:

    * For [HTTP tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-HttpRequest "Google::Cloud::Tasks::V2beta3::HttpRequest \(class\)"), the default is 10 minutes. The deadline must be in the interval [15 seconds, 30 minutes].

    * For [App Engine tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-AppEngineHttpRequest "Google::Cloud::Tasks::V2beta3::AppEngineHttpRequest \(class\)"), 0 indicates that the request has the default deadline. The default deadline depends on the [scaling type](https://cloud.google.com/appengine/docs/standard/go/how-instances-are-managed#instance_scaling) of the service: 10 minutes for standard apps with automatic scaling, 24 hours for standard apps with manual and basic scaling, and 60 minutes for flex apps. If the request deadline is set, it must be in the interval [15 seconds, 24 hours 15 seconds]. Regardless of the task's `dispatch_deadline`, the app handler will not run for longer than than the service's timeout. We recommend setting the `dispatch_deadline` to at most a few seconds more than the app handler's timeout. For more information see [Timeouts](https://cloud.google.com/tasks/docs/creating-appengine-handlers#timeouts).

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `dispatch_deadline` will be truncated to the nearest millisecond. The deadline is an approximate deadline. 




### #first_attempt
    
    
    def first_attempt() -> ::Google::Cloud::Tasks::V2beta3::Attempt

**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Attempt](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt)) — Output only. The status of the task's first attempt.

Only [dispatch_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt#Google__Cloud__Tasks__V2beta3__Attempt_dispatch_time_instance_ "Google::Cloud::Tasks::V2beta3::Attempt#dispatch_time \(method\)") will be set. The other [Attempt](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt "Google::Cloud::Tasks::V2beta3::Attempt \(class\)") information is not retained by Cloud Tasks. 




### #first_attempt=
    
    
    def first_attempt=(value) -> ::Google::Cloud::Tasks::V2beta3::Attempt

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta3::Attempt](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt)) — Output only. The status of the task's first attempt.

Only [dispatch_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt#Google__Cloud__Tasks__V2beta3__Attempt_dispatch_time_instance_ "Google::Cloud::Tasks::V2beta3::Attempt#dispatch_time \(method\)") will be set. The other [Attempt](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt "Google::Cloud::Tasks::V2beta3::Attempt \(class\)") information is not retained by Cloud Tasks. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Attempt](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt)) — Output only. The status of the task's first attempt.

Only [dispatch_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt#Google__Cloud__Tasks__V2beta3__Attempt_dispatch_time_instance_ "Google::Cloud::Tasks::V2beta3::Attempt#dispatch_time \(method\)") will be set. The other [Attempt](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt "Google::Cloud::Tasks::V2beta3::Attempt \(class\)") information is not retained by Cloud Tasks. 




### #http_request
    
    
    def http_request() -> ::Google::Cloud::Tasks::V2beta3::HttpRequest

**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-HttpRequest)) — HTTP request that is sent to the task's target.

An HTTP task is a task that has [HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-HttpRequest "Google::Cloud::Tasks::V2beta3::HttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `http_request`, `app_engine_http_request`, `pull_message`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #http_request=
    
    
    def http_request=(value) -> ::Google::Cloud::Tasks::V2beta3::HttpRequest

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta3::HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-HttpRequest)) — HTTP request that is sent to the task's target.

An HTTP task is a task that has [HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-HttpRequest "Google::Cloud::Tasks::V2beta3::HttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `http_request`, `app_engine_http_request`, `pull_message`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-HttpRequest)) — HTTP request that is sent to the task's target.

An HTTP task is a task that has [HttpRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-HttpRequest "Google::Cloud::Tasks::V2beta3::HttpRequest \(class\)") set.

Note: The following fields are mutually exclusive: `http_request`, `app_engine_http_request`, `pull_message`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #last_attempt
    
    
    def last_attempt() -> ::Google::Cloud::Tasks::V2beta3::Attempt

**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Attempt](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt)) — Output only. The status of the task's last attempt. 



### #last_attempt=
    
    
    def last_attempt=(value) -> ::Google::Cloud::Tasks::V2beta3::Attempt

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta3::Attempt](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt)) — Output only. The status of the task's last attempt. 



**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Attempt](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Attempt)) — Output only. The status of the task's last attempt. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — 

Optionally caller-specified in [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#create_task \(method\)").

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

Optionally caller-specified in [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#create_task \(method\)").

The task name.

The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`

    * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling [ListLocations][google.cloud.location.Locations.ListLocations]. For more information, see https://cloud.google.com/about/locations/.
    * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.
    * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.



**Returns**

  * (::String) — 

Optionally caller-specified in [CreateTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_create_task_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#create_task \(method\)").

The task name.

The task name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID/tasks/TASK_ID`

    * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `LOCATION_ID` is the canonical ID for the task's location. The list of available locations can be obtained by calling [ListLocations][google.cloud.location.Locations.ListLocations]. For more information, see https://cloud.google.com/about/locations/.
    * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.
    * `TASK_ID` can contain only letters ([A-Za-z]), numbers ([0-9]), hyphens (-), or underscores (_). The maximum length is 500 characters.



### #pull_message
    
    
    def pull_message() -> ::Google::Cloud::Tasks::V2beta3::PullMessage

**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::PullMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-PullMessage)) — Pull Message contained in a task in a [PULL](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue#Google__Cloud__Tasks__V2beta3__Queue_type_instance_ "Google::Cloud::Tasks::V2beta3::Queue#type \(method\)") queue type. This payload type cannot be explicitly set through Cloud Tasks API. Its purpose, currently is to provide backward compatibility with App Engine Task Queue [pull](https://cloud.google.com/appengine/docs/standard/java/taskqueue/pull/) queues to provide a way to inspect contents of pull tasks through the [CloudTasks.GetTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_get_task_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#get_task \(method\)").

Note: The following fields are mutually exclusive: `pull_message`, `app_engine_http_request`, `http_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #pull_message=
    
    
    def pull_message=(value) -> ::Google::Cloud::Tasks::V2beta3::PullMessage

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta3::PullMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-PullMessage)) — Pull Message contained in a task in a [PULL](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue#Google__Cloud__Tasks__V2beta3__Queue_type_instance_ "Google::Cloud::Tasks::V2beta3::Queue#type \(method\)") queue type. This payload type cannot be explicitly set through Cloud Tasks API. Its purpose, currently is to provide backward compatibility with App Engine Task Queue [pull](https://cloud.google.com/appengine/docs/standard/java/taskqueue/pull/) queues to provide a way to inspect contents of pull tasks through the [CloudTasks.GetTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_get_task_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#get_task \(method\)").

Note: The following fields are mutually exclusive: `pull_message`, `app_engine_http_request`, `http_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::PullMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-PullMessage)) — Pull Message contained in a task in a [PULL](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Queue#Google__Cloud__Tasks__V2beta3__Queue_type_instance_ "Google::Cloud::Tasks::V2beta3::Queue#type \(method\)") queue type. This payload type cannot be explicitly set through Cloud Tasks API. Its purpose, currently is to provide backward compatibility with App Engine Task Queue [pull](https://cloud.google.com/appengine/docs/standard/java/taskqueue/pull/) queues to provide a way to inspect contents of pull tasks through the [CloudTasks.GetTask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-CloudTasks-Client#Google__Cloud__Tasks__V2beta3__CloudTasks__Client_get_task_instance_ "Google::Cloud::Tasks::V2beta3::CloudTasks::Client#get_task \(method\)").

Note: The following fields are mutually exclusive: `pull_message`, `app_engine_http_request`, `http_request`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #response_count
    
    
    def response_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. The number of attempts which have received a response. 



### #response_count=
    
    
    def response_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. The number of attempts which have received a response. 



**Returns**

  * (::Integer) — Output only. The number of attempts which have received a response. 



### #retry_config
    
    
    def retry_config() -> ::Google::Cloud::Tasks::V2beta3::RetryConfig

**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig)) — Optional. Specifies the task-level retry config.

If present, this overrides the queue-level retry config for this task. 




### #retry_config=
    
    
    def retry_config=(value) -> ::Google::Cloud::Tasks::V2beta3::RetryConfig

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta3::RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig)) — Optional. Specifies the task-level retry config.

If present, this overrides the queue-level retry config for this task. 




**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig)) — Optional. Specifies the task-level retry config.

If present, this overrides the queue-level retry config for this task. 




### #schedule_time
    
    
    def schedule_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Timestamp)) — The time when the task is scheduled to be attempted.

For App Engine queues, this is when the task will be attempted or retried.

`schedule_time` will be truncated to the nearest microsecond. 




### #schedule_time=
    
    
    def schedule_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Timestamp)) — The time when the task is scheduled to be attempted.

For App Engine queues, this is when the task will be attempted or retried.

`schedule_time` will be truncated to the nearest microsecond. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Timestamp)) — The time when the task is scheduled to be attempted.

For App Engine queues, this is when the task will be attempted or retried.

`schedule_time` will be truncated to the nearest microsecond. 




### #view
    
    
    def view() -> ::Google::Cloud::Tasks::V2beta3::Task::View

**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Task::View](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View)) — Output only. The view specifies which subset of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task "Google::Cloud::Tasks::V2beta3::Task \(class\)") has been returned. 



### #view=
    
    
    def view=(value) -> ::Google::Cloud::Tasks::V2beta3::Task::View

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2beta3::Task::View](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View)) — Output only. The view specifies which subset of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task "Google::Cloud::Tasks::V2beta3::Task \(class\)") has been returned. 



**Returns**

  * ([::Google::Cloud::Tasks::V2beta3::Task::View](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task-View)) — Output only. The view specifies which subset of the [Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task "Google::Cloud::Tasks::V2beta3::Task \(class\)") has been returned. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
