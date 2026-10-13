---
url: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException
title: Exception ApiException (2.87.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:22.104310+00:00
---

# Exception ApiException (2.87.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ApiException

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Exception ApiException (2.87.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.87.0 (latest)  2.83.0  2.82.0  2.81.0  2.80.0  2.79.0  2.76.0  2.75.0  2.74.1  2.73.1  2.72.2  2.71.0  2.70.3  2.69.0  2.68.2  2.67.0  2.66.0  2.65.0  2.63.1  2.62.0  2.61.0  2.60.0  2.59.1  2.58.0  2.57.0  2.55.0  2.54.1  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.1  2.47.0  2.46.1  2.45.0  2.43.0  2.42.0  2.41.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.1  2.33.0  2.32.1  2.31.1  2.30.1  2.24.0  2.23.3  2.22.0  2.21.0  2.20.1  2.19.6  2.18.7  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.2  2.11.0  2.10.0  2.9.0  2.8.1  2.7.1 
    
    
    public class ApiException extends RuntimeException

Represents an exception thrown during an RPC call.

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

### ApiException(@Nullable String message, @Nullable Throwable cause, StatusCode statusCode, boolean retryable)
    
    
    public ApiException(@Nullable String message, @Nullable Throwable cause, StatusCode statusCode, boolean retryable)

**Parameters**  
---  
**Name** | **Description**  
`message` | `@org.jspecify.annotations.Nullable java.lang.String`  
  
`cause` | `@org.jspecify.annotations.Nullable java.lang.Throwable`  
  
`statusCode` | `[StatusCode](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StatusCode)`  
  
`retryable` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### ApiException(@Nullable String message, @Nullable Throwable cause, StatusCode statusCode, boolean retryable, @Nullable ErrorDetails errorDetails)
    
    
    public ApiException(@Nullable String message, @Nullable Throwable cause, StatusCode statusCode, boolean retryable, @Nullable ErrorDetails errorDetails)

**Parameters**  
---  
**Name** | **Description**  
`message` | `@org.jspecify.annotations.Nullable java.lang.String`  
  
`cause` | `@org.jspecify.annotations.Nullable java.lang.Throwable`  
  
`statusCode` | `[StatusCode](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StatusCode)`  
  
`retryable` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`errorDetails` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ErrorDetails`  
  
  
### ApiException(@Nullable Throwable cause, StatusCode statusCode, boolean retryable)
    
    
    public ApiException(@Nullable Throwable cause, StatusCode statusCode, boolean retryable)

**Parameters**  
---  
**Name** | **Description**  
`cause` | `@org.jspecify.annotations.Nullable java.lang.Throwable`  
  
`statusCode` | `[StatusCode](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StatusCode)`  
  
`retryable` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### ApiException(@Nullable Throwable cause, StatusCode statusCode, boolean retryable, @Nullable ErrorDetails errorDetails)
    
    
    public ApiException(@Nullable Throwable cause, StatusCode statusCode, boolean retryable, @Nullable ErrorDetails errorDetails)

**Parameters**  
---  
**Name** | **Description**  
`cause` | `@org.jspecify.annotations.Nullable java.lang.Throwable`  
  
`statusCode` | `[StatusCode](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StatusCode)`  
  
`retryable` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`errorDetails` | `@org.jspecify.annotations.Nullable com.google.api.gax.rpc.ErrorDetails`  
  
  
## Methods 

### getDomain()
    
    
    public @Nullable String getDomain()

Returns the logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. e.g. googleapis.com

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable java.lang.String` |   
  
### getErrorDetails()
    
    
    public ErrorDetails getErrorDetails()

Returns all standard error messages that server sends.

**Returns**  
---  
**Type** | **Description**  
`[ErrorDetails](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.ErrorDetails)` |   
  
### getMetadata()
    
    
    public @Nullable Map<String,String> getMetadata()

Returns additional structured details about this exception.

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable java.util.Map<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getReason()
    
    
    public @Nullable String getReason()

Returns the reason of the exception. This is a constant value that identifies the proximate cause of the error. e.g. SERVICE_DISABLED

**Returns**  
---  
**Type** | **Description**  
`@org.jspecify.annotations.Nullable java.lang.String` |   
  
### getStatusCode()
    
    
    public StatusCode getStatusCode()

Returns the status code of the underlying exception.

**Returns**  
---  
**Type** | **Description**  
`[StatusCode](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.rpc.StatusCode)` |   
  
### isRetryable()
    
    
    public boolean isRetryable()

Returns whether the failed request can be retried.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
