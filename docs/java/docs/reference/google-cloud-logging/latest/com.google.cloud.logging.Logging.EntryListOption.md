---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption
title: Class Logging.EntryListOption (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:59.353189+00:00
---

# Class Logging.EntryListOption (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Logging.EntryListOption (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public static final class Logging.EntryListOption extends Option

Class for specifying options for listing log entries.

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > com.google.cloud.logging.Option > Logging.EntryListOption

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

### billingAccount(String billingAccount)
    
    
    public static Logging.EntryListOption billingAccount(String billingAccount)

Returns an option to specify a billingAccount for the log entries to be listed.

**Parameter**  
---  
**Name** | **Description**  
`billingAccount` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption)` |   
  
### filter(String filter)
    
    
    public static Logging.EntryListOption filter(String filter)

Returns an option to specify a filter to the log entries to be listed. See Also: [Advanced Logs Filters](https://cloud.google.com/logging/docs/view/advanced_filters)

**Parameter**  
---  
**Name** | **Description**  
`filter` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption)` |   
  
### folder(String folder)
    
    
    public static Logging.EntryListOption folder(String folder)

Returns an option to specify a folder for the log entries to be listed.

**Parameter**  
---  
**Name** | **Description**  
`folder` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption)` |   
  
### organization(String organization)
    
    
    public static Logging.EntryListOption organization(String organization)

Returns an option to specify an organization for the log entries to be listed.

**Parameter**  
---  
**Name** | **Description**  
`organization` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption)` |   
  
### pageSize(int pageSize)
    
    
    public static Logging.EntryListOption pageSize(int pageSize)

Returns an option to specify the maximum number of log entries returned per page.

**Parameter**  
---  
**Name** | **Description**  
`pageSize` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption)` |   
  
### pageToken(String pageToken)
    
    
    public static Logging.EntryListOption pageToken(String pageToken)

Returns an option to specify the page token from which to start listing log entries.

**Parameter**  
---  
**Name** | **Description**  
`pageToken` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption)` |   
  
### sortOrder(Logging.SortingField field, Logging.SortingOrder order)
    
    
    public static Logging.EntryListOption sortOrder(Logging.SortingField field, Logging.SortingOrder order)

Returns an option to sort log entries. If not specified, log entries are sorted in ascending (most-recent last) order with respect to the [LogEntry#getTimestamp()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry#com_google_logging_v2_LogEntry_getTimestamp__) value.

**Parameters**  
---  
**Name** | **Description**  
`field` | `[Logging.SortingField](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.SortingField)`  
  
`order` | `[Logging.SortingOrder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.SortingOrder)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Logging.EntryListOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.EntryListOption)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
