---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.MaximumRequestCallbackWaitTimeExceededException
title: Exception Exceptions.MaximumRequestCallbackWaitTimeExceededException (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:59:47.368318+00:00
---

# Exception Exceptions.MaximumRequestCallbackWaitTimeExceededException (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.Exceptions.MaximumRequestCallbackWaitTimeExceededException

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Exception Exceptions.MaximumRequestCallbackWaitTimeExceededException (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public static class Exceptions.MaximumRequestCallbackWaitTimeExceededException extends RuntimeException

The connection was shut down because a callback was not received within the maximum wait time.

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

[Throwable.addSuppressed(Throwable)](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#addSuppressed-java.lang.Throwable-)

[Throwable.fillInStackTrace()](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#fillInStackTrace--)

[Throwable.getCause()](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#getCause--)

[Throwable.getLocalizedMessage()](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#getLocalizedMessage--)

[Throwable.getMessage()](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#getMessage--)

[Throwable.getStackTrace()](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#getStackTrace--)

[Throwable.getSuppressed()](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#getSuppressed--)

[Throwable.initCause(Throwable)](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#initCause-java.lang.Throwable-)

[Throwable.printStackTrace()](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#printStackTrace--)

[Throwable.printStackTrace(PrintStream)](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#printStackTrace-java.io.PrintStream-)

[Throwable.printStackTrace(PrintWriter)](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#printStackTrace-java.io.PrintWriter-)

[Throwable.setStackTrace(StackTraceElement[])](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#setStackTrace-java.lang.StackTraceElement\[\]-)

[Throwable.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html#toString--)

## Constructors 

### MaximumRequestCallbackWaitTimeExceededException(Duration callbackWaitTime, String writerId, Duration callbackWaitTimeLimit) (deprecated)
    
    
    public MaximumRequestCallbackWaitTimeExceededException(Duration callbackWaitTime, String writerId, Duration callbackWaitTimeLimit)

**Parameters**  
---  
**Name** | **Description**  
`callbackWaitTime` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
`writerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`callbackWaitTimeLimit` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
  
### MaximumRequestCallbackWaitTimeExceededException(Duration callbackWaitTime, String writerId, Duration callbackWaitTimeLimit, Instant requestReceivedTime, Instant placedInWaitingQueueTime, Instant placedInInflightQueueTime, List<Instant> dispatchTimes)
    
    
    public MaximumRequestCallbackWaitTimeExceededException(Duration callbackWaitTime, String writerId, Duration callbackWaitTimeLimit, Instant requestReceivedTime, Instant placedInWaitingQueueTime, Instant placedInInflightQueueTime, List<Instant> dispatchTimes)

**Parameters**  
---  
**Name** | **Description**  
`callbackWaitTime` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
`writerId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`callbackWaitTimeLimit` | `[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)`  
  
`requestReceivedTime` | `[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)`  
  
`placedInWaitingQueueTime` | `[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)`  
  
`placedInInflightQueueTime` | `[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)`  
  
`dispatchTimes` | `[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)>`  
  
  
## Methods 

### getCallbackWaitTime()
    
    
    public Duration getCallbackWaitTime()

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)` |   
  
### getCallbackWaitTimeLimit()
    
    
    public Duration getCallbackWaitTimeLimit()

**Returns**  
---  
**Type** | **Description**  
`[Duration](https://docs.oracle.com/javase/8/docs/api/java/time/Duration.html)` |   
  
### getDispatchTimes()
    
    
    public ImmutableList<Instant> getDispatchTimes()

**Returns**  
---  
**Type** | **Description**  
`com.google.common.collect.ImmutableList<[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)>` |   
  
### getPlacedInInflightQueueTime()
    
    
    public Instant getPlacedInInflightQueueTime()

**Returns**  
---  
**Type** | **Description**  
`[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)` |   
  
### getPlacedInWaitingQueueTime()
    
    
    public Instant getPlacedInWaitingQueueTime()

**Returns**  
---  
**Type** | **Description**  
`[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)` |   
  
### getRequestReceivedTime()
    
    
    public Instant getRequestReceivedTime()

**Returns**  
---  
**Type** | **Description**  
`[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)` |   
  
### getWriterId()
    
    
    public String getWriterId()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
