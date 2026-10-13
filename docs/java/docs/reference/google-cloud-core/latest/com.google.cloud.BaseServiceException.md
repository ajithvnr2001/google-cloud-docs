---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.BaseServiceException
title: Exception BaseServiceException (2.77.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:03.679221+00:00
---

# Exception BaseServiceException (2.77.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.BaseServiceException

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Exception BaseServiceException (2.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.77.0 (latest)  2.73.0  2.72.0  2.71.0  2.70.0  2.69.0  2.66.0  2.65.0  2.64.1  2.63.1  2.62.2  2.61.0  2.60.3  2.59.0  2.58.2  2.57.0  2.56.0  2.55.0  2.53.1  2.52.0  2.51.0  2.50.0  2.49.1  2.48.0  2.47.0  2.45.0  2.44.1  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.1  2.37.0  2.36.1  2.35.0  2.33.0  2.32.0  2.31.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.1  2.23.0  2.22.1  2.21.1  2.20.1  2.13.0  2.12.0  2.11.0  2.9.4  2.8.27  2.7.1  2.6.1  2.5.11  2.4.0  2.3.5 
    
    
    public class BaseServiceException extends RuntimeException

Base class for all service exceptions.

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

## Static Fields 

### UNKNOWN_CODE
    
    
    public static final int UNKNOWN_CODE

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### isRetryable(boolean idempotent, IOException exception)
    
    
    public static boolean isRetryable(boolean idempotent, IOException exception)

**Internal Only** : This feature is not stable for application use.

**Parameters**  
---  
**Name** | **Description**  
`idempotent` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`exception` | `[IOException](https://docs.oracle.com/javase/8/docs/api/java/io/IOException.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### isRetryable(Integer code, String reason, boolean idempotent, Set<BaseServiceException.Error> retryableErrors)
    
    
    public static boolean isRetryable(Integer code, String reason, boolean idempotent, Set<BaseServiceException.Error> retryableErrors)

**Internal Only** : This feature is not stable for application use.

**Parameters**  
---  
**Name** | **Description**  
`code` | `[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)`  
  
`reason` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`idempotent` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`retryableErrors` | `[Set](https://docs.oracle.com/javase/8/docs/api/java/util/Set.html)<[Error](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.BaseServiceException.Error)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### translate(RetryHelper.RetryHelperException ex)
    
    
    public static void translate(RetryHelper.RetryHelperException ex)

**Internal Only** : This feature is not stable for application use.

**Parameter**  
---  
**Name** | **Description**  
`ex` | `[RetryHelper.RetryHelperException](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.RetryHelper.RetryHelperException)`  
  
  
### translate(ExecutionException ex)
    
    
    public static void translate(ExecutionException ex)

**Internal Only** : This feature is not stable for application use.

**Parameter**  
---  
**Name** | **Description**  
`ex` | `[ExecutionException](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/ExecutionException.html)`  
  
  
## Constructors 

### BaseServiceException(BaseServiceException.ExceptionData exceptionData)
    
    
    protected BaseServiceException(BaseServiceException.ExceptionData exceptionData)

**Internal Only** : This feature is not stable for application use.

_This class should only be extended within google-cloud-java_

**Parameter**  
---  
**Name** | **Description**  
`exceptionData` | `[BaseServiceException.ExceptionData](https://docs.cloud.google.com/java/docs/reference/google-cloud-core/latest/com.google.cloud.BaseServiceException.ExceptionData)`  
  
  
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

### getCode()
    
    
    public int getCode()

Returns the code associated with this exception.

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDebugInfo()
    
    
    public String getDebugInfo()

**Internal Only** : This feature is not stable for application use.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLocation()
    
    
    public String getLocation()

Returns the service location where the error causing the exception occurred. Returns ` null` if not available.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getReason()
    
    
    public String getReason()

Returns the reason that caused the exception.

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

### isRetryable()
    
    
    public boolean isRetryable()

Returns `true` when it is safe to retry the operation that caused this exception.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
