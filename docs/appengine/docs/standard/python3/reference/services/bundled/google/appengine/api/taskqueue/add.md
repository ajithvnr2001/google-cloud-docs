---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/add/
title: google.appengine.api.taskqueue.add \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:18:57.771444+00:00
---

# google.appengine.api.taskqueue.add  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.taskqueue.add Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L2499-L2598) Convenience method that creates a task and adds it to a queue.
    
    
    google.appengine.api.taskqueue.add(
        *args, **kwargs
    )
    

All parameters are optional. Push tasks cannot be added to queues in pull mode. Similarly, pull tasks cannot be added to queues in push mode. | 

## Args  
  
---  
  
`payload` |  The payload data for this task that will be delivered to the webhook or backend as the HTTP request body (for push queues) or fetched by workers as part of the response from `lease_tasks()` (for pull queues). This argument is only allowed for `POST` and `PUT` methods and pull tasks.   
`queue_name` |  Name of queue to insert task into. If a name is not supplied, defaults to the default queue.   
`name` |  Name to give the task; if not specified, a name will be auto-generated when added to a queue and assigned to this object. The name must match the `_TASK_NAME_PATTERN` regular expression.   
`method` |  Method to use when accessing the webhook; the default value is `POST`. Other accepted values are `GET`, `PUT`, `DELETE`, `HEAD`, or `PULL`. Do not specify a method for push tasks, as the method will default to `POST` and post assigned tasks to the web hook at the `url` you specify. If you set the `method` to `PULL`, the task will not be automatically delivered to the webhook; instead, it will remain in the queue until leased.   
`url` |  Relative URL where the webhook that should handle this task is located for this application. You can use a query string unless this argument is used in a `POST` method. You cannot use this argument in a pull task.   
`headers` |  Dictionary of headers to pass to the webhook. Values in the dictionary can be iterable to indicate repeated header fields. If you do not specify a `Content-Type` header for a `PUSH` method, the default header (`text/plain`) will be used. If you specify a `Host` header for a `PUSH` method, do not specify a `target` argument. You cannot use a `header` argument in a pull task. Any headers that use the `X-AppEngine` prefix will also be dropped.   
`params` |  Dictionary of parameters to use for this task. For `POST` and pull requests, the values in the dictionary can be iterable to indicate repeated parameters, and these parameters will be encoded as `application/x-www-form-urlencoded` and set to the payload. For both `POST` and pull requests, do not specify parameters if you have already specified a payload. For `PUT` requests, parameters are converted to a query string if the URL contains a query string, or if the task already has a payload. For `PUT` requests, do not specify parameters if the URL already contains a query string and the method is `GET`. For all other methods, the parameters will be converted to a query string.   
`transactional` |  Optional. If `True`, adds tasks if and only if the enclosing transaction is successfully committed. An error will be returned if this argument is set to `True` in the absence of an enclosing transaction. If `False`, adds the tasks immediately, ignoring any enclosing transaction's success or failure.   
`countdown` |  Time in seconds into the future that this task should run or be leased. Defaults to zero. Do not specify this argument if you specified an `eta`.   
`eta` |  A `datetime.datetime` that specifies the absolute earliest time at which the task should run. You cannot specify this argument if the `countdown` argument is specified. This argument can be time zone-aware or time zone-naive, or set to a time in the past. If the argument is set to None, the default value is now. For pull tasks, no worker can lease the task before the time indicated by the `eta` argument.   
`retry_options` |  `TaskRetryOptions` used to control when the task will be retried if it fails. For pull tasks, you can only specify the `task_retry_limit` option to specify the number of times that a task can be leased before it is deleted from the queue. For push tasks, you can specify the `min_backoff_seconds`, `max_backoff_seconds`, `task_age_limit`, `max_doublings`, and `task_retry_limit` options.   
`tag` |  The tag to be used when grouping by tag (pull tasks only).   
`target` |  Push tasks only; specifies the alternate version or backend on which to run this task, or `DEFAULT_APP_VERSION` to run on the application's default version. You can specify a module or version, a frontend version, or a backend on which to run this task. The string that you specify will be prepended to the domain name of your app. If you specify the `target` argument, do not specify a `Host` header in the dictionary for the `headers` argument.   
  
## Returns  
  
---  
The task that was added to the queue.   
  
## Raises  
  
---  
  
`BadTransactionStateError` |  If the transactional argument is true but this call is being made outside of the context of a transaction.   
`InvalidEtaError` |  If the `eta` is set too far into the future.   
`InvalidQueueModeError` |  If a pull task is added to a queue in push mode, or a task with `method` not equal to `PULL` is added to a queue in pull mode.   
`InvalidTagError` |  If the tag is too long.   
`InvalidTaskError` |  If any of the parameters are invalid.   
`InvalidTaskNameError` |  If the task name is invalid.   
`InvalidUrlError` |  If the task URL is invalid or too long.   
`TaskTooLargeError` |  If the task with its associated payload is too large.   
`TransactionalRequestTooLargeError` |  If transactional is `True` and the total size of the tasks and supporting request data exceeds the `MAX_TRANSACTIONAL_REQUEST_SIZE_BYTES` quota.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
