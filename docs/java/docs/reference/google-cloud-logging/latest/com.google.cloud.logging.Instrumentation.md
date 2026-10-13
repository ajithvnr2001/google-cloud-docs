---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Instrumentation
title: Class Instrumentation (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:58.130556+00:00
---

# Class Instrumentation (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Instrumentation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Instrumentation (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public final class Instrumentation

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Instrumentation

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

## Static Fields 

### DEFAULT_INSTRUMENTATION_VERSION
    
    
    public static final String DEFAULT_INSTRUMENTATION_VERSION

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### DIAGNOSTIC_INFO_KEY
    
    
    public static final String DIAGNOSTIC_INFO_KEY

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### INSTRUMENTATION_LOG_NAME
    
    
    public static final String INSTRUMENTATION_LOG_NAME

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### INSTRUMENTATION_NAME_KEY
    
    
    public static final String INSTRUMENTATION_NAME_KEY

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### INSTRUMENTATION_SOURCE_KEY
    
    
    public static final String INSTRUMENTATION_SOURCE_KEY

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### INSTRUMENTATION_VERSION_KEY
    
    
    public static final String INSTRUMENTATION_VERSION_KEY

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### JAVA_LIBRARY_NAME_PREFIX
    
    
    public static final String JAVA_LIBRARY_NAME_PREFIX

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### MAX_DIAGNOSTIC_ENTIES
    
    
    public static final int MAX_DIAGNOSTIC_ENTIES

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### MAX_DIAGNOSTIC_VALUE_LENGTH
    
    
    public static final int MAX_DIAGNOSTIC_VALUE_LENGTH

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### addPartialSuccessOption(Logging.WriteOption[] options)
    
    
    public static Logging.WriteOption[] addPartialSuccessOption(Logging.WriteOption[] options)

Adds a partialSuccess flag option to array of WriteOption

**Parameter**  
---  
**Name** | **Description**  
`options` | `[WriteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption)[]`  
{WriteOption[]} The options array to be extended  
**Returns**  
---  
**Type** | **Description**  
`[WriteOption](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Logging.WriteOption)[]` | The new array of oprions containing WriteOption.OptionType.PARTIAL_SUCCESS flag set to true  
  
### createDiagnosticEntry(String libraryName, String libraryVersion)
    
    
    public static LogEntry createDiagnosticEntry(String libraryName, String libraryVersion)

The helper method to generate a log entry with diagnostic instrumentation data.

**Parameters**  
---  
**Name** | **Description**  
`libraryName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
{string} The name of the logging library to be reported. Should be prefixed with 'java'. Will be truncated if longer than 14 characters.  
`libraryVersion` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
{string} The version of the logging library to be reported. Will be truncated if longer than 14 characters.  
**Returns**  
---  
**Type** | **Description**  
`[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)` | {LogEntry} The entry with diagnostic instrumentation data.  
  
### getLibraryVersion(Class<?> libraryClass)
    
    
    public static String getLibraryVersion(Class<?> libraryClass)

Returns a library version associated with given class

**Parameter**  
---  
**Name** | **Description**  
`libraryClass` | `[Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)<?>`  
The class to be used to determine a library version  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The version number string for given class or DEFAULT_INSTRUMENTATION_VERSION if class library version cannot be detected  
  
### populateInstrumentationInfo(Iterable<LogEntry> logEntries)
    
    
    public static Tuple<Boolean,Iterable<LogEntry>> populateInstrumentationInfo(Iterable<LogEntry> logEntries)

Populates entries with instrumentation info which is added in separate log entry

**Parameter**  
---  
**Name** | **Description**  
`logEntries` | `[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)>`  
`Iterable<LogEntry>` The list of entries to be populated  
**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.Tuple<[Boolean](https://docs.oracle.com/javase/8/docs/api/java/lang/Boolean.html),[Iterable](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)>>` | `Tuple<Boolean, Iterable<LogEntry>>` containing a flag if instrumentation info was added or not and a modified list of log entries  
  
### truncateValue(String value)
    
    
    public static String truncateValue(String value)

Trancates given string to MAX_DIAGNOSTIC_VALUE_LENGTH and adds "*" instead of reduced suffix

**Parameter**  
---  
**Name** | **Description**  
`value` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
{String} Value to be truncated  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The truncated string  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
