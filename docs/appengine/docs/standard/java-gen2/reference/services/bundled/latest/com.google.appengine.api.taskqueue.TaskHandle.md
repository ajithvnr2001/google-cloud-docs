---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle
title: Class TaskHandle (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:44:52.710587+00:00
---

# Class TaskHandle (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class TaskHandle (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class TaskHandle implements Serializable

Created from [Queue#add(TaskOptions)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_add_com_google_appengine_api_taskqueue_TaskOptions_). Contains the task name (generated if otherwise unspecified), task ETA (computed if not specified) and queue name. The queue name and task name uniquely identify the task for an application.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TaskHandle

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

### TaskHandle(TaskOptions options, String queueName)
    
    
    public TaskHandle(TaskOptions options, String queueName)

**Parameters**  
---  
**Name** | **Description**  
`options` | `[TaskOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskOptions)`  
  
`queueName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
### TaskHandle(String name, String queueName, long etaMillis) (deprecated)
    
    
    public TaskHandle(String name, String queueName, long etaMillis)

**Deprecated.** _Use[TaskHandle#TaskHandle(TaskOptions, String)](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.TaskHandle#com_google_appengine_api_taskqueue_TaskHandle_TaskHandle_com_google_appengine_api_taskqueue_TaskOptions_java_lang_String_)_

**Parameters**  
---  
**Name** | **Description**  
`name` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`queueName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`etaMillis` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
## Methods 

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

### extractParams()
    
    
    public List<Map.Entry<String,String>> extractParams()

Attempts to decode the `payload` byte array in our `options` into a list of ` Map.Entry<String, String>`.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Entry](https://docs.oracle.com/javase/8/docs/api/java/util/Map/Entry.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>>` |   
**Exceptions**  
---  
**Type** | **Description**  
`[UnsupportedEncodingException](https://docs.oracle.com/javase/8/docs/api/java/io/UnsupportedEncodingException.html)` | if the payload cannot be decoded as a ` application/x-www-form-urlencoded` string.  
`[UnsupportedOperationException](https://docs.oracle.com/javase/8/docs/api/java/lang/UnsupportedOperationException.html)` | if the payload cannot be decoded as a ` application/x-www-form-urlencoded` string.  
  
### getEtaMillis()
    
    
    public long getEtaMillis()

Returns a time comparable to System#currentTimeMillis() when this task is scheduled for execution.

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getName()
    
    
    public String getName()

Returns the name of this task. This may have been generated by a call to [Queue#add()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.Queue#com_google_appengine_api_taskqueue_Queue_add__) if the name was not otherwise specified.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getPayload()
    
    
    public byte[] getPayload()

Returns binary payload data of this task. Can return `null`.

**Returns**  
---  
**Type** | **Description**  
`byte[]` |   
  
### getQueueName()
    
    
    public String getQueueName()

Returns the name of the queue that this task was submitted into.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getRetryCount()
    
    
    public Integer getRetryCount()

Returns number of leases that had been performed on this task. Can return `null`.

**Returns**  
---  
**Type** | **Description**  
`[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)` |   
  
### getTag()
    
    
    public String getTag()

Returns tag of this task. Can return `null`.

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

Returns tag of this task. Can return `null`.

**Returns**  
---  
**Type** | **Description**  
`byte[]` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
