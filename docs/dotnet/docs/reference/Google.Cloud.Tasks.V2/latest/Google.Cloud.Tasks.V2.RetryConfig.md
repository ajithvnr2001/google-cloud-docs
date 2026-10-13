---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RetryConfig
title: Google Cloud Tasks v2 API - Class RetryConfig (3.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:38.892834+00:00
---

# Google Cloud Tasks v2 API - Class RetryConfig (3.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RetryConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2 API - Class RetryConfig (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class RetryConfig : IMessage<RetryConfig>, IEquatable<RetryConfig>, IDeepCloneable<RetryConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Tasks v2 API class RetryConfig.

Retry config.

These settings determine when a failed task attempt is retried.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RetryConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RetryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RetryConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RetryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RetryConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RetryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RetryConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Tasks.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2)

## Assembly

Google.Cloud.Tasks.V2.dll

## Constructors 

### RetryConfig()
    
    
    public RetryConfig()

### RetryConfig(RetryConfig)
    
    
    public RetryConfig(RetryConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RetryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.RetryConfig)`  
  
  
## Properties 

### MaxAttempts
    
    
    public int MaxAttempts { get; set; }

Number of attempts per task, including the first attempt. (If the first attempt fails, there will be `max_attempts - 1` retries.)

Must be greater than or equal to -1, which indicates unlimited attempts.

Cloud Tasks stops retrying only when `max_attempts` and `max_retry_duration` are both satisfied, or when the task is successfully executed. When the task has been attempted `max_attempts` times and when the `max_retry_duration` time has passed, no further attempts are made, and the task is deleted. If `max_attempts` is set to -1 and `max_retry_duration` is set to 0, the task is retried until the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit is reached.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_retry_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaxBackoff
    
    
    public Duration MaxBackoff { get; set; }

A task will be [scheduled][google.cloud.tasks.v2.Task.schedule_time] for retry between [min_backoff][google.cloud.tasks.v2.RetryConfig.min_backoff] and [max_backoff][google.cloud.tasks.v2.RetryConfig.max_backoff] duration after it fails, if the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig] specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### MaxDoublings
    
    
    public int MaxDoublings { get; set; }

The time between retries will double `max_doublings` times.

A task's retry interval starts at [min_backoff][google.cloud.tasks.v2.RetryConfig.min_backoff], then doubles `max_doublings` times, then increases linearly, and finally retries at intervals of [max_backoff][google.cloud.tasks.v2.RetryConfig.max_backoff] up to [max_attempts][google.cloud.tasks.v2.RetryConfig.max_attempts] times.

For example, if [min_backoff][google.cloud.tasks.v2.RetryConfig.min_backoff] is 10s, [max_backoff][google.cloud.tasks.v2.RetryConfig.max_backoff] is 300s, and `max_doublings` is 3, then the a task will first be retried in 10s. The retry interval will double three times, and then increase linearly by 2^3 * 10s. Finally, the task will retry at intervals of [max_backoff][google.cloud.tasks.v2.RetryConfig.max_backoff] until the task has been attempted [max_attempts][google.cloud.tasks.v2.RetryConfig.max_attempts] times. Thus, the requests will retry at 10s, 20s, 40s, 80s, 160s, 240s, 300s, 300s, ....

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [max_doublings in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### MaxRetryDuration
    
    
    public Duration MaxRetryDuration { get; set; }

If positive, `max_retry_duration` specifies the time limit for retrying a failed task, measured from when the task was first attempted. Once `max_retry_duration` time has passed _and_ the task has been attempted [max_attempts][google.cloud.tasks.v2.RetryConfig.max_attempts] times, no further attempts are made and the task is deleted.

A zero (0) indicates an unlimited duration, up to the [maximum task retention](https://docs.cloud.google.com/tasks/docs/quotas#limits) limit.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For the maximum possible value or the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `max_retry_duration` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [task_age_limit in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### MinBackoff
    
    
    public Duration MinBackoff { get; set; }

A task will be [scheduled][google.cloud.tasks.v2.Task.schedule_time] for retry between [min_backoff][google.cloud.tasks.v2.RetryConfig.min_backoff] and [max_backoff][google.cloud.tasks.v2.RetryConfig.max_backoff] duration after it fails, if the queue's [RetryConfig][google.cloud.tasks.v2.RetryConfig] specifies that the task should be retried.

The value must be given as a string that indicates the length of time (in seconds) followed by `s` (for "seconds"). For more information on the format, see the documentation for [Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration). `min_backoff` will be truncated to the nearest second.

If unspecified when the queue is created, Cloud Tasks will pick the default.

This field has the same meaning as [min_backoff_seconds in queue.yaml/xml](https://cloud.google.com/appengine/docs/standard/python/config/queueref#retry_parameters).

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
