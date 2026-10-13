---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue/
title: Cloud Tasks V2 API - Class Google::Cloud::Tasks::V2::Queue (v1.7.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:54.149883+00:00
---

# Cloud Tasks V2 API - Class Google::Cloud::Tasks::V2::Queue (v1.7.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2 API - Class Google::Cloud::Tasks::V2::Queue (v1.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.0 (latest)  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.11.0  0.10.2  0.9.0  0.8.2  0.7.0  0.6.0  0.5.0  0.4.6 

Reference documentation and code samples for the Cloud Tasks V2 API class Google::Cloud::Tasks::V2::Queue.

A queue is a container of related tasks. Queues are configured to manage how those tasks are dispatched. Configurable properties include rate limits, retry options, queue types, and others.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #app_engine_routing_override
    
    
    def app_engine_routing_override() -> ::Google::Cloud::Tasks::V2::AppEngineRouting

**Returns**

  * ([::Google::Cloud::Tasks::V2::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineRouting)) — Overrides for [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing]. These settings apply only to [App Engine tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest "Google::Cloud::Tasks::V2::AppEngineHttpRequest \(class\)") in this queue. [Http tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpRequest "Google::Cloud::Tasks::V2::HttpRequest \(class\)") are not affected.

If set, `app_engine_routing_override` is used for all [App Engine tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest "Google::Cloud::Tasks::V2::AppEngineHttpRequest \(class\)") in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing]. 




### #app_engine_routing_override=
    
    
    def app_engine_routing_override=(value) -> ::Google::Cloud::Tasks::V2::AppEngineRouting

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineRouting)) — Overrides for [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing]. These settings apply only to [App Engine tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest "Google::Cloud::Tasks::V2::AppEngineHttpRequest \(class\)") in this queue. [Http tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpRequest "Google::Cloud::Tasks::V2::HttpRequest \(class\)") are not affected.

If set, `app_engine_routing_override` is used for all [App Engine tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest "Google::Cloud::Tasks::V2::AppEngineHttpRequest \(class\)") in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing]. 




**Returns**

  * ([::Google::Cloud::Tasks::V2::AppEngineRouting](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineRouting)) — Overrides for [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing]. These settings apply only to [App Engine tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest "Google::Cloud::Tasks::V2::AppEngineHttpRequest \(class\)") in this queue. [Http tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpRequest "Google::Cloud::Tasks::V2::HttpRequest \(class\)") are not affected.

If set, `app_engine_routing_override` is used for all [App Engine tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-AppEngineHttpRequest "Google::Cloud::Tasks::V2::AppEngineHttpRequest \(class\)") in the queue, no matter what the setting is for the [task-level app_engine_routing][google.cloud.tasks.v2.AppEngineHttpRequest.app_engine_routing]. 




### #http_target
    
    
    def http_target() -> ::Google::Cloud::Tasks::V2::HttpTarget

**Returns**

  * ([::Google::Cloud::Tasks::V2::HttpTarget](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpTarget)) — Modifies HTTP target for HTTP tasks. 



### #http_target=
    
    
    def http_target=(value) -> ::Google::Cloud::Tasks::V2::HttpTarget

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2::HttpTarget](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpTarget)) — Modifies HTTP target for HTTP tasks. 



**Returns**

  * ([::Google::Cloud::Tasks::V2::HttpTarget](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-HttpTarget)) — Modifies HTTP target for HTTP tasks. 



### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — 

Caller-specified and required in [CreateQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_queue \(method\)"), after which it becomes output only.

The queue name.

The queue name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

    * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `LOCATION_ID` is the canonical ID for the queue's location. The list of available locations can be obtained by calling [ListLocations][google.cloud.location.Locations.ListLocations]. For more information, see https://cloud.google.com/about/locations/.
    * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.



### #name=
    
    
    def name=(value) -> ::String

**Parameter**

  * **value** (::String) — 

Caller-specified and required in [CreateQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_queue \(method\)"), after which it becomes output only.

The queue name.

The queue name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

    * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `LOCATION_ID` is the canonical ID for the queue's location. The list of available locations can be obtained by calling [ListLocations][google.cloud.location.Locations.ListLocations]. For more information, see https://cloud.google.com/about/locations/.
    * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.



**Returns**

  * (::String) — 

Caller-specified and required in [CreateQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_create_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#create_queue \(method\)"), after which it becomes output only.

The queue name.

The queue name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

    * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
    * `LOCATION_ID` is the canonical ID for the queue's location. The list of available locations can be obtained by calling [ListLocations][google.cloud.location.Locations.ListLocations]. For more information, see https://cloud.google.com/about/locations/.
    * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.



### #purge_time
    
    
    def purge_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Protobuf-Timestamp)) — Output only. The last time this queue was purged.

All tasks that were [created](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Task#Google__Cloud__Tasks__V2__Task_create_time_instance_ "Google::Cloud::Tasks::V2::Task#create_time \(method\)") before this time were purged.

A queue can be purged using [PurgeQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_purge_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#purge_queue \(method\)"), the [App Engine Task Queue SDK, or the Cloud Console](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue).

Purge time will be truncated to the nearest microsecond. Purge time will be unset if the queue has never been purged. 




### #purge_time=
    
    
    def purge_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Protobuf-Timestamp)) — Output only. The last time this queue was purged.

All tasks that were [created](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Task#Google__Cloud__Tasks__V2__Task_create_time_instance_ "Google::Cloud::Tasks::V2::Task#create_time \(method\)") before this time were purged.

A queue can be purged using [PurgeQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_purge_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#purge_queue \(method\)"), the [App Engine Task Queue SDK, or the Cloud Console](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue).

Purge time will be truncated to the nearest microsecond. Purge time will be unset if the queue has never been purged. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Protobuf-Timestamp)) — Output only. The last time this queue was purged.

All tasks that were [created](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Task#Google__Cloud__Tasks__V2__Task_create_time_instance_ "Google::Cloud::Tasks::V2::Task#create_time \(method\)") before this time were purged.

A queue can be purged using [PurgeQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_purge_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#purge_queue \(method\)"), the [App Engine Task Queue SDK, or the Cloud Console](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue).

Purge time will be truncated to the nearest microsecond. Purge time will be unset if the queue has never been purged. 




### #rate_limits
    
    
    def rate_limits() -> ::Google::Cloud::Tasks::V2::RateLimits

**Returns**

  * ([::Google::Cloud::Tasks::V2::RateLimits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-RateLimits)) — 

Rate limits for task dispatches.

[rate_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_rate_limits_instance_ "Google::Cloud::Tasks::V2::Queue#rate_limits \(method\)") and [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)") are related because they both control task attempts. However they control task attempts in different ways:

    * [rate_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_rate_limits_instance_ "Google::Cloud::Tasks::V2::Queue#rate_limits \(method\)") controls the total rate of dispatches from a queue (i.e. all traffic dispatched from the queue, regardless of whether the dispatch is from a first attempt or a retry).
    * [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)") controls what happens to a particular task after its first attempt fails. That is, [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)") controls task retries (the second attempt, third attempt, etc).

The queue's actual dispatch rate is the result of:

    * Number of tasks in the queue
    * User-specified throttling: [rate_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_rate_limits_instance_ "Google::Cloud::Tasks::V2::Queue#rate_limits \(method\)"), [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)"), and the [queue's state][google.cloud.tasks.v2.Queue.state].
    * System throttling due to `429` (Too Many Requests) or `503` (Service Unavailable) responses from the worker, high error rates, or to smooth sudden large traffic spikes.



### #rate_limits=
    
    
    def rate_limits=(value) -> ::Google::Cloud::Tasks::V2::RateLimits

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2::RateLimits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-RateLimits)) — 

Rate limits for task dispatches.

[rate_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_rate_limits_instance_ "Google::Cloud::Tasks::V2::Queue#rate_limits \(method\)") and [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)") are related because they both control task attempts. However they control task attempts in different ways:

    * [rate_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_rate_limits_instance_ "Google::Cloud::Tasks::V2::Queue#rate_limits \(method\)") controls the total rate of dispatches from a queue (i.e. all traffic dispatched from the queue, regardless of whether the dispatch is from a first attempt or a retry).
    * [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)") controls what happens to a particular task after its first attempt fails. That is, [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)") controls task retries (the second attempt, third attempt, etc).

The queue's actual dispatch rate is the result of:

    * Number of tasks in the queue
    * User-specified throttling: [rate_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_rate_limits_instance_ "Google::Cloud::Tasks::V2::Queue#rate_limits \(method\)"), [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)"), and the [queue's state][google.cloud.tasks.v2.Queue.state].
    * System throttling due to `429` (Too Many Requests) or `503` (Service Unavailable) responses from the worker, high error rates, or to smooth sudden large traffic spikes.



**Returns**

  * ([::Google::Cloud::Tasks::V2::RateLimits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-RateLimits)) — 

Rate limits for task dispatches.

[rate_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_rate_limits_instance_ "Google::Cloud::Tasks::V2::Queue#rate_limits \(method\)") and [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)") are related because they both control task attempts. However they control task attempts in different ways:

    * [rate_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_rate_limits_instance_ "Google::Cloud::Tasks::V2::Queue#rate_limits \(method\)") controls the total rate of dispatches from a queue (i.e. all traffic dispatched from the queue, regardless of whether the dispatch is from a first attempt or a retry).
    * [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)") controls what happens to a particular task after its first attempt fails. That is, [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)") controls task retries (the second attempt, third attempt, etc).

The queue's actual dispatch rate is the result of:

    * Number of tasks in the queue
    * User-specified throttling: [rate_limits](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_rate_limits_instance_ "Google::Cloud::Tasks::V2::Queue#rate_limits \(method\)"), [retry_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue#Google__Cloud__Tasks__V2__Queue_retry_config_instance_ "Google::Cloud::Tasks::V2::Queue#retry_config \(method\)"), and the [queue's state][google.cloud.tasks.v2.Queue.state].
    * System throttling due to `429` (Too Many Requests) or `503` (Service Unavailable) responses from the worker, high error rates, or to smooth sudden large traffic spikes.



### #retry_config
    
    
    def retry_config() -> ::Google::Cloud::Tasks::V2::RetryConfig

**Returns**

  * ([::Google::Cloud::Tasks::V2::RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-RetryConfig)) — 

Settings that determine the retry behavior.

    * For tasks created using Cloud Tasks: the queue-level retry settings apply to all tasks in the queue that were created using Cloud Tasks. Retry settings cannot be set on individual tasks.
    * For tasks created using the App Engine SDK: the queue-level retry settings apply to all tasks in the queue which do not have retry settings explicitly set on the task and were created by the App Engine SDK. See [App Engine documentation](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/retrying-tasks).



### #retry_config=
    
    
    def retry_config=(value) -> ::Google::Cloud::Tasks::V2::RetryConfig

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2::RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-RetryConfig)) — 

Settings that determine the retry behavior.

    * For tasks created using Cloud Tasks: the queue-level retry settings apply to all tasks in the queue that were created using Cloud Tasks. Retry settings cannot be set on individual tasks.
    * For tasks created using the App Engine SDK: the queue-level retry settings apply to all tasks in the queue which do not have retry settings explicitly set on the task and were created by the App Engine SDK. See [App Engine documentation](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/retrying-tasks).



**Returns**

  * ([::Google::Cloud::Tasks::V2::RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-RetryConfig)) — 

Settings that determine the retry behavior.

    * For tasks created using Cloud Tasks: the queue-level retry settings apply to all tasks in the queue that were created using Cloud Tasks. Retry settings cannot be set on individual tasks.
    * For tasks created using the App Engine SDK: the queue-level retry settings apply to all tasks in the queue which do not have retry settings explicitly set on the task and were created by the App Engine SDK. See [App Engine documentation](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/retrying-tasks).



### #stackdriver_logging_config
    
    
    def stackdriver_logging_config() -> ::Google::Cloud::Tasks::V2::StackdriverLoggingConfig

**Returns**

  * ([::Google::Cloud::Tasks::V2::StackdriverLoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-StackdriverLoggingConfig)) — Configuration options for writing logs to [Stackdriver Logging](https://cloud.google.com/logging/docs/). If this field is unset, then no logs are written. 



### #stackdriver_logging_config=
    
    
    def stackdriver_logging_config=(value) -> ::Google::Cloud::Tasks::V2::StackdriverLoggingConfig

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2::StackdriverLoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-StackdriverLoggingConfig)) — Configuration options for writing logs to [Stackdriver Logging](https://cloud.google.com/logging/docs/). If this field is unset, then no logs are written. 



**Returns**

  * ([::Google::Cloud::Tasks::V2::StackdriverLoggingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-StackdriverLoggingConfig)) — Configuration options for writing logs to [Stackdriver Logging](https://cloud.google.com/logging/docs/). If this field is unset, then no logs are written. 



### #state
    
    
    def state() -> ::Google::Cloud::Tasks::V2::Queue::State

**Returns**

  * ([::Google::Cloud::Tasks::V2::Queue::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue-State)) — Output only. The state of the queue.

`state` can only be changed by calling [PauseQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_pause_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#pause_queue \(method\)"), [ResumeQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_resume_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#resume_queue \(method\)"), or uploading [queue.yaml/xml](https://cloud.google.com/appengine/docs/python/config/queueref). [UpdateQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_update_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#update_queue \(method\)") cannot be used to change `state`. 




### #state=
    
    
    def state=(value) -> ::Google::Cloud::Tasks::V2::Queue::State

**Parameter**

  * **value** ([::Google::Cloud::Tasks::V2::Queue::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue-State)) — Output only. The state of the queue.

`state` can only be changed by calling [PauseQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_pause_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#pause_queue \(method\)"), [ResumeQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_resume_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#resume_queue \(method\)"), or uploading [queue.yaml/xml](https://cloud.google.com/appengine/docs/python/config/queueref). [UpdateQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_update_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#update_queue \(method\)") cannot be used to change `state`. 




**Returns**

  * ([::Google::Cloud::Tasks::V2::Queue::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-Queue-State)) — Output only. The state of the queue.

`state` can only be changed by calling [PauseQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_pause_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#pause_queue \(method\)"), [ResumeQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_resume_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#resume_queue \(method\)"), or uploading [queue.yaml/xml](https://cloud.google.com/appengine/docs/python/config/queueref). [UpdateQueue](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2/latest/Google-Cloud-Tasks-V2-CloudTasks-Client#Google__Cloud__Tasks__V2__CloudTasks__Client_update_queue_instance_ "Google::Cloud::Tasks::V2::CloudTasks::Client#update_queue \(method\)") cannot be used to change `state`. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
