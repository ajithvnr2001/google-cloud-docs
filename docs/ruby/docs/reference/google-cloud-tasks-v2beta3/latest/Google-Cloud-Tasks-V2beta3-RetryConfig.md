---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig/
title: Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::RetryConfig (v0.20.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:13:07.126251+00:00
---

# Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::RetryConfig (v0.20.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Tasks V2beta3 API - Class Google::Cloud::Tasks::V2beta3::RetryConfig (v0.20.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.2 (latest)  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.0  0.13.1  0.12.3  0.11.0  0.10.2  0.9.0  0.8.0  0.7.0  0.6.6 

Reference documentation and code samples for the Cloud Tasks V2beta3 API class Google::Cloud::Tasks::V2beta3::RetryConfig.

Retry config.

These settings determine when a failed task attempt is retried.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #max_attempts
    
    
    def max_attempts() -> ::Integer

**Returns**

  * (::Integer) — Number of attempts per task, including the first attempt. (If the first attempt fails, there will be `max_attempts - 1` retries.)

Must be greater than or equal to -1, which indicates unlimited attempts.

Cloud Tasks stops retrying only when `max_attempts` and `max_retry_duration` are both satisfied, or when the task is successfully executed. When the task has been attempted `max_attempts` times and when the `max_retry_duration` time has passed, no further attempts are made, and the task is deleted. If `max_attempts` is set to -1 and `max_retry_duration` is set to 0, the task is retried until the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit is reached.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_retry_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




### #max_attempts=
    
    
    def max_attempts=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of attempts per task, including the first attempt. (If the first attempt fails, there will be `max_attempts - 1` retries.)

Must be greater than or equal to -1, which indicates unlimited attempts.

Cloud Tasks stops retrying only when `max_attempts` and `max_retry_duration` are both satisfied, or when the task is successfully executed. When the task has been attempted `max_attempts` times and when the `max_retry_duration` time has passed, no further attempts are made, and the task is deleted. If `max_attempts` is set to -1 and `max_retry_duration` is set to 0, the task is retried until the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit is reached.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_retry_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




**Returns**

  * (::Integer) — Number of attempts per task, including the first attempt. (If the first attempt fails, there will be `max_attempts - 1` retries.)

Must be greater than or equal to -1, which indicates unlimited attempts.

Cloud Tasks stops retrying only when `max_attempts` and `max_retry_duration` are both satisfied, or when the task is successfully executed. When the task has been attempted `max_attempts` times and when the `max_retry_duration` time has passed, no further attempts are made, and the task is deleted. If `max_attempts` is set to -1 and `max_retry_duration` is set to 0, the task is retried until the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit is reached.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_retry_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




### #max_backoff
    
    
    def max_backoff() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — A task will be [scheduled](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_schedule_time_instance_ "Google::Cloud::Tasks::V2beta3::Task#schedule_time \(method\)") for retry between [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)") and [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") duration after it fails, if the queue's [RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig "Google::Cloud::Tasks::V2beta3::RetryConfig \(class\)") specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




### #max_backoff=
    
    
    def max_backoff=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — A task will be [scheduled](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_schedule_time_instance_ "Google::Cloud::Tasks::V2beta3::Task#schedule_time \(method\)") for retry between [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)") and [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") duration after it fails, if the queue's [RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig "Google::Cloud::Tasks::V2beta3::RetryConfig \(class\)") specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — A task will be [scheduled](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_schedule_time_instance_ "Google::Cloud::Tasks::V2beta3::Task#schedule_time \(method\)") for retry between [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)") and [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") duration after it fails, if the queue's [RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig "Google::Cloud::Tasks::V2beta3::RetryConfig \(class\)") specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




### #max_doublings
    
    
    def max_doublings() -> ::Integer

**Returns**

  * (::Integer) — The time between retries will double `max_doublings` times.

A task's retry interval starts at [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)"), then doubles `max_doublings` times, then increases linearly, and finally retries at intervals of [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") up to [max_attempts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_attempts_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_attempts \(method\)") times.

For example, if [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)") is 10s, [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") is 300s, and `max_doublings` is 3, then the a task will first be retried in 10s. The retry interval will double three times, and then increase linearly by 2^3 * 10s. Finally, the task will retry at intervals of [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") until the task has been attempted [max_attempts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_attempts_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_attempts \(method\)") times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, ....

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_doublings in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




### #max_doublings=
    
    
    def max_doublings=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The time between retries will double `max_doublings` times.

A task's retry interval starts at [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)"), then doubles `max_doublings` times, then increases linearly, and finally retries at intervals of [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") up to [max_attempts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_attempts_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_attempts \(method\)") times.

For example, if [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)") is 10s, [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") is 300s, and `max_doublings` is 3, then the a task will first be retried in 10s. The retry interval will double three times, and then increase linearly by 2^3 * 10s. Finally, the task will retry at intervals of [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") until the task has been attempted [max_attempts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_attempts_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_attempts \(method\)") times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, ....

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_doublings in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




**Returns**

  * (::Integer) — The time between retries will double `max_doublings` times.

A task's retry interval starts at [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)"), then doubles `max_doublings` times, then increases linearly, and finally retries at intervals of [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") up to [max_attempts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_attempts_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_attempts \(method\)") times.

For example, if [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)") is 10s, [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") is 300s, and `max_doublings` is 3, then the a task will first be retried in 10s. The retry interval will double three times, and then increase linearly by 2^3 * 10s. Finally, the task will retry at intervals of [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") until the task has been attempted [max_attempts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_attempts_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_attempts \(method\)") times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, ....

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_doublings in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




### #max_retry_duration
    
    
    def max_retry_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted [max_attempts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_attempts_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_attempts \(method\)") times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




### #max_retry_duration=
    
    
    def max_retry_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted [max_attempts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_attempts_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_attempts \(method\)") times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted [max_attempts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_attempts_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_attempts \(method\)") times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




### #min_backoff
    
    
    def min_backoff() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — A task will be [scheduled](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_schedule_time_instance_ "Google::Cloud::Tasks::V2beta3::Task#schedule_time \(method\)") for retry between [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)") and [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") duration after it fails, if the queue's [RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig "Google::Cloud::Tasks::V2beta3::RetryConfig \(class\)") specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




### #min_backoff=
    
    
    def min_backoff=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — A task will be [scheduled](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_schedule_time_instance_ "Google::Cloud::Tasks::V2beta3::Task#schedule_time \(method\)") for retry between [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)") and [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") duration after it fails, if the queue's [RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig "Google::Cloud::Tasks::V2beta3::RetryConfig \(class\)") specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Protobuf-Duration)) — A task will be [scheduled](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-Task#Google__Cloud__Tasks__V2beta3__Task_schedule_time_instance_ "Google::Cloud::Tasks::V2beta3::Task#schedule_time \(method\)") for retry between [min_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_min_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#min_backoff \(method\)") and [max_backoff](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig#Google__Cloud__Tasks__V2beta3__RetryConfig_max_backoff_instance_ "Google::Cloud::Tasks::V2beta3::RetryConfig#max_backoff \(method\)") duration after it fails, if the queue's [RetryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-tasks-v2beta3/latest/Google-Cloud-Tasks-V2beta3-RetryConfig "Google::Cloud::Tasks::V2beta3::RetryConfig \(class\)") specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
