---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1
title: Package google.monitoring.dashboard.v1 \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:22.416905+00:00
---

# Package google.monitoring.dashboard.v1  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Package google.monitoring.dashboard.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[DashboardsService](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardsService)` (interface)
  * `[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Aggregation)` (message)
  * `[Aggregation.Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Aggregation.Aligner)` (enum)
  * `[Aggregation.Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Aggregation.Reducer)` (enum)
  * `[AggregationFunction](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.AggregationFunction)` (message)
  * `[AggregationFunction.Parameter](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.AggregationFunction.Parameter)` (message)
  * `[AlertChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.AlertChart)` (message)
  * `[Breakdown](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Breakdown)` (message)
  * `[ChartOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ChartOptions)` (message)
  * `[ChartOptions.Mode](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ChartOptions.Mode)` (enum)
  * `[CollapsibleGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.CollapsibleGroup)` (message)
  * `[ColumnLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ColumnLayout)` (message)
  * `[ColumnLayout.Column](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ColumnLayout.Column)` (message)
  * `[ColumnSortingOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ColumnSortingOptions)` (message)
  * `[CreateDashboardRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.CreateDashboardRequest)` (message)
  * `[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Dashboard)` (message)
  * `[DashboardAnnotations](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardAnnotations)` (message)
  * `[DashboardFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardFilter)` (message)
  * `[DashboardFilter.FilterType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardFilter.FilterType)` (enum)
  * `[DashboardFilter.StringArray](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardFilter.StringArray)` (message)
  * `[DashboardFilter.ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardFilter.ValueType)` (enum)
  * `[DeleteDashboardRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DeleteDashboardRequest)` (message)
  * `[Dimension](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Dimension)` (message)
  * `[ErrorReportingPanel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ErrorReportingPanel)` (message)
  * `[EventAnnotation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.EventAnnotation)` (message)
  * `[EventAnnotation.EventType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.EventAnnotation.EventType)` (enum)
  * `[FilterControl](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.FilterControl)` (message)
  * `[GetDashboardRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.GetDashboardRequest)` (message)
  * `[GridLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.GridLayout)` (message)
  * `[IncidentList](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.IncidentList)` (message)
  * `[ListDashboardsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ListDashboardsRequest)` (message)
  * `[ListDashboardsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ListDashboardsResponse)` (message)
  * `[LogsPanel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.LogsPanel)` (message)
  * `[Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Measure)` (message)
  * `[MosaicLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.MosaicLayout)` (message)
  * `[MosaicLayout.Tile](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.MosaicLayout.Tile)` (message)
  * `[OpsAnalyticsQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.OpsAnalyticsQuery)` (message)
  * `[PickTimeSeriesFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PickTimeSeriesFilter)` (message)
  * `[PickTimeSeriesFilter.Direction](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PickTimeSeriesFilter.Direction)` (enum)
  * `[PickTimeSeriesFilter.Method](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PickTimeSeriesFilter.Method)` (enum)
  * `[PieChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PieChart)` (message)
  * `[PieChart.PieChartDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PieChart.PieChartDataSet)` (message)
  * `[PieChart.PieChartType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PieChart.PieChartType)` (enum)
  * `[RowLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.RowLayout)` (message)
  * `[RowLayout.Row](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.RowLayout.Row)` (message)
  * `[Scorecard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Scorecard)` (message)
  * `[Scorecard.GaugeView](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Scorecard.GaugeView)` (message)
  * `[Scorecard.SparkChartView](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Scorecard.SparkChartView)` (message)
  * `[SectionHeader](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SectionHeader)` (message)
  * `[SingleViewGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SingleViewGroup)` (message)
  * `[SingleViewGroup.DisplayType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SingleViewGroup.DisplayType)` (enum)
  * `[SortOrder](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SortOrder)` (enum)
  * `[SparkChartType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SparkChartType)` (enum)
  * `[TableDisplayOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TableDisplayOptions)` (message)
  * `[Text](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text)` (message)
  * `[Text.Format](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.Format)` (enum)
  * `[Text.TextStyle](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle)` (message)
  * `[Text.TextStyle.FontSize](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle.FontSize)` (enum)
  * `[Text.TextStyle.HorizontalAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle.HorizontalAlignment)` (enum)
  * `[Text.TextStyle.PaddingSize](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle.PaddingSize)` (enum)
  * `[Text.TextStyle.PointerLocation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle.PointerLocation)` (enum)
  * `[Text.TextStyle.VerticalAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle.VerticalAlignment)` (enum)
  * `[Threshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Threshold)` (message)
  * `[Threshold.Color](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Threshold.Color)` (enum)
  * `[Threshold.Direction](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Threshold.Direction)` (enum)
  * `[Threshold.TargetAxis](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Threshold.TargetAxis)` (enum)
  * `[TimeSeriesFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesFilter)` (message)
  * `[TimeSeriesFilterRatio](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesFilterRatio)` (message)
  * `[TimeSeriesFilterRatio.RatioPart](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart)` (message)
  * `[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesQuery)` (message)
  * `[TimeSeriesTable](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesTable)` (message)
  * `[TimeSeriesTable.ColumnSettings](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesTable.ColumnSettings)` (message)
  * `[TimeSeriesTable.ColumnSettings.CellAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesTable.ColumnSettings.CellAlignment)` (enum)
  * `[TimeSeriesTable.MetricVisualization](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesTable.MetricVisualization)` (enum)
  * `[TimeSeriesTable.TableDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesTable.TableDataSet)` (message)
  * `[TraceQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TraceQuery)` (message)
  * `[TraceQuery.SpanDataValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TraceQuery.SpanDataValue)` (enum)
  * `[TraceQuery.SpanFilters](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TraceQuery.SpanFilters)` (message)
  * `[TraceQuery.SpanFilters.SpanAttributeFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TraceQuery.SpanFilters.SpanAttributeFilter)` (message)
  * `[Treemap](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Treemap)` (message)
  * `[Treemap.TreemapDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Treemap.TreemapDataSet)` (message)
  * `[UpdateDashboardRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.UpdateDashboardRequest)` (message)
  * `[Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget)` (message)
  * `[Widget.TemplateVariableCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget.TemplateVariableCondition)` (message)
  * `[Widget.TemplateVariableCondition.Comparator](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget.TemplateVariableCondition.Comparator)` (enum)
  * `[Widget.TimeRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget.TimeRange)` (message)
  * `[Widget.VisibilityCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget.VisibilityCondition)` (message)
  * `[XyChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart)` (message)
  * `[XyChart.Axis](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.Axis)` (message)
  * `[XyChart.Axis.Scale](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.Axis.Scale)` (enum)
  * `[XyChart.DataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.DataSet)` (message)
  * `[XyChart.DataSet.PlotType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.DataSet.PlotType)` (enum)
  * `[XyChart.DataSet.TargetAxis](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.DataSet.TargetAxis)` (enum)



## DashboardsService

Manages Stackdriver dashboards. A dashboard is an arrangement of data display widgets in a specific layout.

CreateDashboard  
---  
` rpc CreateDashboard(`[CreateDashboardRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.CreateDashboardRequest)`) returns (`[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Dashboard)`) ` Creates a new custom dashboard. For examples on how you can use this API to create dashboards, see [Managing dashboards by API](https://cloud.google.com/monitoring/dashboards/api-dashboard). This method requires the `monitoring.dashboards.create` permission on the specified project. For more information about permissions, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteDashboard  
---  
` rpc DeleteDashboard(`[DeleteDashboardRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DeleteDashboardRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes an existing custom dashboard.This method requires the `monitoring.dashboards.delete` permission on the specified dashboard. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetDashboard  
---  
` rpc GetDashboard(`[GetDashboardRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.GetDashboardRequest)`) returns (`[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Dashboard)`) ` Fetches a specific dashboard.This method requires the `monitoring.dashboards.get` permission on the specified dashboard. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListDashboards  
---  
` rpc ListDashboards(`[ListDashboardsRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ListDashboardsRequest)`) returns (`[ListDashboardsResponse](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ListDashboardsResponse)`) ` Lists the existing dashboards.This method requires the `monitoring.dashboards.list` permission on the specified project. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.read`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateDashboard  
---  
` rpc UpdateDashboard(`[UpdateDashboardRequest](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.UpdateDashboardRequest)`) returns (`[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Dashboard)`) ` Replaces an existing custom dashboard with a new definition.This method requires the `monitoring.dashboards.update` permission on the specified dashboard. For more information, see [Cloud Identity and Access Management](https://cloud.google.com/iam).

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/monitoring`
  * ` https://www.googleapis.com/auth/monitoring.write`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## Aggregation

Describes how to combine multiple time series to provide a different view of the data. Aggregation of time series is done in two steps. First, each time series in the set is _aligned_ to the same time interval boundaries, then the set of time series is optionally _reduced_ in number.

Alignment consists of applying the `per_series_aligner` operation to each time series after its data has been divided into regular `alignment_period` time intervals. This process takes _all_ of the data points in an alignment period, applies a mathematical transformation such as averaging, minimum, maximum, delta, etc., and converts them into a single data point per period.

Reduction is when the aligned and transformed time series can optionally be combined, reducing the number of time series through similar mathematical transformations. Reduction involves applying a `cross_series_reducer` to all the time series, optionally sorting the time series into subsets with `group_by_fields`, and applying the reducer to each subset.

The raw time series data can contain a huge amount of information from multiple sources. Alignment and reduction transforms this mass of data into a more manageable and representative collection of data, for example "the 95% latency across the average of all tasks in a cluster". This representative data can be more easily graphed and comprehended, and the individual time series data is still available for later drilldown. For more details, see [Filtering and aggregation](https://cloud.google.com/monitoring/api/v3/aggregation).

Fields  
---  
`alignment_period` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The `alignment_period` specifies a time interval, in seconds, that is used to divide the data in all the `[time series](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.v3#google.monitoring.v3.TimeSeries)` into consistent blocks of time. This will be done before the per-series aligner can be applied to the data.The value must be at least 60 seconds. If a per-series aligner other than `ALIGN_NONE` is specified, this field is required or an error is returned. If no per-series aligner is specified, or the aligner `ALIGN_NONE` is specified, then this field is ignored.The maximum value of the `alignment_period` is 2 years, or 104 weeks.  
`per_series_aligner` |  `[Aligner](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Aggregation.Aligner)` An `Aligner` describes how to bring the data points in a single time series into temporal alignment. Except for `ALIGN_NONE`, all alignments cause all the data points in an `alignment_period` to be mathematically grouped together, resulting in a single data point for each `alignment_period` with end timestamp at the end of the period.Not all alignment operations may be applied to all time series. The valid choices depend on the `metric_kind` and `value_type` of the original time series. Alignment can change the `metric_kind` or the `value_type` of the time series.Time series data must be aligned in order to perform cross-time series reduction. If `cross_series_reducer` is specified, then `per_series_aligner` must be specified and not equal to `ALIGN_NONE` and `alignment_period` must be specified; otherwise, an error is returned.  
`cross_series_reducer` |  `[Reducer](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Aggregation.Reducer)` The reduction operation to be used to combine time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.Not all reducer operations can be applied to all time series. The valid choices depend on the `metric_kind` and the `value_type` of the original time series. Reduction can yield a time series with a different `metric_kind` or `value_type` than the input time series.Time series data must first be aligned (see `per_series_aligner`) in order to perform cross-time series reduction. If `cross_series_reducer` is specified, then `per_series_aligner` must be specified, and must not be `ALIGN_NONE`. An `alignment_period` must also be specified; otherwise, an error is returned.  
`group_by_fields[]` |  `string` The set of fields to preserve when `cross_series_reducer` is specified. The `group_by_fields` determine how the time series are partitioned into subsets prior to applying the aggregation operation. Each subset contains time series that have the same value for each of the grouping fields. Each individual time series is a member of exactly one subset. The `cross_series_reducer` is applied to each subset of time series. It is not possible to reduce across different resource types, so this field implicitly contains `resource.type`. Fields not specified in `group_by_fields` are aggregated away. If `group_by_fields` is not specified and all the time series have the same resource type, then the time series are aggregated into a single output time series. If `cross_series_reducer` is not defined, this field is ignored.  
  
## Aligner

The `Aligner` specifies the operation that will be applied to the data points in each alignment period in a time series. Except for `ALIGN_NONE`, which specifies that no operation be applied, each alignment operation replaces the set of data values in each alignment period with a single value: the result of applying the operation to the data values. An aligned time series has a single data value at the end of each `alignment_period`.

An alignment operation can change the data type of the values, too. For example, if you apply a counting operation to boolean values, the data `value_type` in the original time series is `BOOLEAN`, but the `value_type` in the aligned result is `INT64`.

Enums  
---  
`ALIGN_NONE` | No alignment. Raw data is returned. Not valid if cross-series reduction is requested. The `value_type` of the result is the same as the `value_type` of the input.  
`ALIGN_DELTA` | Align and convert to `[DELTA](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind.ENUM_VALUES.google.api.MetricDescriptor.MetricKind.DELTA)`. The output is `delta = y1 - y0`.This alignment is valid for `[CUMULATIVE](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind.ENUM_VALUES.google.api.MetricDescriptor.MetricKind.CUMULATIVE)` and `DELTA` metrics. If the selected alignment period results in periods with no data, then the aligned value for such a period is created by interpolation. The `value_type` of the aligned result is the same as the `value_type` of the input.  
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
  
## Reducer

A Reducer operation describes how to aggregate data points from multiple time series into a single time series, where the value of each data point in the resulting series is a function of all the already aligned values in the input time series.

Enums  
---  
`REDUCE_NONE` | No cross-time series reduction. The output of the `Aligner` is returned.  
`REDUCE_MEAN` | Reduce by computing the mean value across time series for each alignment period. This reducer is valid for `[DELTA](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind.ENUM_VALUES.google.api.MetricDescriptor.MetricKind.DELTA)` and `[GAUGE](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.MetricKind.ENUM_VALUES.google.api.MetricDescriptor.MetricKind.GAUGE)` metrics with numeric or distribution values. The `value_type` of the output is `[DOUBLE](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MetricDescriptor.ValueType.ENUM_VALUES.google.api.MetricDescriptor.ValueType.DOUBLE)`.  
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
  
## AggregationFunction

Preview: An identifier for an aggregation function. Aggregation functions are SQL functions that group or transform data from multiple points to a single point. This is a preview feature and may be subject to change before final release.

Fields  
---  
`type` |  `string` Required. The type of aggregation function, must be one of the following:

  * "none" - no function.
  * "percentile" - APPROX_QUANTILES() - 1 parameter numeric value
  * "average" - AVG()
  * "count" - COUNT()
  * "count-distinct" - COUNT(DISTINCT)
  * "count-distinct-approx" - APPROX_COUNT_DISTINCT()
  * "max" - MAX()
  * "min" - MIN()
  * "sum" - SUM()

  
`parameters[]` |  `[Parameter](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.AggregationFunction.Parameter)` Optional. Parameters applied to the aggregation function. Only used for functions that require them.  
  
## Parameter

Preview: Parameter value applied to the aggregation function. This is a preview feature and may be subject to change before final release.

Fields  
---  
Union field `value`. Parameter value. `value` can be only one of the following:  
`int_value` |  `int64` An integer parameter value.  
`double_value` |  `double` A floating-point parameter value.  
  
## AlertChart

A chart that displays alert policy data.

Fields  
---  
`name` |  `string` Required. The resource name of the alert policy. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/alertPolicies/[ALERT_POLICY_ID]
      
  
## Breakdown

Preview: A breakdown is an aggregation applied to the measures over a specified column. A breakdown can result in multiple series across a category for the provided measure. This is a preview feature and may be subject to change before final release.

Fields  
---  
`column` |  `string` Required. The name of the column in the dataset containing the breakdown values.  
`limit` |  `int32` Required. A limit to the number of breakdowns. If set to zero then all possible breakdowns are applied. The list of breakdowns is dependent on the value of the `sort_order` field.  
`aggregation_function` |  `[AggregationFunction](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.AggregationFunction)` Required. The Aggregation function is applied across all data in each breakdown created.  
`sort_order` |  `[SortOrder](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SortOrder)` Required. The sort order is applied to the values of the breakdown column.  
  
## ChartOptions

Options to control visual rendering of a chart.

Fields  
---  
`mode` |  `[Mode](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ChartOptions.Mode)` The chart mode.  
`display_horizontal` |  `bool` Preview: Configures whether the charted values are shown on the horizontal or vertical axis. By default, values are represented the vertical axis. This is a preview feature and may be subject to change before final release.  
  
## Mode

Chart mode options.

Enums  
---  
`MODE_UNSPECIFIED` | Mode is unspecified. The view will default to `COLOR`.  
`COLOR` | The chart distinguishes data series using different color. Line colors may get reused when there are many lines in the chart.  
`X_RAY` | The chart uses the Stackdriver x-ray mode, in which each data set is plotted using the same semi-transparent color.  
`STATS` | The chart displays statistics such as average, median, 95th percentile, and more.  
  
## CollapsibleGroup

A widget that groups the other widgets. All widgets that are within the area spanned by the grouping widget are considered member widgets.

Fields  
---  
`collapsed` |  `bool` The collapsed state of the widget on first page load.  
  
## ColumnLayout

A simplified layout that divides the available space into vertical columns and arranges a set of widgets vertically in each column.

Fields  
---  
`columns[]` |  `[Column](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ColumnLayout.Column)` The columns of content to display.  
  
## Column

Defines the layout properties and content for a column.

Fields  
---  
`weight` |  `int64` The relative weight of this column. The column weight is used to adjust the width of columns on the screen (relative to peers). Greater the weight, greater the width of the column on the screen. If omitted, a value of 1 is used while rendering.  
`widgets[]` |  `[Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget)` The display widgets arranged vertically in this column.  
  
## ColumnSortingOptions

Data structure to storing column's sort strategy

Fields  
---  
`column` |  `string` Optional. Column name to sort data by  
`direction` |  `[SortOrder](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SortOrder)` Optional. A sorting direction that determines ascending or descending order. This is a legacy field kept for backwards compatibility with table.  
  
## CreateDashboardRequest

The `CreateDashboard` request.

Fields  
---  
`parent` |  `string` Required. The project on which to execute the request. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

The `[PROJECT_ID_OR_NUMBER]` must match the dashboard resource name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `monitoring.dashboards.create`

  
`dashboard` |  `[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Dashboard)` Required. The initial dashboard specification.  
`validate_only` |  `bool` If set, validate the request and preview the review, but do not actually save it.  
  
## Dashboard

A Google Stackdriver dashboard. Dashboards define the content and layout of pages in the Stackdriver web application.

Fields  
---  
`name` |  `string` Identifier. The resource name of the dashboard.  
`display_name` |  `string` Required. The mutable, human-readable name.  
`etag` |  `string` `etag` is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other. An `etag` is returned in the response to `GetDashboard`, and users are expected to put that etag in the request to `UpdateDashboard` to ensure that their change will be applied to the same version of the Dashboard configuration. The field should not be passed during dashboard creation.  
`dashboard_filters[]` |  `[DashboardFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardFilter)` Filters to reduce the amount of data charted based on the filter criteria.  
`labels` |  `map<string, string>` Labels applied to the dashboard  
`annotations` |  `[DashboardAnnotations](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardAnnotations)` Configuration for event annotations to display on this dashboard.  
Union field `layout`. A dashboard's root container element that defines the layout style. `layout` can be only one of the following:  
`grid_layout` |  `[GridLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.GridLayout)` Content is arranged with a basic layout that re-flows a simple list of informational elements like widgets or tiles.  
`mosaic_layout` |  `[MosaicLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.MosaicLayout)` The content is arranged as a grid of tiles, with each content widget occupying one or more grid blocks.  
`row_layout` |  `[RowLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.RowLayout)` The content is divided into equally spaced rows and the widgets are arranged horizontally.  
`column_layout` |  `[ColumnLayout](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ColumnLayout)` The content is divided into equally spaced columns and the widgets are arranged vertically.  
  
## DashboardAnnotations

Dashboard-level configuration for annotations

Fields  
---  
`default_resource_names[]` |  `string` Dashboard level defaults for names of logging resources to search for events. Currently only projects are supported. Each individual `EventAnnotation` may have its own overrides. If both this field and the per annotation field is empty, then the scoping project is used. Limit: 50 projects. For example:
    
    
    “projects/some-project-id”
      
  
`event_annotations[]` |  `[EventAnnotation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.EventAnnotation)` List of annotation configurations for this dashboard. Each entry specifies one event type.  
  
## DashboardFilter

A filter to reduce the amount of data charted in relevant widgets.

Fields  
---  
`label_key` |  `string` Optional. The key for the label. This must be omitted if the filter_type is VALUE_ONLY but is required otherwise.  
`template_variable` |  `string` The placeholder text that can be referenced in a filter string or MQL query. If omitted, the dashboard filter will be applied to all relevant widgets in the dashboard.  
`value_type` |  `[ValueType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardFilter.ValueType)` The type of the filter value. If value_type is not provided, it will be inferred from the default_value. If neither value_type nor default_value is provided, value_type will be set to STRING by default.  
`filter_type` |  `[FilterType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardFilter.FilterType)` The specified filter type  
Union field `default_value`. The default value used in the filter comparison `default_value` can be only one of the following:  
`string_value` |  `string` A variable-length string value. If this field is set, value_type must be set to STRING or VALUE_TYPE_UNSPECIFIED  
`string_array_value` |  `[StringArray](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardFilter.StringArray)` An array of variable-length string values. If this field is set, value_type must be set to STRING_ARRAY or VALUE_TYPE_UNSPECIFIED  
Union field `value_source`. A definition of the set of valid values for the filter. This is optional but recommended for VALUE_ONLY filters. For other filter types, the set of valid values will be inferred from the charted data. `value_source` can be only one of the following:  
`time_series_query` |  `[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesQuery)` A query to run to fetch possible values for the filter. Only OpsAnalyticsQueries are supported  
`string_array` |  `[StringArray](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.DashboardFilter.StringArray)` A list of possible string values for the filter  
  
## FilterType

The type for the dashboard filter

Enums  
---  
`FILTER_TYPE_UNSPECIFIED` | Filter type is unspecified. This is not valid in a well-formed request.  
`RESOURCE_LABEL` | Filter on a resource label value  
`METRIC_LABEL` | Filter on a metrics label value  
`USER_METADATA_LABEL` | Filter on a user metadata label value  
`SYSTEM_METADATA_LABEL` | Filter on a system metadata label value  
`GROUP` | Filter on a group id  
`VALUE_ONLY` | Filter that only contains a value. The label_key field must be unset for filters of this type.  
  
## StringArray

An array of strings

Fields  
---  
`values[]` |  `string` The values of the array  
  
## ValueType

The type of the filter value

Enums  
---  
`VALUE_TYPE_UNSPECIFIED` | Value type is unspecified  
`STRING` | String type  
`STRING_ARRAY` | String array type  
  
## DeleteDashboardRequest

The `DeleteDashboard` request.

Fields  
---  
`name` |  `string` Required. The resource name of the Dashboard. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID]
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.dashboards.delete`

  
  
## Dimension

A chart dimension. Dimensions are a structured label, class, or category for a set of measurements in your data.

Fields  
---  
`column` |  `string` Required. For widgets that use SQL queries, set the value to the name of the column in the results table whose data is charted. For a histogram that uses a time series query, set the value of this field to `metric_value`.  
`column_type` |  `string` Optional. The type of the dimension column. This is relevant only if one of the bin_size fields is set. If it is empty, the type TIMESTAMP or INT64 will be assumed based on which bin_size field is set. If populated, this should be set to one of the following types: DATE, TIME, DATETIME, TIMESTAMP, BIGNUMERIC, INT64, NUMERIC, FLOAT64.  
`max_bin_count` |  `int32` For widgets that use SQL queries, the limit to the number of bins to generate. When 0 is specified, the maximum count is not enforced. For a histogram that uses a time series query, the exact number of bins to generate. If not specified or the value is 0, then the histogram determines the number of bins to use.  
`sort_order` |  `[SortOrder](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SortOrder)` The sort order applied to the sort column.  
`sort_column` |  `string` The column name to sort on for binning. This column can be the same column as this dimension or any other column used as a measure in the results. If `sort_order` is set to `NONE`, then this value is not used.  
`x_min` |  `double` The minimum value for the x-axis.  
`x_max` |  `double` The maximum value for the x-axis.  
Union field `bin_size`. The values of `bin_size` are used to configure the grouping of points for the dimension specified by the `column` field. `bin_size` can be only one of the following:  
`time_bin_size` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` `time_bin_size` is used when the data type of the specified dimension is a time type and the bin size is determined by a time duration. If `column_type` is `DATE`, this must be a whole value multiple of 1 day. If `column_type` is `TIME`, this must be less than or equal to 24 hours.  
`numeric_bin_size` |  `int32` `numeric_bin_size` is used when the column type used for a dimension is numeric or string. If the `column` field is set to `metric_value`, then `numericBinSize` overrides `maxBinCount`.  
`float_bin_size` |  `double` Optional. `float_bin_size` is used when the column type used for a dimension is a floating point numeric column.  
  
## ErrorReportingPanel

A widget that displays a list of error groups.

Fields  
---  
`project_names[]` |  `string` The resource name of the Google Cloud Platform project. Written as `projects/{projectID}` or `projects/{projectNumber}`, where `{projectID}` and `{projectNumber}` can be found in the [Google Cloud console](https://support.google.com/cloud/answer/6158840).Examples: `projects/my-project-123`, `projects/5551234`.  
`services[]` |  `string` An identifier of the service, such as the name of the executable, job, or Google App Engine service name. This field is expected to have a low number of values that are relatively stable over time, as opposed to `version`, which can be changed whenever new code is deployed.Contains the service name for error reports extracted from Google App Engine logs or `default` if the App Engine default service is used.  
`versions[]` |  `string` Represents the source code version that the developer provided, which could represent a version label or a Git SHA-1 hash, for example. For App Engine standard environment, the version is set to the version of the app.  
  
## EventAnnotation

Annotation configuration for one event type on a dashboard

Fields  
---  
`display_name` |  `string` Solely for UI display. Should not be used programmatically.  
`event_type` |  `[EventType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.EventAnnotation.EventType)` The type of event to display.  
`filter` |  `string` string filtering the events - event dependant. Example values:
    
    
    "resource.labels.pod_name = 'pod-1'"
    "protoPayload.authenticationInfo.principalEmail='user@example.com'"
      
  
`enabled` |  `bool` Whether or not to show the events on the dashboard by default  
`resource_names[]` |  `string` Per annotation level override for the names of logging resources to search for events. Currently only projects are supported. If both this field and the per annotation field is empty, it will default to the host project. Limit: 50 projects. For example:
    
    
    “projects/another-project-id”
      
  
## EventType

Predefined event types.

Enums  
---  
`EVENT_TYPE_UNSPECIFIED` | No event type specified.  
`GKE_WORKLOAD_DEPLOYMENT` | Patch/update of GKE workload.  
`GKE_POD_CRASH` | Crash events for a GKE Pod.  
`GKE_POD_UNSCHEDULABLE` | Scheduling failures for GKE Pods.  
`GKE_CONTAINER_CREATION_FAILED` | Failure to create a GKE container.  
`GKE_CLUSTER_CREATE_DELETE` | Create/delete of a GKE cluster.  
`GKE_CLUSTER_UPDATE` | Update of a GKE cluster.  
`GKE_NODE_POOL_UPDATE` | Update of a GKE node pool.  
`GKE_CLUSTER_AUTOSCALER` | GKE cluster autoscaler event.  
`GKE_POD_AUTOSCALER` | GKE pod autoscaler event.  
`VM_TERMINATION` | Termination of a virtual machine.  
`VM_GUEST_OS_ERROR` | Guest OS error on a virtual machine.  
`VM_START_FAILED` | Start failure on a virtual machine.  
`MIG_UPDATE` | Update of a managed instance group.  
`MIG_AUTOSCALER` | Autoscaler event for a managed instance group.  
`CLOUD_RUN_DEPLOYMENT` | New deployment of a Cloud Run service.  
`CLOUD_SQL_FAILOVER` | Failover of a Cloud SQL instance.  
`CLOUD_SQL_START_STOP` | Start/stop of a Cloud SQL instance.  
`CLOUD_SQL_STORAGE` | Storage event for a Cloud SQL instance.  
`UPTIME_CHECK_FAILURE` | Failure of a Cloud Monitoring uptime check.  
`CLOUD_ALERTING_ALERT` | Alerts from Cloud Alerting  
`SERVICE_HEALTH_INCIDENT` | Incidents from Service Health  
`SAP_BACKINT` | Agent for SAP Backint related events.  
`SAP_AVAILABILITY` | Agent for SAP availability related events.  
`SAP_OPERATIONS` | Agent for SAP operations related events.  
`INTERCONNECT_MAINTENANCE_STARTED` | Interconnect maintenance started event.  
`INTERCONNECT_MAINTENANCE_COMPLETED` | Interconnect maintenance completed event.  
`VPN_TRAFFIC_SELECTOR_NARROWING` | VPN traffic selector narrowing event.  
`VPN_MAINTENANCE` | VPN maintenance event.  
  
## FilterControl

A widget that displays an input field to change the value of a template variable.

Fields  
---  
`template_variable` |  `string` Name of the template variable the widget affects.  
  
## GetDashboardRequest

The `GetDashboard` request.

Fields  
---  
`name` |  `string` Required. The resource name of the Dashboard. The format is one of:

  * `dashboards/[DASHBOARD_ID]` (for system dashboards)
  * `projects/[PROJECT_ID_OR_NUMBER]/dashboards/[DASHBOARD_ID]` (for custom dashboards).

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `monitoring.dashboards.get`

  
  
## GridLayout

A basic layout divides the available space into vertical columns of equal width and arranges a list of widgets using a row-first strategy.

Fields  
---  
`columns` |  `int64` The number of columns into which the view's width is divided. If omitted or set to zero, a system default will be used while rendering.  
`widgets[]` |  `[Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget)` The informational elements that are arranged into the columns row-first.  
  
## IncidentList

A widget that displays a list of incidents

Fields  
---  
`monitored_resources[]` |  `[MonitoredResource](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.api#google.api.MonitoredResource)` Optional. The monitored resource for which incidents are listed. The resource doesn't need to be fully specified. That is, you can specify the resource type but not the values of the resource labels. The resource type and labels are used for filtering.  
`policy_names[]` |  `string` Optional. A list of alert policy names to filter the incident list by. Don't include the project ID prefix in the policy name. For example, use `alertPolicies/utilization`.  
  
## ListDashboardsRequest

The `ListDashboards` request.

Fields  
---  
`parent` |  `string` Required. The scope of the dashboards to list. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]
    

Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `monitoring.dashboards.list`

  
`page_size` |  `int32` A positive number that is the maximum number of results to return. If unspecified, a default of 1000 is used.  
`page_token` |  `string` Optional. If this field is not empty then it must contain the `nextPageToken` value returned by a previous call to this method. Using this field causes the method to return additional results from the previous method call.  
  
## ListDashboardsResponse

The `ListDashboards` request.

Fields  
---  
`dashboards[]` |  `[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Dashboard)` The list of requested dashboards.  
`next_page_token` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `page_token` in the next call to this method.  
  
## LogsPanel

A widget that displays a stream of log.

Fields  
---  
`filter` |  `string` A filter that chooses which log entries to return. See [Advanced Logs Queries](https://cloud.google.com/logging/docs/view/advanced-queries). Only log entries that match the filter are returned. An empty filter matches all log entries.  
`resource_names[]` |  `string` The names of logging resources to collect logs for. Currently projects and storage views are supported. If empty, the widget will default to the host project.  
  
## Measure

A chart measure. Measures represent a measured property in your chart data such as rainfall in inches, number of units sold, revenue gained, etc.

Fields  
---  
`column` |  `string` Required. The column name within in the dataset used for the measure.  
`aggregation_function` |  `[AggregationFunction](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.AggregationFunction)` Required. The aggregation function applied to the input column. This must not be set to `"none"` unless binning is disabled on the dimension. The aggregation function is used to group points on the dimension bins.  
  
## MosaicLayout

A mosaic layout divides the available space into a grid of blocks, and overlays the grid with tiles. Unlike `GridLayout`, tiles may span multiple grid blocks and can be placed at arbitrary locations in the grid.

Fields  
---  
`columns` |  `int32` The number of columns in the mosaic grid. The number of columns must be between 1 and 48, inclusive.  
`tiles[]` |  `[Tile](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.MosaicLayout.Tile)` The tiles to display.  
  
## Tile

A single tile in the mosaic. The placement and size of the tile are configurable.

Fields  
---  
`x_pos` |  `int32` The zero-indexed position of the tile in grid blocks relative to the left edge of the grid. Tiles must be contained within the specified number of columns. `x_pos` cannot be negative.  
`y_pos` |  `int32` The zero-indexed position of the tile in grid blocks relative to the top edge of the grid. `y_pos` cannot be negative.  
`width` |  `int32` The width of the tile, measured in grid blocks. Tiles must have a minimum width of 1.  
`height` |  `int32` The height of the tile, measured in grid blocks. Tiles must have a minimum height of 1.  
`widget` |  `[Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget)` The informational widget contained in the tile. For example an `XyChart`.  
  
## OpsAnalyticsQuery

Preview: A query that produces an aggregated response and supporting data. This is a preview feature and may be subject to change before final release.

Fields  
---  
`sql` |  `string` A SQL query to fetch time series, category series, or numeric series data.  
  
## PickTimeSeriesFilter

Describes a ranking-based time series filter. Each input time series is ranked with an aligner. The filter will allow up to `num_time_series` time series to pass through it, selecting them based on the relative ranking.

For example, if `ranking_method` is `METHOD_MEAN`,`direction` is `BOTTOM`, and `num_time_series` is 3, then the 3 times series with the lowest mean values will pass through the filter.

Fields  
---  
`ranking_method` |  `[Method](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PickTimeSeriesFilter.Method)` `ranking_method` is applied to each time series independently to produce the value which will be used to compare the time series to other time series.  
`num_time_series` |  `int32` How many time series to allow to pass through the filter.  
`direction` |  `[Direction](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PickTimeSeriesFilter.Direction)` How to use the ranking to select time series that pass through the filter.  
`interval` |  `[Interval](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.type#google.type.Interval)` Select the top N streams/time series within this time interval  
  
## Direction

Describes the ranking directions.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Not allowed. You must specify a different `Direction` if you specify a `PickTimeSeriesFilter`.  
`TOP` | Pass the highest `num_time_series` ranking inputs.  
`BOTTOM` | Pass the lowest `num_time_series` ranking inputs.  
  
## Method

The value reducers that can be applied to a `PickTimeSeriesFilter`.

Enums  
---  
`METHOD_UNSPECIFIED` | Not allowed. You must specify a different `Method` if you specify a `PickTimeSeriesFilter`.  
`METHOD_MEAN` | Select the mean of all values.  
`METHOD_MAX` | Select the maximum value.  
`METHOD_MIN` | Select the minimum value.  
`METHOD_SUM` | Compute the sum of all values.  
`METHOD_LATEST` | Select the most recent value.  
  
## PieChart

A widget that displays timeseries data as a pie or a donut.

Fields  
---  
`data_sets[]` |  `[PieChartDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PieChart.PieChartDataSet)` Required. The queries for the chart's data.  
`chart_type` |  `[PieChartType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PieChart.PieChartType)` Required. Indicates the visualization type for the PieChart.  
`show_labels` |  `bool` Optional. Indicates whether or not the pie chart should show slices' labels  
  
## PieChartDataSet

Groups a time series query definition.

Fields  
---  
`time_series_query` |  `[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesQuery)` Required. The query for the PieChart. See, `google.monitoring.dashboard.v1.TimeSeriesQuery`.  
`slice_name_template` |  `string` Optional. A template for the name of the slice. This name will be displayed in the legend and the tooltip of the pie chart. It replaces the auto-generated names for the slices. For example, if the template is set to `${resource.labels.zone}`, the zone's value will be used for the name instead of the default name.  
`min_alignment_period` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes, the `min_alignment_period` should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.  
`dimensions[]` |  `[Dimension](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Dimension)` A dimension is a structured label, class, or category for a set of measurements in your data.  
`measures[]` |  `[Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Measure)` A measure is a measured value of a property in your data. For example, rainfall in inches, number of units sold, revenue gained, etc.  
  
## PieChartType

Types for the pie chart.

Enums  
---  
`PIE_CHART_TYPE_UNSPECIFIED` | The zero value. No type specified. Do not use.  
`PIE` | A Pie type PieChart.  
`DONUT` | Similar to PIE, but the DONUT type PieChart has a hole in the middle.  
  
## RowLayout

A simplified layout that divides the available space into rows and arranges a set of widgets horizontally in each row.

Fields  
---  
`rows[]` |  `[Row](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.RowLayout.Row)` The rows of content to display.  
  
## Row

Defines the layout properties and content for a row.

Fields  
---  
`weight` |  `int64` The relative weight of this row. The row weight is used to adjust the height of rows on the screen (relative to peers). Greater the weight, greater the height of the row on the screen. If omitted, a value of 1 is used while rendering.  
`widgets[]` |  `[Widget](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget)` The display widgets arranged horizontally in this row.  
  
## Scorecard

A widget showing the latest value of a metric, and how this value relates to one or more thresholds.

Fields  
---  
`time_series_query` |  `[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesQuery)` Required. Fields for querying time series data from the Stackdriver metrics API.  
`thresholds[]` |  `[Threshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Threshold)` The thresholds used to determine the state of the scorecard given the time series' current value. For an actual value x, the scorecard is in a danger state if x is less than or equal to a danger threshold that triggers below, or greater than or equal to a danger threshold that triggers above. Similarly, if x is above/below a warning threshold that triggers above/below, then the scorecard is in a warning state - unless x also puts it in a danger state. (Danger trumps warning.)As an example, consider a scorecard with the following four thresholds:
    
    
    {
      value: 90,
      category: 'DANGER',
      trigger: 'ABOVE',
    },
    {
      value: 70,
      category: 'WARNING',
      trigger: 'ABOVE',
    },
    {
      value: 10,
      category: 'DANGER',
      trigger: 'BELOW',
    },
    {
      value: 20,
      category: 'WARNING',
      trigger: 'BELOW',
    }
    

Then: values less than or equal to 10 would put the scorecard in a DANGER state, values greater than 10 but less than or equal to 20 a WARNING state, values strictly between 20 and 70 an OK state, values greater than or equal to 70 but less than 90 a WARNING state, and values greater than or equal to 90 a DANGER state.  
`dimensions[]` |  `[Dimension](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Dimension)` Optional. A dimension is a structured label, class, or category for a set of measurements in your data.  
`measures[]` |  `[Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Measure)` Optional. A measure is a measured value of a property in your data. For example, rainfall in inches, number of units sold, revenue gained, etc.  
`breakdowns[]` |  `[Breakdown](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Breakdown)` Optional. The collection of breakdowns to be applied to the dataset. A breakdown is a way to slice the data. For example, you can break down the data by region.  
Union field `data_view`. Defines the optional additional chart shown on the scorecard. If neither is included - then a default scorecard is shown. `data_view` can be only one of the following:  
`gauge_view` |  `[GaugeView](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Scorecard.GaugeView)` Will cause the scorecard to show a gauge chart.  
`spark_chart_view` |  `[SparkChartView](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Scorecard.SparkChartView)` Will cause the scorecard to show a spark chart.  
`blank_view` |  `[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)` Will cause the `Scorecard` to show only the value, with no indicator to its value relative to its thresholds.  
  
## GaugeView

A gauge chart shows where the current value sits within a pre-defined range. The upper and lower bounds should define the possible range of values for the scorecard's query (inclusive).

Fields  
---  
`lower_bound` |  `double` The lower bound for this gauge chart. The value of the chart should always be greater than or equal to this.  
`upper_bound` |  `double` The upper bound for this gauge chart. The value of the chart should always be less than or equal to this.  
  
## SparkChartView

A sparkChart is a small chart suitable for inclusion in a table-cell or inline in text. This message contains the configuration for a sparkChart to show up on a Scorecard, showing recent trends of the scorecard's timeseries.

Fields  
---  
`spark_chart_type` |  `[SparkChartType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SparkChartType)` Required. The type of sparkchart to show in this chartView.  
`min_alignment_period` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The lower bound on data point frequency in the chart implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes it would not make sense to fetch and align data at one minute intervals. This field is optional and exists only as a hint.For PromQL queries, this field is used to set the minimum interval for the query `step`, controlling data granularity. Larger values can improve performance on long time ranges. See [Querying Basics](https://prometheus.io/docs/prometheus/latest/querying/basics/) and [Range Queries](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries) for more details on the PromQL `step`.  
  
## SectionHeader

A widget that defines a new section header. Sections populate a table of contents and allow easier navigation of long-form content.

Fields  
---  
`subtitle` |  `string` The subtitle of the section  
`divider_below` |  `bool` Whether to insert a divider below the section in the table of contents  
  
## SingleViewGroup

A widget that groups the other widgets by using a dropdown menu. All widgets that are within the area spanned by the grouping widget are considered member widgets.

Fields  
---  
`display_type` |  `[DisplayType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SingleViewGroup.DisplayType)` Optional. Determines how the widget selector will be displayed.  
  
## DisplayType

A type indicating how the wiget selector will be displayed.

Enums  
---  
`DISPLAY_TYPE_UNSPECIFIED` | Display type is not specified, defaults to DROPDOWN.  
`DROPDOWN` | Renders the widget selector as a dropdown.  
`TAB` | Renders the widget selector as a tab list.  
  
## SortOrder

Sort order options.

Enums  
---  
`SORT_ORDER_UNSPECIFIED` | An unspecified sort order. This option is invalid when sorting is required.  
`SORT_ORDER_NONE` | No sorting is applied.  
`SORT_ORDER_ASCENDING` | The lowest-valued entries are selected first.  
`SORT_ORDER_DESCENDING` | The highest-valued entries are selected first.  
  
## SparkChartType

Defines the possible types of spark chart supported by the `Scorecard`.

Enums  
---  
`SPARK_CHART_TYPE_UNSPECIFIED` | Not allowed in well-formed requests.  
`SPARK_LINE` | The sparkline will be rendered as a small line chart.  
`SPARK_BAR` | The sparkbar will be rendered as a small bar chart.  
  
## TableDisplayOptions

Table display options that can be reused.

Fields  
---  
`shown_columns[]  
**(deprecated)**` |  `string` This item is deprecated!Optional. This field is unused and has been replaced by TimeSeriesTable.column_settings  
  
## Text

A widget that displays textual content.

Fields  
---  
`content` |  `string` The text content to be displayed.  
`format` |  `[Format](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.Format)` How the text content is formatted.  
`style` |  `[TextStyle](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle)` How the text is styled  
  
## Format

The format type of the text content.

Enums  
---  
`FORMAT_UNSPECIFIED` | Format is unspecified. Defaults to MARKDOWN.  
`MARKDOWN` | The text contains Markdown formatting.  
`RAW` | The text contains no special formatting.  
  
## TextStyle

Properties that determine how the title and content are styled

Fields  
---  
`background_color` |  `string` The background color as a hex string. "#RRGGBB" or "#RGB"  
`text_color` |  `string` The text color as a hex string. "#RRGGBB" or "#RGB"  
`horizontal_alignment` |  `[HorizontalAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle.HorizontalAlignment)` The horizontal alignment of both the title and content  
`vertical_alignment` |  `[VerticalAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle.VerticalAlignment)` The vertical alignment of both the title and content  
`padding` |  `[PaddingSize](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle.PaddingSize)` The amount of padding around the widget  
`font_size` |  `[FontSize](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle.FontSize)` Font sizes for both the title and content. The title will still be larger relative to the content.  
`pointer_location` |  `[PointerLocation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text.TextStyle.PointerLocation)` The pointer location for this widget (also sometimes called a "tail")  
  
## FontSize

Specifies a font size for the title and content of a text widget

Enums  
---  
`FONT_SIZE_UNSPECIFIED` | No font size specified, will default to FS_LARGE  
`FS_EXTRA_SMALL` | Extra small font size  
`FS_SMALL` | Small font size  
`FS_MEDIUM` | Medium font size  
`FS_LARGE` | Large font size  
`FS_EXTRA_LARGE` | Extra large font size  
  
## HorizontalAlignment

The horizontal alignment of both the title and content on a text widget

Enums  
---  
`HORIZONTAL_ALIGNMENT_UNSPECIFIED` | No horizontal alignment specified, will default to H_LEFT  
`H_LEFT` | Left-align  
`H_CENTER` | Center-align  
`H_RIGHT` | Right-align  
  
## PaddingSize

Specifies padding size around a text widget

Enums  
---  
`PADDING_SIZE_UNSPECIFIED` | No padding size specified, will default to P_EXTRA_SMALL  
`P_EXTRA_SMALL` | Extra small padding  
`P_SMALL` | Small padding  
`P_MEDIUM` | Medium padding  
`P_LARGE` | Large padding  
`P_EXTRA_LARGE` | Extra large padding  
  
## PointerLocation

Specifies where a visual pointer is placed on a text widget (also sometimes called a "tail")

Enums  
---  
`POINTER_LOCATION_UNSPECIFIED` | No visual pointer  
`PL_TOP` | Placed in the middle of the top of the widget  
`PL_RIGHT` | Placed in the middle of the right side of the widget  
`PL_BOTTOM` | Placed in the middle of the bottom of the widget  
`PL_LEFT` | Placed in the middle of the left side of the widget  
`PL_TOP_LEFT` | Placed on the left side of the top of the widget  
`PL_TOP_RIGHT` | Placed on the right side of the top of the widget  
`PL_RIGHT_TOP` | Placed on the top of the right side of the widget  
`PL_RIGHT_BOTTOM` | Placed on the bottom of the right side of the widget  
`PL_BOTTOM_RIGHT` | Placed on the right side of the bottom of the widget  
`PL_BOTTOM_LEFT` | Placed on the left side of the bottom of the widget  
`PL_LEFT_BOTTOM` | Placed on the bottom of the left side of the widget  
`PL_LEFT_TOP` | Placed on the top of the left side of the widget  
  
## VerticalAlignment

The vertical alignment of both the title and content on a text widget

Enums  
---  
`VERTICAL_ALIGNMENT_UNSPECIFIED` | No vertical alignment specified, will default to V_TOP  
`V_TOP` | Top-align  
`V_CENTER` | Center-align  
`V_BOTTOM` | Bottom-align  
  
## Threshold

Defines a threshold for categorizing time series values.

Fields  
---  
`label` |  `string` A label for the threshold.  
`value` |  `double` The value of the threshold. The value should be defined in the native scale of the metric.  
`color` |  `[Color](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Threshold.Color)` The state color for this threshold. Color is not allowed in a XyChart.  
`direction` |  `[Direction](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Threshold.Direction)` The direction for the current threshold. Direction is not allowed in a XyChart.  
`target_axis` |  `[TargetAxis](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Threshold.TargetAxis)` The target axis to use for plotting the threshold. Target axis is not allowed in a Scorecard.  
  
## Color

The color suggests an interpretation to the viewer when actual values cross the threshold. Comments on each color provide UX guidance on how users can be expected to interpret a given state color.

Enums  
---  
`COLOR_UNSPECIFIED` | Color is unspecified. Not allowed in well-formed requests.  
`YELLOW` | Crossing the threshold is "concerning" behavior.  
`RED` | Crossing the threshold is "emergency" behavior.  
  
## Direction

Whether the threshold is considered crossed by an actual value above or below its threshold value.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Not allowed in well-formed requests.  
`ABOVE` | The threshold will be considered crossed if the actual value is above the threshold value.  
`BELOW` | The threshold will be considered crossed if the actual value is below the threshold value.  
  
## TargetAxis

An axis identifier.

Enums  
---  
`TARGET_AXIS_UNSPECIFIED` | The target axis was not specified. Defaults to Y1.  
`Y1` | The y_axis (the right axis of chart).  
`Y2` | The y2_axis (the left axis of chart).  
  
## TimeSeriesFilter

A filter that defines a subset of time series data that is displayed in a widget. Time series data is fetched using the [`ListTimeSeries`](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method.

Fields  
---  
`filter` |  `string` Required. The [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query.  
`aggregation` |  `[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Aggregation)` By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.  
`secondary_aggregation` |  `[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Aggregation)` Apply a second aggregation after `aggregation` is applied.  
Union field `output_filter`. Selects an optional time series filter. `output_filter` can be only one of the following:  
`pick_time_series_filter` |  `[PickTimeSeriesFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PickTimeSeriesFilter)` Ranking based time series filter.  
  
## TimeSeriesFilterRatio

A pair of time series filters that define a ratio computation. The output time series is the pair-wise division of each aligned element from the numerator and denominator time series.

Fields  
---  
`numerator` |  `[RatioPart](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart)` The numerator of the ratio.  
`denominator` |  `[RatioPart](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesFilterRatio.RatioPart)` The denominator of the ratio.  
`secondary_aggregation` |  `[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Aggregation)` Apply a second aggregation after the ratio is computed.  
Union field `output_filter`. Selects an optional filter that is applied to the time series after computing the ratio. `output_filter` can be only one of the following:  
`pick_time_series_filter` |  `[PickTimeSeriesFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PickTimeSeriesFilter)` Ranking based time series filter.  
  
## RatioPart

Describes a query to build the numerator or denominator of a TimeSeriesFilterRatio.

Fields  
---  
`filter` |  `string` Required. The [monitoring filter](https://cloud.google.com/monitoring/api/v3/filters) that identifies the metric types, resources, and projects to query.  
`aggregation` |  `[Aggregation](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Aggregation)` By default, the raw time series data is returned. Use this field to combine multiple time series for different views of the data.  
  
## TimeSeriesQuery

TimeSeriesQuery collects the set of supported methods for querying time series data from the Stackdriver metrics API.

Fields  
---  
`unit_override` |  `string` The unit of data contained in fetched time series. If non-empty, this unit will override any unit that accompanies fetched data. The format is the same as the [`unit`](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors) field in `MetricDescriptor`.  
`output_full_duration` |  `bool` Optional. If set, Cloud Monitoring will treat the full query duration as the alignment period so that there will be only 1 output value.*Note: This could override the configured alignment period except for the cases where a series of data points are expected, like - XyChart - Scorecard's spark chart  
Union field `source`. Parameters needed to obtain data for the chart. `source` can be only one of the following:  
`time_series_filter` |  `[TimeSeriesFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesFilter)` Filter parameters to fetch time series.  
`time_series_filter_ratio` |  `[TimeSeriesFilterRatio](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesFilterRatio)` Parameters to fetch a ratio between two time series filters.  
`time_series_query_language` |  `string` A query used to fetch time series with MQL.  
`prometheus_query` |  `string` A query used to fetch time series with PromQL.  
`ops_analytics_query` |  `[OpsAnalyticsQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.OpsAnalyticsQuery)` Preview: A query used to fetch a time series, category series, or numeric series with SQL. This is a preview feature and may be subject to change before final release.  
`trace_query` |  `[TraceQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TraceQuery)` Optional. Preview: Query for traces. This is a preview feature and may be subject to change before final release.  
  
## TimeSeriesTable

A table that displays time series data.

Fields  
---  
`data_sets[]` |  `[TableDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesTable.TableDataSet)` Required. The data displayed in this table.  
`metric_visualization` |  `[MetricVisualization](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesTable.MetricVisualization)` Optional. Store rendering strategy  
`column_settings[]` |  `[ColumnSettings](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesTable.ColumnSettings)` Optional. The list of the persistent column settings for the table.  
  
## ColumnSettings

The persistent settings for a table's columns.

Fields  
---  
`column` |  `string` Required. The id of the column.  
`visible` |  `bool` Required. Whether the column should be visible on page load.  
`alignment` |  `[CellAlignment](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesTable.ColumnSettings.CellAlignment)` Optional. Whether the column should be left / middle / right aligned  
`display_name` |  `string` Optional. Display name of the column  
`thresholds[]` |  `[Threshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Threshold)` Optional. The thresholds used to determine how the table cell should be rendered given the time series' current value.  
  
## CellAlignment

The horizontal alignment of table cells in that column

Enums  
---  
`CELL_ALIGNMENT_UNSPECIFIED` | No horizontal alignment specified; fall back to the default behavior. Label values are left aligned. Numeric values are right aligned.  
`LEFT` | Left-align  
`CENTER` | Center-align  
`RIGHT` | Right-align  
  
## MetricVisualization

Enum for metric metric_visualization

Enums  
---  
`METRIC_VISUALIZATION_UNSPECIFIED` | Unspecified state  
`NUMBER` | Default text rendering  
`BAR` | Horizontal bar rendering  
  
## TableDataSet

Groups a time series query definition with table options.

Fields  
---  
`time_series_query` |  `[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesQuery)` Required. Fields for querying time series data from the Stackdriver metrics API.  
`table_template` |  `string` Optional. A template string for naming `TimeSeries` in the resulting data set. This should be a string with interpolations of the form `${label_name}`, which will resolve to the label's value i.e. "${resource.labels.project_id}."  
`min_alignment_period` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query For example, if the data is published once every 10 minutes, the `min_alignment_period` should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.  
`table_display_options` |  `[TableDisplayOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TableDisplayOptions)` Optional. Table display options for configuring how the table is rendered.  
  
## TraceQuery

LINT.IfChange Preview: Query for traces. This is a preview feature and may be subject to change before final release.

Fields  
---  
`span_data_value` |  `[SpanDataValue](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TraceQuery.SpanDataValue)` The type of span data value to be displayed on the chart. Required.  
`span_filters` |  `[SpanFilters](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TraceQuery.SpanFilters)` First version of span filtering that we will support. Required.  
`resource_container` |  `string` Optional. The resource name of the project or Trace scope to fetch data from. If empty, the widget will default to the project's default Trace scope. If scope cannot be determined, then we fallback to the current project. Optional.  
  
## SpanDataValue

List of different span data values that is used to determine the data displayed on the chart

Enums  
---  
`SPAN_DATA_VALUE_UNSPECIFIED` | We are required to have an UNSPECIFIED value for enums. This should not be used in practice.  
`SPAN_COUNT` | Span count data value  
`SPAN_DURATION` | Span duration data value  
`SPAN_DURATION_PERCENTILES` | Span duration percentiles data value  
  
## SpanFilters

First version of span filtering that is supported by the Trace component.

Fields  
---  
`services[]` |  `string` Optional. Filtering for spans containing one of the services in the list. Multiple values will be OR'd together.  
`display_names[]` |  `string` Optional. Filtering for spans containing one of the span display names in the list. Multiple values will be OR'd together.  
`status[]` |  `string` Optional. Filtering for spans containing one of the statuses in the list. Multiple values will be OR'd together.  
`kinds[]` |  `string` Optional. Filtering for spans containing one of the kinds in the list. Multiple values will be OR'd together.  
`min_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Filtering for spans with a minimum duration.  
`max_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Filtering for spans with a maximum duration.  
`attributes[]` |  `[SpanAttributeFilter](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TraceQuery.SpanFilters.SpanAttributeFilter)` Optional. List of span attribute filters. Each SpanAttributeFilter key must be unique. Multiple attribute filters will be AND'd together.  
`is_root_span` |  `bool` Optional. Filters for root spans only if set to true. A root span is a span without a defined parent span ID.  
`application_ids[]` |  `string` Optional. Filtering for spans containing one of the Apphub Application IDs in the list. Multiple values will be OR'd together.  
`apphub_services[]` |  `string` Optional. Filtering for spans containing one of the Apphub service IDs in the list. Multiple values will be OR'd together. Example: ["service-id1", "service-id2"]  
`apphub_workloads[]` |  `string` Optional. Filtering for spans containing one of the Apphub workload IDs in the list. Multiple values will be OR'd together. Example: ["workload-id1", "workload-id2"]  
  
## SpanAttributeFilter

Span attribute key and list of values to be used for filtering.

Fields  
---  
`key` |  `string` Key of the attribute  
`value[]` |  `string` List of attribute values for given key. Multiple values will be OR'd together.  
  
## Treemap

A widget that displays hierarchical data as a treemap.

Fields  
---  
`data_sets[]` |  `[TreemapDataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Treemap.TreemapDataSet)` Required. The collection of datasets used to construct and populate the treemap. For the rendered treemap rectangles:

  * Color is determined by the aggregated value for each grouping.
  * Size is proportional to the count of time series aggregated within that rectangle's segment.

  
`treemap_hierarchy[]` |  `string` Required. Ordered labels representing the hierarchical treemap structure.  
  
## TreemapDataSet

The data represented by the treemap. Needs to include the data itself, plus rules on how to organize it hierarchically.

Fields  
---  
`time_series_query` |  `[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesQuery)` Required. The query that fetches the relevant data. See `google.monitoring.dashboard.v1.TimeSeriesQuery`  
`measures[]` |  `[Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Measure)` Optional. A collection of measures. A measure is a measured value of a property in your data. For example, rainfall in inches, number of units sold, revenue gained, etc.  
`breakdowns[]` |  `[Breakdown](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Breakdown)` Optional. The collection of breakdowns to be applied to the dataset. A breakdown is a way to slice the data. For example, you can break down the data by region.  
  
## UpdateDashboardRequest

The `UpdateDashboard` request.

Fields  
---  
`dashboard` |  `[Dashboard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Dashboard)` Required. The dashboard that will replace the existing dashboard. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `dashboard`:

  * `monitoring.dashboards.update`

  
`validate_only` |  `bool` If set, validate the request and preview the review, but do not actually save it.  
  
## Widget

Widget contains a single dashboard component and configuration of how to present the component in the dashboard.

Fields  
---  
`title` |  `string` Optional. The title of the widget.  
`id` |  `string` Optional. The widget id. Ids may be made up of alphanumerics, dashes and underscores. Widget ids are optional.  
`visibility_condition` |  `[VisibilityCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget.VisibilityCondition)` Optional. If set, this widget is rendered only when the condition is evaluated to true.  
`time_range` |  `[TimeRange](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget.TimeRange)` Optional. Represents a time range for the widget. When set, this time range will override the dashboard time range. Supported for line, stacked area and stacked bar widgets only.  
Union field `content`. Content defines the component used to populate the widget. `content` can be only one of the following:  
`xy_chart` |  `[XyChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart)` A chart of time series data.  
`scorecard` |  `[Scorecard](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Scorecard)` A scorecard summarizing time series data.  
`text` |  `[Text](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Text)` A raw string or markdown displaying textual content.  
`blank` |  `[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)` A blank space.  
`alert_chart` |  `[AlertChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.AlertChart)` A chart of alert policy data.  
`time_series_table` |  `[TimeSeriesTable](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesTable)` A widget that displays time series data in a tabular format.  
`collapsible_group` |  `[CollapsibleGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.CollapsibleGroup)` A widget that groups the other widgets. All widgets that are within the area spanned by the grouping widget are considered member widgets.  
`logs_panel` |  `[LogsPanel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.LogsPanel)` A widget that shows a stream of logs.  
`incident_list` |  `[IncidentList](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.IncidentList)` A widget that shows list of incidents.  
`pie_chart` |  `[PieChart](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.PieChart)` A widget that displays timeseries data as a pie chart.  
`treemap` |  `[Treemap](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Treemap)` A widget that displays data as a treemap.  
`error_reporting_panel` |  `[ErrorReportingPanel](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ErrorReportingPanel)` A widget that displays a list of error groups.  
`section_header` |  `[SectionHeader](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SectionHeader)` A widget that defines a section header for easier navigation of the dashboard.  
`single_view_group` |  `[SingleViewGroup](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.SingleViewGroup)` A widget that groups the other widgets by using a dropdown menu.  
`filter_control` |  `[FilterControl](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.FilterControl)` A widget that displays an input field to change the value of a template variable.  
  
## TemplateVariableCondition

A condition whose evaluation is based on the value of a template variable.

Fields  
---  
`template_variable` |  `string` The template variable whose value is evaluated.  
`template_variable_value` |  `string` The value to compare the template variable to. For example, if the comparator is REGEX_FULL_MATCH, this field should contain a regex.  
`comparator` |  `[Comparator](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget.TemplateVariableCondition.Comparator)` Comparator to use to evaluate whether the value of the template variable matches the template_variable_value. For example, if the comparator is REGEX_FULL_MATCH, template_variable_value would contain a regex that is matched against the value of the template variable.  
  
## Comparator

Comparator options to evaluate when the template variable value matches.

Enums  
---  
`COMPARATOR_UNSPECIFIED` | No comparator specified. Behavior defaults to REGEX_FULL_MATCH.  
`REGEX_FULL_MATCH` | Condition with this comparator evaluates to true when the value of the template variables matches the specified regex.  
  
## TimeRange

Represents a time range.

Fields  
---  
Union field `time_interval`. Specifies the type of time range interval. `time_interval` can be only one of the following:  
`absolute_window` |  `[Interval](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.type#google.type.Interval)` Optional. Represents a time range with absolute start and end times. The start time is inclusive, and the end time is exclusive.  
`relative_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. Specifies the duration used to shift the data relative to current time as the end time. The duration must be positive.  
  
## VisibilityCondition

Condition that determines whether the widget should be displayed.

Fields  
---  
`template_variable_condition` |  `[TemplateVariableCondition](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Widget.TemplateVariableCondition)` A condition whose evaluation is based on the value of a template variable.  
  
## XyChart

A chart that displays data on a 2D (X and Y axes) plane.

Fields  
---  
`data_sets[]` |  `[DataSet](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.DataSet)` Required. The data displayed in this chart.  
`timeshift_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` The duration used to display a comparison chart. A comparison chart simultaneously shows values from two similar-length time periods (e.g., week-over-week metrics). The duration must be positive, and it can only be applied to charts with data sets of LINE plot type.  
`thresholds[]` |  `[Threshold](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Threshold)` Threshold lines drawn horizontally across the chart.  
`x_axis` |  `[Axis](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.Axis)` The properties applied to the x-axis.  
`y_axis` |  `[Axis](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.Axis)` The properties applied to the y-axis.  
`y2_axis` |  `[Axis](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.Axis)` The properties applied to the y2-axis.  
`chart_options` |  `[ChartOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ChartOptions)` Display options for the chart.  
  
## Axis

A chart axis.

Fields  
---  
`label` |  `string` The label of the axis.  
`scale` |  `[Scale](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.Axis.Scale)` The axis scale. By default, a linear scale is used.  
  
## Scale

Types of scales used in axes.

Enums  
---  
`SCALE_UNSPECIFIED` | Scale is unspecified. The view will default to `LINEAR`.  
`LINEAR` | Linear scale.  
`LOG10` | Logarithmic scale (base 10).  
  
## DataSet

Groups a time series query definition with charting options.

Fields  
---  
`time_series_query` |  `[TimeSeriesQuery](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.TimeSeriesQuery)` Required. Fields for querying time series data from the Stackdriver metrics API.  
`plot_type` |  `[PlotType](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.DataSet.PlotType)` How this data should be plotted on the chart.  
`legend_template` |  `string` A template string for naming `TimeSeries` in the resulting data set. This should be a string with interpolations of the form `${label_name}`, which will resolve to the label's value.  
`min_alignment_period` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. The lower bound on data point frequency for this data set, implemented by specifying the minimum alignment period to use in a time series query. For example, if the data is published once every 10 minutes, the `min_alignment_period` should be at least 10 minutes. It would not make sense to fetch and align data at one minute intervals.For PromQL queries, this field is used to set the minimum interval for the query `step`, controlling data granularity. Larger values can improve performance on long time ranges. See [Querying Basics](https://prometheus.io/docs/prometheus/latest/querying/basics/) and [Range Queries](https://prometheus.io/docs/prometheus/latest/querying/api/#range-queries) for more details on the PromQL `step`.  
`target_axis` |  `[TargetAxis](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.XyChart.DataSet.TargetAxis)` Optional. The target axis to use for plotting the metric.  
`dimensions[]` |  `[Dimension](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Dimension)` Optional. A collection of dimension columns.  
`measures[]` |  `[Measure](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Measure)` Optional. A collection of measures.  
`breakdowns[]` |  `[Breakdown](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.Breakdown)` Optional. The collection of breakdowns to be applied to the dataset.  
`sort[]` |  `[ColumnSortingOptions](https://docs.cloud.google.com/monitoring/api/ref_v3/rpc/google.monitoring.dashboard.v1#google.monitoring.dashboard.v1.ColumnSortingOptions)` Optional. A collection of sort options, affects the order of the data and legend.  
  
## PlotType

The types of plotting strategies for data sets.

Enums  
---  
`PLOT_TYPE_UNSPECIFIED` | Plot type is unspecified. The view will default to `LINE`.  
`LINE` | The data is plotted as a set of lines (one line per series).  
`STACKED_AREA` | The data is plotted as a set of filled areas (one area per series), with the areas stacked vertically (the base of each area is the top of its predecessor, and the base of the first area is the x-axis). Since the areas do not overlap, each is filled with a different opaque color.  
`STACKED_BAR` | The data is plotted as a set of rectangular boxes (one box per series), with the boxes stacked vertically (the base of each box is the top of its predecessor, and the base of the first box is the x-axis). Since the boxes do not overlap, each is filled with a different opaque color.  
`HEATMAP` | The data is plotted as a heatmap. The series being plotted must have a `DISTRIBUTION` value type. The value of each bucket in the distribution is displayed as a color. This type is not currently available in the Stackdriver Monitoring application.  
  
## TargetAxis

An axis identifier.

Enums  
---  
`TARGET_AXIS_UNSPECIFIED` | The target axis was not specified. Defaults to Y1.  
`Y1` | The y_axis (the right axis of chart).  
`Y2` | The y2_axis (the left axis of chart).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
