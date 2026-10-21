---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/
title: Module: google.appengine.api.taskqueue \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:40:16.295032+00:00
---

# Module: google.appengine.api.taskqueue  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Module: google.appengine.api.taskqueue Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/__init__.py) Task Queue API module.

## Classes

[`class BadTaskStateError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/BadTaskStateError): The task is in the wrong state for the requested operation. [`class BadTransactionState`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/BadTransactionState): The state of the current transaction does not permit this operation. [`class BadTransactionStateError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/BadTransactionState): The state of the current transaction does not permit this operation. [`class DatastoreError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/DatastoreError): There was a datastore error while accessing the queue. [`class DuplicateTaskNameError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/DuplicateTaskNameError): Two tasks have the same name. [`class Error`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Error): Base class for exceptions in this module. [`class InternalError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InternalError): An internal error occurred while accessing this queue. [`class InvalidDeadlineError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidDeadlineError): The requested deadline in `lease_tasks` is invalid. [`class InvalidDispatchDeadlineError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidDispatchDeadlineError): The requested dispatch deadline for a `push task` is invalid. [`class InvalidEtaError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidEtaError): The task's ETA is invalid. [`class InvalidLeaseTimeError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidLeaseTimeError): The lease time period is invalid. [`class InvalidMaxTasksError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidMaxTasksError): The requested maximum number of tasks in `lease_tasks` is invalid. [`class InvalidQueueError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidQueueError): The queue's configuration is invalid. [`class InvalidQueueModeError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidQueueModeError): Invokes a pull queue operation on a push queue or vice versa. [`class InvalidQueueNameError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidQueueNameError): The name of the queue is invalid. [`class InvalidTagError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidTagError): The specified tag is invalid. [`class InvalidTaskError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidTaskError): The parameters, headers, or method of the task is invalid. [`class InvalidTaskNameError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidTaskNameError): The name of the task is invalid. [`class InvalidUrlError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/InvalidUrlError): The relative URL used for the task is invalid. [`class PermissionDeniedError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/PermissionDeniedError): The requested operation is not allowed for this app. [`class Queue`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue): Represents a queue. [`class QueuePausedError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/QueuePausedError): The queue is paused and cannot process modify task lease requests. [`class QueueStatistics`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/QueueStatistics): Represents the current state of a queue. [`class Task`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Task): Represents a single task on a queue. [`class TaskAlreadyExistsError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/TaskAlreadyExistsError): The task already exists. It has not yet run. [`class TaskLeaseExpiredError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/TaskLeaseExpiredError): The task lease could not be renewed because it had already expired. [`class TaskRetryOptions`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/TaskRetryOptions): The options used to decide when a failed task will be retried. [`class TaskTooLargeError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/TaskTooLargeError): The task is too large with its headers and payload. [`class TombstonedTaskError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/TombstonedTaskError): The task has been tombstoned. [`class TooManyTasksError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/TooManyTasksError): Too many tasks were present in a single function call. [`class TransientError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/TransientError): A transient error occurred while accessing the queue. Try again later. [`class UnknownQueueError`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/UnknownQueueError): The queue specified is unknown.

## Functions

[`add(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/add): Convenience method that creates a task and adds it to a queue. [`create_rpc(...)`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/create_rpc): Creates an RPC object for use with the Task Queue API. | 

## Other Members  
  
---  
  
DEFAULT_APP_VERSION |  Instance of `google.appengine.api.taskqueue.taskqueue._DefaultAppVersionSingleton`  
MAX_LEASE_SECONDS |  `604800`  
MAX_PULL_TASK_SIZE_BYTES |  `1048576`  
MAX_PUSH_TASK_SIZE_BYTES |  `102400`  
MAX_QUEUE_NAME_LENGTH |  `100`  
MAX_TASKS_PER_ADD |  `100`  
MAX_TASKS_PER_LEASE |  `1000`  
MAX_TASK_NAME_LENGTH |  `500`  
MAX_TASK_SIZE_BYTES |  `102400`  
MAX_URL_LENGTH |  `2083`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
