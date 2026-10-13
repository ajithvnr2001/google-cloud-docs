---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntryOrBuilder
title: Interface LogEntryOrBuilder (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:10.139391+00:00
---

# Interface LogEntryOrBuilder (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntryOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LogEntryOrBuilder (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public interface LogEntryOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

Optional. A map of key, value pairs that provides additional information about the log entry. The labels can be user-defined or system-defined.

User-defined labels are arbitrary key, value pairs that you can use to classify logs.

System-defined labels are defined by GCP services for platform logs. They have two components - a service namespace component and the attribute name. For example: `compute.googleapis.com/resource_name`.

Cloud Logging truncates label keys that exceed 512 B and label values that exceed 64 KB upon their associated log entry being written. The truncation is indicated by an ellipsis at the end of the character string.

`map<string, string> labels = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getHttpRequest()
    
    
    public abstract HttpRequest getHttpRequest()

Optional. Information about the HTTP request associated with this log entry, if applicable.

` .google.logging.type.HttpRequest http_request = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.logging.type.HttpRequest` | The httpRequest.  
  
### getHttpRequestOrBuilder()
    
    
    public abstract HttpRequestOrBuilder getHttpRequestOrBuilder()

Optional. Information about the HTTP request associated with this log entry, if applicable.

` .google.logging.type.HttpRequest http_request = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.logging.type.HttpRequestOrBuilder` |   
  
### getInsertId()
    
    
    public abstract String getInsertId()

Optional. A unique identifier for the log entry. If you provide a value, then Logging considers other log entries in the same project, with the same `timestamp`, and with the same `insert_id` to be duplicates which are removed in a single query result. However, there are no guarantees of de-duplication in the export of logs.

If the `insert_id` is omitted when writing a log entry, the Logging API assigns its own unique identifier in this field.

In queries, the `insert_id` is also used to order log entries that have the same `log_name` and `timestamp` values.

`string insert_id = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The insertId.  
  
### getInsertIdBytes()
    
    
    public abstract ByteString getInsertIdBytes()

Optional. A unique identifier for the log entry. If you provide a value, then Logging considers other log entries in the same project, with the same `timestamp`, and with the same `insert_id` to be duplicates which are removed in a single query result. However, there are no guarantees of de-duplication in the export of logs.

If the `insert_id` is omitted when writing a log entry, the Logging API assigns its own unique identifier in this field.

In queries, the `insert_id` is also used to order log entries that have the same `log_name` and `timestamp` values.

`string insert_id = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for insertId.  
  
### getJsonPayload()
    
    
    public abstract Struct getJsonPayload()

The log entry payload, represented as a structure that is expressed as a JSON object.

`.google.protobuf.Struct json_payload = 6;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The jsonPayload.  
  
### getJsonPayloadOrBuilder()
    
    
    public abstract StructOrBuilder getJsonPayloadOrBuilder()

The log entry payload, represented as a structure that is expressed as a JSON object.

`.google.protobuf.Struct json_payload = 6;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntryOrBuilder#com_google_logging_v2_LogEntryOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

Optional. A map of key, value pairs that provides additional information about the log entry. The labels can be user-defined or system-defined.

User-defined labels are arbitrary key, value pairs that you can use to classify logs.

System-defined labels are defined by GCP services for platform logs. They have two components - a service namespace component and the attribute name. For example: `compute.googleapis.com/resource_name`.

Cloud Logging truncates label keys that exceed 512 B and label values that exceed 64 KB upon their associated log entry being written. The truncation is indicated by an ellipsis at the end of the character string.

`map<string, string> labels = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

Optional. A map of key, value pairs that provides additional information about the log entry. The labels can be user-defined or system-defined.

User-defined labels are arbitrary key, value pairs that you can use to classify logs.

System-defined labels are defined by GCP services for platform logs. They have two components - a service namespace component and the attribute name. For example: `compute.googleapis.com/resource_name`.

Cloud Logging truncates label keys that exceed 512 B and label values that exceed 64 KB upon their associated log entry being written. The truncation is indicated by an ellipsis at the end of the character string.

`map<string, string> labels = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

Optional. A map of key, value pairs that provides additional information about the log entry. The labels can be user-defined or system-defined.

User-defined labels are arbitrary key, value pairs that you can use to classify logs.

System-defined labels are defined by GCP services for platform logs. They have two components - a service namespace component and the attribute name. For example: `compute.googleapis.com/resource_name`.

Cloud Logging truncates label keys that exceed 512 B and label values that exceed 64 KB upon their associated log entry being written. The truncation is indicated by an ellipsis at the end of the character string.

`map<string, string> labels = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

Optional. A map of key, value pairs that provides additional information about the log entry. The labels can be user-defined or system-defined.

User-defined labels are arbitrary key, value pairs that you can use to classify logs.

System-defined labels are defined by GCP services for platform logs. They have two components - a service namespace component and the attribute name. For example: `compute.googleapis.com/resource_name`.

Cloud Logging truncates label keys that exceed 512 B and label values that exceed 64 KB upon their associated log entry being written. The truncation is indicated by an ellipsis at the end of the character string.

`map<string, string> labels = 11 [(.google.api.field_behavior) = OPTIONAL];`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLogName()
    
    
    public abstract String getLogName()

Required. The resource name of the log to which this log entry belongs:

"projects/[PROJECT_ID]/logs/[LOG_ID]" "organizations/[ORGANIZATION_ID]/logs/[LOG_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]" "folders/[FOLDER_ID]/logs/[LOG_ID]"

A project number may be used in place of PROJECT_ID. The project number is translated to its corresponding PROJECT_ID internally and the `log_name` field will contain PROJECT_ID in queries and exports.

`[LOG_ID]` must be URL-encoded within `log_name`. Example: `"organizations/1234567890/logs/cloudresourcemanager.googleapis.com%2Factivity"`.

`[LOG_ID]` must be less than 512 characters long and can only include the following characters: upper and lower case alphanumeric characters, forward-slash, underscore, hyphen, and period.

For backward compatibility, if `log_name` begins with a forward-slash, such as `/projects/...`, then the log entry is ingested as usual, but the forward-slash is removed. Listing the log entry will not show the leading slash and filtering for a log name with a leading slash will never return any results.

`string log_name = 12 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The logName.  
  
### getLogNameBytes()
    
    
    public abstract ByteString getLogNameBytes()

Required. The resource name of the log to which this log entry belongs:

"projects/[PROJECT_ID]/logs/[LOG_ID]" "organizations/[ORGANIZATION_ID]/logs/[LOG_ID]" "billingAccounts/[BILLING_ACCOUNT_ID]/logs/[LOG_ID]" "folders/[FOLDER_ID]/logs/[LOG_ID]"

A project number may be used in place of PROJECT_ID. The project number is translated to its corresponding PROJECT_ID internally and the `log_name` field will contain PROJECT_ID in queries and exports.

`[LOG_ID]` must be URL-encoded within `log_name`. Example: `"organizations/1234567890/logs/cloudresourcemanager.googleapis.com%2Factivity"`.

`[LOG_ID]` must be less than 512 characters long and can only include the following characters: upper and lower case alphanumeric characters, forward-slash, underscore, hyphen, and period.

For backward compatibility, if `log_name` begins with a forward-slash, such as `/projects/...`, then the log entry is ingested as usual, but the forward-slash is removed. Listing the log entry will not show the leading slash and filtering for a log name with a leading slash will never return any results.

`string log_name = 12 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for logName.  
  
### getOperation()
    
    
    public abstract LogEntryOperation getOperation()

Optional. Information about an operation associated with the log entry, if applicable.

` .google.logging.v2.LogEntryOperation operation = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LogEntryOperation](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntryOperation)` | The operation.  
  
### getOperationOrBuilder()
    
    
    public abstract LogEntryOperationOrBuilder getOperationOrBuilder()

Optional. Information about an operation associated with the log entry, if applicable.

` .google.logging.v2.LogEntryOperation operation = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LogEntryOperationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntryOperationOrBuilder)` |   
  
### getPayloadCase()
    
    
    public abstract LogEntry.PayloadCase getPayloadCase()

**Returns**  
---  
**Type** | **Description**  
`[LogEntry.PayloadCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntry.PayloadCase)` |   
  
### getProtoPayload()
    
    
    public abstract Any getProtoPayload()

The log entry payload, represented as a protocol buffer. Some Google Cloud Platform services use this field for their log entry payloads.

The following protocol buffer types are supported; user-defined types are not supported:

"type.googleapis.com/google.cloud.audit.AuditLog" "type.googleapis.com/google.appengine.logging.v1.RequestLog"

`.google.protobuf.Any proto_payload = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Any](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Any.html)` | The protoPayload.  
  
### getProtoPayloadOrBuilder()
    
    
    public abstract AnyOrBuilder getProtoPayloadOrBuilder()

The log entry payload, represented as a protocol buffer. Some Google Cloud Platform services use this field for their log entry payloads.

The following protocol buffer types are supported; user-defined types are not supported:

"type.googleapis.com/google.cloud.audit.AuditLog" "type.googleapis.com/google.appengine.logging.v1.RequestLog"

`.google.protobuf.Any proto_payload = 2;`

**Returns**  
---  
**Type** | **Description**  
`[AnyOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AnyOrBuilder.html)` |   
  
### getReceiveTimestamp()
    
    
    public abstract Timestamp getReceiveTimestamp()

Output only. The time the log entry was received by Logging.

` .google.protobuf.Timestamp receive_timestamp = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The receiveTimestamp.  
  
### getReceiveTimestampOrBuilder()
    
    
    public abstract TimestampOrBuilder getReceiveTimestampOrBuilder()

Output only. The time the log entry was received by Logging.

` .google.protobuf.Timestamp receive_timestamp = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getResource()
    
    
    public abstract MonitoredResource getResource()

Required. The monitored resource that produced this log entry.

Example: a log entry that reports a database error would be associated with the monitored resource designating the particular database that reported the error.

`.google.api.MonitoredResource resource = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.api.MonitoredResource` | The resource.  
  
### getResourceOrBuilder()
    
    
    public abstract MonitoredResourceOrBuilder getResourceOrBuilder()

Required. The monitored resource that produced this log entry.

Example: a log entry that reports a database error would be associated with the monitored resource designating the particular database that reported the error.

`.google.api.MonitoredResource resource = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.api.MonitoredResourceOrBuilder` |   
  
### getSeverity()
    
    
    public abstract LogSeverity getSeverity()

Optional. The severity of the log entry. The default value is `LogSeverity.DEFAULT`.

`.google.logging.type.LogSeverity severity = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`com.google.logging.type.LogSeverity` | The severity.  
  
### getSeverityValue()
    
    
    public abstract int getSeverityValue()

Optional. The severity of the log entry. The default value is `LogSeverity.DEFAULT`.

`.google.logging.type.LogSeverity severity = 10 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for severity.  
  
### getSourceLocation()
    
    
    public abstract LogEntrySourceLocation getSourceLocation()

Optional. Source code location information associated with the log entry, if any.

` .google.logging.v2.LogEntrySourceLocation source_location = 23 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LogEntrySourceLocation](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntrySourceLocation)` | The sourceLocation.  
  
### getSourceLocationOrBuilder()
    
    
    public abstract LogEntrySourceLocationOrBuilder getSourceLocationOrBuilder()

Optional. Source code location information associated with the log entry, if any.

` .google.logging.v2.LogEntrySourceLocation source_location = 23 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[LogEntrySourceLocationOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogEntrySourceLocationOrBuilder)` |   
  
### getSpanId()
    
    
    public abstract String getSpanId()

Optional. The ID of the [Cloud Trace](https://cloud.google.com/trace) span associated with the current operation in which the log is being written. For example, if a span has the REST resource name of "projects/some-project/traces/some-trace/spans/some-span-id", then the `span_id` field is "some-span-id".

A [Span](https://cloud.google.com/trace/docs/reference/v2/rest/v2/projects.traces/batchWrite#Span) represents a single operation within a trace. Whereas a trace may involve multiple different microservices running on multiple different machines, a span generally corresponds to a single logical operation being performed in a single instance of a microservice on one specific machine. Spans are the nodes within the tree that is a trace.

Applications that are [instrumented for tracing](https://cloud.google.com/trace/docs/setup) will generally assign a new, unique span ID on each incoming request. It is also common to create and record additional spans corresponding to internal processing elements as well as issuing requests to dependencies.

The span ID is expected to be a 16-character, hexadecimal encoding of an 8-byte array and should not be zero. It should be unique within the trace and should, ideally, be generated in a manner that is uniformly random.

Example values:

  * `000000000000004a`
  * `7a2190356c3fc94b`
  * `0000f00300090021`
  * `d39223e101960076`



`string span_id = 27 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The spanId.  
  
### getSpanIdBytes()
    
    
    public abstract ByteString getSpanIdBytes()

Optional. The ID of the [Cloud Trace](https://cloud.google.com/trace) span associated with the current operation in which the log is being written. For example, if a span has the REST resource name of "projects/some-project/traces/some-trace/spans/some-span-id", then the `span_id` field is "some-span-id".

A [Span](https://cloud.google.com/trace/docs/reference/v2/rest/v2/projects.traces/batchWrite#Span) represents a single operation within a trace. Whereas a trace may involve multiple different microservices running on multiple different machines, a span generally corresponds to a single logical operation being performed in a single instance of a microservice on one specific machine. Spans are the nodes within the tree that is a trace.

Applications that are [instrumented for tracing](https://cloud.google.com/trace/docs/setup) will generally assign a new, unique span ID on each incoming request. It is also common to create and record additional spans corresponding to internal processing elements as well as issuing requests to dependencies.

The span ID is expected to be a 16-character, hexadecimal encoding of an 8-byte array and should not be zero. It should be unique within the trace and should, ideally, be generated in a manner that is uniformly random.

Example values:

  * `000000000000004a`
  * `7a2190356c3fc94b`
  * `0000f00300090021`
  * `d39223e101960076`



`string span_id = 27 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for spanId.  
  
### getSplit()
    
    
    public abstract LogSplit getSplit()

Optional. Information indicating this LogEntry is part of a sequence of multiple log entries split from a single LogEntry.

`.google.logging.v2.LogSplit split = 35 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[LogSplit](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSplit)` | The split.  
  
### getSplitOrBuilder()
    
    
    public abstract LogSplitOrBuilder getSplitOrBuilder()

Optional. Information indicating this LogEntry is part of a sequence of multiple log entries split from a single LogEntry.

`.google.logging.v2.LogSplit split = 35 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[LogSplitOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.logging.v2.LogSplitOrBuilder)` |   
  
### getTextPayload()
    
    
    public abstract String getTextPayload()

The log entry payload, represented as a Unicode string (UTF-8).

`string text_payload = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The textPayload.  
  
### getTextPayloadBytes()
    
    
    public abstract ByteString getTextPayloadBytes()

The log entry payload, represented as a Unicode string (UTF-8).

`string text_payload = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for textPayload.  
  
### getTimestamp()
    
    
    public abstract Timestamp getTimestamp()

Optional. The time the event described by the log entry occurred. This time is used to compute the log entry's age and to enforce the logs retention period. If this field is omitted in a new log entry, then Logging assigns it the current time. Timestamps have nanosecond accuracy, but trailing zeros in the fractional seconds might be omitted when the timestamp is displayed.

Incoming log entries must have timestamps that don't exceed the [logs retention period](https://cloud.google.com/logging/quotas#logs_retention_periods) in the past, and that don't exceed 24 hours in the future. Log entries outside those time boundaries aren't ingested by Logging.

`.google.protobuf.Timestamp timestamp = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The timestamp.  
  
### getTimestampOrBuilder()
    
    
    public abstract TimestampOrBuilder getTimestampOrBuilder()

Optional. The time the event described by the log entry occurred. This time is used to compute the log entry's age and to enforce the logs retention period. If this field is omitted in a new log entry, then Logging assigns it the current time. Timestamps have nanosecond accuracy, but trailing zeros in the fractional seconds might be omitted when the timestamp is displayed.

Incoming log entries must have timestamps that don't exceed the [logs retention period](https://cloud.google.com/logging/quotas#logs_retention_periods) in the past, and that don't exceed 24 hours in the future. Log entries outside those time boundaries aren't ingested by Logging.

`.google.protobuf.Timestamp timestamp = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getTrace()
    
    
    public abstract String getTrace()

Optional. The REST resource name of the trace being written to [Cloud Trace](https://cloud.google.com/trace) in association with this log entry. For example, if your trace data is stored in the Cloud project "my-trace-project" and if the service that is creating the log entry receives a trace header that includes the trace ID "12345", then the service should use "projects/my-tracing-project/traces/12345".

The `trace` field provides the link between logs and traces. By using this field, you can navigate from a log entry to a trace.

`string trace = 22 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The trace.  
  
### getTraceBytes()
    
    
    public abstract ByteString getTraceBytes()

Optional. The REST resource name of the trace being written to [Cloud Trace](https://cloud.google.com/trace) in association with this log entry. For example, if your trace data is stored in the Cloud project "my-trace-project" and if the service that is creating the log entry receives a trace header that includes the trace ID "12345", then the service should use "projects/my-tracing-project/traces/12345".

The `trace` field provides the link between logs and traces. By using this field, you can navigate from a log entry to a trace.

`string trace = 22 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for trace.  
  
### getTraceSampled()
    
    
    public abstract boolean getTraceSampled()

Optional. The sampling decision of the trace associated with the log entry.

True means that the trace resource name in the `trace` field was sampled for storage in a trace backend. False means that the trace was not sampled for storage when this log entry was written, or the sampling decision was unknown at the time. A non-sampled `trace` value is still useful as a request correlation identifier. The default is False.

`bool trace_sampled = 30 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The traceSampled.  
  
### hasHttpRequest()
    
    
    public abstract boolean hasHttpRequest()

Optional. Information about the HTTP request associated with this log entry, if applicable.

` .google.logging.type.HttpRequest http_request = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the httpRequest field is set.  
  
### hasJsonPayload()
    
    
    public abstract boolean hasJsonPayload()

The log entry payload, represented as a structure that is expressed as a JSON object.

`.google.protobuf.Struct json_payload = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the jsonPayload field is set.  
  
### hasOperation()
    
    
    public abstract boolean hasOperation()

Optional. Information about an operation associated with the log entry, if applicable.

` .google.logging.v2.LogEntryOperation operation = 15 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the operation field is set.  
  
### hasProtoPayload()
    
    
    public abstract boolean hasProtoPayload()

The log entry payload, represented as a protocol buffer. Some Google Cloud Platform services use this field for their log entry payloads.

The following protocol buffer types are supported; user-defined types are not supported:

"type.googleapis.com/google.cloud.audit.AuditLog" "type.googleapis.com/google.appengine.logging.v1.RequestLog"

`.google.protobuf.Any proto_payload = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the protoPayload field is set.  
  
### hasReceiveTimestamp()
    
    
    public abstract boolean hasReceiveTimestamp()

Output only. The time the log entry was received by Logging.

` .google.protobuf.Timestamp receive_timestamp = 24 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the receiveTimestamp field is set.  
  
### hasResource()
    
    
    public abstract boolean hasResource()

Required. The monitored resource that produced this log entry.

Example: a log entry that reports a database error would be associated with the monitored resource designating the particular database that reported the error.

`.google.api.MonitoredResource resource = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the resource field is set.  
  
### hasSourceLocation()
    
    
    public abstract boolean hasSourceLocation()

Optional. Source code location information associated with the log entry, if any.

` .google.logging.v2.LogEntrySourceLocation source_location = 23 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the sourceLocation field is set.  
  
### hasSplit()
    
    
    public abstract boolean hasSplit()

Optional. Information indicating this LogEntry is part of a sequence of multiple log entries split from a single LogEntry.

`.google.logging.v2.LogSplit split = 35 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the split field is set.  
  
### hasTextPayload()
    
    
    public abstract boolean hasTextPayload()

The log entry payload, represented as a Unicode string (UTF-8).

`string text_payload = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the textPayload field is set.  
  
### hasTimestamp()
    
    
    public abstract boolean hasTimestamp()

Optional. The time the event described by the log entry occurred. This time is used to compute the log entry's age and to enforce the logs retention period. If this field is omitted in a new log entry, then Logging assigns it the current time. Timestamps have nanosecond accuracy, but trailing zeros in the fractional seconds might be omitted when the timestamp is displayed.

Incoming log entries must have timestamps that don't exceed the [logs retention period](https://cloud.google.com/logging/quotas#logs_retention_periods) in the past, and that don't exceed 24 hours in the future. Log entries outside those time boundaries aren't ingested by Logging.

`.google.protobuf.Timestamp timestamp = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timestamp field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
