---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api
title: Package google.api \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:21.224918+00:00
---

# Package google.api  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Package google.api Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Distribution](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution)` (message)
  * `[Distribution.BucketOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.BucketOptions)` (message)
  * `[Distribution.BucketOptions.Explicit](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.BucketOptions.Explicit)` (message)
  * `[Distribution.BucketOptions.Exponential](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.BucketOptions.Exponential)` (message)
  * `[Distribution.BucketOptions.Linear](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.BucketOptions.Linear)` (message)
  * `[Distribution.Exemplar](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.Exemplar)` (message)
  * `[Distribution.Range](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.Range)` (message)
  * `[HttpBody](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.HttpBody)` (message)
  * `[LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LabelDescriptor)` (message)
  * `[LabelDescriptor.ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LabelDescriptor.ValueType)` (enum)
  * `[LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LaunchStage)` (enum)
  * `[Metric](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Metric)` (message)
  * `[MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor)` (message)
  * `[MetricDescriptor.MetricDescriptorMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricDescriptorMetadata)` (message)
  * `[MetricDescriptor.MetricDescriptorMetadata.TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricDescriptorMetadata.TimeSeriesResourceHierarchyLevel)` (enum)
  * `[MetricDescriptor.MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind)` (enum)
  * `[MetricDescriptor.ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.ValueType)` (enum)
  * `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResource)` (message)
  * `[MonitoredResourceDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResourceDescriptor)` (message)
  * `[MonitoredResourceMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResourceMetadata)` (message)



## Distribution

`Distribution` contains summary statistics for a population of values. It optionally contains a histogram representing the distribution of those values across a set of buckets.

The summary statistics are the count, mean, sum of the squared deviation from the mean, the minimum, and the maximum of the set of population of values. The histogram is based on a sequence of buckets and gives a count of values that fall into each bucket. The boundaries of the buckets are given either explicitly or by formulas for buckets of fixed or exponentially increasing widths.

Although it is not forbidden, it is generally a bad idea to include non-finite values (infinities or NaNs) in the population of values, as this will render the `mean` and `sum_of_squared_deviation` fields meaningless.

Fields  
---  
`count` |  `int64` The number of values in the population. Must be non-negative. This value must equal the sum of the values in `bucket_counts` if a histogram is provided.  
`mean` |  `double` The arithmetic mean of the values in the population. If `count` is zero then this field must be zero.  
`sum_of_squared_deviation` |  `double` The sum of squared deviations from the mean of the values in the population. For values x_i this is:
    
    
    Sum[i=1..n]((x_i - mean)^2)
    

Knuth, "The Art of Computer Programming", Vol. 2, page 232, 3rd edition describes Welford's method for accumulating this sum in one pass.If `count` is zero then this field must be zero.  
`range` |  `[Range](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.Range)` If specified, contains the range of the population values. The field must not be present if the count is zero. This field is presently ignored by the Cloud Monitoring API v3.  
`bucket_options` |  `[BucketOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.BucketOptions)` Required in the Cloud Monitoring API v3. Defines the histogram bucket boundaries.  
`bucket_counts[]` |  `int64` Required in the Cloud Monitoring API v3. The values for each bucket specified in `bucket_options`. The sum of the values in `bucketCounts` must equal the value in the count field of the `Distribution` object. The order of the bucket counts follows the numbering schemes described for the three bucket types. The underflow bucket has number 0; the finite buckets, if any, have numbers 1 through N-2; and the overflow bucket has number N-1. The size of `bucket_counts` must not be greater than N. If the size is less than N, then the remaining buckets are assigned values of zero.  
`exemplars[]` |  `[Exemplar](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.Exemplar)` Must be in increasing order of `value` field.  
  
## BucketOptions

`BucketOptions` describes the bucket boundaries used to create a histogram for the distribution. The buckets can be in a linear sequence, an exponential sequence, or each bucket can be specified explicitly. `BucketOptions` does not include the number of values in each bucket.

A bucket has an inclusive lower bound and exclusive upper bound for the values that are counted for that bucket. The upper bound of a bucket must be strictly greater than the lower bound. The sequence of N buckets for a distribution consists of an underflow bucket (number 0), zero or more finite buckets (number 1 through N - 2) and an overflow bucket (number N - 1). The buckets are contiguous: the lower bound of bucket i (i > 0) is the same as the upper bound of bucket i - 1. The buckets span the whole range of finite values: lower bound of the underflow bucket is -infinity and the upper bound of the overflow bucket is +infinity. The finite buckets are so-called because both bounds are finite.

Fields  
---  
Union field `options`. Exactly one of these three fields must be set. `options` can be only one of the following:  
`linear_buckets` |  `[Linear](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.BucketOptions.Linear)` The linear bucket.  
`exponential_buckets` |  `[Exponential](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.BucketOptions.Exponential)` The exponential buckets.  
`explicit_buckets` |  `[Explicit](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution.BucketOptions.Explicit)` The explicit buckets.  
  
## Explicit

Specifies a set of buckets with arbitrary widths.

There are `size(bounds) + 1` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): bounds[i] Lower bound (1 <= i < N); bounds[i - 1]

The `bounds` field must contain at least one element. If `bounds` has only one element, then there are no finite buckets, and that single element is the common boundary of the overflow and underflow buckets.

Fields  
---  
`bounds[]` |  `double` The values must be monotonically increasing.  
  
## Exponential

Specifies an exponential sequence of buckets that have a width that is proportional to the value of the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket.

There are `num_finite_buckets + 2` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): scale * (growth_factor ^ i).

Lower bound (1 <= i < N): scale * (growth_factor ^ (i - 1)).

Fields  
---  
`num_finite_buckets` |  `int32` Must be greater than 0.  
`growth_factor` |  `double` Must be greater than 1.  
`scale` |  `double` Must be greater than 0.  
  
## Linear

Specifies a linear sequence of buckets that all have the same width (except overflow and underflow). Each bucket represents a constant absolute uncertainty on the specific value in the bucket.

There are `num_finite_buckets + 2` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): offset + (width * i).

Lower bound (1 <= i < N): offset + (width * (i - 1)).

Fields  
---  
`num_finite_buckets` |  `int32` Must be greater than 0.  
`width` |  `double` Must be greater than 0.  
`offset` |  `double` Lower bound of the first bucket.  
  
## Exemplar

Exemplars are example points that may be used to annotate aggregated distribution values. They are metadata that gives information about a particular value added to a Distribution bucket, such as a trace ID that was active when a value was added. They may contain further information, such as a example values and timestamps, origin, etc.

Fields  
---  
`value` |  `double` Value of the exemplar point. This value determines to which bucket the exemplar belongs.  
`timestamp` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The observation (sampling) time of the above value.  
`attachments[]` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` Contextual information about the example value. Examples are:Trace: type.googleapis.com/google.monitoring.v3.SpanContextLiteral string: type.googleapis.com/google.protobuf.StringValueLabels dropped during aggregation: type.googleapis.com/google.monitoring.v3.DroppedLabelsThere may be only a single attachment of any given message type in a single exemplar, and this is enforced by the system.  
  
## Range

The range of the population values.

Fields  
---  
`min` |  `double` The minimum of the population values.  
`max` |  `double` The maximum of the population values.  
  
## HttpBody

Message that represents an arbitrary HTTP body. It should only be used for payload formats that can't be represented as JSON, such as raw binary or an HTML page.

This message can be used both in streaming and non-streaming API methods in the request as well as the response.

It can be used as a top-level request field, which is convenient if one wants to extract parameters from either the URL or HTTP template into the request fields and also want access to the raw HTTP body.

Example:
    
    
    message GetResourceRequest {
      // A unique request id.
      string request_id = 1;
    
      // The raw HTTP body is bound to this field.
      google.api.HttpBody http_body = 2;
    
    }
    
    service ResourceService {
      rpc GetResource(GetResourceRequest)
        returns (google.api.HttpBody);
      rpc UpdateResource(google.api.HttpBody)
        returns (google.protobuf.Empty);
    
    }
    

Example with streaming methods:
    
    
    service CaldavService {
      rpc GetCalendar(stream google.api.HttpBody)
        returns (stream google.api.HttpBody);
      rpc UpdateCalendar(stream google.api.HttpBody)
        returns (stream google.api.HttpBody);
    
    }
    

Use of this type only changes how the request and response bodies are handled, all other features will continue to work unchanged.

Fields  
---  
`content_type` |  `string` The HTTP Content-Type header value specifying the content type of the body.  
`data` |  `bytes` The HTTP request/response body as raw binary.  
`extensions[]` |  `[Any](https://protobuf.dev/reference/protobuf/google.protobuf/#any)` Application specific response metadata. Must be set in the first response for streaming APIs.  
  
## LabelDescriptor

A description of a label.

Fields  
---  
`key` |  `string` The key for this label. The key must meet the following criteria:

  * Does not exceed 100 characters.
  * Matches the following regular expression: `[a-zA-Z][a-zA-Z0-9_]*`
    * The first character must be an upper- or lower-case letter.
    * The remaining characters must be letters, digits, or underscores.

  
`value_type` |  `[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LabelDescriptor.ValueType)` The type of data that can be assigned to the label.  
`description` |  `string` A human-readable description for the label.  
  
## ValueType

Value types that can be used as label values.

Enums  
---  
`STRING` | A variable-length string, not to exceed 1,024 characters. This is the default value type.  
`BOOL` | Boolean; true or false.  
`INT64` | A 64-bit signed integer.  
  
## LaunchStage

The launch stage as defined by [Google Cloud Platform Launch Stages](https://cloud.google.com/terms/launch-stages).

Enums  
---  
`LAUNCH_STAGE_UNSPECIFIED` | Do not use this default value.  
`UNIMPLEMENTED` | The feature is not yet implemented. Users can not use it.  
`PRELAUNCH` | Prelaunch features are hidden from users and are only visible internally.  
`EARLY_ACCESS` | Early Access features are limited to a closed group of testers. To use these features, you must sign up in advance and sign a Trusted Tester agreement (which includes confidentiality provisions). These features may be unstable, changed in backward-incompatible ways, and are not guaranteed to be released.  
`ALPHA` | Alpha is a limited availability test for releases before they are cleared for widespread use. By Alpha, all significant design issues are resolved and we are in the process of verifying functionality. Alpha customers need to apply for access, agree to applicable terms, and have their projects allowlisted. Alpha releases don't have to be feature complete, no SLAs are provided, and there are no technical support obligations, but they will be far enough along that customers can actually use them in test environments or for limited-use tests -- just like they would in normal production cases.  
`BETA` | Beta is the point at which we are ready to open a release for any customer to use. There are no SLA or technical support obligations in a Beta release. Products will be complete from a feature perspective, but may have some open outstanding issues. Beta releases are suitable for limited production use cases.  
`GA` | GA features are open to all developers and are considered stable and fully qualified for production use.  
`DEPRECATED` | Deprecated features are scheduled to be shut down and removed. For more information, see the "Deprecation Policy" section of our [Terms of Service](https://cloud.google.com/terms/) and the [Google Cloud Platform Subject to the Deprecation Policy](https://cloud.google.com/terms/deprecation) documentation.  
  
## Metric

A specific metric, identified by specifying values for all of the labels of a `[`MetricDescriptor`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor)`.

Fields  
---  
`type` |  `string` An existing metric type, see `[google.api.MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor)`. For example, `custom.googleapis.com/invoice/paid/amount`.  
`labels` |  `map<string, string>` The set of label values that uniquely identify this metric. All labels listed in the `MetricDescriptor` must be assigned values.  
  
## MetricDescriptor

Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.

Fields  
---  
`name` |  `string` The resource name of the metric descriptor.  
`type` |  `string` The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:
    
    
    "custom.googleapis.com/invoice/paid/amount"
    "external.googleapis.com/prometheus/up"
    "appengine.googleapis.com/http/server/response_latencies"
      
  
`labels[]` |  `[LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LabelDescriptor)` The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.  
`metric_kind` |  `[MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind)` Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metric_kind` and `value_type` might not be supported.  
`value_type` |  `[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.ValueType)` Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metric_kind` and `value_type` might not be supported.  
`unit` |  `string` The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:**Basic units (UNIT)**

  * `bit` bit
  * `By` byte
  * `s` second
  * `min` minute
  * `h` hour
  * `d` day
  * `1` dimensionless

**Prefixes (PREFIX)**

  * `k` kilo (10^3)
  * `M` mega (10^6)
  * `G` giga (10^9)
  * `T` tera (10^12)
  * `P` peta (10^15)
  * `E` exa (10^18)
  * `Z` zetta (10^21)
  * `Y` yotta (10^24)
  * `m` milli (10^-3)
  * `u` micro (10^-6)
  * `n` nano (10^-9)
  * `p` pico (10^-12)
  * `f` femto (10^-15)
  * `a` atto (10^-18)
  * `z` zepto (10^-21)
  * `y` yocto (10^-24)
  * `Ki` kibi (2^10)
  * `Mi` mebi (2^20)
  * `Gi` gibi (2^30)
  * `Ti` tebi (2^40)
  * `Pi` pebi (2^50)

**Grammar** The grammar also includes these connectors:

  * `/` division or ratio (as an infix operator). For examples, `kBy/{email}` or `MiBy/10ms` (although you should almost never have `/s` in a metric `unit`; rates should always be computed at query time from the underlying cumulative or delta value).
  * `.` multiplication or composition (as an infix operator). For examples, `GBy.d` or `k{watt}.h`.

The grammar for a unit is as follows:
    
    
    Expression = Component { "." Component } { "/" Component } ;
    
    Component = ( [ PREFIX ] UNIT | "%" ) [ Annotation ]
              | Annotation
              | "1"
              ;
    
    Annotation = "{" NAME "}" ;
    

Notes:

  * `Annotation` is just a comment if it follows a `UNIT`. If the annotation is used alone, then the unit is equivalent to `1`. For examples, `{request}/s == 1/s`, `By{transmitted}/s == By/s`.
  * `NAME` is a sequence of non-blank printable ASCII characters not containing `{` or `}`.
  * `1` represents a unitary [dimensionless unit](https://en.wikipedia.org/wiki/Dimensionless_quantity) of 1, such as in `1/s`. It is typically used when none of the basic units are appropriate. For example, "new users per day" can be represented as `1/d` or `{new-users}/d` (and a metric value `5` would mean "5 new users). Alternatively, "thousands of page views per day" would be represented as `1000/d` or `k1/d` or `k{page_views}/d` (and a metric value of `5.3` would mean "5300 page views per day").
  * `%` represents dimensionless value of 1/100, and annotates values giving a percentage (so the metric values are typically in the range of 0..100, and a metric value `3` means "3 percent").
  * `10^2.%` indicates a metric contains a ratio, typically in the range 0..1, that will be multiplied by 100 and displayed as a percentage (so a metric value `0.03` means "3 percent").

  
`description` |  `string` A detailed description of the metric, which can be used in documentation.  
`display_name` |  `string` A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.  
`metadata` |  `[MetricDescriptorMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricDescriptorMetadata)` Optional. Metadata which can be used to guide usage of the metric.  
`launch_stage` |  `[LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LaunchStage)` Optional. The launch stage of the metric definition.  
`monitored_resource_types[]` |  `string` Read-only. If present, then a `[time series](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeries)`, which is identified partially by a metric type and a `[MonitoredResourceDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResourceDescriptor)`, that is associated with this metric type can only be associated with one of the monitored resource types listed here.  
  
## MetricDescriptorMetadata

Additional annotations that can be used to guide the usage of a metric.

Fields  
---  
`launch_stage  
**(deprecated)**` |  `[LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LaunchStage)` This item is deprecated!Deprecated. Must use the `[MetricDescriptor.launch_stage](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.FIELDS.google.api.LaunchStage.google.api.MetricDescriptor.launch_stage)` instead.  
`sample_period` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.  
`ingest_delay` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.  
`time_series_resource_hierarchy_level[]` |  `[TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricDescriptorMetadata.TimeSeriesResourceHierarchyLevel)` The scope of the timeseries data of the metric.  
  
## TimeSeriesResourceHierarchyLevel

The resource hierarchy level of the timeseries data of a metric.

Enums  
---  
`TIME_SERIES_RESOURCE_HIERARCHY_LEVEL_UNSPECIFIED` | Do not use this default value.  
`PROJECT` | Scopes a metric to a project.  
`ORGANIZATION` | Scopes a metric to an organization.  
`FOLDER` | Scopes a metric to a folder.  
  
## MetricKind

The kind of measurement. It describes how the data is reported. For information on setting the start time and end time based on the MetricKind, see `[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeInterval)`.

Enums  
---  
`METRIC_KIND_UNSPECIFIED` | Do not use this default value.  
`GAUGE` | An instantaneous measurement of a value.  
`DELTA` | The change in a value during a time interval.  
`CUMULATIVE` | A value accumulated over a time interval. Cumulative measurements in a time series should have the same start time and increasing end times, until an event resets the cumulative value to zero and sets a new start time for the following points.  
  
## ValueType

The value type of a metric.

Enums  
---  
`VALUE_TYPE_UNSPECIFIED` | Do not use this default value.  
`BOOL` | The value is a boolean. This value type can be used only if the metric kind is `GAUGE`.  
`INT64` | The value is a signed 64-bit integer.  
`DOUBLE` | The value is a double precision floating point number.  
`STRING` | The value is a text string. This value type can be used only if the metric kind is `GAUGE`.  
`DISTRIBUTION` | The value is a `[`Distribution`](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.Distribution)`.  
  
## MonitoredResource

An object representing a resource that can be used for monitoring, logging, billing, or other purposes. Examples include virtual machine instances, databases, and storage devices such as disks. The `type` field identifies a `[MonitoredResourceDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResourceDescriptor)` object that describes the resource's schema. Information in the `labels` field identifies the actual resource and its attributes according to the schema. For example, a particular Compute Engine VM instance could be represented by the following object, because the `[MonitoredResourceDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResourceDescriptor)` for `"gce_instance"` has labels `"project_id"`, `"instance_id"` and `"zone"`:
    
    
    { "type": "gce_instance",
      "labels": { "project_id": "my-project",
                  "instance_id": "12345678901234",
                  "zone": "us-central1-a" }}
    

Fields  
---  
`type` |  `string` Required. The monitored resource type. This field must match the `type` field of a `[MonitoredResourceDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResourceDescriptor)` object. For example, the type of a Compute Engine VM instance is `gce_instance`. For a list of types, see [Monitoring resource types](https://cloud.google.com/monitoring/api/resources) and [Logging resource types](https://cloud.google.com/logging/docs/api/v2/resource-list).  
`labels` |  `map<string, string>` Required. Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels `"project_id"`, `"instance_id"`, and `"zone"`.  
  
## MonitoredResourceDescriptor

An object that describes the schema of a `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResource)` object using a type name and a set of labels. For example, the monitored resource descriptor for Google Compute Engine VM instances has a type of `"gce_instance"` and specifies the use of the labels `"instance_id"` and `"zone"` to identify particular VM instances.

Different APIs can support different monitored resource types. APIs generally provide a `list` method that returns the monitored resource descriptors used by the API.

Fields  
---  
`name` |  `string` Optional. The resource name of the monitored resource descriptor: `"projects/{project_id}/monitoredResourceDescriptors/{type}"` where {type} is the value of the `type` field in this object and {project_id} is a project ID that provides API-specific context for accessing the type. APIs that do not use project information can use the resource name format `"monitoredResourceDescriptors/{type}"`.  
`type` |  `string` Required. The monitored resource type. For example, the type `"cloudsql_database"` represents databases in Google Cloud SQL. For a list of types, see [Monitored resource types](https://cloud.google.com/monitoring/api/resources) and [Logging resource types](https://cloud.google.com/logging/docs/api/v2/resource-list).  
`display_name` |  `string` Optional. A concise name for the monitored resource type that might be displayed in user interfaces. It should be a Title Cased Noun Phrase, without any article or other determiners. For example, `"Google Cloud SQL Database"`.  
`description` |  `string` Optional. A detailed description of the monitored resource type that might be used in documentation.  
`labels[]` |  `[LabelDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LabelDescriptor)` Required. A set of labels used to describe instances of this monitored resource type. For example, an individual Google Cloud SQL database is identified by values for the labels `"database_id"` and `"zone"`.  
`launch_stage` |  `[LaunchStage](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.LaunchStage)` Optional. The launch stage of the monitored resource definition.  
  
## MonitoredResourceMetadata

Auxiliary metadata for a `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResource)` object. `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResource)` objects contain the minimum set of information to uniquely identify a monitored resource instance. There is some other useful auxiliary metadata. Monitoring and Logging use an ingestion pipeline to extract metadata for cloud resources of all types, and store the metadata in this message.

Fields  
---  
`system_labels` |  `[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` Output only. Values for predefined system metadata labels. System labels are a kind of metadata extracted by Google, including "machine_image", "vpc", "subnet_id", "security_group", "name", etc. System label values can be only strings, Boolean values, or a list of strings. For example:
    
    
    { "name": "my-test-instance",
      "security_group": ["a", "b", "c"],
      "spot_instance": false }
      
  
`user_labels` |  `map<string, string>` Output only. A map of user-defined metadata labels.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
