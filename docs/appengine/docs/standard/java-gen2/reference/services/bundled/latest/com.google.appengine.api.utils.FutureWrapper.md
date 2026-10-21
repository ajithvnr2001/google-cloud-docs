---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.FutureWrapper
title: Class FutureWrapper<K,V> (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:47:53.146299+00:00
---

# Class FutureWrapper<K,V> (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.utils.FutureWrapper

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class FutureWrapper<K,V> (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public abstract class FutureWrapper<K,V> implements Future<V>

`FutureWrapper` is a simple [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) that wraps a parent `Future`. This class is thread-safe.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FutureWrapper<K,V>

## Implements

[Future<V>](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future<V>.html)

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

## Type Parameters  
  
---  
**Name** | **Description**  
`K` |   
`V` |   
  
## Constructors 

### FutureWrapper(Future<K> parent)
    
    
    public FutureWrapper(Future<K> parent)

**Parameter**  
---  
**Name** | **Description**  
`parent` | `[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<K>`  
  
  
## Methods 

### absorbParentException(Throwable cause)
    
    
    protected V absorbParentException(Throwable cause)

Override this method if you want to suppress an exception thrown by the parent and return a value instead.

**Parameter**  
---  
**Name** | **Description**  
`cause` | `[Throwable](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`V` |   
**Exceptions**  
---  
**Type** | **Description**  
`[Throwable](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html)` |   
  
### cancel(boolean mayInterruptIfRunning)
    
    
    public boolean cancel(boolean mayInterruptIfRunning)

**Parameter**  
---  
**Name** | **Description**  
`mayInterruptIfRunning` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### convertException(Throwable cause)
    
    
    protected abstract Throwable convertException(Throwable cause)

**Parameter**  
---  
**Name** | **Description**  
`cause` | `[Throwable](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Throwable](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html)` |   
  
### equals(@Nullable Object obj)
    
    
    public final boolean equals(@Nullable Object obj)

**Parameter**  
---  
**Name** | **Description**  
`obj` | `[Nullable Object](https://docs.oracle.com/javase/8/docs/api/java/lang/@org/jspecify/annotations/Nullable%20Object.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

### get()
    
    
    public V get()

**Returns**  
---  
**Type** | **Description**  
`V` |   
**Exceptions**  
---  
**Type** | **Description**  
`[ExecutionException](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutionException.html)` |   
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
  
### get(long timeout, TimeUnit unit)
    
    
    public V get(long timeout, TimeUnit unit)

**Parameters**  
---  
**Name** | **Description**  
`timeout` | `[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`unit` | `[TimeUnit](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeUnit.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`V` |   
**Exceptions**  
---  
**Type** | **Description**  
`[InterruptedException](https://docs.oracle.com/javase/8/docs/api/java/lang/InterruptedException.html)` |   
`[TimeoutException](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/TimeoutException.html)` |   
`[ExecutionException](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutionException.html)` |   
  
### hashCode()
    
    
    public final int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### isCancelled()
    
    
    public boolean isCancelled()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isDone()
    
    
    public boolean isDone()

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### wrap(@Nullable K key)
    
    
    protected abstract V wrap(@Nullable K key)

**Parameter**  
---  
**Name** | **Description**  
`key` | `@org.jspecify.annotations.Nullable K`  
  
**Returns**  
---  
**Type** | **Description**  
`V` |   
**Exceptions**  
---  
**Type** | **Description**  
`[Exception](https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
