---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue
title: Interface Queue (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:33:19.200790+00:00
---

# Interface Queue (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Interface Queue (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public interface Queue

[Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) is used to manage a task queue.

Implementations of this interface must be threadsafe.

Queues are transactional. If a datastore transaction is in progress when [#add()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_add__) or [#add(TaskOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_add_com_google_appengine_api_taskqueue_TaskOptions_) is invoked, the task will only be added to the queue if the datastore transaction successfully commits. If you want to add a task to a queue and have that operation succeed or fail independently of an existing datastore transaction you can invoke [#add(Transaction, TaskOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_add_com_google_appengine_api_datastore_Transaction_com_google_appengine_api_taskqueue_TaskOptions_) with a `null` transaction argument. Note that while the addition of the task to the queue can participate in an existing transaction, the execution of the task cannot participate in this transaction. In other words, when the transaction commits you are guaranteed that your task will be added and run, not that your task executed successfully.

Queues may be configured in either push or pull mode, but they share the same interface. However, only tasks with [TaskOptions.Method#PULL](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Method#com_google_appengine_api_taskqueue_TaskOptions_Method_PULL) may be added to pull queues. The tasks in push queues must be added with one of the other available methods.

Pull mode queues do not automatically deliver tasks to the application. The application is required to call [leaseTasks](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_leaseTasks_long_java_util_concurrent_TimeUnit_long_) to acquire a lease on the task and process them explicitly. Attempting to call [leaseTasks](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_leaseTasks_long_java_util_concurrent_TimeUnit_long_) on a push queue causes a [InvalidQueueModeException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.InvalidQueueModeException) to be thrown. When the task processing has finished processing a task that is leased, it should call [#deleteTask(String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_deleteTask_java_lang_String_). If deleteTask is not called before the lease expires, the task will again be available for lease.

Queue mode can be switched between push and pull. When switching from push to pull, tasks will stay in the task queue and are available for lease, but url and headers information will be ignored when returning the tasks. When switching from pull to push, existing tasks will remain in the queue but will fail on auto-execution because they lack a url. If the queue mode is once again changed to pull, these tasks will eventually be available for lease.

## Static Fields 

### DEFAULT_QUEUE
    
    
    public static final String DEFAULT_QUEUE

The default queue name.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### DEFAULT_QUEUE_PATH
    
    
    public static final String DEFAULT_QUEUE_PATH

The default queue path.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Methods 

### add()
    
    
    public abstract TaskHandle add()

Submits a task to this queue with an auto generated name with default options.

This method is similar to calling [#add(TaskOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_add_com_google_appengine_api_taskqueue_TaskOptions_) with a [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) object returned by [TaskOptions.Builder#withDefaults()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Builder#com_google_appengine_api_taskqueue_TaskOptions_Builder_withDefaults__).

**Returns**  
---  
**Type** | **Description**  
`[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)` | A [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle).  
  
### add(Transaction txn, TaskOptions taskOptions)
    
    
    public abstract TaskHandle add(Transaction txn, TaskOptions taskOptions)

Submits a task to this queue in the provided Transaction.

A task is added if and only if the transaction is applied successfully.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
an enclosing [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) or null, if not null a task cannot be named.  
`taskOptions` | `[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)`  
The definition of the task.  
**Returns**  
---  
**Type** | **Description**  
`[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)` | A [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle).  
  
### add(Transaction txn, Iterable<TaskOptions> taskOptions)
    
    
    public abstract List<TaskHandle> add(Transaction txn, Iterable<TaskOptions> taskOptions)

Submits tasks to this queue in the provided Transaction.

The tasks are added if and only if the transaction is applied successfully.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
an enclosing [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) or null, if not null a task cannot be named.  
`taskOptions` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)>`  
An iterable over task definitions.  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>` | A list containing a [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each added task.  
  
### add(TaskOptions taskOptions)
    
    
    public abstract TaskHandle add(TaskOptions taskOptions)

Submits a task to this queue.

**Parameter**  
---  
**Name** | **Description**  
`taskOptions` | `[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)`  
The definition of the task.  
**Returns**  
---  
**Type** | **Description**  
`[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)` | A [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle).  
  
### add(Iterable<TaskOptions> taskOptions)
    
    
    public abstract List<TaskHandle> add(Iterable<TaskOptions> taskOptions)

Submits tasks to this queue.

Submission is not atomic i.e. if this method throws then some tasks may have been added to the queue.

**Parameter**  
---  
**Name** | **Description**  
`taskOptions` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)>`  
An iterable over task definitions.  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>` | A list containing a [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each added task.  
  
### addAsync()
    
    
    public abstract Future<TaskHandle> addAsync()

Asynchronously submits a task to this queue with an auto generated name with default options.

This method is similar to calling [#addAsync(TaskOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_addAsync_com_google_appengine_api_taskqueue_TaskOptions_) with a [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) object returned by [TaskOptions.Builder#withDefaults()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Builder#com_google_appengine_api_taskqueue_TaskOptions_Builder_withDefaults__).

**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>` | A `Future` with a result type of [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle).  
  
### addAsync(Transaction txn, TaskOptions taskOptions)
    
    
    public abstract Future<TaskHandle> addAsync(Transaction txn, TaskOptions taskOptions)

Asynchronously submits a task to this queue in the provided Transaction.

A task is added if and only if the transaction is applied successfully.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
an enclosing [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) or null, if not null a task cannot be named.  
`taskOptions` | `[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)`  
The definition of the task.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>` | A `Future` with a result type of [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle).  
  
### addAsync(Transaction txn, Iterable<TaskOptions> taskOptions)
    
    
    public abstract Future<List<TaskHandle>> addAsync(Transaction txn, Iterable<TaskOptions> taskOptions)

Asynchronously submits tasks to this queue in the provided Transaction.

The tasks are added if and only if the transaction is applied successfully.

**Parameters**  
---  
**Name** | **Description**  
`txn` | `[Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction)`  
an enclosing [Transaction](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.Transaction) or null, if not null a task cannot be named.  
`taskOptions` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)>`  
An iterable over task definitions.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>>` | A `Future` whose result is a list containing a [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each added task.  
  
### addAsync(TaskOptions taskOptions)
    
    
    public abstract Future<TaskHandle> addAsync(TaskOptions taskOptions)

Asynchronously submits a task to this queue.

**Parameter**  
---  
**Name** | **Description**  
`taskOptions` | `[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)`  
The definition of the task.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>` | A `Future` with a result type of [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle).  
  
### addAsync(Iterable<TaskOptions> taskOptions)
    
    
    public abstract Future<List<TaskHandle>> addAsync(Iterable<TaskOptions> taskOptions)

Asynchronously submits tasks to this queue.

Submission is not atomic i.e. if this method fails then some tasks may have been added to the queue.

**Parameter**  
---  
**Name** | **Description**  
`taskOptions` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)>`  
An iterable over task definitions.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>>` | A `Future` whose result is a list containing a [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each added task.  
  
### deleteTask(TaskHandle taskHandle)
    
    
    public abstract boolean deleteTask(TaskHandle taskHandle)

Deletes a task from this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue). Task is identified by a TaskHandle.

**Parameter**  
---  
**Name** | **Description**  
`taskHandle` | `[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)`  
handle of the task to delete.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | True if the task was successfully deleted. False if the task was not found or was previously deleted.  
  
### deleteTask(String taskName)
    
    
    public abstract boolean deleteTask(String taskName)

Deletes a task from this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue). Task is identified by taskName.

**Parameter**  
---  
**Name** | **Description**  
`taskName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the task to delete.  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | True if the task was successfully deleted. False if the task was not found or was previously deleted.  
  
### deleteTask(List<TaskHandle> taskHandles)
    
    
    public abstract List<Boolean> deleteTask(List<TaskHandle> taskHandles)

Deletes a list of tasks from this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue). The tasks are identified by a list of TaskHandles. This method supports deleting up to 1000 tasks.

**Parameter**  
---  
**Name** | **Description**  
`taskHandles` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>`  
list of handles of tasks to delete.  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` | `List<Boolean>` that represents the result of deleting each task in the same order as the input handles. True if a task was successfully deleted. False if the task was not found or was previously deleted.  
  
### deleteTaskAsync(TaskHandle taskHandle)
    
    
    public abstract Future<Boolean> deleteTaskAsync(TaskHandle taskHandle)

Asynchronously deletes a task from this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue). Task is identified by a TaskHandle.

**Parameter**  
---  
**Name** | **Description**  
`taskHandle` | `[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)`  
handle of the task to delete.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` | A `Future` whose result is True if the task was successfully deleted, False if the task was not found or was previously deleted.  
  
### deleteTaskAsync(String taskName)
    
    
    public abstract Future<Boolean> deleteTaskAsync(String taskName)

Asynchronously deletes a task from this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue). Task is identified by taskName.

**Parameter**  
---  
**Name** | **Description**  
`taskName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
name of the task to delete.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>` | A `Future` whose result is True if the task was successfully deleted, False if the task was not found or was previously deleted.  
  
### deleteTaskAsync(List<TaskHandle> taskHandles)
    
    
    public abstract Future<List<Boolean>> deleteTaskAsync(List<TaskHandle> taskHandles)

Asynchronously deletes a list of tasks from this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue). The tasks are identified by a list of TaskHandles. This method supports deleting up to 1000 tasks.

**Parameter**  
---  
**Name** | **Description**  
`taskHandles` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>`  
list of handles of tasks to delete.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)>>` | A `Future` whose result is a `List<Boolean>` that represents the result of deleting each task in the same order as the input handles. True if a task was successfully deleted. False if the task was not found or was previously deleted.  
  
### fetchStatistics()
    
    
    public abstract QueueStatistics fetchStatistics()

Obtain statistics for this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue).

**Returns**  
---  
**Type** | **Description**  
`[QueueStatistics](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueStatistics)` | The current [QueueStatistics](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueStatistics) for this queue.  
  
### fetchStatisticsAsync(@Nullable Double deadlineInSeconds)
    
    
    public abstract Future<QueueStatistics> fetchStatisticsAsync(@Nullable Double deadlineInSeconds)

Asynchronously obtains statistics for this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue).

**Parameter**  
---  
**Name** | **Description**  
`deadlineInSeconds` | `[Nullable Double](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Double.html)`  
the maximum duration, in seconds, that the fetch statistics request can run. A default deadline will be used if `null` is supplied.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[QueueStatistics](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueStatistics)>` | A `Future` with a result type of [QueueStatistics](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueStatistics).  
  
### getQueueName()
    
    
    public abstract String getQueueName()

Returns the queue name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### leaseTasks(LeaseOptions options)
    
    
    public abstract List<TaskHandle> leaseTasks(LeaseOptions options)

Leases tasks from this queue, with lease period and other options specified by `options`. The available tasks are those in the queue having the earliest eta such that eta is prior to the time at which the lease is requested.

If `options` specifies a tag, only tasks having that tag will be returned. If ` options` specifies no tag, but does specify `groupByTag`, only tasks having the same tag as the task with earliest eta will be returned.

It is guaranteed that the leased tasks will be unavailable for lease to others in the lease period. You must call deleteTask to prevent the task from being leased again after the lease period. This method supports leasing a maximum of 1000 tasks for no more than one week. If you generate more than 10 LeaseTasks requests per second, only the first 10 requests will return results. The others will return no results.

**Parameter**  
---  
**Name** | **Description**  
`options` | `[LeaseOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.LeaseOptions)`  
Specific options for this lease request  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>` | A list of [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each leased task.  
  
### leaseTasks(long lease, TimeUnit unit, long countLimit)
    
    
    public abstract List<TaskHandle> leaseTasks(long lease, TimeUnit unit, long countLimit)

Leases up to `countLimit` tasks from this queue for a period specified by `lease` and `unit`. If fewer tasks than `countLimit` are available, all available tasks in this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) will be returned. The available tasks are those in the queue having the earliest eta such that eta is prior to the time at which the lease is requested. It is guaranteed that the leased tasks will be unavailable for lease to others in the lease period. You must call deleteTask to prevent the task from being leased again after the lease period. This method supports leasing a maximum of 1000 tasks for no more than one week. If you generate more than 10 LeaseTasks requests per second, only the first 10 requests will return results. The others will return no results.

**Parameters**  
---  
**Name** | **Description**  
`lease` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Number of `unit`s in the lease period  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
Time unit of the lease period  
`countLimit` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
maximum number of tasks to lease  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>` | A list of [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each leased task.  
  
### leaseTasksAsync(LeaseOptions options)
    
    
    public abstract Future<List<TaskHandle>> leaseTasksAsync(LeaseOptions options)

Asynchronously leases tasks from this queue, with lease period and other options specified by `options`. The available tasks are those in the queue having the earliest eta such that eta is prior to the time at which the lease is requested.

If `options` specifies a tag, only tasks having that tag will be returned. If ` options` specifies no tag, but does specify `groupByTag`, only tasks having the same tag as the task with earliest eta will be returned.

It is guaranteed that the leased tasks will be unavailable for lease to others in the lease period. You must call deleteTask to prevent the task from being leased again after the lease period. This method supports leasing a maximum of 1000 tasks for no more than one week. If you generate more than 10 LeaseTasks requests per second, only the first 10 requests will return results. The others will return no results.

**Parameter**  
---  
**Name** | **Description**  
`options` | `[LeaseOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.LeaseOptions)`  
Specific options for this lease request  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>>` | A `Future` whose result is a list of [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each leased task.  
  
### leaseTasksAsync(long lease, TimeUnit unit, long countLimit)
    
    
    public abstract Future<List<TaskHandle>> leaseTasksAsync(long lease, TimeUnit unit, long countLimit)

Asynchronously leases up to `countLimit` tasks from this queue for a period specified by `lease` and `unit`. If fewer tasks than `countLimit` are available, all available tasks in this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) will be returned. The available tasks are those in the queue having the earliest eta such that eta is prior to the time at which the lease is requested. It is guaranteed that the leased tasks will be unavailable for lease to others in the lease period. You must call deleteTask to prevent the task from being leased again after the lease period. This method supports leasing a maximum of 1000 tasks for no more than one week. If you generate more than 10 LeaseTasks requests per second, only the first 10 requests will return results. The others will return no results.

**Parameters**  
---  
**Name** | **Description**  
`lease` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Number of `unit`s in the lease period  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
Time unit of the lease period  
`countLimit` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
maximum number of tasks to lease  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>>` | A `Future` whose result is a list of [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each leased task.  
  
### leaseTasksByTag(long lease, TimeUnit unit, long countLimit, String tag)
    
    
    public abstract List<TaskHandle> leaseTasksByTag(long lease, TimeUnit unit, long countLimit, String tag)

Leases up to `countLimit` tasks from this queue for a period specified by `lease` and `unit`, having tag `tag`. If `tag` is `null`, tasks having the same tag as the task with earliest eta will be returned. If fewer such tasks than `countLimit` are available, all available such tasks in this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) will be returned. The available tasks are those in the queue having the earliest eta such that eta is prior to the time at which the lease is requested.

It is guaranteed that the leased tasks will be unavailable for lease to others in the lease period. You must call deleteTask to prevent the task from being leased again after the lease period. This method supports leasing a maximum of 1000 tasks for no more than one week. If you generate more than 10 LeaseTasks requests per second, only the first 10 requests will return results. The others will return no results.

**Parameters**  
---  
**Name** | **Description**  
`lease` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Number of `unit`s in the lease period  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
Time unit of the lease period  
`countLimit` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
maximum number of tasks to lease  
`tag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
User defined `String` tag required for returned tasks. If `null`, the tag of the task with earliest eta will be used.  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>` | A list of [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each leased task.  
  
### leaseTasksByTagAsync(long lease, TimeUnit unit, long countLimit, String tag)
    
    
    public abstract Future<List<TaskHandle>> leaseTasksByTagAsync(long lease, TimeUnit unit, long countLimit, String tag)

Asynchronously leases up to `countLimit` tasks from this queue for a period specified by `lease` and `unit`, having tag `tag`. If `tag` is `null`, tasks having the same tag as the task with earliest eta will be returned. If fewer such tasks than `countLimit` are available, all available such tasks in this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) will be returned. The available tasks are those in the queue having the earliest eta such that eta is prior to the time at which the lease is requested.

It is guaranteed that the leased tasks will be unavailable for lease to others in the lease period. You must call deleteTask to prevent the task from being leased again after the lease period. This method supports leasing a maximum of 1000 tasks for no more than one week. If you generate more than 10 LeaseTasks requests per second, only the first 10 requests will return results. The others will return no results.

**Parameters**  
---  
**Name** | **Description**  
`lease` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Number of `unit`s in the lease period  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
Time unit of the lease period  
`countLimit` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
maximum number of tasks to lease  
`tag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
User defined `String` tag required for returned tasks. If `null`, the tag of the task with earliest eta will be used.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>>` | A `Future` whose result is a list of [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each leased task.  
  
### leaseTasksByTagBytes(long lease, TimeUnit unit, long countLimit, byte[] tag)
    
    
    public abstract List<TaskHandle> leaseTasksByTagBytes(long lease, TimeUnit unit, long countLimit, byte[] tag)

Leases up to `countLimit` tasks from this queue for a period specified by `lease` and `unit`, having tag `tag`. If `tag` is `null`, tasks having the same tag as the task with earliest eta will be returned. If fewer such tasks than `countLimit` are available, all available such tasks in this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) will be returned. The available tasks are those in the queue having the earliest eta such that eta is prior to the time at which the lease is requested. It is guaranteed that the leased tasks will be unavailable for lease to others in the lease period. You must call deleteTask to prevent the task from being leased again after the lease period. This method supports leasing a maximum of 1000 tasks for no more than one week. If you generate more than 10 LeaseTasks requests per second, only the first 10 requests will return results. The others will return no results.

**Parameters**  
---  
**Name** | **Description**  
`lease` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Number of `unit`s in the lease period  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
Time unit of the lease period  
`countLimit` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
maximum number of tasks to lease  
`tag` | `byte[]`  
User defined tag required for returned tasks. If `null`, the tag of the task with earliest eta will be used.  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>` | A list of [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each leased task.  
  
### leaseTasksByTagBytesAsync(long lease, TimeUnit unit, long countLimit, byte[] tag)
    
    
    public abstract Future<List<TaskHandle>> leaseTasksByTagBytesAsync(long lease, TimeUnit unit, long countLimit, byte[] tag)

Asynchronously leases up to `countLimit` tasks from this queue for a period specified by `lease` and `unit`, having tag `tag`. If `tag` is `null`, tasks having the same tag as the task with earliest eta will be returned. If fewer such tasks than `countLimit` are available, all available such tasks in this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) will be returned. The available tasks are those in the queue having the earliest eta such that eta is prior to the time at which the lease is requested. It is guaranteed that the leased tasks will be unavailable for lease to others in the lease period. You must call deleteTask to prevent the task from being leased again after the lease period. This method supports leasing a maximum of 1000 tasks for no more than one week. If you generate more than 10 LeaseTasks requests per second, only the first 10 requests will return results. The others will return no results.

**Parameters**  
---  
**Name** | **Description**  
`lease` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Number of `unit`s in the lease period  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
Time unit of the lease period  
`countLimit` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
maximum number of tasks to lease  
`tag` | `byte[]`  
User defined tag required for returned tasks. If `null`, the tag of the task with earliest eta will be used.  
**Returns**  
---  
**Type** | **Description**  
`[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)>>` | A `Future` whose result is a list of [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) for each leased task.  
  
### modifyTaskLease(TaskHandle taskHandle, long lease, TimeUnit unit)
    
    
    public abstract TaskHandle modifyTaskLease(TaskHandle taskHandle, long lease, TimeUnit unit)

Modify the lease of the specified task in this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue) for a period of time specified by `lease` and `unit`. A lease time of 0 will relinquish the lease on the task and make it available to be leased by calling [leaseTasks](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_leaseTasks_com_google_appengine_api_taskqueue_LeaseOptions_).

**Parameters**  
---  
**Name** | **Description**  
`taskHandle` | `[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)`  
handle of the task that is having its lease modified.  
`lease` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Number of `unit`s in the lease period.  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
Time unit of the lease period.  
**Returns**  
---  
**Type** | **Description**  
`[TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle)` | Updated [TaskHandle](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle) with the new lease period.  
  
### purge()
    
    
    public abstract void purge()

Clears all the tasks in this [Queue](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue). This function returns immediately. Some delay may apply on the server before the Queue is actually purged. Tasks being executed at the time the purge call is made will continue executing, other tasks in this Queue will continue being dispatched and executed before the purge call takes effect.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
