---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName
title: Class LogDestinationName (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:58.659864+00:00
---

# Class LogDestinationName (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LogDestinationName (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public final class LogDestinationName extends Option

Class for specifying resource name of the log to which this log entry belongs (see 'logName' parameter in <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>)

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.cloud.logging.Option > LogDestinationName

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

### billingAccount(String id)
    
    
    public static LogDestinationName billingAccount(String id)

Returns an option which sets and validates project ID resource name for log entries.

**Parameter**  
---  
**Name** | **Description**  
`id` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
corresponds to BILLING_ACCOUNT_ID token in 'logName' field described in <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>  
**Returns**  
---  
**Type** | **Description**  
`[LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName)` |   
  
### folder(String id)
    
    
    public static LogDestinationName folder(String id)

Returns an option which sets and validates project ID resource name for log entries.

**Parameter**  
---  
**Name** | **Description**  
`id` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
corresponds to FOLDER_ID token in 'logName' field described in <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>  
**Returns**  
---  
**Type** | **Description**  
`[LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName)` |   
  
### fromLogName(LogName logName)
    
    
    public static LogDestinationName fromLogName(LogName logName)

Creates a `LogDestinationName` object from given `LogName`.

**Parameter**  
---  
**Name** | **Description**  
`logName` | `[LogName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogName)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName)` |   
  
### organization(String id)
    
    
    public static LogDestinationName organization(String id)

Returns an option which sets and validates project ID resource name for log entries.

**Parameter**  
---  
**Name** | **Description**  
`id` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
corresponds to ORGANIZATION_ID token in 'logName' field described in <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>  
**Returns**  
---  
**Type** | **Description**  
`[LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName)` |   
  
### project(String id)
    
    
    public static LogDestinationName project(String id)

Returns an option which sets and validates project ID resource name for log entries.

**Parameter**  
---  
**Name** | **Description**  
`id` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
corresponds to PROJECT_ID token in 'logName' field described in <https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry>  
**Returns**  
---  
**Type** | **Description**  
`[LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName)` |   
  
## Methods 

### getDestinationId()
    
    
    public String getDestinationId()

Returns ID value associated with `LogDestinationName` object

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getDestinationType()
    
    
    public LogDestinationName.DestinationType getDestinationType()

Returns destination type option value associated with `LogDestinationName` object

**Returns**  
---  
**Type** | **Description**  
`[LogDestinationName.DestinationType](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName.DestinationType)` |   
  
### toLogName(String logId)
    
    
    public LogName toLogName(String logId)

Creates a `LogEntry` object for given log ID.

**Parameter**  
---  
**Name** | **Description**  
`logId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
