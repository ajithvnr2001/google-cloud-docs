---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.QueueOrBuilder
title: Interface QueueOrBuilder (2.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:06.171801+00:00
---

# Interface QueueOrBuilder (2.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.QueueOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface QueueOrBuilder (2.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.99.0 (latest)  2.95.0  2.94.0  2.93.0  2.91.0  2.88.0  2.87.0  2.85.0  2.83.0  2.82.0  2.80.0  2.78.0  2.76.0  2.75.0  2.74.0  2.73.0  2.72.0  2.70.0  2.68.0  2.67.0  2.64.0  2.63.0  2.62.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.12  2.2.0  2.1.11 
    
    
    public interface QueueOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAppEngineHttpTarget()
    
    
    public abstract AppEngineHttpTarget getAppEngineHttpTarget()

App Engine HTTP target.

An App Engine queue is a queue that has an AppEngineHttpTarget.

`.google.cloud.tasks.v2beta2.AppEngineHttpTarget app_engine_http_target = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AppEngineHttpTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.AppEngineHttpTarget)` | The appEngineHttpTarget.  
  
### getAppEngineHttpTargetOrBuilder()
    
    
    public abstract AppEngineHttpTargetOrBuilder getAppEngineHttpTargetOrBuilder()

App Engine HTTP target.

An App Engine queue is a queue that has an AppEngineHttpTarget.

`.google.cloud.tasks.v2beta2.AppEngineHttpTarget app_engine_http_target = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AppEngineHttpTargetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.AppEngineHttpTargetOrBuilder)` |   
  
### getHttpTarget()
    
    
    public abstract HttpTarget getHttpTarget()

An http_target is used to override the target values for HTTP tasks.

`.google.cloud.tasks.v2beta2.HttpTarget http_target = 17;`

**Returns**  
---  
**Type** | **Description**  
`[HttpTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.HttpTarget)` | The httpTarget.  
  
### getHttpTargetOrBuilder()
    
    
    public abstract HttpTargetOrBuilder getHttpTargetOrBuilder()

An http_target is used to override the target values for HTTP tasks.

`.google.cloud.tasks.v2beta2.HttpTarget http_target = 17;`

**Returns**  
---  
**Type** | **Description**  
`[HttpTargetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.HttpTargetOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Caller-specified and required in CreateQueue, after which it becomes output only.

The queue name.

The queue name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

  * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `LOCATION_ID` is the canonical ID for the queue's location. The list of available locations can be obtained by calling ListLocations. For more information, see <https://cloud.google.com/about/locations/>.
  * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.



`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Caller-specified and required in CreateQueue, after which it becomes output only.

The queue name.

The queue name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

  * `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see [Identifying projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects)
  * `LOCATION_ID` is the canonical ID for the queue's location. The list of available locations can be obtained by calling ListLocations. For more information, see <https://cloud.google.com/about/locations/>.
  * `QUEUE_ID` can contain letters ([A-Za-z]), numbers ([0-9]), or hyphens (-). The maximum length is 100 characters.



`string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPullTarget()
    
    
    public abstract PullTarget getPullTarget()

Pull target.

A pull queue is a queue that has a PullTarget.

`.google.cloud.tasks.v2beta2.PullTarget pull_target = 4;`

**Returns**  
---  
**Type** | **Description**  
`[PullTarget](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.PullTarget)` | The pullTarget.  
  
### getPullTargetOrBuilder()
    
    
    public abstract PullTargetOrBuilder getPullTargetOrBuilder()

Pull target.

A pull queue is a queue that has a PullTarget.

`.google.cloud.tasks.v2beta2.PullTarget pull_target = 4;`

**Returns**  
---  
**Type** | **Description**  
`[PullTargetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.PullTargetOrBuilder)` |   
  
### getPurgeTime()
    
    
    public abstract Timestamp getPurgeTime()

Output only. The last time this queue was purged.

All tasks that were created before this time were purged.

A queue can be purged using PurgeQueue, the [App Engine Task Queue SDK, or the Cloud Console](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue).

Purge time will be truncated to the nearest microsecond. Purge time will be unset if the queue has never been purged.

`.google.protobuf.Timestamp purge_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The purgeTime.  
  
### getPurgeTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getPurgeTimeOrBuilder()

Output only. The last time this queue was purged.

All tasks that were created before this time were purged.

A queue can be purged using PurgeQueue, the [App Engine Task Queue SDK, or the Cloud Console](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue).

Purge time will be truncated to the nearest microsecond. Purge time will be unset if the queue has never been purged.

`.google.protobuf.Timestamp purge_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getRateLimits()
    
    
    public abstract RateLimits getRateLimits()

Rate limits for task dispatches.

rate_limits and retry_config are related because they both control task attempts however they control how tasks are attempted in different ways:

  * rate_limits controls the total rate of dispatches from a queue (i.e. all traffic dispatched from the queue, regardless of whether the dispatch is from a first attempt or a retry).
  * retry_config controls what happens to particular a task after its first attempt fails. That is, retry_config controls task retries (the second attempt, third attempt, etc).



`.google.cloud.tasks.v2beta2.RateLimits rate_limits = 5;`

**Returns**  
---  
**Type** | **Description**  
`[RateLimits](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.RateLimits)` | The rateLimits.  
  
### getRateLimitsOrBuilder()
    
    
    public abstract RateLimitsOrBuilder getRateLimitsOrBuilder()

Rate limits for task dispatches.

rate_limits and retry_config are related because they both control task attempts however they control how tasks are attempted in different ways:

  * rate_limits controls the total rate of dispatches from a queue (i.e. all traffic dispatched from the queue, regardless of whether the dispatch is from a first attempt or a retry).
  * retry_config controls what happens to particular a task after its first attempt fails. That is, retry_config controls task retries (the second attempt, third attempt, etc).



`.google.cloud.tasks.v2beta2.RateLimits rate_limits = 5;`

**Returns**  
---  
**Type** | **Description**  
`[RateLimitsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.RateLimitsOrBuilder)` |   
  
### getRetryConfig()
    
    
    public abstract RetryConfig getRetryConfig()

Settings that determine the retry behavior.

  * For tasks created using Cloud Tasks: the queue-level retry settings apply to all tasks in the queue that were created using Cloud Tasks. Retry settings cannot be set on individual tasks.
  * For tasks created using the App Engine SDK: the queue-level retry settings apply to all tasks in the queue which do not have retry settings explicitly set on the task and were created by the App Engine SDK. See [App Engine documentation](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/retrying-tasks).



`.google.cloud.tasks.v2beta2.RetryConfig retry_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[RetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.RetryConfig)` | The retryConfig.  
  
### getRetryConfigOrBuilder()
    
    
    public abstract RetryConfigOrBuilder getRetryConfigOrBuilder()

Settings that determine the retry behavior.

  * For tasks created using Cloud Tasks: the queue-level retry settings apply to all tasks in the queue that were created using Cloud Tasks. Retry settings cannot be set on individual tasks.
  * For tasks created using the App Engine SDK: the queue-level retry settings apply to all tasks in the queue which do not have retry settings explicitly set on the task and were created by the App Engine SDK. See [App Engine documentation](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/retrying-tasks).



`.google.cloud.tasks.v2beta2.RetryConfig retry_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[RetryConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.RetryConfigOrBuilder)` |   
  
### getState()
    
    
    public abstract Queue.State getState()

Output only. The state of the queue.

`state` can only be changed by called PauseQueue, ResumeQueue, or uploading [queue.yaml/xml](https://cloud.google.com/appengine/docs/python/config/queueref). UpdateQueue cannot be used to change `state`.

`.google.cloud.tasks.v2beta2.Queue.State state = 7;`

**Returns**  
---  
**Type** | **Description**  
`[Queue.State](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.Queue.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The state of the queue.

`state` can only be changed by called PauseQueue, ResumeQueue, or uploading [queue.yaml/xml](https://cloud.google.com/appengine/docs/python/config/queueref). UpdateQueue cannot be used to change `state`.

`.google.cloud.tasks.v2beta2.Queue.State state = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getStats()
    
    
    public abstract QueueStats getStats()

Output only. The realtime, informational statistics for a queue. In order to receive the statistics the caller should include this field in the FieldMask.

` .google.cloud.tasks.v2beta2.QueueStats stats = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[QueueStats](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.QueueStats)` | The stats.  
  
### getStatsOrBuilder()
    
    
    public abstract QueueStatsOrBuilder getStatsOrBuilder()

Output only. The realtime, informational statistics for a queue. In order to receive the statistics the caller should include this field in the FieldMask.

` .google.cloud.tasks.v2beta2.QueueStats stats = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[QueueStatsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.QueueStatsOrBuilder)` |   
  
### getTargetTypeCase()
    
    
    public abstract Queue.TargetTypeCase getTargetTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[Queue.TargetTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-tasks/latest/com.google.cloud.tasks.v2beta2.Queue.TargetTypeCase)` |   
  
### getTaskTtl()
    
    
    public abstract Duration getTaskTtl()

The maximum amount of time that a task will be retained in this queue.

Queues created by Cloud Tasks have a default `task_ttl` of 31 days. After a task has lived for `task_ttl`, the task will be deleted regardless of whether it was dispatched or not.

The `task_ttl` for queues created via queue.yaml/xml is equal to the maximum duration because there is a [storage quota](https://cloud.google.com/appengine/quotas#Task_Queue) for these queues. To view the maximum valid duration, see the documentation for Duration.

`.google.protobuf.Duration task_ttl = 9;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The taskTtl.  
  
### getTaskTtlOrBuilder()
    
    
    public abstract DurationOrBuilder getTaskTtlOrBuilder()

The maximum amount of time that a task will be retained in this queue.

Queues created by Cloud Tasks have a default `task_ttl` of 31 days. After a task has lived for `task_ttl`, the task will be deleted regardless of whether it was dispatched or not.

The `task_ttl` for queues created via queue.yaml/xml is equal to the maximum duration because there is a [storage quota](https://cloud.google.com/appengine/quotas#Task_Queue) for these queues. To view the maximum valid duration, see the documentation for Duration.

`.google.protobuf.Duration task_ttl = 9;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### getTombstoneTtl()
    
    
    public abstract Duration getTombstoneTtl()

The task tombstone time to live (TTL).

After a task is deleted or completed, the task's tombstone is retained for the length of time specified by `tombstone_ttl`. The tombstone is used by task de-duplication; another task with the same name can't be created until the tombstone has expired. For more information about task de-duplication, see the documentation for CreateTaskRequest.

Queues created by Cloud Tasks have a default `tombstone_ttl` of 1 hour.

`.google.protobuf.Duration tombstone_ttl = 10;`

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Duration.html)` | The tombstoneTtl.  
  
### getTombstoneTtlOrBuilder()
    
    
    public abstract DurationOrBuilder getTombstoneTtlOrBuilder()

The task tombstone time to live (TTL).

After a task is deleted or completed, the task's tombstone is retained for the length of time specified by `tombstone_ttl`. The tombstone is used by task de-duplication; another task with the same name can't be created until the tombstone has expired. For more information about task de-duplication, see the documentation for CreateTaskRequest.

Queues created by Cloud Tasks have a default `tombstone_ttl` of 1 hour.

`.google.protobuf.Duration tombstone_ttl = 10;`

**Returns**  
---  
**Type** | **Description**  
`[DurationOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DurationOrBuilder.html)` |   
  
### hasAppEngineHttpTarget()
    
    
    public abstract boolean hasAppEngineHttpTarget()

App Engine HTTP target.

An App Engine queue is a queue that has an AppEngineHttpTarget.

`.google.cloud.tasks.v2beta2.AppEngineHttpTarget app_engine_http_target = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the appEngineHttpTarget field is set.  
  
### hasHttpTarget()
    
    
    public abstract boolean hasHttpTarget()

An http_target is used to override the target values for HTTP tasks.

`.google.cloud.tasks.v2beta2.HttpTarget http_target = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the httpTarget field is set.  
  
### hasPullTarget()
    
    
    public abstract boolean hasPullTarget()

Pull target.

A pull queue is a queue that has a PullTarget.

`.google.cloud.tasks.v2beta2.PullTarget pull_target = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the pullTarget field is set.  
  
### hasPurgeTime()
    
    
    public abstract boolean hasPurgeTime()

Output only. The last time this queue was purged.

All tasks that were created before this time were purged.

A queue can be purged using PurgeQueue, the [App Engine Task Queue SDK, or the Cloud Console](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/deleting-tasks-and-queues#purging_all_tasks_from_a_queue).

Purge time will be truncated to the nearest microsecond. Purge time will be unset if the queue has never been purged.

`.google.protobuf.Timestamp purge_time = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the purgeTime field is set.  
  
### hasRateLimits()
    
    
    public abstract boolean hasRateLimits()

Rate limits for task dispatches.

rate_limits and retry_config are related because they both control task attempts however they control how tasks are attempted in different ways:

  * rate_limits controls the total rate of dispatches from a queue (i.e. all traffic dispatched from the queue, regardless of whether the dispatch is from a first attempt or a retry).
  * retry_config controls what happens to particular a task after its first attempt fails. That is, retry_config controls task retries (the second attempt, third attempt, etc).



`.google.cloud.tasks.v2beta2.RateLimits rate_limits = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rateLimits field is set.  
  
### hasRetryConfig()
    
    
    public abstract boolean hasRetryConfig()

Settings that determine the retry behavior.

  * For tasks created using Cloud Tasks: the queue-level retry settings apply to all tasks in the queue that were created using Cloud Tasks. Retry settings cannot be set on individual tasks.
  * For tasks created using the App Engine SDK: the queue-level retry settings apply to all tasks in the queue which do not have retry settings explicitly set on the task and were created by the App Engine SDK. See [App Engine documentation](https://cloud.google.com/appengine/docs/standard/python/taskqueue/push/retrying-tasks).



`.google.cloud.tasks.v2beta2.RetryConfig retry_config = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the retryConfig field is set.  
  
### hasStats()
    
    
    public abstract boolean hasStats()

Output only. The realtime, informational statistics for a queue. In order to receive the statistics the caller should include this field in the FieldMask.

` .google.cloud.tasks.v2beta2.QueueStats stats = 16 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stats field is set.  
  
### hasTaskTtl()
    
    
    public abstract boolean hasTaskTtl()

The maximum amount of time that a task will be retained in this queue.

Queues created by Cloud Tasks have a default `task_ttl` of 31 days. After a task has lived for `task_ttl`, the task will be deleted regardless of whether it was dispatched or not.

The `task_ttl` for queues created via queue.yaml/xml is equal to the maximum duration because there is a [storage quota](https://cloud.google.com/appengine/quotas#Task_Queue) for these queues. To view the maximum valid duration, see the documentation for Duration.

`.google.protobuf.Duration task_ttl = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the taskTtl field is set.  
  
### hasTombstoneTtl()
    
    
    public abstract boolean hasTombstoneTtl()

The task tombstone time to live (TTL).

After a task is deleted or completed, the task's tombstone is retained for the length of time specified by `tombstone_ttl`. The tombstone is used by task de-duplication; another task with the same name can't be created until the tombstone has expired. For more information about task de-duplication, see the documentation for CreateTaskRequest.

Queues created by Cloud Tasks have a default `tombstone_ttl` of 1 hour.

`.google.protobuf.Duration tombstone_ttl = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tombstoneTtl field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
