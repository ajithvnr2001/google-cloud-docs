---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue/
title: google.appengine.api.taskqueue.Queue \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:02:09.523712+00:00
---

# google.appengine.api.taskqueue.Queue  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.taskqueue.Queue Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1606-L2494) Represents a queue. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.taskqueue.Queue(
        name=_DEFAULT_QUEUE
    )
    

The `Queue` class is used to prepare tasks for offline execution by App Engine. A queue object is instantiated by name. The name must correspond either to the default queue (provided by the system) or a user-defined queue as specified in the application's `queue.yaml` configuration file. The queue object can then be used to insert new task instances for offline execution by App Engine. Multiple queue objects can correspond to the same underlying system queue. However, a single task object can only be added to one queue. | 

## Args  
  
---  
  
`name` |  Optional; name of this queue, which must correspond to a user-defined queue name from `queue.yaml`. If not supplied, defaults to the default queue.   
  
## Raises  
  
---  
  
`InvalidQueueNameError` |  If the queue name is invalid.   
  
## Attributes  
  
---  
  
`name` |  Returns the name of this queue.   
  
## Methods

### `add`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L2146-L2212)
    
    
    add(
        task, transactional=False
    )
    

Adds a task or list of tasks into this queue.

If a list of more than one tasks is given, a raised exception does not guarantee that no tasks were added to the queue (unless `transactional` is set to `True`). To determine which tasks were successfully added when an exception is raised, check the [`Task.was_enqueued`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Task#was_enqueued) property.

Push tasks, or those with a method not equal to pull cannot be added to queues in pull mode. Similarly, pull tasks cannot be added to queues in push mode.

If a `TaskAlreadyExistsError` or `TombstonedTaskError` is raised, the caller can be guaranteed that for each one of the provided tasks, either the corresponding task was successfully added, or a task with the given name was successfully added in the past.

Args  
---  
  
`task` |  A task instance or a list of task instances that will be added to the queue. If `task` is set to a list of task objects, all tasks are added to the queue. If `Transactional=True`, then all of the tasks are added in the same active Datastore transaction, and if any of the tasks cannot be added to the queue, none of the tasks are added to the queue, and the Datastore transaction will fail. If `transactional=False`, a failure to add any task to the queue will raise an exception, but other tasks will be added to the queue.   
`transactional` |  If `True`, transactional tasks will be added to the queue but cannot be run or leased until after the transaction succeeds. If the transaction fails then the tasks will be removed from the queue (and therefore will never run). If `False`, the added tasks are available to run immediately; any enclosing transaction's success or failure is ignored.   
  
Returns  
---  
The task or list of tasks that was supplied to this method. Successfully queued tasks will have a valid queue name and task name after the call; these task objects are marked as queued and cannot be added again.   
`Note` |  Task objects returned from transactional adds are not notified or updated when the enclosing transaction succeeds or fails.   
  
Raises  
---  
  
`BadTaskStateError` |  If the task has already been added to a queue.   
`BadTransactionStateError` |  If the `transactional` argument is `True` but this call is being made outside of the context of a transaction.   
`DuplicateTaskNameError` |  If a task name is repeated in the request.   
`InvalidTaskNameError` |  If a task name is provided but is not valid.   
`InvalidTaskError` |  If both push and pull tasks exist in the task list.   
`InvalidQueueModeError` |  If a pull task is added to a queue in push mode, or if a push task is added to a queue in pull mode.   
`TaskAlreadyExistsError` |  If a task with the same name as a given name has previously been added to the queue.   
`TombstonedTaskError` |  If a task with the same name as a given name has previously been added to the queue and deleted.   
`TooManyTasksError` |  If a task contains more than `MAX_TASKS_PER_ADD` tasks.   
`TransactionalRequestTooLargeError` |  If transactional is `True` and the total size of the tasks and supporting request data exceeds the `MAX_TRANSACTIONAL_REQUEST_SIZE_BYTES` quota. Error-subclass on application errors.   
  
### `add_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L2064-L2144)
    
    
    add_async(
        task, transactional=False, rpc=None
    )
    

Asynchronously adds a task or list of tasks into this queue.

This function is identical to `add()` except that it returns an asynchronous object. You can call `get_result()` on the return value to block on the call.

Args  
---  
  
`task` |  A task instance or a list of task instances that will be added to the queue. If `task` is a list of task objects, all tasks are added to the queue. If `Transactional=True`, then all of the tasks are added in the same active Datastore transaction, and if any of the tasks cannot be added to the queue, none of the tasks are added to the queue and the Datastore transaction will fail. If `transactional=False`, a failure to add a task to the queue will raise an exception, but other tasks will be enqueued.   
`transactional` |  If `True`, transactional tasks will be added to the queue but cannot be run or leased until after the transaction succeeds. If the transaction fails, the tasks will be removed from the queue (and therefore will never run). If `False`, the added tasks are available to run immediately; any enclosing transaction's success or failure is ignored.   
`rpc` |  An optional UserRPC object.   
  
Returns  
---  
A UserRPC object. Call `get_result()` to complete the RPC and obtain the task or list of tasks that was supplied to this method. Successfully queued tasks will have a valid queue name and task name after the call; such task objects are marked as queued and cannot be added again.   
`Note` |  Task objects that are returned from transactional adds are not notified or updated when the enclosing transaction succeeds or fails.   
  
Raises  
---  
  
`BadTaskStateError` |  If the tasks have already been added to a queue.   
`BadTransactionStateError` |  If the transactional argument is `True` but this call is being made outside of the context of a transaction.   
`DuplicateTaskNameError` |  If a task name is repeated in the request.   
`InvalidTaskError` |  If both push and pull tasks exist in the task list.   
`InvalidTaskNameError` |  If a task name is provided but is not valid.   
`TooManyTasksError` |  If the task contains more than `MAX_TASKS_PER_ADD` tasks.   
`TransactionalRequestTooLargeError` |  If transactional is `True` and the total size of the tasks and supporting request data exceeds the `MAX_TRANSACTIONAL_REQUEST_SIZE_BYTES` quota.   
  
### `delete_tasks`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1765-L1788)
    
    
    delete_tasks(
        task
    )
    

Deletes a task or list of tasks in this queue.

When multiple tasks are specified, an exception will be raised if any individual task fails to be deleted. Check the `task.was_deleted` property.

The task name is the only task attribute that is used to select tasks for deletion. If any task exists that is unnamed or with the `was_deleted` property set to `True`, a `BadTaskStateError` will be raised immediately.

Args  
---  
  
`task` |  A task instance or a list of task instances that will be deleted from the queue.   
  
Returns  
---  
The task or list of tasks passed into this call.   
  
Raises  
---  
  
`BadTaskStateError` |  If the tasks to be deleted do not have task names or have already been deleted.   
`DuplicateTaskNameError` |  If a task is repeated in the request. Error-subclass on application errors.   
  
### `delete_tasks_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1731-L1763)
    
    
    delete_tasks_async(
        task, rpc=None
    )
    

Asynchronously deletes a task or list of tasks in this queue.

The task name is the only task attribute that is used to select tasks for deletion.

This function is identical to `delete_tasks()` except that it returns an asynchronous object. You can call `get_result()` on the return value to block on the call.

Args  
---  
  
`task` |  A task instance or a list of task instances that will be deleted from the queue.   
`rpc` |  An optional UserRPC object.   
  
Returns  
---  
A UserRPC object. Call `get_result()` to complete the RPC and obtain the task or list of tasks passed into this call.   
  
Raises  
---  
  
`BadTaskStateError` |  If the tasks to be deleted do not have task names or have already been deleted.   
`DuplicateTaskNameError` |  If a task is repeated in the request.   
  
### `delete_tasks_by_name`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1706-L1729)
    
    
    delete_tasks_by_name(
        task_name
    )
    

Deletes a task or list of tasks in this queue, by name.

When multiple tasks are specified, an exception will be raised if any individual task fails to be deleted.

Args  
---  
  
`task_name` |  A string corresponding to a task name, or an iterable of strings corresponding to task names.   
  
Returns  
---  
If an iterable, other than string, is provided as input, a list of task objects is returned, one for each task name in the order requested. The [`Task.was_deleted`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Task#was_deleted) property will be `True` for each task deleted by this call, and will be `False` for unknown and tombstoned tasks. Otherwise, if a single string was provided as input, a single task object is returned.   
  
Raises  
---  
  
`DuplicateTaskNameError` |  If a task name is repeated in the request. Error-subclass on application errors.   
  
### `delete_tasks_by_name_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1672-L1704)
    
    
    delete_tasks_by_name_async(
        task_name, rpc=None
    )
    

Asynchronously deletes a task or list of tasks in this queue, by name.

This function is identical to `delete_tasks_by_name()` except that it returns an asynchronous object. You can call `get_result()` on the return value to block on the call.

Args  
---  
  
`task_name` |  A string corresponding to a task name, or an iterable of strings corresponding to task names.   
`rpc` |  An optional UserRPC object.   
  
Returns  
---  
A UserRPC object. Call `get_result()` to complete the RPC and obtain the result. If an iterable, other than string, is provided as input, the result will be a list of of task objects, one for each task name in the order requested. The [`Task.was_deleted`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Task#was_deleted) property will be `True` for each task deleted by this call, and will be `False` for unknown and tombstoned tasks. Otherwise, if a single string was provided as input, then the result will be a single task object.   
  
Raises  
---  
  
`DuplicateTaskNameError` |  If a task name is repeated in the request.   
  
### `fetch_statistics`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L2462-L2476)
    
    
    fetch_statistics(
        deadline=10
    )
    

Gets the current details about this queue.

Args  
---  
  
`deadline` |  The maximum number of seconds to wait before aborting the method call.   
  
Returns  
---  
A `QueueStatistics` instance that contains information about this queue. Error-subclass on application errors.   
  
### `fetch_statistics_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L2450-L2460)
    
    
    fetch_statistics_async(
        rpc=None
    )
    

Asynchronously gets the current details about this queue.

Args  
---  
  
`rpc` |  An optional UserRPC object.   
  
Returns  
---  
A UserRPC object. Call `get_result()` to complete the RPC and obtain a `QueueStatistics` instance that contains information about this queue.   
  
### `lease_tasks`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1948-L1979)
    
    
    lease_tasks(
        lease_seconds, max_tasks, deadline=10
    )
    

Leases a number of tasks from the queue for a period of time.

This method can only be performed on a pull queue. Any non-pull tasks in the pull queue will be converted into pull tasks when being leased. If fewer than the specified number of `max_tasks` are available, all available tasks will be returned. The `lease_tasks` method supports leasing at most 1000 tasks for no longer than a week in a single call.

Args  
---  
  
`lease_seconds` |  Number of seconds to lease the tasks, up to one week (604,800 seconds). Must be a positive integer.   
`max_tasks` |  The maximum number of tasks to lease from the pull queue, up to 1000 tasks.   
`deadline` |  The maximum number of seconds to wait before aborting the method call.   
  
Returns  
---  
A list of tasks leased from the queue.   
  
Raises  
---  
  
`InvalidLeaseTimeError` |  If `lease_seconds` is not a valid float or integer number or is outside the valid range.   
`InvalidMaxTasksError` |  If `max_tasks` is not a valid integer or is outside the valid range.   
`InvalidQueueModeError` |  If invoked on a queue that is not in pull mode. Error-subclass on application errors.   
  
### `lease_tasks_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1905-L1946)
    
    
    lease_tasks_async(
        lease_seconds, max_tasks, rpc=None
    )
    

Asynchronously leases a number of tasks from the queue.

This method can only be performed on a pull queue. Attempts to lease tasks from a push queue results in an `InvalidQueueModeError`. All non-pull tasks in the pull queue will be converted into pull tasks when leased. If fewer than the specified value of `max_tasks` are available, all available tasks on a best-effort basis are returned. The `lease_tasks_async` method supports leasing at most 1000 tasks for no longer than a week in a single call.

This function is identical to `lease_tasks()` except that it returns an asynchronous object. You can call `get_result()` on the return value to block on the call.

Args  
---  
  
`lease_seconds` |  Number of seconds to lease the tasks, up to one week (604,800 seconds). Must be a positive integer.   
`max_tasks` |  Maximum number of tasks to lease from the pull queue, up to 1000 tasks.   
`rpc` |  An optional UserRPC object.   
  
Returns  
---  
A UserRPC object. Call `get_result()` to complete the RPC and obtain the list of tasks leased from the queue.   
  
Raises  
---  
  
`InvalidLeaseTimeError` |  If `lease_seconds` is not a valid float or integer number or is outside the valid range.   
`InvalidMaxTasksError` |  If `max_tasks` is not a valid integer or is outside the valid range.   
  
### `lease_tasks_by_tag`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L2027-L2062)
    
    
    lease_tasks_by_tag(
        lease_seconds, max_tasks, tag=None, deadline=10
    )
    

Leases tasks with the same tag from the queue.

If a `tag` is specified, tasks with that tag are leased for a specified period of time. If a `tag` is not specified, the tag of the queue's oldest task (specified by the `eta`) will be used.

This method can only be performed on a pull queue. Any non-pull tasks in the pull queue will be converted into pull tasks when being leased. If fewer than the specified value of `max_tasks` are available, all available tasks will be returned. The `lease_tasks` method supports leasing at most 1000 tasks for no longer than a week in a single call.

Args  
---  
  
`lease_seconds` |  Number of seconds to lease the tasks.   
`max_tasks` |  The maximum number of tasks to lease from the pull queue.   
`tag` |  The tag to query for, or None to group by the first available tag.   
`deadline` |  The maximum number of seconds to wait before aborting the method call.   
  
Returns  
---  
A list of tasks leased from the queue.   
  
Raises  
---  
  
`InvalidLeaseTimeError` |  If `lease_seconds` is not a valid float or integer number or is outside the valid range.   
`InvalidMaxTasksError` |  If `max_tasks` is not a valid integer or is outside the valid range.   
`InvalidQueueModeError` |  If invoked on a queue that is not in pull mode. Error-subclass on application errors.   
  
### `lease_tasks_by_tag_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1981-L2025)
    
    
    lease_tasks_by_tag_async(
        lease_seconds, max_tasks, tag=None, rpc=None
    )
    

Asynchronously leases tasks with the same tag from the queue.

If a `tag` is specified, tasks with that tag are leased for a specified period of time. If a `tag` is not specified, the best-effort oldest tag of the queue's oldest task (specified by the `eta`) will be used.

This function is identical to `lease_tasks_by_tag()` except that it returns an asynchronous object. You can call `get_result()` on the return value to block on the call.

Args  
---  
  
`lease_seconds` |  Number of seconds to lease the tasks.   
`max_tasks` |  The maximum number of tasks to lease from the pull queue.   
`tag` |  The tag to query for, or None to group by the first available tag.   
`rpc` |  An optional UserRPC object.   
  
Returns  
---  
A UserRPC object. Call `get_result()` to complete the RPC and obtain the list of tasks leased from the queue.   
  
Raises  
---  
  
`InvalidLeaseTimeError` |  If `lease_seconds` is not a valid float or integer number or is outside the valid range.   
`InvalidMaxTasksError` |  If `max_tasks` is not a valid integer or is outside the valid range.   
  
### `modify_task_lease`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L2414-L2448)
    
    
    modify_task_lease(
        task, lease_seconds
    )
    

Modifies the lease of a task in this queue.

Args  
---  
  
`task` |  A task instance that will have its lease modified.   
`lease_seconds` |  Number of seconds, from the current time, that the task lease will be modified to. If `lease_seconds` is `0`, the task lease is removed and the task will be available for leasing again using the `lease_tasks` method.   
  
Raises  
---  
  
`TypeError` |  If `lease_seconds` is not a valid float or integer.   
`InvalidLeaseTimeError` |  If `lease_seconds` is outside of the valid range. Error-subclass on application errors.   
  
### `purge`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1647-L1670)
    
    
    purge()
    

Removes all of the tasks in this queue.

Purging the queue takes time, regardless of the queue size. Tasks continue to run until the backends recognize that the queue has been purged. This operation is permanent; purged tasks cannot be recovered.

Raises  
---  
Error-subclass on application errors.   
  
### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L2486-L2489)
    
    
    __eq__(
        o
    )
    

Return self==value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L2491-L2494)
    
    
    __ne__(
        o
    )
    

Return self!=value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
