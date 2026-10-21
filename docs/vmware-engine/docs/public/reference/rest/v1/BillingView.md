---
url: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView/
title: BillingView \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:58:56.127008+00:00
---

# BillingView  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest)



Send feedback 

#  BillingView Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ReportRequest
    * JSON representation
  * Operation
    * JSON representation
  * MetricValueSet
    * JSON representation
  * MetricValue
    * JSON representation
  * Distribution
    * JSON representation
  * LinearBuckets
    * JSON representation
  * ExponentialBuckets
    * JSON representation
  * ExplicitBuckets
    * JSON representation
  * Exemplar
    * JSON representation
  * Money
    * JSON representation
  * LogEntry
    * JSON representation
  * HttpRequest
    * JSON representation
  * LogEntryOperation
    * JSON representation
  * LogEntrySourceLocation
    * JSON representation
  * QuotaProperties
    * JSON representation
  * ResourceInfo
    * JSON representation
  * TraceSpan
    * JSON representation
  * TruncatableString
    * JSON representation
  * Attributes
    * JSON representation
  * AttributeValue
    * JSON representation



Message for reporting billing requests through Eventstream.

JSON representation  
---  
      
    
    {
      "reportRequests": [
        {
          object ([ReportRequest](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#ReportRequest))
        }
      ]
    }  
  
Fields  
---  
`reportRequests[]` |  `object (`[ReportRequest](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#ReportRequest)`)` Billing requests to be reported for cloud.eventstream.v2.ResourceEvent  
  
## ReportRequest

Request message for the services.report method.

JSON representation  
---  
      
    
    {
      "serviceName": string,
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Operation))
        }
      ],
      "serviceConfigId": string
    }  
  
Fields  
---  
`serviceName` |  `string` The service name as specified in its service configuration. For example, `"pubsub.googleapis.com"`.See [google.api.Service](https://cloud.google.com/service-management/reference/rpc/google.api#google.api.Service) for the definition of a service name.  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Operation)`)` Operations to be reported.Typically the service should report one operation per request. Putting multiple operations into a single request is allowed, but should be used only when multiple operations are natually available at the time of the report.There is no limit on the number of operations in the same ReportRequest, however the ReportRequest size should be no larger than 1MB. See `ReportResponse.report_errors` for partial failure behavior.  
`serviceConfigId` |  `string` Specifies which version of service config should be used to process the request.If unspecified or no matching version can be found, the latest one will be used.  
  
## Operation

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
          object ([MetricValueSet](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#MetricValueSet))
        }
      ],
      "logEntries": [
        {
          object ([LogEntry](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#LogEntry))
        }
      ],
      "quotaProperties": {
        object ([QuotaProperties](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#QuotaProperties))
      },
      "importance": enum ([Importance](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/Importance)),
      "userLabels": {
        string: string,
        ...
      },
      "resources": [
        {
          object ([ResourceInfo](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#ResourceInfo))
        }
      ],
      "traceSpans": [
        {
          object ([TraceSpan](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#TraceSpan))
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

  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. Start time of the operation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` End time of the operation. Required when the operation is used in `ServiceController.Report`, but optional when the operation is used in `ServiceController.Check`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Labels describing the operation. Only the following labels are allowed:

  * Labels describing monitored resources as defined in the service configuration.
  * Default labels of metric values. When specified, labels defined in the metric value override these default.
  * The following labels defined by Google Cloud Platform: 
    * `cloud.googleapis.com/location` describing the location where the operation happened,
    * `servicecontrol.googleapis.com/userAgent` describing the user agent of the API request,
    * `servicecontrol.googleapis.com/service_agent` describing the service used to handle the API request (e.g. ESP),
    * `servicecontrol.googleapis.com/platform` describing the platform where the API is served, such as App Engine, Compute Engine, or Kubernetes Engine.

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`metricValueSets[]` |  `object (`[MetricValueSet](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#MetricValueSet)`)` Represents information about this operation. Each MetricValueSet corresponds to a metric defined in the service configuration. The data type used in the MetricValueSet must agree with the data type specified in the metric definition.Within a single operation, it is not allowed to have more than one MetricValue instances that have the same metric names and identical label value combinations. If a request has such duplicated MetricValue instances, the entire request is rejected with an invalid argument error.  
`logEntries[]` |  `object (`[LogEntry](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#LogEntry)`)` Represents information to be logged.  
`quotaProperties` |  `object (`[QuotaProperties](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#QuotaProperties)`)` Represents the properties needed for quota check. Applicable only if this operation is for a quota check request. If this is not specified, no quota check will be performed.  
`importance` |  `enum (`[Importance](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/Importance)`)` DO NOT USE. This is an experimental field.  
`userLabels` |  `map (key: string, value: string)` Private Preview. This feature is only available for approved services.User defined labels for the resource that this operation is associated with.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`resources[]` |  `object (`[ResourceInfo](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#ResourceInfo)`)` The resources that are involved in the operation. The maximum supported number of entries in this field is 100.  
`traceSpans[]` |  `object (`[TraceSpan](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#TraceSpan)`)` Unimplemented. A list of Cloud Trace spans. The span names shall contain the id of the destination project which can be either the produce or the consumer project.  
  
## MetricValueSet

Represents a set of metric values in the same metric. Each metric value in the set should have a unique combination of start time, end time, and label values.

JSON representation  
---  
      
    
    {
      "metricName": string,
      "metricValues": [
        {
          object ([MetricValue](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#MetricValue))
        }
      ]
    }  
  
Fields  
---  
`metricName` |  `string` The metric name defined in the service configuration.  
`metricValues[]` |  `object (`[MetricValue](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#MetricValue)`)` The values in this metric.  
  
## MetricValue

Represents a single metric value.

JSON representation  
---  
      
    
    {
      "labels": {
        string: string,
        ...
      },
      "startTime": string,
      "endTime": string,
    
      // Union field value can be only one of the following:
      "boolValue": boolean,
      "int64Value": string,
      "doubleValue": number,
      "stringValue": string,
      "distributionValue": {
        object ([Distribution](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Distribution))
      },
      "moneyValue": {
        object ([Money](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Money))
      }
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
`labels` |  `map (key: string, value: string)` The labels describing the metric value. See comments on `[google.api.servicecontrol.v1.Operation.labels](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Operation.FIELDS.labels)` for the overriding relationship. Note that this map must not contain monitored resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The start of the time period over which this metric value's measurement applies. The time period has different semantics for different metric types (cumulative, delta, and gauge). See the metric definition documentation in the service configuration for details. If not specified, `[google.api.servicecontrol.v1.Operation.start_time](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Operation.FIELDS.start_time)` will be used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The end of the time period over which this metric value's measurement applies. If not specified, `[google.api.servicecontrol.v1.Operation.end_time](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Operation.FIELDS.end_time)` will be used.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `value`. The value. The type of value used in the request must agree with the metric definition in the service configuration, otherwise the MetricValue is rejected. `value` can be only one of the following:  
`boolValue` |  `boolean` A boolean value.  
`int64Value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` A signed 64-bit integer value.  
`doubleValue` |  `number` A double precision floating point value.  
`stringValue` |  `string` A text string value.  
`distributionValue` |  `object (`[Distribution](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Distribution)`)` A distribution value.  
`moneyValue` |  `object (`[Money](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Money)`)` A money value.  
  
## Distribution

Distribution represents a frequency distribution of double-valued sample points. It contains the size of the population of sample points plus additional optional information:

  * the arithmetic mean of the samples
  * the minimum and maximum of the samples
  * the sum-squared-deviation of the samples, used to compute variance
  * a histogram of the values of the sample points

JSON representation  
---  
      
    
    {
      "count": string,
      "mean": number,
      "minimum": number,
      "maximum": number,
      "sumOfSquaredDeviation": number,
      "bucketCounts": [
        string
      ],
      "exemplars": [
        {
          object ([Exemplar](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Exemplar))
        }
      ],
    
      // Union field bucket_option can be only one of the following:
      "linearBuckets": {
        object ([LinearBuckets](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#LinearBuckets))
      },
      "exponentialBuckets": {
        object ([ExponentialBuckets](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#ExponentialBuckets))
      },
      "explicitBuckets": {
        object ([ExplicitBuckets](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#ExplicitBuckets))
      }
      // End of list of possible types for union field bucket_option.
    }  
  
Fields  
---  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of samples in the distribution. Must be >= 0.  
`mean` |  `number` The arithmetic mean of the samples in the distribution. If `count` is zero then this field must be zero.  
`minimum` |  `number` The minimum of the population of values. Ignored if `count` is zero.  
`maximum` |  `number` The maximum of the population of values. Ignored if `count` is zero.  
`sumOfSquaredDeviation` |  `number` The sum of squared deviations from the mean: Sum[i=1..count]((x_i - mean)^2) where each x_i is a sample values. If `count` is zero then this field must be zero, otherwise validation of the request fails.  
`bucketCounts[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of samples in each histogram bucket. `bucketCounts` are optional. If present, they must sum to the `count` value.The buckets are defined below in `bucket_option`. There are N buckets. `bucketCounts[0]` is the number of samples in the underflow bucket. `bucketCounts[1]` to `bucketCounts[N-1]` are the numbers of samples in each of the finite buckets. And `bucketCounts[N]` is the number of samples in the overflow bucket. See the comments of `bucket_option` below for more details.Any suffix of trailing zeros may be omitted.  
`exemplars[]` |  `object (`[Exemplar](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Exemplar)`)` Example points. Must be in increasing order of `value` field.  
Union field `bucket_option`. Defines the buckets in the histogram. `bucket_option` and `bucket_counts` must be both set, or both unset.Buckets are numbered in the range of [0, N], with a total of N+1 buckets. There must be at least two buckets (a single-bucket histogram gives no information that isn't already provided by `count`).The first bucket is the underflow bucket which has a lower bound of -inf. The last bucket is the overflow bucket which has an upper bound of +inf. All other buckets (if any) are called "finite" buckets because they have finite lower and upper bounds. As described below, there are three ways to define the finite buckets.(1) Buckets with constant width. (2) Buckets with exponentially growing widths. (3) Buckets with arbitrary user-provided widths.In all cases, the buckets cover the entire real number line (-inf, +inf). Bucket upper bounds are exclusive and lower bounds are inclusive. The upper bound of the underflow bucket is equal to the lower bound of the smallest finite bucket; the lower bound of the overflow bucket is equal to the upper bound of the largest finite bucket. `bucket_option` can be only one of the following:  
`linearBuckets` |  `object (`[LinearBuckets](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#LinearBuckets)`)` Buckets with constant width.  
`exponentialBuckets` |  `object (`[ExponentialBuckets](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#ExponentialBuckets)`)` Buckets with exponentially growing width.  
`explicitBuckets` |  `object (`[ExplicitBuckets](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#ExplicitBuckets)`)` Buckets with arbitrary user-provided width.  
  
## LinearBuckets

Describing buckets with constant width.

JSON representation  
---  
      
    
    {
      "numFiniteBuckets": integer,
      "width": number,
      "offset": number
    }  
  
Fields  
---  
`numFiniteBuckets` |  `integer` The number of finite buckets. With the underflow and overflow buckets, the total number of buckets is `numFiniteBuckets` \+ 2. See comments on `bucketOptions` for details.  
`width` |  `number` The i'th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to numFiniteBuckets, inclusive. Must be strictly positive.  
`offset` |  `number` The i'th linear bucket covers the interval [offset + (i-1) * width, offset + i * width) where i ranges from 1 to numFiniteBuckets, inclusive.  
  
## ExponentialBuckets

Describing buckets with exponentially growing width.

JSON representation  
---  
      
    
    {
      "numFiniteBuckets": integer,
      "growthFactor": number,
      "scale": number
    }  
  
Fields  
---  
`numFiniteBuckets` |  `integer` The number of finite buckets. With the underflow and overflow buckets, the total number of buckets is `numFiniteBuckets` \+ 2. See comments on `bucketOptions` for details.  
`growthFactor` |  `number` The i'th exponential bucket covers the interval [scale * growthFactor^(i-1), scale * growthFactor^i) where i ranges from 1 to numFiniteBuckets inclusive. Must be larger than 1.0.  
`scale` |  `number` The i'th exponential bucket covers the interval [scale * growthFactor^(i-1), scale * growthFactor^i) where i ranges from 1 to numFiniteBuckets inclusive. Must be > 0.  
  
## ExplicitBuckets

Describing buckets with arbitrary user-provided width.

JSON representation  
---  
      
    
    {
      "bounds": [
        number
      ]
    }  
  
Fields  
---  
`bounds[]` |  `number` 'bound' is a list of strictly increasing boundaries between buckets. Note that a list of length N-1 defines N buckets because of fenceposting. See comments on `bucketOptions` for details.The i'th finite bucket covers the interval [bound[i-1], bound[i]) where i ranges from 1 to bound_size() - 1. Note that there are no finite buckets at all if 'bound' only contains a single element; in that special case the single bound defines the boundary between the underflow and overflow buckets.bucket number lower bound upper bound i == 0 (underflow) -inf bound[i] 0 < i < bound_size() bound[i-1] bound[i] i == bound_size() (overflow) bound[i-1] +inf  
  
## Exemplar

Exemplars are example points that may be used to annotate aggregated distribution values. They are metadata that gives information about a particular value added to a Distribution bucket, such as a trace ID that was active when a value was added. They may contain further information, such as a example values and timestamps, origin, etc.

JSON representation  
---  
      
    
    {
      "value": number,
      "timestamp": string,
      "attachments": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`value` |  `number` Value of the exemplar point. This value determines to which bucket the exemplar belongs.  
`timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The observation (sampling) time of the above value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attachments[]` |  `object` Contextual information about the example value. Examples are:Trace: type.googleapis.com/google.monitoring.v3.SpanContextLiteral string: type.googleapis.com/google.protobuf.StringValueLabels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabelsThere may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
## Money

Represents an amount of money with its currency type.

JSON representation  
---  
      
    
    {
      "currencyCode": string,
      "units": string,
      "nanos": integer
    }  
  
Fields  
---  
`currencyCode` |  `string` The three-letter currency code defined in ISO 4217.  
`units` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The whole units of the amount. For example if `currencyCode` is `"USD"`, then 1 unit is one US dollar.  
`nanos` |  `integer` Number of nano (10^-9) units of the amount. The value must be between -999,999,999 and +999,999,999 inclusive. If `units` is positive, `nanos` must be positive or zero. If `units` is zero, `nanos` can be positive, zero, or negative. If `units` is negative, `nanos` must be negative or zero. For example $-1.75 is represented as `units`=-1 and `nanos`=-750,000,000.  
  
## LogEntry

An individual log entry.

JSON representation  
---  
      
    
    {
      "name": string,
      "timestamp": string,
      "severity": enum ([LogSeverity](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/LogSeverity)),
      "httpRequest": {
        object ([HttpRequest](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#HttpRequest))
      },
      "trace": string,
      "insertId": string,
      "labels": {
        string: string,
        ...
      },
      "operation": {
        object ([LogEntryOperation](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#LogEntryOperation))
      },
      "sourceLocation": {
        object ([LogEntrySourceLocation](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#LogEntrySourceLocation))
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
`timestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the event described by the log entry occurred. If omitted, defaults to operation start time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`severity` |  `enum (`[LogSeverity](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/LogSeverity)`)` The severity of the log entry. The default value is `LogSeverity.DEFAULT`.  
`httpRequest` |  `object (`[HttpRequest](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#HttpRequest)`)` Optional. Information about the HTTP request associated with this log entry, if applicable.  
`trace` |  `string` Optional. Resource name of the trace associated with the log entry, if any. If this field contains a relative resource name, you can assume the name is relative to `//tracing.googleapis.com`. Example: `projects/my-projectid/traces/06796866738c859f2f19b7cfb3214824`  
`insertId` |  `string` A unique ID for the log entry used for deduplication. If omitted, the implementation will generate one based on operationId.  
`labels` |  `map (key: string, value: string)` A set of user-defined (key, value) data that provides additional information about the log entry.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`operation` |  `object (`[LogEntryOperation](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#LogEntryOperation)`)` Optional. Information about an operation associated with the log entry, if applicable.  
`sourceLocation` |  `object (`[LogEntrySourceLocation](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#LogEntrySourceLocation)`)` Optional. Source code location information associated with the log entry, if any.  
Union field `payload`. The log entry payload, which can be one of multiple types. `payload` can be only one of the following:  
`protoPayload` |  `object` The log entry payload, represented as a protocol buffer that is expressed as a JSON object. The only accepted type currently is `AuditLog`.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`textPayload` |  `string` The log entry payload, represented as a Unicode string (UTF-8).  
`structPayload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` The log entry payload, represented as a structure that is expressed as a JSON object.  
  
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
`referer` |  `string` The referer URL of the request, as defined in [HTTP/1.1 Header Field Definitions](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).  
`latency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The request processing latency on the server, from the time the request was received until the response was sent.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
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
  
## QuotaProperties

Represents the properties needed for quota operations.

JSON representation  
---  
      
    
    {
      "quotaMode": enum ([QuotaMode](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/QuotaMode))
    }  
  
Fields  
---  
`quotaMode` |  `enum (`[QuotaMode](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/QuotaMode)`)` Quota mode for this operation.  
  
## ResourceInfo

Describes a resource associated with this operation.

JSON representation  
---  
      
    
    {
      "resourceContainer": string,
      "resourceName": string,
      "resourceLocation": string,
      "permission": string
    }  
  
Fields  
---  
`resourceContainer` |  `string` The identifier of the parent of this resource instance. Must be in one of the following formats: - `projects/<project-id or project-number>` \- `folders/<folder-id>` \- `organizations/<organization-id>`  
`resourceName` |  `string` Name of the resource. This is used for auditing purposes.  
`resourceLocation` |  `string` The location of the resource. If not empty, the resource will be checked against location policy. The value must be a valid zone, region or multiregion. For example: "europe-west4" or "northamerica-northeast1-a"  
`permission` |  `string` The resource permission required for this request.  
  
## TraceSpan

A span represents a single operation within a trace. Spans can be nested to form a trace tree. Often, a trace contains a root span that describes the end-to-end latency, and one or more subspans for its sub-operations. A trace can also contain multiple root spans, or none at all. Spans do not need to be contiguous—there may be gaps or overlaps between spans in a trace.

JSON representation  
---  
      
    
    {
      "name": string,
      "spanId": string,
      "parentSpanId": string,
      "displayName": {
        object ([TruncatableString](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#TruncatableString))
      },
      "startTime": string,
      "endTime": string,
      "attributes": {
        object ([Attributes](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Attributes))
      },
      "status": {
        object ([Status](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.operations#Status))
      },
      "sameProcessAsParentSpan": boolean,
      "childSpanCount": integer,
      "spanKind": enum ([SpanKind](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/SpanKind))
    }  
  
Fields  
---  
`name` |  `string` The resource name of the span in the following format:
    
    
    projects/[PROJECT_ID]/traces/[TRACE_ID]/spans/[SPAN_ID]
    

[TRACE_ID] is a unique identifier for a trace within a project; it is a 32-character hexadecimal encoding of a 16-byte array.[SPAN_ID] is a unique identifier for a span within a trace; it is a 16-character hexadecimal encoding of an 8-byte array.  
`spanId` |  `string` The [SPAN_ID] portion of the span's resource name.  
`parentSpanId` |  `string` The [SPAN_ID] of this span's parent span. If this is a root span, then this field must be empty.  
`displayName` |  `object (`[TruncatableString](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#TruncatableString)`)` A description of the span's operation (up to 128 bytes). Stackdriver Trace displays the description in the Google Cloud Platform Console. For example, the display name can be a qualified method name or a file name and a line number where the operation is called. A best practice is to use the same display name within an application and at the same call point. This makes it easier to correlate spans in different traces.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The start time of the span. On the client side, this is the time kept by the local machine where the span execution starts. On the server side, this is the time when the server's application handler starts running.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The end time of the span. On the client side, this is the time kept by the local machine where the span execution ends. On the server side, this is the time when the server application handler stops running.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`attributes` |  `object (`[Attributes](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#Attributes)`)` A set of attributes on the span. You can have up to 32 attributes per span.  
`status` |  `object (`[Status](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/projects.locations.operations#Status)`)` An optional final status for this span.  
`sameProcessAsParentSpan` |  `boolean` (Optional) Set this parameter to indicate whether this span is in the same process as its parent. If you do not set this parameter, Stackdriver Trace is unable to take advantage of this helpful information.  
`childSpanCount` |  `integer` An optional number of child spans that were generated while this span was active. If set, allows implementation to detect missing child spans.  
`spanKind` |  `enum (`[SpanKind](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/SpanKind)`)` Distinguishes between spans generated in a particular context. For example, two spans with the same name may be distinguished using `CLIENT` (caller) and `SERVER` (callee) to identify an RPC call.  
  
## TruncatableString

Represents a string that might be shortened to a specified length.

JSON representation  
---  
      
    
    {
      "value": string,
      "truncatedByteCount": integer
    }  
  
Fields  
---  
`value` |  `string` The shortened string. For example, if the original string is 500 bytes long and the limit of the string is 128 bytes, then `value` contains the first 128 bytes of the 500-byte string.Truncation always happens on a UTF8 character boundary. If there are multi-byte characters in the string, then the length of the shortened string might be less than the size limit.  
`truncatedByteCount` |  `integer` The number of bytes removed from the original string. If this value is 0, then the string was not shortened.  
  
## Attributes

A set of attributes, each in the format `[KEY]:[VALUE]`.

JSON representation  
---  
      
    
    {
      "attributeMap": {
        string: {
          object ([AttributeValue](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#AttributeValue))
        },
        ...
      },
      "droppedAttributesCount": integer
    }  
  
Fields  
---  
`attributeMap` |  `map (key: string, value: object (`[AttributeValue](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#AttributeValue)`))` The set of attributes. Each attribute's key can be up to 128 bytes long. The value can be a string up to 256 bytes, a signed 64-bit integer, or the Boolean values `true` and `false`. For example:
    
    
    "/instance_id": "my-instance"
    "/http/userAgent": ""
    "/http/request_bytes": 300
    "example.com/myattribute": true
    

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`droppedAttributesCount` |  `integer` The number of attributes that were discarded. Attributes can be discarded because their keys are too long or because there are too many attributes. If this value is 0 then all attributes are valid.  
  
## AttributeValue

The allowed types for [VALUE] in a `[KEY]:[VALUE]` attribute.

JSON representation  
---  
      
    
    {
    
      // Union field value can be only one of the following:
      "stringValue": {
        object ([TruncatableString](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#TruncatableString))
      },
      "intValue": string,
      "boolValue": boolean
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
Union field `value`. The type of the value. `value` can be only one of the following:  
`stringValue` |  `object (`[TruncatableString](https://docs.cloud.google.com/vmware-engine/docs/public/reference/rest/v1/BillingView#TruncatableString)`)` A string up to 256 bytes long.  
`intValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` A 64-bit signed integer.  
`boolValue` |  `boolean` A Boolean value represented by `true` or `false`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-11 UTC."],[],[]] 
