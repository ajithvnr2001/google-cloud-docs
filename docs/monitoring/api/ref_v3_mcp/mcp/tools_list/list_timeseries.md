---
url: https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries/
title: MCP Tools Reference: monitoring.googleapis.com \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:23.038039+00:00
---

# MCP Tools Reference: monitoring.googleapis.com  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  MCP Tools Reference: monitoring.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_timeseries`

Lists time series data from the Google Cloud Monitoring API

The following code sample shows how to use `curl` to call the `list_timeseries` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://monitoring.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_timeseries",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

The `ListTimeSeries` request.

### ListTimeSeriesRequest

JSON representation  
---  
      
    
    {
      "name": string,
      "filter": string,
      "interval": {
        object ([TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.TimeInterval))
      },
      "aggregation": {
        object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aggregation))
      },
      "secondaryAggregation": {
        object ([Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aggregation))
      },
      "orderBy": string,
      "view": enum ([TimeSeriesView](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.TimeSeriesView)),
      "pageSize": integer,
      "pageToken": string
    }  
  
Fields  
---  
`name` |  `string` Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name), organization or folder on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    organizations/[ORGANIZATION_ID]
    folders/[FOLDER_ID]
      
  
`filter` |  `string` Required. A [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that specifies which time series should be returned. The filter must specify a single metric type, and can additionally specify metric labels and other information. For example:
    
    
    metric.type = "compute.googleapis.com/instance/cpu/usage_time" AND
        metric.labels.instance_name = "my-instance-name"
      
  
`interval` |  `object (`[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.TimeInterval)`)` Required. The time interval for which results should be returned. Only time series that contain data points in the specified interval are included in the response.  
`aggregation` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aggregation)`)` Specifies the alignment of data points in individual time series as well as how to combine the retrieved time series across specified labels.By default (if no `aggregation` is explicitly specified), the raw time series data is returned.  
`secondaryAggregation` |  `object (`[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aggregation)`)` Apply a second aggregation after `aggregation` is applied. May only be specified if `aggregation` is specified.  
`orderBy` |  `string` Unsupported: must be left blank. The points in each time series are currently returned in reverse time order (most recent to oldest).  
`view` |  `enum (`[TimeSeriesView](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.TimeSeriesView)`)` Required. Specifies which information is returned about the time series.  
`pageSize` |  `integer` A positive number that is the maximum number of results to return. If `page_size` is empty or more than 100,000 results, the effective `page_size` is 100,000 results. If `view` is set to `FULL`, this is the maximum number of `Points` returned. If `view` is set to `HEADERS`, this is the maximum number of `TimeSeries` returned.  
`pageToken` |  `string` If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
  
### TimeInterval

JSON representation  
---  
      
    
    {
      "endTime": string,
      "startTime": string
    }  
  
Fields  
---  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The end of the time interval.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The beginning of the time interval. The default value for the start time is the end time. The start time must not be later than the end time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### Aggregation

JSON representation  
---  
      
    
    {
      "alignmentPeriod": string,
      "perSeriesAligner": enum ([Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aligner)),
      "crossSeriesReducer": enum ([Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Reducer)),
      "groupByFields": [
        string
      ]
    }  
  
Fields  
---  
`alignmentPeriod` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The `alignment_period` specifies a time interval, in seconds, that is used to divide the data in all the `[time series](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.TimeSeries)` into consistent blocks of time. This will be done before the per-series aligner can be applied to the data.The value must be at least 60 seconds. If a per-series aligner other than `ALIGN_NONE` is specified, this field is required or an error is returned. If no per-series aligner is specified, or the aligner `ALIGN_NONE` is specified, then this field is ignored.The maximum value of the `alignment_period` is 104 weeks (2 years) for charts, and 90,000 seconds (25 hours) for alerting policies.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`perSeriesAligner` |  `enum (`[Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Aligner)`)` An `Aligner` describes how to bring the data points in a single time series into temporal alignment. Except for `ALIGN_NONE`, all alignments cause all the data points in an `alignment_period` to be mathematically grouped together, resulting in a single data point for each `alignment_period` with end timestamp at the end of the period.Not all alignment operations may be applied to all time series. The valid choices depend on the `metric_kind` and `value_type` of the original time series. Alignment can change the `metric_kind` or the `value_type` of the time series.Time series data must be aligned in order to perform cross-time series reduction. If `cross_series_reducer` is specified, then `per_series_aligner` must be specified and not equal to `ALIGN_NONE` and `alignment_period` must be specified; otherwise, an error is returned.  
`crossSeriesReducer` |  `enum (`[Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.Reducer)`)` The reduction operation to be used to combine time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.Not all reducer operations can be applied to all time series. The valid choices depend on the `metric_kind` and the `value_type` of the original time series. Reduction can yield a time series with a different `metric_kind` or `value_type` than the input time series.Time series data must first be aligned (see `per_series_aligner`) in order to perform cross-time series reduction. If `cross_series_reducer` is specified, then `per_series_aligner` must be specified, and must not be `ALIGN_NONE`. An `alignment_period` must also be specified; otherwise, an error is returned.  
`groupByFields[]` |  `string` The set of fields to preserve when `cross_series_reducer` is specified. The `group_by_fields` determine how the time series are partitioned into subsets prior to applying the aggregation operation. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The `cross_series_reducer` is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains `resource.type`. Fields not specified in `group_by_fields` are aggregated away. If `group_by_fields` is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If `cross_series_reducer` is not defined, this field is ignored.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### Aligner

The `Aligner` specifies the operation that will be applied to the data points in each alignment period in a time series. Except for `ALIGN_NONE`, which specifies that no operation be applied, each alignment operation replaces the set of data values in each alignment period with a single value: the result of applying the operation to the data values. An aligned time series has a single data value at the end of each `alignment_period`.

An alignment operation can change the data type of the values, too. For example, if you apply a counting operation to boolean values, the data `value_type` in the original time series is `BOOLEAN`, but the `value_type` in the aligned result is `INT64`.

Enums  
---  
`ALIGN_NONE` | No alignment. Raw data is returned. Not valid if cross-series reduction is requested. The `value_type` of the result is the same as the `value_type` of the input.  
`ALIGN_DELTA` | Align and convert to `DELTA`. The output is `delta = y1 - y0`.This alignment is valid for `CUMULATIVE` and `DELTA` metrics. If the selected alignment period results in periods with no data, then the aligned value for such a period is created by interpolation. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_RATE` | Align and convert to a rate. The result is computed as `rate = (y1 - y0)/(t1 - t0)`, or "delta over time". Think of this aligner as providing the slope of the line that passes through the value at the start and at the end of the `alignment_period`.This aligner is valid for `CUMULATIVE` and `DELTA` metrics with numeric values. If the selected alignment period results in periods with no data, then the aligned value for such a period is created by interpolation. The output is a `GAUGE` metric with `value_type` `DOUBLE`.If, by "rate", you mean "percentage change", see the `ALIGN_PERCENT_CHANGE` aligner instead.  
`ALIGN_INTERPOLATE` | Align by interpolating between adjacent points around the alignment period boundary. This aligner is valid for `GAUGE` metrics with numeric values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_NEXT_OLDER` | Align by moving the most recent data point before the end of the alignment period to the boundary at the end of the alignment period. This aligner is valid for `GAUGE` metrics. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_MIN` | Align the time series by returning the minimum value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_MAX` | Align the time series by returning the maximum value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_MEAN` | Align the time series by returning the mean value in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the aligned result is `DOUBLE`.  
`ALIGN_COUNT` | Align the time series by returning the number of values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric or Boolean values. The `value_type` of the aligned result is `INT64`.  
`ALIGN_SUM` | Align the time series by returning the sum of the values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric and distribution values. The `value_type` of the aligned result is the same as the `value_type` of the input.  
`ALIGN_STDDEV` | Align the time series by returning the standard deviation of the values in each alignment period. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. The `value_type` of the output is `DOUBLE`.  
`ALIGN_COUNT_TRUE` | Align the time series by returning the number of `True` values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The `value_type` of the output is `INT64`.  
`ALIGN_COUNT_FALSE` | Align the time series by returning the number of `False` values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The `value_type` of the output is `INT64`.  
`ALIGN_FRACTION_TRUE` | Align the time series by returning the ratio of the number of `True` values to the total number of values in each alignment period. This aligner is valid for `GAUGE` metrics with Boolean values. The output value is in the range [0.0, 1.0] and has `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_99` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 99th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_95` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 95th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_50` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 50th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENTILE_05` | Align the time series by using [percentile aggregation](https://en.wikipedia.org/wiki/Percentile). The resulting data point in each alignment period is the 5th percentile of all data points in the period. This aligner is valid for `GAUGE` and `DELTA` metrics with distribution values. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
`ALIGN_PERCENT_CHANGE` | Align and convert to a percentage change. This aligner is valid for `GAUGE` and `DELTA` metrics with numeric values. This alignment returns `((current - previous)/previous) * 100`, where the value of `previous` is determined based on the `alignment_period`.If the values of `current` and `previous` are both 0, then the returned value is 0. If only `previous` is 0, the returned value is infinity.A 10-minute moving mean is computed at each point of the alignment period prior to the above calculation to smooth the metric and prevent false positives from very short-lived spikes. The moving mean is only applicable for data whose values are `>= 0`. Any values `< 0` are treated as a missing datapoint, and are ignored. While `DELTA` metrics are accepted by this alignment, special care should be taken that the values for the metric will always be positive. The output is a `GAUGE` metric with `value_type` `DOUBLE`.  
  
### Reducer

A Reducer operation describes how to aggregate data points from multiple time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.

Enums  
---  
`REDUCE_NONE` | No cross-time series reduction. The output of the `Aligner` is returned.  
`REDUCE_MEAN` | Reduce by computing the mean value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric or distribution values. The `value_type` of the output is `DOUBLE`.  
`REDUCE_MIN` | Reduce by computing the minimum value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric values. The `value_type` of the output is the same as the `value_type` of the input.  
`REDUCE_MAX` | Reduce by computing the maximum value across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric values. The `value_type` of the output is the same as the `value_type` of the input.  
`REDUCE_SUM` | Reduce by computing the sum across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric and distribution values. The `value_type` of the output is the same as the `value_type` of the input.  
`REDUCE_STDDEV` | Reduce by computing the standard deviation across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics with numeric or distribution values. The `value_type` of the output is `DOUBLE`.  
`REDUCE_COUNT` | Reduce by computing the number of data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of numeric, Boolean, distribution, and string `value_type`. The `value_type` of the output is `INT64`.  
`REDUCE_COUNT_TRUE` | Reduce by computing the number of `True`-valued data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `value_type`. The `value_type` of the output is `INT64`.  
`REDUCE_COUNT_FALSE` | Reduce by computing the number of `False`-valued data points across time series for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `value_type`. The `value_type` of the output is `INT64`.  
`REDUCE_FRACTION_TRUE` | Reduce by computing the ratio of the number of `True`-valued data points to the total number of data points for each alignment period. This reducer is valid for `DELTA` and `GAUGE` metrics of Boolean `value_type`. The output value is in the range [0.0, 1.0] and has `value_type` `DOUBLE`.  
`REDUCE_PERCENTILE_99` | Reduce by computing the [99th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_95` | Reduce by computing the [95th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_50` | Reduce by computing the [50th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
`REDUCE_PERCENTILE_05` | Reduce by computing the [5th percentile](https://en.wikipedia.org/wiki/Percentile) of data points across time series for each alignment period. This reducer is valid for `GAUGE` and `DELTA` metrics of numeric and distribution type. The value of the output is `DOUBLE`.  
  
### TimeSeriesView

Controls which fields are returned by `ListTimeSeries*`.

Enums  
---  
`FULL` | Returns the identity of the metric(s), the time series, and the time series data.  
`HEADERS` | Returns the identity of the metric and the time series resource, but not the time series data.  
  
## Output Schema

The `ListTimeSeries` response.

### ListTimeSeriesResponse

JSON representation  
---  
      
    
    {
      "timeSeries": [
        {
          object ([TimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.TimeSeries))
        }
      ],
      "nextPageToken": string,
      "executionErrors": [
        {
          object ([Status](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Status))
        }
      ],
      "unit": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`timeSeries[]` |  `object (`[TimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.TimeSeries)`)` One or more time series that match the filter included in the request.  
`nextPageToken` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
`executionErrors[]` |  `object (`[Status](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Status)`)` Query execution errors that may have caused the time series data returned to be incomplete.  
`unit` |  `string` The unit in which all `time_series` point values are reported. `unit` follows the UCUM format for units as seen in <https://unitsofmeasure.org/ucum.html>. If different `time_series` have different units (for example, because they come from different metric types, or a unit is absent), then `unit` will be "{not_a_unit}".  
`unreachable[]` |  `string` Cloud regions that were unreachable which may have caused incomplete data to be returned.  
  
### TimeSeries

JSON representation  
---  
      
    
    {
      "metric": {
        object ([Metric](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Metric))
      },
      "resource": {
        object ([MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MonitoredResource))
      },
      "metadata": {
        object ([MonitoredResourceMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MonitoredResourceMetadata))
      },
      "metricKind": enum ([MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MetricKind)),
      "valueType": enum ([ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.ValueType)),
      "points": [
        {
          object ([Point](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Point))
        }
      ],
      "unit": string,
      "description": string
    }  
  
Fields  
---  
`metric` |  `object (`[Metric](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Metric)`)` The associated metric. A fully-specified metric used to identify the time series.  
`resource` |  `object (`[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MonitoredResource)`)` The associated monitored resource. Custom metrics can use only certain monitored resource types in their time series data. For more information, see [Monitored resources for custom metrics](https://cloud.google.com/monitoring/custom-metrics/creating-metrics#custom-metric-resources).  
`metadata` |  `object (`[MonitoredResourceMetadata](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MonitoredResourceMetadata)`)` Output only. The associated monitored resource metadata. When reading a time series, this field will include metadata labels that are explicitly named in the reduction. When creating a time series, this field is ignored.  
`metricKind` |  `enum (`[MetricKind](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.MetricKind)`)` The metric kind of the time series. When listing time series, this metric kind might be different from the metric kind of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the metric kind of the associated metric. If the associated metric's descriptor must be auto-created, then this field specifies the metric kind of the new descriptor and must be either `GAUGE` (the default) or `CUMULATIVE`.  
`valueType` |  `enum (`[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.ValueType)`)` The value type of the time series. When listing time series, this value type might be different from the value type of the associated metric if this time series is an alignment or reduction of other time series.When creating a time series, this field is optional. If present, it must be the same as the type of the data in the `points` field.  
`points[]` |  `object (`[Point](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Point)`)` The data points of this time series. When listing time series, points are returned in reverse time order.When creating a time series, this field must contain exactly one point and the point's type must be the same as the value type of the associated metric. If the associated metric's descriptor must be auto-created, then the value type of the descriptor is determined by the point's type, which must be `BOOL`, `INT64`, `DOUBLE`, or `DISTRIBUTION`.  
`unit` |  `string` The units in which the metric value is reported. It is only applicable if the `value_type` is `INT64`, `DOUBLE`, or `DISTRIBUTION`. The `unit` defines the representation of the stored metric values. This field can only be changed through CreateTimeSeries when it is empty.  
`description` |  `string` Input only. A detailed description of the time series that will be associated with the `[google.api.MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.MetricDescriptor)` for the metric. Once set, this field cannot be changed through CreateTimeSeries.  
  
### Metric

JSON representation  
---  
      
    
    {
      "type": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`type` |  `string` An existing metric type, see `[google.api.MetricDescriptor](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_metric_descriptors#Output.Schema.MetricDescriptor)`. For example, `custom.googleapis.com/invoice/paid/amount`.  
`labels` |  `map (key: string, value: string)` The set of label values that uniquely identify this metric. All labels listed in the `MetricDescriptor` must be assigned values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### MonitoredResource

JSON representation  
---  
      
    
    {
      "type": string,
      "labels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`type` |  `string` Required. The monitored resource type. This field must match the `type` field of a `MonitoredResourceDescriptor` object. For example, the type of a Compute Engine VM instance is `gce_instance`. For a list of types, see [Monitoring resource types](https://cloud.google.com/monitoring/api/resources) and [Logging resource types](https://cloud.google.com/logging/docs/api/v2/resource-list).  
`labels` |  `map (key: string, value: string)` Required. Values for all of the labels listed in the associated monitored resource descriptor. For example, Compute Engine VM instances use the labels `"project_id"`, `"instance_id"`, and `"zone"`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### MonitoredResourceMetadata

JSON representation  
---  
      
    
    {
      "systemLabels": {
        object
      },
      "userLabels": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`systemLabels` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. Values for predefined system metadata labels. System labels are a kind of metadata extracted by Google, including "machine_image", "vpc", "subnet_id", "security_group", "name", etc. System label values can be only strings, Boolean values, or a list of strings. For example:
    
    
    { "name": "my-test-instance",
      "security_group": ["a", "b", "c"],
      "spot_instance": false }
      
  
`userLabels` |  `map (key: string, value: string)` Output only. A map of user-defined metadata labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### UserLabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Point

JSON representation  
---  
      
    
    {
      "interval": {
        object ([TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.TimeInterval))
      },
      "value": {
        object ([TypedValue](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.TypedValue))
      }
    }  
  
Fields  
---  
`interval` |  `object (`[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.TimeInterval)`)` The time interval to which the data point applies. For `GAUGE` metrics, the start time is optional, but if it is supplied, it must equal the end time. For `DELTA` metrics, the start and end time should specify a non-zero interval, with subsequent points specifying contiguous and non-overlapping intervals. For `CUMULATIVE` metrics, the start and end time should specify a non-zero interval, with subsequent points specifying the same start time and increasing end times, until an event resets the cumulative value to zero and sets a new start time for the following points.  
`value` |  `object (`[TypedValue](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.TypedValue)`)` The value of the data point.  
  
### TimeInterval

JSON representation  
---  
      
    
    {
      "endTime": string,
      "startTime": string
    }  
  
Fields  
---  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Required. The end of the time interval.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. The beginning of the time interval. The default value for the start time is the end time. The start time must not be later than the end time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### TypedValue

JSON representation  
---  
      
    
    {
    
      // Union field value can be only one of the following:
      "boolValue": boolean,
      "int64Value": string,
      "doubleValue": number,
      "stringValue": string,
      "distributionValue": {
        object ([Distribution](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Distribution))
      }
      // End of list of possible types for union field value.
    }  
  
Fields  
---  
Union field `value`. The typed value field. `value` can be only one of the following:  
`boolValue` |  `boolean` A Boolean value: `true` or `false`.  
`int64Value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` A 64-bit integer. Its range is approximately ±9.2x1018.  
`doubleValue` |  `number` A 64-bit double-precision floating-point number. Its magnitude is approximately ±10±300 and it has 16 significant digits of precision.  
`stringValue` |  `string` A variable-length string value.  
`distributionValue` |  `object (`[Distribution](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Distribution)`)` A distribution value.  
  
### Distribution

JSON representation  
---  
      
    
    {
      "count": string,
      "mean": number,
      "sumOfSquaredDeviation": number,
      "range": {
        object ([Range](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Range))
      },
      "bucketOptions": {
        object ([BucketOptions](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.BucketOptions))
      },
      "bucketCounts": [
        string
      ],
      "exemplars": [
        {
          object ([Exemplar](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Exemplar))
        }
      ]
    }  
  
Fields  
---  
`count` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of values in the population. Must be non-negative. This value must equal the sum of the values in `bucket_counts` if a histogram is provided.  
`mean` |  `number` The arithmetic mean of the values in the population. If `count` is zero then this field must be zero.  
`sumOfSquaredDeviation` |  `number` The sum of squared deviations from the mean of the values in the population. For values x_i this is:
    
    
    Sum[i=1..n]((x_i - mean)^2)
    

Knuth, "The Art of Computer Programming", Vol. 2, page 232, 3rd edition describes Welford's method for accumulating this sum in one pass.If `count` is zero then this field must be zero.  
`range` |  `object (`[Range](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Range)`)` If specified, contains the range of the population values. The field must not be present if the count is zero. This field is presently ignored by the Cloud Monitoring API v3.  
`bucketOptions` |  `object (`[BucketOptions](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.BucketOptions)`)` Required in the Cloud Monitoring API v3. Defines the histogram bucket boundaries.  
`bucketCounts[]` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required in the Cloud Monitoring API v3. The values for each bucket specified in `bucket_options`. The sum of the values in `bucketCounts` must equal the value in the count field of the `Distribution` object. The order of the bucket counts follows the numbering schemes described for the three bucket types. The underflow bucket has number 0; the finite buckets, if any, have numbers 1 through N-2; and the overflow bucket has number N-1. The size of `bucket_counts` must not be greater than N. If the size is less than N, then the remaining buckets are assigned values of zero.  
`exemplars[]` |  `object (`[Exemplar](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Exemplar)`)` Must be in increasing order of `value` field.  
  
### Range

JSON representation  
---  
      
    
    {
      "min": number,
      "max": number
    }  
  
Fields  
---  
`min` |  `number` The minimum of the population values.  
`max` |  `number` The maximum of the population values.  
  
### BucketOptions

JSON representation  
---  
      
    
    {
    
      // Union field options can be only one of the following:
      "linearBuckets": {
        object ([Linear](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Linear))
      },
      "exponentialBuckets": {
        object ([Exponential](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Exponential))
      },
      "explicitBuckets": {
        object ([Explicit](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Explicit))
      }
      // End of list of possible types for union field options.
    }  
  
Fields  
---  
Union field `options`. Exactly one of these three fields must be set. `options` can be only one of the following:  
`linearBuckets` |  `object (`[Linear](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Linear)`)` The linear bucket.  
`exponentialBuckets` |  `object (`[Exponential](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Exponential)`)` The exponential buckets.  
`explicitBuckets` |  `object (`[Explicit](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Explicit)`)` The explicit buckets.  
  
### Linear

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
  
### Exponential

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
  
### Explicit

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
  
### Exemplar

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
  
### Any

JSON representation  
---  
      
    
    {
      "typeUrl": string,
      "value": string
    }  
  
Fields  
---  
`typeUrl` |  `string` Identifies the type of the serialized Protobuf message with a URI reference consisting of a prefix ending in a slash and the fully-qualified type name.Example: type.googleapis.com/google.protobuf.StringValueThis string must contain at least one `/` character, and the content after the last `/` must be the fully-qualified name of the type in canonical form, without a leading dot. Do not write a scheme on these URI references so that clients do not attempt to contact them.The prefix is arbitrary and Protobuf implementations are expected to simply strip off everything up to and including the last `/` to identify the type. `type.googleapis.com/` is a common default prefix that some legacy implementations require. This prefix does not indicate the origin of the type, and URIs containing it are not expected to respond to any requests.All type URL strings must be legal URI references with the additional restriction (for the text format) that the content of the reference must consist only of alphanumeric characters, percent-encoded escapes, and characters in the following set (not including the outer backticks): `/-.~_!$&()*+,;=`. Despite our allowing percent encodings, implementations should not unescape them to prevent confusion with existing parsers. For example, `type.googleapis.com%2FFoo` should be rejected.In the original design of `Any`, the possibility of launching a type resolution service at these type URLs was considered but Protobuf never implemented one and considers contacting these URLs to be problematic and a potential security issue. Do not attempt to contact type URLs.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Holds a Protobuf serialization of the type described by type_url.A base64-encoded string.  
  
### Status

JSON representation  
---  
      
    
    {
      "code": integer,
      "message": string,
      "details": [
        {
          "@type": string,
          field1: ...,
          ...
        }
      ]
    }  
  
Fields  
---  
`code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### MetricKind

The kind of measurement. It describes how the data is reported. For information on setting the start time and end time based on the MetricKind, see `[TimeInterval](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Input.Schema.TimeInterval)`.

Enums  
---  
`METRIC_KIND_UNSPECIFIED` | Do not use this default value.  
`GAUGE` | An instantaneous measurement of a value.  
`DELTA` | The change in a value during a time interval.  
`CUMULATIVE` | A value accumulated over a time interval. Cumulative measurements in a time series should have the same start time and increasing end times, until an event resets the cumulative value to zero and sets a new start time for the following points.  
  
### ValueType

The value type of a metric.

Enums  
---  
`VALUE_TYPE_UNSPECIFIED` | Do not use this default value.  
`BOOL` | The value is a boolean. This value type can be used only if the metric kind is `GAUGE`.  
`INT64` | The value is a signed 64-bit integer.  
`DOUBLE` | The value is a double precision floating point number.  
`STRING` | The value is a text string. This value type can be used only if the metric kind is `GAUGE`.  
`DISTRIBUTION` | The value is a `[`Distribution`](https://docs.cloud.google.com/monitoring/api/ref_v3_mcp/mcp/tools_list/list_timeseries#Output.Schema.Distribution)`.  
`MONEY` | The value is money.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-04 UTC."],[],[]] 
