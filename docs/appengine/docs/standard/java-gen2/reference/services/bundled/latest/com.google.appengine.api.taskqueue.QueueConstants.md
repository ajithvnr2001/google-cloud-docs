---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueConstants
title: Class QueueConstants (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:45:35.225227+00:00
---

# Class QueueConstants (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueConstants

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class QueueConstants (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class QueueConstants

Describes various taskqueue limits.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > QueueConstants

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

## Static Fields 

### QUEUE_NAME_PATTERN
    
    
    public static final Pattern QUEUE_NAME_PATTERN

**Field Value**  
---  
**Type** | **Description**  
`[Pattern](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html)` |   
  
### QUEUE_NAME_REGEX
    
    
    public static final String QUEUE_NAME_REGEX

Regular expression that matches all valid queue names.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### TASK_NAME_PATTERN
    
    
    public static final Pattern TASK_NAME_PATTERN

**Field Value**  
---  
**Type** | **Description**  
`[Pattern](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Pattern.html)` |   
  
### TASK_NAME_REGEX
    
    
    public static final String TASK_NAME_REGEX

Regular expression that matches all valid task names.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### getMaxEtaDeltaMillis()
    
    
    public static long getMaxEtaDeltaMillis()

Returns the maximum time into the future that a task may be scheduled.

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### maxLease(TimeUnit unit)
    
    
    public static long maxLease(TimeUnit unit)

Returns the maximum length of period to lease a task.

**Parameter**  
---  
**Name** | **Description**  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### maxLeaseCount()
    
    
    public static long maxLeaseCount()

Returns the maximum number of tasks to lease in one call.

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### maxPullTaskSizeBytes()
    
    
    public static int maxPullTaskSizeBytes()

Returns the maximum pull task size.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### maxPushTaskSizeBytes()
    
    
    public static int maxPushTaskSizeBytes()

Returns the maximum push task size.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### maxQueueNameLength()
    
    
    public static int maxQueueNameLength()

Returns the maximum length of a queue name.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### maxTaskNameLength()
    
    
    public static int maxTaskNameLength()

Returns the maximum length of a task name.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### maxTaskSizeBytes() (deprecated)
    
    
    public static int maxTaskSizeBytes()

**Deprecated.** _Use[#maxPushTaskSizeBytes()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueConstants#com_google_appengine_api_taskqueue_QueueConstants_maxPushTaskSizeBytes__)_

Returns the maximum push task size.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### maxTaskTagLength()
    
    
    public static int maxTaskTagLength()

Returns the maximum length of a task tag.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### maxTasksPerAdd()
    
    
    public static int maxTasksPerAdd()

Returns the maximum number of tasks that may be passed to a single add call.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### maxUrlLength()
    
    
    public static int maxUrlLength()

Returns the maximum URL length.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
