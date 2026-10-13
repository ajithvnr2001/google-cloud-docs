---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.ThreadManager
title: Class ThreadManager (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:06:54.869989+00:00
---

# Class ThreadManager (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.ThreadManager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class ThreadManager (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class ThreadManager

`ThreadManager` exposes a [ThreadFactory](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadFactory.html) that allows App Engine applications to spawn new threads.

Refer to [ this discussion of threads](https://cloud.google.com/appengine/docs/java/runtime#threads) for drawbacks of thread usage and possible alternatives.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > ThreadManager

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

## Static Methods 

### backgroundThreadFactory()
    
    
    public static ThreadFactory backgroundThreadFactory()

Returns a [ThreadFactory](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadFactory.html) that will create threads that are independent of the current request.

This ThreadFactory can currently only be used by backends.

Note that calling ThreadFactory#newThread on the returned instance may throw any of the unchecked exceptions mentioned by [#createBackgroundThread](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.ThreadManager#com_google_appengine_api_ThreadManager_createBackgroundThread_).

**Returns**  
---  
**Type** | **Description**  
`[ThreadFactory](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadFactory.html)` |   
  
### createBackgroundThread(Runnable runnable)
    
    
    public static Thread createBackgroundThread(Runnable runnable)

Create a new [Thread](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html) that executes `runnable` independent of the current request. Calling this method is equivalent to invoking ThreadFactory#newThread on the ThreadFactory returned from [#backgroundThreadFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.ThreadManager#com_google_appengine_api_ThreadManager_backgroundThreadFactory_).

This method can currently only be used by backends.

**Parameter**  
---  
**Name** | **Description**  
`runnable` | `[Runnable](https://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Thread](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html)` |   
  
### createThreadForCurrentRequest(Runnable runnable)
    
    
    public static Thread createThreadForCurrentRequest(Runnable runnable)

Create a new [Thread](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html) that executes `runnable` for the duration of the current request. Calling this method is equivalent to invoking ThreadFactory#newThread on the ThreadFactory returned from [#currentRequestThreadFactory](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.ThreadManager#com_google_appengine_api_ThreadManager_currentRequestThreadFactory_). This thread will be interrupted at the end of the current request and must complete within the request deadline. If it fails to, the instance containing it may be terminated.

**Parameter**  
---  
**Name** | **Description**  
`runnable` | `[Runnable](https://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Thread](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html)` |   
  
### currentRequestThreadFactory()
    
    
    public static ThreadFactory currentRequestThreadFactory()

Returns a [ThreadFactory](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadFactory.html) which will create threads scoped to the current request. These threads will be interrupted at the end of the current request and must complete within the request deadline. If they fail to, the instance containing them may be terminated.

The principal reason to use this method is so that the created threads can make App Engine API calls (`com.google.appengine.api.*`). In general, threads not associated with a request cannot make these API calls.

The returned factory is typically used with a call like java.util.concurrent.Executors#newCachedThreadPool(ThreadFactory). Do not use the [ExecutorService](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutorService.html) returned by this call after the request that created it has completed.

Note that calling ThreadFactory#newThread on the returned instance may throw any of the unchecked exceptions mentioned by [#createBackgroundThread](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.ThreadManager#com_google_appengine_api_ThreadManager_createBackgroundThread_).

**Returns**  
---  
**Type** | **Description**  
`[ThreadFactory](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadFactory.html)` |   
  
### currentRequestThreadFactoryOptional()
    
    
    public static Optional<ThreadFactory> currentRequestThreadFactoryOptional()

Returns an Optional [ThreadFactory](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadFactory.html) which will create threads scoped to the current request. These threads will be interrupted at the end of the current request and must complete within the request deadline. If they fail to, the instance containing them may be terminated.

If this method is not called from an App Engine request thread, returns an empty Optional instance.

The principal reason to use this method is so that the created threads can make App Engine API calls (`com.google.appengine.api.*`). In general, threads not associated with a request cannot make these API calls.

The returned factory is typically used with a call like java.util.concurrent.Executors#newCachedThreadPool(ThreadFactory). Do not use the [ExecutorService](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutorService.html) returned by this call after the request that created it has completed.

Note that calling ThreadFactory#newThread on the returned instance may throw any of the unchecked exceptions mentioned by [#createBackgroundThread](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.ThreadManager#com_google_appengine_api_ThreadManager_createBackgroundThread_).

**Returns**  
---  
**Type** | **Description**  
`[Optional](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html)<[ThreadFactory](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadFactory.html)>` |   
  
## Constructors 

### ThreadManager()
    
    
    public ThreadManager()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
