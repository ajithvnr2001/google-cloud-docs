---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/QueueStatistics/
title: google.appengine.api.taskqueue.QueueStatistics \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:03:07.721333+00:00
---

# google.appengine.api.taskqueue.QueueStatistics  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/QueueStatistics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.taskqueue.QueueStatistics Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1353-L1603) Represents the current state of a queue. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.taskqueue.QueueStatistics(
        queue,
        tasks,
        oldest_eta_usec=None,
        executed_last_minute=None,
        in_flight=None,
        enforced_rate=None
    )
    

| 

## Args  
  
---  
  
`queue` |  The queue instance for which you intend to use `QueueStatistics`.   
`tasks` |  The number of tasks remaining in the queue. **Note:** It is not always possible to accurately determine the value for the `tasks` field. Use this field with caution.   
`oldest_eta_usec` |  The `eta` of the oldest non-completed task for the queue; `None` if unknown or no incomplete tasks remain in the queue. The value `None` indicates that the queue has no backlog; the queue is empty or only contains tasks with an `eta` in the future. The `eta` represents the time at which a push queue task is eligible to run or a pull queue task can be leased. The value is expressed as microseconds since January 1, 1970. App Engine will not run a task before its `eta` time.**Note:** It is not always possible to accurately determine the value for the `oldest_eta_usec` field. Use this field with caution.   
`executed_last_minute` |  The number of tasks ran or leased in the last minute.   
`in_flight` |  For push queues, the number of tasks that are currently running. This value is not relevant for pull queues.   
`enforced_rate` |  For push queues, the current enforced rate in tasks per second. This value is not relevant for pull queues. The enforced rate is the actual rate at which tasks are being processed after any throttling done by App Engine to prevent the queue from overwhelming your application. The enforced rate can be smaller than the rate you specify in the queue configuration. If the enforced rate is too small, you can change performance settings for your application.   
  
## Methods

### `fetch`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1517-L1562)
    
    
    @classmethod
    fetch(
        queue_or_queues, deadline=10
    )
    

Get the queue details for multiple queues.

Use [`QueueStatistics.fetch()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/taskqueue/QueueStatistics#fetch) to get `QueueStatistics` objects for the queues you are interested in. You can specify one or more queues.

Example::
    
    
    statsList = taskqueue.QueueStatistics.fetch([taskqueue.Queue("foo"),
                                                 taskqueue.Queue("bar")])
    

Args  
---  
  
`queue_or_queues` |  The queue or list of queues for which you are obtaining statistics. If you are retrieving statistics for a single queue, you can supply either a queue instance or the name of the queue. If you are retrieving statistics for a list of queues, you can supply an iterable list of queue instances or an iterable list of queue names.   
`deadline` |  The maximum number of seconds to wait before aborting the method call.   
  
Returns  
---  
If an iterable (other than string) is provided as input, a list of of `QueueStatistics` objects will be returned, one for each queue in the order requested. Otherwise, if a single item was provided as input, then a single `QueueStatistics` object will be returned.   
  
Raises  
---  
  
`TypeError` |  If `queue_or_queues` is not a queue instance, string, an iterable containing only queue instances, or an iterable containing only strings. Error-subclass on application errors.   
  
### `fetch_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1455-L1515)
    
    
    @classmethod
    fetch_async(
        queue_or_queues, rpc=None
    )
    

Asynchronously get the queue details for multiple queues.

Example::
    
    
    rpc = taskqueue.create_rpc(deadline=1.0)
    taskqueue.QueueStatistics.fetch_async([taskqueue.Queue("foo"),
                                            taskqueue.Queue("bar")], rpc)
    statsList = rpc.get_result()
    

Args  
---  
  
`queue_or_queues` |  The queue or list of queues for which you are obtaining statistics. If you are retrieving statistics for a single queue, you can supply either a queue instance or the name of the queue. If you are retrieving a list of queues, you can supply an iterable list of queue instances or an iterable list of queue names.   
`rpc` |  An optional UserRPC object.   
  
Returns  
---  
A UserRPC object. Call `get_result()` to complete the RPC and obtain the result. If an iterable (other than string) is provided as input, the result will be a list of of `QueueStatistics` objects, one for each queue in the order requested. Otherwise, if a single item was provided as input, then the result will be a single `QueueStatistics` object.   
  
Raises  
---  
  
`TypeError` |  If `queue_or_queues` is not a queue instance, string, an iterable containing only queue instances, or an iterable containing only strings.   
  
### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1407-L1414)
    
    
    __eq__(
        o
    )
    

Return self==value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/taskqueue/taskqueue.py#L1416-L1423)
    
    
    __ne__(
        o
    )
    

Return self!=value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
