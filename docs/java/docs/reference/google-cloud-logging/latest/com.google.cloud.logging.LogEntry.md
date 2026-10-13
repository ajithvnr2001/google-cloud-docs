---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry
title: Class LogEntry (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:58.839229+00:00
---

# Class LogEntry (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class LogEntry (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public class LogEntry implements Serializable

A Cloud Logging log entry. All log entries are represented via objects of this class. Log entries can have different type of payloads: an UTF-8 string (see [Payload.StringPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.StringPayload)), a JSON object (see [Payload.JsonPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.JsonPayload), or a protobuf object (see [Payload.ProtoPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.ProtoPayload)). Entries can also store additional information about the operation or the HTTP request that generated the log (see [LogEntry#getOperation()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry#com_google_cloud_logging_LogEntry_getOperation__) and [LogEntry#getHttpRequest()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry#com_google_cloud_logging_LogEntry_getHttpRequest__), respectively). See Also: [Log Entries and Logs](https://cloud.google.com/logging/docs/view/logs_index)

## Inheritance

[Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > LogEntry

## Implements

[Serializable](https://docs.oracle.com/javase/8/docs/api/java/io/Serializable.html)

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

### fromPb(LogEntry entryPb)
    
    
    public static LogEntry fromPb(LogEntry entryPb)

**Parameter**  
---  
**Name** | **Description**  
`entryPb` | `[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry)`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)` |   
  
### newBuilder(Payload<?> payload)
    
    
    public static LogEntry.Builder newBuilder(Payload<?> payload)

Returns a builder for `LogEntry` objects given the entry payload.

**Parameter**  
---  
**Name** | **Description**  
`payload` | `[Payload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload)<?>`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogEntry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.Builder)` |   
  
### of(Payload<?> payload)
    
    
    public static LogEntry of(Payload<?> payload)

Creates a `LogEntry` object given the entry payload.

**Parameter**  
---  
**Name** | **Description**  
`payload` | `[Payload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload)<?>`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)` |   
  
### of(String logName, MonitoredResource resource, Payload<?> payload)
    
    
    public static LogEntry of(String logName, MonitoredResource resource, Payload<?> payload)

Creates a `LogEntry` object given the log name, the monitored resource and the entry payload.

**Parameters**  
---  
**Name** | **Description**  
`logName` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`resource` | `com.google.cloud.MonitoredResource`  
  
`payload` | `[Payload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload)<?>`  
  
**Returns**  
---  
**Type** | **Description**  
`[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry)` |   
  
### toPbFunction(String projectId)
    
    
    public static Function<LogEntry,LogEntry> toPbFunction(String projectId)

**Parameter**  
---  
**Name** | **Description**  
`projectId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`com.google.common.base.Function<[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry),[LogEntry](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry)>` |   
  
## Methods 

### <T>getPayload()
    
    
    public T <T>getPayload()

Returns the payload for this log entry. The log entry payload can be an UTF-8 string (see [Payload.StringPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.StringPayload)), a JSON object (see [Payload.JsonPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.JsonPayload), or a protobuf object (see [Payload.ProtoPayload](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Payload.ProtoPayload)). See Also: [Log Entries and Logs](https://cloud.google.com/logging/docs/view/logs_index)

**Returns**  
---  
**Type** | **Description**  
`T` |   
  
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

### getDestination()
    
    
    public LogDestinationName getDestination()

Returns the log path destination name type associated with log entry. By default, project name based destination is used. See Also: [logName](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry)

**Returns**  
---  
**Type** | **Description**  
`[LogDestinationName](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogDestinationName)` |   
  
### getHttpRequest()
    
    
    public HttpRequest getHttpRequest()

Returns information about the HTTP request associated with this log entry, if applicable.

**Returns**  
---  
**Type** | **Description**  
`[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest)` |   
  
### getInsertId()
    
    
    public String getInsertId()

Returns a unique ID for the log entry. The Logging service considers other log entries in the same log with the same ID as duplicates which can be removed.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getInstantReceiveTimestamp()
    
    
    public Instant getInstantReceiveTimestamp()

Returns the time the log entry was received by Cloud Logging, in milliseconds.

**Returns**  
---  
**Type** | **Description**  
`[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)` | timestamp as [Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)  
  
### getInstantTimestamp()
    
    
    public Instant getInstantTimestamp()

Returns the time at which the event described by the log entry occurred.

**Returns**  
---  
**Type** | **Description**  
`[Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)` | timestamp as [Instant](https://docs.oracle.com/javase/8/docs/api/java/time/Instant.html)  
  
### getLabels()
    
    
    public Map<String,String> getLabels()

Returns an optional set of user-defined (key, value) data that provides additional information about the log entry.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLogName()
    
    
    public String getLogName()

Returns the name of the log to which this log entry belongs. The log name must be less than 512 characters long and can only include the following characters: upper and lower case alphanumeric characters: `[A-Za-z0-9]`; and punctuation characters: `_-./`. The forward-slash (`/`) characters in the log name must be URL-encoded. Examples: ` syslog`, `library.googleapis.com%2Fbook_log`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getOperation()
    
    
    public Operation getOperation()

Returns information about an operation associated with the log entry, if applicable.

**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Operation)` |   
  
### getReceiveTimestamp() (deprecated)
    
    
    public Long getReceiveTimestamp()

**Deprecated.** _This method is no longer recommended to get the received time timestamp._

_Use getInstantReceiveTimestamp() instead._

Returns the time the log entry was received by Cloud Logging, in milliseconds.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` | timestamp in milliseconds  
  
### getResource()
    
    
    public MonitoredResource getResource()

Returns the monitored resource associated with this log entry. Example: a log entry that reports a database error would be associated with the monitored resource designating the particular database that reported the error.

**Returns**  
---  
**Type** | **Description**  
`com.google.cloud.MonitoredResource` |   
  
### getSeverity()
    
    
    public Severity getSeverity()

Returns the severity of the log entry. If not set, [Severity#DEFAULT](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Severity#com_google_cloud_logging_Severity_DEFAULT) is used.

**Returns**  
---  
**Type** | **Description**  
`[Severity](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Severity)` |   
  
### getSourceLocation()
    
    
    public SourceLocation getSourceLocation()

Returns the source code location information associated with the log entry, if any.

**Returns**  
---  
**Type** | **Description**  
`[SourceLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.SourceLocation)` |   
  
### getSpanId()
    
    
    public String getSpanId()

Returns the ID of the trace span associated with the log entry, if any.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTimestamp() (deprecated)
    
    
    public Long getTimestamp()

**Deprecated.** _This method is no longer recommended to get the entry timestamp._

_Use getInstantTimestamp() instead._

Returns the time at which the event described by the log entry occurred, in milliseconds.

**Returns**  
---  
**Type** | **Description**  
`[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)` | timestamp in milliseconds  
  
### getTrace()
    
    
    public String getTrace()

Returns the resource name of the trace associated with the log entry, if any. If it contains a relative resource name, the name is assumed to be relative to `//tracing.googleapis.com`.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getTraceSampled()
    
    
    public boolean getTraceSampled()

Returns the sampling decision of the trace span associated with the log entry, or `false` if there is no trace span.

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### hashCode()
    
    
    public int hashCode()

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
**Overrides**

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

### toBuilder()
    
    
    public LogEntry.Builder toBuilder()

Returns a `Builder` for this log entry.

**Returns**  
---  
**Type** | **Description**  
`[LogEntry.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.LogEntry.Builder)` |   
  
### toString()
    
    
    public String toString()

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
**Overrides**

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

### toStructuredJsonString()
    
    
    public String toStructuredJsonString()

Serializes the object to a one line JSON string in the simplified format that can be parsed by the logging agents that run on Google Cloud resources.

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
