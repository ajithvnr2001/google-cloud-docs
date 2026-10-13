---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation/
title: Operation \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:05.151839+00:00
---

# Operation  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Operation Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * LogEntry
    * JSON representation
  * LogSeverity
  * HttpRequest
    * JSON representation
  * LogEntryOperation
    * JSON representation
  * LogEntrySourceLocation
    * JSON representation
  * Importance
  * TraceSpan
    * JSON representation
  * Attributes
    * JSON representation
  * SpanKind



Represents information regarding an operation.

JSON representation  
---  
      
    
    {
      "operationId": string,
      "operationName": string,
      "consumerId": string,
      "startTime": string,
      "endTime": string,
      "labels": {
        string: string,
        ...
      },
      "metricValueSets": [
        {
          object ([MetricValueSet](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet))
        }
      ],
      "logEntries": [
        {
          object ([LogEntry](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#LogEntry))
        }
      ],
      "importance": enum ([Importance](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#Importance)),
      "userLabels": {
        string: string,
        ...
      },
      "traceSpans": [
        {
          object ([TraceSpan](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#TraceSpan))
        }
      ],
      "extensions": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`operationId` |  `string` Identity of the operation. This must be unique within the scope of the service that generated the operation. If the service calls services.check() and services.report() on the same operation, the two calls should carry the same id.UUID version 4 is recommended, though not required. In scenarios where an operation is computed from existing information and an idempotent id is desirable for deduplication purpose, UUID version 5 is recommended. See RFC 4122 for details.  
`operationName` |  `string` Fully qualified name of the operation. Reserved for future use.  
`consumerId` |  `string` Identity of the consumer who is using the service. This field should be filled in for the operations initiated by a consumer, but not for service-initiated operations that are not related to a specific consumer.

  * This can be in one of the following formats: 
    * project:PROJECT_ID,
    * project`_`number:PROJECT_NUMBER,
    * projects/PROJECT_ID or PROJECT_NUMBER,
    * folders/FOLDER_NUMBER,
    * organizations/ORGANIZATION_NUMBER,
    * api`_`key:API_KEY.

  
`startTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Required. Start time of the operation.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` End time of the operation. Required when the operation is used in `[ServiceController.Report](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/report#google.api.servicecontrol.v1.ServiceController.Report)`, but optional when the operation is used in `[ServiceController.Check](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/services/check#google.api.servicecontrol.v1.ServiceController.Check)`.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`labels` |  `map (key: string, value: string)` Labels describing the operation. Only the following labels are allowed:

  * Labels describing monitored resources as defined in the service configuration.
  * Default labels of metric values. When specified, labels defined in the metric value override these default.
  * The following labels defined by Google Cloud Platform: 
    * `cloud.googleapis.com/location` describing the location where the operation happened,
    * `servicecontrol.googleapis.com/userAgent` describing the user agent of the API request,
    * `servicecontrol.googleapis.com/service_agent` describing the service used to handle the API request (e.g. ESP),
    * `servicecontrol.googleapis.com/platform` describing the platform where the API is served, such as App Engine, Compute Engine, or Kubernetes Engine.

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`metricValueSets[]` |  `object (`[MetricValueSet](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/MetricValueSet)`)` Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition.Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error.  
`logEntries[]` |  `object (`[LogEntry](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#LogEntry)`)` Represents information to be logged.  
`importance` |  `enum (`[Importance](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#Importance)`)` DO NOT USE. This is an experimental field.  
`userLabels` |  `map (key: string, value: string)` Private Preview. This feature is only available for approved services.User defined labels for the resource that this operation is associated with. Only a combination of 1000 user labels per consumer project are allowed.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`traceSpans[]` |  `object (`[TraceSpan](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#TraceSpan)`)` Unimplemented. A list of Cloud Trace spans. The span names shall contain the id of the destination project which can be either the produce or the consumer project.  
`extensions[]` |  `object` Unimplemented.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
## LogEntry

An individual log entry.

JSON representation  
---  
      
    
    {
      "name": string,
      "timestamp": string,
      "severity": enum ([LogSeverity](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#LogSeverity)),
      "httpRequest": {
        object ([HttpRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#HttpRequest))
      },
      "trace": string,
      "insertId": string,
      "labels": {
        string: string,
        ...
      },
      "operation": {
        object ([LogEntryOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#LogEntryOperation))
      },
      "sourceLocation": {
        object ([LogEntrySourceLocation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#LogEntrySourceLocation))
      },
    
      // Union field payload can be only one of the following:
      "protoPayload": {
        "@type": string,
        field1: ...,
        ...
      },
      "textPayload": string,
      "structPayload": {
        object
      }
      // End of list of possible types for union field payload.
    }  
  
Fields  
---  
`name` |  `string` Required. The log to which this log entry belongs. Examples: `"syslog"`, `"book_log"`.  
`timestamp` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The time the event described by the log entry occurred. If omitted, defaults to operation start time.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`severity` |  `enum (`[LogSeverity](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#LogSeverity)`)` The severity of the log entry. The default value is `LogSeverity.DEFAULT`.  
`httpRequest` |  `object (`[HttpRequest](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#HttpRequest)`)` Optional. Information about the HTTP request associated with this log entry, if applicable.  
`trace` |  `string` Optional. Resource name of the trace associated with the log entry, if any. If this field contains a relative resource name, you can assume the name is relative to `//tracing.googleapis.com`. Example: `projects/my-projectid/traces/06796866738c859f2f19b7cfb3214824`  
`insertId` |  `string` A unique ID for the log entry used for deduplication. If omitted, the implementation will generate one based on operationId.  
`labels` |  `map (key: string, value: string)` A set of user-defined (key, value) data that provides additional information about the log entry.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`operation` |  `object (`[LogEntryOperation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#LogEntryOperation)`)` Optional. Information about an operation associated with the log entry, if applicable.  
`sourceLocation` |  `object (`[LogEntrySourceLocation](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#LogEntrySourceLocation)`)` Optional. Source code location information associated with the log entry, if any.  
Union field `payload`. The log entry payload, which can be one of multiple types. `payload` can be only one of the following:  
`protoPayload` |  `object` The log entry payload, represented as a protocol buffer that is expressed as a JSON object. The only accepted type currently is `[AuditLog](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog)`.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`textPayload` |  `string` The log entry payload, represented as a Unicode string (UTF-8).  
`structPayload` |  `object (`[Struct](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Struct)` format)` The log entry payload, represented as a structure that is expressed as a JSON object.  
  
## LogSeverity

The severity of the event described in a log entry, expressed as one of the standard severity levels listed below. For your reference, the levels are assigned the listed numeric values. The effect of using numeric values other than those listed is undefined.

You can filter for log entries by severity. For example, the following filter expression will match log entries with severities `INFO`, `NOTICE`, and `WARNING`:
    
    
    severity > DEBUG AND severity <= WARNING
    

If you are writing log entries, you should map other severity encodings to one of these standard levels. For example, you might map all of Java's FINE, FINER, and FINEST levels to `LogSeverity.DEBUG`. You can preserve the original severity level in the log entry payload if you wish.

Enums  
---  
`DEFAULT` | (0) The log entry has no assigned severity level.  
`DEBUG` | (100) Debug or trace information.  
`INFO` | (200) Routine information, such as ongoing status or performance.  
`NOTICE` | (300) Normal but significant events, such as start up, shut down, or a configuration change.  
`WARNING` | (400) Warning events might cause problems.  
`ERROR` | (500) Error events are likely to cause problems.  
`CRITICAL` | (600) Critical events cause more severe problems or outages.  
`ALERT` | (700) A person must take an action immediately.  
`EMERGENCY` | (800) One or more systems are unusable.  
  
## HttpRequest

A common proto for logging HTTP requests. Only contains semantics defined by the HTTP specification. Product-specific logging information MUST be defined in a separate message.

JSON representation  
---  
      
    
    {
      "requestMethod": string,
      "requestUrl": string,
      "requestSize": string,
      "status": integer,
      "responseSize": string,
      "userAgent": string,
      "remoteIp": string,
      "serverIp": string,
      "referer": string,
      "latency": string,
      "cacheLookup": boolean,
      "cacheHit": boolean,
      "cacheValidatedWithOriginServer": boolean,
      "cacheFillBytes": string,
      "protocol": string
    }  
  
Fields  
---  
`requestMethod` |  `string` The request method. Examples: `"GET"`, `"HEAD"`, `"PUT"`, `"POST"`.  
`requestUrl` |  `string` The scheme (http, https), the host name, the path, and the query portion of the URL that was requested. Example: `"http://example.com/some/info?color=red"`.  
`requestSize` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The size of the HTTP request message in bytes, including the request headers and the request body.  
`status` |  `integer` The response code indicating the status of the response. Examples: 200, 404.  
`responseSize` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The size of the HTTP response message sent back to the client, in bytes, including the response headers and the response body.  
`userAgent` |  `string` The user agent sent by the client. Example: `"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)"`.  
`remoteIp` |  `string` The IP address (IPv4 or IPv6) of the client that issued the HTTP request. Examples: `"192.168.1.1"`, `"FE80::0202:B3FF:FE1E:8329"`.  
`serverIp` |  `string` The IP address (IPv4 or IPv6) of the origin server that the request was sent to.  
`referer` |  `string` The referer URL of the request, as defined in [HTTP/1.1 Header Field Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).  
`latency` |  `string (`[Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration)` format)` The request processing latency on the server, from the time the request was received until the response was sent.A duration in seconds with up to nine fractional digits, terminated by '`s`'. Example: `"3.5s"`.  
`cacheLookup` |  `boolean` Whether or not a cache lookup was attempted.  
`cacheHit` |  `boolean` Whether or not an entity was served from cache (with or without validation).  
`cacheValidatedWithOriginServer` |  `boolean` Whether or not the response was validated with the origin server before being served from cache. This field is only meaningful if `cacheHit` is True.  
`cacheFillBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of HTTP response bytes inserted into cache. Set only when a cache fill was attempted.  
`protocol` |  `string` Protocol used for the request. Examples: "HTTP/1.1", "HTTP/2", "websocket"  
  
## LogEntryOperation

Additional information about a potentially long-running operation with which a log entry is associated.

JSON representation  
---  
      
    
    {
      "id": string,
      "producer": string,
      "first": boolean,
      "last": boolean
    }  
  
Fields  
---  
`id` |  `string` Optional. An arbitrary operation identifier. Log entries with the same identifier are assumed to be part of the same operation.  
`producer` |  `string` Optional. An arbitrary producer identifier. The combination of `id` and `producer` must be globally unique. Examples for `producer`: `"MyDivision.MyBigCompany.com"`, `"github.com/MyProject/MyApplication"`.  
`first` |  `boolean` Optional. Set this to True if this is the first log entry in the operation.  
`last` |  `boolean` Optional. Set this to True if this is the last log entry in the operation.  
  
## LogEntrySourceLocation

Additional information about the source code location that produced the log entry.

JSON representation  
---  
      
    
    {
      "file": string,
      "line": string,
      "function": string
    }  
  
Fields  
---  
`file` |  `string` Optional. Source file name. Depending on the runtime environment, this might be a simple name or a fully-qualified name.  
`line` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Line within the source file. 1-based; 0 indicates no line number available.  
`function` |  `string` Optional. Human-readable name of the function or method being invoked, with optional context such as the class or package name. This information may be used in contexts such as the logs viewer, where a file and line number are less meaningful. The format can vary by language. For example: `qual.if.ied.Class.method` (Java), `dir/package.func` (Go), `function` (Python).  
  
## Importance

Defines the importance of the data contained in the operation.

Enums  
---  
`LOW` | Allows data caching, batching, and aggregation. It provides higher performance with higher data loss risk.  
`HIGH` | Disables data aggregation to minimize data loss. It is for operations that contains significant monetary value or audit trail. This feature only applies to the client libraries.  
  
## TraceSpan

A span represents a single operation within a trace. Spans can be nested to form a trace tree. Often, a trace contains a root span that describes the end-to-end latency, and one or more subspans for its sub-operations. A trace can also contain multiple root spans, or none at all. Spans do not need to be contiguous—there may be gaps or overlaps between spans in a trace.

JSON representation  
---  
      
    
    {
      "name": string,
      "spanId": string,
      "parentSpanId": string,
      "displayName": {
        object ([TruncatableString](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AttributeValue#TruncatableString))
      },
      "startTime": string,
      "endTime": string,
      "attributes": {
        object ([Attributes](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#Attributes))
      },
      "status": {
        object ([Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Status))
      },
      "sameProcessAsParentSpan": boolean,
      "childSpanCount": integer,
      "spanKind": enum ([SpanKind](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#SpanKind))
    }  
  
Fields  
---  
`name` |  `string` The resource name of the span in the following format:
    
    
    projects/[PROJECT_ID]/traces/[TRACE_ID]/spans/[SPAN_ID]
    

[TRACE_ID] is a unique identifier for a trace within a project; it is a 32-character hexadecimal encoding of a 16-byte array.[SPAN_ID] is a unique identifier for a span within a trace; it is a 16-character hexadecimal encoding of an 8-byte array.  
`spanId` |  `string` The [SPAN_ID] portion of the span's resource name.  
`parentSpanId` |  `string` The [SPAN_ID] of this span's parent span. If this is a root span, then this field must be empty.  
`displayName` |  `object (`[TruncatableString](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AttributeValue#TruncatableString)`)` A description of the span's operation (up to 128 bytes). Stackdriver Trace displays the description in the Google Cloud Platform Console. For example, the display name can be a qualified method name or a file name and a line number where the operation is called. A best practice is to use the same display name within an application and at the same call point. This makes it easier to correlate spans in different traces.  
`startTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The start time of the span. On the client side, this is the time kept by the local machine where the span execution starts. On the server side, this is the time when the server's application handler starts running.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` The end time of the span. On the client side, this is the time kept by the local machine where the span execution ends. On the server side, this is the time when the server application handler stops running.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`attributes` |  `object (`[Attributes](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#Attributes)`)` A set of attributes on the span. You can have up to 32 attributes per span.  
`status` |  `object (`[Status](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AuditLog#Status)`)` An optional final status for this span.  
`sameProcessAsParentSpan` |  `boolean` (Optional) Set this parameter to indicate whether this span is in the same process as its parent. If you do not set this parameter, Stackdriver Trace is unable to take advantage of this helpful information.  
`childSpanCount` |  `integer` An optional number of child spans that were generated while this span was active. If set, allows implementation to detect missing child spans.  
`spanKind` |  `enum (`[SpanKind](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/v1/Operation#SpanKind)`)` Distinguishes between spans generated in a particular context. For example, two spans with the same name may be distinguished using `CLIENT` (caller) and `SERVER` (callee) to identify an RPC call.  
  
## Attributes

A set of attributes, each in the format `[KEY]:[VALUE]`.

JSON representation  
---  
      
    
    {
      "attributeMap": {
        string: {
          object ([AttributeValue](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AttributeValue))
        },
        ...
      },
      "droppedAttributesCount": integer
    }  
  
Fields  
---  
`attributeMap` |  `map (key: string, value: object (`[AttributeValue](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rest/Shared.Types/AttributeValue)`))` The set of attributes. Each attribute's key can be up to 128 bytes long. The value can be a string up to 256 bytes, a signed 64-bit integer, or the Boolean values `true` and `false`. For example:
    
    
    "/instance_id": "my-instance"
    "/http/userAgent": ""
    "/http/request_bytes": 300
    "example.com/myattribute": true
    

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`droppedAttributesCount` |  `integer` The number of attributes that were discarded. Attributes can be discarded because their keys are too long or because there are too many attributes. If this value is 0 then all attributes are valid.  
  
## SpanKind

Type of span. Can be used to specify additional relationships between spans in addition to a parent/child relationship.

Enums  
---  
`SPAN_KIND_UNSPECIFIED` | Unspecified. Do NOT use as default. Implementations MAY assume SpanKind.INTERNAL to be default.  
`INTERNAL` | Indicates that the span is used internally. Default value.  
`SERVER` | Indicates that the span covers server-side handling of an RPC or other remote network request.  
`CLIENT` | Indicates that the span covers the client-side wrapper around an RPC or other remote request.  
`PRODUCER` | Indicates that the span describes producer sending a message to a broker. Unlike client and server, there is no direct critical path latency relationship between producer and consumer spans (e.g. publishing a message to a pubsub service).  
`CONSUMER` | Indicates that the span describes consumer receiving a message from a broker. Unlike client and server, there is no direct critical path latency relationship between producer and consumer spans (e.g. receiving a message from a pubsub service subscription).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
