---
url: https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics
title: REST Resource: projects.metrics \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:35.621555+00:00
---

# REST Resource: projects.metrics  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Reference ](https://docs.cloud.google.com/logging/docs/apis)



Send feedback 

#  REST Resource: projects.metrics Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: LogMetric
    * JSON representation
  * MetricDescriptor
    * JSON representation
  * LabelDescriptor
    * JSON representation
  * ValueType
  * MetricKind
  * ValueType
  * MetricDescriptorMetadata
    * JSON representation
  * LaunchStage
  * TimeSeriesResourceHierarchyLevel
  * BucketOptions
    * JSON representation
  * Linear
    * JSON representation
  * Exponential
    * JSON representation
  * Explicit
    * JSON representation
  * ApiVersion
  * Methods



## Resource: LogMetric

Describes a logs-based metric. The value of the metric is the number of log entries that match a logs filter in a given time interval.

Logs-based metrics can also be used to extract values from logs and create a distribution of the values. The distribution records the statistics of the extracted values along with an optional histogram of the values as specified by the bucket options.

JSON representation  
---  
      
    
    {
      "name": string,
      "resourceName": string,
      "description": string,
      "filter": string,
      "bucketName": string,
      "disabled": boolean,
      "metricDescriptor": {
        object ([MetricDescriptor](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#MetricDescriptor))
      },
      "valueExtractor": string,
      "labelExtractors": {
        string: string,
        ...
      },
      "bucketOptions": {
        object ([BucketOptions](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#BucketOptions))
      },
      "createTime": string,
      "updateTime": string,
      "version": enum ([ApiVersion](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#ApiVersion))
    }  
  
Fields  
---  
`name` |  `string` Required. The client-assigned metric identifier. Examples: `"error_count"`, `"nginx/requests"`.Metric identifiers are limited to 100 characters and can include only the following characters: `A-Z`, `a-z`, `0-9`, and the special characters `_-.,+!*',()%/`. The forward-slash character (`/`) denotes a hierarchy of name pieces, and it cannot be the first character of the name.This field is the `[METRIC_ID]` part of a metric resource name in the format "projects/[PROJECT_ID]/metrics/[METRIC_ID]". Example: If the resource name of a metric is `"projects/my-project/metrics/nginx%2Frequests"`, this field's value is `"nginx/requests"`.  
`resourceName` |  `string` Output only. The resource name of the metric:
    
    
    "projects/[PROJECT_ID]/metrics/[METRIC_ID]"
      
  
`description` |  `string` Optional. A description of this metric, which is used in documentation. The maximum length of the description is 8000 characters.  
`filter` |  `string` Required. An [advanced logs filter](https://cloud.google.com/logging/docs/view/advanced_filters) which is used to match log entries. Example:
    
    
    "resource.type=gae_app AND severity>=ERROR"
    

The maximum length of the filter is 20000 characters.  
`bucketName` |  `string` Optional. The resource name of the Log Bucket that owns the Log Metric. Only Log Buckets in projects are supported. The bucket has to be in the same project as the metric.For example:`projects/my-project/locations/global/buckets/my-bucket`If empty, then the Log Metric is considered a non-Bucket Log Metric.  
`disabled` |  `boolean` Optional. If set to True, then this metric is disabled and it does not generate any points.  
`metricDescriptor` |  `object (`[MetricDescriptor](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#MetricDescriptor)`)` Optional. The metric descriptor associated with the logs-based metric. If unspecified, it uses a default metric descriptor with a DELTA metric kind, INT64 value type, with no labels and a unit of "1". Such a metric counts the number of log entries matching the `filter` expression.The `name`, `type`, and `description` fields in the `metricDescriptor` are output only, and is constructed using the `name` and `description` field in the LogMetric.To create a logs-based metric that records a distribution of log values, a DELTA metric kind with a DISTRIBUTION value type must be used along with a `valueExtractor` expression in the LogMetric.Each label in the metric descriptor must have a matching label name as the key and an extractor expression as the value in the `labelExtractors` map.The `metricKind` and `valueType` fields in the `metricDescriptor` cannot be updated once initially configured. New labels can be added in the `metricDescriptor`, but existing labels cannot be modified except for their description.  
`valueExtractor` |  `string` Optional. A `valueExtractor` is required when using a distribution logs-based metric to extract the values to record from a log entry. Two functions are supported for value extraction: `EXTRACT(field)` or `REGEXP_EXTRACT(field, regex)`. The arguments are:

  1. field: The name of the log entry field from which the value is to be extracted.
  2. regex: A regular expression using the Google RE2 syntax (<https://github.com/google/re2/wiki/Syntax>) with a single capture group to extract data from the specified log entry field. The value of the field is converted to a string before applying the regex. It is an error to specify a regex that does not include exactly one capture group.

The result of the extraction must be convertible to a double type, as the distribution always records double values. If either the extraction or the conversion to double fails, then those values are not recorded in the distribution.Example: `REGEXP_EXTRACT(jsonPayload.request, ".*quantity=(\d+).*")`  
`labelExtractors` |  `map (key: string, value: string)` Optional. A map from a label key string to an extractor expression which is used to extract data from a log entry field and assign as the label value. Each label key specified in the LabelDescriptor must have an associated extractor expression in this map. The syntax of the extractor expression is the same as for the `valueExtractor` field.The extracted value is converted to the type defined in the label descriptor. If either the extraction or the type conversion fails, the label will have a default value. The default value for a string label is an empty string, for an integer label its 0, and for a boolean label its `false`.Note that there are upper bounds on the maximum number of labels and the number of active time series that are allowed in a project.  
`bucketOptions` |  `object (`[BucketOptions](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#BucketOptions)`)` Optional. The `bucketOptions` are required when the logs-based metric is using a DISTRIBUTION value type and it describes the bucket boundaries used to create a histogram of the extracted values.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation timestamp of the metric.This field may not be present for older metrics.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update timestamp of the metric.This field may not be present for older metrics.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`version  
**(deprecated)**` |  `enum (`[ApiVersion](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#ApiVersion)`)` This item is deprecated!Deprecated. The API version that created or updated this metric. The v2 format is used by default and cannot be changed.  
  
## MetricDescriptor

Defines a metric type and its schema. Once a metric descriptor is created, deleting or altering it stops data collection and makes the metric type's existing data unusable.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "labels": [
        {
          object ([LabelDescriptor](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LabelDescriptor))
        }
      ],
      "metricKind": enum ([MetricKind](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#MetricKind)),
      "valueType": enum ([ValueType](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#ValueType_1)),
      "unit": string,
      "description": string,
      "displayName": string,
      "metadata": {
        object ([MetricDescriptorMetadata](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#MetricDescriptorMetadata))
      },
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LaunchStage)),
      "monitoredResourceTypes": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` The resource name of the metric descriptor.  
`type` |  `string` The metric type, including its DNS name prefix. The type is not URL-encoded. All user-defined metric types have the DNS name `custom.googleapis.com` or `external.googleapis.com`. Metric types should use a natural hierarchical grouping. For example:
    
    
    "custom.googleapis.com/invoice/paid/amount"
    "external.googleapis.com/prometheus/up"
    "appengine.googleapis.com/http/server/response_latencies"
      
  
`labels[]` |  `object (`[LabelDescriptor](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LabelDescriptor)`)` The set of labels that can be used to describe a specific instance of this metric type. For example, the `appengine.googleapis.com/http/server/response_latencies` metric type has a label for the HTTP response code, `response_code`, so you can look at latencies for successful responses or just for responses that failed.  
`metricKind` |  `enum (`[MetricKind](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#MetricKind)`)` Whether the metric records instantaneous values, changes to a value, etc. Some combinations of `metricKind` and `valueType` might not be supported.  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#ValueType_1)`)` Whether the measurement is an integer, a floating-point number, etc. Some combinations of `metricKind` and `valueType` might not be supported.  
`unit` |  `string` The units in which the metric value is reported. It is only applicable if the `valueType` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values.Different systems might scale the values to be more easily displayed (so a value of `0.02kBy` _might_ be displayed as `20By`, and a value of `3523kBy` _might_ be displayed as `3.5MBy`). However, if the `unit` is `kBy`, then the value of the metric is always in thousands of bytes, no matter how it might be displayed.If you want a custom metric to record the exact number of CPU-seconds used by a job, you can create an `INT64 CUMULATIVE` metric whose `unit` is `s{CPU}` (or equivalently `1s{CPU}` or just `s`). If the job uses 12,005 CPU-seconds, then the value is written as `12005`.Alternatively, if you want a custom metric to record data in a more granular way, you can create a `DOUBLE CUMULATIVE` metric whose `unit` is `ks{CPU}`, and then write the value `12.005` (which is `12005/1000`), or use `Kis{CPU}` and write `11.723` (which is `12005/1024`).The supported units are a subset of [The Unified Code for Units of Measure](https://unitsofmeasure.org/ucum.html) standard:**Basic units (UNIT)**

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
`displayName` |  `string` A concise name for the metric, which can be displayed in user interfaces. Use sentence case without an ending period, for example "Request count". This field is optional but it is recommended to be set for any metrics associated with user-visible concepts, such as Quota.  
`metadata` |  `object (`[MetricDescriptorMetadata](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#MetricDescriptorMetadata)`)` Optional. Metadata which can be used to guide usage of the metric.  
`launchStage` |  `enum (`[LaunchStage](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LaunchStage)`)` Optional. The launch stage of the metric definition.  
`monitoredResourceTypes[]` |  `string` Read-only. If present, then a [time series](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries), which is identified partially by a metric type and a `[MonitoredResourceDescriptor](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/monitoredResourceDescriptors/list#MonitoredResourceDescriptor)`, that is associated with this metric type can only be associated with one of the monitored resource types listed here.  
  
## LabelDescriptor

A description of a label.

JSON representation  
---  
      
    
    {
      "key": string,
      "valueType": enum ([ValueType](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#ValueType)),
      "description": string
    }  
  
Fields  
---  
`key` |  `string` The label key.  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#ValueType)`)` The type of data that can be assigned to the label.  
`description` |  `string` A human-readable description for the label.  
  
## ValueType

Value types that can be used as label values.

Enums  
---  
`STRING` | A variable-length string. This is the default.  
`BOOL` | Boolean; true or false.  
`INT64` | A 64-bit signed integer.  
  
## MetricKind

The kind of measurement. It describes how the data is reported. For information on setting the start time and end time based on the MetricKind, see [TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.snoozes#TimeInterval).

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
`DISTRIBUTION` | The value is a ``Distribution``.  
`MONEY` | The value is money.  
  
## MetricDescriptorMetadata

Additional annotations that can be used to guide the usage of a metric.

JSON representation  
---  
      
    
    {
      "launchStage": enum ([LaunchStage](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LaunchStage)),
      "samplePeriod": string,
      "ingestDelay": string,
      "timeSeriesResourceHierarchyLevel": [
        enum ([TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#TimeSeriesResourceHierarchyLevel))
      ]
    }  
  
Fields  
---  
`launchStage  
**(deprecated)**` |  `enum (`[LaunchStage](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LaunchStage)`)` This item is deprecated!Deprecated. Must use the `[MetricDescriptor.launch_stage](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#MetricDescriptor.FIELDS.launch_stage)` instead.  
`samplePeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The sampling period of metric data points. For metrics which are written periodically, consecutive data points are stored at this time interval, excluding data loss due to errors. Metrics with a higher granularity have a smaller sampling period.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`ingestDelay` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The delay of data points caused by ingestion. Data points older than this age are guaranteed to be ingested and available to be read, excluding data loss due to errors.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`timeSeriesResourceHierarchyLevel[]` |  `enum (`[TimeSeriesResourceHierarchyLevel](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#TimeSeriesResourceHierarchyLevel)`)` The scope of the timeseries data of the metric.  
  
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
  
## TimeSeriesResourceHierarchyLevel

The resource hierarchy level of the timeseries data of a metric.

Enums  
---  
`TIME_SERIES_RESOURCE_HIERARCHY_LEVEL_UNSPECIFIED` | Do not use this default value.  
`PROJECT` | Scopes a metric to a project.  
`ORGANIZATION` | Scopes a metric to an organization.  
`FOLDER` | Scopes a metric to a folder.  
  
## BucketOptions

`BucketOptions` describes the bucket boundaries used to create a histogram for the distribution. The buckets can be in a linear sequence, an exponential sequence, or each bucket can be specified explicitly. `BucketOptions` does not include the number of values in each bucket.

A bucket has an inclusive lower bound and exclusive upper bound for the values that are counted for that bucket. The upper bound of a bucket must be strictly greater than the lower bound. The sequence of N buckets for a distribution consists of an underflow bucket (number 0), zero or more finite buckets (number 1 through N - 2) and an overflow bucket (number N - 1). The buckets are contiguous: the lower bound of bucket i (i > 0) is the same as the upper bound of bucket i - 1. The buckets span the whole range of finite values: lower bound of the underflow bucket is -infinity and the upper bound of the overflow bucket is +infinity. The finite buckets are so-called because both bounds are finite.

JSON representation  
---  
      
    
    {
    
      // Union field options can be only one of the following:
      "linearBuckets": {
        object ([Linear](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#Linear))
      },
      "exponentialBuckets": {
        object ([Exponential](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#Exponential))
      },
      "explicitBuckets": {
        object ([Explicit](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#Explicit))
      }
      // End of list of possible types for union field options.
    }  
  
Fields  
---  
Union field `options`. Exactly one of these three fields must be set. `options` can be only one of the following:  
`linearBuckets` |  `object (`[Linear](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#Linear)`)` The linear bucket.  
`exponentialBuckets` |  `object (`[Exponential](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#Exponential)`)` The exponential buckets.  
`explicitBuckets` |  `object (`[Explicit](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#Explicit)`)` The explicit buckets.  
  
## Linear

Specifies a linear sequence of buckets that all have the same width (except overflow and underflow). Each bucket represents a constant absolute uncertainty on the specific value in the bucket.

There are `numFiniteBuckets + 2` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): offset + (width * i).

Lower bound (1 <= i < N): offset + (width * (i - 1)).

JSON representation  
---  
      
    
    {
      "numFiniteBuckets": integer,
      "width": number,
      "offset": number
    }  
  
Fields  
---  
`numFiniteBuckets` |  `integer` Must be greater than 0.  
`width` |  `number` Must be greater than 0.  
`offset` |  `number` Lower bound of the first bucket.  
  
## Exponential

Specifies an exponential sequence of buckets that have a width that is proportional to the value of the lower bound. Each bucket represents a constant relative uncertainty on a specific value in the bucket.

There are `numFiniteBuckets + 2` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): scale * (growthFactor ^ i).

Lower bound (1 <= i < N): scale * (growthFactor ^ (i - 1)).

JSON representation  
---  
      
    
    {
      "numFiniteBuckets": integer,
      "growthFactor": number,
      "scale": number
    }  
  
Fields  
---  
`numFiniteBuckets` |  `integer` Must be greater than 0.  
`growthFactor` |  `number` Must be greater than 1.  
`scale` |  `number` Must be greater than 0.  
  
## Explicit

Specifies a set of buckets with arbitrary widths.

There are `size(bounds) + 1` (= N) buckets. Bucket `i` has the following boundaries:

Upper bound (0 <= i < N-1): bounds[i] Lower bound (1 <= i < N); bounds[i - 1]

The `bounds` field must contain at least one element. If `bounds` has only one element, then there are no finite buckets, and that single element is the common boundary of the overflow and underflow buckets.

JSON representation  
---  
      
    
    {
      "bounds": [
        number
      ]
    }  
  
Fields  
---  
`bounds[]` |  `number` The values must be monotonically increasing.  
  
## ApiVersion

Logging API version.

Enums  
---  
`V2` | Logging API v2.  
`V1` | Logging API v1.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/create)`

|  Creates a logs-based metric.  
  
### `[delete](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/delete)`

|  Deletes a logs-based metric.  
  
### `[get](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/get)`

|  Gets a logs-based metric.  
  
### `[list](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/list)`

|  Lists logs-based metrics.  
  
### `[update](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics/update)`

|  Creates or updates a logs-based metric.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-02 UTC."],[],[]] 
