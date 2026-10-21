---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue
title: Package com.google.appengine.api.taskqueue (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:16:21.830924+00:00
---

# Package com.google.appengine.api.taskqueue (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Package com.google.appengine.api.taskqueue (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

Provides a mechanism to perform work initiated by a user request, outside of that request. See Also: [com.google.appengine.api.taskqueue.Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue), [The Task Queue Java API in the _Google App Engine Developer's Guide_](http://cloud.google.com/appengine/docs/java/taskqueue/).

## Classes 

### [DeferredTaskContext](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTaskContext)

Resources for managing [DeferredTask](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTask).

### [IQueueFactoryProvider](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.IQueueFactoryProvider)

Factory provider for [IQueueFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.IQueueFactory).

**Note:** This class is not intended for end users.

### [LeaseOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.LeaseOptions)

Contains various options for lease requests following the builder pattern. Calls to [LeaseOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.LeaseOptions) methods may be chained to specify multiple options in the one [LeaseOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.LeaseOptions) object.

Notes on usage:  
The recommended way to instantiate a [LeaseOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.LeaseOptions) object is to statically import Builder.* and invoke a static creation method followed by instance mutators:
    
    
     import static com.google.appengine.api.taskqueue.LeaseOptions.Builder.*;
    
     ...
     tasks = pullQueue.leaseTasks(withLeasePeriod(2, TimeUnit.HOURS).countLimit(1000));
     

### [LeaseOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.LeaseOptions.Builder)

Provides static creation methods for [LeaseOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.LeaseOptions).

### [QueueConstants](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueConstants)

Describes various taskqueue limits.

### [QueueFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueFactory)

Creates [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) objects. [QueueFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueFactory) is thread safe.

### [QueueStatistics](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueStatistics)

[QueueStatistics](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueStatistics) allow observation of the rate that tasks on a given queue are being executed. Note that statistics provided are only approximate, and some statistics may be delayed or transiently unavailable.

### [RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions)

Contains various options for a task's retry strategy. Calls to [RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions) methods may be chained to specify multiple options in the one [RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions) object.

Notes on usage:  
The recommended way to instantiate a [RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions) object is to statically import Builder.* and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import static com.google.appengine.api.taskqueue.RetryOptions.Builder.*;
    
     ...
     RetryOptions retry = withTaskRetryLimit(10).taskAgeLimitSeconds("4d")
         .minBackoffSeconds(120).maxBackoffSeconds(3600).maxDoublings(5);
     [QueueFactory#getDefaultQueue()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueFactory#com_google_appengine_api_taskqueue_QueueFactory_getDefaultQueue__).add(retryOptions(retry));
     

### [RetryOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions.Builder)

Provides static creation methods for [RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions).

### [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)

Created from [Queue#add(TaskOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_add_com_google_appengine_api_taskqueue_TaskOptions_). Contains the task name (generated if otherwise unspecified), task ETA (computed if not specified) and queue name. The queue name and task name uniquely identify the task for an application.

### [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)

Contains various options for a task following the builder pattern. Calls to [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) methods may be chained to specify multiple options in the one [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) object.

taskOptions can have either [TaskOptions.Method](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Method) PULL or a PUSH-related method, e.g. POST, GET, ... Tasks with PULL method can only be added into a PULL queue and PUSH tasks can only be added into a PUSH queue.

Notes on usage:  
The recommended way to instantiate a [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) object is to statically import Builder.* and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import static com.google.appengine.api.taskqueue.TaskOptions.Builder.*;
    
     ...
     [QueueFactory#getDefaultQueue()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueFactory#com_google_appengine_api_taskqueue_QueueFactory_getDefaultQueue__).add(withUrl(url).etaMillis(eta));
     

### [TaskOptions.Builder](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Builder)

Provides static creation methods for [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions).

## Interfaces 

### [DeferredTask](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTask)

Interface for deferred tasks. Classes implementing this interface may use [TaskOptions#payload(DeferredTask)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_payload_com_google_appengine_api_taskqueue_DeferredTask_) to serialize the [DeferredTask](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTask) into the payload of the task definition. The DeferredTask#run() method will be called when the task is received by the built in DeferredTask servlet.

Normal return from this method is considered success and will not retry unless [DeferredTaskContext#markForRetry](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTaskContext#com_google_appengine_api_taskqueue_DeferredTaskContext_markForRetry_) is called. Exceptions thrown from this method will indicate a failure and will be processed as a retry attempt unless [DeferredTaskContext#setDoNotRetry(boolean)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTaskContext#com_google_appengine_api_taskqueue_DeferredTaskContext_setDoNotRetry_boolean_) was set to `true`.

### [IQueueFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.IQueueFactory)

Creates [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) objects. [QueueFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueFactory) is thread safe.

### [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue)

[Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) is used to manage a task queue.

Implementations of this interface must be threadsafe.

Queues are transactional. If a datastore transaction is in progress when [#add()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_add__) or [#add(TaskOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_add_com_google_appengine_api_taskqueue_TaskOptions_) is invoked, the task will only be added to the queue if the datastore transaction successfully commits. If you want to add a task to a queue and have that operation succeed or fail independently of an existing datastore transaction you can invoke [#add(Transaction, TaskOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_add_com_google_appengine_api_datastore_Transaction_com_google_appengine_api_taskqueue_TaskOptions_) with a `null` transaction argument. Note that while the addition of the task to the queue can participate in an existing transaction, the execution of the task cannot participate in this transaction. In other words, when the transaction commits you are guaranteed that your task will be added and run, not that your task executed successfully.

Queues may be configured in either push or pull mode, but they share the same interface. However, only tasks with [TaskOptions.Method#PULL](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Method#com_google_appengine_api_taskqueue_TaskOptions_Method_PULL) may be added to pull queues. The tasks in push queues must be added with one of the other available methods.

Pull mode queues do not automatically deliver tasks to the application. The application is required to call [leaseTasks](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_leaseTasks_long_java_util_concurrent_TimeUnit_long_) to acquire a lease on the task and process them explicitly. Attempting to call [leaseTasks](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_leaseTasks_long_java_util_concurrent_TimeUnit_long_) on a push queue causes a [InvalidQueueModeException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.InvalidQueueModeException) to be thrown. When the task processing has finished processing a task that is leased, it should call [#deleteTask(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_deleteTask_java_lang_String_). If deleteTask is not called before the lease expires, the task will again be available for lease.

Queue mode can be switched between push and pull. When switching from push to pull, tasks will stay in the task queue and are available for lease, but url and headers information will be ignored when returning the tasks. When switching from pull to push, existing tasks will remain in the queue but will fail on auto-execution because they lack a url. If the queue mode is once again changed to pull, these tasks will eventually be available for lease.

## Enums 

### [TaskOptions.Method](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Method)

Methods supported by [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue). Tasks added to pull queues must have the [#Method](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Method) PULL. All other methods are appropriate for push queues. See [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) for more detail on pull and push mode queues.

## Exceptions 

### [DeferredTaskCreationException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTaskCreationException)

Indicates a failure to create a task payload. This is most likely an issue with serialization.

### [InternalFailureException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.InternalFailureException)

Internal task queue error.

### [InvalidQueueModeException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.InvalidQueueModeException)

Mismatch of task method and queue mode. e.g. Queue#leaseTasks(long, java.util.concurrent.TimeUnit, long) called on a push queue, [Queue#add(TaskOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_add_com_google_appengine_api_taskqueue_TaskOptions_) with method [TaskOptions.Method](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Method) PULL to a push queue, or with [TaskOptions.Method](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Method) not equal to PULL to a pull queue.

### [QueueFailureException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueFailureException)

Unspecified queue failure.

### [QueueNameMismatchException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueNameMismatchException)

Queue name mismatch failure.

### [TaskAlreadyExistsException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskAlreadyExistsException)

One or more task names already exists in the queue.

### [TransactionalTaskException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TransactionalTaskException)

Queue operation failure caused by Datastore exception

### [TransientFailureException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TransientFailureException)

Intermittent failure.

The requested operation may succeed if attempted again.

### [UnsupportedTranslationException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.UnsupportedTranslationException)

Attempt to convert String to an unsupported charset.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
