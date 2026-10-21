---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions
title: Class RetryOptions (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:13:34.222393+00:00
---

# Class RetryOptions (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class RetryOptions (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class RetryOptions implements Serializable

Contains various options for a task's retry strategy. Calls to [RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions) methods may be chained to specify multiple options in the one [RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions) object.

Notes on usage:  
The recommended way to instantiate a [RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions) object is to statically import Builder.* and invoke a static creation method followed by an instance mutator (if needed):
    
    
     import static com.google.appengine.api.taskqueue.RetryOptions.Builder.*;
    
     ...
     RetryOptions retry = withTaskRetryLimit(10).taskAgeLimitSeconds("4d")
         .minBackoffSeconds(120).maxBackoffSeconds(3600).maxDoublings(5);
     [QueueFactory#getDefaultQueue()](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.QueueFactory#com_google_appengine_api_taskqueue_QueueFactory_getDefaultQueue__).add(retryOptions(retry));
     

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RetryOptions

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

### RetryOptions(RetryOptions options)
    
    
    public RetryOptions(RetryOptions options)

**Parameter**  
---  
**Name** | **Description**  
`options` | `[RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions)`  
  
  
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

### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### maxBackoffSeconds(double maxBackoffSeconds)
    
    
    public RetryOptions maxBackoffSeconds(double maxBackoffSeconds)

Sets the maximum retry backoff interval, in seconds.

**Parameter**  
---  
**Name** | **Description**  
`maxBackoffSeconds` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Seconds value for the maximum backoff interval.  
**Returns**  
---  
**Type** | **Description**  
`[RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions)` | the RetryOptions object for chaining.  
  
### maxDoublings(int maxDoublings)
    
    
    public RetryOptions maxDoublings(int maxDoublings)

Sets the maximum times the retry backoff interval should double before rising linearly to the maximum.

**Parameter**  
---  
**Name** | **Description**  
`maxDoublings` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The number of allowed doublings. Must not be negative.  
**Returns**  
---  
**Type** | **Description**  
`[RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions)` | the RetryOptions object for chaining.  
  
### minBackoffSeconds(double minBackoffSeconds)
    
    
    public RetryOptions minBackoffSeconds(double minBackoffSeconds)

Sets the minimum retry backoff interval, in seconds.

**Parameter**  
---  
**Name** | **Description**  
`minBackoffSeconds` | `[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
Seconds value for the minimum backoff interval.  
**Returns**  
---  
**Type** | **Description**  
`[RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions)` | the RetryOptions object for chaining.  
  
### taskAgeLimitSeconds(long taskAgeLimitSeconds)
    
    
    public RetryOptions taskAgeLimitSeconds(long taskAgeLimitSeconds)

Sets the maximum age from the first attempt to execute a task after which any new task failure can be permanent. If both taskRetryLimit and taskAgeLimitSeconds are specified, then both limits must be exceeded before a task can fail permanently.

**Parameter**  
---  
**Name** | **Description**  
`taskAgeLimitSeconds` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The age limit in seconds. Must not be negative.  
**Returns**  
---  
**Type** | **Description**  
`[RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions)` | the RetryOptions object for chaining.  
  
### taskRetryLimit(int taskRetryLimit)
    
    
    public RetryOptions taskRetryLimit(int taskRetryLimit)

Sets the number of retries allowed before a task can fail permanently. If both taskRetryLimit and taskAgeLimitSeconds are specified, then both limits must be exceeded before a task can fail permanently.

**Parameter**  
---  
**Name** | **Description**  
`taskRetryLimit` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RetryOptions](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.RetryOptions)` |   
  
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
