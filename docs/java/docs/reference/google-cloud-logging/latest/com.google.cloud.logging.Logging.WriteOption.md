---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption
title: Class Logging.WriteOption (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:21:00.368123+00:00
---

# Class Logging.WriteOption (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Logging.WriteOption (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public static final class Logging.WriteOption extends Option

Class for specifying options for writing log entries.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.cloud.logging.Option > Logging.WriteOption

## Inherited Members

com.google.cloud.logging.Option.equals(java.lang.Object)

com.google.cloud.logging.Option.hashCode()

com.google.cloud.logging.Option.toString()

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### autoPopulateMetadata(boolean autoPopulateMetadata)
    
    
    public static Logging.WriteOption autoPopulateMetadata(boolean autoPopulateMetadata)

Returns an option to opt-out automatic population of log entries metadata fields that are not set.

**Parameter**  
---  
**Name** | **Description**  
`autoPopulateMetadata` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.WriteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption)` |   
  
### destination(LogDestinationName destination)
    
    
    public static Logging.WriteOption destination(LogDestinationName destination)

Returns an option to specify a log destination resource path (see [LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName) for details)

**Parameter**  
---  
**Name** | **Description**  
`destination` | `[LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.WriteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption)` |   
  
### labels(Map<String,String> labels)
    
    
    public static Logging.WriteOption labels(Map<String,String> labels)

Sets an option to specify (key, value) pairs that are added to the [LogEntry#getLabels()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry#com_google_logging_v2_LogEntry_getLabels__) of each log entry written, except when a log entry already has a value associated to the same key.

**Parameter**  
---  
**Name** | **Description**  
`labels` | `[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.WriteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption)` |   
  
### logName(String logName)
    
    
    public static Logging.WriteOption logName(String logName)

Returns an option to specify a default log name (see [LogEntry#getLogName()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry#com_google_logging_v2_LogEntry_getLogName__)) for those log entries that do not specify their own log name. Example: `syslog`.

**Parameter**  
---  
**Name** | **Description**  
`logName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.WriteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption)` |   
  
### partialSuccess(boolean partialSuccess)
    
    
    public static Logging.WriteOption partialSuccess(boolean partialSuccess)

Returns an option to set partialSuccess flag. See [the API documentation](https://cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write#body.request_body.FIELDS.partial_success) for more details.

**Parameter**  
---  
**Name** | **Description**  
`partialSuccess` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.WriteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption)` |   
  
### resource(MonitoredResource resource)
    
    
    public static Logging.WriteOption resource(MonitoredResource resource)

Returns an option to specify a default monitored resource (see [LogEntry#getResource()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry#com_google_logging_v2_LogEntry_getResource__)) for those log entries that do not specify their own resource.

**Parameter**  
---  
**Name** | **Description**  
`resource` | `com.google.cloud.MonitoredResource`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.WriteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
