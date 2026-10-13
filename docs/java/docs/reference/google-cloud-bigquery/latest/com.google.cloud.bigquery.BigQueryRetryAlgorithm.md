---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryRetryAlgorithm
title: Class BigQueryRetryAlgorithm<ResponseT> (2.73.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:38.729937+00:00
---

# Class BigQueryRetryAlgorithm<ResponseT> (2.73.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryRetryAlgorithm

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BigQueryRetryAlgorithm<ResponseT> (2.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.73.0 (latest)  2.69.0  2.68.0  2.67.0  2.65.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.2  2.56.0  2.55.3  2.54.2  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.1  2.47.0  2.46.0  2.45.0  2.44.0  2.43.3  2.42.3  2.41.0  2.40.3  2.39.1  2.38.2  2.37.2  2.36.0  2.35.0  2.34.2  2.33.2 
    
    
    public class BigQueryRetryAlgorithm<ResponseT> extends RetryAlgorithm<ResponseT>

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > [RetryAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetryAlgorithm.html) > BigQueryRetryAlgorithm<ResponseT>

## Inherited Members

[RetryAlgorithm.createFirstAttempt()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetryAlgorithm.html#com_google_api_gax_retrying_RetryAlgorithm_createFirstAttempt__)

com.google.api.gax.retrying.RetryAlgorithm.createFirstAttempt(com.google.api.gax.retrying.RetryingContext)

com.google.api.gax.retrying.RetryAlgorithm.createNextAttempt(com.google.api.gax.retrying.RetryingContext,java.lang.Throwable,ResponseT,com.google.api.gax.retrying.TimedAttemptSettings)

[RetryAlgorithm.createNextAttempt(Throwable,ResponseT,TimedAttemptSettings)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetryAlgorithm.html#com_google_api_gax_retrying_RetryAlgorithm_createNextAttempt_java_lang_Throwable_ResponseT_com_google_api_gax_retrying_TimedAttemptSettings_)

[RetryAlgorithm.getResultAlgorithm()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetryAlgorithm.html#com_google_api_gax_retrying_RetryAlgorithm_getResultAlgorithm__)

[RetryAlgorithm.getTimedAlgorithm()](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetryAlgorithm.html#com_google_api_gax_retrying_RetryAlgorithm_getTimedAlgorithm__)

com.google.api.gax.retrying.RetryAlgorithm.shouldRetry(com.google.api.gax.retrying.RetryingContext,java.lang.Throwable,ResponseT,com.google.api.gax.retrying.TimedAttemptSettings)

[RetryAlgorithm.shouldRetry(Throwable,ResponseT,TimedAttemptSettings)](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetryAlgorithm.html#com_google_api_gax_retrying_RetryAlgorithm_shouldRetry_java_lang_Throwable_ResponseT_com_google_api_gax_retrying_TimedAttemptSettings_)

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

## Type Parameter  
  
---  
**Name** | **Description**  
`ResponseT` |   
  
## Static Methods 

### matchRegEx(String retriableRegEx, String errorDesc)
    
    
    public static boolean matchRegEx(String retriableRegEx, String errorDesc)

**Parameters**  
---  
**Name** | **Description**  
`retriableRegEx` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`errorDesc` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Constructors 

### BigQueryRetryAlgorithm(ResultRetryAlgorithm<ResponseT> resultAlgorithm, TimedRetryAlgorithm timedAlgorithm, BigQueryRetryConfig bigQueryRetryConfig)
    
    
    public BigQueryRetryAlgorithm(ResultRetryAlgorithm<ResponseT> resultAlgorithm, TimedRetryAlgorithm timedAlgorithm, BigQueryRetryConfig bigQueryRetryConfig)

**Parameters**  
---  
**Name** | **Description**  
`resultAlgorithm` | `[ResultRetryAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.ResultRetryAlgorithm.html)<ResponseT>`  
  
`timedAlgorithm` | `[TimedRetryAlgorithm](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.TimedRetryAlgorithm.html)`  
  
`bigQueryRetryConfig` | `[BigQueryRetryConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.BigQueryRetryConfig)`  
  
  
## Methods 

### createNextAttempt(RetryingContext context, Throwable previousThrowable, ResponseT previousResponse, TimedAttemptSettings previousSettings)
    
    
    public TimedAttemptSettings createNextAttempt(RetryingContext context, Throwable previousThrowable, ResponseT previousResponse, TimedAttemptSettings previousSettings)

**Parameters**  
---  
**Name** | **Description**  
`context` | `[RetryingContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetryingContext.html)`  
  
`previousThrowable` | `[Throwable](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html)`  
  
`previousResponse` | `ResponseT`  
  
`previousSettings` | `[TimedAttemptSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.TimedAttemptSettings.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TimedAttemptSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.TimedAttemptSettings.html)` |   
**Overrides**

com.google.api.gax.retrying.RetryAlgorithm.createNextAttempt(com.google.api.gax.retrying.RetryingContext,java.lang.Throwable,ResponseT,com.google.api.gax.retrying.TimedAttemptSettings)

### shouldRetry(RetryingContext context, Throwable previousThrowable, ResponseT previousResponse, TimedAttemptSettings nextAttemptSettings)
    
    
    public boolean shouldRetry(RetryingContext context, Throwable previousThrowable, ResponseT previousResponse, TimedAttemptSettings nextAttemptSettings)

**Parameters**  
---  
**Name** | **Description**  
`context` | `[RetryingContext](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.RetryingContext.html)`  
  
`previousThrowable` | `[Throwable](https://docs.oracle.com/javase/8/docs/api/java/lang/Throwable.html)`  
  
`previousResponse` | `ResponseT`  
  
`nextAttemptSettings` | `[TimedAttemptSettings](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.api.gax.retrying.TimedAttemptSettings.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

com.google.api.gax.retrying.RetryAlgorithm.shouldRetry(com.google.api.gax.retrying.RetryingContext,java.lang.Throwable,ResponseT,com.google.api.gax.retrying.TimedAttemptSettings)

**Exceptions**  
---  
**Type** | **Description**  
`[CancellationException](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CancellationException.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
