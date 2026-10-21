---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Task/
title: google.appengine.api.taskqueue.Task \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:13:01.703856+00:00
---

# google.appengine.api.taskqueue.Task  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Task/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.taskqueue.Task Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L693-L1350) Represents a single task on a queue. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.taskqueue.Task(
        payload=None, **kwargs
    )
    

The `Task` class enables an application to queue background work. Work is done through webhooks that process tasks pushed from a push queue, or workers that manually pull tasks from a pull queue. In push queues, most tasks are delivered in best-effort order of ETA.

#### Note:

Occasionally, tasks might be delivered out of order of ETA. However, for corner cases, tasks are delivered out of order for an extended period of time. You should not rely on tasks being delivered in order, as the results aren't always consistent. Webhooks that fail cause tasks to be retried at a later time. You can configure the rate and number of retries for failed tasks. You can specify webhook URLs directly for push tasks. You can also use the default URL scheme, which translates task names into URLs that are relative to a queue's base path. A default queue is also provided for simple usage. In pull queues, workers are responsible for leasing tasks, processing them, and deleting them after processing. You can configure the number of task retries, which is based on how many times the task has been leased. You can define multiple queues with independent throttling controls. You set the various properties for a task in the constructor. Once the `Task` object is instantiated, you insert that task into a queue. A task instance can be inserted into one queue only. | 

## Args  
  
---  
  
`payload` |  Optional; the payload data for this task. This argument is only allowed for `POST` and `PUT` methods and pull tasks. In push queues, the payload is delivered to the webhook or backend in the body of an HTTP request. In pull queues, the payload is fetched by workers as part of the response from `lease_tasks()`.   
`name` |  Optional; the name to give the task. If you do not specify a name, a name is auto-generated when added to a queue and assigned to this object. The name must match the `_TASK_NAME_PATTERN` regular expression. Avoid sequential names, such as counters or timestamps, as these names can lead to decreased availability and performance.   
`method` |  Optional; the HTTP method to use when accessing the webhook. The default value is `POST`. This argument is not used for pull queues.   
`url` |  Optional; the relative URL where the webhook that should handle this task is located for this application. You can include a query string in this value unless it is being used in a `POST` method. You cannot specify a URL for pull tasks.   
`headers` |  Optional; a dictionary of headers to pass to the webhook. The values in the dictionary can be iterable to indicate repeated header fields. You cannot specify headers for pull tasks. In a push task, if you do not specify a `Content-Type` header, the default value of `text/plain` will be used. In a push task, if you specify a `Host` header, you cannot use the `target` keyword argument. Any headers that use the `X-AppEngine` prefix will also be dropped.   
`params` |  Optional; a dictionary of parameters to use for the task. For `POST` requests and PULL tasks, these parameters are encoded as `application/x-www-form-urlencoded` and set to the payload. For both `POST` and pull requests, you cannot specify parameters if you already specified a `payload`. In `PUT` requests, parameters are converted to a query string if the URL contains a query string, or if the task already has a `payload`. Do not specify parameters if the URL contains a query string and the method is `GET`.   
`countdown` |  Optional; time in seconds into the future that this task should run or be leased. The default value is zero. Do not specify a countdown if you also specified an `eta`, as it sets the ETA to a value of now + `countdown`.   
`eta` |  Optional; a `datetime.datetime` specifying the absolute time at which the task should be run or leased. The `eta` argument must not be specified if `countdown` is specified. This value can be time zone-aware or time zone-naive. If the value is set to None, the default value is now. For pull tasks, no worker will be able to lease this task before the time indicated by the `eta` argument.   
`retry_options` |  Optional; a `TaskRetryOptions` object used to control how the task will be retried if it fails. For pull tasks, only the `task_retry_limit` option is allowed. For push tasks, you can use the `min_backoff_seconds`, `max_backoff_seconds`, `task_age_limit`, `max_doublings`, and `task_retry_limit` options.   
`target` |  Optional; a string that names a module or version, a frontend version, or a backend on which to run the task. The string is prepended to the domain name of your app. If you set the `target`, do not specify a `Host` header in the dictionary for the `headers` argument. For pull tasks, do not specify a target.   
`tag` |  Optional; the tag to be used when grouping by tag (pull tasks only).   
`dispatch_deadline_usec` |  A duration of time that serves as a limit on the dispatch duration; if the task's end point does not respond to the request within this deadline, the task is canceled (and retried depending on the config).   
  
## Raises  
  
---  
  
`InvalidDispatchDeadlineError` |  If the `dispatch_deadline_usec` is not within valid limits.   
`InvalidEtaError` |  If the `eta` is too far into the future.   
`InvalidTagError` |  If the tag is too long.   
`InvalidTaskError` |  If any of the parameters are invalid.   
`InvalidTaskNameError` |  If the task name is invalid.   
`InvalidUrlError` |  If the task URL is invalid or too long.   
`TaskTooLargeError` |  If the task with its associated payload is too large.   
  
## Attributes  
  
---  
  
`dispatch_deadline_usec` |  Returns the dispatch deadline set for the task.   
`eta` |  Returns a `datetime.datatime` when this task will run or be leased.   
`eta_posix` |  Returns a POSIX timestamp of when this task will run or be leased.   
`headers` |  Returns a copy of the HTTP headers for this task (push tasks only).   
`method` |  Returns the method to use for this task.   
`name` |  Returns the name of this task.   
`on_queue_url` |  Returns True if task runs on queue's default URL (push tasks only).   
`payload` |  Returns the payload to be used when the task is invoked (can be None).   
`queue_name` |  Returns the name of the queue with which this task is associated.   
`retry_count` |  Returns the number of retries or leases attempted on the task.   
`retry_options` |  Returns any or all the `TaskRetryOptions` tasks.   
`size` |  Returns the size of this task in bytes.   
`tag` |  Returns the tag for this task.   
`target` |  Returns the target for this task.   
`url` |  Returns the relative URL for this task (push tasks only).   
`was_deleted` |  Returns `True` if this task was successfully deleted.   
`was_enqueued` |  Returns `True` if this task has been inserted into a queue.   
  
## Methods

### `add`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1291-L1293)
    
    
    add(
        queue_name=_DEFAULT_QUEUE, transactional=False
    )
    

Adds this task to a queue. See [`Queue.add`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#add).

### `add_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1287-L1289)
    
    
    add_async(
        queue_name=_DEFAULT_QUEUE, transactional=False, rpc=None
    )
    

Asynchronously adds this task to a queue. See [`Queue.add_async`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/Queue#add_async).

### `extract_params`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1295-L1335)
    
    
    extract_params()
    

Returns the parameters for this task.

If the same name parameter has several values, then the value is a list of strings. For `POST` requests and pull tasks, the parameters are extracted from the task payload; for all other methods, the parameters are extracted from the URL query string.

Returns  
---  
A dictionary of strings that map parameter names to their values as strings. If the same name parameter has several values, the value will be a list of strings. For `POST` requests and pull tasks, the parameters are extracted from the task payload. For all other methods, the parameters are extracted from the URL query string. An empty dictionary is returned if the task contains an empty payload or query string.   
  
Raises  
---  
  
`ValueError` |  If the payload does not contain valid `application/x-www-form-urlencoded` data (for `POST` requests and pull tasks) or the URL does not contain a valid query (all other requests).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
