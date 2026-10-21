---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions
title: Class TaskOptions (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:46:55.314438+00:00
---

# Class TaskOptions (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class TaskOptions (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class TaskOptions implements Serializable

Contains various options for a task following the builder pattern. Calls to [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) methods may be chained to specify multiple options in the one [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) object.

taskOptions can have either [TaskOptions.Method](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Method) PULL or a PUSH-related method, e.g. POST, GET, ... Tasks with PULL method can only be added into a PULL queue and PUSH tasks can only be added into a PUSH queue.

Notes on usage:  
The recommended way to instantiate a [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions) object is to statically import Builder.* and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import static com.google.appengine.api.taskqueue.TaskOptions.Builder.*;
    
     ...
     [QueueFactory#getDefaultQueue()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueFactory#com_google_appengine_api_taskqueue_QueueFactory_getDefaultQueue__).add(withUrl(url).etaMillis(eta));
     

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TaskOptions

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Constructors 

### TaskOptions(TaskOptions options)
    
    
    public TaskOptions(TaskOptions options)

A copy constructor for [TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions).

**Parameter**  
---  
**Name** | **Description**  
`options` | `[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)`  
  
  
## Methods 

### clearParams()
    
    
    public TaskOptions clearParams()

Clears the parameters.

**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### countdownMillis(long countdownMillis)
    
    
    public TaskOptions countdownMillis(long countdownMillis)

Set the number of milliseconds delay before execution of the task.

**Parameter**  
---  
**Name** | **Description**  
`countdownMillis` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### dispatchDeadline(Duration dispatchDeadline)
    
    
    public TaskOptions dispatchDeadline(Duration dispatchDeadline)

Sets the dispatch deadline for a task. The dispatch deadline should be no smaller than TaskOptions#MIN_DISPATCH_DEADLINE and no larger than TaskOptions#MAX_DISPATCH_DEADLINE.

**Parameter**  
---  
**Name** | **Description**  
`dispatchDeadline` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### equals(Object obj)
    
    
    public boolean equals(Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### etaMillis(long etaMillis)
    
    
    public TaskOptions etaMillis(long etaMillis)

Sets the approximate absolute time to execute. (i.e. etaMillis is comparable with System#currentTimeMillis()).

**Parameter**  
---  
**Name** | **Description**  
`etaMillis` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### getByteArrayParams()
    
    
    public Map<String,List<byte[]>> getByteArrayParams()

Returns a copy of the task's byte-array-valued parameters as a map from each parameter name to a list of values for that name.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<byte[]>>` |   
  
### getCountdownMillis()
    
    
    public Long getCountdownMillis()

Returns the delay to apply to the submitted time. May be `null`.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getDispatchDeadline()
    
    
    public @Nullable Duration getDispatchDeadline()

Returns the dispatch deadline for a task. The dispatch deadline determines how long the of a task should take. If a task exceeds its deadline, it will be canceled and retried based on retry configurations of the task and/or queue.

**Returns**  
---  
**Type** | **Description**  
`[Nullable Duration](https://docs.oracle.com/javase/8/docs/api/java/time/@org/jspecify/annotations/Nullable%20Duration.html)` |   
  
### getEtaMillis()
    
    
    public Long getEtaMillis()

Returns the specified ETA for a task. May be `null` if not specified.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` |   
  
### getHeaders()
    
    
    public Map<String,List<String>> getHeaders()

Returns a copy of the task's headers as a map from each header name to a list of values for that header name.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>>` |   
  
### getMethod()
    
    
    public TaskOptions.Method getMethod()

Returns the method used for this task.

**Returns**  
---  
**Type** | **Description**  
`[TaskOptions.Method](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Method)` |   
  
### getPayload()
    
    
    public byte[] getPayload()

Returns the live payload for the task, not a copy. May be `null`.

**Returns**  
---  
**Type** | **Description**  
`byte[]` |   
  
### getRetryOptions()
    
    
    public RetryOptions getRetryOptions()

Returns a copy of the retry options for a task. May be `null` if not specified.

**Returns**  
---  
**Type** | **Description**  
`[RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions)` |   
  
### getStringParams()
    
    
    public Map<String,List<String>> getStringParams()

Returns a copy of the task's string-valued parameters as a map from each parameter name to a list of values for that name.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>>` |   
  
### getTag()
    
    
    public String getTag()

Returns the tag for a task. May be `null` if tag is not specified.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Exceptions**  
---  
**Type** | **Description**  
`[UnsupportedEncodingException](https://docs.oracle.com/javase/8/docs/api/java/io/UnsupportedEncodingException.html)` |   
  
### getTagAsBytes()
    
    
    public byte[] getTagAsBytes()

Returns the live tag bytes for a task, not a copy. May be `null` if tag is not specified.

**Returns**  
---  
**Type** | **Description**  
`byte[]` |   
  
### getTaskName()
    
    
    public String getTaskName()

Returns the task name.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getUrl()
    
    
    public String getUrl()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### header(String headerName, String value)
    
    
    public TaskOptions header(String headerName, String value)

Adds a header `name/value` pair.

**Parameters**  
---  
**Name** | **Description**  
`headerName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### headers(Map<String,String> headers)
    
    
    public TaskOptions headers(Map<String,String> headers)

Replaces the existing headers with the provided header `name/value` mapping.

**Parameter**  
---  
**Name** | **Description**  
`headers` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
The headers to copy.  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` | TaskOptions object for chaining.  
  
### method(TaskOptions.Method method)
    
    
    public TaskOptions method(TaskOptions.Method method)

Set the method used for this task. Defaults to Method#POST.

**Parameter**  
---  
**Name** | **Description**  
`method` | `[TaskOptions.Method](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions.Method)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### param(String name, byte[] value)
    
    
    public TaskOptions param(String name, byte[] value)

Add a named `byte` array parameter.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the parameter. Must not be null or empty.  
`value` | `byte[]`  
A byte array and encoded as-is (i.e. without character encoding transformations). `value` must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### param(String name, String value)
    
    
    public TaskOptions param(String name, String value)

Add a named [String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html) parameter.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the parameter. Must not be null or empty.  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The value of the parameter will undergo a "UTF-8" character encoding transformation upon being added to the queue. `value` must not be `null`.  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### payload(byte[] payload)
    
    
    public TaskOptions payload(byte[] payload)

Sets the payload directly without specifying the content-type. If this task is added to a push queue, the content-type will be set to 'application/octet-stream' by default.

**Parameter**  
---  
**Name** | **Description**  
`payload` | `byte[]`  
The bytes representing the paylaod.  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` | TaskOptions object for chaining.  
  
### payload(byte[] payload, String contentType)
    
    
    public TaskOptions payload(byte[] payload, String contentType)

Set the payload with the given content type.

**Parameters**  
---  
**Name** | **Description**  
`payload` | `byte[]`  
The bytes representing the paylaod.  
`contentType` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The content-type of the bytes.  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` | TaskOptions object for chaining.  
  
### payload(DeferredTask deferredTask)
    
    
    public TaskOptions payload(DeferredTask deferredTask)

Sets the payload to the serialized form of the deferredTask object. The payload will be generated by serializing the deferredTask object using ObjectOutputStream#writeObject(Object). If the deferredTask's Method is not PULL, the content type will be set to [DeferredTaskContext#RUNNABLE_TASK_CONTENT_TYPE](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTaskContext#com_google_appengine_api_taskqueue_DeferredTaskContext_RUNNABLE_TASK_CONTENT_TYPE), the method will be forced to Method#POST and if otherwise not specified, the url will be set to [DeferredTaskContext#DEFAULT_DEFERRED_URL](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTaskContext#com_google_appengine_api_taskqueue_DeferredTaskContext_DEFAULT_DEFERRED_URL); the [DeferredTask](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTask) servlet is, by default, mapped to this url.

Note: While this may be a convenient API, it requires careful control of the serialization compatibility of objects passed into [#payload(DeferredTask)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions#com_google_appengine_api_taskqueue_TaskOptions_payload_com_google_appengine_api_taskqueue_DeferredTask_) method as objects placed in the task queue will survive revision updates of the application and hence may fail deserialization when the task is decoded with new revisions of the application. In particular, Java anonymous classes are convenient but may be particularly difficult to control or test for serialization compatibility.

**Parameter**  
---  
**Name** | **Description**  
`deferredTask` | `[DeferredTask](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTask)`  
The object to serialize into the payload.  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### payload(String payload)
    
    
    public TaskOptions payload(String payload)

Set the payload by [String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html). The charset to convert the String to will be UTF-8 unless the method is PULL, in which case the String's bytes will be used directly.

**Parameter**  
---  
**Name** | **Description**  
`payload` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The String to be used.  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` | TaskOptions object for chaining.  
  
### payload(String payload, String charset)
    
    
    public TaskOptions payload(String payload, String charset)

Sets the payload from a [String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html) given a specific character set.

**Parameters**  
---  
**Name** | **Description**  
`payload` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`charset` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### removeHeader(String headerName)
    
    
    public TaskOptions removeHeader(String headerName)

Remove all headers with the given name.

**Parameter**  
---  
**Name** | **Description**  
`headerName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### removeParam(String paramName)
    
    
    public TaskOptions removeParam(String paramName)

Remove all parameters with the given name.

**Parameter**  
---  
**Name** | **Description**  
`paramName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
Name of the parameter. Must not be null or empty.  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### retryOptions(RetryOptions retryOptions)
    
    
    public TaskOptions retryOptions(RetryOptions retryOptions)

Sets retry options for this task. Retry Options must be built with ` RetryOptions.Builder`.

**Parameter**  
---  
**Name** | **Description**  
`retryOptions` | `[RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### tag(byte[] tag)
    
    
    public TaskOptions tag(byte[] tag)

Sets the tag for a task. Ignores null or zero-length tags.

**Parameter**  
---  
**Name** | **Description**  
`tag` | `byte[]`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### tag(String tag)
    
    
    public TaskOptions tag(String tag)

Sets the tag for a task. Ignores null or empty tags.

**Parameter**  
---  
**Name** | **Description**  
`tag` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### taskName(String taskName)
    
    
    public TaskOptions taskName(String taskName)

Sets the task name.

**Parameter**  
---  
**Name** | **Description**  
`taskName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

### url(String url)
    
    
    public TaskOptions url(String url)

Set the URL.

Default value is `null`.

**Parameter**  
---  
**Name** | **Description**  
`url` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
String containing URL.  
**Returns**  
---  
**Type** | **Description**  
`[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
