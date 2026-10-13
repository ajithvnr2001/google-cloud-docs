---
url: https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue
title: Class Queue (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:14:16.262533+00:00
---

# Class Queue (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Queue (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.3  2.18.0  2.17.1  2.16.5  2.15.1  2.14.2  2.13.2  2.12.1  2.11.0  2.10.4  2.9.1  2.8.1  2.7.2  2.6.0  2.5.3  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.5.2  1.4.0  1.3.0  1.2.1 
    
    
    Queue(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A queue is a container of related tasks. Queues are configured to manage how those tasks are dispatched. Configurable properties include rate limits, retry options, target types, and others.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Caller-specified and required in CreateQueue, after which it becomes output only. The queue name. The queue name must have the following format: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID` \- `PROJECT_ID` can contain letters ([A-Za-z]), numbers ([0-9]), hyphens (-), colons (:), or periods (.). For more information, see `Identifying projects   
`app_engine_http_target` |  `[google.cloud.tasks_v2beta2.types.AppEngineHttpTarget](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.AppEngineHttpTarget)`   
App Engine HTTP target. An App Engine queue is a queue that has an AppEngineHttpTarget. This field is a member of `oneof`_ `target_type`.   
`pull_target` |  `[google.cloud.tasks_v2beta2.types.PullTarget](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.PullTarget)`   
Pull target. A pull queue is a queue that has a PullTarget. This field is a member of `oneof`_ `target_type`.   
`http_target` |  `[google.cloud.tasks_v2beta2.types.HttpTarget](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.HttpTarget)`   
An http_target is used to override the target values for HTTP tasks. This field is a member of `oneof`_ `target_type`.   
`rate_limits` |  `[google.cloud.tasks_v2beta2.types.RateLimits](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.RateLimits)`   
Rate limits for task dispatches. rate_limits and retry_config are related because they both control task attempts however they control how tasks are attempted in different ways: \- rate_limits controls the total rate of dispatches from a queue (i.e. all traffic dispatched from the queue, regardless of whether the dispatch is from a first attempt or a retry). \- retry_config controls what happens to particular a task after its first attempt fails. That is, retry_config controls task retries (the second attempt, third attempt, etc).   
`retry_config` |  `[google.cloud.tasks_v2beta2.types.RetryConfig](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.RetryConfig)`   
Settings that determine the retry behavior. \- For tasks created using Cloud Tasks: the queue-level retry settings apply to all tasks in the queue that were created using Cloud Tasks. Retry settings cannot be set on individual tasks. \- For tasks created using the App Engine SDK: the queue-level retry settings apply to all tasks in the queue which do not have retry settings explicitly set on the task and were created by the App Engine SDK. See `App Engine documentation   
`state` |  `[google.cloud.tasks_v2beta2.types.Queue.State](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.Queue.State)`   
Output only. The state of the queue. `state` can only be changed by called PauseQueue, ResumeQueue, or uploading `queue.yaml/xml `__. UpdateQueue cannot be used to change `state`.   
`purge_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The last time this queue was purged. All tasks that were created before this time were purged. A queue can be purged using PurgeQueue, the `App Engine Task Queue SDK, or the Cloud Console   
`task_ttl` |  `google.protobuf.duration_pb2.Duration`   
The maximum amount of time that a task will be retained in this queue. Queues created by Cloud Tasks have a default `task_ttl` of 31 days. After a task has lived for `task_ttl`, the task will be deleted regardless of whether it was dispatched or not. The `task_ttl` for queues created via queue.yaml/xml is equal to the maximum duration because there is a `storage quota   
`tombstone_ttl` |  `google.protobuf.duration_pb2.Duration`   
The task tombstone time to live (TTL). After a task is deleted or completed, the task's tombstone is retained for the length of time specified by `tombstone_ttl`. The tombstone is used by task de-duplication; another task with the same name can't be created until the tombstone has expired. For more information about task de-duplication, see the documentation for CreateTaskRequest. Queues created by Cloud Tasks have a default `tombstone_ttl` of 1 hour.   
`stats` |  `[google.cloud.tasks_v2beta2.types.QueueStats](https://docs.cloud.google.com/python/docs/reference/cloudtasks/latest/google.cloud.tasks_v2beta2.types.QueueStats)`   
Output only. The realtime, informational statistics for a queue. In order to receive the statistics the caller should include this field in the FieldMask.   
  
## Classes 

### State
    
    
    State(value)

State of the queue.
    
    
        If the queue was created using Cloud Tasks and the queue has
        had no activity (method calls or task dispatches) for 30
        days, the queue may take a few minutes to re-activate. Some
        method calls may return
        `NOT_FOUND][google.rpc.Code.NOT_FOUND]` and tasks may not be
        dispatched for a few minutes until the queue has been
        re-activated.
    PAUSED (2):
        Tasks are paused by the user. If the queue is paused then
        Cloud Tasks will stop delivering tasks from it, but more
        tasks can still be added to it by the user. When a pull
        queue is paused, all
        <xref uid="google.cloud.tasks.v2beta2.CloudTasks.LeaseTasks">LeaseTasks</xref>
        calls will return a
        `FAILED_PRECONDITION][google.rpc.Code.FAILED_PRECONDITION]`.
    DISABLED (3):
        The queue is disabled.
    
        A queue becomes `DISABLED` when
        `queue.yaml <https://cloud.google.com/appengine/docs/python/config/queueref>`__
        or
        `queue.xml <https://cloud.google.com/appengine/docs/standard/java/config/queueref>`__
        is uploaded which does not contain the queue. You cannot
        directly disable a queue.
    
        When a queue is disabled, tasks can still be added to a
        queue but the tasks are not dispatched and
        <xref uid="google.cloud.tasks.v2beta2.CloudTasks.LeaseTasks">LeaseTasks</xref>
        calls return a `FAILED_PRECONDITION` error.
    
        To permanently delete this queue and all of its tasks, call
        <xref uid="google.cloud.tasks.v2beta2.CloudTasks.DeleteQueue">DeleteQueue</xref>.
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
