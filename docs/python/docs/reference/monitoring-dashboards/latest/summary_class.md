---
url: https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/summary_class/
title: Package Classes (3.2.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:26.877575+00:00
---

# Package Classes (3.2.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.22.0  2.21.0  2.20.1  2.19.0  2.18.2  2.17.0  2.16.1  2.15.3  2.14.1  2.13.0  2.12.3  2.11.1  2.10.0  2.9.0  2.8.0  2.7.4  2.6.1  2.5.1  2.4.1  2.3.0  2.2.4  2.1.0  2.0.0  1.0.2  0.1.2 

Summary of entries of Classes for monitoring-dashboards.

## Classes 

### [DashboardsServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.services.dashboards_service.DashboardsServiceAsyncClient)

Manages Stackdriver dashboards. A dashboard is an arrangement of data display widgets in a specific layout.

### [DashboardsServiceClient](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.services.dashboards_service.DashboardsServiceClient)

Manages Stackdriver dashboards. A dashboard is an arrangement of data display widgets in a specific layout.

### [ListDashboardsAsyncPager](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.services.dashboards_service.pagers.ListDashboardsAsyncPager)

A pager for iterating through `list_dashboards` requests.

This class thinly wraps an initial [ListDashboardsResponse](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ListDashboardsResponse) object, and provides an `__aiter__` method to iterate through its `dashboards` field.

If there are more pages, the `__aiter__` method will make additional `ListDashboards` requests and continue to iterate through the `dashboards` field on the corresponding responses.

All the usual [ListDashboardsResponse](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ListDashboardsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDashboardsPager](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.services.dashboards_service.pagers.ListDashboardsPager)

A pager for iterating through `list_dashboards` requests.

This class thinly wraps an initial [ListDashboardsResponse](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ListDashboardsResponse) object, and provides an `__iter__` method to iterate through its `dashboards` field.

If there are more pages, the `__iter__` method will make additional `ListDashboards` requests and continue to iterate through the `dashboards` field on the corresponding responses.

All the usual [ListDashboardsResponse](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ListDashboardsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [Aggregation](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Aggregation)

Describes how to combine multiple time series to provide a different view of the data. Aggregation of time series is done in two steps. First, each time series in the set is _aligned_ to the same time interval boundaries, then the set of time series is optionally _reduced_ in number.

Alignment consists of applying the `per_series_aligner` operation to each time series after its data has been divided into regular `alignment_period` time intervals. This process takes _all_ of the data points in an alignment period, applies a mathematical transformation such as averaging, minimum, maximum, delta, etc., and converts them into a single data point per period.

Reduction is when the aligned and transformed time series can optionally be combined, reducing the number of time series through similar mathematical transformations. Reduction involves applying a `cross_series_reducer` to all the time series, optionally sorting the time series into subsets with `group_by_fields`, and applying the reducer to each subset.

The raw time series data can contain a huge amount of information from multiple sources. Alignment and reduction transforms this mass of data into a more manageable and representative collection of data, for example "the 95% latency across the average of all tasks in a cluster". This representative data can be more easily graphed and comprehended, and the individual time series data is still available for later drilldown. For more details, see `Filtering and aggregation <https://cloud.google.com/monitoring/api/v3/aggregation>`__.

### [Aligner](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Aggregation.Aligner)

The `Aligner` specifies the operation that will be applied to the data points in each alignment period in a time series. Except for `ALIGN_NONE`, which specifies that no operation be applied, each alignment operation replaces the set of data values in each alignment period with a single value: the result of applying the operation to the data values. An aligned time series has a single data value at the end of each `alignment_period`.

An alignment operation can change the data type of the values, too. For example, if you apply a counting operation to boolean values, the data `value_type` in the original time series is `BOOLEAN`, but the `value_type` in the aligned result is `INT64`.
    
    
        This alignment is valid for
        `CUMULATIVE][google.api.MetricDescriptor.MetricKind.CUMULATIVE]`
        and `DELTA` metrics. If the selected alignment period
        results in periods with no data, then the aligned value for
        such a period is created by interpolation. The
        `value_type` of the aligned result is the same as the
        `value_type` of the input.
    ALIGN_RATE (2):
        Align and convert to a rate. The result is computed as
        `rate = (y1 - y0)/(t1 - t0)`, or "delta over time". Think
        of this aligner as providing the slope of the line that
        passes through the value at the start and at the end of the
        `alignment_period`.
    
        This aligner is valid for `CUMULATIVE` and `DELTA`
        metrics with numeric values. If the selected alignment
        period results in periods with no data, then the aligned
        value for such a period is created by interpolation. The
        output is a `GAUGE` metric with `value_type` `DOUBLE`.
    
        If, by "rate", you mean "percentage change", see the
        `ALIGN_PERCENT_CHANGE` aligner instead.
    ALIGN_INTERPOLATE (3):
        Align by interpolating between adjacent points around the
        alignment period boundary. This aligner is valid for
        `GAUGE` metrics with numeric values. The `value_type` of
        the aligned result is the same as the `value_type` of the
        input.
    ALIGN_NEXT_OLDER (4):
        Align by moving the most recent data point before the end of
        the alignment period to the boundary at the end of the
        alignment period. This aligner is valid for `GAUGE`
        metrics. The `value_type` of the aligned result is the
        same as the `value_type` of the input.
    ALIGN_MIN (10):
        Align the time series by returning the minimum value in each
        alignment period. This aligner is valid for `GAUGE` and
        `DELTA` metrics with numeric values. The `value_type` of
        the aligned result is the same as the `value_type` of the
        input.
    ALIGN_MAX (11):
        Align the time series by returning the maximum value in each
        alignment period. This aligner is valid for `GAUGE` and
        `DELTA` metrics with numeric values. The `value_type` of
        the aligned result is the same as the `value_type` of the
        input.
    ALIGN_MEAN (12):
        Align the time series by returning the mean value in each
        alignment period. This aligner is valid for `GAUGE` and
        `DELTA` metrics with numeric values. The `value_type` of
        the aligned result is `DOUBLE`.
    ALIGN_COUNT (13):
        Align the time series by returning the number of values in
        each alignment period. This aligner is valid for `GAUGE`
        and `DELTA` metrics with numeric or Boolean values. The
        `value_type` of the aligned result is `INT64`.
    ALIGN_SUM (14):
        Align the time series by returning the sum of the values in
        each alignment period. This aligner is valid for `GAUGE`
        and `DELTA` metrics with numeric and distribution values.
        The `value_type` of the aligned result is the same as the
        `value_type` of the input.
    ALIGN_STDDEV (15):
        Align the time series by returning the standard deviation of
        the values in each alignment period. This aligner is valid
        for `GAUGE` and `DELTA` metrics with numeric values. The
        `value_type` of the output is `DOUBLE`.
    ALIGN_COUNT_TRUE (16):
        Align the time series by returning the number of `True`
        values in each alignment period. This aligner is valid for
        `GAUGE` metrics with Boolean values. The `value_type` of
        the output is `INT64`.
    ALIGN_COUNT_FALSE (24):
        Align the time series by returning the number of `False`
        values in each alignment period. This aligner is valid for
        `GAUGE` metrics with Boolean values. The `value_type` of
        the output is `INT64`.
    ALIGN_FRACTION_TRUE (17):
        Align the time series by returning the ratio of the number
        of `True` values to the total number of values in each
        alignment period. This aligner is valid for `GAUGE`
        metrics with Boolean values. The output value is in the
        range [0.0, 1.0] and has `value_type` `DOUBLE`.
    ALIGN_PERCENTILE_99 (18):
        Align the time series by using `percentile
        aggregation <https://en.wikipedia.org/wiki/Percentile>`__.
        The resulting data point in each alignment period is the
        99th percentile of all data points in the period. This
        aligner is valid for `GAUGE` and `DELTA` metrics with
        distribution values. The output is a `GAUGE` metric with
        `value_type` `DOUBLE`.
    ALIGN_PERCENTILE_95 (19):
        Align the time series by using `percentile
        aggregation <https://en.wikipedia.org/wiki/Percentile>`__.
        The resulting data point in each alignment period is the
        95th percentile of all data points in the period. This
        aligner is valid for `GAUGE` and `DELTA` metrics with
        distribution values. The output is a `GAUGE` metric with
        `value_type` `DOUBLE`.
    ALIGN_PERCENTILE_50 (20):
        Align the time series by using `percentile
        aggregation <https://en.wikipedia.org/wiki/Percentile>`__.
        The resulting data point in each alignment period is the
        50th percentile of all data points in the period. This
        aligner is valid for `GAUGE` and `DELTA` metrics with
        distribution values. The output is a `GAUGE` metric with
        `value_type` `DOUBLE`.
    ALIGN_PERCENTILE_05 (21):
        Align the time series by using `percentile
        aggregation <https://en.wikipedia.org/wiki/Percentile>`__.
        The resulting data point in each alignment period is the 5th
        percentile of all data points in the period. This aligner is
        valid for `GAUGE` and `DELTA` metrics with distribution
        values. The output is a `GAUGE` metric with `value_type`
        `DOUBLE`.
    ALIGN_PERCENT_CHANGE (23):
        Align and convert to a percentage change. This aligner is
        valid for `GAUGE` and `DELTA` metrics with numeric
        values. This alignment returns
        `((current - previous)/previous) * 100`, where the value
        of `previous` is determined based on the
        `alignment_period`.
    
        If the values of `current` and `previous` are both 0,
        then the returned value is 0. If only `previous` is 0, the
        returned value is infinity.
    
        A 10-minute moving mean is computed at each point of the
        alignment period prior to the above calculation to smooth
        the metric and prevent false positives from very short-lived
        spikes. The moving mean is only applicable for data whose
        values are `>= 0`. Any values `< 0` are treated as a
        missing datapoint, and are ignored. While `DELTA` metrics
        are accepted by this alignment, special care should be taken
        that the values for the metric will always be positive. The
        output is a `GAUGE` metric with `value_type` `DOUBLE`.
    

### [Reducer](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Aggregation.Reducer)

A Reducer operation describes how to aggregate data points from multiple time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.

### [AlertChart](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.AlertChart)

A chart that displays alert policy data.

### [ChartOptions](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ChartOptions)

Options to control visual rendering of a chart.

### [Mode](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ChartOptions.Mode)

Chart mode options.

### [CollapsibleGroup](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.CollapsibleGroup)

A widget that groups the other widgets. All widgets that are within the area spanned by the grouping widget are considered member widgets.

### [ColumnLayout](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ColumnLayout)

A simplified layout that divides the available space into vertical columns and arranges a set of widgets vertically in each column.

### [Column](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ColumnLayout.Column)

Defines the layout properties and content for a column.

### [CreateDashboardRequest](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.CreateDashboardRequest)

The `CreateDashboard` request.

### [Dashboard](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Dashboard)

A Google Stackdriver dashboard. Dashboards define the content and layout of pages in the Stackdriver web application.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Dashboard.LabelsEntry)

The abstract base class for a message.

### [DashboardFilter](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.DashboardFilter)

A filter to reduce the amount of data charted in relevant widgets.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FilterType](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.DashboardFilter.FilterType)

The type for the dashboard filter

### [DeleteDashboardRequest](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.DeleteDashboardRequest)

The `DeleteDashboard` request.

### [ErrorReportingPanel](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ErrorReportingPanel)

A widget that displays a list of error groups.

### [GetDashboardRequest](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.GetDashboardRequest)

The `GetDashboard` request.

### [GridLayout](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.GridLayout)

A basic layout divides the available space into vertical columns of equal width and arranges a list of widgets using a row-first strategy.

### [IncidentList](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.IncidentList)

A widget that displays a list of alerts

### [ListDashboardsRequest](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ListDashboardsRequest)

The `ListDashboards` request.

### [ListDashboardsResponse](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.ListDashboardsResponse)

The `ListDashboards` request.

### [LogsPanel](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.LogsPanel)

A widget that displays a stream of log.

### [MosaicLayout](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.MosaicLayout)

A mosaic layout divides the available space into a grid of blocks, and overlays the grid with tiles. Unlike `GridLayout`, tiles may span multiple grid blocks and can be placed at arbitrary locations in the grid.

### [Tile](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.MosaicLayout.Tile)

A single tile in the mosaic. The placement and size of the tile are configurable.

### [PickTimeSeriesFilter](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.PickTimeSeriesFilter)

Describes a ranking-based time series filter. Each input time series is ranked with an aligner. The filter will allow up to `num_time_series` time series to pass through it, selecting them based on the relative ranking.

For example, if `ranking_method` is `METHOD_MEAN`,\ `direction` is `BOTTOM`, and `num_time_series` is 3, then the 3 times series with the lowest mean values will pass through the filter.

### [Direction](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.PickTimeSeriesFilter.Direction)

Describes the ranking directions.

### [Method](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.PickTimeSeriesFilter.Method)

The value reducers that can be applied to a `PickTimeSeriesFilter`.

### [PieChart](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.PieChart)

A widget that displays timeseries data as a pie or a donut.

### [PieChartDataSet](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.PieChart.PieChartDataSet)

Groups a time series query definition.

### [PieChartType](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.PieChart.PieChartType)

Types for the pie chart.

### [RowLayout](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.RowLayout)

A simplified layout that divides the available space into rows and arranges a set of widgets horizontally in each row.

### [Row](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.RowLayout.Row)

Defines the layout properties and content for a row.

### [Scorecard](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Scorecard)

A widget showing the latest value of a metric, and how this value relates to one or more thresholds.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GaugeView](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Scorecard.GaugeView)

A gauge chart shows where the current value sits within a pre-defined range. The upper and lower bounds should define the possible range of values for the scorecard's query (inclusive).

### [SparkChartView](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Scorecard.SparkChartView)

A sparkChart is a small chart suitable for inclusion in a table-cell or inline in text. This message contains the configuration for a sparkChart to show up on a Scorecard, showing recent trends of the scorecard's timeseries.

### [SectionHeader](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.SectionHeader)

A widget that defines a new section header. Sections populate a table of contents and allow easier navigation of long-form content.

### [SingleViewGroup](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.SingleViewGroup)

A widget that groups the other widgets by using a dropdown menu. All widgets that are within the area spanned by the grouping widget are considered member widgets.

### [SparkChartType](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.SparkChartType)

Defines the possible types of spark chart supported by the `Scorecard`.

### [StatisticalTimeSeriesFilter](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.StatisticalTimeSeriesFilter)

A filter that ranks streams based on their statistical relation to other streams in a request. Note: This field is deprecated and completely ignored by the API.

### [Method](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.StatisticalTimeSeriesFilter.Method)

The filter methods that can be applied to a stream.

### [TableDisplayOptions](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.TableDisplayOptions)

Table display options that can be reused.

### [Text](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Text)

A widget that displays textual content.

### [Format](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Text.Format)

The format type of the text content.

### [TextStyle](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Text.TextStyle)

Properties that determine how the title and content are styled

### [FontSize](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Text.TextStyle.FontSize)

Specifies a font size for the title and content of a text widget

### [HorizontalAlignment](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Text.TextStyle.HorizontalAlignment)

The horizontal alignment of both the title and content on a text widget

### [PaddingSize](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Text.TextStyle.PaddingSize)

Specifies padding size around a text widget

### [PointerLocation](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Text.TextStyle.PointerLocation)

Specifies where a visual pointer is placed on a text widget (also sometimes called a "tail")

### [VerticalAlignment](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Text.TextStyle.VerticalAlignment)

The vertical alignment of both the title and content on a text widget

### [Threshold](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Threshold)

Defines a threshold for categorizing time series values.

### [Color](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Threshold.Color)

The color suggests an interpretation to the viewer when actual values cross the threshold. Comments on each color provide UX guidance on how users can be expected to interpret a given state color.

### [Direction](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Threshold.Direction)

Whether the threshold is considered crossed by an actual value above or below its threshold value.

### [TargetAxis](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Threshold.TargetAxis)

An axis identifier.

### [TimeSeriesFilter](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.TimeSeriesFilter)

A filter that defines a subset of time series data that is displayed in a widget. Time series data is fetched using the ``ListTimeSeries` <https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list>`__ method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TimeSeriesFilterRatio](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.TimeSeriesFilterRatio)

A pair of time series filters that define a ratio computation. The output time series is the pair-wise division of each aligned element from the numerator and denominator time series.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RatioPart](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.TimeSeriesFilterRatio.RatioPart)

Describes a query to build the numerator or denominator of a TimeSeriesFilterRatio.

### [TimeSeriesQuery](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.TimeSeriesQuery)

TimeSeriesQuery collects the set of supported methods for querying time series data from the Stackdriver metrics API.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TimeSeriesTable](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.TimeSeriesTable)

A table that displays time series data.

### [ColumnSettings](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.TimeSeriesTable.ColumnSettings)

The persistent settings for a table's columns.

### [MetricVisualization](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.TimeSeriesTable.MetricVisualization)

Enum for metric metric_visualization

### [TableDataSet](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.TimeSeriesTable.TableDataSet)

Groups a time series query definition with table options.

### [UpdateDashboardRequest](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.UpdateDashboardRequest)

The `UpdateDashboard` request.

### [Widget](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.Widget)

Widget contains a single dashboard component and configuration of how to present the component in the dashboard.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [XyChart](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.XyChart)

A chart that displays data on a 2D (X and Y axes) plane.

### [Axis](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.XyChart.Axis)

A chart axis.

### [Scale](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.XyChart.Axis.Scale)

Types of scales used in axes.

### [DataSet](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.XyChart.DataSet)

Groups a time series query definition with charting options.

### [PlotType](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.XyChart.DataSet.PlotType)

The types of plotting strategies for data sets.

### [TargetAxis](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.types.XyChart.DataSet.TargetAxis)

An axis identifier.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/monitoring-dashboards/latest/google.cloud.monitoring_dashboard_v1.services.dashboards_service.pagers)

API documentation for `monitoring_dashboard_v1.services.dashboards_service.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
