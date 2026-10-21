---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FutureHelper
title: Class FutureHelper (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:07:59.826885+00:00
---

# Class FutureHelper (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.FutureHelper

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class FutureHelper (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class FutureHelper

Utilities for working with [Futures](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html) in the synchronous datastore api.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > FutureHelper

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

### <T,E>quietGet(Future<T> future, Class<E> exceptionClass)
    
    
    public static T <T,E>quietGet(Future<T> future, Class<E> exceptionClass)

Return the result of the provided [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html), converting all checked exceptions except those of the provided type to unchecked exceptions so the caller doesn't have to handle them. If an ExecutionException is thrown and the type of the cause does not equal `exceptionClass` the cause is wrapped in a [RuntimeException](https://docs.oracle.com/javase/8/docs/api/java/lang/RuntimeException.html). If the type of the cause does equal `exceptionClass` the cause itself is thrown. If an InterruptedException is thrown it is wrapped in a [DatastoreFailureException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreFailureException).

**Parameters**  
---  
**Name** | **Description**  
`future` | `[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<T>`  
The Future whose result we want to return.  
`exceptionClass` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<E>`  
Exceptions of this type will be rethrown.  
**Returns**  
---  
**Type** | **Description**  
`T` | The result of the provided Future.  
**Exceptions**  
---  
**Type** | **Description**  
`E` | Thrown If an ExecutionException with a cause of the appropriate type is caught.  
  
### <T>quietGet(Future<T> future)
    
    
    public static T <T>quietGet(Future<T> future)

Return the result of the provided [Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html), converting all checked exceptions to unchecked exceptions so the caller doesn't have to handle them. If an ExecutionException is thrown the cause is wrapped in a [RuntimeException](https://docs.oracle.com/javase/8/docs/api/java/lang/RuntimeException.html). If an InterruptedException is thrown it is wrapped in a [DatastoreFailureException](https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.datastore.DatastoreFailureException).

**Parameter**  
---  
**Name** | **Description**  
`future` | `[Future](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/Future.html)<T>`  
The Future whose result we want to return.  
**Returns**  
---  
**Type** | **Description**  
`T` | The result of the provided Future.  
  
## Constructors 

### FutureHelper()
    
    
    public FutureHelper()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
