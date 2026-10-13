---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.monitoring.v3
title: Package google.monitoring.v3 \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:56.003152+00:00
---

# Package google.monitoring.v3  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.monitoring.v3

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Package google.monitoring.v3 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[Point](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.monitoring.v3#google.monitoring.v3.Point)` (message)
  * `[TimeInterval](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.monitoring.v3#google.monitoring.v3.TimeInterval)` (message)
  * `[TimeSeries](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeries)` (message)
  * `[TypedValue](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.monitoring.v3#google.monitoring.v3.TypedValue)` (message)



## Point

A single data point in a time series.

Fields  
---  
`interval` |  `[TimeInterval](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.monitoring.v3#google.monitoring.v3.TimeInterval)` The time interval to which the data point applies. For `GAUGE` metrics, the start time is optional, but if it is supplied, it must equal the end time. For `DELTA` metrics, the start and end time should specify a non-zero interval, with subsequent points specifying contiguous and non-overlapping intervals. For `CUMULATIVE` metrics, the start and end time should specify a non-zero interval, with subsequent points specifying the same start time and increasing end times, until an event resets the cumulative value to zero and sets a new start time for the following points.  
`value` |  `[TypedValue](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.monitoring.v3#google.monitoring.v3.TypedValue)` The value of the data point.  
  
## TimeInterval

A time interval extending just after a start time through an end time. If the start time is the same as the end time, then the interval represents a single point in time.

Fields  
---  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Required. The end of the time interval.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. The beginning of the time interval. The default value for the start time is the end time. The start time must not be later than the end time.  
  
## TimeSeries

A collection of data points that describes the time-varying values of a metric. A time series is identified by a combination of a fully-specified monitored resource and a fully-specified metric. This type is used for both listing and creating time series.

Fields  
---  
`metric` |  `[Metric](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.api#google.api.Metric)` The associated metric. A fully-specified metric used to identify the time series.  
`resource` |  `[MonitoredResource](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.api#google.api.MonitoredResource)` The associated monitored resource. Custom metrics can use only certain monitored resource types in their time series data. For more information, see [Monitored resources for custom metrics](https://cloud.google.com/monitoring/custom-metrics/creating-metrics#custom-metric-resources).  
`metadata` |  `[MonitoredResourceMetadata](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.api#google.api.MonitoredResourceMetadata)` Output only. The associated monitored resource metadata. When reading a time series, this field will include metadata labels that are explicitly named in the reduction. When creating a time series, this field is ignored.  
`metric_kind` |  `[MetricKind](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.api#google.api.MetricDescriptor.MetricKind)` The metric kind of the time series. When listing time series, this metric kind might be different from the metric kind of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the metric kind of the associated metric. If the associated metric's descriptor must be auto-created, then this field specifies the metric kind of the new descriptor and must be either `GAUGE` (the default) or `CUMULATIVE`.  
`value_type` |  `[ValueType](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.api#google.api.MetricDescriptor.ValueType)` The value type of the time series. When listing time series, this value type might be different from the value type of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the type of the data in the `points` field.  
`points[]` |  `[Point](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.monitoring.v3#google.monitoring.v3.Point)` The data points of this time series. When listing time series, points are returned in reverse time order.When creating a time series, this field must contain exactly one point and the point's type must be the same as the value type of the associated metric. If the associated metric's descriptor must be auto-created, then the value type of the descriptor is determined by the point's type, which must be `BOOL`, `INT64`, `DOUBLE`, or `DISTRIBUTION`.  
`unit` |  `string` The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values. This field can only be changed through CreateTimeSeries when it is empty.  
`description` |  `string` Input only. A detailed description of the time series that will be associated with the `[google.api.MetricDescriptor](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.api#google.api.MetricDescriptor)` for the metric. Once set, this field cannot be changed through CreateTimeSeries.  
  
## TypedValue

A single strongly-typed value.

Fields  
---  
Union field `value`. The typed value field. `value` can be only one of the following:  
`bool_value` |  `bool` A Boolean value: `true` or `false`.  
`int64_value` |  `int64` A 64-bit integer. Its range is approximately ±9.2x1018.  
`double_value` |  `double` A 64-bit double-precision floating-point number. Its magnitude is approximately ±10±300 and it has 16 significant digits of precision.  
`string_value` |  `string` A variable-length string value.  
`distribution_value` |  `[Distribution](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.api#google.api.Distribution)` A distribution value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-08 UTC."],[],[]] 
