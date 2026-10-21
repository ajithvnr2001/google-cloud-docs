---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/TaskRetryOptions/
title: google.appengine.api.taskqueue.TaskRetryOptions \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:29:49.702246+00:00
---

# google.appengine.api.taskqueue.TaskRetryOptions  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/TaskRetryOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.taskqueue.TaskRetryOptions Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L578-L690) The options used to decide when a failed task will be retried. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.taskqueue.TaskRetryOptions(
        **kwargs
    )
    

Tasks executing in the task queue can fail for many reasons. If a task fails to execute, which is indicated by returning any HTTP status code outside of the range 200-299, App Engine retries the task until it succeeds. By default, the system gradually reduces the retry rate to avoid flooding your application with too many requests, but schedules retry attempts to recur at a maximum of once per hour until the task succeeds. 503 errors, however, are treated as special cases and should not be returned by user code. The `TaskRetryOptions` class provides the properties that you can use to decide when to retry a failed task at runtime. | 

## Args  
  
---  
  
`min_backoff_seconds` |  Optional; the minimum number of seconds to wait before retrying a task after it fails.   
`max_backoff_seconds` |  Optional; the maximum number of seconds to wait before retrying a task after it fails.   
`task_age_limit` |  Optional; the number of seconds after creation that a failed task will no longer be retried. The given value is rounded up to the nearest integer. If `task_retry_limit` is also specified, the task will be retried until both limits are reached.   
`max_doublings` |  Optional; the maximum number of times that the interval between failed task retries will be doubled before the increase becomes constant. The constant is: `2**(max_doublings - 1) * min_backoff_seconds`.   
`task_retry_limit` |  Optional; the maximum number of times to retry a failed task before giving up. In push queues, the counter is incremented each time App Engine tries the tasks, up to the specified limit. If `task_age_limit` is also specified, the task will be retried until both limits are reached.   
  
## Raises  
  
---  
  
`InvalidTaskRetryOptionsError` |  If any of the parameters are invalid.   
  
## Attributes  
  
---  
  
`max_backoff_seconds` |  The maximum number of seconds to wait before retrying a task.   
`max_doublings` |  The number of times that the retry interval will be doubled.   
`min_backoff_seconds` |  The minimum number of seconds to wait before retrying a task.   
`task_age_limit` |  The number of seconds after which a failed task will not be retried.   
`task_retry_limit` |  The number of times that a failed task will be retried.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
