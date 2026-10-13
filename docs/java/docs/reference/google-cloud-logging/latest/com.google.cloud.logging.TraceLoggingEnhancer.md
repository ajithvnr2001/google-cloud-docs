---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.TraceLoggingEnhancer
title: Class TraceLoggingEnhancer (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:05.592334+00:00
---

# Class TraceLoggingEnhancer (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.TraceLoggingEnhancer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TraceLoggingEnhancer (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public class TraceLoggingEnhancer implements LoggingEnhancer

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TraceLoggingEnhancer

## Implements

[LoggingEnhancer](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LoggingEnhancer)

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

### getCurrentSpanId()
    
    
    public static String getCurrentSpanId()

Get the Span ID associated with any logging done by the current thread.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | id The span ID  
  
### getCurrentTraceId()
    
    
    public static String getCurrentTraceId()

Get the Trace ID associated with any logging done by the current thread.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | id The trace ID  
  
### getCurrentTraceSampled()
    
    
    public static Boolean getCurrentTraceSampled()

Get the trace sampled flag associated with any logging done by the current thread.

**Returns**  
---  
**Type** | **Description**  
`[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)` | traceSampled The traceSampled flag  
  
### setCurrentSpanId(String id)
    
    
    public static void setCurrentSpanId(String id)

Set the Span ID associated with any logging done by the current thread.

**Parameter**  
---  
**Name** | **Description**  
`id` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The spanID  
  
### setCurrentTraceId(String id)
    
    
    public static void setCurrentTraceId(String id)

Set the Trace ID associated with any logging done by the current thread.

**Parameter**  
---  
**Name** | **Description**  
`id` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
The traceID, in the form projects/[PROJECT_ID]/traces/[TRACE_ID]  
  
### setCurrentTraceSampled(Boolean isTraceSampled)
    
    
    public static void setCurrentTraceSampled(Boolean isTraceSampled)

Set the trace sampled flag associated with any logging done by the current thread.

**Parameter**  
---  
**Name** | **Description**  
`isTraceSampled` | `[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html)`  
The traceSampled flag  
  
## Constructors 

### TraceLoggingEnhancer()
    
    
    public TraceLoggingEnhancer()

### TraceLoggingEnhancer(String prefix)
    
    
    public TraceLoggingEnhancer(String prefix)

**Parameter**  
---  
**Name** | **Description**  
`prefix` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
  
## Methods 

### enhanceLogEntry(LogEntry.Builder builder)
    
    
    public void enhanceLogEntry(LogEntry.Builder builder)

**Parameter**  
---  
**Name** | **Description**  
`builder` | `[LogEntry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.Builder)`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
