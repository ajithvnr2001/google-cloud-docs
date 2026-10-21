---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.RequestThreadFactory
title: Class RequestThreadFactory (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:12:13.073586+00:00
---

# Class RequestThreadFactory (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.setup.RequestThreadFactory

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class RequestThreadFactory (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class RequestThreadFactory implements ThreadFactory

Thread factory creating threads with a request specific thread local environment.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > RequestThreadFactory

## Implements

[ThreadFactory](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ThreadFactory.html)

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

### RequestThreadFactory(ApiProxy.Environment requestEnvironment)
    
    
    public RequestThreadFactory(ApiProxy.Environment requestEnvironment)

Create a new VmRequestThreadFactory.

**Parameter**  
---  
**Name** | **Description**  
`requestEnvironment` | `[Environment](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.apphosting.api.ApiProxy.Environment)`  
The request environment to install on each thread.  
  
## Methods 

### getRequestThreads()
    
    
    public List<Thread> getRequestThreads()

Returns an immutable copy of the current request thread list.

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Thread](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html)>` |   
  
### newThread(Runnable runnable)
    
    
    public Thread newThread(Runnable runnable)

Create a new [Thread](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html) that executes `runnable` for the duration of the current request. This thread will be interrupted at the end of the current request.

**Parameter**  
---  
**Name** | **Description**  
`runnable` | `[Runnable](https://docs.oracle.com/javase/8/docs/api/java/lang/Runnable.html)`  
The object whose run method is invoked when this thread is started. If null, this classes run method does nothing.  
**Returns**  
---  
**Type** | **Description**  
`[Thread](https://docs.oracle.com/javase/8/docs/api/java/lang/Thread.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
