---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1
title: Package google.api.servicecontrol.v1 \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:47.633258+00:00
---

# Package google.api.servicecontrol.v1  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  Package google.api.servicecontrol.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Distribution](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution)` (message)
  * `[Distribution.ExplicitBuckets](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.ExplicitBuckets)` (message)
  * `[Distribution.ExponentialBuckets](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.ExponentialBuckets)` (message)
  * `[Distribution.LinearBuckets](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.LinearBuckets)` (message)
  * `[HttpRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.HttpRequest)` (message)
  * `[LogEntry](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntry)` (message)
  * `[LogEntryOperation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntryOperation)` (message)
  * `[LogEntrySourceLocation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntrySourceLocation)` (message)
  * `[MetricValue](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.MetricValue)` (message)
  * `[MetricValueSet](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.MetricValueSet)` (message)
  * `[Operation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation)` (message)
  * `[Operation.Importance](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.Importance)` (enum)
  * `[Operation.ResourceInfo](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.ResourceInfo)` (message)
  * `[QuotaProperties](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaProperties)` (message)
  * `[QuotaProperties.QuotaMode](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaProperties.QuotaMode)` (enum)
  * `[ReportRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.ReportRequest)` (message)
  * `[TraceSpan](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan)` (message)
  * `[TraceSpan.AttributeValue](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.AttributeValue)` (message)
  * `[TraceSpan.Attributes](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.Attributes)` (message)
  * `[TraceSpan.SpanKind](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.SpanKind)` (enum)
  * `[TruncatableString](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TruncatableString)` (message)



## Distribution

Distribution represents a frequency distribution of double-valued sample points. It contains the size of the population of sample points plus additional optional information:

  * the arithmetic mean of the samples
  * the minimum and maximum of the samples
  * the sum-squared-deviation of the samples, used to compute variance
  * a histogram of the values of the sample points

Fields  
---  
`count` |  `int64` The total number of samples in the distribution. Must be >= 0.  
`mean` |  `double` The arithmetic mean of the samples in the distribution. If `count` is zero then this field must be zero.  
`minimum` |  `double` The minimum of the population of values. Ignored if `count` is zero.  
`maximum` |  `double` The maximum of the population of values. Ignored if `count` is zero.  
`sum_of_squared_deviation` |  `double` The sum of squared deviations from the mean: Sum[i=1..count]((x_i - mean)^2) where each x_i is a sample values. If `count` is zero then this field must be zero, otherwise validation of the request fails.  
`bucket_counts[]` |  `int64` The number of samples in each histogram bucket. `bucket_counts` are optional. If present, they must sum to the `count` value.The buckets are defined below in `bucket_option`. There are N buckets. `bucket_counts[0]` is the number of samples in the underflow bucket. `bucket_counts[1]` to `bucket_counts[N-1]` are the numbers of samples in each of the finite buckets. And `bucket_counts[N]` is the number of samples in the overflow bucket. See the comments of `bucket_option` below for more details.Any suffix of trailing zeros may be omitted.  
`exemplars[]` |  `[Exemplar](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api#google.api.Distribution.Exemplar)` Example points. Must be in increasing order of `value` field.  
Union field `bucket_option`. Defines the buckets in the histogram. `bucket_option` and `bucket_counts` must be both set, or both unset.Buckets are numbered in the range of [0, N], with a total of N+1 buckets. There must be at least two buckets (a single-bucket histogram gives no information that isn't already provided by `count`).The first bucket is the underflow bucket which has a lower bound of -inf. The last bucket is the overflow bucket which has an upper bound of +inf. All other buckets (if any) are called "finite" buckets because they have finite lower and upper bounds. As described below, there are three ways to define the finite buckets.(1) Buckets with constant width. (2) Buckets with exponentially growing widths. (3) Buckets with arbitrary user-provided widths.In all cases, the buckets cover the entire real number line (-inf, +inf). Bucket upper bounds are exclusive and lower bounds are inclusive. The upper bound of the underflow bucket is equal to the lower bound of the smallest finite bucket; the lower bound of the overflow bucket is equal to the upper bound of the largest finite bucket. `bucket_option` can be only one of the following:  
`linear_buckets` |  `[LinearBuckets](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.LinearBuckets)` Buckets with constant width.  
`exponential_buckets` |  `[ExponentialBuckets](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.ExponentialBuckets)` Buckets with exponentially growing width.  
`explicit_buckets` |  `[ExplicitBuckets](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution.ExplicitBuckets)` Buckets with arbitrary user-provided width.  
  
## ExplicitBuckets

Describing buckets with arbitrary user-provided width.

Fields  
---  
`bounds[]` |  `double` 'bound' is a list of strictly increasing boundaries between buckets. Note that a list of length N-1 defines N buckets because of fenceposting. See comments on `bucket_options` for details.The i'th finite bucket covers the interval [bound[i-1], bound[i]) where i ranges from 1 to bound_size() - 1. Note that there are no finite buckets at all if 'bound' only contains a single element; in that special case the single bound defines the boundary between the underflow and overflow buckets.bucket number lower bound upper bound i == 0 (underflow) -inf bound[i] 0 < i < bound_size() bound[i-1] bound[i] i == bound_size() (overflow) bound[i-1] +inf  
  
## ExponentialBuckets

Describing buckets with exponentially growing width.

Fields  
---  
`num_finite_buckets` |  `int32` The number of finite buckets. With the underflow and overflow buckets, the total number of buckets is `num_finite_buckets` \+ 2. See comments on `bucket_options` for details.  
`growth_factor` |  `double` The i'th exponential bucket covers the interval [scale * growth_factor^(i-1), scale * growth_factor^i) where i ranges from 1 to num_finite_buckets inclusive. Must be larger than 1.0.  
`scale` |  `double` The i'th exponential bucket covers the interval [scale * growth_factor^(i-1), scale * growth_factor^i) where i ranges from 1 to num_finite_buckets inclusive. Must be > 0.  
  
## LinearBuckets

Describing buckets with constant width.

Fields  
---  
`num_finite_buckets` |  `int32` The number of finite buckets. With the underflow and overflow buckets, the total number of buckets is `num_finite_buckets` \+ 2. See comments on `bucket_options` for details.  
`width` |  `double` The i'th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to num_finite_buckets, inclusive. Must be strictly positive.  
`offset` |  `double` The i'th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to num_finite_buckets, inclusive.  
  
## HttpRequest

A common proto for logging HTTP requests. Only contains semantics defined by the HTTP specification. Product-specific logging information MUST be defined in a separate message.

Fields  
---  
`request_method` |  `string` The request method. Examples: `"GET"`, `"HEAD"`, `"PUT"`, `"POST"`.  
`request_url` |  `string` The scheme (http, https), the host name, the path, and the query portion of the URL that was requested. Example: `"http://example.com/some/info?color=red"`.  
`request_size` |  `int64` The size of the HTTP request message in bytes, including the request headers and the request body.  
`status` |  `int32` The response code indicating the status of the response. Examples: 200, 404.  
`response_size` |  `int64` The size of the HTTP response message sent back to the client, in bytes, including the response headers and the response body.  
`user_agent` |  `string` The user agent sent by the client. Example: `"Mozilla/4.0 (compatible; MSIE 6.0; Windows 98; Q312461; .NET CLR 1.0.3705)"`.  
`remote_ip` |  `string` The IP address (IPv4 or IPv6) of the client that issued the HTTP request. Examples: `"192.168.1.1"`, `"FE80::0202:B3FF:FE1E:8329"`.  
`server_ip` |  `string` The IP address (IPv4 or IPv6) of the origin server that the request was sent to.  
`referer` |  `string` The referer URL of the request, as defined in [HTTP/1.1 Header Field Definitions](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).  
`latency` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The request processing latency on the server, from the time the request was received until the response was sent.  
`cache_lookup` |  `bool` Whether or not a cache lookup was attempted.  
`cache_hit` |  `bool` Whether or not an entity was served from cache (with or without validation).  
`cache_validated_with_origin_server` |  `bool` Whether or not the response was validated with the origin server before being served from cache. This field is only meaningful if `cache_hit` is True.  
`cache_fill_bytes` |  `int64` The number of HTTP response bytes inserted into cache. Set only when a cache fill was attempted.  
`protocol` |  `string` Protocol used for the request. Examples: "HTTP/1.1", "HTTP/2", "websocket"  
  
## LogEntry

An individual log entry.

Fields  
---  
`name` |  `string` Required. The log to which this log entry belongs. Examples: `"syslog"`, `"book_log"`.  
`timestamp` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the event described by the log entry occurred. If omitted, defaults to operation start time.  
`severity` |  `[LogSeverity](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.logging.type#google.logging.type.LogSeverity)` The severity of the log entry. The default value is `LogSeverity.DEFAULT`.  
`http_request` |  `[HttpRequest](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.HttpRequest)` Optional. Information about the HTTP request associated with this log entry, if applicable.  
`trace` |  `string` Optional. Resource name of the trace associated with the log entry, if any. If this field contains a relative resource name, you can assume the name is relative to `//tracing.googleapis.com`. Example: `projects/my-projectid/traces/06796866738c859f2f19b7cfb3214824`  
`insert_id` |  `string` A unique ID for the log entry used for deduplication. If omitted, the implementation will generate one based on operation_id.  
`labels` |  `map<string, string>` A set of user-defined (key, value) data that provides additional information about the log entry.  
`operation` |  `[LogEntryOperation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntryOperation)` Optional. Information about an operation associated with the log entry, if applicable.  
`source_location` |  `[LogEntrySourceLocation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntrySourceLocation)` Optional. Source code location information associated with the log entry, if any.  
Union field `payload`. The log entry payload, which can be one of multiple types. `payload` can be only one of the following:  
`proto_payload` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` The log entry payload, represented as a protocol buffer that is expressed as a JSON object. The only accepted type currently is `AuditLog`.  
`text_payload` |  `string` The log entry payload, represented as a Unicode string (UTF-8).  
`struct_payload` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` The log entry payload, represented as a structure that is expressed as a JSON object.  
  
## LogEntryOperation

Additional information about a potentially long-running operation with which a log entry is associated.

Fields  
---  
`id` |  `string` Optional. An arbitrary operation identifier. Log entries with the same identifier are assumed to be part of the same operation.  
`producer` |  `string` Optional. An arbitrary producer identifier. The combination of `id` and `producer` must be globally unique. Examples for `producer`: `"MyDivision.MyBigCompany.com"`, `"github.com/MyProject/MyApplication"`.  
`first` |  `bool` Optional. Set this to True if this is the first log entry in the operation.  
`last` |  `bool` Optional. Set this to True if this is the last log entry in the operation.  
  
## LogEntrySourceLocation

Additional information about the source code location that produced the log entry.

Fields  
---  
`file` |  `string` Optional. Source file name. Depending on the runtime environment, this might be a simple name or a fully-qualified name.  
`line` |  `int64` Optional. Line within the source file. 1-based; 0 indicates no line number available.  
`function` |  `string` Optional. Human-readable name of the function or method being invoked, with optional context such as the class or package name. This information may be used in contexts such as the logs viewer, where a file and line number are less meaningful. The format can vary by language. For example: `qual.if.ied.Class.method` (Java), `dir/package.func` (Go), `function` (Python).  
  
## MetricValue

Represents a single metric value.

Fields  
---  
`labels` |  `map<string, string>` The labels describing the metric value. See comments on `[google.api.servicecontrol.v1.Operation.labels](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.FIELDS.repeated.google.api.servicecontrol.v1.Operation.LabelsEntry.google.api.servicecontrol.v1.Operation.labels)` for the overriding relationship. Note that this map must not contain monitored resource labels.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The start of the time period over which this metric value's measurement applies. The time period has different semantics for different metric types (cumulative, delta, and gauge). See the metric definition documentation in the service configuration for details. If not specified, `[google.api.servicecontrol.v1.Operation.start_time](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.FIELDS.google.protobuf.Timestamp.google.api.servicecontrol.v1.Operation.start_time)` will be used.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The end of the time period over which this metric value's measurement applies. If not specified, `[google.api.servicecontrol.v1.Operation.end_time](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.FIELDS.google.protobuf.Timestamp.google.api.servicecontrol.v1.Operation.end_time)` will be used.  
Union field `value`. The value. The type of value used in the request must agree with the metric definition in the service configuration, otherwise the MetricValue is rejected. `value` can be only one of the following:  
`bool_value` |  `bool` A boolean value.  
`int64_value` |  `int64` A signed 64-bit integer value.  
`double_value` |  `double` A double precision floating point value.  
`string_value` |  `string` A text string value.  
`distribution_value` |  `[Distribution](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Distribution)` A distribution value.  
`money_value` |  `[Money](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.type#google.type.Money)` A money value.  
  
## MetricValueSet

Represents a set of metric values in the same metric. Each metric value in the set should have a unique combination of start time, end time, and label values.

Fields  
---  
`metric_name` |  `string` The metric name defined in the service configuration.  
`metric_values[]` |  `[MetricValue](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.MetricValue)` The values in this metric.  
  
## Operation

Represents information regarding an operation.

Fields  
---  
`operation_id` |  `string` Identity of the operation. This must be unique within the scope of the service that generated the operation. If the service calls Check() and Report() on the same operation, the two calls should carry the same id.UUID version 4 is recommended, though not required. In scenarios where an operation is computed from existing information and an idempotent id is desirable for deduplication purpose, UUID version 5 is recommended. See RFC 4122 for details.  
`operation_name` |  `string` Fully qualified name of the operation. Reserved for future use.  
`consumer_id` |  `string` Identity of the consumer who is using the service. This field should be filled in for the operations initiated by a consumer, but not for service-initiated operations that are not related to a specific consumer.

  * This can be in one of the following formats: 
    * project:PROJECT_ID,
    * project`_`number:PROJECT_NUMBER,
    * projects/PROJECT_ID or PROJECT_NUMBER,
    * folders/FOLDER_NUMBER,
    * organizations/ORGANIZATION_NUMBER,
    * api`_`key:API_KEY.

  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Required. Start time of the operation.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` End time of the operation. Required when the operation is used in `ServiceController.Report`, but optional when the operation is used in `ServiceController.Check`.  
`labels` |  `map<string, string>` Labels describing the operation. Only the following labels are allowed:

  * Labels describing monitored resources as defined in the service configuration.
  * Default labels of metric values. When specified, labels defined in the metric value override these default.
  * The following labels defined by Google Cloud Platform: 
    * `cloud.googleapis.com/location` describing the location where the operation happened,
    * `servicecontrol.googleapis.com/user_agent` describing the user agent of the API request,
    * `servicecontrol.googleapis.com/service_agent` describing the service used to handle the API request (e.g. ESP),
    * `servicecontrol.googleapis.com/platform` describing the platform where the API is served, such as App Engine, Compute Engine, or Kubernetes Engine.

  
`metric_value_sets[]` |  `[MetricValueSet](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.MetricValueSet)` Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition.Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error.  
`log_entries[]` |  `[LogEntry](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.LogEntry)` Represents information to be logged.  
`quota_properties` |  `[QuotaProperties](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaProperties)` Represents the properties needed for quota check. Applicable only if this operation is for a quota check request. If this is not specified, no quota check will be performed.  
`importance` |  `[Importance](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.Importance)` DO NOT USE. This is an experimental field.  
`user_labels` |  `map<string, string>` Private Preview. This feature is only available for approved services.User defined labels for the resource that this operation is associated with.  
`resources[]` |  `[ResourceInfo](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation.ResourceInfo)` The resources that are involved in the operation. The maximum supported number of entries in this field is 100.  
`trace_spans[]` |  `[TraceSpan](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan)` Unimplemented. A list of Cloud Trace spans. The span names shall contain the id of the destination project which can be either the produce or the consumer project.  
  
## Importance

Defines the importance of the data contained in the operation.

Enums  
---  
`LOW` | Allows data caching, batching, and aggregation. It provides higher performance with higher data loss risk.  
`HIGH` | Disables data aggregation to minimize data loss. It is for operations that contains significant monetary value or audit trail. This feature only applies to the client libraries.  
`DEBUG` | Deprecated. Do not use.Disables data aggregation and enables additional validation logic. It should only be used during the onboarding process. It is only available to Google internal services, and the service must be approved by [chemist-dev@google.com](mailto:chemist-dev@google.com) in order to use this level.  
`PROMOTED` | Used internally by Chemist.  
  
## ResourceInfo

Describes a resource associated with this operation.

Fields  
---  
`resource_container` |  `string` The identifier of the parent of this resource instance. Must be in one of the following formats: - `projects/<project-id or project-number>` \- `folders/<folder-id>` \- `organizations/<organization-id>`  
`resource_name` |  `string` Name of the resource. This is used for auditing purposes.  
`resource_location` |  `string` The location of the resource. If not empty, the resource will be checked against location policy. The value must be a valid zone, region or multiregion. For example: "europe-west4" or "northamerica-northeast1-a"  
`permission` |  `string` The resource permission required for this request.  
  
## QuotaProperties

Represents the properties needed for quota operations.

Fields  
---  
`quota_mode` |  `[QuotaMode](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.QuotaProperties.QuotaMode)` Quota mode for this operation.  
  
## QuotaMode

Supported quota enforcement modes.

Enums  
---  
`ACQUIRE` | Decreases available quota by the cost specified for the operation. If cost is higher than available quota, operation fails and returns error.  
`ACQUIRE_BEST_EFFORT` | Decreases available quota by the cost specified for the operation. If cost is higher than available quota, operation does not fail and available quota goes down to zero but it returns error.  
`CHECK` | Does not change any available quota. Only checks if there is enough quota. No lock is placed on the checked tokens neither.  
  
## ReportRequest

Request message for the Report method.

Fields  
---  
`service_name` |  `string` The service name as specified in its service configuration. For example, `"pubsub.googleapis.com"`.See [google.api.Service](https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service) for the definition of a service name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `serviceName`:

  * `servicemanagement.services.report`

  
`operations[]` |  `[Operation](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.Operation)` Operations to be reported.Typically the service should report one operation per request. Putting multiple operations into a single request is allowed, but should be used only when multiple operations are natually available at the time of the report.There is no limit on the number of operations in the same ReportRequest, however the ReportRequest size should be no larger than 1MB. See `ReportResponse.report_errors` for partial failure behavior.  
`service_config_id` |  `string` Specifies which version of service config should be used to process the request.If unspecified or no matching version can be found, the latest one will be used.  
  
## TraceSpan

A span represents a single operation within a trace. Spans can be nested to form a trace tree. Often, a trace contains a root span that describes the end-to-end latency, and one or more subspans for its sub-operations. A trace can also contain multiple root spans, or none at all. Spans do not need to be contiguous—there may be gaps or overlaps between spans in a trace.

Fields  
---  
`name` |  `string` The resource name of the span in the following format:
    
    
    projects/[PROJECT_ID]/traces/[TRACE_ID]/spans/[SPAN_ID]
    

[TRACE_ID] is a unique identifier for a trace within a project; it is a 32-character hexadecimal encoding of a 16-byte array.[SPAN_ID] is a unique identifier for a span within a trace; it is a 16-character hexadecimal encoding of an 8-byte array.  
`span_id` |  `string` The [SPAN_ID] portion of the span's resource name.  
`parent_span_id` |  `string` The [SPAN_ID] of this span's parent span. If this is a root span, then this field must be empty.  
`display_name` |  `[TruncatableString](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TruncatableString)` A description of the span's operation (up to 128 bytes). Stackdriver Trace displays the description in the Google Cloud Platform Console. For example, the display name can be a qualified method name or a file name and a line number where the operation is called. A best practice is to use the same display name within an application and at the same call point. This makes it easier to correlate spans in different traces.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The start time of the span. On the client side, this is the time kept by the local machine where the span execution starts. On the server side, this is the time when the server's application handler starts running.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The end time of the span. On the client side, this is the time kept by the local machine where the span execution ends. On the server side, this is the time when the server application handler stops running.  
`attributes` |  `[Attributes](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.Attributes)` A set of attributes on the span. You can have up to 32 attributes per span.  
`status` |  `[Status](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.rpc#google.rpc.Status)` An optional final status for this span.  
`same_process_as_parent_span` |  `[BoolValue](https://protobuf.dev/reference/protobuf/google.protobuf/#bool-value)` (Optional) Set this parameter to indicate whether this span is in the same process as its parent. If you do not set this parameter, Stackdriver Trace is unable to take advantage of this helpful information.  
`child_span_count` |  `[Int32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#int32-value)` An optional number of child spans that were generated while this span was active. If set, allows implementation to detect missing child spans.  
`span_kind` |  `[SpanKind](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.SpanKind)` Distinguishes between spans generated in a particular context. For example, two spans with the same name may be distinguished using `CLIENT` (caller) and `SERVER` (callee) to identify an RPC call.  
  
## AttributeValue

The allowed types for [VALUE] in a `[KEY]:[VALUE]` attribute.

Fields  
---  
Union field `value`. The type of the value. `value` can be only one of the following:  
`string_value` |  `[TruncatableString](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TruncatableString)` A string up to 256 bytes long.  
`int_value` |  `int64` A 64-bit signed integer.  
`bool_value` |  `bool` A Boolean value represented by `true` or `false`.  
  
## Attributes

A set of attributes, each in the format `[KEY]:[VALUE]`.

Fields  
---  
`attribute_map` |  `map<string, `[AttributeValue](https://docs.cloud.google.com/fault-injection-testing/reference/rpc/google.api/servicecontrol.v1#google.api.servicecontrol.v1.TraceSpan.AttributeValue)`>` The set of attributes. Each attribute's key can be up to 128 bytes long. The value can be a string up to 256 bytes, a signed 64-bit integer, or the Boolean values `true` and `false`. For example:
    
    
    "/instance_id": "my-instance"
    "/http/user_agent": ""
    "/http/request_bytes": 300
    "example.com/myattribute": true
      
  
`dropped_attributes_count` |  `int32` The number of attributes that were discarded. Attributes can be discarded because their keys are too long or because there are too many attributes. If this value is 0 then all attributes are valid.  
  
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
  
## TruncatableString

Represents a string that might be shortened to a specified length.

Fields  
---  
`value` |  `string` The shortened string. For example, if the original string is 500 bytes long and the limit of the string is 128 bytes, then `value` contains the first 128 bytes of the 500-byte string.Truncation always happens on a UTF8 character boundary. If there are multi-byte characters in the string, then the length of the shortened string might be less than the size limit.  
`truncated_byte_count` |  `int32` The number of bytes removed from the original string. If this value is 0, then the string was not shortened.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-21 UTC."],[],[]] 
