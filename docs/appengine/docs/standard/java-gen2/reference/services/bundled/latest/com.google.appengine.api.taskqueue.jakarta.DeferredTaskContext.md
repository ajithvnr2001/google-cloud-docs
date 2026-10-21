---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.jakarta.DeferredTaskContext
title: Class DeferredTaskContext (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:46:27.264238+00:00
---

# Class DeferredTaskContext (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.jakarta.DeferredTaskContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class DeferredTaskContext (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class DeferredTaskContext

Resources for managing [com.google.appengine.api.taskqueue.DeferredTask](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTask).

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DeferredTaskContext

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

### DEFAULT_DEFERRED_URL
    
    
    public static final String DEFAULT_DEFERRED_URL

The URL the DeferredTask servlet is mapped to by default.

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### RUNNABLE_TASK_CONTENT_TYPE
    
    
    public static final String RUNNABLE_TASK_CONTENT_TYPE

The content type of a serialized [com.google.appengine.api.taskqueue.DeferredTask](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.DeferredTask).

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
## Static Methods 

### getCurrentRequest()
    
    
    public static HttpServletRequest getCurrentRequest()

Returns the HttpServletRequest instance for the current running deferred task for the current thread or `null` if there is no current deferred task active for this thread.

**Returns**  
---  
**Type** | **Description**  
`jakarta.servlet.http.HttpServletRequest` |   
  
### getCurrentResponse()
    
    
    public static HttpServletResponse getCurrentResponse()

Returns the HttpServletResponse instance for the current running deferred task for the current thread or `null` if there is no current deferred task active for this thread.

**Returns**  
---  
**Type** | **Description**  
`jakarta.servlet.http.HttpServletResponse` |   
  
### getCurrentServlet()
    
    
    public static HttpServlet getCurrentServlet()

Returns the HttpServlet instance for the current running deferred task for the current thread or `null` if there is no current deferred task active for this thread.

**Returns**  
---  
**Type** | **Description**  
`jakarta.servlet.http.HttpServlet` |   
  
### markForRetry()
    
    
    public static void markForRetry()

Request a retry of this task, even if an exception was not thrown. If an exception was thrown and [#setDoNotRetry](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.taskqueue.jakarta.DeferredTaskContext#com_google_appengine_api_taskqueue_jakarta_DeferredTaskContext_setDoNotRetry_) is set to `true` the request will not be retried.

### setDoNotRetry(boolean value)
    
    
    public static void setDoNotRetry(boolean value)

Sets the action on task failure. Normally when an exception is thrown, the task will be retried, however if `setDoNotRetry` is set to `true`, the task will not be retried.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
