---
url: https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types/
title: Value types and metric kinds \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:49.510915+00:00
---

# Value types and metric kinds  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Value types and metric kinds Stay organized with collections  Save and categorize content based on your preferences. 

In the discussion of the metric model, the section [Metric types](https://docs.cloud.google.com/monitoring/api/v3/metric-model#metric_types) provides a general discussion of the attributes that describe a metric type. This section provides a more detailed discussion of two of those attributes:

  * Value type
  * Metric kind



### Value type

The _value type_ is the data type for the measurements. Each time series records the value type (type [`ValueType`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#ValueType)) for its data points.

  * For measurements consisting of a single value at a time, like boolean values and numeric data, the value type tells you how the data is stored:

    * `BOOL`, a boolean
    * `INT64`, a 64-bit integer
    * `DOUBLE`, a double-precision float
    * `STRING`, a string
  * For distribution measurements, the value isn't a single value but a group of values. The value type for distribution measurements is `DISTRIBUTION`.

A distribution contains statistics that summarize a group of values. The values in a distribution include the mean, count, max, and other statistics, computed for a group of values. A distribution can also include a histogram that represents how the values are distributed across a set of ranges.




Latency metrics typically capture data as distributions. For more information about distributions, see the [`Distribution`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TypedValue#Distribution) reference page. For information about charting these metrics, see [Distribution metrics](https://docs.cloud.google.com/monitoring/charts/charting-distribution-metrics). 

### Metric kind

Each time series includes the metric kind (type [`MetricKind`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind)) for its data points. The _kind_ of metric data tells you how to interpret the values relative to each other. Cloud Monitoring metrics are one of three kinds:

  * A _gauge_ metric, in which the value measures a specific instant in time. For example, metrics measuring CPU utilization are gauge metrics; each point records the CPU utilization at the time of measurement. Another example of a gauge metric is the current temperature.

  * A _delta_ metric, in which the value measures the change in a time interval. For reads, the time interval is half-open, it excludes the start time but includes the end time: `(startTime, endTime]`. For example, metrics measuring request counts are delta metrics; each value records how many requests were received after the start time, up to and including the end time.

**Note:** All metrics that count discrete items over a time interval are delta metrics. It is reasonable to expect such values to be integers, but for historical implementation reasons, they are reported as floating-point numbers. 
  * A _cumulative_ metric, in which the value constantly increases over time. For example, a metric for “sent bytes” might be cumulative; each value records the total number of bytes sent by a service at that time.




### Supported combinations

Not all combinations of metric kind and value type make sense. For example, you never see a delta metric with boolean data. There are certain combinations that make sense together.

The following table lists the supported metric kinds and value types:

Value type | GAUGE | DELTA | CUMULATIVE4  
---|---|---|---  
BOOL | yes | no | no  
INT64 | yes | yes1 | yes  
DOUBLE | yes | yes1 | yes  
STRING | yes1 | no | no  
DISTRIBUTION | yes2 | yes1, 3 | yes  
  
1 This combination isn't permitted in custom metrics, `custom.googleapis.com`.  
2 This combination isn't permitted for log-based metrics. For more information, see [Configure distribution-type log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics/distribution-metrics#api).  
3 This is the only combination permitted for log-based metrics, `logging.googleapis.com/user`, with value type `DISTRIBUTION`; for more information, see the [`metricDescriptor` field](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/projects.metrics#LogMetric.FIELDS.metric_descriptor) in the Logging API `LogMetric` reference.  
4 Cumulative metrics can't be used directly for charting or alerting in Monitoring, but they can be aggregated into non-cumulative metrics that can be used in these ways. See [Kinds, types, and conversions](https://docs.cloud.google.com/monitoring/api/v3/aggregation#ts-conversion) for more information.

Additionally, if you are creating your own metrics, you must use only valid combinations of value types and metric kinds.

#### Emulating string-valued custom metrics

String values in custom metrics are not supported, but you can replicate string-valued metric functionality in the following ways:

  * Create a GAUGE metric using an INT64 value as an enum that maps to a string value. Externally translate the enum to a string value when you query the metric.
  * Create a GAUGE metric with a BOOL value and a label whose value is one of the strings you want to monitor. Use the boolean to indicate if the value is the active value.



For example, suppose you want to create a string-valued metric called "status" with possible options OK, OFFLINE, or PENDING. You could make a GAUGE metric with a label called `status_value`. Each update would write three time series, one for each `status_value` (OK, OFFLINE, or PENDING), with a value of 1 for "true" or 0 for "false". 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
